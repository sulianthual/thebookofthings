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
from math import pi as math_pi
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
        share.screen.screen=pyg.newdisplay(1280,720)# initialize screen (?)
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


####################################################################################################################

# Screen Manager (draws on it)
class obj_screen:
    def __init__(self):
        self.screen=None
    def set_alpha(self,value):
        self.screen.set_alpha(value)
    def fillsurf(self,value):
        self.screen.fill(value)
    def drawsurf(self,surface,xy):# xy is not the center!!!!
        self.screen.blit(surface,xy)
    def drawrect(self,color,rect,thickness=3,fill=False):
        pyg.rectdisplay(self.screen,color,rect,thickness=thickness,fill=fill)
    def drawcross(self,color,xy,radius,thickness=3,diagonal=False):
        pyg.crossdisplay(self.screen,color,xy,radius,thickness=thickness,diagonal=diagonal)
    def drawline(self,color,xy1,xy2,thickness=3):
        pyg.linedisplay(self.screen,color,xy1,xy2,thickness=thickness)





# Game Sprite: manages any 2d surface to be rendered on screen
#              any image but also text, line, cross, rectangle (all treated as surfaces)
# Sprite doesnt have a position x,y!!!!! (that is managed elsewhere)
#$ sprite=obj_sprite()
#$ sprite.load('test.png')
#$ sprite.flip(True,False)
# sprite.display()# display on screen
class obj_sprite:
    def __init__(self):
        self.type='sprite'
        self.spritetype=None#image,text,etc...        

# line sprite
class obj_sprite_line(obj_sprite):
    def __init__(self):
        super().__init__()
        self.surf=None
    def make(self):
        pass
    def display(self,color,xy1,xy2):
        share.screen.drawline(color,xy1,xy2)

# line sequence sprite (from list of points)
class obj_sprite_linesequence(obj_sprite):
    def __init__(self):
        super().__init__()
        self.surf=None
    def make(self):
        pass
    def display(self,color,xylist):#xylist=[xy1,xy2,...]
        if xylist and len(xylist)>1:
            for i,j in zip( range(0,len(xylist)-2) , range(1,len(xylist)-1) ):
                xy1,xy2=xylist[i],xylist[j]
                share.screen.drawline(color,xy1,xy2)
        
# cross sprite
class obj_sprite_cross(obj_sprite):
    def __init__(self):
        super().__init__()
        self.surf=None
    def make(self):
        pass
    def display(self,color,xy,radius,diagonal=False):
        share.screen.drawcross(color,xy,radius,diagonal=diagonal)
        
        
# rectangle sprite
class obj_sprite_rect(obj_sprite):
    def __init__(self):
        super().__init__()
        self.surf=None
    def make(self):
        pass
    def display(self,color,rect):
        share.screen.drawrect(color,rect)      

        
class obj_sprite_image(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='image'       
        self.surf=None# associated pygame surface
        self.rx=None# half-width
        self.ry=None# half-heigth
        self.colorkey=share.colors.colorkey# transparent color
    def makefrompygamesurface(self,pygamesurface):# Should be unecessary eventually once every surface is made an obj_sprite
        self.surf=pygamesurface
        self.addtransparency()
    def make(self):# create empty
        pass
    def makeempty(self,rx,ry):
        self.surf=pyg.newsurface((2*rx,2*ry))
        self.addtransparency()
        self.fill(self.colorkey)
    def load(self,path,convert=True,failsafe=True):
        if os.path.exists(path):
            self.surf=pyg.loadsurface(path,convert=convert)
            self.addtransparency()
            self.rx,self.ry=self.getrxry()
        elif failsafe:
            self.surf=pyg.loadsurface('data/error.png',convert=convert)
            self.addtransparency()
            self.rx,self.ry=self.getrxry()
        else:
            self.surf,self.rx,self.ry=None,None,None
    def save(self,name):
        pyg.savesurface(self.surf,name)
    def addtransparency(self):
        self.surf.set_colorkey(self.colorkey)
    def getrx(self):
        return self.surf.get_rect().size[0]/2
    def getry(self):
        return self.surf.get_rect().size[1]/2
    def getrxry(self):
        term=self.surf.get_rect().size
        return (term[0]/2,term[1]/2)
    def blitfrom(self,sprite_source,xoffset,yoffset): # blit from OTHER sprite_image object
        self.surf.blit(sprite_source.surf,(xoffset,yoffset))
    def copyfrom(self,sprite_source):# not really a copy but a link?
        self.surf=sprite_source.surf
    def fill(self,color):
        self.surf.fill(color)
    def flip(self,fliph,flipv):
        if fliph or flipv:
            self.surf=pyg.flipsurface(self.surf,fliph,flipv)
    def scale(self,scaling,target=False):# scaling factor or target size
        if not target:            
            if scaling !=1: 
                termx=self.getrx()*2*scaling
                termy=self.getry()*2*scaling
                self.surf=pyg.scalesurface(self.surf,(termx,termy))
                self.rx,self.ry=self.getrxry()
        else:
                self.surf=pyg.scalesurface(self.surf,scaling)
                self.rx,self.ry=self.getrxry()            
    def rotate(self,angle):# returns position offset from rotation
        if angle !=0:
            xold,yold=self.surf.get_rect().center
            self.surf=pyg.rotatesurface(self.surf,angle)
            xnew,ynew=self.surf.get_rect().center
            self.rx,self.ry=self.getrxry()
            return xold-xnew,yold-ynew
        else:
            return 0,0
    def rotate90(self,angle):#rotate by closest increment
        angle= int(round(angle%360/90,0)*90)# (in 0,90,180,270)
        if angle !=0:
            self.surf=pyg.rotatesurface(self.surf,angle)
            self.rx,self.ry=self.getrxry()
    def display(self,x,y):# xy=(x,y) center of display
        xd,yd=x-self.getrx(),y-self.getry()# recompute        
        # xd,yd=x-self.rx,y-self.ry# no need to recompute if always up-to-date
        share.screen.drawsurf(self.surf,(int(xd),int(yd)))
        
        
# brush used for drawing
class obj_sprite_brush(obj_sprite_image):
    def __init__(self):  
        super().__init__()
    def makebrush(self,pen):
        self.load(pen[0])
        self.scale(pen[1],target=True)
    
    
# text=like an image but with prerender
class obj_sprite_text(obj_sprite_image):          
    def __init__(self):
        super().__init__()
        self.spritetype='text'
    def make(self,text,font,color,bold=False):
        self.surf=font.render(text,bold,color)
        self.rx,self.ry=self.getrxry()

####################################################################################################################

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
        return pyg.getclockfps(self.clock)
    def update(self):
        pyg.clocktick(self.clock,self.targetfps)



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
def pi():
    return math_pi
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

