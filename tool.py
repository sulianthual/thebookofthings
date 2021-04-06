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
from random import randint as random_randint
from random import choices as random_randchoice# choices not choice
from random import gauss as random_randgauss

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

# module math (with degrees instead of radians)
def pi():
    return math_pi
def cos(x):
    return math_cos(x*pi()/180)
def sin(x):
    return math_sin(x*pi()/180)
def angle(a_xy,b_xy):# angle between points a=(x,y) and b=(x,y)
    return math_atan2(b_xy[1]-a_xy[1],b_xy[0]-a_xy[0])*180/pi()# in DEG
def actorsangle(a,b):# angle between actors a,b (with attributes a.x,a.y) in radian
    return math_atan2(b.y-a.y,b.x-a.x)*180/pi()# in DEG

# module random
def randint(minrange,maxrange):# returns integer within range with equal probabilities
    return random_randint(minrange,maxrange)

def randchoice(list,probas=None):# returns element from list (with either equal probabilities or weights)
    if probas is None:
        return random_randchoice(list)[0]
    else:
        return random_randchoice(list,weights=probas,k=1)[0]

def randgauss(mean,std):# returns normal gaussian distribution of given mean and std
    return random_randgauss(mean,std)

def randbool():# return True or False with equal probabilities
    return bool(random_randint(0,1))
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

# check if two actors a,b (with attributes x,y) are within given distance r
def checkdistance(a,b,r):
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
        self.amount=round(amount)
        # 3 states for the timer: on, ring, off
        self.on=False# countdown happens
        self.ring=False# (once when countdown finishes)
        self.off=True
        self.t=0# countdown time
        self.cycle=cycle# timer cycles (restarts automatically when done)
    def start(self,amount=None):# start (or restart) timer
        if amount:
            self.t=round(amount)# change duration only for this countdown
        else:
            self.t=self.amount# use default duration
        self.on=True
        self.ring=False
        self.off=False
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
    def end(self):# force end to timer
        self.on=False
        self.ring=False
        self.off=True
        self.t=0



# BETTER: do timer manager with queries? (creates a new timer object here for each query)

####################################################################################################################
