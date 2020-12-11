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
                   '\nThe Hero ',('{heroname}',share.colors.hero),' lived in a large house. '\
                   'The ',('house',share.colors.house),' was name like this and looked like this from the outside. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.textinput1=draw.obj_textinput('housename',25,(650,260),color=share.colors.house)# input keyword, max characters, position
        self.textinput1.legend='House Name'
    def page(self,controls):
        self.textinput1.update(controls)
    def prevpage(self):
        share.words.save()# resave (entire) dictionary of words in file
        super().prevpage()
    # def nextpage(self):
        # self.creator.scene=obj_scene_ch1p1(self.creator)# next scene
        # share.words.save()# resave (entire) dictionary of words in file