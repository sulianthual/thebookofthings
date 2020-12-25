#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# share.py: shared (global) game elements (accessible by all modules)
#
# Note: the modules (draw,utils,world,actor...) import each other (cyclically)
#       but it doesnt matter as long as we refer to them by name (e.g. $ a=draw.obj_image())
#       however absolutely avoid partial imports (e.g. $ from draw import obj_image)
# 
##########################################################
##########################################################

import utils
import pyg
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
pyg.initialize()# game engine (pygrame)
clock=utils.obj_clock()# game clock 
screen=utils.obj_screen()# drawing screen
display=utils.obj_display()# window display (pygame.display.update)
controls=pyg.obj_controls()# mouse/keyboard controls
windowicon=utils.obj_windowicon()# window icon
#
# Databases
fonts=page.obj_fonts()# text fonts 
colors=page.obj_colors()# dictionary of colors
brushes=page.obj_brushes()# brushes used for drawing
#
# Utilities
words=utils.obj_savewords()# save/load data (words)
savefile=utils.obj_savefile()# save/load data 
quitgame=utils.obj_quit()# function quit game
#
# Scenes
scenemanager=utils.obj_scenemanager()# game scene manager (switch scenes+quit...) 
titlescreen=menu.obj_scene_titlescreen(scenemanager)
scenemanager.scene=titlescreen# set starting scene

##########################################################





