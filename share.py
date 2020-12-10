#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# share.py: all shared (global) items, accessible by main and all file modules
#
##########################################################
##########################################################

import pygame
import utils
import draw
import menu

##########################################################
# Global variables 
#
fps= 60  # game frames per second
devmode = False # developer mode on (toggle False at game release)

itest=0# index of current text in test menu
ipage=1# current page within a chapter
##########################################################
# Shared Modules

# Pygame Global Screen (used/modified by ALL modules very often)
screen=pygame.display.set_mode((1280,720))

##########################################################
# Shared Objects (accessible by main and all file modules)

# Initialize shared game objects (order matters)
clock=pygame.time.Clock()# start clock (to control framerate)
display=utils.obj_display()# display screen 
controls=utils.obj_controls()# mouse/keyboard controls
fonts=utils.obj_fonts()# text fonts
windowicon=utils.obj_windowicon()# game window icon
textdisplay=utils.obj_textdisplay()# text display function
colors=draw.obj_colors()# dictionary of colors
words=utils.obj_savewords()# words written by player in the book


fpsdisplay=utils.obj_fpsdisplay()# fps display function
pagenumberdisplay=utils.obj_pagenumberdisplay()# page display function 
crossdisplay=utils.obj_crossdisplay()#cross display function
brushes=draw.obj_brushes()# brushes used for drawing
savefile=utils.obj_savefile()# save file manager
quitgame=utils.obj_quit()# function quit game
scenemanager=utils.obj_scenemanager()# game scene manager (switch scenes+quit...) 
titlescreen=menu.obj_scene_titlescreen(scenemanager)# activate reference scene=titlescreen
scenemanager.scene=titlescreen# set starting scene=titlescreen

##########################################################





