#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter0.py: prologue
#
##########################################################
##########################################################

import share
import tool
import draw
import page
import actor
import world

##########################################################
##########################################################

# Chapter: Game Prologue
# *PROLOGUE
class obj_scene_prologue(page.obj_chapterpage):
    def setup(self):
        self.text=['-----   Prologue   -----   ',\
                   '\nIn the Beginning, there was Nothing. Absolutely Nothing. \nBut one Could Press [Enter] to Continue.']
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p1())


class obj_scene_ch0p1(page.obj_chapterpage):
    def setup(self):
        self.text=['One Could Press [Enter] to Continue, or [Tab] to go back. It was always like that.',\
                   '\n[Tab: Back]   [Enter: Continue]']
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_prologue())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())


# Scene: Draw Pen
class obj_scene_ch0p2(page.obj_chapterpage):
    def setup(self):
        self.text=['There was going to be a pen, and the pen was going to be drawn. ',\
                   'The pen was to be drawn with a lot of emotions, even if it was just a pen.',\
                   'The pen was drawn with [Left Mouse] and erased with [Right Mouse].',\
                   ]
        self.addpart( draw.obj_drawing('pen',(600,440),legend='Pen') )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())


class obj_scene_ch0p3(page.obj_chapterpage):
    def setup(self):
        self.text=['The Pen liked to move around a little. it was a happy pen.',\
                   ]
        self.addpart( draw.obj_animation('penmove','pen',(640,360)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())


# Scene: Draw Eraser
class obj_scene_ch0p4(page.obj_chapterpage):
    def setup(self):
        self.text=['Along with the pen, there was going to be an eraser.',\
                   '\nThe eraser was drawn with [Left Mouse] and erased with [Right Mouse]',\
                   ]
        self.addpart( draw.obj_drawing('eraser',(900,450), legend='Eraser') )
        self.addpart( draw.obj_animation('penmove2','pen',(640,360)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())


class obj_scene_ch0p5(page.obj_chapterpage):
    def setup(self):
        self.text=['The Pen and Eraser looked like this, and they were very happy.',\
                   'They danced together all day.',\
                   ]
        animation1=draw.obj_animation('penmove2','pen',(640,360))
        animation2=draw.obj_animation('erasermove','eraser',(640,360),sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p6())


class obj_scene_ch0p6(page.obj_chapterpage):
    def setup(self):
        self.text=['Because in the Beginning, there was Nothing, It was unclear how the pen had been drawn.',\
                   'And when there would be nothing again, it was unclear how the eraser would be erased.',\
                   ' But it didnt matter much right now because there were many more things to draw and erase.',\
                   ]
        animation1=draw.obj_animation('penmove2a','pen',(640,360))
        animation2=draw.obj_animation('erasermovea','eraser',(640,360),sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())


class obj_scene_ch0p7(page.obj_chapterpage):
    def setup(self):
        self.text=['In the middle of the dancing, there was going to be a book. A very mysterious book [draw].',\
                   'It was drawn with [Left Mouse], and could be restarted with [Right Mouse]. ',\
                   ]
        self.addpart( draw.obj_drawing('book',(640,420), legend='Mysterious Book') )
        self.addpart( draw.obj_animation('penmove3','pen',(640,360)) )
        self.addpart( draw.obj_animation('erasermove3','eraser',(640,360)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())


class obj_scene_ch0p8(page.obj_chapterpage):
    def setup(self):
        self.text=['It was the book of things. The book of all things were all things would be.',
                   'With the help of the pen and eraser, there would be many things to draw in the book.',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0end())


class obj_scene_ch0end(page.obj_chapterpage):
    def setup(self):
        self.text=['And so the book began...',\
                   ]
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())
    def nextpage(self):
        share.datamanager.updateprogress(chapter=1)# chapter 1 becomes available
        super().nextpage()


####################################################################################################################
