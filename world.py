#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# world.py: worlds and rules for mini-games
#
# (every world can hold rules and actors that it manages)
# add a world with actors to a page if complex interactions between actors are necessary
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


####################################################################################################################
# World Rules
# *RULES
# a rule exists in a world, and has subjects that are actors in the world
# Each world update, the rule is applied to its subjects
# To determine if an actor is subject to a rule, use matching actor types.
# $ rule.subject_types["subjects_heros"]=["hero"].
# $ rule.subject_types["subjects_items"]=["item"]
# Then All subjects with type "hero" pick up all subjects with type "items", if they collide.


# waarning !
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
        self.subject_types["scolliders"]=["rbody"]# rigidbody actors only!
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


####################################################################################################################

# Mini Game: Wake Up Hero
class obj_world_wakeup(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        # bed frame
        bed=actor.obj_grandactor(self,(440,500))
        bed.addpart( 'img',draw.obj_image('bed',(440,500),scale=0.75) )
        # text
        self.text1=actor.obj_grandactor(self,(840,500))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Hold [W] to Wake up',(1100,480)) )
        self.text2=actor.obj_grandactor(self,(840,500))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Good Morning!',(1100,480)) )
        # three actors for hero: sleep, wake, awake (toggle show between each)
        self.herostate='sleep'
        self.timer=tool.obj_timer(100)
        self.hero_sleep=actor.obj_grandactor(self,(640,360))
        self.hero_sleep.addpart( 'img_asleep',draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.hero_wake=actor.obj_grandactor(self,(640,360))
        self.hero_wake.addpart( 'anim_awakes',draw.obj_animation('ch1_heroawakes','herobase',(640,360),scale=0.7) )
        self.hero_awake=actor.obj_grandactor(self,(640,360))
        self.hero_awake.addpart( 'img_awake',draw.obj_image('herobase',(903,452),scale=0.7) )
        #
        self.hero_sleep.show=True
        self.hero_wake.show=False
        self.hero_awake.show=False
        self.text1.show=True
        self.text2.show=False
        # short timer to finish game
        self.timerend=tool.obj_timer(80)
    def update(self,controls):
        super().update(controls)
        if self.herostate=='sleep':
            self.hero_sleep.show=True
            self.hero_wake.show=False
            self.hero_awake.show=False
            self.text1.show=True
            self.text2.show=False
            if controls.w:
                self.herostate='wake'
                self.hero_wake.dict['anim_awakes'].rewind()
                self.timer.start()# reset timer
        elif self.herostate=='wake':
            self.hero_sleep.show=False
            self.hero_wake.show=True
            self.hero_awake.show=False
            self.text1.show=True
            self.text2.show=False
            self.timer.update()
            if not controls.w: self.herostate='sleep'
            if self.timer.ring:
                self.herostate='awake'
                self.timerend.start()
        elif self.herostate=='awake':
            self.hero_sleep.show=False
            self.hero_wake.show=False
            self.hero_awake.show=True
            self.text1.show=False
            self.text2.show=True
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame



####################################################################################################################

# Mini Game: Fishing
class obj_world_fishing(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        # hook
        self.hook=actor.obj_grandactor(self,(640,100))
        self.hook.actortype='hook'
        self.hook.rx=30
        self.hook.ry=30
        self.hook.r=30
        self.hook.addpart( 'line',draw.obj_image('hookline',(640,100-390)) )
        self.hook.addpart( 'img_fish',draw.obj_image('fish',(640,100+50),scale=0.25,rotate=-90) )
        self.hook.dict['img_fish'].show=False
        self.hook.addpart( 'img_hook',draw.obj_image('hook',(640,100),scale=0.25) )
        self.dydown=5
        self.dyup=2
        # fish status
        self.fishfree=True# fish not caugth (yet)
        # fish animation
        self.fish=actor.obj_grandactor(self,(640,360))
        self.fish.addpart( 'anim_fish',draw.obj_animation('fishmove1','fish',(640,360),imgscale=0.25) )
        # fish hit box
        self.fishbox=actor.obj_grandactor(self,(340,360))
        self.fishbox.actortype='fish'
        self.fishbox.rx=30
        self.fishbox.ry=30
        self.fishbox.r=30
        # short timer at end
        self.timerend=tool.obj_timer(100)
        # textbox when caught
        self.text1=actor.obj_grandactor(self,(840,500))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Hold [S] to lower Hook',(1100,480)) )
        self.text2=actor.obj_grandactor(self,(840,500))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Nice Catch!',(1100,480)) )
        self.text1.show=True
        self.text2.show=False
    def update(self,controls):
        super().update(controls)
        # hook
        if controls.s and self.fishfree:
            if self.hook.y<720-50: self.hook.movey(self.dydown)
        else:
            if self.hook.y>0+50: self.hook.movey(-self.dyup)
        # fish swims:
        if self.fishfree:
            # fish box
            self.fishbox.x=self.fish.dict['anim_fish'].devxy[0]# hitbox follows animation
            self.fishbox.y=self.fish.dict['anim_fish'].devxy[1]
            # check collision
            if tool.checkrectcollide(self.hook,self.fishbox):
                self.fishbox.kill()# hitbox
                self.fish.kill()# fish swimming
                self.text1.show=False
                self.text2.show=True
                self.hook.dict['img_fish'].show=True
                self.timerend.start()
                self.fishfree=False
        else:
            # end of mini-game
            self.timerend.update()
            if self.timerend.ring:
                self.done=True


####################################################################################################################


# Mini Game: Eat Fish
class obj_world_eatfish(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        self.doneeating=False# done eating
        self.bites=20# total number of bites
        self.alternate_LR=True# alternate Left-Right pattern to eat
        self.eating=False
        # fish
        self.fish=actor.obj_grandactor(self,(640,360))
        self.fishscale=1# initial size of fish
        self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,400), scale=self.fishscale,rotate=-45) )
        # hero eating or not eating
        self.herostand=actor.obj_grandactor(self,(640,360))
        self.herostand.addpart( 'img_stand',draw.obj_image('herobase',(340,400), scale=0.7) )
        self.heroeat=actor.obj_grandactor(self,(640,360))
        self.animation1=draw.obj_animation('ch1_heroeats1','herobase',(640,360),imgscale=0.7)
        self.heroeat.addpart('anim_eat', self.animation1)
        self.herostand.show=True
        self.heroeat.show=False
        # text
        self.text1=actor.obj_grandactor(self,(640,360))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Pound [A] and [S] to Eat',(640,660)) )
        self.text2=actor.obj_grandactor(self,(640,360))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Burp!',(800,390)) )
        self.text1.show=True
        self.text2.show=False
        # textbox images
        self.text3=actor.obj_grandactor(self,(640,360))
        if False:
            textbox=draw.obj_textbox("crunch",(640,360))
            textbox.snapshot('says_crunch',path='premade')
            textbox=draw.obj_textbox(" ",(640,360))
            textbox.snapshot('says_empty',path='premade')
            textbox=draw.obj_textbox("miam",(640,360))
            textbox.snapshot('says_miam',path='premade')
            textbox=draw.obj_textbox("gulp",(640,360))
            textbox.snapshot('says_gulp',path='premade')
        self.animation2=draw.obj_animation('ch1_eatsounds','says_crunch',(360,360),sync=self.animation1,path='premade')
        self.animation2.addimage('says_miam')
        self.animation2.addimage('says_gulp')
        self.animation2.addimage('says_empty')
        self.text3.addpart('anim_eatsounds', self.animation2)
        self.text3.show=False
        # timer for eating
        self.timer=tool.obj_timer(50)
        # short timer after done eating
        self.timerend=tool.obj_timer(100)
    def eatfood(self):
        self.eating=True
        self.timer.start()
        self.bites -=1
        self.fishscale *= 0.98
        self.fish.removepart( 'img_fish')
        self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,400), scale=self.fishscale,rotate=-45) )
    def update(self,controls):
        super().update(controls)
        if not self.doneeating:
            if self.alternate_LR:
                if controls.a and controls.ac:
                    self.eatfood()
                    self.alternate_LR=False
            else:
                if controls.d and controls.dc:
                    self.eatfood()
                    self.alternate_LR=True
            if self.eating:
                self.herostand.show=False
                self.heroeat.show=True
                self.text3.show=True
                self.timer.update()# stop eating on timer
                if self.timer.ring:
                    self.eating=False
                    self.animation2.rewind()
                    self.animation1.rewind()
            else:
                self.herostand.show=True
                self.heroeat.show=False
                self.text3.show=False
            if self.bites<1:
                self.doneeating=True
                self.timerend.start()
        else:# done eating
            self.herostand.show=True
            self.heroeat.show=False
            self.fish.show=False
            self.text1.show=False
            self.text2.show=True
            self.text3.show=False
            self.timerend.update()
            if self.timerend.ring: self.done=True





# Mini Game: Put Hero back to bed
# (We have just inverted the images and animations from wake up, not the code)
class obj_world_gotobed(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        # bed frame
        bed=actor.obj_grandactor(self,(440,500))
        bed.addpart( 'img',draw.obj_image('bed',(440,500),scale=0.75) )
        # text
        self.text1=actor.obj_grandactor(self,(840,500))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Hold [S] to go to Sleep',(1100,480)) )
        self.text2=actor.obj_grandactor(self,(840,500))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Sweet Dreams!',(1100,480)) )
        # three actors for hero: sleep, wake, awake (toggle show between each)
        self.herostate='sleep'
        self.timer=tool.obj_timer(80)
        self.hero_sleep=actor.obj_grandactor(self,(640,360))
        # self.hero_sleep.addpart( 'img_asleep',draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        # self.hero_sleep.addpart( 'img_asleep',draw.obj_image('herobase',(903,452),scale=0.7) )# actually awake
        self.hero_sleep.addpart( 'img_asleep', draw.obj_animation('ch1_awaken','herobase',(640,360),scale=0.7))# actually awake
        self.hero_wake=actor.obj_grandactor(self,(640,360))
        self.hero_wake.addpart( 'anim_awakes',draw.obj_animation('ch1_herotosleep','herobase',(640,360),scale=0.7) )
        self.hero_awake=actor.obj_grandactor(self,(640,360))
        # self.hero_awake.addpart( 'img_awake',draw.obj_image('herobase',(903,452),scale=0.7) )
        self.hero_awake.addpart( 'img_awake',draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )# actually asleep
        #
        self.hero_sleep.show=True
        self.hero_wake.show=False
        self.hero_awake.show=False
        self.text1.show=True
        self.text2.show=False
        # short timer to finish game
        self.timerend=tool.obj_timer(100)
    def update(self,controls):
        super().update(controls)
        if self.herostate=='sleep':
            self.hero_sleep.show=True
            self.hero_wake.show=False
            self.hero_awake.show=False
            self.text1.show=True
            self.text2.show=False
            if controls.s:
                self.herostate='wake'
                self.hero_wake.dict['anim_awakes'].rewind()
                self.timer.start()# reset timer
        elif self.herostate=='wake':
            self.hero_sleep.show=False
            self.hero_wake.show=True
            self.hero_awake.show=False
            self.text1.show=True
            self.text2.show=False
            self.timer.update()
            if not controls.s: self.herostate='sleep'
            if self.timer.ring:
                self.herostate='awake'
                self.timerend.start()
        elif self.herostate=='awake':
            self.hero_sleep.show=False
            self.hero_wake.show=False
            self.hero_awake.show=True
            self.text1.show=False
            self.text2.show=True
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame



####################################################################################################################



















#
