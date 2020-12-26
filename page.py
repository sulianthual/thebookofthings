#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# pages.py: game objects that make up a page in the book
#
##########################################################
##########################################################

import share
import draw
import core
import tool

##########################################################
##########################################################       

# Scene Manager: switches between scenes (called pages in the book of things)
class obj_scenemanager:
    def __init__(self):
        self.scene=None# current scene being played (must initialize object externally)
    def update(self,controls):
        self.scene.update(controls)# Update current scene
        if controls.quit: share.quitgame()# Quit game (close window)
        if controls.lctrl and controls.lctrlc: share.devmode = not share.devmode# toggle dev mode
        if share.devmode and controls.mouse3 and controls.mouse3c:
            print( '('+str(controls.mousex)+','+str(controls.mousey)+')')


####################################################################################################################    

# Template for any game scene (called a page in the book of things)
class obj_page: 
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.presetup()# 
        self.setup()
        self.postsetup()
    def presetup(self):# background
        # background sprite
        self.background=core.obj_sprite_background()
        self.background.setcolor(share.colors.background)  
        # elements
        self.to_update=[]
        self.to_finish=[]
    def setup(self):# page setup
        pass
    def postsetup(self):# foreground
        self.pagedisplay_fps=obj_pagedisplay_fps()
    def addpart(self,element):
        if element.type in ['drawing','textinput','textchoice','textbox','image','animation','dispgroup','world']:
            self.to_update.append(element)            
        if element.type in ['drawing','textinput','textchoice']:
            self.to_finish.append(element)        
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i: i.remove(element)
    def update(self,controls):
        self.prepage(controls)
        self.page(controls) 
        self.postpage(controls)
    def prepage(self,controls):# background
        self.background.display()
        for i in self.to_update: i.update(controls)
    def page(self,controls):
        pass
    def postpage(self,controls):# foreground
        self.pagedisplay_fps.update()
    def preendpage(self):# before exiting page
        for i in self.to_finish: i.finish()     



# chapter page template: a page in a chapter of the book
class obj_chapterpage(obj_page):  
    def __init__(self,creator):
        super().__init__(creator)
    ###
    def presetup(self):
        super().presetup() 
        self.text=[]# Main body of text
        self.textkeys={}
    def setup(self):
        super().setup()
    def postsetup(self):
        super().postsetup()
        self.pagenumber=obj_pagedisplay_number()
        self.pagenote=obj_pagedisplay_note()
        self.pagenote.make('[Tab: Back]  [Enter: Continue]')
        self.pagetext=obj_pagedisplay_text()
        self.pagetext.make(self.text,**self.textkeys)# rebuild main text
    ###
    def prepage(self,controls):# background
        super().prepage(controls)
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
    def page(self,controls):
        super().page(controls)
    def postpage(self,controls):# foreground
        super().postpage(controls)
        self.pagenumber.display()
        self.pagenote.display()
        self.pagetext.display()
    ###
    def callprevpage(self,controls):
        if controls.tab and controls.tabc:
            self.preendpage()# template
            self.endpage()# customized
            share.ipage -= 1
            self.prevpage()# switch to prev page
    def callnextpage(self,controls):
        if controls.enter and controls.enterc: 
            self.preendpage()# template
            self.endpage()# customized
            share.ipage += 1
            self.nextpage()# switch to next page
    def callexitpage(self,controls):
        if controls.esc and controls.esc: # go back to main menu
            self.preendpage()# template
            self.endpage()# customized
            share.titlescreen.setup()
            self.creator.scene=share.titlescreen
            # self.creator.scene=menu.obj_scene_titlescreen(share.scenemanager)
    ###
    def endpage(self):# when exit page 
        pass
    def prevpage(self):# actions to prev page (replace here)**
        share.titlescreen.setup()# refresh titlescreen content
        self.creator.scene=share.titlescreen# default back to menu
        # self.creator.scene=menu.obj_scene_titlescreen(share.scenemanager)
    def nextpage(self):# actions to next page (replace here)**
        share.titlescreen.setup()# refresh titlescreen content
        self.creator.scene=share.titlescreen# default back to menu
        # self.creator.scene=menu.obj_scene_titlescreen(share.scenemanager)
    
    
####################################################################################################################
# page display: game UI elements on a book page (usually in the foreground)

# display fps
class obj_pagedisplay_fps: 
    def __init__(self):
        self.sprite=core.obj_sprite_text()
        self.make()
    def make(self):
        text='FPS='+str(int(share.clock.getfps()))
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))
    def display(self):
        self.sprite.display(50,20)
    def update(self):
        self.make()# rebuild sprite every update
        self.display()

 
# display page number        
class obj_pagedisplay_number:
    def __init__(self):
        self.sprite=core.obj_sprite_text()
        self.make()
    def make(self):
        text='Page '+str(share.ipage)
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))    
    def display(self):
        self.sprite.display(1190,680)
    def update(self):
        self.display()

# display recurrent page note        
class obj_pagedisplay_note:
    def __init__(self):
        self.sprite=core.obj_sprite_text()
    def make(self,text):
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))
    def display(self):
        self.sprite.display(1140,30)
    def update(self):
        self.display()


# Main body of text on a story page
class obj_pagedisplay_text:
    def __init__(self):
        self.words_prerender=[]# list of words (sprites and positions)        
    def make(self,textmatrix,pos=(50,50),xmin=50,xmax=1230, linespacing=55,fontsize='medium'):
        self.words_prerender=[]       
        if textmatrix: 
            self.ipos=pos# text cursor position
            for i in textmatrix:
                if type(i) is str:
                    text, color = i, (0,0,0)# input: text
                else:
                    text, color = i# input: (text,color)
                text=self.formattext(text,**share.words.dict)
                self.ipos=self.rebuildtext(text,self.ipos,share.fonts.font(fontsize),xmin,xmax,linespacing,color=color)    
    def formattext(self,text,**kwargs):# Format text using the keywords written in the book of things (words.txt)
        try:
            text=text.format(**kwargs)
        except:
            pass
        return text    
    def rebuildtext(self,text,pos,font,xmin,xmax,linespacing,color=(0,0,0)):
        wordmatrix=[row.split(' ') for row in text.splitlines()]# 2D array of words
        space_width=font.size(' ')[0]# width of a space
        x,y=pos# text position (top left corner)
        if x<xmin: x==xmin
        for count,line in enumerate(wordmatrix):
            for word in line:                
                word_surface=core.obj_sprite_text()# New sprite_text object for each word
                word_surface.make(word,font,color)
                word_width, word_height = 2*word_surface.getrx(),2*word_surface.getry()
                if x + word_width >= xmax:
                    x = xmin
                    y += linespacing
                self.words_prerender.append( (word_surface,(x+word_width/2,y+word_height/2)) )# record prerendered text
                x += word_width + space_width
            # return to line from user
            if count<len(wordmatrix)-1:
                x = xmin
                y += linespacing        
        return x,y# return position for next call  
    def display(self):
        for i in self.words_prerender:
            word_surface, xy=i
            word_surface.display(xy[0],xy[1])
    def update(self):
        self.display()


####################################################################################################################

