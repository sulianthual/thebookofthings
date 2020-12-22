#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# pyg.py: game engine module
#
# Any call to the game engine must be linked here.
# Currently the game engine is pygame (version 1.9.4)
# 
# Why?
# - We may be able to improve the game engine more easily, for example using dirty sprites
# - If we wanted to change the game engine we could do it more easily here.
# 
##########################################################
##########################################################

import pygame

##########################################################
##########################################################

# initialize game engine
def initialize():
    pygame.init()# init all modules (we could select them if they are not all used)
    pygame.time.wait(200)# wait 200 ms (to let some modules like pygame.font initialize entirely)

# exit game engine
def shutdown():
    pygame.display.quit()
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

##########################################################
# pygame display

# new display object (returns object surface, not display !?!)
def newdisplay(width,heigth):
    return pygame.display.set_mode((width,heigth))
def display_set_caption(text):
    pygame.display.set_caption(text)
def display_set_icon(image):
    pygame.display.set_icon(image)
def display_quit():
    pygame.display.quit()
def display_update():
    pygame.display.update()


    
##########################################################
# Pygame surfaces


# create new pygame surface object (returns surface object)
def newsurface(size):
    return pygame.Surface(size)    

# load pygame surface object from file (returns surface object)
def loadsurface(path,convert=True):
    if convert:
        return pygame.image.load(path).convert()
    else:
        return pygame.image.load(path)

# save pygame surface object to file
def savesurface(img,path):
    pygame.image.save(img,path) 

def fillsurface(surface,color):
    return surface.fill(color)

def blitsurface(surface,blitsurface,xy):
    return surface.blit(blitsurface,xy)

# flip a pygame surface object (returns modified surface object)
# $ a=flipsurface(surface,True,False)
def flipsurface(surface,fliph,flipv):
    return pygame.transform.flip(surface,fliph,flipv)

# scale a pygame surface object (returns modified surface object)
# $ a=scalesurface(surface,(100,200))
def scalesurface(surface, newscales):
    return pygame.transform.scale( surface, (int(newscales[0]),int(newscales[1])) )

# rotate a pygame surface object (returns modified surface object)
# $ a=rotatesurface(surface,45)
def rotatesurface(surface, angle):
    return pygame.transform.rotate(surface,angle)

##########################################################
# Pygame others

def mouse_set_visible(value):# value is bool
    pygame.mouse.set_visible(value)
    
# pygame clock object (returns clock object)
def newclock():
    return pygame.time.Clock()
def getclockfps(clock):
    return clock.get_fps()# method: get_fps
def clocktick(clock,fps):
    clock.tick(fps)

# new pygame font object (returns font object)
# $ a=newfont('AmaticSC-Bold.ttf', 15)
def newfont(filename,size):
    return pygame.font.Font(filename, size)

    

# Cross display
def crossdisplay(screen,color,xy,radius,thickness=3,diagonal=False):
    if not diagonal:        
        pygame.draw.line(screen,color,(xy[0]-radius,xy[1]),(xy[0]+radius,xy[1]),thickness)
        pygame.draw.line(screen,color,(xy[0],xy[1]-radius),(xy[0],xy[1]+radius),thickness)
    else:
        pygame.draw.line(screen,color,(xy[0]-radius,xy[1]-radius),(xy[0]+radius,xy[1]+radius),thickness)
        pygame.draw.line(screen,color,(xy[0]+radius,xy[1]-radius),(xy[0]-radius,xy[1]+radius),thickness) 

    
# Rectangle display
# $ rectdisplay(screen,(0,0,0),(640,360),10,10)
def rectdisplay(screen,color,rect,thickness=3,fill=False):# x,y=center
    x,y,width,height=rect
    if fill:
        pygame.draw.rect(screen, color, (int(x-width/2), int(y-height/2), int(width), int(height)), 0)
    else:
        pygame.draw.rect(screen, color, (int(x-width/2), int(y-height/2), int(width), int(height)), thickness)
    
    
# Line display
# $ linedisplay(screen,(0,0,0),(10,20),(30,40))
def linedisplay(screen,color,xy1,xy2,thickness=3):
    pygame.draw.line(screen,color,xy1,xy2,thickness)
    
    

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
    
    

    
    
    
    