#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# actor.py: all games actors (hero, enemies, obstacles)
#
# (actors are held in worlds that manages them)
##########################################################
##########################################################

import sys
import os
import pygame
#
import share
import utils
import draw

####################################################################################################################

                        
####################################################################################################################
# Actor Main Templates

# Template for most basic actors
class obj_actor:
    def __init__(self,creator):
        self.creator=creator# created by world
        self.setup()
        self.birth()
    def setup(self):# add here modifications for childs 
        self.type='actor'# type (overwritten for each specific actor)
        self.actortype='None'        
    def birth(self):# add to world
        self.creator.addactor(self)# add self to world list of actors    
    def kill(self):# remove from world
        self.creator.removeactor(self)  
    def update(self,controls):
        pass
        
        
# Template for grand actors in world (hero, items, enemies..., obstacles...)
# A grand actor is more elaborate: 
# - has a hitbox (rd,rx,ry)
# - can have display elements (textbox,image,animation or dispgroup) 
# - can be transformed: movex(),movetox(),scale(),fliph()...,rotate90()
#                       (rotate not done due to enlargen-memory issues)   
class obj_grandactor():
    def __init__(self,creator,xy,scale=1):
        # Creation
        self.creator=creator# created by world
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        # Setup and Birth
        self.setup()
        self.birth()# add self to world ONLY ONCE setup finished
        if scale != 1: self.scale(scale)# scale ONCE setup finished
    def setup(self):# add here modifications for childs 
        self.type='actor'# type (overwritten for each specific actor)
        self.actortype='grandactor'
        # Reference Values (must be defined for any actor)
        self.x=self.xini# actor position for tracking 
        self.y=self.yini
        self.fh=False# flipped horizontally (inverted) or not (original)
        self.fv=False# flipped vertically (inverted) or not (original)
        self.s=1# scaling factor
        self.r=0# rotation angle
        self.rx=50# radius width for rectangle collisions 
        self.ry=50# radius height for rectangle collisions 
        self.rd=50# radius for circle collisions
        #
        # Dictionary of actor elements
        self.dict={}# {elementkey: element object}
        self.dictx={}# relative position of element (conserved)
        self.dicty={}
        self.show=True# display elements or not (can be toggled)
    def birth(self):# add to world
        self.creator.addactor(self)
    def kill(self):# remove from world
        self.creator.removeactor(self)
    def destroy(self):# kill with additional funcionalities (e.g. leave trailing smoke)
        self.kill()
    def addpart(self,name,element):# add element
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )
    def removepart(self,name):# remove element
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
    def movetox(self,x):# 
        self.x=x
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movetoy(self,y):# 
        self.y=y
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def movex(self,dx):# displace actor by dx (as well as all actor elements)
        self.x += dx
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,dy):# displace actor by dy (as well as all actor elements)
        self.y += dy
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def symh(self,name): # shift element horizontally (relative to dispgroup)
        self.dictx[name] *= -1
        self.dict[name].movetox(self.x + self.dictx[name])
    def symv(self,name): # shift element vertically (relative to dispgroup)
        self.dicty[name] *= -1
        self.dict[name].movetoy(self.y + self.dicty[name])
    def fliph(self): # flip group horizontally
        self.fh=not self.fh
        for i in self.dict.keys(): 
            self.dict[i].fliph()
            self.symh(i)  
    def ifliph(self):# flip group horizontally to inverted orientation
        if not self.fh:
            self.fh=True
            for i in self.dict.keys(): 
                self.dict[i].ifliph()
                self.symh(i)                  
    def ofliph(self):# flip group horizontally to original orientation
        if self.fh:
            self.fh=False
            for i in self.dict.keys(): 
                self.dict[i].ofliph()
                self.symh(i)    
    def flipv(self): # flip group vertically
        self.fv=not self.fv
        for i in self.dict.keys(): 
            self.dict[i].flipv()
            self.symv(i) 
    def iflipv(self):# flip group vertically to inverted orientation
        if not self.fv:
            self.fv=True
            for i in self.dict.keys(): 
                self.dict[i].iflipv()
                self.symv(i)   
    def oflipv(self):# flip group vertically to original orientation
        if self.fv:
            self.fv=False
            for i in self.dict.keys(): 
                self.dict[i].oflipv()
                self.symv(i)
    def scale(self,s):# scale actor elements (permanent)
        self.s *= s# update actor scale
        self.rx *= s# scale actorh hitbox (rectx)
        self.ry *= s# (recty)
        self.rd *= s# (circle radius)
        for i in self.dict.keys():
            self.dict[i].scale(s)# scale element
            self.dictx[i] *= s# update element position in dispgroup
            self.dicty[i] *= s
            self.dict[i].movetox(self.x+self.dictx[i])# update element position
            self.dict[i].movetoy(self.y+self.dicty[i])
    def rotate90(self,r):# rotate actor elements in 90 increments (permanent)
        r=int(round(r%360/90,0)*90)# r in 0,90,180,270
        self.r += r
        for i in self.dict.keys():
            self.dict[i].rotate90(r)
            termx,termy=self.dictx[i],self.dicty[i]
            if r==90:
                self.dictx[i],self.dicty[i]=termy,-termx
                self.rx,self.ry=self.ry,self.rx
            elif r==180: 
                self.dictx[i],self.dicty[i]=-termx,-termy
            if r==270:
                self.dictx[i],self.dicty[i]=-termy,termx
                self.rx,self.ry=self.ry,self.rx             
            self.dict[i].movetox(self.x+self.dictx[i])# update element position
            self.dict[i].movetoy(self.y+self.dicty[i])
    def play(self,controls):
        for i in self.dict.values():  i.play(controls)   
    def devtools(self):# display grand actor hit box
        pygame.draw.rect(share.screen,share.colors.devactor, (self.x-self.rx, self.y-self.ry, 2*self.rx,2*self.ry), 3)
    def update(self,controls):
        if self.show: self.play(controls)  
        if share.devmode: self.devtools()


# Template: grand actor with rigidbody fonctionalities
# - rigidbody controls speed u,v inducing additional movement to x,y
# - external forces must be applied to exit stalling. 
# - rigidbody dynamics are not computed if actor is stalling
# - friction slows any rigidbody untils stalls again. 
# - if stalling the actor can still be controlled directly on x,y just like a non-rigidbody
class obj_rbodyactor(obj_grandactor):
    def setup(self):
        super().setup()
        self.actortype="rbody"   #### MUST BE DETERMINED BEFORE BIRTH WHEN ADDS TO WORLD
        self.stalling=True# stalling or not
        self.dt=1# update rate
        self.u=0# rigid body speed
        self.v=0
        self.m=1# mass (must be >0)
        self.d=0.01# dissipation rate
        self.umin2=1# min speed for stalling (squared)
    def forcex(self,force):# apply forcex (call externally)
        self.u += force*self.dt/self.m
        self.stalling=False
    def forcey(self,force):# apply forcey (call externally)
        self.v += force*self.dt/self.m
        self.stalling=False
    def stall(self):# stall rigidbody (can be called externally)
        self.stalling=True
        self.u,self.v=0,0
    def friction(self,d):# apply dissipation internally
        self.u -= d*self.u*self.dt
        self.v -= d*self.v*self.dt        
    def rigidbodyupdate(self):# move from speed
        if self.u**2+self.v**2>self.umin2:
            self.movex(self.u*self.dt)
            self.movey(self.v*self.dt)
            self.friction(self.d)
        else:
            self.stall()
    def update(self,controls):
        super().update(controls)
        if not self.stalling: self.rigidbodyupdate()


####################################################################################################################
# Hero actors

#Template hero (image only)
class obj_actor_hero(obj_rbodyactor):
    def setup(self):
        super().setup()
        self.actortype='hero'# type=hero
        self.weapon=None# attached weapon (must be an object= weapon actor)
        self.rd=100# sphere collision radius
        self.rx=120# rect collisions radius x
        self.ry=100
        self.addpart('img_herolegs_stand',draw.obj_image('herolegs_stand',(self.xini,self.yini+160)))
        self.addpart('img_herohead',draw.obj_image('herohead',(self.xini,self.yini)))


# Hero with basic movement (arrows only) to do tests.
class obj_actor_hero_v0(obj_actor_hero):
    def setup(self):
        super().setup()
        self.move_dx=5# movement amount
        self.move_dy=5
    def controls_move(self,controls):
        if controls.right: self.movex(self.move_dx) 
        if controls.left: self.movex(-self.move_dx)  
        if controls.up: self.movey(-self.move_dy) 
        if controls.down: self.movey(self.move_dy)           
    def update(self,controls):
        super().update(controls)
        self.controls_move(controls)
        
        
# Hero with only legs walking around (remove initial head and legs)
class obj_actor_hero_v1(obj_actor_hero_v0):
    def setup(self):
        super().setup()
        self.removepart('img_herolegs_stand')# remove initial head and legs
        self.removepart('img_herohead')
        dispgroup=draw.obj_dispgroup((self.xini,self.yini))
        animation=draw.obj_animation('herolegs_walk','herolegs_stand',(self.xini,self.yini+160))# start animation
        animation.addimage('herolegs_walk')# add image to list
        dispgroup.addpart("legs_walk",animation)
        animation=draw.obj_animation('herolegs_stand','herolegs_stand',(self.xini,self.yini+160))# standing
        dispgroup.addpart("legs_stand",animation)
        self.addpart("hero_dispgroup",dispgroup)
        #
        self.walking=False# hero is walking or not
        self.facingright=True# hero is facing to the right (False=to the left)
        self.turnright=False# hero is turning to the right
        self.turnleft=False
    def controls_move(self,controls):# overwritten
        if controls.d or controls.a or controls.w or controls.s \
            or controls.right or controls.left or controls.up or controls.down:
            self.walking=True
        else:
            self.walking=False
        self.turnright=False# reset
        self.turnleft=False
        if self.walking:
            self.dict["hero_dispgroup"].dict["legs_walk"].show=True
            self.dict["hero_dispgroup"].dict["legs_stand"].show=False
        else:
            self.dict["hero_dispgroup"].dict["legs_walk"].show=False
            self.dict["hero_dispgroup"].dict["legs_stand"].show=True        
        if controls.d or controls.right: 
            self.movex(self.move_dx) 
            if controls.dc or controls.rightc:
                self.turnright=True
                self.facingright= True
                self.dict["hero_dispgroup"].ofliph()
                self.dict["hero_dispgroup"].dict["legs_walk"].firstframe()# reset to first frame 
        if controls.a or controls.left: 
            self.movex(-self.move_dx)  
            if controls.ac or controls.leftc:
                self.turnleft= True
                self.facingright= False
                self.dict["hero_dispgroup"].ifliph()
                self.dict["hero_dispgroup"].dict["legs_walk"].firstframe()# reset to first frame 
        if controls.w or controls.up: 
            self.movey(-self.move_dy) 
            if controls.wc or controls.upc: 
                self.dict["hero_dispgroup"].dict["legs_walk"].firstframe()# reset to first frame  
        if controls.s or controls.down: 
            self.movey(self.move_dy)        
            if controls.sc or controls.downc: 
                self.dict["hero_dispgroup"].dict["legs_walk"].firstframe()# reset to first frame      


# Hero with only legs walking around, add head
class obj_actor_hero_v2(obj_actor_hero_v1):
    def setup(self):
        super().setup() 
        animation=draw.obj_animation('herohead_basic','herohead',(self.xini,self.yini))
        animation.scale(self.s)
        self.dict["hero_dispgroup"].addpart("head",animation)


# Hero with only heads and legs walking around, add face expressions
class obj_actor_hero_v3(obj_actor_hero_v2):
    def setup(self):
        super().setup() 
        self.timer_quickface=utils.obj_timer(20)# time amount for making face expressions
    def update(self,controls):# add timer and autoresetface to update
        super().update(controls)        
        self.autoresetface()
    def makenormalface(self):# make happy face
        self.dict["hero_dispgroup"].dict["head"].replaceimage('herohead',0)
    def makehappyface(self):# make happy face
        self.dict["hero_dispgroup"].dict["head"].replaceimage('herohead_happy',0)
    def makeangryface(self):# make happy face
        self.dict["hero_dispgroup"].dict["head"].replaceimage('herohead_angry',0)
    def autoresetface(self):# reset face automatically if timer rings
        self.timer_quickface.update()
        if self.timer_quickface.ring: self.makenormalface()
    def quickhappyface(self):# make happy face (temporary)
        self.makehappyface()
        self.timer_quickface.start()# could be run instead
    def quickangryface(self):# make angry face (temporary)
        self.makeangryface()
        self.timer_quickface.start()          

# Hero ... above, add sword with strike        
class obj_actor_hero_v4(obj_actor_hero_v3):
    def setup(self):
        super().setup()
        self.weapon=obj_actor_sword(self,self.creator,(self.xini,self.yini))# attach sword (padre=self)
        # timers for strike
        self.timer_strikeshow=utils.obj_timer(20)# time amount strike on screen
        self.timer_strikereload=utils.obj_timer(30)# time amount to reload a strike
    def update(self,controls):# add timer and autoresetface to update
        super().update(controls)
        self.controls_strike(controls)
        self.autoresetstrike()
        self.autoreloadstrike()
        # self.weapon.show=self.show# only show weapon if show self
    def autoreloadstrike(self):
        self.timer_strikereload.update()
    def autoresetstrike(self):# reset face automatically if timer rings
        self.timer_strikeshow.update()
        if self.timer_strikeshow.ring: self.endstrike()
    def controls_strike(self,controls):
        if (controls.mouse1 and controls.mouse1c) or (controls.space and controls.spacec):
            if self.timer_strikereload.off: # reloaded
                self.startstrike()
                self.quickangryface()
                self.timer_strikereload.start()
    def startstrike(self):
        self.weapon.startstrike()# weapon strikes
        self.timer_strikeshow.start()# could be run instead
    def endstrike(self):
        self.weapon.endstrike()# weapon no longer strikes 
    def scale(self,s):# scaling also scales the weapon
        super().scale(s)
        self.weapon.scale(s)
        self.weapon.xoff *= s# weapon offset to padre=hero
        self.weapon.yoff *= s


####################################################################################################################

        
# Sword actor
# Always attached to a padre (e.g. a hero.)
class obj_actor_sword(obj_grandactor):
    def __init__(self,padre,*args):# call sequence is obj_actor_sword(parent,creator,xy)
        super().__init__(*args)# regular arguments
        self.padre=padre# Always attached to a parent=hero
    def setup(self):
        super().setup()
        self.actortype="sword"
        self.show=True# show entire sword (supersedes show strike)
        self.xoff=240# sword offset respect to padre (if facing right)
        self.yoff=80
        self.rx=180# radius width for rectangle collisions 
        self.ry=100# radius height for rectangle collisions 
        self.rd=0# radius for circle collisions
        self.knockback=5# force of knockback when striking rigidbodies
        term=draw.obj_image('herostrike',(self.xini,self.yini))
        term.show=False# show sword image
        term.scale(self.s)
        self.addpart("strike",term)# add to self
        self.striking=False# sword is striking or not
        self.striking0=False# first frame of striking 
        self.striking1=False# second frame of striking
    def startstrike(self):
        self.striking=True
        self.striking0=True
        if self.show: self.dict["strike"].show=True# show image
    def endstrike(self):
        self.striking=False
        self.dict["strike"].show=False# show image
    def update(self,controls):
        super().update(controls)
        # position/orientation follows padre
        if self.padre.facingright:
            self.x =self.padre.x + self.xoff            
        else:
            self.x =self.padre.x - self.xoff
        self.y= self.padre.y +self.yoff
        self.dict["strike"].x=self.x# image
        self.dict["strike"].y=self.y# image
        if self.padre.turnright: self.dict["strike"].ofliph()# flip image
        if self.padre.turnleft: self.dict["strike"].ifliph()# flip image
        if self.striking:# evolve from first to second frame of striking (for hit detection)
            if self.striking0: 
                self.striking0=False# 
                self.striking1=True
            elif self.striking1:
                self.striking1=False


####################################################################################################################
# Basic Actors (not grandactors, no rigidbody)


# A goal in the game (allows to reach next level, etc...)
class obj_actor_goal(obj_actor):
    def setup(self):
        super().setup()
        self.actortype='goal'
        self.reached=False# reached goal or not


# Goal: collide two actors 
# $ self.goal=actor.obj_actor_goal_collideactors(self.world,(self.hero,self.door),timer=50)
# $ if self.goal.reached:
class obj_actor_goal_collideactors(obj_actor_goal):
    def __init__(self,creator,actors,timer=0):
        super().__init__(creator)
        self.actor1=actors[0]
        self.actor2=actors[1]
        self.timer=timer# actors must collide for >timer to reach goal
    def setup(self):
        super().setup()
        self.t=0# time increment
    def updatecollide(self):
        self.t += 1
        if self.t>self.timer: self.reached=True         
    def resetcollide(self):
            self.t = 0
            self.reached=False
    def update(self,controls):
        super().update(controls)
        if utils.checkrectcollide(self.actor1,self.actor2):
            self.updatecollide()
        else:
            self.resetcollide()


# Goal: hero stands on open door        
# $ self.goal=actor.obj_actor_goal_collideactors(self.world,(self.hero,self.door),timer=50)
# $ if self.goal.reached:
class obj_actor_goal_opendoor(obj_actor_goal_collideactors):
    def updatecollide(self):
        super().updatecollide() 
        if not self.actor2.open: # goal reached only door is open
            self.t = 0
            self.reached=False
            self.actor1.show=True# hide hero
        else:
            self.actor1.show=False# hide hero
    def resetcollide(self):
        super().resetcollide() 
        self.actor1.show=True# hide hero


# Boundary (basic actor)
class obj_actor_bdry(obj_actor):# basic actor
    def __init__(self,creator,bounds=(100,1280-100,100,720-100),push=(3,-3,3,-3)):
        super().__init__(creator)
        self.bdry_lim=bounds# limits (xmin,xmax,ymin,ymax). 
        self.bdry_push=push# push rate at boundaries (if =0, boundary not applied)        
    def setup(self):
        super().setup()
        self.actortype='bdry'


####################################################################################################################
# World 




# Door: open with hit, shuts on a timer
class obj_actor_door(obj_grandactor):# not a rigidbody
    def setup(self):
        super().setup()
        self.actortype='door'
        self.rd=8# small hitbox (must stand right on its)
        self.rx=8
        self.ry=8
        dispgroup=draw.obj_dispgroup((self.xini,self.yini))
        image=draw.obj_image('door_closed',(self.xini,self.yini))
        dispgroup.addpart("image_closed",image)
        image=draw.obj_image('door_open',(self.xini,self.yini))
        image.show=False
        dispgroup.addpart("image_open",image)
        self.addpart("door_dispgroup",dispgroup)
        self.open=False# door is open
    def hit(self): # door is hit (open or close)
        if self.open:
            self.closedoor()
        else:
            self.opendoor()
        self.open = not self.open
    def opendoor(self):
        self.dict["door_dispgroup"].dict["image_closed"].show=False
        self.dict["door_dispgroup"].dict["image_open"].show=True
    def closedoor(self):
        self.dict["door_dispgroup"].dict["image_closed"].show=True
        self.dict["door_dispgroup"].dict["image_open"].show=False  
        
        
####################################################################################################################
# Effects Actors        
     
# trail of smoke when something breaks/dies
# (created by other actors upon kill)
class obj_actor_effects_smoke(obj_grandactor):# grandactor because scaled
    def setup(self):
        super().setup()
        self.actortype='smoke'
        self.addpart("image",draw.obj_image('smoke',(self.xini,self.yini)) )
        self.timer=utils.obj_timer(30)# timer for existence
        self.timer.start()# start timer at creation
    def update(self,controls):
        super().update(controls)
        self.timer.update()
        if self.timer.ring: self.kill()# kill upon timer end
            
        
####################################################################################################################
# Stuff in world
        
# loved item (static)
class obj_actor_item_loved(obj_grandactor):# not a rigidbody
    def setup(self):
        super().setup()
        self.actortype='item_loved'
        self.rd=100
        self.rx=100
        self.ry=100
        dispgroup=draw.obj_dispgroup((self.xini,self.yini))
        image=draw.obj_image('herothings_loved',(self.xini,self.yini))
        textbox=draw.obj_textbox(share.words.dict["itemloved"],(self.xini,self.yini+100),fontsize='big')     
        dispgroup.addpart("image",image)
        dispgroup.addpart("textbox",textbox)
        self.addpart("item_dispgroup",dispgroup)
    def destroy(self):# when destroyed, leave trailing smoke 
        self.kill()# remove from world
        term=obj_actor_effects_smoke(self.creator,(self.x,self.y),scale=self.s)# trailing smoke

        
# hated item (static)
class obj_actor_item_hated(obj_actor_item_loved):# not a rigidbody
    def setup(self):
        super().setup()
        self.actortype='item_hated'
        self.dict["item_dispgroup"].dict["image"].replaceimage('herothings_hated')
        self.dict["item_dispgroup"].dict["textbox"].replacetext(share.words.dict["itemhated"])


# furniture (from chapter 2 hero house)
class obj_actor_furniture_wide(obj_rbodyactor):
    def setup(self):
        super().setup()
        self.actortype='furniture'
        self.rd=200# sphere collision radius
        self.rx=500# rect collisions radius x
        self.ry=100
        self.addpart('img',draw.obj_image('furniture_wide',(self.xini,self.yini)))  
        self.addpart('textbox',draw.obj_textbox(share.words.dict["furniture_wide_name"],(self.xini,self.yini+100),fontsize='big')) 


class obj_actor_furniture_square(obj_rbodyactor):
    def setup(self):
        super().setup()
        self.actortype='furniture'
        self.rd=200# sphere collision radius
        self.rx=200# rect collisions radius x
        self.ry=200
        self.addpart('img',draw.obj_image('furniture_square',(self.xini,self.yini)))
        self.addpart('textbox',draw.obj_textbox(share.words.dict["furniture_square_name"],(self.xini,self.yini+150),fontsize='big'))       

        
class obj_actor_furniture_tall(obj_rbodyactor):
    def setup(self):
        super().setup()
        self.actortype='furniture'
        self.rd=200# sphere collision radius
        self.rx=100# rect collisions radius x
        self.ry=300
        self.addpart('img',draw.obj_image('furniture_tall',(self.xini,self.yini)))
        self.addpart('textbox',draw.obj_textbox(share.words.dict["furniture_tall_name"],(self.xini,self.yini+200),fontsize='big'))
    

    