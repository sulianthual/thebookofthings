#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# main.py: main executable
#
##########################################################
##########################################################
# Import libraries and other files
import sys# to properly quit game
import os# for knowing which level files are present
import pygame

# Initialize pygame (before import of file modules!)
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.init()
pygame.init()

import share# all shared objects, variables
        
##########################################################
##########################################################

# Initialize game 
# share.scenemanager.scene=menu.obj_scene_titlescreen(share.scenemanager)# first scene=titlescreen

##########################################################
# Game Loop

while True:
    
    # Updates    
    share.clock.tick(share.fps)# delay loop for game to update at 60 fps
    share.display.update()
    share.controls.update()
    share.scenemanager.update(share.controls)# everything happens here!
    #
    
##########################################################
##########################################################
##########################################################