#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# utils.py: General Tools (Display, GUI, general functions)
#
##########################################################
##########################################################

import sys
import os
import pygame
#
import share

####################################################################################################################
# Display Manager
#*DISPLAY
# Manages display
class obj_display:
    def __init__(self):
        self.setup()# initial setup (can be repeated on settings changes)
        #    
    def setup(self):
        # Create Game Screen (drawn on constantly)
        share.screen.set_alpha(None) # Remove alpha (for increased performances ?)
        pygame.display.set_caption("The Book of Things")# text on window banner
        if os.path.exists('drawings/bookicon.png'):# this is created by the player
            pygame.display.set_icon(pygame.image.load('drawings/bookicon.png').convert_alpha())# icon on window banner 
        else:
            pygame.display.set_icon(pygame.image.load('data/booknoicon.png').convert_alpha())# before exists
        pygame.mouse.set_visible(True)# Show Mouse (needed to draw)
        #
    def reset(self):# reset display with new values 
        pygame.display.quit()
        self.setup()
        #
    def update(self):
        # Update display
        pygame.display.update()# (could also update only rects, less costly but need to keep track)

####################################################################################################################               
# Scene Manager
# *SCENE 
# Creates/Deletes and switches between levels
class obj_scenemanager:
    def __init__(self):
        self.scene=[]# current scene being played (must initialize object externally)
        self.page=0# current story page
    def update(self,controls):
        self.scene.update(controls)# Update current scene
        share.fpsdisplay()# display fps on top 
        if controls.quit: share.quitgame()# Quit game (close window)
        if controls.lctrl and controls.lctrlc: share.devmode = not share.devmode# toggle dev mode
        #
        # dev tests:
        if share.devmode and controls.mouse3 and controls.mouse3c: 
            print( '('+str(controls.mousex)+','+str(controls.mousey)+')')
        
####################################################################################################################
# Function Quit Game
#*QUIT
class obj_quit:
     def __init__(self):
         pass
     def __call__(self):
         #savefile.save()# save current game state
         pygame.display.quit()
         pygame.mixer.music.stop()
         pygame.mixer.quit()
         pygame.quit()
         sys.exit()# very important to properly quit game without crashing

####################################################################################################################
# General Page class (base functions repeated for each page within a chapter)
# *PAGE            


class obj_page:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.presetup()# template
        self.setup()# customized
        self.postsetup()# template
    def presetup(self):
        self.text=[]# displayed text 
        self.textkeys={}# can add keys in setup (e.g. self.textkeys['xmin']=150)
        self.to_update=[]# list of elements to update during page (includes everyone)
        self.to_finish=[]# list of elements to finish on endpage (drawing, textinput)
    def postsetup(self):
        share.textdisplay(self.text,rebuild=True,**self.textkeys)# rebuild text to display
        share.pagenumberdisplay(rebuild=True)# rebuild page display
    def addpart(self,element):# add element (must have a self.type)
        if element.type in ['drawing','textinput','textbox','image','animation','dispgroup','world']:
            self.to_update.append(element)            
        if element.type in ['drawing','textinput']:
            self.to_finish.append(element)
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i: i.remove(element)
    def update(self,controls):
        self.prepage(controls)# template
        self.page(controls)# customized
        self.postpage(controls)# template
    def prepage(self,controls):
        share.screen.fill((255,255,255))
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
        for i in self.to_update: i.update(controls)# update elements
    def postpage(self,controls):
        share.textdisplay(self.text)# display text
        share.pagenumberdisplay()# display page number
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
    def preendpage(self):
        for i in self.to_finish: i.finish()# finish elements
    # This content to be edited for each page
    def setup(self):# page setup
        pass
    def page(self,controls):# page update
        pass
    def endpage(self):# when exit page 
        pass
    def prevpage(self):# actions to prev page (replace here)**
        share.titlescreen.setup()# refresh titlescreen content
        self.creator.scene=share.titlescreen# default back to menu
    def nextpage(self):# actions to next page (replace here)**
        share.titlescreen.setup()# refresh titlescreen content
        self.creator.scene=share.titlescreen# default back to menu

         
####################################################################################################################
# Save Data into Files (also manages all drawings in folder /drawings)
# *SAVE
class obj_savefile:
    def __init__(self):
        self.filename='drawings/save.txt'# saved along with drawings
        self.chapter=0# current chapter
        self.load()
    def load(self):# load savefile (or set default parameters if doesnt exist)
        if os.path.exists('drawings/save.txt'): 
            f1=open(self.filename,'r+')
            line=f1.readline()# chapter
            line=line.split(",")
            self.chapter=int(line[1])
            f1.close()
        else:
            self.chapter=0
    def save(self):
        f1=open(self.filename,'w+')
        f1.write('chapter,'+str(self.chapter)+'\n')# first line
        f1.close()
    def eraseall(self):# erase all progress + drawings
        files = os.listdir('drawings')
        for i in files: os.remove('drawings/'+i)
        self.load()# reload

# Dictionary of keywords written in the book of things (by the player)
class obj_savewords:
    def __init__(self):# most entries are created during the game
        self.filename='drawings/words.txt'# save file for all keywords
        self.dict={}
        self.load()# load savefile
    def save(self):# save keywords to file
        with open(self.filename,'w') as f1:
            for i in self.dict.items():# iterate over tuples =(key,value)
                f1.write(str(i[0])+'\n')#key
                f1.write(str(i[1])+'\n')#value
    def load(self):# load keywords from file
        if os.path.exists(self.filename): 
            with open(self.filename,'r') as f1:
                matrix=f1.read().splitlines()
                for i in range(int(len(matrix)/2)):# read alternated key,value on lines
                    self.dict[matrix[i*2]]=matrix[i*2+1]                
    def eraseall(self):
        self.dict={}
        self.save()# write empty dictionary
         
####################################################################################################################
# Methods for GUIs
# *GUI

# Window icon
class obj_windowicon:
    def __init__(self):
        self.reset()
    def reset(self):
        self.makeicon()
        self.seticon()
    def makeicon(self):
        if os.path.exists('drawings/book.png'):# this is created by the player
            self.imgicon=pygame.image.load('drawings/book.png')
            self.imgicon=pygame.transform.scale(self.imgicon,(36,42))
            pygame.image.save(self.imgicon, 'drawings/bookicon.png')
    def seticon(self):
        if os.path.exists('drawings/bookicon.png'):# this is created by the player
            pygame.display.set_icon(pygame.image.load('drawings/bookicon.png').convert_alpha())# icon on window banner 
        else:
            pygame.display.set_icon(pygame.image.load('data/booknoicon.png').convert_alpha())# default            
           
# Game text display 
# *TEXT DISPLAY
class obj_textdisplay:
    def __init__(self):
        self.words_prerender=[]# list of word_surface and positions (pre-redendered)
    def __call__(self,textmatrix,rebuild=False, pos=(50,30),xmin=50,xmax=1230, linespacing=55,fontsize='medium'):# call text display
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
        text=text.format(**kwargs)
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
                # share.screen.blit(word_surface, (x,y))# old, display text on screen
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
            share.screen.blit(word_surface, xy)
        
# Page Number display
class obj_pagenumberdisplay:
    def __init__(self):
        self.prerender=[]# prerender text
    def __call__(self,rebuild=False):
        if rebuild:
            self.prerender=share.fonts.font30.render('Page '+str(share.ipage), True, (0, 0, 0))
        else:
            share.screen.blit(self.prerender, (1190,5))# fast display
        
# FPS display
class obj_fpsdisplay:
    def __init__(self):
        pass
    def __call__(self):
        # annoying to prerender (must have all possible values): so no prerender for fps
        share.screen.blit(share.fonts.font15.render('FPS='+str(int(share.clock.get_fps())), True, (0, 0, 0)), (30,5))# show fps 

# Cross display
class obj_crossdisplay:
    def __init__(self):
        pass
    def __call__(self,xy,radius,color,thickness,diagonal=False):
        if not diagonal:        
            pygame.draw.line(share.screen,color,(xy[0]-radius,xy[1]),(xy[0]+radius,xy[1]),thickness)
            pygame.draw.line(share.screen,color,(xy[0],xy[1]-radius),(xy[0],xy[1]+radius),thickness)
        else:
            pygame.draw.line(share.screen,color,(xy[0]-radius,xy[1]-radius),(xy[0]+radius,xy[1]+radius),thickness)
            pygame.draw.line(share.screen,color,(xy[0]+radius,xy[1]-radius),(xy[0]-radius,xy[1]+radius),thickness)            
        
####################################################################################################################
# General Functions and objects for All Uses
# *FUNCTIONS

# check if a point x,y is in a given rectangle rect=(xmin,xmax,ymin,ymax)
def isinrect(x,y,rect):
    (xmin,xmax,ymin,ymax)=rect# not a pygame rectangle definition
    if x>xmin and x<xmax and y>ymin and y<ymax:
        return True
    else:
        return False

# check if two actors a,b (with attributes x,y) are colliding (within given distance r)
def checkdotscollide(a,b,r):
    return (a.x-b.x)**2+(a.y-b.y)**2<r**2

# check if two actors a,b (with attributes x,y,rd) are colliding 
def checkcirclecollide(a,b):
    return (a.x-b.x)**2+(a.y-b.y)**2<(a.rd+b.rd)**2

# check if two actors a,b (with attributes x,y,rx,ry) are colliding 
def checkrectcollide(a,b):
    return abs(a.x-b.x)<a.rx+b.rx and abs(a.y-b.y)<a.ry+b.ry
    
# Timer for any purpose
# *TIMER
class obj_timer:
    def __init__(self,amount,cycle=False):
        self.amount=amount# integer, amount of time from timer
        # 3 states for the timer: on, ring, off
        self.on=False
        self.ring=False# timer rings (happens once when countdown finishes)
        self.off=True# timer done or not, check it here
        self.t=0# time count
        self.cycle=cycle# optional, timer cycles (restarts automatically when done)
    def start(self):# start (or restart) timer
        self.on=True
        self.ring=False
        self.off=False
        self.t=int(self.amount)
    def run(self):# run timer (without restarting)
        if not self.on: self.start()
    def update(self):# update timer 
        if self.on:
            self.t -= 1
            if self.t <0:
                self.ring=True
                self.on=False
        elif self.ring:
            self.ring=False
            self.off=True
            if self.cycle: self.start()# restart if cycled
                
                

        
        
####################################################################################################################

# Controls 
# *CONTROLS
# Manages Input controls
class obj_controls:
    def __init__(self):
        # special
        self.events=pygame.event.get()
        self.quit=False       
        # mouse
        self.mousex=0
        self.mousey=0
        self.mouse1=False# pressed or not
        self.mouse2=False
        self.mouse3=False
        self.mouse4=False
        self.mouse5=False
        # keys
        self.esc=False
        self.enter=False
        self.backspace=False
        self.tab=False
        self.space=False
        self.lctrl=False
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.a=False
        self.d=False
        self.w=False
        self.s=False
        self.q=False
        self.e=False
        self.r=False
        self.f=False
        # booleans to detect if change on frame
        self.mouse1c=False# changed or not
        self.mouse2c=False        
        self.mouse3c=False
        self.mouse4c=False
        self.mouse5c=False
        # keys
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.lctrlc=False
        self.leftc=False
        self.rightc=False
        self.upc=False
        self.downc=False
        self.ac=False
        self.dc=False
        self.wc=False
        self.sc=False        
        self.qc=False
        self.ec=False
        self.rc=False
        self.fc=False 
    def edittext(self,text):# edit existing text with keyboard inputs
        for event in self.events:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:# Pressed once
                    text = ''#remove all#text[:-1]# remove character
                elif event.key == pygame.K_RETURN:# Enter (nothing happens)
                    pass
                elif event.key==pygame.K_ESCAPE:# Esc (nothing happens)
                    pass
                elif event.key==pygame.K_TAB:# Tab (nothing happens)
                    pass
                else:
                    text += event.unicode# record text
        return text
    def getevents(self):
        self.events=pygame.event.get()           
    def getmouse(self):        
        self.mouse1c=False# left click
        self.mouse2c=False# right click
        self.mouse3c=False# middle click
        self.mouse4c=False#middle up
        self.mouse5c=False# middle down
        (self.mousex,self.mousey)=pygame.mouse.get_pos()
        self.mousex=int(self.mousex)# very important if screen is stretched
        self.mousey=int(self.mousey)
        for event in self.events:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1: 
                    self.mouse1, self.mouse1c = True, True 
                elif event.button==3: 
                    self.mouse2, self.mouse2c = True, True                  
                elif event.button==2: 
                    self.mouse3, self.mouse3c = True, True 
                elif event.button==4: 
                    self.mouse4, self.mouse4c = True, True 
                elif event.button==5: 
                    self.mouse5, self.mouse5c = True, True 
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==1: 
                    self.mouse1, self.mouse1c = False, True 
                elif event.button==3: 
                    self.mouse2, self.mouse2c = False, True                  
                elif event.button==2: 
                    self.mouse3, self.mouse3c = False, True 
                elif event.button==4: 
                    self.mouse4, self.mouse4c = False, True 
                elif event.button==5: 
                    self.mouse5, self.mouse5c = False, True   
    def getkeys(self):        
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.lctrlc=False
        self.leftc=False
        self.rightc=False
        self.upc=False
        self.downc=False
        self.ac=False
        self.dc=False
        self.wc=False
        self.sc=False   
        self.qc=False
        self.ec=False
        self.rc=False
        self.fc=False
        for event in self.events:
            if event.type==pygame.KEYDOWN:                 
                if event.key==pygame.K_ESCAPE: 
                    self.esc, self.escc = True, True
                elif event.key==pygame.K_RETURN: 
                    self.enter, self.enterc = True, True
                elif event.key==pygame.K_BACKSPACE: 
                    self.backspace, self.backspacec = True, True
                elif event.key==pygame.K_TAB: 
                    self.tab, self.tabc = True, True
                elif event.key==pygame.K_SPACE: 
                    self.space, self.spacec = True, True
                elif event.key==pygame.K_LCTRL: 
                    self.lctrl, self.lctrlc = True, True
                elif event.key==pygame.K_LEFT: 
                    self.left, self.leftc = True, True
                elif event.key==pygame.K_RIGHT: 
                    self.right, self.rightc = True, True
                elif event.key==pygame.K_UP: 
                    self.up, self.upc = True, True
                elif event.key==pygame.K_DOWN: 
                    self.down, self.downc = True, True
                elif event.key==pygame.K_d: 
                    self.d, self.dc = True, True
                elif event.key==pygame.K_s: 
                    self.s, self.sc = True, True
                elif event.key==pygame.K_a: 
                    self.a, self.ac = True, True
                elif event.key==pygame.K_w: 
                    self.w, self.wc = True, True
                elif event.key==pygame.K_q: 
                    self.q, self.qc = True, True
                elif event.key==pygame.K_e: 
                    self.e, self.ec = True, True
                elif event.key==pygame.K_r: 
                    self.r, self.rc = True, True
                elif event.key==pygame.K_f: 
                    self.f, self.fc = True, True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE: 
                    self.esc, self.escc = False, True
                elif event.key==pygame.K_RETURN: 
                    self.enter, self.enterc = False, True
                elif event.key==pygame.K_BACKSPACE: 
                    self.backspace, self.backspacec = False, True
                elif event.key==pygame.K_TAB: 
                    self.tab, self.tabc = False, True
                elif event.key==pygame.K_SPACE: 
                    self.space, self.spacec = False, True
                elif event.key==pygame.K_LCTRL: 
                    self.lctrl, self.lctrlc = False, True
                elif event.key==pygame.K_LEFT: 
                    self.left, self.leftc = False, True
                elif event.key==pygame.K_RIGHT: 
                    self.right, self.rightc = False, True
                elif event.key==pygame.K_UP: 
                    self.up, self.upc = False, True
                elif event.key==pygame.K_DOWN: 
                    self.down, self.downc = False, True
                elif event.key==pygame.K_d: 
                    self.d, self.dc = False, True
                elif event.key==pygame.K_s: 
                    self.s, self.sc = False, True
                elif event.key==pygame.K_a: 
                    self.a, self.ac = False, True
                elif event.key==pygame.K_w: 
                    self.w, self.wc = False, True
                elif event.key==pygame.K_q: 
                    self.q, self.qc = False, True
                elif event.key==pygame.K_e: 
                    self.e, self.ec = False, True
                elif event.key==pygame.K_r: 
                    self.r, self.rc = False, True
                elif event.key==pygame.K_f: 
                    self.f, self.fc = False, True
                        
    def getquit(self):
        for event in self.events:
            if event.type==pygame.QUIT:
                self.quit=True          
    def update(self):
        self.getevents()# Important: only get events once per frame!
        self.getmouse()
        self.getkeys()
        self.getquit()

####################################################################################################################



