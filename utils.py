#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# utils.py: utility tools and external libraries
#
# Any call to external libraries (math,os,sys) must be linked here.
#
# Why?
# - If we want to change the external libraries it is much easier
#
##########################################################
##########################################################

import sys
import os
from math import cos as linkcos
from math import sin as linksin
from math import atan2 as linkatan2
import pygame
#
import share

####################################################################################################################
# Game Core


# Display Manager
class obj_display:
    def __init__(self):
        self.setup()# initial setup (can be repeated on settings changes)
        #    
    def setup(self):
        share.screen=pygame.display.set_mode((1280,720))
        share.screen.set_alpha(None) # Remove alpha=transparency (for increased performances)
        pygame.display.set_caption("The Book of Things")# window banner
        pygame.mouse.set_visible(True)# show mouse
        #
    def seticon(self,image):# set window icon
        pygame.display.set_icon(image)
    def reset(self):# reset display with new values 
        pygame.display.quit()
        self.setup()
        #
    def update(self):
        pygame.display.update()# (could also update only rects, less costly but need to keep track)

        
# Scene Manager
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
        

# Quit Game Procedure
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


# Game Clock (delays game update to given fps)
class obj_clock:
    def __init__(self):
        self.clock=pygame.time.Clock()
        self.targetfps=share.fps
    def getfps(self):
        return self.clock.get_fps()
    def update(self):
        self.clock.tick(self.targetfps)

        
        
####################################################################################################################


# Game Window icon
class obj_windowicon:
    def __init__(self):
        self.reset()
    def reset(self):
        self.makeicon()
        self.seticon()
    def makeicon(self):# make window icon from a player drawing
        if os.path.exists('book/book.png'):
            img=pygame.image.load('book/book.png').convert()
            img=pygame.transform.scale(img,(36,42))
            pygame.image.save(img, 'book/bookicon.png')
    def seticon(self):          
        if os.path.exists('book/bookicon.png'):
            img=pygame.image.load('book/bookicon.png').convert()
        else:
            img=pygame.image.load('data/booknoicon.png').convert()
        img.set_colorkey((255,255,255))# white
        share.display.seticon(img)#pygame.display.set_icon(img)
        
        
# Handle data (save.txt and drawings)
class obj_savefile:
    def __init__(self):
        self.filename='book/save.txt'# saved along with drawings
        self.chapter=0# current chapter
        self.load()
    def load(self):# load savefile (or set default parameters if doesnt exist)
        if os.path.exists('book/save.txt'): 
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
        files = os.listdir('book')
        for i in files: os.remove('book/'+i)
        self.load()# reload


# Dictionary of textinputs,textchoices written in the book of things (by the player)
class obj_savewords:
    def __init__(self):# most entries are created during the game
        self.filename='book/words.txt'# save file for all keywords
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
# General Functions and objects for all uses

# links to module os
def pathexists(path):
    return os.path.exists(path)

# links to module math
def cos(x):
    return linkcos(x)
def sin(x):
    return linksin(x)
def atan2(y,x):
    return linkatan2(y,x)
def angle(a_xy,b_xy):# angle between points a=(x,y) and b=(x,y)
    return linkatan2(b_xy[1]-a_xy[1],b_xy[0]-a_xy[0])
def actorsangle(a,b):# angle between actors a,b (with attributes a.x,a.y)
    return linkatan2(b.y-a.y,b.x-a.x)

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

    
# Cross display       
def crossdisplay(xy,radius,color,thickness,diagonal=False):
        if not diagonal:        
            pygame.draw.line(share.screen,color,(xy[0]-radius,xy[1]),(xy[0]+radius,xy[1]),thickness)
            pygame.draw.line(share.screen,color,(xy[0],xy[1]-radius),(xy[0],xy[1]+radius),thickness)
        else:
            pygame.draw.line(share.screen,color,(xy[0]-radius,xy[1]-radius),(xy[0]+radius,xy[1]+radius),thickness)
            pygame.draw.line(share.screen,color,(xy[0]+radius,xy[1]-radius),(xy[0]-radius,xy[1]+radius),thickness) 
            

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



