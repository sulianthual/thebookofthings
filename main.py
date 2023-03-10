#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# main.py: main executable
#          ($ python main.py)
#
##########################################################
##########################################################


import os
# 1) change directory to current directory
os.chdir(os.getcwd())

import share

##########################################################
# Game Loop

def main():

    while True:
        share.scenemanager.update(share.controls)# (everything happens here)
        share.display.update()
        share.controls.update()
        share.clock.update()


if __name__ == '__main__':
    main()

##########################################################
##########################################################
##########################################################
