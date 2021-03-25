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
        # NB: colorkey is defined in share (as global variable)
        # base colors
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(220,0,0)# bit darker
        self.blue=(0,0,220)
        self.green=(0,220,0)
        self.gray=(150,150,150)
        self.darkgray=(100,100,100)
        self.brown=(165,42,42)
        self.maroon=(128,0,0)
        self.purple=(128,0,128)
        self.pink=(231,84,128)
        # Colors devmode
        self.devtextbox=(233,222,100)# yellow
        self.devimage=(250,150,0)# orange
        self.devanimation=(0,220,0)# green
        self.devdispgroup=(128,0,128)# purple
        self.devactor=(0,0,220)# blue (hitbox)
        # Colors game elements
        self.background=self.white# game background
        self.instructions=self.purple# any instruction text/element
        self.drawing=(220,0,0)# drawing
        self.input=self.red# text input (in text)
        self.textinput=(200,0,0)# text input (box)
        self.textchoice=(180,0,0)# text input box
        # Colors for story
        self.hero=self.red# hero text color
        self.partner=self.pink#partner text color
        self.villain=self.brown#partner text color
        self.item=self.blue# items (bed, fish,etc...)
        self.action=self.green# actions text (fishing, etc...)



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
        self.bigpen=('data/pen.png',(16,16))
        self.pen12=('data/pen.png',(12,12))
        self.pen=('data/pen.png',(8,8))
        self.smallpen=('data/pen.png',(4,4))
        self.tinypen=('data/pen.png',(2,2))
        self.shadowpen=('data/shadowpen.png',(64,64))


####################################################################################################################

# Data Manager: manages all data files
# flieprogress: last unlocked chapter
# filewords: dictionary of textinputs,textchoices written in the book of things (by the player)
class obj_datamanager:
    def __init__(self):
        self.fileprogress='book/progress.txt'# current game progress for unlocks
        self.loadprogress()
        self.filewords='book/words.txt'# current written words for things
        self.loadwords()
    def erasebook(self):
        files = tool.oslistdir('book')
        for i in files: tool.osremove('book/'+i)
        self.chapter=0
        self.dictwords={}
        self.saveprogress()
        self.savewords()
    def getprogress(self):
        return self.chapter# last chapter unlocked
    def saveprogress(self):
        with open(self.fileprogress,'w+') as f1:
            f1.write('chapter,'+str(self.chapter)+'\n')# first line
    def loadprogress(self):
        if tool.ospathexists(self.fileprogress):
            with open(self.fileprogress,'r+') as f1:
                line=f1.readline()# chapter
                line=line.split(",")
                self.chapter=int(line[1])
        else:
            self.chapter=0
    def updateprogress(self,chapter=None):
        if chapter:
            self.chapter=max(self.chapter,chapter)
        self.saveprogress()
    def getwords(self):
        return self.dictwords# dictionary of words=(key,value)
    def getwordkeys(self):
        return self.dictwords.keys()
    def getword(self,wordkey):
        return self.dictwords[wordkey]
    def writeword(self,wordkey,wordvalue):
        self.dictwords[wordkey]=wordvalue
    def savewords(self):# save keywords to file
        with open(self.filewords,'w') as f1:
            for i in self.dictwords.items():# iterate over tuples =(key,value)
                f1.write(str(i[0])+'\n')#key
                f1.write(str(i[1])+'\n')#value
    def loadwords(self):# load keywords from file
        if tool.ospathexists(self.filewords):
            self.dictwords={}
            with open(self.filewords,'r') as f1:
                matrix=f1.read().splitlines()
                for i in range(int(len(matrix)/2)):# read alternated key,value on lines
                    self.dictwords[matrix[i*2]]=matrix[i*2+1]
        else:
            self.dictwords={}





####################################################################################################################
