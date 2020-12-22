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

import pyg
pyg.initialize()# initialize game engine
import share# initialize shared objects


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