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
from math import cos as math_cos
from math import sin as math_sin
from math import atan2 as math_atan2
#
import share
import pyg

####################################################################################################################
# Game Core


# Display Manager
class obj_display:
    def __init__(self):
        self.setup()# initial setup (can be repeated on settings changes)
        #    
    def setup(self):
        share.screen=pyg.newdisplay(1280,720)
        share.screen.set_alpha(None) # Remove alpha=transparency (for increased performances)
        pyg.display_set_caption("The Book of Things")# window banner
        pyg.mouse_set_visible(True)# show mouse
    def seticon(self,image):# set window icon
        pyg.display_set_icon(image)
    def reset(self):# reset display with new values 
        pyg.display_quit()
        self.setup()
        #
    def update(self):
        pyg.display_update()# (could also update only rects, less costly but need to keep track)

        
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
         pyg.shutdown()
         sys.exit()


# Game Clock (delays game update to given fps)
class obj_clock:
    def __init__(self):
        self.clock=pyg.newclock()
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
            img=pyg.loadsurface('book/book.png')
            img=pyg.scalesurface(img,(36,42))
            pyg.savesurface(img, 'book/bookicon.png')
    def seticon(self):          
        if os.path.exists('book/bookicon.png'):
            img=pyg.loadsurface('book/bookicon.png')
        else:
            img=pyg.loadsurface('data/booknoicon.png')
        img.set_colorkey((255,255,255))# white
        share.display.seticon(img)
        
        
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
# Links to external libraries


# links to module os
def pathexists(path):
    return os.path.exists(path)


# links to module math
def cos(x):
    return math_cos(x)
def sin(x):
    return math_sin(x)
def atan2(y,x):
    return math_atan2(y,x)
def angle(a_xy,b_xy):# angle between points a=(x,y) and b=(x,y)
    return math_atan2(b_xy[1]-a_xy[1],b_xy[0]-a_xy[0])
def actorsangle(a,b):# angle between actors a,b (with attributes a.x,a.y)
    return math_atan2(b.y-a.y,b.x-a.x)



####################################################################################################################
# General Functions and objects for all uses

# check if a point x,y is in a given rectangle rect=(xmin,xmax,ymin,ymax)
def isinrect(x,y,rect):
    (xmin,xmax,ymin,ymax)=rect
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

