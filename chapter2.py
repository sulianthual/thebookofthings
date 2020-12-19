#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# chapter2.py: a house
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
import actor

##########################################################
##########################################################

# Chapter I: A House
# *CHAPTER II

# 
class obj_scene_chapter2(utils.obj_page):
    def setup(self):
        self.text=['-----   Chapter II: A House   -----   ',\
                   '\nIn the book of things, the Hero ',('{heroname}',share.colors.hero),' lived in a house, '\
                   'and there would be a lot of things to do in that house. ',\
                   'The ',('house',share.colors.house),' was to be named using the [KEYBOARD].',\
                       ]
        self.textinput1=draw.obj_textinput('housename',25,(650,260),color=share.colors.house)# input keyword, max characters, position
        self.textinput1.makelegend('House Name')
    def page(self,controls):
        self.textinput1.update(controls)
    def prevpage(self):
        share.words.save()# resave (entire) dictionary of words in file
        super().prevpage()
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p1(self.creator)# next scene
        share.words.save()# resave (entire) dictionary of words in file
        
        
class obj_scene_ch2p1(utils.obj_page):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house, ",\
                   'that was named',('{housename}',share.colors.house),' had a door. '\
                   'It was a very common door, that could be found everywhere. '
                   'It would open when ',('{heroname}',share.colors.hero), ' entered, '\
                   'and close the rest of the time. '
                   '[Tab: Back]   [Enter: Continue]']
        # 
        self.drawing=draw.obj_drawing('housedoor_closed',(340,460))# new drawing 
        self.drawing.makelegend('Door Closed')
        self.drawing2=draw.obj_drawing('housedoor_open',(940,460))# new drawing 
        self.drawing2.makelegend('Door Open')
        self.drawlist=[self.drawing,self.drawing2]
        #
        # add hero in the middle
        self.animlist=[]
        self.animlist.append(draw.obj_animation('herolegs_stand','herolegs_stand',(640,460-60+160)))
        self.animlist.append(draw.obj_animation('herohead_lookaround','herohead',(640,460-60)))
    def page(self,controls):
        for i in self.drawlist:
            i.display()
            i.update(controls) 
        for i in self.animlist: i.play(controls)
    def prevpage(self):
        for i in self.drawlist: i.finish()# save drawing
        self.creator.scene=obj_scene_chapter2(self.creator)
    def nextpage(self):
        for i in self.drawlist: i.finish()# save drawing
        self.creator.scene=obj_scene_ch2p2(self.creator)# next scene  


class obj_scene_ch2p2(utils.obj_page):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house, ",\
                   'that was named',('{housename}',share.colors.house),\
                   'looked like this from the outside. ',\
                   '[Tab: Back]   [Enter: Continue]']
        # 
        self.s=0.25
        self.drawing=draw.obj_drawing('house',(640,400))# new drawing 
        self.drawing.makelegend('House from outside')
        self.drawing.brush=share.brushes.smallpen# draw with smaller pen
        self.image=draw.obj_image('housedoor_closed',(640,500))# new drawing 
        self.image.scale(self.s)
        #
        # add hero in the middle
        self.animlist=[]
        self.animlist.append(draw.obj_animation('herolegs_stand','herolegs_stand',(240,560-60+160*self.s)))
        self.animlist.append(draw.obj_animation('herohead_lookaround','herohead',(240,560-60)))
        for i in self.animlist: i.scale(self.s)
    def page(self,controls):        
        self.drawing.update(controls) 
        self.image.display()
        for i in self.animlist: i.play(controls)
    def prevpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_ch2p1(self.creator)
    def nextpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_ch2p3(self.creator)# next scene  


class obj_scene_ch2p3(utils.obj_page):
    def setup(self):         
        self.text=['To enter house hero needed to knock the door with his weapon called...',\
                   '[Tab: Back]   [Enter: Continue]']
        # 
        self.image=draw.obj_image('house',(640,400))# new drawing 
        #
        # put world with hero at 0.25s: => MUST SCALE actor, dispgroup properly!!!
        # restrict world boundaries to an horizon line (with dy much stronger on top)

        # self.image=draw.obj_image('housedoor_closed',(640,500))# new drawing 
        # self.image.scale(self.s)

    def page(self,controls):        

        self.image.display()

    def prevpage(self):
        self.creator.scene=obj_scene_ch2p2(self.creator)
    # def nextpage(self):
        # self.creator.scene=obj_scene_ch2p4(self.creator)# next scene  

