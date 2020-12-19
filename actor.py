#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# actor.py: all games actors (hero, enemies, obstacles, world...)
#
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
# World
#* WORLD

# World Template
class obj_world:
    def __init__(self,creator):
        self.creator=creator# created by scene
        self.ruledict={}# dictionary of rules in the world (non-ordered)
        self.actorlist=[]# list of actors in the world (ordered for updates)
        self.setup()
    def setup(self):# fill here for childs
        pass
    def addrule(self,name,rule):# add rule to the world
        self.ruledict[name]=rule
        for i in self.actorlist: self.addactortorule(rule,i)# add all actors to rule
    def removerule(self,name):# remove rule from the world
        self.ruledict.pop(name,None)# removes element if exists (returns None otherwise)        
    def addactor(self,actor):# add actor to the world
        self.actorlist.append(actor)
        for i in self.ruledict.values(): self.addactortorule(i,actor)# add actor to all rules
    def removeactor(self,actor):# remove actor from the world
        if actor in self.actorlist:
            self.actorlist.remove(actor)
        for i in self.ruledict.values(): self.removeactorfromrule(i,actor)# remove actor from all rules
    def addactortorule(self,rule,actor):# add an actor to a rule as a subject (if type matches)
        for i,j in rule.subject_types.items():
            if actor.type in j: # if actor type matches an accepted actor type
                if actor not in rule.subjects[i]:# if actor not already a rule subject
                    rule.subjects[i].append(actor)# add actor as subject to rule
    def removeactorfromrule(self,rule,actor):# remove an actor from a rule (if type matches)
        for i,j in rule.subject_types.items():
            if actor.type in j: # if actor type matches an accepted actor type
                if actor in rule.subjects[i]:# if actor a rule subject
                    rule.subjects[i].remove(actor)# remove actor  
    def update(self,controls):
        for i in self.ruledict.values(): i.update(controls)# update rules
        for j in self.actorlist: j.update(controls)# update actors

# World with rule boundary conditions
class obj_world_v1(obj_world):
    def setup(self):
        self.addrule('rule_world_bdry', obj_rule_world_bdry(self))# add rule collision with boundaries


# version with rule hero collects items
class obj_world_v2(obj_world_v1):
    def setup(self):
        super().setup()
        self.addrule('rule_hero_collects_item', obj_rule_hero_collects_item(self))# rule collision hero loved item

# version with rule weapon breaks stuff
class obj_world_v3(obj_world_v2):
    def setup(self):
        super().setup()
        self.addrule('rule_weapon_breaks_stuff', obj_rule_weapon_breaks_stuff(self))# rule collision hero loved item
        

####################################################################################################################
# World Rules
# *RULES
# Each update, a rule is applied to its subjects (that are actors from the world)
# Subjects have different types:
# rule.subject_types["subjects_heros"]=["hero"], actors with actor.type=hero become subjects with type "subjects_hero"
# The rule checks interactions between subjects and modifies accordingly depending on their types
# For example, a rule for collision between actors "hero" and actors "items": 
# All subjects with type "hero" pick up all subjects with type "items", if they collide.

# Rule Template
class obj_rule:
    def __init__(self,creator):
        self.creator=creator# created by world
        #
        self.setupstart()
        self.setup()# edit for childs
        self.setupend()
    def setupstart(self):
        self.subject_types={}# subject types for the rule 
    def setup(self):# edit for childrens
        pass
    def setupend(self):
        self.subjects={key: [] for key in self.subject_types}# lists of subject ordered by key=subject type
    def update(self,controls):# edit for childrens
        pass

# Rule: boundary conditions (pushes back actors)
# NEED TO MAKE THE BOUNDARIES AN ACTOR (SUCH THAT CAN BE TWEAKED)
class obj_rule_world_bdry(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_collider_with_bdry"]=["hero"]# actors that collide
        # rule parameters
        self.bdry=(100,1180,0,560)# world boundaries tuple=(xmin,xmax,ymin,ymax)
        self.dxbdry=3# push rate at boundaries
        self.dybdry=3
    def update(self,controls):
        for i in self.subjects["subjects_collider_with_bdry"]:# subjects that collide with bdry
            if i.x<self.bdry[0]: 
                i.movex(self.dxbdry)
            elif i.x>self.bdry[1]:
                i.movex(-self.dxbdry)
            if i.y<self.bdry[2]: 
                i.movey(self.dybdry)
            elif i.y>self.bdry[3]:
                i.movey(-self.dxbdry)             


# Rule: hero collects items
# when: collision loved, then: hero makes quickhappyface, picks up item
# when: collision hated, then: hero makes angryface
class obj_rule_hero_collects_item(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_hero"]=["hero"]# hero
        self.subject_types["subjects_item_loved"]=["item_loved"]# loved items
        self.subject_types["subjects_item_hated"]=["item_hated"]# hated items
    def update(self,controls):
        for i in self.subjects["subjects_hero"]:
            for j in self.subjects["subjects_item_loved"]:
                if utils.checkrectcollide(i,j):
                    i.quickhappyface()# hero happy briefly
                    j.kill()# item disappears (pickup)
            for j in self.subjects["subjects_item_hated"]:
                if utils.checkrectcollide(i,j):
                    i.quickangryface()# hero angry briefly

# Rule: weapon breaks stuff
# when: collision with item then: destroy item
class obj_rule_weapon_breaks_stuff(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_weapon"]=["sword"]# hero
        self.subject_types["subjects_stuff"]=["item_loved","item_hated"]# loved items
    def update(self,controls):
        for i in self.subjects["subjects_weapon"]:
            if i.striking0 or i.striking1:# if weapon is striking (first or second frame only)
                for j in self.subjects["subjects_stuff"]:
                    if utils.checkrectcollide(i,j):
                        j.destroy()# item is destroyed (kill+possible effect e.g. smoke)
                        
####################################################################################################################
# Actor

# Template for any actor in world (hero, items, enemies..., obstacles...)
# Actor can have elements (textbox,image,animation or dispgroup) 
# All elements must have foncitonalities:
#  self.x, self.y: position
# self.movex(), movey(), movetox(), movetoy()
# self.fliph(), self.flipv() (and oflip, iflip...)
# self.scale()
# self.rotate()
class obj_actor:
    def __init__(self,creator,xy):
        # Creation
        self.creator=creator# created by world
        self.type='None'# type of actor (hero,item...): determines interactions with rules       
        #
        # Reference Values (must be defined for any actor)
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.x=self.xini# actor position for tracking 
        self.y=self.yini
        self.s=1# scaling factor
        self.r=0# rotation angle
        self.rx=0# radius width for rectangle collisions 
        self.ry=0# radius height for rectangle collisions 
        self.rd=0# radius for circle collisions
        self.move_dx=5# movement amount
        self.move_dy=5
        #
        # Dictionary of actor elements (embedded actors, images/animations/dispgroups)
        self.dict={}
        self.dictx={}# relative position of element (conserved)
        self.dicty={}
        #
        # Booleans for behavior (must be defined)
        self.show=True# show actor (can be toggled on/off)
        #
        # Setup and Birth
        self.setup()
        self.birth()# add self to world ONLY ONCE setup finished
        #
    def setup(self):# add here modifications for childs 
        pass
    def birth(self):# add to world
        self.creator.addactor(self)# add self to world list of actors    
    def kill(self):# remove from world
        self.creator.removeactor(self)
    def destroy(self):# kill with additional funcionalities (e.g. leave trailing smoke)
        self.kill()
    def addpart(self,name,element):# add element to actor dictionary (embedded actor, image,animation or dispgroup...)
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )# record relative difference        
    def removepart(self,name):# remove element
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)# removes element if exists (returns None otherwise)
    def movetox(self,x):# 
        self.x=x
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movetoy(self,y):# 
        self.y=y
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def movex(self,dx):# displace actor by dx (as well as all actor elements)
        self.x += dx
        # for i in self.dict.values(): i.movex(dx)# old translation
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,dy):# displace actor by dy (as well as all actor elements)
        self.y += dy
        # for i in self.dict.values(): i.movey(dy)# old translation
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])

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
    def play(self,controls):
        for i in self.dict.values():  i.play(controls)   
    def devtools(self):# display hit box
        pygame.draw.rect(share.screen,share.colors.devactor, (self.x-self.rx, self.y-self.ry, 2*self.rx,2*self.ry), 3)
    def update(self,controls):
        if self.show: self.play(controls)  
        if share.devmode: self.devtools()
        
####################################################################################################################
# Hero Actor
# *ACTORS
# Note: the creator for any actor is the world they are in

#Template hero (no image)
class obj_actor_hero(obj_actor):
    def setup(self):
        self.type='hero'# type=hero
        self.apply_controls_move=True# actor can be moved with WASD or arrows
        self.show=True# show actor images/anim (can be toggled on/off)
        self.weapon=None# attached weapon (must be an object= weapon actor)
        self.move_dx=5# movement amount
        self.move_dy=5
        self.rd=100# sphere collision radius
        self.rx=100# rect collisions radius x
        self.ry=100
    def controls_move(self,controls):
        if controls.d or controls.right: self.movex(self.move_dx) 
        if controls.a or controls.left: self.movex(-self.move_dx)  
        if controls.w or controls.up: self.movey(-self.move_dy) 
        if controls.s or controls.down: self.movey(self.move_dy)           
    def update(self,controls):
        super().update(controls)
        if self.apply_controls_move: self.controls_move(controls)
  
    
# Hero with only legs walking around
class obj_actor_hero_v1(obj_actor_hero):
    def setup(self):
        super().setup()
        #
        self.s=1# scaling factor
        dispgroup=draw.obj_dispgroup((self.xini,self.yini))
        animation=draw.obj_animation('herolegs_walk','herolegs_stand',(self.xini,self.yini+160))# start animation
        animation.addimage('herolegs_walk')# add image to list
        animation.scale(self.s)
        dispgroup.addpart("legs_walk",animation)
        #
        animation=draw.obj_animation('herolegs_stand','herolegs_stand',(self.xini,self.yini+160))# standing
        animation.scale(self.s)
        dispgroup.addpart("legs_stand",animation)
        self.addpart("hero_dispgroup",dispgroup)
        #
        self.walking=False# hero is walking or not
        self.facingright=True# hero is facing to the right (False=to the left)
        self.turnright=False# hero is turning to the right
        self.turnleft=False
    def controls_move(self,controls):# rewrite move function
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

        
# Weapon Actor: sword :
# Always attached to a padre (e.g. a hero.)
class obj_actor_sword(obj_actor):
    def __init__(self,padre,*args):# call sequence is obj_actor_sword(parent,creator,xy)
        super().__init__(*args)# regular arguments
        self.padre=padre# Always attached to a parent=hero
    def setup(self):
        self.type="sword"
        self.xoff=240# sword offset respect to padre (if facing right)
        self.yoff=80
        self.rx=180# radius width for rectangle collisions 
        self.ry=100# radius height for rectangle collisions 
        self.rd=0# radius for circle collisions 
        self.s=1# scaling
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
        self.dict["strike"].show=True# show image
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
# Effects Actors        
     
# trail of smoke when something breaks/dies
# (created by other actors upon kill)
class obj_actor_effects_smoke(obj_actor):
    def setup(self):
        self.type='smoke'
        image=draw.obj_image('smoke',(self.xini,self.yini))
        self.s=0.5
        image.scale(self.s)
        self.addpart("image",image)
        self.timer=utils.obj_timer(30)# timer for existence
        self.timer.start()# start timer at creation
    def update(self,controls):
        super().update(controls)
        self.timer.update()
        if self.timer.ring: self.kill()# kill upon timer end
            
        
####################################################################################################################
# Items Actors
        
# loved item (static)
class obj_actor_item_loved(obj_actor):
    def setup(self):
        self.type='item_loved'
        self.rd=50
        self.rx=50
        self.ry=50
        self.image1=draw.obj_image('herothings_loved',(self.xini,self.yini))
        self.s=0.5
        self.image1.scale(self.s)
        self.addpart("image",self.image1)
        self.dict["image"].legend=share.words.dict["itemloved"]
    def destroy(self):# when destroyed, leave trailing smoke 
        self.kill()# remove from world
        term=obj_actor_effects_smoke(self.creator,(self.x,self.y))# trailing smoke
        
# hated item (static)
class obj_actor_item_hated(obj_actor_item_loved):
    def setup(self):
        super().setup()
        self.type='item_hated'
        self.dict["image"].replaceimage('herothings_hated')
        self.dict["image"].legend=share.words.dict["itemhated"]
