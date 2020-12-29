#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapteri.py: some ideas
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

class obj_scene_chapterideas(page.obj_chapterpage):
    def setup(self):
        self.text=['-----   Chapter What: Ideas   -----   ',\
                   'bla bla bla ',\
                   ]

    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_chip1())# draw door


class obj_scene_chip1(page.obj_chapterpage):
    def setup(self):         
        self.text=['draw',\
                   ] 
        self.addpart( draw.obj_drawing('sun',(640,210),legend='The Sun') )
        self.addpart( draw.obj_drawing('horizon',(640,560),legend='The Horizon') )

    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapterideas())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_chip2())
    
class obj_scene_chip2(page.obj_chapterpage):
    def setup(self):         
        self.text=['sunrise (using an imagefill)',\
                   ] 
        self.addpart( draw.obj_animation('sunrise','sun',(640,210),record=True) )
        
        self.addpart(draw.obj_imagefill((share.colors.background,630,100),(640,670)))# filler
        self.addpart( draw.obj_image('horizon',(640,560)) )

    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chip1())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_chip2())
    
    
    
    
    