#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# ideas.py: menu with some ideas
#
##########################################################
###########################################################

import share
import tool
import draw
import page
import actor
import world

##########################################################
##########################################################

# Test Menu
class obj_scene_ideamenu(page.obj_page):
    def __init__(self):
        super().__init__()
    def setup(self):
        super().setup()
        share.ipage=1# current page number in chapter
        self.nrow=17# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Appendix Ideas [Enter: Read] [Tab: Back]',(640,50),fontsize='medium'))
        self.addpart(draw.obj_textbox('[Space: Main Menu]',(1120,700),fontsize='smaller'))
        for i,test in enumerate(self.list[:self.nrow-1]):
            self.addpart(draw.obj_textbox(test.name,(250,130+i*30),fontsize='smaller'))
        for i,test in enumerate(self.list[self.nrow-1:]):
            self.addpart(draw.obj_textbox(test.name,(640,130+i*30),fontsize='smaller'))
        self.sprite_pointer=draw.obj_textbox('---',(640,360),fontsize='smaller')# moved around
        self.addpart(self.sprite_pointer)
    def page(self,controls):
        if share.iidea<self.nrow-1:
            self.sprite_pointer.movetox(60)
            self.sprite_pointer.movetoy(130+share.iidea*30)
        else:
            self.sprite_pointer.movetox(460)
            self.sprite_pointer.movetoy(130+(share.iidea-self.nrow+1)*30)
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            share.iidea += 1
            if share.iidea == self.listlen: share.iidea=0
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            share.iidea -= 1
            if share.iidea == -1: share.iidea=self.listlen-1
        if (controls.enter and controls.enterc):
            share.scenemanager.switchscene(self.list[share.iidea],init=True)
        if controls.space and controls.spacec:
            share.scenemanager.switchscene(share.titlescreen)

    def loadtests(self):# load all tests
        # developper
        self.list.append(obj_scene_ideatodo())
        self.list.append(obj_scene_idea1())
        #
        self.listlen=len(self.list)


# Template for test page = chapter page with slightly modified functionalities
class obj_ideapage(page.obj_chapterpage):
    def __init__(self):
        self.name='Unamed'# needs name to display on test menu
        super().__init__()
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_ideamenu())
    def exitpage(self):
        share.scenemanager.switchscene(obj_scene_ideamenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_ideamenu())

#########################################################################
#########################################################################

class obj_scene_ideatodo(obj_ideapage):
    def setup(self):
        self.name='Todo List'
        self.text=['Todo List:',\
                   '\nx) No more advanced physics! Only simple minigames',\
                   '\nx) From simple story hero-princess, make alterations each day ',\
                   '\nx) Use mise en abime where book, pen and eraser discuss new changes each day',\
                   '\nx) Open new alterations with simple puzzles (get item from previous choice, etc...)',\
                   '\nx)',\
                   '\nx)',\
                   ]
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting

class obj_scene_idea1(obj_ideapage):
    def setup(self):
        self.name='Sunrise'
        self.text=['draw',\
                   ]
        self.addpart( draw.obj_drawing('sun',(640,210),legend='The Sun') )
        self.addpart( draw.obj_drawing('horizon',(640,560),legend='The Horizon') )
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_idea1p2())
class obj_scene_idea1p2(obj_ideapage):
    def setup(self):
        self.name='Sunrise p2'
        self.text=['sunrise (using an imagefill)',\
                   ]
        self.addpart( draw.obj_animation('sunrise','sun',(640,210),record=True) )

        self.addpart(draw.obj_imagefill((share.colors.background,630,100),(640,670)))# filler
        self.addpart( draw.obj_image('horizon',(640,560)) )
