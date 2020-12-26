#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# datb.py: databases and file utilities
#
##########################################################
##########################################################

import core
import tool

##########################################################
##########################################################

# Databases

# colors database (RGB)
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
        # Colors devmode
        self.devtextbox=(233,222,100)# yellow
        self.devimage=(250,150,0)# orange
        self.devanimation=(0,220,0)# green
        self.devdispgroup=(128,0,128)# purple
        self.devactor=(0,0,220)# blue (hitbox)
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


# fonts database
class obj_fonts:
    def __init__(self):
         self.font15=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 15)# tiny (for FPS) 
         self.font30=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 30)# small indicators,textbox
         self.font40=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 40)# small indicators,textbox
         self.font50=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 50)# medium (for story text)
         self.font60=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 60)# large
         self.font100=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 100)# big (for titlescreen)
         self.font120=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 120)# huge
    def font(self,fontname):# call by key(string)
         if fontname=='tiny' or fontname==15:
             return self.font15
         elif fontname=='smaller' or fontname==30:
             return self.font30
         elif fontname=='small' or fontname==40:
             return self.font40
         elif fontname=='medium' or fontname==50:
             return self.font50
         elif fontname=='large' or fontname==60:
             return self.font60
         elif fontname=='big' or fontname==100:
             return self.font100
         elif fontname=='huge' or fontname==120:
             return self.font120
         else:
             return self.font50# medium font  


# brushes  database (used for drawing)
class obj_brushes:
    def __init__(self):        
        self.pen=('data/pen.png',(8,8))
        self.smallpen=('data/pen.png',(4,4))
        self.tinypen=('data/pen.png',(2,2))

####################################################################################################################
# File Utilities

class obj_savefile:
    def __init__(self):
        self.filename='book/save.txt'# saved along with drawings
        self.chapter=0# current chapter
        self.load()
    def save(self):
        f1=open(self.filename,'w+')
        f1.write('chapter,'+str(self.chapter)+'\n')# first line
        f1.close()
    def load(self):# load savefile (or set default parameters if doesnt exist)
        if tool.pathexists('book/save.txt'):
            f1=open(self.filename,'r+')
            line=f1.readline()# chapter
            line=line.split(",")
            self.chapter=int(line[1])
            f1.close()
        else:
            self.chapter=0
    def eraseall(self):# erase all progress + drawings
        files = tool.oslistdir('book')
        for i in files: tool.osremove('book/'+i)
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
        if tool.pathexists(self.filename):
            with open(self.filename,'r') as f1:
                matrix=f1.read().splitlines()
                for i in range(int(len(matrix)/2)):# read alternated key,value on lines
                    self.dict[matrix[i*2]]=matrix[i*2+1]
    def eraseall(self):
        self.dict={}
        self.save()# write empty dictionary

####################################################################################################################


