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

import share

##########################################################
# Game Loop
# ttterm1=21

def main():

    while True:
        share.clock.update()
        share.display.update()
        share.controls.update()
        share.scenemanager.update(share.controls)# (everything happens here)


if __name__ == '__main__': main()#tesresr

##########################################################
##########################################################
##########################################################
