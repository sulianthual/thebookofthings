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
                   '\nx) No more advanced physics! Only simple goofy minigames',\
                   '\nx) No more advanced drawings, only simple and goofy. Like same face on everything',\
                   '\nx) Basis=3 chapter story: Hero, Partner, Villain.',\
                   '\nx) Beware not to put choices (except gender/basic stuff) in the basis? ',\
                   '\nx) Each new choice must be introduced and requires new drawings.',\
                   '\nx) Then make alterations in Part II, Part III (Partner=He,She, Pet. Relation=love,friends,its complicated) ',\
                   '\nx) In Subsequent Parts on can add alterations to the basic story (choose from list at beginning of the day)',\
                   '\nx) Use mise en abime where book, pen and eraser discuss new changes each day',\
                   '\nx) book=instructions/critic, pen=new content, eraser=modify content',\
                   '\nx) Open new alterations with simple puzzles (get item from previous choice, etc...)',\
                   '\nx)',\
                   '\nx)',\
                   ]
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting

class obj_scene_idea1(obj_ideapage):
    def setup(self):
        self.name='Mini Games Ideas'
        self.text=['Mini Games Ideas:',\
                   '\nx) Game Mechanics: ',\
                   '\nx) Waking up=Hold [W]',\
                   '\nx) Fishing=Lower Hook [S]',\
                   '\nx) Eating=Mash [A][D]',\
                   '\nx) Shoot arrow=Parabolic Arc [A][D] then [W]',\
                   '\nx) Fight = Play Pong [W][S]',\
                   '\nx) Fight = Mash [A][D]',\
                   '\nx) Fight = Rock Paper Scissors (choose quickly on beat [A][W][D])',\
                   '\nx) Flappy Bird=One tap to stay level',\
                   '\nx) Serenade=[W][A][S][D] random sequence on music sheet to reproduce (draw guitare and musical note)',\
                   '\nx) Mario level= move [A][D] and jump [W]',\
                   '\nx) avoid falling boulders=[A][D]',\
                   '\nx) Kissing=[S] at right time for Hero/Princess moving opposite up down on left/right side of screen',\
                   '\nx) Basketball=jump and shoot Holding [S] in moving hoop laterally ',\
                   '\nx) Bait=guide monster to trap [WASD]. It charges straigth',\
                   '\nx) Shooter=Cannon on fast rotating wheel, shoot stuff with [W]',\
                   '\nx) Indiana jones ball behind=[A][D] to avoid obstacles',\
                   '\nx)',\
                   '\nx)',\
                   '\nx)',\
                   '\nx)',\
                   '\nx)',\
                   '\nx)',\
                   ]
