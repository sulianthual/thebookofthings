#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# world.py: all games worlds and rules
#
# (every world can hold rules and actors that it manages)
##########################################################
##########################################################

import sys
import os
import pygame
#
import share
import utils
import draw
import actor

####################################################################################################################
# World
#* WORLD


# World Template
class obj_world:
    def __init__(self,creator):
        self.type='world'
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
            if actor.actortype in j: # if actor type matches an accepted actor type
                if actor not in rule.subjects[i]:# if actor not already a rule subject
                    rule.subjects[i].append(actor)# add actor as subject to rule
    def removeactorfromrule(self,rule,actor):# remove an actor from a rule (if type matches)
        for i,j in rule.subject_types.items():
            if actor.actortype in j: # if actor type matches an accepted actor type
                if actor in rule.subjects[i]:# if actor a rule subject
                    rule.subjects[i].remove(actor)# remove actor  
    def update(self,controls):
        for i in self.ruledict.values(): i.update(controls)# update rules
        for j in self.actorlist: j.update(controls)# update actors

# world chapter I
class obj_world_ch1(obj_world):
    def setup(self):
        super().setup()
        bdry=actor.obj_actor_bdry(self)# default boundaries
        self.addrule('rule_world_bdry', obj_rule_world_bdry(self))# add rule collision with boundaries
        self.addrule('rule_hero_collects_item', obj_rule_hero_collects_item(self))# rule collision hero loved item
        self.addrule('rule_weapon_breaks_stuff', obj_rule_weapon_breaks_stuff(self))# rule collision hero loved item


# world chapter II (boundaries must be specified each page)
class obj_world_ch2(obj_world):
    def setup(self):
        super().setup()
        self.addrule('bdry_bounces_rigidbody', obj_rule_bdry_bounces_rigidbody(self))#bdry collision for rigidbodies
        self.addrule('rule_hero_collects_item', obj_rule_hero_collects_item(self))# rule collision hero loved item
        self.addrule('rule_weapon_breaks_stuff', obj_rule_weapon_breaks_stuff(self))# rule collision hero loved item
        self.addrule('rule_weapon_door', obj_rule_weapon_opens_door(self))# weapon opens/closes door
        self.addrule('weapon_strikes_rigidbody', obj_rule_weapon_strikes_rigidbody(self) )


####################################################################################################################
# World Rules
# *RULES
# a rule exists in a world, and has subjects that are actors in the world
# Each world update, the rule is applied to its subjects
# To determine if an actor is subject to a rule, use matching actor types.
# $ rule.subject_types["subjects_heros"]=["hero"].
# $ rule.subject_types["subjects_items"]=["item"]
# Then All subjects with type "hero" pick up all subjects with type "items", if they collide.


# Rule Template
class obj_rule:
    def __init__(self,creator):
        self.type='rule'
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


# Rule: boundary conditions (pushes back any grand actor)
class obj_rule_world_bdry(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_collider_with_bdry"]=["hero","furniture"]# actors that collide
        self.subject_types["subjects_bdry"]=["bdry"]# boundaries
    def update(self,controls):
        for i in self.subjects["subjects_bdry"]:        
            for j in self.subjects["subjects_collider_with_bdry"]:# subjects that collide with bdry
                if j.x<i.bdry_lim[0]: 
                    j.movex(i.bdry_push[0])
                elif j.x>i.bdry_lim[1]:
                    j.movex(i.bdry_push[1])
                if j.y<i.bdry_lim[2]: 
                    j.movey(i.bdry_push[2])
                elif j.y>i.bdry_lim[3]:
                    j.movey(i.bdry_push[3])              


# Rule: boundary conditions (inverts speed to inwards for any actor with rigidbody)
# actors must have rigidbody fonctionalities!
class obj_rule_bdry_bounces_rigidbody(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_collider_with_bdry"]=["hero","furniture"]# rigidbody actors only!
        self.subject_types["subjects_bdry"]=["bdry"]# boundaries
    def update(self,controls):
        for i in self.subjects["subjects_bdry"]:        
            for j in self.subjects["subjects_collider_with_bdry"]:# subjects that collide with bdry
                if j.x<i.bdry_lim[0]: 
                    j.movex(i.bdry_push[0])
                    if j.u<0: j.u *= -1
                elif j.x>i.bdry_lim[1]:
                    j.movex(i.bdry_push[1])
                    if j.u>0: j.u *= -1
                if j.y<i.bdry_lim[2]: 
                    j.movey(i.bdry_push[2])
                    if j.v<0: j.v *= -1
                elif j.y>i.bdry_lim[3]:
                    j.movey(i.bdry_push[3])
                    if j.v>0: j.v *= -1

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


# Rule: weapon opens door
# when: collision with door then: opendoor
class obj_rule_weapon_opens_door(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_weapon"]=["sword"]# hero
        self.subject_types["subjects_door"]=["door"]# loved items
    def update(self,controls):
        for i in self.subjects["subjects_weapon"]:
            if i.striking0:# if weapon is striking (first frame only)
                for j in self.subjects["subjects_door"]:
                    if utils.checkrectcollide(i,j):
                        j.hit()# door is hit


# Rule: weapon strikes rigidbody 
# when: collision weapon with rigidbody then: apply knockback force to rigidbody
class obj_rule_weapon_strikes_rigidbody(obj_rule):
    def setup(self):
        # rule subjects 
        self.subject_types["subjects_weapon"]=["sword"]
        self.subject_types["subjects_rigidbody"]=["furniture"]
    def update(self,controls):
        for i in self.subjects["subjects_weapon"]:
            if i.striking0:# if weapon is striking (first frame only)
                for j in self.subjects["subjects_rigidbody"]:
                    if utils.checkrectcollide(i,j):
                        # theta=utils.atan2( j.y-i.y, j.x-i.x )
                        # theta=utils.angle( (i.x,i.y),(j.x,j.y) )
                        theta=utils.actorsangle( i,j )
                        j.forcex(i.knockback*utils.cos(theta))
                        j.forcey(i.knockback*utils.sin(theta))
                    
                    
                    
                    
                    
                    
                    

####################################################################################################################                    
                    







