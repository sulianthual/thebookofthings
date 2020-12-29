#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# tool.py: basic utility tools and external modules
#
# Any call to external modules (sys,os,math...) is made here.
#
# Why?
# - It it easier to manage the external modules this way
#
##########################################################
##########################################################

from sys import exit as sys_exit
from os import path as os_path
from os import listdir as os_listdir
from os import remove as os_remove
from math import pi as math_pi
from math import cos as math_cos
from math import sin as math_sin
from math import atan2 as math_atan2


##########################################################
##########################################################
# Calls to external modules

# module sys
def sysexit():
    sys_exit()
    
# module os
def ospathexists(path):
    return os_path.exists(path)
def oslistdir(path):
    return os_listdir(path)
def osremove(path):
    os_remove(path)

# module math
def pi():
    return math_pi
def cos(x):
    return math_cos(x)
def sin(x):
    return math_sin(x)
def angle(a_xy,b_xy):# angle between points a=(x,y) and b=(x,y)
    return math_atan2(b_xy[1]-a_xy[1],b_xy[0]-a_xy[0])
def actorsangle(a,b):# angle between actors a,b (with attributes a.x,a.y)
    return math_atan2(b.y-a.y,b.x-a.x)

        
####################################################################################################################
# General Functions and objects for all uses


# Format text using dictionary of keywords 
# $ text='{heroname} was happy'
# $ dict={'heroname':'link'}
# $ a=formattext(text,dict) => 'link was happy' 
def formattext(text,**kwargs):# Format text using the keywords written in the book of things (words.txt)
    try:
        text=text.format(**kwargs)# **kwargs is wordkey=wordvalue
        # Format a second time if the value was itself a keyword (e.g. '{marco}' instead of 'link' )
        try:
            text=text.format(**kwargs)
        except:
            pass
    except:
        pass
    return text 
    
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
class obj_timer:
    def __init__(self,amount,cycle=False):
        self.amount=amount# countdown duraction (int)
        # 3 states for the timer: on, ring, off
        self.on=False# countdown happens
        self.ring=False# (once when countdown finishes)
        self.off=True
        self.t=0# countdown time
        self.cycle=cycle# timer cycles (restarts automatically when done)
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




