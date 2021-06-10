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
import menu



##########################################################
# Global parameters
#
fps=60# game fps (only supports 60, 30 and 20 fps, see draw.py/obj_animation)
colorkey=(128,0,128)# color used for transparency on images (purple)


# Global variables
#
devaccess=False# user has access to developer mode (cant change here, must change MANUALLY in the settings file)
devmode=False # developer mode toggle
dt=1# elapsed time since last frame (updated by game clock each frame)
itest=0# test menu index
iidea=0# idea menu index

##########################################################
# Initialize shared elements (order matters)



# Game Core (order matters)
core.initialize()# start game engine (pygame)
clock=core.obj_clock()# game clock
screen=core.obj_screen()# display buffer screen
datamanager=datb.obj_datamanager()# data manager (display, music,etc...)
musicplayer=core.obj_musicplayer()# music player
soundplayer=core.obj_soundplayer()# sound player

controls=core.obj_controls()# mouse/keyboard controls
snapshotmanager=datb.obj_snapshotmanager()# snapshot manager (manages dependencies for images that combine drawings)
display=core.obj_display()# window display (pygame.display.update)
quitgame=core.obj_quit()# function quit game
#
# Databases with quick access
fonts=datb.obj_fonts()# text fonts
colors=datb.obj_colors()# dictionary of colors
brushes=datb.obj_brushes()# brushes used for drawing
musics=datb.obj_musics()# music names
sounds=datb.obj_sounds()# sound names
gamecredits=datb.obj_gamecredits()# game credits text
#
# Devtools
devaccess=datamanager.getdevaccess()# ask datamanager if user has dev access (edit file settings.txt to allow)
#
# Scenes
scenemanager=core.obj_scenemanager()# game scene manager (switch scenes+quit...)
titlescreen=menu.obj_scene_titlescreen()# menu object has only ONE instance
scenemanager.switchscene(titlescreen)# set starting scene


##########################################################
