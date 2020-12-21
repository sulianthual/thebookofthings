#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# chapter0.py: prologue
#
##########################################################
##########################################################

import sys
import os
import pygame
#
import share
import draw
import utils
import menu

##########################################################
##########################################################

# Chapter: Game Prologue
# *PROLOGUE 
class obj_scene_prologue(utils.obj_page):
    def setup(self):         
        self.text=['-----   Prologue   -----   ',\
                   '\nIn the Beginning, there was Nothing. Absolutely Nothing. \nBut one Could Press [Enter] to Continue.']
    def postsetup(self):
        super().postsetup()
        share.pagenotedisplay(' ',rebuild=True)# no page note
    def prevpage(self): 
        super().prevpage()# includes refresh titlescreen
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p1(self.creator)

class obj_scene_ch0p1(utils.obj_page):
    def setup(self):       
        self.text=['One Could Press [Enter] to Continue, or [Tab] to go back. It was always like that.',\
                   '\n[Tab: Back]   [Enter: Continue]']
    def postsetup(self):
        super().postsetup()
        share.pagenotedisplay(' ',rebuild=True)# no page note
    def prevpage(self): 
        self.creator.scene=obj_scene_prologue(self.creator) 
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p2(self.creator) 

        
# Scene: Draw Pen
class obj_scene_ch0p2(utils.obj_page):
    def setup(self):       
        self.text=['There was going to be a pen, and the pen was going to be drawn. ',\
                   'The pen was to be drawn with a lot of emotions, even if it was just a pen.',\
                   'The pen was drawn with [Left Mouse] and erased with [Right Mouse].',\
                   ]
        self.addpart( draw.obj_drawing('pen',(600,440),legend='Pen') )
    def prevpage(self):
        self.creator.scene=obj_scene_ch0p1(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch0p3(self.creator)# next scene


class obj_scene_ch0p3(utils.obj_page):
    def setup(self):      
        self.text=['The Pen liked to move around a little. it was a happy pen.',\
                   ]
        self.addpart( draw.obj_animation('penmove','pen',(640,360)) )
    def prevpage(self): 
        self.creator.scene=obj_scene_ch0p2(self.creator)
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p4(self.creator)            


# Scene: Draw Eraser
class obj_scene_ch0p4(utils.obj_page):
    def setup(self):      
        self.text=['Along with the pen, there was going to be an eraser.',\
                   '\nThe eraser was drawn with [Left Mouse] and erased with [Right Mouse]',\
                   ]
        self.addpart( draw.obj_drawing('eraser',(900,450), legend='Eraser') )
        self.addpart( draw.obj_animation('penmove2','pen',(640,360)) )
    def prevpage(self):
        self.creator.scene=obj_scene_ch0p3(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch0p5(self.creator)# next scene


class obj_scene_ch0p5(utils.obj_page):
    def setup(self):       
        self.text=['The Pen and Eraser looked like this, and they were very happy.',\
                   'They danced together all day.',\
                   ]
        animation1=draw.obj_animation('penmove2','pen',(640,360))
        animation2=draw.obj_animation('erasermove','eraser',(640,360))
        animation2.ntmax=animation1.nt# same number of frames
        self.addpart( animation1 )
        self.addpart( animation2 )
    def prevpage(self): 
        self.creator.scene=obj_scene_ch0p4(self.creator)
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p6(self.creator)

class obj_scene_ch0p6(utils.obj_page):
    def setup(self):        
        self.text=['Because in the Beginning, there was Nothing, It was unclear how the pen had been drawn.',\
                   'And when there would be nothing again, it was unclear how the eraser would be erased.',\
                   ' But it didnt matter much right now because there were many more things to draw and erase.',\
                   ]
        animation1=draw.obj_animation('penmove2a','pen',(640,360))# start animation
        animation2=draw.obj_animation('erasermovea','eraser',(640,360))# start animation
        animation2.ntmax=animation1.nt# same number of frames
        self.addpart( animation1 )
        self.addpart( animation2 )
    def prevpage(self): 
        self.creator.scene=obj_scene_ch0p5(self.creator)
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p7(self.creator)
        
# Scene: Draw Book
class obj_scene_ch0p7(utils.obj_page):
    def setup(self):      
        self.text=['In the middle of the dancing, there was going to be a book. A very mysterious book [draw].',\
                   'It was drawn with [Left Mouse], and could be restarted with [Right Mouse]. ',\
                   ]
        self.addpart( draw.obj_drawing('book',(640,420), legend='Mysterious Book') )
        self.addpart( draw.obj_animation('penmove3','pen',(640,360)) )
        self.addpart( draw.obj_animation('erasermove3','eraser',(640,360)) )  
    def prevpage(self):
        self.creator.scene=obj_scene_ch0p6(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch0p8(self.creator)# next scene

class obj_scene_ch0p8(utils.obj_page):
    def setup(self):       
        self.text=['It was the book of things. The book of all things were all things would be.',
                   'With the help of the pen and eraser, there would be many things to draw in the book.',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )
    def prevpage(self): 
        self.creator.scene=obj_scene_ch0p7(self.creator)
    def nextpage(self): 
        self.creator.scene=obj_scene_ch0p9(self.creator)

class obj_scene_ch0p9(utils.obj_page):
    def setup(self):       
        self.text=['And so the book began...',\
                   ]
    def prevpage(self): 
        self.creator.scene=obj_scene_ch0p8(self.creator)
    def nextpage(self): 
        share.savefile.chapter=max(share.savefile.chapter,1)# update progress to chapter 1
        share.savefile.save()# save progress in file
        super().nextpage()

####################################################################################################################



