#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# tool.py: basic utility tools and external libraries
#
# Any call to external libraries (math,os,sys) is linked here.
#
# Why?
# - If we want to change the external libraries it is much easier
#
##########################################################
##########################################################

import sys
import os
from math import cos as math_cos
from math import sin as math_sin
from math import atan2 as math_atan2
from math import pi as math_pi

##########################################################
##########################################################
# Links to external libraries


# links to module os
def pathexists(path):
    return os.path.exists(path)
def oslistdir(path):
    return os.listdir(path)
def osremove(path):
    os.remove(path)

# links to module math
def pi():
    return math_pi
def cos(x):
    return math_cos(x)
def sin(x):
    return math_sin(x)
def atan2(y,x):
    return math_atan2(y,x)
def angle(a_xy,b_xy):# angle between points a=(x,y) and b=(x,y)
    return math_atan2(b_xy[1]-a_xy[1],b_xy[0]-a_xy[0])
def actorsangle(a,b):# angle between actors a,b (with attributes a.x,a.y)
    return math_atan2(b.y-a.y,b.x-a.x)

        
####################################################################################################################
# General Functions and objects for all uses

# check if a point x,y is in a given rectangle rect=(xmin,xmax,ymin,ymax)
def isinrect(x,y,rect):
    (xmin,xmax,ymin,ymax)=rect
    if x>xmin and x<xmax and y>ymin and y<ymax:
        return True
    else:
        return False

# check if two actors a,b (with attributes x,y) are colliding (within given distance r)
def checkdotscollide(a,b,r):
    return (a.x-b.x)**2+(a.y-b.y)**2<r**2

# check if two actors a,b (with attributes x,y,rd) are colliding
def checkcirclecollide(a,b):
    return (a.x-b.x)**2+(a.y-b.y)**2<(a.rd+b.rd)**2

# check if two actors a,b (with attributes x,y,rx,ry) are colliding
def checkrectcollide(a,b):
    return abs(a.x-b.x)<a.rx+b.rx and abs(a.y-b.y)<a.ry+b.ry


# Timer for any purpose
# *TIMER
class obj_timer:
    def __init__(self,amount,cycle=False):
        self.amount=amount# integer, amount of time from timer
        # 3 states for the timer: on, ring, off
        self.on=False
        self.ring=False# timer rings (happens once when countdown finishes)
        self.off=True# timer done or not, check it here
        self.t=0# time count
        self.cycle=cycle# optional, timer cycles (restarts automatically when done)
    def start(self):# start (or restart) timer
        self.on=True
        self.ring=False
        self.off=False
        self.t=int(self.amount)
    def run(self):# run timer (without restarting)
        if not self.on: self.start()
    def update(self):# update timer
        if self.on:
            self.t -= 1
            if self.t <0:
                self.ring=True
                self.on=False
        elif self.ring:
            self.ring=False
            self.off=True
            if self.cycle: self.start()# restart if cycled
            
            
####################################################################################################################




