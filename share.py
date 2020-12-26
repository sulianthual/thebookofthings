#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# share.py: shared (global) game elements (accessible by all modules)
#
# Note: the modules (draw,core,world,actor...) import each other (cyclically)
#       but it doesnt matter as long as we refer to them by name (e.g. $ a=draw.obj_image())
#       however absolutely avoid partial imports (e.g. $ from draw import obj_image)
# 
##########################################################
##########################################################

import core
import datb
#
import page
import menu



##########################################################
# Global variables 
#
fps=60 # (keep at 60 because game is fps based)
devmode=False # developer mode toggle

itest=0# index of current text in test menu
ipage=1# current page within a chapter

##########################################################
# Initialize shared elements (order matters)

# Game Core
core.initialize()# start game engine (pygame)
clock=core.obj_clock()# game clock 
screen=core.obj_screen()# display buffer screen
display=core.obj_display()# window display (pygame.display.update)
controls=core.obj_controls()# mouse/keyboard controls
windowicon=core.obj_windowicon()# window icon
quitgame=core.obj_quit()# function quit game
#
# Databases and File Utilities
fonts=datb.obj_fonts()# text fonts 
colors=datb.obj_colors()# dictionary of colors
brushes=datb.obj_brushes()# brushes used for drawing
words=datb.obj_savewords()# save/load data (words)
savefile=datb.obj_savefile()# save/load data (progress)
#
# Scenes
scenemanager=page.obj_scenemanager()# game scene manager (switch scenes+quit...) 
titlescreen=menu.obj_scene_titlescreen(scenemanager)
scenemanager.scene=titlescreen# set starting scene

##########################################################





