#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter5.py: ...
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

# Chapter V: ...
# *CHAPTER V


class obj_scene_chapter5(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p0())
    def setup(self):
        self.text=['-----   Chapter V: Treasure Hunt   -----   ',\
                   '\n In this chapter introduce the second part of quest (sailor/pirate in south). ',\
                  '\n sailor gives quest if help retrieve treasure (from skeletons on skull island). hero learns to steal ',\
                 '\n draw sailor, and henchmens skeletons ',\
                  '\n add minigame stealth (walk and hide in places with henchmens patrolling) ',\
                   ]



class obj_scene_ch5p0(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def setup(self):
        self.text=['-----   Chapter V: Treasure Hunt   -----   ',\

                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch5p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p0())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VI',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=6)# chapter 6 becomes available