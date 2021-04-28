#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter7.py: ...
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

# Chapter VII: ...
# *CHAPTER VII

class obj_scene_chapter7(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p0())
    def triggernextpage(self,controls):
        return True
    # def setup(self):
    #     self.text=['-----   Chapter VII: Showtime   -----   ',\
    #                '\n Final chapter. hero unlocks east gate, confronts villain, rescues partner. ',\
    #               '\n Reuse all minigames but in setting against the villain, as the final fight. ',\
    #                ]


class obj_scene_ch7p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p1())
    def setup(self):
        self.text=['-----   Chapter VII: Showtime   -----   ',\
                  '\n Sorry this chapter isnt ready yet, come back later. ',\
                'The mottos are not fight-perservere-overcome, but lie-cheat-steal. ',\
              'and the mottos: "lie in any situation. always cheat. steal everything" ',\

                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch7p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p0())
    def setup(self):
        self.text=['You have unlocked the credits! Access them from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=8)# chapter 8 (credits)
