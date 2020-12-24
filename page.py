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
import utils

##########################################################
##########################################################       
# Libraries

# Colors (dictionary of RGB)
class obj_colors:
    def __init__(self):
        # base colors
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(220,0,0)# bit darker
        self.blue=(0,0,220)
        self.green=(0,220,0)
        self.gray=(150,150,150)
        self.brown=(165,42,42)
        self.maroon=(128,0,0)
        #
        # Colors devmode
        self.devtextbox=(233,222,100)# yellow
        self.devimage=(250,150,0)# orange
        self.devanimation=(0,220,0)# green
        self.devdispgroup=(128,0,128)# purple
        self.devactor=(0,0,220)# blue (hitbox)
        #
        # Colors game elements
        self.colorkey=self.white# transparent color (all sprites except background)
        self.background=self.white# game background
        self.drawing=(220,0,0)# drawing
        self.input=self.red# text input (in text)
        self.textinput=(200,0,0)# text input (box)
        self.textchoice=(180,0,0)# text input box        
        # Colors for story
        self.book=self.blue# anything book of thing
        self.hero=self.red# hero text color
        self.weapon=self.brown# hero weapon text color
        self.itemloved=(220,50,50)
        self.itemhated=self.maroon
        self.house=self.red# hero house


# Fonts
# $ a=share.fonts.font50# direct access
# $ a=share.fonts.font('medium')# by keyword
class obj_fonts:
    def __init__(self):
         self.font15=utils.obj_font('data/AmaticSC-Bold.ttf', 15)# tiny (for FPS) 
         self.font30=utils.obj_font('data/AmaticSC-Bold.ttf', 30)# small indicators,textbox
         self.font40=utils.obj_font('data/AmaticSC-Bold.ttf', 40)# small indicators,textbox
         self.font50=utils.obj_font('data/AmaticSC-Bold.ttf', 50)# medium (for story text)
         self.font60=utils.obj_font('data/AmaticSC-Bold.ttf', 60)# large
         self.font100=utils.obj_font('data/AmaticSC-Bold.ttf', 100)# big (for titlescreen)
         self.font120=utils.obj_font('data/AmaticSC-Bold.ttf', 120)# huge
    def font(self,fontname):# call by key(string)
         if fontname=='tiny' or fontname==15:
             return self.font15.font
         elif fontname=='smaller' or fontname==30:
             return self.font30.font
         elif fontname=='small' or fontname==40:
             return self.font40.font
         elif fontname=='medium' or fontname==50:
             return self.font50.font
         elif fontname=='large' or fontname==60:
             return self.font60.font
         elif fontname=='big' or fontname==100:
             return self.font100.font
         elif fontname=='huge' or fontname==120:
             return self.font120.font
         else:
             return self.font50.font# medium font  


# Brushes used for drawing
class obj_brushes:
    def __init__(self):        
        self.pen=('data/pen.png',(8,8))
        self.smallpen=('data/pen.png',(4,4))
        self.tinypen=('data/pen.png',(2,2))

    
    
####################################################################################################################

# Template for any game scene
class obj_pagetemplate: # rename to obj_page later
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.presetup()# 
        self.setup()
        self.postsetup()
    def presetup(self):
        # background sprite
        self.background=utils.obj_sprite_background()
        self.background.setcolor(share.colors.background)  
        # elements
        self.to_update=[]
        self.to_finish=[]
    def setup(self):# page setup
        pass
    def postsetup(self):
        pass
    def addpart(self,element):
        if element.type in ['drawing','textinput','textchoice','textbox','image','animation','dispgroup','world']:
            self.to_update.append(element)            
        if element.type in ['drawing','textinput','textchoice']:
            self.to_finish.append(element)        
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i: i.remove(element)
    def update(self,controls):
        self.prepage(controls)# background and elements
        self.page(controls)# 
        self.postpage(controls)# foreground
    def prepage(self,controls):
        self.background.display()
        for i in self.to_update: i.update(controls)
    def page(self,controls):
        pass
    def postpage(self,controls):
        share.fpsdisplay()
    def preendpage(self):# before exiting page
        for i in self.to_finish: i.finish()     



# chapter page template: a page in a chapter of the book
class obj_page(obj_pagetemplate):  ### rename to obj_chapterpage later
    def __init__(self,creator):
        super().__init__(creator)
    def presetup(self):
        super().presetup()
        # Main body of text
        self.text=[]
        self.textkeys={}
    def postsetup(self):
        super().postsetup()
        share.textdisplay(self.text,rebuild=True,**self.textkeys)# rebuild text to display
        share.pagenumberdisplay(rebuild=True)
        share.pagenotedisplay('[Tab: Back]  [Enter: Continue]',rebuild=True)
    def prepage(self,controls):
        super().prepage(controls)
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
    def page(self,controls):# page update
        pass
    def postpage(self,controls):
        super().postpage(controls)
        share.textdisplay(self.text)
        share.pagenumberdisplay()
        share.pagenotedisplay('')
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
# Page utilities


# Page Number display
class obj_pagenumberdisplay:
    def __init__(self):
        self.prerender=[]# prerender text
        self.xy=(0,0)# position of text
    def __call__(self,rebuild=False,fontsize='smaller',xy=(1190,680),bold=True,color=(0,0,0)):
        if rebuild:
            self.prerender=share.fonts.font(fontsize).render('Page '+str(share.ipage), bold, color)
            self.xy=xy
        else:
            share.screen.drawsurf(self.prerender,self.xy)# fast display


# Page Note display (e.g. instructions)
class obj_pagenotedisplay:
    def __init__(self):
        self.prerender=[]# prerender text
        self.xy=(0,0)# position of text
    def __call__(self,text,xy=(1020,5),rebuild=False,fontsize='smaller',bold=True,color=(0,0,0)):
        if rebuild:
            self.prerender=share.fonts.font(fontsize).render(text,bold,color)
            self.xy=xy
        else:
            share.screen.drawsurf(self.prerender,self.xy)# fast display        

        
# FPS display (could be a function)
class obj_fpsdisplay: 
    def __init__(self):
        pass
    def __call__(self):
        share.screen.drawsurf(share.fonts.font('smaller').render('FPS='+str(int(share.clock.getfps())), True, (0, 0, 0)), (30,5))
        
        
# Main body of text on a story page
class obj_textdisplay:
    def __init__(self):
        self.words_prerender=[]# list of word_surface and positions (pre-redendered)
    def __call__(self,textmatrix,rebuild=False, pos=(50,50),xmin=50,xmax=1230, linespacing=55,fontsize='medium'):# call text display
        # pos: starting xy of text, xmin/xmax: margins
        # rebuild=True: renders the text entirely (expensive, use for first call with new text)
        # rebuild=False: displays previous text surface (prefer for efficiency, skips font render)
        if rebuild: # expensive rebuild
            self.words_prerender=[]# reset prerender text
            if textmatrix: # if not empty text
                self.ipos=pos# text cursor position
                for i in textmatrix:
                    if type(i) is str:# either text=string
                        text, color = i, (0,0,0)
                    else:
                        text, color = i# or tuple (text,color)
                    text=self.formattext(text,**share.words.dict)# FORMAT with written words from book 
                    self.ipos=self.rebuildtext(text,self.ipos,share.fonts.font(fontsize),xmin,xmax,linespacing,color=color)
        else:
            self.disptext()
    # Format text using the words written in the book of things
    def formattext(self,text,**kwargs):
        try:
            text=text.format(**kwargs)
        except:
            pass
        return text
    # Display text on surface with automatic return to line
    def rebuildtext(self,text,pos,font,xmin,xmax,linespacing,color=(0,0,0)):
        wordmatrix=[row.split(' ') for row in text.splitlines()]# 2D array of words
        space_width=font.size(' ')[0]# width of a space
        x,y=pos# text position
        if x<xmin: x==xmin
        for count,line in enumerate(wordmatrix):
            for word in line:
                word_surface=font.render(word,True,color)# Very expensive if redone each frame!
                word_width, word_height = word_surface.get_size()
                # return to line automated
                if x + word_width >= xmax:
                    x = xmin
                    y += linespacing
                # record prerendered text
                self.words_prerender.append( (word_surface,(x,y)) )# record prerendered text
                x += word_width + space_width
            # return to line from user
            if count<len(wordmatrix)-1:
                x = xmin
                y += linespacing        
        return x,y# return position for next call  
    def disptext(self):# display prerendered text
        for i in self.words_prerender:
            word_surface, xy=i
            share.screen.drawsurf(word_surface, xy)


####################################################################################################################

