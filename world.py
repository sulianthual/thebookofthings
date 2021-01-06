#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# world.py: all games worlds and rules
#
# (every world can hold rules and actors that it manages)
##########################################################
##########################################################

import share
import tool
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
    def addrule(self,name,rule):# add rule to the world (name must match object name!)
        self.ruledict[name]=rule
        for i in self.actorlist: rule.addactor(i)
    def removerule(self,name):# remove rule from the world
        self.ruledict.pop(name,None)# removes element if exists (returns None otherwise)
    def addactor(self,actor):# add actor to the world
        self.actorlist.append(actor)
        for i in self.ruledict.values(): i.addactor(actor)
    def removeactor(self,actor):# remove actor from the world
        if actor in self.actorlist: self.actorlist.remove(actor)
        for i in self.ruledict.values(): i.removeactor(actor)
    def update(self,controls):
        for i in self.ruledict.values(): i.update(controls)# update rules
        for j in self.actorlist: j.update(controls)# update actors


# world chapter I
class obj_world_ch1(obj_world):
    def setup(self):
        super().setup()
        bdry=actor.obj_actor_bdry(self)# default boundaries
        self.addrule('rule_world_bdry', obj_rule_bdry_bounces_rigidbody(self))# add rule collision with boundaries
        self.addrule('rule_hero_collects_item', obj_rule_hero_collects_item(self))# rule collision hero loved item
        self.addrule('rule_weapon_hits_stuff', obj_rule_weapon_hits_stuff(self))# rule collision hero loved item


# world chapter II (boundaries must be specified each page)
class obj_world_ch2(obj_world):
    def setup(self):
        super().setup()
        self.addrule('bdry_bounces_rigidbody', obj_rule_bdry_bounces_rigidbody(self))#bdry collision for rigidbodies
        self.addrule('rule_hero_collects_item', obj_rule_hero_collects_item(self))# rule collision hero loved item
        self.addrule('rule_weapon_hits_stuff', obj_rule_weapon_hits_stuff(self))# rule collision hero loved item
        self.addrule('critterweapon_strikes_rigidbody', obj_rule_critterweapon_strikes_rigidbody(self) )
        self.addrule('weapon_strikes_rigidbody', obj_rule_weapon_strikes_rigidbody(self) )
        self.addrule('hero_alerts_critter', obj_rule_hero_alerts_critter(self) )
        self.addrule('rule_critter_follows_hero', obj_rule_critter_follows_hero(self) )
        self.addrule('obj_rule_wall_cant_through', obj_rule_wall_cant_through(self) )







####################################################################################################################
# World Rules
# *RULES
# a rule exists in a world, and has subjects that are actors in the world
# Each world update, the rule is applied to its subjects
# To determine if an actor is subject to a rule, use matching actor types.
# $ rule.subject_types["subjects_heros"]=["hero"].
# $ rule.subject_types["subjects_items"]=["item"]
# Then All subjects with type "hero" pick up all subjects with type "items", if they collide.


# WARNING !
# checkrectcollide is ran for each active rule to chekc collision between actors.
# This can lead to performance issues if many calls (in 2**N where N is the number of actors)
# Avoid duplicate calls:
# -write rules that are always for the ENTIRE interaction between a pair of actors.

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
    def isactive(self):# determine if rule needs to be checked on (edit for childrens)
        return True
    def addactor(self,actor):#add actor as potential subject
        for i,j in self.subject_types.items():
            if actor.actortype in j: # actor type matches an accepted actor type
                if actor not in self.subjects[i]:# actor not already a subject
                    self.subjects[i].append(actor)# add actor as subject to rule
    def removeactor(self,actor):# remove actor from all subject lists
        for i,j in self.subject_types.items():
            if actor.actortype in j: # if actor type matches an accepted actor type
                if actor in self.subjects[i]:# if actor a rule subject
                    self.subjects[i].remove(actor)# remove actor
    def update(self,controls):# edit for childrens
        pass

####################################################################################################################
# Physics Rules

# Rule: boundary conditions on grand actors (that have rigidbodies)
# when: collision then: pushes back and orients rigidbody speed inwards
class obj_rule_bdry_bounces_rigidbody(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["scolliders"]=["hero","furniture","rbody","critter"]# rigidbody actors only!
        self.subject_types["sbdry"]=["bdry"]# boundaries
    def update(self,controls):
        for i in self.subjects["sbdry"]:
            for j in self.subjects["scolliders"]:# subjects that collide with bdry
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

# cant go through walls
class obj_rule_wall_cant_through(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["scolliders"]=["hero","furniture","rbody","critter"]
        self.subject_types["swall"]=["wall"]
    def update(self,controls):
        for i in self.subjects["swall"]:
            for j in self.subjects["scolliders"]:
                if tool.checkrectcollide(i,j):
                    if i.rx==0:# (a wall is a line with rx or ry=0)
                        if j.x>i.x:
                            j.movex(i.x+i.rx-j.x+j.rx)
                        else:
                            j.movex(i.x-i.rx-j.x-j.rx)
                    elif i.ry==0:
                        if j.y>i.y:
                            j.movey(i.y+i.ry-j.y+j.ry)
                        else:
                            j.movey(i.y-i.ry-j.y-j.ry)

####################################################################################################################
# Item Rules

# Rule: hero collects items
# hero: self.inventory (=obj_actor_inventory)
# item: self.kill(), self.inventoryicon (image), self.inventoryname(text)
class obj_rule_hero_collects_item(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["shero"]=["hero"]# hero
        self.subject_types["sitem_happy"]=["item_loved","doorkey"]# items
        self.subject_types["sitem_angry"]=["item_hated"]# items
    def update(self,controls):
        for i in self.subjects["shero"]:
            for j in self.subjects["sitem_happy"]:
                if tool.checkrectcollide(i,j):
                    i.quickhappyface()# hero happy briefly
                    j.kill()# item disappears (pickup)
                    i.inventory.additem(j.inventoryname,j.inventoryicon)
            for j in self.subjects["sitem_angry"]:
                if tool.checkrectcollide(i,j):
                    i.quickangryface()# hero angry briefly
                    j.kill()# item disappears (pickup)
                    i.inventory.additem(j.inventoryname,j.inventoryicon)




####################################################################################################################
# Weapon Rules

# Rule: weapon hits stuff
# when: collision with item then: calls hit function
class obj_rule_weapon_hits_stuff(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["sweapon"]=["sword"]# hero
        self.subject_types["sstuff"]=["door","doorwithlock","pot","critter"]
    def update(self,controls):
        for i in self.subjects["sweapon"]:
            if i.striking0:# if weapon is striking (first frame only)
                for j in self.subjects["sstuff"]:
                    if tool.checkrectcollide(i,j):
                        j.hit(i)


# Rule: hero weapon strikes rigidbody
# when: collision weapon with rigidbody then: apply knockback force to rigidbody
class obj_rule_weapon_strikes_rigidbody(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["sweapon"]=["sword"]
        self.subject_types["srbody"]=["rbody","furniture","critter"]
    def update(self,controls):
        for i in self.subjects["sweapon"]:
            if i.striking0:# if weapon is striking (first frame only)
                for j in self.subjects["srbody"]:
                    if tool.checkrectcollide(i,j):
                        theta=tool.actorsangle( i,j )
                        j.forcex(i.knockback*tool.cos(theta))
                        j.forcey(i.knockback*tool.sin(theta))


# Rule: critter weapons strike rigidbody (and is destroyed in the process)
# when: collision weapon with rigidbody then: apply knockback force to rigidbody
# Needs: i.knockback i.hitbox j.hitbox
class obj_rule_critterweapon_strikes_rigidbody(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["sweapon"]=["critterspit"]
        self.subject_types["srbody"]=["hero","furniture"]
    def update(self,controls):
        for j in self.subjects["srbody"]:
            for i in self.subjects["sweapon"]:
                if tool.checkrectcollide(i,j):
                    theta=tool.actorsangle( i,j )
                    j.forcex(i.knockback*tool.cos(theta))
                    j.forcey(i.knockback*tool.sin(theta))
                    j.hit(i)
                    i.hit(j)
                    break






####################################################################################################################
# Critter Rules

# Rule: hero in the world alerts critters if in their vision field
# when critter state=patrol and within radius, critter starts alert state
class obj_rule_hero_alerts_critter(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["shero"]=["hero"]
        self.subject_types["scritter"]=["critter"]
    def update(self,controls):
        if self.subjects["shero"] and self.subjects["scritter"]:
            for i in self.subjects["shero"]:
                for j in self.subjects["scritter"]:
                    if j.state["patrol"]:
                        if not j.visionrd or tool.checkdistance(i,j,j.visionrd):
                            j.startalert()

# Rule: critters follow the hero (unless they patrol)
class obj_rule_critter_follows_hero(obj_rule):
    def setup(self):
        # rule subjects
        self.subject_types["shero"]=["hero"]
        self.subject_types["scritter"]=["critter"]
    def update(self,controls):
        if self.subjects["shero"] and self.subjects["scritter"]:
            for i in self.subjects["shero"]:
                for j in self.subjects["scritter"]:
                    if j.state["follow"]:
                        j.bfliph(i.x>j.x)
                        j.aimr=tool.actorsangle(j,i)# aims at hero



####################################################################################################################
