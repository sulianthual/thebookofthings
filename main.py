#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# main.py: main executable
#          ($ python -m main.py)
#
##########################################################
##########################################################
# Import libraries and other files

import pygame

# Initialize pygame
pygame.init()# init all modules (we could select them if they are not all used)
pygame.time.wait(200)# wait 200 ms (to let some modules like pygame.font initialize entirely)

import share# all shared objects, variables

##########################################################
# Game Loop

while True:
    
    # Updates    
    share.clock.update()
    share.display.update()
    share.controls.update()
    share.scenemanager.update(share.controls)# everything happens here!
    #
    
##########################################################
##########################################################
##########################################################