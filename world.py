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
import draw
import tool
import core


####################################################################################################################
# World
#* WORLD


# World Template
class obj_world:
    def __init__(self,creator,**kwargs):
        self.type='world'
        self.creator=creator# created by scene (i.e. page)
        self.ruledict={}# dictionary of rules in the world (non-ordered)
        self.actorlist=[]# list of actors in the world (ordered for updates)
        self.setup(**kwargs)
    def setup(self,**kwargs):# fill here for childs
        pass
    def addrule(self,name,rule):# add rule to the world (name must match object name!)
        self.ruledict[name]=rule
        for i in self.actorlist: rule.addactor(i)
    def removerule(self,name):# remove rule from the world
        self.ruledict.pop(name,None)# removes element if exists (returns None otherwise)
    def addactor(self,actor,foreground=True):# add actor to the world
        if foreground:# add actor in foreground (end of list, updated and drawn last)
            self.actorlist.append(actor)
        else:# add actor in background (beginning of list, updated and drawn first)
            self.actorlist.insert(0,actor)
        for i in self.ruledict.values(): i.addactor(actor)# non-indexed
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
# Actor Main Templates
# *ACTOR

# Template for most basic actors
class obj_actor:
    def __init__(self,creator):
        self.creator=creator# created by world
        self.setup()
        self.birth()
    def setup(self):# add here modifications for childs
        self.type='actor'# type (overwritten for each specific actor)
        self.actortype='None'
        self.alive=False# actor is alive in world
    def birth(self):# add to world
        self.creator.addactor(self)# add self to world list of actors
        self.alive=True
    def kill(self):# remove from world
        self.creator.removeactor(self)
        self.alive=False
    def update(self ,controls):
        pass


# Template for grand actors in world (hero, items, enemies..., obstacles...)
# A grand actor is more elaborate:
# - has a hitbox (rd,rx,ry)
# - can have display elements (textbox,image,animation or dispgroup)
# - can be transformed: movex(),movetox(),scale(),fliph()...,rotate90()
#                       (rotate not done due to enlargen-memory issues)
# *GRANDACTOR
class obj_grandactor():
    def __init__(self,creator,xy,scale=1,rotate=0,fliph=False,flipv=False,fliphv=False,foreground=True):
        # Creation
        self.creator=creator# created by world
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.foreground=foreground# if True, inserts in world to foreground, if False, in background
        # Setup and Birth
        self.setup()
        self.birth()# add self to world ONLY ONCE setup finished
        if scale != 1: self.scale(scale)# scale ONCE setup finished
        if rotate !=0: self.rotate90(rotate)
        if fliph: self.fliph()
        if flipv: self.flipv()
        if fliphv:
            self.fliph()
            self.flipv()
    def setup(self):# add here modifications for childs
        self.type='actor'# type (overwritten for each specific actor)
        self.actortype='grandactor'
        self.x=self.xini# position
        self.y=self.yini
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.show=True# show or not (can be toggled)
        self.alive=False# actor is alive in world
        # hitbox
        self.rx=5# radius width for rectangle collisions
        self.ry=5# radius height for rectangle collisions
        self.rd=5# radius for circle collisions
        # elements
        self.dict={}
        self.dictx={}# relative position
        self.dicty={}
        # devtools
        self.devrect=core.obj_sprite_rect()
    def birth(self):# add to world (at given layer index)
        self.creator.addactor(self,foreground=self.foreground)
        self.alive=True
    def kill(self):# remove from world
        self.creator.removeactor(self)
        self.alive=False
    def addpart(self,name,element):# add element
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )
    def removepart(self,name):# remove element
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
    def clearparts(self):# remove all elements
        self.dict={}
        self.dictx={}
        self.dicty={}
    def movetox(self,x):
        self.x=x
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movetoy(self,y):
        self.y=y
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def movetoxy(self,xy):
        self.movetox(xy[0])
        self.movetoy(xy[1])
    def movex(self,dx):
        self.x += dx
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,dy):
        self.y += dy
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def symh(self,name):# shift element symmetrically (horizontal)
        self.dictx[name] *= -1
        self.dict[name].movetox(self.x + self.dictx[name])
    def symv(self,name):# shift element symmetrically (vertical)
        self.dicty[name] *= -1
        self.dict[name].movetoy(self.y + self.dicty[name])
    def fliph(self):# horizontal
        self.fh=not self.fh
        for i in self.dict.keys():
            self.dict[i].fliph()
            self.symh(i)
    def bfliph(self,boolflip):# boolean flip
        if boolflip:
            self.ofliph()
        else:
            self.ifliph()
    def ifliph(self):# to inverted
        if not self.fh:
            self.fh=True
            for i in self.dict.keys():
                self.dict[i].ifliph()
                self.symh(i)
    def ofliph(self):# to original
        if self.fh:
            self.fh=False
            for i in self.dict.keys():
                self.dict[i].ofliph()
                self.symh(i)
    def flipv(self):# vertical
        self.fv=not self.fv
        for i in self.dict.keys():
            self.dict[i].flipv()
            self.symv(i)
    def bflipv(self,boolflip):# boolean flip
        if boolflip:
            self.oflipv()
        else:
            self.iflipv()
    def iflipv(self):# to inverted
        if not self.fv:
            self.fv=True
            for i in self.dict.keys():
                self.dict[i].iflipv()
                self.symv(i)
    def oflipv(self):# to original
        if self.fv:
            self.fv=False
            for i in self.dict.keys():
                self.dict[i].oflipv()
                self.symv(i)
    def scale(self,s):
        self.s *= s
        self.rx *= s# scale hitbox
        self.ry *= s
        self.rd *= s
        for i in self.dict.keys():
            self.dict[i].scale(s)
            self.dictx[i] *= s
            self.dicty[i] *= s
            self.dict[i].movetox(self.x+self.dictx[i])
            self.dict[i].movetoy(self.y+self.dicty[i])
    def rotate90(self,r):
        r=int(round(r%360/90,0)*90)# in 0,90,180,270
        self.r += r
        for i in self.dict.keys():
            self.dict[i].rotate90(r)
            termx,termy=self.dictx[i],self.dicty[i]
            if r==90:
                self.dictx[i],self.dicty[i]=termy,-termx
                self.rx,self.ry=self.ry,self.rx# rotate hitbox
            elif r==180:
                self.dictx[i],self.dicty[i]=-termx,-termy
            if r==270:
                self.dictx[i],self.dicty[i]=-termy,termx
                self.rx,self.ry=self.ry,self.rx# rotate hitbox
            self.dict[i].movetox(self.x+self.dictx[i])
            self.dict[i].movetoy(self.y+self.dicty[i])
    def play(self,controls):
        for i in self.dict.values():  i.play(controls)
    def devtools(self):
        self.devrect.display(share.colors.devactor,(self.x,self.y,2*self.rx,2*self.ry))# hitbox
    def update(self,controls):
        if self.show: self.play(controls)
        if share.devmode: self.devtools()


# Template: grand actor with rigidbody fonctionalities
# - rigidbody controls speed u,v inducing additional movement to x,y
# - external forces must be applied to exit stalling.
# - rigidbody dynamics are not computed if actor is stalling
# - friction slows any rigidbody untils stalls again.
# - if stalling the actor can still be controlled directly on x,y just like a non-rigidbody
# *RIGIDBODY
class obj_rbodyactor(obj_grandactor):
    def setup(self):
        super().setup()
        self.actortype="rbody"
        self.stalling=True# stalling or not
        self.dt=1#(could make it depend on game fps)
        self.u=0# rigid body speed
        self.v=0
        self.m=1# mass (must be >0)
        self.d=0.01# dissipation rate
        self.umin2=1# min speed for stalling (squared)
    def movex(self,u):# rewritten to not be game fps dependent
        self.x += round(u*self.dt)
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,v):
        self.y += round(v*self.dt)
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
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
####################################################################################################################
####################################################################################################################

# Mini Game: sunrise
# *SUNRISE
class obj_world_sunrise(obj_world):
    def setup(self):
        #
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.ungoing=False# ungoing or back to start
        # layering
        self.startactor=obj_grandactor(self,(640,360))
        self.ungoingactor=obj_grandactor(self,(640,360))
        self.finishactor=obj_grandactor(self,(640,360))
        self.staticactor=obj_grandactor(self,(640,360))# static in front here
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.staticactor.show=True
        self.startactor.show=True
        self.ungoingactor.show=False
        self.finishactor.show=False
        self.text_undone.show=True
        self.text_done.show=False
        # static actor
        self.staticactor.addpart( "img3", draw.obj_image('flower',(102,440),scale=0.28,rotate=0,fliph=True,flipv=False) )
        #
        self.staticactor.addpart( 'imgref1', draw.obj_image('horizon',(640,720-150),path='data/premade') )
        self.staticactor.addpart( 'imgref2', draw.obj_image('house',(296,443),scale=0.5) )
        self.staticactor.addpart( "imgref3", draw.obj_image('pond',(650,611),scale=0.5,rotate=0,fliph=False,flipv=False) )
        #
        self.staticactor.addpart( "img1", draw.obj_image('bush',(827,452),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img2", draw.obj_image('bush',(486,648),scale=0.32,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img4", draw.obj_image('flower',(186,615),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img5", draw.obj_image('flower',(101,567),scale=0.28,rotate=0,fliph=True,flipv=False) )
        #
        # start actor
        # self.startactor.addpart( 'img1', draw.obj_image('sun',(660,300),scale=0.5) )
        # ungoing actor
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch2_sunrise','sun',(640,360)) )
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('sun',(660,300),scale=0.5) )


        # text
        self.textboxclick=draw.obj_textbox('Hold ['+share.datamanager.controlname('up')\
        +'] to rise the sun',(1000,620),color=share.colors.instructions,hover=True)
        self.text_undone.addpart( 'text1', self.textboxclick )
        self.text_done.addpart( 'text1', draw.obj_textbox('Morning Time!',(1000,620)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(100)# ungoing part
        self.timerend=tool.obj_timer(100)# goal to done
        self.timer.start()# reset ungoing timer
        #
        self.soundstart=draw.obj_sound('sunrise_start')
        self.creator.addpart(self.soundstart)
        self.soundend=draw.obj_sound('sunrise_end')
        self.creator.addpart(self.soundend)



    def triggerungoing(self,controls):
        return controls.gu and controls.guc or (True and self.textboxclick.isclicked(controls))
    def triggerstart(self,controls):
        return not controls.gu and not self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.goal:
            # goal unreached state
            if not self.ungoing:
                # start substate
                if self.triggerungoing(controls):# flip to ungoing
                    self.soundstart.play()
                    self.ungoing=True
                    self.startactor.show=False
                    self.ungoingactor.show=True
                    self.finishactor.show=False
                    self.timer.start()# reset ungoing timer
                    self.ungoingactor.dict["anim1"].rewind()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                if self.timer.ring:# flip to goal reached
                    self.goal=True
                    self.startactor.show=False
                    self.ungoingactor.show=False
                    self.finishactor.show=True
                    self.text_undone.show=False
                    self.text_done.show=True
                    self.timerend.start()
                    self.soundend.play()
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: wakeup
# *WAKEUP WAKE UP
class obj_world_wakeup(obj_world):
    def setup(self,**kwargs):
        # default options
        self.addpartner=False# add partner alongside hero
        self.addbug=False# add bug alongside hero
        self.partnerangry=False# partner is angry
        self.heroangry=False# hero is angry
        self.addsun=True# add the sun (must have been drawn)
        self.addalarmclock=False# add the alarm clock and night stand
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# partner options
            if 'bug' in kwargs: self.addbug=kwargs["bug"]# partner options
            if 'heroangry' in kwargs: self.heroangry=kwargs["heroangry"]# partner options
            if 'partnerangry' in kwargs: self.partnerangry=kwargs["partnerangry"]# partner options
            if 'sun' in kwargs: self.addsun=kwargs["sun"]# partner options
            if 'alarmclock' in kwargs: self.addalarmclock=kwargs["alarmclock"]# partner options
        #
        # change base picture
        self.herobaseimg='herobase'
        self.partnerbaseimg='partnerbase'
        if self.heroangry:# replace with angry characters
            self.herobaseimg='herobaseangry'
        if self.partnerangry:
            self.partnerbaseimg='partnerbaseangry'
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.ungoing=False# ungoing or back to start
        #
        # layering
        self.staticactor=obj_grandactor(self,(640,360))
        self.startactor=obj_grandactor(self,(640,360))
        self.ungoingactor=obj_grandactor(self,(640,360))
        self.finishactor=obj_grandactor(self,(640,360))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.staticactor.show=True
        self.startactor.show=True
        self.ungoingactor.show=False
        self.finishactor.show=False
        self.text_undone.show=True
        self.text_done.show=False
        # static actor
        self.staticactor.addpart( 'img1', draw.obj_image('bed',(440,500),scale=0.75) )
        if self.addsun:
            self.staticactor.addpart( 'annim',draw.obj_animation('wakeup_sun','sun',(640,360)) )
        if self.addalarmclock:
            animation1=draw.obj_animation('wakeup_alarmclock','alarmclock8am',(640,360+50))
            animation1.addsound( "wakeup_alarm", [5] )
            self.staticactor.addpart( 'annim1', animation1 )
            self.staticactor.addpart( 'img2',draw.obj_image('nightstand',(100,530),scale=0.5) )
        # start actor
        if self.addpartner:# add partner
            self.startactor.addpart( 'imgadd1', draw.obj_image(self.partnerbaseimg,(420+100,490-50),scale=0.7,rotate=80) )
        # self.startactor.addpart( 'img1', draw.obj_image(self.herobaseimg,(420,490),scale=0.7,rotate=80) )
        animation=draw.obj_animation('ch1_hero1inbed','herobase',(360,360))
        animation.addsound( "wakeup_snore1", [14] )
        animation.addsound( "wakeup_snore2", [134] )
        self.startactor.addpart( 'anim1', animation )
        self.startactor.addpart( 'anim1a', draw.obj_animation('ch1_heroinbedZ','sleepZ',(700,400),path='data/premade'))
        self.startactor.addpart( 'anim1b', draw.obj_animation('ch1_heroinbedZ','sleepZ',(700+60,400-20),path='data/premade',imgscale=0.7))
        self.startactor.addpart( 'anim1c', draw.obj_animation('ch1_heroinbedZ','sleepZ',(700+100,400-30),path='data/premade',imgscale=0.5))


        # ungoing actor
        if self.addpartner:# add partner in love
            self.ungoingactor.addpart( 'animadd1', draw.obj_animation('ch1_heroawakes',self.partnerbaseimg,(640+100,360-50),scale=0.7) )
        if self.addbug:# add bug crawling out of bed
            self.ungoingactor.addpart( 'animadd2', draw.obj_animation('ch4_heroawakesbug','bug',(640,360)) )
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch1_heroawakes',self.herobaseimg,(640,360),scale=0.7) )
        # finish actor
        if self.addpartner:# add partner in love
            self.finishactor.addpart( 'imgadd1', draw.obj_image(self.partnerbaseimg,(903+100,452-50),scale=0.7) )
        if self.addbug:
            self.finishactor.addpart( 'imgadd2', draw.obj_image('bug',(1168,595),scale=0.33) )
        self.finishactor.addpart( 'img1', draw.obj_image(self.herobaseimg,(903,452),scale=0.7) )
        # text
        self.textboxclick=draw.obj_textbox('Hold ['+share.datamanager.controlname('right')+'] to Wake up',(1100,480),color=share.colors.instructions,hover=True)
        self.text_undone.addpart( 'text1', self.textboxclick )
        self.text_done.addpart( 'text1', draw.obj_textbox('Good Morning!',(1150,480)) )


        # self.creator.addpart( draw.obj_textbox('Hold ['+share.datamanager.controlname('right')+'] to Wake up',(1100,480+100),color=share.colors.instructions,hover=True) )
        # timer for ungoing part
        self.timer=tool.obj_timer(100)# ungoing part
        self.timerend=tool.obj_timer(90)# goal to done
        self.timer.start()# reset ungoing timer
        # audio
        self.soundstart=draw.obj_sound('wakeup_wake1')
        self.creator.addpart(self.soundstart)
        self.sounddone=draw.obj_sound('wakeup_wake2')
        self.creator.addpart(self.sounddone)

    def triggerungoing(self,controls):
        return controls.gr and controls.grc or (True and self.textboxclick.isclicked(controls))
    def triggerstart(self,controls):
        return not controls.gr and not self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.goal:
            # goal unreached state
            if not self.ungoing:
                # start substate
                if self.triggerungoing(controls):# flip to ungoing
                    self.soundstart.play()
                    self.ungoing=True
                    self.startactor.show=False
                    self.ungoingactor.show=True
                    self.finishactor.show=False
                    self.ungoingactor.dict["anim1"].rewind()
                    if self.addpartner:
                        self.ungoingactor.dict["animadd1"].rewind()
                    if self.addbug:
                        self.ungoingactor.dict["animadd2"].rewind()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    # self.soundback.play()
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                    self.timer.start()# reset ungoing timer
                    self.startactor.dict["anim1"].rewind()
                    self.startactor.dict["anim1a"].rewind()
                    self.startactor.dict["anim1b"].rewind()
                    self.startactor.dict["anim1c"].rewind()
                if self.timer.ring:# flip to goal reached
                    self.goal=True
                    self.sounddone.play()
                    self.timerend.start()
                    self.startactor.show=False
                    self.ungoingactor.show=False
                    self.finishactor.show=True
                    self.text_undone.show=False
                    self.text_done.show=True
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame


####################################################################################################################

# Mini Game: sneak drink at breakfast
#*DRINKING *BREAKFAST
class obj_world_breakfastdrinking(obj_world):
    def setup(self,**kwargs):
        # default options
        self.addpartner=True# add partner alongside hero (otherwise can just drink alone)
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# partner options
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.progressbar=obj_grandactor(self,(640,360))# progress bar
        self.hero=obj_grandactor(self,(145,515))# hero
        self.partner=obj_grandactor(self,(1160,490))# partner
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        # static
        self.staticactor.addpart( 'img1', draw.obj_image('floor3',(640,720-150),path='data/premade') )
        if self.addpartner:
            self.staticactor.addpart( 'img2', draw.obj_image('coffeecup',(640+180,600),scale=0.4,fliph=False) )
        self.staticactor.addpart( 'img3', draw.obj_image('coffeecup',(640-180,600),scale=0.4,fliph=True) )
        self.staticactor.addpart( 'img4', draw.obj_image('flowervase',(640,440),scale=0.5) )
        # progress bar
        self.progressbar.addpart( 'bar', draw.obj_image('completion1fill',(640,200),path='data/premade') )
        self.progressbar.addpart( 'slide', draw.obj_image('completion1slide',(640,200),path='data/premade') )
        self.progressbar.addpart( 'borders', draw.obj_image('completion1',(640,200),path='data/premade') )
        self.progressbar.addpart( 'textbox', draw.obj_textbox('0%',(640,270)) )
        self.progressmx=2#1# move rate of progressbar (respect to self.progress)
        self.progressmax=int(567/self.progressmx)# max progress
        self.progress=0# 0 to max progress
        ydown=60# shift down hero/partner
        # hero
        self.hero.addpart( 'waiting', draw.obj_image('herobaseangry',(150,540+ydown),scale=1.15,fliph=False) )
        self.hero.addpart( 'happy', draw.obj_image('herobase',(150,540+ydown),scale=1.15,fliph=False) )
        self.hero.addpart( 'drinkinghero', draw.obj_animation('ch4_herodrinks1','herobase',(640,360+ydown)) )
        self.hero.addpart( 'drinkingdrink', draw.obj_animation('ch4_herodrinks2','drink',(640,360+ydown)) )
        # self.hero.addpart( 'busted', draw.obj_image('herobaseangry',(195,620),scale=1.2,rotate=26) )
        self.hero.addpart( 'busted', draw.obj_animation('ch4_herodrinks1','herobaseangry',(640,360+ydown)) )
        self.hero.addpart( 'finished', draw.obj_animation('world_breakfastdrinking3','herobase',(640,360+ydown)) )
        self.hero.dict['waiting'].show=True
        self.hero.dict['happy'].show=False
        self.hero.dict['drinkinghero'].show=False
        self.hero.dict['drinkingdrink'].show=False
        self.hero.dict['busted'].show=False
        self.hero.dict['finished'].show=False
        self.herostate=0# 0,1,2 for neutral,drinking,happy (excludes busted from partnerbusting)
        self.herohappytimer=tool.obj_timer(100)# timer for happy after drinking
        # partner
        if self.addpartner:
            self.partner.addpart( 'waiting_base', draw.obj_image('stickbody',(1160-50,640+15+ydown),scale=1.15,fliph=True,path='data/premade') )
            self.partner.addpart( 'waiting_headleft', draw.obj_image('partnerhead',(1160-50,340+15+ydown),scale=1.15,fliph=True) )
            self.partner.addpart( 'waiting_headright', draw.obj_image('partnerhead',(1160-50+30,340+15+ydown),scale=1.15,fliph=False) )
            self.partner.addpart( 'waiting_headrightup', draw.obj_image('partnerhead',(1160-50+20,340+15+ydown),scale=1.15,rotate=15,fliph=False) )
            self.partner.addpart( 'waiting_headrightbobble', draw.obj_image('partnerhead',(1160-50+30,340+15+ydown),scale=1.15,rotate=-15,fliph=False) )
            self.partner.addpart( 'busting', draw.obj_animation('world_breakfastdrinking2','partnerbase',(640,360+ydown)) )
            self.partner.addpart( 'bustingmark', draw.obj_image('exclamationmark',(1100,130+ydown),scale=1.5,path='data/premade') )
            self.partner.addpart( 'whatmark', draw.obj_image('interrogationmark',(1160,130+ydown),scale=1.5,path='data/premade') )
            self.partner.addpart( 'bustedtext', draw.obj_textbox('Busted!',(640,400+ydown),fontsize='huge') )
            self.partner.dict['waiting_base'].show=True
            self.partner.dict['waiting_headleft'].show=False
            self.partner.dict['waiting_headright'].show=True
            self.partner.dict['waiting_headrightup'].show=False
            self.partner.dict['waiting_headrightbobble'].show=False
            self.partner.dict['busting'].show=False
            self.partner.dict['bustingmark'].show=False
            self.partner.dict['bustedtext'].show=False
            self.partner.dict['whatmark'].show=False
            self.partnerbusting=False# busting or not (2 states)
            self.partnerstate=1# while not busting, state 0,1,2,3 for headleft,headright,headrightup,headrightbobble
            self.partnertimer=tool.obj_timer(50)# timer for switch states
            self.partnertimer.start()
            self.partnertimerbusting=tool.obj_timer(110)# timer for busting
        else:
            # ensure partner is never seen
            self.partnerbusting=False
            self.partnerstate=1
            self.partnertimer=tool.obj_timer(0)# dummy
        # text
        if self.addpartner:
            self.text_undone.addpart( 'text1', \
            draw.obj_textbox('Hold ['+share.datamanager.controlname('up')+'] to Sneak Drink',(640,690),color=share.colors.instructions) )
        else:
            self.text_undone.addpart( 'text1', \
            draw.obj_textbox('Hold ['+share.datamanager.controlname('up')+'] to Drink',(640,690),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Wasted!',(640,690)) )
        self.text_undone.show=True
        self.text_done.show=False
        # timer for end
        self.timerend=tool.obj_timer(210)# goal to done
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            if self.progress>self.progressmax-1:# reached goal
                self.goal=True
                self.timerend.start()
                self.text_undone.show=False
                self.text_done.show=True
                self.hero.dict['waiting'].show=False
                self.hero.dict['drinkinghero'].show=False
                self.hero.dict['drinkingdrink'].show=False
                self.hero.dict['busted'].show=False
                self.hero.dict['finished'].show=True
                self.hero.dict['finished'].rewind()
                if self.addpartner:
                    self.partner.dict['waiting_base'].show=False
                    self.partner.dict['waiting_headleft'].show=False
                    self.partner.dict['waiting_headright'].show=False
                    self.partner.dict['waiting_headrightup'].show=False
                    self.partner.dict['waiting_headrightbobble'].show=False
                    self.partner.dict['busting'].show=False
                    self.partner.dict['bustingmark'].show=False
                    self.partner.dict['bustedtext'].show=False
                    self.partner.dict['whatmark'].show=False
                self.staticactor.show=True
                self.progressbar.show=True
            #
            # partner is busting hero
            if self.partnerbusting:
                self.partnertimerbusting.update()
                if self.partnertimerbusting.ring:# switch back to normal
                    self.partnerbusting=False
                    self.herostate=0
                    self.partnerstate=1# goes to facing right
                    self.partnertimer.amount=100
                    self.partnertimer.start()
                    self.hero.dict['waiting'].show=True
                    self.hero.dict['drinkinghero'].show=False
                    self.hero.dict['drinkingdrink'].show=False
                    self.hero.dict['busted'].show=False
                    self.hero.dict['finished'].show=False
                    self.partner.dict['waiting_base'].show=True
                    self.partner.dict['waiting_headleft'].show=False
                    self.partner.dict['waiting_headright'].show=True
                    self.partner.dict['waiting_headrightup'].show=False
                    self.partner.dict['waiting_headrightbobble'].show=False
                    self.partner.dict['busting'].show=False
                    self.partner.dict['bustingmark'].show=False
                    self.partner.dict['bustedtext'].show=False
                    self.partner.dict['whatmark'].show=False
                    self.staticactor.show=True
                    self.progressbar.show=True

            # partner is not busting hero
            else:
                # switch to busting
                if self.herostate==1 and self.partnerstate==0:# busted drinking
                    self.partnerbusting=True
                    self.partnertimerbusting.start()
                    self.progress = 0# reset progress
                    self.progressbar.dict['slide'].movetox(640+self.progress*self.progressmx)
                    self.progressbar.dict['textbox'].replacetext( str(int(self.progress/self.progressmax*100))+'%' )
                    self.hero.dict['waiting'].show=False
                    self.hero.dict['drinkinghero'].show=False
                    self.hero.dict['drinkingdrink'].show=True
                    self.hero.dict['busted'].show=True
                    self.hero.dict['finished'].show=False
                    self.partner.dict['waiting_base'].show=True
                    self.partner.dict['waiting_headleft'].show=True
                    self.partner.dict['waiting_headright'].show=False
                    self.partner.dict['waiting_headrightup'].show=False
                    self.partner.dict['waiting_headrightbobble'].show=False
                    self.partner.dict['busting'].show=False
                    self.partner.dict['bustingmark'].show=True
                    self.partner.dict['bustedtext'].show=True
                    self.partner.dict['whatmark'].show=False
                    self.staticactor.show=False
                    self.progressbar.show=False
                # hero behavior
                if self.herostate==0:# neutral
                    if controls.gu and controls.guc:# switch to drinking
                        self.herostate=1#
                        self.hero.dict['waiting'].show=False
                        self.hero.dict['happy'].show=False
                        self.hero.dict['drinkinghero'].show=True
                        self.hero.dict['drinkingdrink'].show=True
                        self.hero.dict['busted'].show=False
                        self.hero.dict['finished'].show=False
                elif self.herostate==1:# drinking
                    self.progress += 1# update progress
                    self.progressbar.dict['slide'].movetox(640+self.progress*self.progressmx)
                    self.progressbar.dict['textbox'].replacetext( str(int(self.progress/self.progressmax*100))+'%' )
                    if not controls.gu and controls.guc:# switch to happy
                        self.herostate=2#
                        self.herohappytimer.start()
                        self.hero.dict['waiting'].show=False
                        self.hero.dict['happy'].show=True
                        self.hero.dict['drinkinghero'].show=False
                        self.hero.dict['drinkingdrink'].show=False
                        self.hero.dict['busted'].show=False
                        self.hero.dict['finished'].show=False
                elif self.herostate==2:# happy
                    if controls.gu and controls.guc:# switch to drinking
                        self.herostate=1#
                        self.hero.dict['waiting'].show=False
                        self.hero.dict['happy'].show=False
                        self.hero.dict['drinkinghero'].show=True
                        self.hero.dict['drinkingdrink'].show=True
                        self.hero.dict['busted'].show=False
                        self.hero.dict['finished'].show=False
                    else:# switch back to neutral
                        self.herohappytimer.update()
                        if self.herohappytimer.ring:# switch to neutral
                            self.herostate=0
                            self.hero.dict['waiting'].show=True
                            self.hero.dict['happy'].show=False
                            self.hero.dict['drinkinghero'].show=False
                            self.hero.dict['drinkingdrink'].show=False
                            self.hero.dict['busted'].show=False
                            self.hero.dict['finished'].show=False
                # partner behavior
                self.partnertimer.update()
                if self.partnertimer.ring:# regular switches between partner attitudes
                    # decide next state
                    if self.partnerstate==0:# headleft (unsafe) to headright,headrightup or headrightbobble
                        self.partnerstate=tool.randchoice([1,2,3],probas=[40,40,20])# 20% chance of going to danger zone
                    elif self.partnerstate==1:# headright to headrightup or headrightbobble
                        self.partnerstate=tool.randchoice([2,3],probas=[30,70])# 70% chance of going to danger zone
                    elif self.partnerstate==2:# headrightup to headright 1 or headrightbobble 3
                        self.partnerstate=tool.randchoice([1,3],probas=[30,70])# 70% chance of going to danger zone
                    elif self.partnerstate==3:# headrightbobble to headleft (unsafe) always
                        self.partnerstate=0
                    # switch to next state
                    if self.partnerstate==0:# headleft
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=True
                        self.partner.dict['waiting_headright'].show=False
                        self.partner.dict['waiting_headrightup'].show=False
                        self.partner.dict['waiting_headrightbobble'].show=False
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
                        self.partner.dict['whatmark'].show=False
                    elif self.partnerstate==1:# headright
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=True
                        self.partner.dict['waiting_headrightup'].show=False
                        self.partner.dict['waiting_headrightbobble'].show=False
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
                        self.partner.dict['whatmark'].show=False
                    elif self.partnerstate==2:# headrightup
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=False
                        self.partner.dict['waiting_headrightup'].show=True
                        self.partner.dict['waiting_headrightbobble'].show=False
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
                        self.partner.dict['whatmark'].show=False
                    elif self.partnerstate==3:# headrightbobble
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=False
                        self.partner.dict['waiting_headrightup'].show=False
                        self.partner.dict['waiting_headrightbobble'].show=True
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
                        self.partner.dict['whatmark'].show=True# interrogation mark
                    # decide next timer (depends on next state)
                    if self.partnerstate==0:# headleft
                        self.partnertimer.amount=100+tool.randint(0,100)
                    elif self.partnerstate==1:# headright
                        self.partnertimer.amount=90+tool.randint(0,100)
                    elif self.partnerstate==2:# headrightup
                        self.partnertimer.amount=90+tool.randint(0,100)
                    elif self.partnerstate==3:# headrightbobble (fast countdown)
                        self.partnertimer.amount=80
                    # start next timer
                    self.partnertimer.start()

        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame


####################################################################################################################

# Mini Game: Fishing
# *FISHING
class obj_world_fishing(obj_world):
    def setup(self):
        self.done=False# mini game is finished

        # hook
        self.hook=obj_grandactor(self,(640,100))
        self.hook.actortype='hook'
        self.hook.rx=30
        self.hook.ry=30
        self.hook.r=30
        self.hook.addpart( 'line',draw.obj_image('hookline',(640,100-390),path='data/premade') )
        self.hook.addpart( 'img_fish',draw.obj_image('fish',(640,100+50),scale=0.25,rotate=-90) )
        self.hook.dict['img_fish'].show=False
        self.hook.addpart( 'img_hook',draw.obj_image('hook',(640,100),scale=0.25) )
        self.dydown=5
        self.dyup=2
        # fish status
        self.fishfree=True# fish not caugth (yet)
        # fish animation
        self.fish=obj_grandactor(self,(640,360))
        animation=draw.obj_animation('fishmove1','fish',(640,360),imgscale=0.25)
        # animation.addsound( "fishing_swim", [13, 97, 258, 316, 510, 565, 734, 766] )
        self.fish.addpart( 'anim_fish',animation )
        # fish hit box
        self.fishbox=obj_grandactor(self,(340,360))
        self.fishbox.actortype='fish'
        self.fishbox.rx=30
        self.fishbox.ry=30
        self.fishbox.r=30
        # short timer at end
        self.timerend=tool.obj_timer(90)# 50
        # textbox when caught
        self.text1=obj_grandactor(self,(840,500))
        tempo='['+share.datamanager.controlname('down')+': lower hook]'
        self.textboxclick=draw.obj_textbox(tempo,(1100,460),color=share.colors.instructions,hover=True)
        self.text1.addpart( 'textbox1',self.textboxclick )
        self.text2=obj_grandactor(self,(840,500))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Nice Catch!',(1100,460)) )
        self.text1.show=True
        self.text2.show=False
        #
        self.soundreel=draw.obj_sound('fishing_reel')
        self.creator.addpart(self.soundreel)
        self.soundcatch=draw.obj_sound('fishing_catch')
        self.creator.addpart(self.soundcatch)
    def triggerlowerhook(self,controls):
        return controls.gd or self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        # hook
        if self.triggerlowerhook(controls) and self.fishfree:
            if controls.gdc or self.textboxclick.isclicked(controls):
                self.soundreel.play(loop=True)
                # self.soundreel.play()
            if self.hook.y<720-50:
                self.hook.movey(self.dydown)
            else:
                self.soundreel.stop()
        else:
            self.soundreel.stop()
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
                self.soundcatch.play()
        else:
            # end of mini-game
            self.timerend.update()
            if self.timerend.ring:
                self.done=True



####################################################################################################################

# Mini Game: Eat Fish
# *EAT *EATFISH
class obj_world_eatfish(obj_world):
    def setup(self,**kwargs):
        # default options
        self.addpartner=False
        self.eldereats=False# replace hero with elder as eater
        self.heroisangry=False# angry face on hero
        self.eatcake=False# eat cake insteaf of fish
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# partner options
            if 'eldereats' in kwargs: self.eldereats=kwargs["eldereats"]
            if 'heroangry' in kwargs: self.heroisangry=kwargs["heroangry"]
            if 'cake' in kwargs: self.eatcake=kwargs["cake"]
        #
        self.done=False# mini game is finished
        self.doneeating=False# done eating
        self.bites=6# total number of bites
        self.alternate_LR=True# alternate Left-Right pattern to eat
        self.eating=False

        # fish
        self.fish=obj_grandactor(self,(640,360))
        self.fishscale=1# initial size of fish
        if self.eatcake:
            self.fish.addpart( 'img_fish',draw.obj_image('cake',(800,450), scale=self.fishscale) )
        else:
            self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,450), scale=self.fishscale,rotate=-45) )
        # hero eating or not eating
        self.herostand=obj_grandactor(self,(640,360))
        if self.addpartner:# add partner
            self.herostand.addpart( 'imgadd1', draw.obj_image('partnerbase',(340-100,400-10), scale=0.7) )
        if self.eldereats:
            self.herostand.addpart( 'img_stand',draw.obj_image('elderbase',(340,400), scale=0.7) )
        else:
            if self.heroisangry:
                self.herostand.addpart( 'img_stand',draw.obj_image('herobaseangry',(340,400), scale=0.7) )
            else:
                self.herostand.addpart( 'img_stand',draw.obj_image('herobase',(340,400), scale=0.7) )
        self.heroeat=obj_grandactor(self,(640,360))
        if self.addpartner:# add partner in love
            self.heroeat.addpart( 'imgadd1', draw.obj_animation('ch1_heroeats1','partnerbase',(640-100,360-10),imgscale=0.7) )
        if self.eldereats:
            self.animation1=draw.obj_animation('ch1_heroeats1','elderbase',(640,360),imgscale=0.7)
        else:
            if self.heroisangry:
                self.animation1=draw.obj_animation('ch1_heroeats1','herobaseangry',(640,360),imgscale=0.7)
            else:
                self.animation1=draw.obj_animation('ch1_heroeats1','herobase',(640,360),imgscale=0.7)
        self.heroeat.addpart('anim_eat', self.animation1)
        self.herostand.show=True
        self.heroeat.show=False
        # text
        self.text1=obj_grandactor(self,(640,360))
        tempo='alternate ['+share.datamanager.controlname('left')
        tempo +='] and ['+share.datamanager.controlname('right')+'] to eat'
        self.textboxclick=draw.obj_textbox(tempo,(480,660),color=share.colors.instructions,hover=True)
        self.text1.addpart( 'textbox1',self.textboxclick )
        self.text2=obj_grandactor(self,(640,360))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Burp!',(800,390),fontsize='large') )
        self.text1.show=True
        self.text2.show=False
        # textbox crunch
        self.text3=obj_grandactor(self,(640,360))
        self.text3.addpart( 'textbox1', draw.obj_textbox('Crunch!',(893,236),fontsize='large') )
        self.text3.show=False
        # timer for eating
        self.timer=tool.obj_timer(50)
        # short timer after done eating
        self.timerend=tool.obj_timer(50)
        #
        self.soundeat=draw.obj_sound('eat')
        self.creator.addpart(self.soundeat)
        if self.eatcake:
            self.soundeatend=draw.obj_sound('eatendpowerup')# different sound if eating cake
            self.creator.addpart(self.soundeatend)
        else:
            self.soundeatend=draw.obj_sound('eatend')
            self.creator.addpart(self.soundeatend)
        #
    def eatfood(self):
        if self.bites in [6,4,2]:
            self.soundeat.play()
        elif self.bites==1:
            self.soundeatend.play()
        self.eating=True
        self.timer.start()
        self.bites -=1
        self.fishscale *= 0.8
        self.fish.removepart( 'img_fish')
        if self.eatcake:
            self.fish.addpart( 'img_fish',draw.obj_image('cake',(800,450), scale=self.fishscale) )
        else:
            self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,450), scale=self.fishscale,rotate=-45) )
    def triggerleftbite(self,controls):
        return (controls.gl and controls.glc) or self.textboxclick.isclicked(controls)
    def triggerrightbite(self,controls):
        return (controls.gr and controls.grc) or self.textboxclick.isclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.doneeating:
            if self.alternate_LR:
                if self.triggerleftbite(controls):
                    self.eatfood()
                    self.alternate_LR=False
            else:
                if self.triggerrightbite(controls):
                    self.eatfood()
                    self.alternate_LR=True
            if self.eating:
                self.herostand.show=False
                self.heroeat.show=True
                self.text3.show=True
                self.timer.update()# stop eating on timer
                if self.timer.ring:
                    self.eating=False
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

####################################################################################################################
#
# # Mini Game: travel on overworld
# *TRAVEL
class obj_world_travel(obj_world):
    def setup(self,**kwargs):
        #
        #
        ##############################################3

        self.done=False# end of minigame
        self.goal=False# destination reached
        self.goalname=None# name of reached goal (if multiple)
        self.doambience=True# add ambience sounds to the world (forest sounds)
        #
        # Default parameters
        self.wherestart='home'# where the hero starts
        self.whereends='nowhere'# where the goal is
        self.hasboat=False# hero has boat and can sail south
        self.chapter=1# level of drawings to show from chapters (1=tree/house, 3=tower/mountain, 5=peak+cloud/lightning)
        self.removelist=[]# force to remove specific items (if they dont exit yet)
        self.addpartner=False# add partner walking with hero
        self.addsailor=False# add sailor walking with hero
        self.minigame=None# add mini-game on the travel game (minigame='flowers',etc....)
        self.addbeachquestionmark=False# add a question mark on the beach
        self.addbeachmark=False# add a cross mark on the beach
        self.addsailorwait=False# add the sailor (waiting on the beach)
        self.noending=False# skip the completion part of minigame

        # scene tuning
        if kwargs is not None:
            if 'chapter' in kwargs: self.chapter=kwargs["chapter"]
            if 'start' in kwargs: self.wherestart=kwargs["start"]
            if 'goal' in kwargs: self.whereends=kwargs["goal"]# option go back home
            if 'boat' in kwargs: self.hasboat=kwargs["boat"]
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# option partner walks with hero
            if 'sailor' in kwargs: self.addsailor=kwargs["sailor"]# option sailor walks with hero
            if 'minigame' in kwargs: self.minigame=kwargs["minigame"]# option add minigame
            if 'remove' in kwargs: self.removelist=kwargs["remove"]
            if 'noending' in kwargs: self.noending=kwargs["noending"]
            if 'sailorwait' in kwargs: self.addsailorwait=kwargs["sailorwait"]
            if 'beachquestionmark' in kwargs: self.addbeachquestionmark=kwargs["beachquestionmark"]
            if 'beachmark' in kwargs: self.addbeachmark=kwargs["beachmark"]
            if 'ambience' in kwargs: self.doambience=kwargs["ambience"]
            #
        ##########################3
        # Premake necessary images
        # combine herohead+stickwalk = herowalk
        image1=draw.obj_image('stickwalk',(640,460),path='data/premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herowalk')
        # combine partnerhead+stickwalk = partnerwalk
        if self.addpartner:
            image1=draw.obj_image('stickwalk',(640,460),path='data/premade')# snapshot
            image2=draw.obj_image('partnerhair',(640,200))
            image3=draw.obj_image('herohead',(640,200),scale=0.5)# hero instead of stick head
            dispgroup2=draw.obj_dispgroup((640,360))
            dispgroup2.addpart('part1',image1)
            dispgroup2.addpart('part2',image2)
            dispgroup2.addpart('part3',image3)
            dispgroup2.snapshot((640,330,200,330),'partnerwalk')
        # combine sailorhead+stickwalk = sailorwalk
        if self.addsailor:
            dispgroup2=draw.obj_dispgroup((640,360))
            dispgroup2.addpart('part1',draw.obj_image('stickwalk',(640,460),path='data/premade') )
            dispgroup2.addpart('part2',draw.obj_image('sailorbaldhead',(640,200),scale=0.5))
            dispgroup2.addpart('part3',draw.obj_image('sailorhat',(640,200-100),scale=0.5))
            dispgroup2.snapshot((640,360-15,200,360+15),'sailorwalk')
        ##########################3
        #
        #
        if type(self.wherestart)==tuple:
            self.xyhero=self.wherestart
        else:
            if self.wherestart=='home':# initial position of hero
                self.xyhero=(0,0)
            elif self.wherestart=='pond':
                self.xyhero=(-320,-180)
            elif self.wherestart=='atpartner':
                self.xyhero=(172-640,571-360)#(870-640,570-360)
            elif self.wherestart=='mech':
                self.xyhero=(1100-640,10-360)
            elif self.wherestart=='cake':
                self.xyhero=(210,-50)
            elif self.wherestart=='tower':
                self.xyhero=(-1280,0)
            elif self.wherestart=='forest':
                self.xyhero=(1280,0)
            elif self.wherestart=='peak':
                self.xyhero=(0,-1080)
            elif self.wherestart=='beach':
                self.xyhero=(-1280,1080-120)
            elif self.wherestart=='island':
                self.xyhero=(1280,1080+1080)
            else:
                self.xyhero=(0,0)
        #
        self.multiplegoals=False# single end goal/location
        if self.whereends=='home':# goal position
            self.xygoal=(0,0)
        elif self.whereends=='pond':
            self.xygoal=(-320,-180)
        elif self.whereends=='atpartner':
            self.xygoal=(172-640,571-360)#(870-640,570-360)
        elif self.whereends=='mech':
            self.xygoal=(1100-640,10-360)
        elif self.whereends=='cake':
            self.xygoal=(210,-50)
        elif self.whereends=='tower':
            self.xygoal=(-1280,0)
        elif self.whereends=='forest':
            self.xygoal=(1280,0)
        elif self.whereends=='peak':
            self.xygoal=(0,-1080-80)
        elif self.whereends=='beach':
            self.xygoal=(-1280,1080-120)
        elif self.whereends=='island':
            self.xygoal=(1280,1080+1080)
        elif self.whereends=='everywhere':# multiple possible locations
            self.multiplegoals=True
            self.allxygoals={}
            self.allxygoals['home']=(0,0)
            self.allxygoals['pond']=(-320,-180)
            self.allxygoals['mech']=(1100-640,10-360)
            self.allxygoals['cake']=(210,-50)
            self.allxygoals['atpartner']=(172-640,571-360)
            self.allxygoals['tower']=(-1280,0)
            self.allxygoals['forest']=(1280,0)
            self.allxygoals['peak']=(0,-1080-80)
            self.allxygoals['beach']=(-1280,1080-120)
            self.allxygoals['island']=(1280,1080+1080)
        elif self.whereends=='nowhere':# cant reach
            self.xygoal=(1280+300,0)
        else:
            self.xygoal=(1280+300,0)# cant reach
        #
        # layering
        self.staticactor00=obj_grandactor(self,(640,360))
        self.staticactor01=obj_grandactor(self,(640,360))
        self.staticactor02=obj_grandactor(self,(640,360))
        self.staticactor10=obj_grandactor(self,(640,360))
        self.staticactor11=obj_grandactor(self,(640,360))
        self.staticactor12=obj_grandactor(self,(640,360))
        self.staticactor20=obj_grandactor(self,(640,360))
        self.staticactor21=obj_grandactor(self,(640,360))
        self.staticactor22=obj_grandactor(self,(640,360))
        self.staticactor03=obj_grandactor(self,(640,360))
        self.staticactor13=obj_grandactor(self,(640,360))
        self.staticactor23=obj_grandactor(self,(640,360))
        # others
        self.staticactorplus=obj_grandactor(self,(640,360))
        self.hero=obj_grandactor(self,(640,360))# hero
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_undoneenter=obj_grandactor(self,(640,360))
        self.text_done=obj_grandactor(self,(640,360))
        #
        # background world (12 panels 0-1-2 left right, 0-1-2-3 top down, each 1280x720)
        self.panels=[]
        self.panels.append(self.staticactor00)
        self.panels.append(self.staticactor01)
        self.panels.append(self.staticactor02)
        self.panels.append(self.staticactor10)
        self.panels.append(self.staticactor11)
        self.panels.append(self.staticactor12)
        self.panels.append(self.staticactor20)
        self.panels.append(self.staticactor21)
        self.panels.append(self.staticactor22)
        self.panels.append(self.staticactor03)
        self.panels.append(self.staticactor13)
        self.panels.append(self.staticactor23)
        self.panels.append(self.staticactorplus)
        # offsets
        self.staticactor00.xymapoff=(-1280,-1080)
        self.staticactor01.xymapoff=(-1280,0)
        self.staticactor02.xymapoff=(-1280,1080)
        self.staticactor10.xymapoff=(0,-1080)
        self.staticactor11.xymapoff=(0,0)
        self.staticactor12.xymapoff=(0,1080)
        self.staticactor20.xymapoff=(1280,-1080)
        self.staticactor21.xymapoff=(1280,0)
        self.staticactor22.xymapoff=(1280,1080)
        self.staticactor03.xymapoff=(-1280,1080+1080)
        self.staticactor13.xymapoff=(0,1080+1080)
        self.staticactor23.xymapoff=(1280,1080+1080)
        #
        # central panel 1-1: hero house (always shown)
        # textpass=share.datamanager.getword('housename')
        self.staticactor11.addpart( 'textref', draw.obj_textbox('Home Sweet Home',(640,360+120),color=share.colors.location) )
        self.staticactor11.addpart( 'ref', draw.obj_image('house',(640,360),scale=0.5) )
        if 'pond' not in self.removelist:
            self.staticactor11.addpart( 'textref2', draw.obj_textbox('Pond',(640-320,360-180+120),color=share.colors.location) )
            self.staticactor11.addpart( 'ref2', draw.obj_image('pond',(640-320,360-180),scale=0.5) )
        self.staticactor11.addpart( 'ref3', draw.obj_image('mailbox',(834,182),scale=0.25) )
        #
        if 'garden' not in self.removelist:
            self.staticactor11.addpart( 'textref3', draw.obj_textbox('Garden',(640+320+100,360+120),color=share.colors.location) )
        if 'flower' not in self.removelist:
            self.staticactor11.addpart( "img1", draw.obj_image('flower',(925+100,362),scale=0.34,rotate=0,fliph=False,flipv=False) )
            self.staticactor11.addpart( "img2", draw.obj_image('flower',(990+100,266),scale=0.34,rotate=0,fliph=True,flipv=False) )
            self.staticactor11.addpart( "img3", draw.obj_image('flower',(1040+100,369),scale=0.34,rotate=0,fliph=False,flipv=False) )
            self.staticactor11.addpart( "img4", draw.obj_image('flower',(1103+100,259),scale=0.34,rotate=0,fliph=False,flipv=False) )
            self.staticactor11.addpart( "img5", draw.obj_image('flower',(851+100,280),scale=0.34,rotate=0,fliph=True,flipv=False) )
        if 'bush' not in self.removelist:
            self.staticactor11.addpart( "img6", draw.obj_image('bush',(523,170),scale=0.34,rotate=0,fliph=True,flipv=False) )
            self.staticactor11.addpart( "img7", draw.obj_image('bush',(214,46),scale=0.34,rotate=0,fliph=True,flipv=False) )
            self.staticactor11.addpart( "img8", draw.obj_image('bush',(164,261),scale=0.34,rotate=0,fliph=False,flipv=False) )
        if self.chapter>=8:
            self.staticactor11.addpart( 'refcake', draw.obj_image('cake',(640+210,360-50),scale=0.25) )
            self.staticactor11.addpart( 'refmark_cake', draw.obj_image('exclamationmarkred',(640+210,360-50),scale=0.5,path='data/premade') )
            self.staticactor11.addpart( 'textrefcake', draw.obj_textbox('Credits',(640+210,360-50+70),color=share.colors.location) )
            #
            self.staticactor11.addpart( 'refroam_bug', draw.obj_image('bug',(640-150,360),scale=0.25) )
            self.staticactor11.addpart( 'refmark_home', draw.obj_image('exclamationmarkred',(640,360),scale=0.5,path='data/premade') )
            self.staticactor11.addpart( 'refmark_pond', draw.obj_image('exclamationmarkred',(640-320,360-180),scale=0.5,path='data/premade') )
            self.staticactor11.addpart( 'refroam_mech', draw.obj_image('villainmechbase_noface',(1100,10),scale=0.4,rotate=-118,fliph=False,flipv=False) )
            self.staticactor11.addpart( 'refmark_mech', draw.obj_image('exclamationmarkred',(1100,10),scale=0.5,path='data/premade') )
            #
        if self.chapter>=8 or self.minigame=='flowers':
            self.staticactor11.addpart( 'refroam_partner', draw.obj_image('partnerbase',(172-50,571),scale=0.25,fliph=False) )
        if self.chapter>=8:
            self.staticactor11.addpart( 'refmark_atpartner', draw.obj_image('exclamationmarkred',(172,571),scale=0.5,path='data/premade') )


        #
        # west panel 0-1: villain tower
        if self.chapter>=3:
            self.staticactor01.addpart( 'textref', draw.obj_textbox('evil tower',(640,360+120),color=share.colors.location) )
            self.staticactor01.addpart( 'ref', draw.obj_image('tower',(640,360),scale=0.5) )
            #
            self.staticactor01.addpart( "img2", draw.obj_image('mountain',(845,587),scale=0.57,rotate=0,fliph=True,flipv=False) )
            self.staticactor01.addpart( "img3", draw.obj_image('mountain',(1007,385),scale=0.44,rotate=0,fliph=True,flipv=False) )
            self.staticactor01.addpart( "img4", draw.obj_image('mountain',(404,499),scale=0.53,rotate=0,fliph=False,flipv=False) )
            self.staticactor01.addpart( "img5", draw.obj_image('mountain',(308,351),scale=0.3,rotate=0,fliph=False,flipv=False) )
            self.staticactor01.addpart( "img6", draw.obj_image('mountain',(508,162),scale=0.35,rotate=0,fliph=True,flipv=False) )
            self.staticactor01.addpart( "img7", draw.obj_image('mountain',(731,155),scale=0.44,rotate=0,fliph=True,flipv=False) )
            self.staticactor01.addpart( "img8", draw.obj_image('mountain',(987,526),scale=0.26,rotate=0,fliph=True,flipv=False) )
            self.staticactor01.addpart( "img9", draw.obj_image('mountain',(519,633),scale=0.26,rotate=0,fliph=False,flipv=False) )
            if self.chapter>=5:
                self.staticactor01.addpart( "img12", draw.obj_image('cloud',(794,59),scale=0.26,rotate=0,fliph=True,flipv=False) )
                self.staticactor01.addpart( "img13", draw.obj_image('cloud',(421,69),scale=0.32,rotate=0,fliph=False,flipv=False) )
                self.staticactor01.addpart( "img14", draw.obj_image('cloud',(627,570),scale=0.28,rotate=0,fliph=True,flipv=False) )
        if self.chapter>=8:
            self.staticactor01.addpart( 'refroam', draw.obj_image('villainbase',(640-150,360),scale=0.25) )
            self.staticactor01.addpart( 'refmark_tower', draw.obj_image('exclamationmarkred',(640,360),scale=0.5,path='data/premade') )
        #
        # east panel 2-1: magical forest and cave
        if self.chapter>=4:
            self.staticactor21.addpart( 'textref', draw.obj_textbox('magical cave',(640,360+120),color=share.colors.location) )
            self.staticactor21.addpart( 'ref', draw.obj_image('cave',(640,360),scale=0.5) )
            #
            self.staticactor21.addpart( "img1", draw.obj_image('tree',(377,210),scale=0.46,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img2", draw.obj_image('tree',(395,512),scale=0.46,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img3", draw.obj_image('tree',(826,137),scale=0.46,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img4", draw.obj_image('tree',(919,331),scale=0.46,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img5", draw.obj_image('tree',(843,514),scale=0.44,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img6", draw.obj_image('tree',(1112,616),scale=0.44,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img7", draw.obj_image('tree',(520,698),scale=0.44,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img8", draw.obj_image('tree',(552,6),scale=0.44,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img9", draw.obj_image('tree',(935,670),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img10", draw.obj_image('tree',(243,394),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img11", draw.obj_image('tree',(475,350),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img12", draw.obj_image('tree',(667,164),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img13", draw.obj_image('tree',(997,477),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img14", draw.obj_image('tree',(682,624),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.staticactor21.addpart( "img15", draw.obj_image('tree',(129,131),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.staticactor21.addpart( "img16", draw.obj_image('tree',(185,644),scale=0.36,rotate=0,fliph=True,flipv=False) )
        if self.chapter>=8:
            self.staticactor21.addpart( 'refroam', draw.obj_image('bunnybase',(640+150,360),scale=0.25,fliph=True) )
            self.staticactor21.addpart( 'refmark_cave', draw.obj_image('exclamationmarkred',(640,360),scale=0.5,path='data/premade') )
        #
        # north panel 1-0: highest peak
        if self.chapter>=5:
            self.staticactor10.addpart( 'textref', draw.obj_textbox('highest peak',(640,200+220),color=share.colors.location) )
            self.staticactor10.addpart( 'imgref', draw.obj_image('mountain',(640,200)) )
            #
            self.staticactor10.addpart( "img1a", draw.obj_image('cloud',(865,205),scale=0.38,rotate=0,fliph=False,flipv=False) )
            self.staticactor10.addpart( "img2a", draw.obj_image('cloud',(417,151),scale=0.45,rotate=0,fliph=True,flipv=False) )
            self.staticactor10.addpart( "img3a", draw.obj_image('lightningbolt',(640,8),scale=0.33,rotate=0,fliph=True,flipv=False) )
            self.staticactor10.addpart( "img4a", draw.obj_image('lightningbolt',(500,31),scale=0.33,rotate=-34,fliph=True,flipv=False) )
            self.staticactor10.addpart( "img5a", draw.obj_image('lightningbolt',(800,30),scale=0.33,rotate=-30,fliph=False,flipv=False) )
        if self.chapter>=8:
            self.staticactor10.addpart( 'refroam', draw.obj_image('elderbase',(640-150,200+100),scale=0.25) )
            self.staticactor10.addpart( 'refmark_peak', draw.obj_image('exclamationmarkred',(640,360-50),scale=0.5,path='data/premade') )
        # north east panel 2-0: sun and horizon
        if self.chapter>=5:
            self.staticactor20.addpart( "img1", draw.obj_image('sun',(1009,167),scale=0.68,rotate=0,fliph=False,flipv=False) )
            self.staticactor20.addpart( "img2", draw.obj_image('cloud',(735,141),scale=0.43,rotate=0,fliph=False,flipv=False) )
            self.staticactor20.addpart( "img3", draw.obj_image('cloud',(231,203),scale=0.35,rotate=0,fliph=True,flipv=False) )
            self.staticactor20.addpart( "img4", draw.obj_image('cloud',(1203,327),scale=0.24,rotate=0,fliph=False,flipv=False) )
            self.staticactor20.addpart( "img5", draw.obj_image('tree',(733,539),scale=0.42,rotate=0,fliph=False,flipv=False) )
            self.staticactor20.addpart( "img6", draw.obj_image('tree',(859,691),scale=0.32,rotate=0,fliph=True,flipv=False) )
            self.staticactor20.addpart( "img7", draw.obj_image('tree',(406,325-50),scale=0.41,rotate=0,fliph=False,flipv=False) )
        # north west panel 0-0: moon and horizon
        if self.chapter>=5:
            self.staticactor00.addpart( "img1", draw.obj_image('moon',(1280-1009,167),scale=0.68,rotate=0,fliph=False,flipv=False) )
            self.staticactor00.addpart( "img2", draw.obj_image('cloud',(1280-735,141),scale=0.43,rotate=0,fliph=False,flipv=False) )
            self.staticactor00.addpart( "img3", draw.obj_image('cloud',(1280-231,203),scale=0.35,rotate=0,fliph=True,flipv=False) )
            self.staticactor00.addpart( "img4", draw.obj_image('cloud',(1280-1203,327),scale=0.24,rotate=0,fliph=False,flipv=False) )
            self.staticactor00.addpart( "img5", draw.obj_image('bush',(1280-733,539),scale=0.42,rotate=0,fliph=False,flipv=False) )
            self.staticactor00.addpart( "img6", draw.obj_image('bush',(1280-859,691),scale=0.32,rotate=0,fliph=True,flipv=False) )
            self.staticactor00.addpart( "img7", draw.obj_image('bush',(1280-406,325-50),scale=0.41,rotate=0,fliph=False,flipv=False) )
        #
        # south panel 1-2: beach south
        if self.chapter>=6:
            self.staticactor12.addpart( "img1", draw.obj_image('palmtree',(491,186),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor12.addpart( "img2", draw.obj_image('palmtree',(1145,176),scale=0.5,rotate=0,fliph=True,flipv=False) )
            self.staticactor12.addpart( "img1a", draw.obj_image('wave',(937,499),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor12.addpart( "img2a", draw.obj_image('wave',(452,714),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor12.addpart( "img3a", draw.obj_image('wave',(128,502),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor12.addpart( "img6", draw.obj_image('cloud',(995,1000),scale=0.4,rotate=0,fliph=True,flipv=False) )
        # south panel 2-2: beach south east
        if self.chapter>=6:
            self.staticactor22.addpart( "img1", draw.obj_image('palmtree',(231,228),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img2", draw.obj_image('palmtree',(995,63),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img3", draw.obj_image('wave',(1068,345),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img4", draw.obj_image('wave',(855,578),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img5", draw.obj_image('wave',(32,605),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img6", draw.obj_image('wave',(400,456),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor22.addpart( "img7", draw.obj_image('cloud',(295,715+100),scale=0.4,rotate=0,fliph=False,flipv=False) )
        #
        # south panel 0-2: beach south west
        if self.chapter>=6:
            if self.addsailorwait:
                self.staticactor02.addpart( 'ref', draw.obj_image('sailorbase',(640-50,360-120),scale=0.25) )
            if self.addbeachquestionmark:
                pass# NOT NEEDED, WE HAVE THE RED MARKER NOW
                # self.staticactor02.addpart( 'refqmark', draw.obj_image('interrogationmark',(640,360-120),path='data/premade') )
            if self.addbeachmark:
                pass# NOT NEEDED, WE HAVE THE RED MARKER NOW
                # self.staticactor02.addpart( 'refmark', draw.obj_image('smallcross',(640,360-120),path='data/premade') )
            self.staticactor02.addpart( 'textref', draw.obj_textbox('beach',(640,360),color=share.colors.location) )
            self.staticactor02.addpart( "img1", draw.obj_image('palmtree',(1040,199),scale=0.5,rotate=0,fliph=True,flipv=False) )
            self.staticactor02.addpart( "img2", draw.obj_image('palmtree',(255,21),scale=0.5,rotate=0,fliph=True,flipv=False) )
            self.staticactor02.addpart( "img3", draw.obj_image('palmtree',(776,3),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor02.addpart( "img1a", draw.obj_image('wave',(281,341),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor02.addpart( "img2a", draw.obj_image('wave',(501,610),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor02.addpart( "img3a", draw.obj_image('wave',(1062,511),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor02.addpart( "img4a", draw.obj_image('cloud',(998,705),scale=0.4,rotate=0,fliph=False,flipv=False) )
        if self.chapter>=8:
            self.staticactor02.addpart( 'refroam', draw.obj_image('sailorbase',(640-70,360-120),scale=0.25) )
            self.staticactor02.addpart( 'refroam_cow', draw.obj_image('cow',(640-70-100,360-120-200),scale=0.4) )
            self.staticactor02.addpart( 'refmark_atsailor', draw.obj_image('exclamationmarkred',(640,360-120),scale=0.5,path='data/premade') )
        # south-south east panel 2-3: island south east
        if self.chapter>=6:
            self.staticactor23.addpart( 'textref', draw.obj_textbox('Skull Island',(640,360+120),color=share.colors.location) )
            self.staticactor23.addpart( 'imgref', draw.obj_image('island1',(640,360),path='data/premade') )
            self.staticactor23.addpart( 'imgref2', draw.obj_image('skeletonhead',(640,360),scale=0.5) )
            self.staticactor23.addpart( "img1", draw.obj_image('mountain',(392,319),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img2", draw.obj_image('mountain',(224,280),scale=0.35,rotate=0,fliph=True,flipv=False) )
            self.staticactor23.addpart( "img3", draw.obj_image('mountain',(371,165),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img4", draw.obj_image('palmtree',(870,470),scale=0.4,rotate=0,fliph=True,flipv=False) )
            self.staticactor23.addpart( "img5", draw.obj_image('palmtree',(1017,418),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img2a", draw.obj_image('cloud',(774,123),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img3a", draw.obj_image('wave',(329,11),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img4a", draw.obj_image('wave',(25,170),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor23.addpart( "img5a", draw.obj_image('cloud',(978,255),scale=0.4,rotate=0,fliph=True,flipv=False) )
        if self.chapter>=8:
            self.staticactor23.addpart( 'refroam', draw.obj_image('skeletonbase',(640+150,360),scale=0.25,fliph=True) )
            self.staticactor23.addpart( 'refmark_island', draw.obj_image('exclamationmarkred',(640,360),scale=0.5,path='data/premade') )
        # south-south panel 1-3: just ocean
        if self.chapter>=6:
            self.staticactor13.addpart( "img1", draw.obj_image('wave',(1053,445),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor13.addpart( "img2", draw.obj_image('wave',(744,150),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor13.addpart( "img3", draw.obj_image('wave',(48,345),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor13.addpart( "img4", draw.obj_image('wave',(259,28),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor13.addpart( "img5", draw.obj_image('cloud',(333,421),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # south-south west panel 0-3: just ocean
        if self.chapter>=6:
            self.staticactor03.addpart( "img2", draw.obj_image('wave',(858,112),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor03.addpart( "img6", draw.obj_image('cloud',(905,298),scale=0.4,rotate=0,fliph=False,flipv=False) )
        #
        # Move all panels
        for i in self.panels:
            for j in i.dict.values():
                j.movex(i.xymapoff[0])
                j.movey(i.xymapoff[1])
        #
        # individual elements
        if self.chapter>=3:# west
            pass
            # self.staticactorplus.addpart( "imgw1", draw.obj_image('path1',(640-640,360+0),path='data/premade',fliph=True) )
        if self.chapter>=5:# north
            # self.staticactorplus.addpart( "imgn1", draw.obj_image('path2',(640+0,360-540),rotate=90,path='data/premade') )
            self.staticactorplus.addpart( "imgn2", draw.obj_image('horizon1',(640,360-1080-50),path='data/premade') )
            self.staticactorplus.addpart( "imgn3", draw.obj_image('horizon2',(1280+320,360-1080-50),path='data/premade') )
            self.staticactorplus.addpart( "imgn4", draw.obj_image('horizon3',(1280+640+320,360-1080+180-50),path='data/premade') )
            self.staticactorplus.addpart( "imgn5", draw.obj_image('horizon4',(-640+320,360-1080-50),path='data/premade') )# redo this
            self.staticactorplus.addpart( "imgn6", draw.obj_image('horizon3',(-1280+640-320,360-1080+180-50),path='data/premade',fliph=True) )
        if self.chapter>=6:# south
            self.staticactorplus.addpart( "imgs1", draw.obj_image('beach1',(640,360+1080),path='data/premade') )
            self.staticactorplus.addpart( "imgs2", draw.obj_image('beach2',(640+1280-320,360+1080),path='data/premade') )
            self.staticactorplus.addpart( "imgs3", draw.obj_image('beach3',(640+1280+320,360+1080-180),path='data/premade') )
            self.staticactorplus.addpart( "imgs4", draw.obj_image('beach4',(640-1280+320,360+1080),path='data/premade') )
            self.staticactorplus.addpart( "imgs5", draw.obj_image('beach3',(640-1280-320,360+1080-180),fliph=True,path='data/premade') )

        # ADD MARKER TO GOAL
        if not (self.multiplegoals or self.whereends=='everywhere' or self.whereends=='nowhere'):
            tempo=(640+self.xygoal[0],360+self.xygoal[1])
            self.staticactorplus.addpart( 'refmark_goal', draw.obj_image('exclamationmarkred',tempo,scale=0.5,path='data/premade') )

        ###############
        # boundaries (chapter dependent. At max should be +-1280,+-720, with small additional margin  )
        self.xbm=50#50# margin
        self.ybm=50#50
        if self.chapter in [1,2]:# just roam around the house
            self.xhwmax=640
            self.xhwmin=-640
            self.yhwmax=360
            self.yhwmin=-360
        elif self.chapter == 3:# can go west
            self.xhwmax=640
            self.xhwmin=-1280-self.xbm
            self.yhwmax=360
            self.yhwmin=-360
        elif self.chapter == 4:# can go west and east
            self.xhwmax=1280+self.xbm
            self.xhwmin=-1280-self.xbm
            self.yhwmax=360
            self.yhwmin=-360
        elif self.chapter==5:# can go north too
            self.xhwmax=1280+self.xbm
            self.xhwmin=-1280-self.xbm
            self.yhwmax=360
            self.yhwmin=-1080-self.ybm
        elif self.chapter==6:# can go south too (so everywhere)
            if self.hasboat:# can sail (further south)
                self.xhwmax=1280+self.xbm
                self.xhwmin=-1280-self.xbm
                self.yhwmax=1080+1080+self.ybm
                self.yhwmin=-1080-self.ybm
            else:# can only go on the southern beach
                self.xhwmax=1280+self.xbm
                self.xhwmin=-1280-self.xbm
                self.yhwmax=1080+self.ybm
                self.yhwmin=-1080-self.ybm
        else:# can go everywhere
            self.xhwmax=1280+self.xbm
            self.xhwmin=-1280-self.xbm
            self.yhwmax=1080+1080+self.ybm
            self.yhwmin=-1080-self.ybm
        ###############
        # hero (+1 unique buddy walking along)
        if self.addpartner:
            self.hero.addpart( 'pface_right', draw.obj_image('partnerbase',(640+30,360-30),scale=0.25) )
            self.hero.addpart( 'pface_left', draw.obj_image('partnerbase',(640+30,360-30),scale=0.25,fliph=True) )
            self.hero.addpart( 'pwalk_right', draw.obj_image('partnerwalk',(640+30,360-30),scale=0.25) )
            self.hero.addpart( 'pwalk_left', draw.obj_image('partnerwalk',(640+30,360-30),scale=0.25,fliph=True) )
        elif self.addsailor:
            self.hero.addpart( 'pface_right', draw.obj_image('sailorbase',(640+30,360-30),scale=0.25) )
            self.hero.addpart( 'pface_left', draw.obj_image('sailorbase',(640+30,360-30),scale=0.25,fliph=True) )
            self.hero.addpart( 'pwalk_right', draw.obj_image('sailorwalk',(640+30,360-30),scale=0.25) )
            self.hero.addpart( 'pwalk_left', draw.obj_image('sailorwalk',(640+30,360-30),scale=0.25,fliph=True) )
        self.hero.addpart( 'face_right', draw.obj_image('herobase',(640,360),scale=0.25) )
        self.hero.addpart( 'face_left', draw.obj_image('herobase',(640,360),scale=0.25,fliph=True) )
        self.hero.addpart( 'walk_right', draw.obj_image('herowalk',(640,360),scale=0.25) )
        self.hero.addpart( 'walk_left', draw.obj_image('herowalk',(640,360),scale=0.25,fliph=True) )
        self.hero.addpart( 'boat_right', draw.obj_image('sailboat',(640,360),scale=0.25) )
        self.hero.addpart( 'boat_left', draw.obj_image('sailboat',(640,360),scale=0.25,fliph=True) )

        self.herofaceright=True
        self.herowalking=False# hero walking or standing
        self.herosails=False# hero is sailing (obsolete notation)
        self.herosailing=self.herosails# hero is sailing or not
        self.heronearpeak=False# hero is near the peak (play wind sound ambience)
        self.hero.dict['face_right'].show=not self.herosails and (self.herofaceright and not self.herowalking)
        self.hero.dict['face_left'].show=not self.herosails and (not self.herofaceright and not self.herowalking)
        self.hero.dict['walk_right'].show=not self.herosails and (self.herofaceright and self.herowalking)
        self.hero.dict['walk_left'].show=not self.herosails and (not self.herofaceright and self.herowalking)
        self.hero.dict['boat_right'].show=self.herosails and self.herofaceright
        self.hero.dict['boat_left'].show=self.herosails and not self.herofaceright
        if self.addpartner or self.addsailor:
            self.hero.dict['pface_right'].show=self.hero.dict['face_right'].show
            self.hero.dict['pface_left'].show=self.hero.dict['face_left'].show
            self.hero.dict['pwalk_right'].show=self.hero.dict['walk_right'].show
            self.hero.dict['pwalk_left'].show=self.hero.dict['walk_left'].show

        self.herowalktimer=tool.obj_timer(10)# timer to alternate walk slides
        self.herowalkframe1=True# alternate True/False for two frames
        self.herospeed=6# hero walking speed
        self.heromx=self.herospeed# moving rate
        self.heromy=self.herospeed# moving rate
        # goal(s) to reach
        self.hitboxes=[]# may track several locations
        if not self.multiplegoals:
            self.goalarea=obj_grandactor(self,self.xygoal)
            self.goalarea.rx=100
            self.goalarea.ry=100
            self.hitboxes.append(self.goalarea)
        else:
            self.allgoalareas={}# dictionary of goal objects
            for i in self.allxygoals.keys():
                goalarea=obj_grandactor(self,self.allxygoals[i])
                goalarea.rx=100
                goalarea.ry=100
                self.allgoalareas[i]=goalarea
                self.hitboxes.append(goalarea)
        ####
        # End of Setup: place hero (move background+hitboxes)
        self.xhw=self.xyhero[0]# relative to world (0,0 = house)
        self.yhw=self.xyhero[1]
        for j in self.panels:
            for i in j.dict.values():# move world
                i.movex(-self.xhw)
                i.movey(-self.yhw)
        for k in self.hitboxes:
            k.movex(640-self.xhw)
            k.movey(360-self.yhw)
        #
        # text rect for main body
        # image1=draw.obj_image('textbanner',(640,70),path='data/premade')# Not great
        # self.text_undone.addpart('textwhiterect', image1)
        # text
        self.text_undone.addpart( 'text1', \
        draw.obj_textbox('['+share.datamanager.controlname('arrows')+': move]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        if self.addsailorwait or self.addbeachmark:# talk to a character
            self.text_undoneenter.addpart( 'textenter', draw.obj_textbox('['+share.datamanager.controlname('action')+': talk]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        elif self.addbeachquestionmark:# investigate
            self.text_undoneenter.addpart( 'textenter', draw.obj_textbox('['+share.datamanager.controlname('action')+': investigate]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        elif self.chapter>=8:
            self.text_undoneenter.addpart( 'textenter', draw.obj_textbox('['+share.datamanager.controlname('action')+': interact]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        elif self.minigame=='flowers':
            self.text_undoneenter.addpart( 'textenter', draw.obj_textbox('['+share.datamanager.controlname('action')+': give flower]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        else:# enter a location
            self.text_undoneenter.addpart( 'textenter', draw.obj_textbox('['+share.datamanager.controlname('action')+': go inside]',(640,680),color=share.colors.instructions,fillcolor=share.colors.white) )
        #
        self.text_done.addpart( 'text1', draw.obj_textbox('We made it!',(640,680),fillcolor=share.colors.white) )
        self.text_undone.show=True
        self.text_undoneenter.show=False
        self.text_done.show=False
        # timer
        self.timerend=tool.obj_timer(60)# goal to done
        # audio
        self.soundenter=draw.obj_sound('travel_enter')
        self.creator.addpart(self.soundenter)
        # ambience sounds (add to page!)
        if self.doambience:
            self.soundambience_forest=draw.obj_sound('travel_forest')
            self.creator.addpart(self.soundambience_forest)
            self.soundambience_ocean=draw.obj_sound('travel_ocean')
            self.creator.addpart(self.soundambience_ocean)
            self.soundambience_winds=draw.obj_sound('travel_winds')
            self.creator.addpart(self.soundambience_winds)
            #
            self.ambiencesoundname='forest'# name of ambience sound name (default one)
            self.soundambience=self.soundambience_forest
            self.soundambience.play(loop=True)# should die when exit page

        #####
        # minigame flowers
        # *FLOWERS
        self.flowercount=0# picked flowers
        self.flowerneed=1# needed flowers for goal
        self.floweractors=[]# make a list of grandactors flowers
        if self.minigame=='flowers':
            if self.flowerneed == 1:
                self.flowermessage=draw.obj_textbox('You have collected 0/'+str(self.flowerneed)+' flower',(640,610),color=share.colors.instructions,fillcolor=share.colors.white)
            else:
                self.flowermessage=draw.obj_textbox('You have collected 0/'+str(self.flowerneed)+' flowers',(640,610),color=share.colors.instructions,fillcolor=share.colors.white)
            self.text_undone.addpart( 'textflowers', self.flowermessage  )
            for i in self.panels:# remove flower from panels and make them into individual grandactors
                panelflowerkeys=[]# list of flowers keys in this panel
                for k in i.dict.keys():# browse elements
                    j=i.dict[k]
                    if j.type=='image' and j.name=='flower':
                        passactor=obj_grandactor(self,(j.x,j.y),foreground=False)# make a new grandactor (in background)
                        j.xytoxyini()# reinitialize initial coordinates of image
                        passactor.addpart('img', j )# add flower image to it
                        passactor.rx=25# hitbox
                        passactor.ry=25
                        self.floweractors.append(passactor)
                        panelflowerkeys.append(k)
                for j in panelflowerkeys:# remove flowers from panels
                    i.removepart(j)
            for k in self.floweractors:# append flower actors to tracked hitboxes
                self.hitboxes.append(k)
            self.soundpickflower=draw.obj_sound('travel_pickflower')
            self.creator.addpart(self.soundpickflower)
        #
        #####
        # minigame logs (go on logs an pickup with Space)
        # *LOG
        self.logcount=0# picked logs
        self.logneed=10# needed logs for goal
        self.logactors=[]# make a list of grandactors logs
        if self.minigame=='logs':
            self.logmessage=draw.obj_textbox('You have collected 0/'+str(self.logneed)+' logs',(640,610),color=share.colors.instructions,fillcolor=share.colors.white)
            self.text_undone.addpart( 'textlogs', self.logmessage  )
            # self.text_undone.dict['text1'].replacetext('Move with [W][A][S][D]')
            for i in self.panels:# remove tree from panels and make them into individual grandactors
                panellogkeys=[]# list of tree keys in this panel
                for k in i.dict.keys():# browse elements
                    j=i.dict[k]
                    if j.type=='image' and (j.name=='tree' or j.name=='palmtree'):
                        passactor=obj_grandactor(self,(j.x,j.y))# make a new grandactor
                        j.xytoxyini()# reinitialize initial coordinates of image
                        passactor.addpart('img', j )# add flower image to it
                        passactor.rx=75# hitbox
                        passactor.ry=75
                        self.logactors.append(passactor)
                        panellogkeys.append(k)
                for j in panellogkeys:# remove trees from panels
                    i.removepart(j)
            for k in self.logactors:# append log actors to tracked hitboxes
                self.hitboxes.append(k)
            #
            self.soundlogchop=draw.obj_sound('travel_chop')
            self.creator.addpart(self.soundlogchop)
            self.soundlogchoplast=draw.obj_sound('travel_choplast')
            self.creator.addpart(self.soundlogchoplast)
    #
    #############################################################
    def reachgoal(self,controls):# check contact with goal
        if not self.multiplegoals:
            if tool.checkrectcollide(self.hero,self.goalarea):# contact with goal
                self.text_undone.show=False# message to enter on contact
                self.text_undoneenter.show=True
                if controls.ga and controls.gac:# enter goal
                    if self.noending:
                        self.goal=True
                        self.done=True
                    else:
                        self.goal=True
                        self.timerend.start()
                        self.text_undone.show=False
                        self.text_undoneenter.show=False
                        self.text_done.show=True
                        self.soundenter.play()
            else:
                self.text_undone.show=True
                self.text_undoneenter.show=False
        else:# multiple end locations
            self.text_undone.show=True
            self.text_undoneenter.show=False
            for i in self.allxygoals.keys():
                if tool.checkrectcollide(self.hero,self.allgoalareas[i]):# contact with goal
                    self.text_undone.show=False# message to enter on contact
                    self.text_undoneenter.show=True
                    if controls.ga and controls.gac:# enter goal
                        if self.noending:
                            self.goal=True
                            self.goalname=i
                            self.done=True
                        else:
                            self.goal=True
                            self.goalname=i
                            self.timerend.start()
                            self.text_undone.show=False
                            self.text_undoneenter.show=False
                            self.text_done.show=True
                            self.soundenter.play()

    ####
    def update(self,controls):
        super().update(controls)
        #
        # sounds
        if self.doambience:
            if self.herosailing:
                if self.ambiencesoundname !='ocean':# switch to sailing sound ambience
                    self.soundambience.stop()
                    self.soundambience=self.soundambience_ocean
                    self.soundambience.play(loop=True)
                    self.ambiencesoundname='ocean'
            else:
                self.heronearpeak=(self.yhw<-840 and self.xhw<640 and self.xhw>-640) or (self.xhw<-840 and self.yhw<360 and self.yhw>-360)# hero is near windy peak or villain lair
                if self.heronearpeak:
                    if self.ambiencesoundname !='winds':# switch to winds sound ambience
                        self.soundambience.stop()
                        self.soundambience=self.soundambience_winds
                        self.soundambience.play(loop=True)
                        self.ambiencesoundname='winds'
                else:
                    if self.ambiencesoundname !='forest':# switch to forest sound ambience
                        self.soundambience.stop()
                        self.soundambience=self.soundambience_forest
                        self.soundambience.play(loop=True)
                        self.ambiencesoundname='forest'


        if not self.goal:
            # goal unreached state
            # Hero motion
            if controls.gl:
                if self.xhw>self.xhwmin:# boundary
                    self.xhw -= self.heromx
                    for j in self.panels:
                        for i in j.dict.values():
                            i.movex(self.heromx)
                    for k in self.hitboxes:
                        k.movex(self.heromx)
                if controls.glc:
                    self.herofaceright=False
            if controls.gr:
                if self.xhw<self.xhwmax:
                    self.xhw += self.heromx
                    for j in self.panels:
                        for i in j.dict.values():
                            i.movex(-self.heromx)
                    for k in self.hitboxes:
                        k.movex(-self.heromx)
                    if controls.grc:
                        self.herofaceright=True
            if controls.gu:
                if self.yhw>self.yhwmin:
                    self.yhw -= self.heromy
                    for j in self.panels:
                        for i in j.dict.values():
                            i.movey(self.heromy)
                    for k in self.hitboxes:
                        k.movey(self.heromy)
            if controls.gd:
                if self.yhw<self.yhwmax:
                    self.yhw += self.heromy
                    for j in self.panels:
                        for i in j.dict.values():
                            i.movey(-self.heromy)
                    for k in self.hitboxes:
                        k.movey(-self.heromy)
            # tune the walking speed if diagonal:
            if (controls.gu or controls.gd) and (controls.gl or controls.gr):
                self.heromx=self.herospeed/tool.sqrt(2)
                self.heromy=self.herospeed/tool.sqrt(2)
            else:
                self.heromx=self.herospeed# moving rate
                self.heromy=self.herospeed# moving rate


            # Images from state= sailing, walking or standing
            self.herosailing=self.yhw>1080+self.ybm+10 and not (self.xhw>680 and self.yhw>1910)# separation land and sea (beach + skull island)
            if self.herosailing:
                self.herowalking=False
                self.hero.dict['boat_right'].show=self.herofaceright
                self.hero.dict['boat_left'].show=not self.herofaceright
                self.hero.dict['face_right'].show=False
                self.hero.dict['face_left'].show=False
                self.hero.dict['walk_right'].show=False
                self.hero.dict['walk_left'].show=False
            else:
                self.hero.dict['boat_right'].show=False
                self.hero.dict['boat_left'].show=False
                # walking or standing
                if controls.gl or controls.gr or controls.gu or controls.gd:
                    self.herowalking=True
                else:
                    self.herowalking=False
                # walking
                if self.herowalking:
                    if not self.herowalkframe1:
                        self.hero.dict['face_right'].show=self.herofaceright
                        self.hero.dict['face_left'].show=not self.herofaceright
                        self.hero.dict['walk_right'].show=False
                        self.hero.dict['walk_left'].show=False
                    else:
                        self.hero.dict['face_right'].show=False
                        self.hero.dict['face_left'].show=False
                        self.hero.dict['walk_right'].show=self.herofaceright
                        self.hero.dict['walk_left'].show=not self.herofaceright
                    # walking motion (2 frames)
                    self.herowalktimer.update()
                    if self.herowalktimer.ring:
                        self.herowalkframe1=not self.herowalkframe1
                        self.herowalktimer.start()
                else:# standing
                    self.hero.dict['face_right'].show=self.herofaceright
                    self.hero.dict['face_left'].show=not self.herofaceright
                    self.hero.dict['walk_right'].show=False
                    self.hero.dict['walk_left'].show=False
                    self.herowalktimer.start()# reset timer for next walking
            # partner when walking
            if self.addpartner or self.addsailor:
                self.hero.dict['pface_right'].show=self.hero.dict['face_right'].show
                self.hero.dict['pface_left'].show=self.hero.dict['face_left'].show
                self.hero.dict['pwalk_right'].show=self.hero.dict['walk_right'].show
                self.hero.dict['pwalk_left'].show=self.hero.dict['walk_left'].show
            #
            ######################
            # goals
            if not self.minigame:# no minigame, just reach a point on map
                self.reachgoal(controls)
            elif self.minigame=='flowers':# mini-game pickup some flowers
                if self.flowercount<self.flowerneed:
                    tokill=[]
                    for i in self.floweractors:
                        if tool.checkrectcollide(self.hero,i):
                            self.flowercount += 1
                            if self.flowerneed == 1:
                                self.flowermessage.replacetext('You have collected '+str(self.flowercount)+'/'+str(self.flowerneed)+' flower')
                            else:
                                self.flowermessage.replacetext('You have collected '+str(self.flowercount)+'/'+str(self.flowerneed)+' flowers')
                            tokill.append(i)
                    for i in tokill:
                        self.floweractors.remove(i)
                        i.clearparts()
                        i.kill()
                        self.soundpickflower.play()
                else:# when obtained all flowers can reach goal
                    self.reachgoal(controls)
            #
            elif self.minigame=='logs':# mini-game chop some wood
                if self.logcount<self.logneed:
                    tokill=[]
                    for i in self.logactors:
                        if tool.checkrectcollide(self.hero,i):
                            self.logcount += 1
                            self.logmessage.replacetext('You have collected '+str(self.logcount)+'/'+str(self.logneed)+' logs')
                            tokill.append(i)
                    for i in tokill:
                        self.logactors.remove(i)
                        i.clearparts()
                        i.kill()
                        self.soundlogchop.play()
                        if self.logcount==self.logneed:
                            self.soundlogchoplast.play()
                else:# when obtained all logs can reach goal
                    self.reachgoal(controls)
                    self.text_undone.dict['text1'].replacetext('['+share.datamanager.controlname('arrows')+']: move]')

        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame


####################################################################################################################

# Mini Game: dodge gun shots
#*DODGE *GUN
class obj_world_dodgegunshots(obj_world):
    def setup(self,**kwargs):
        # default options
        self.heroisangry=False# hero is angry during fight
        self.partnerisenemy=False# parnter is alongside enemy during fight
        self.intower=False# inside tower not outside
        self.dotutorial=False# do the tutorial
        self.dotrailer=False# do a trailer (control villain shooting)
        # scene tuning
        if kwargs is not None:
            if 'heroangry' in kwargs: self.heroisangry=kwargs["heroangry"]# OBSOLETE
            if 'partnerenemy' in kwargs: self.partnerisenemy=kwargs["partnerenemy"]# OBSOLETE
            if 'intower' in kwargs: self.intower=kwargs["intower"]
            if 'tutorial' in kwargs: self.dotutorial=kwargs["tutorial"]
            if 'trailer' in kwargs: self.dotrailer=kwargs["trailer"]
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached (doesnt necessarily mean game is won)
        self.win=True# game is won
        self.yoff=-50# offset for hero/villain
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.hero=obj_grandactor(self,(200,500+10+self.yoff))
        self.herodead=obj_grandactor(self,(640,360))
        self.villain=obj_grandactor(self,(640,360))
        self.texthurt=obj_grandactor(self,(640,360))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_donewin.show=False
        self.text_donelost.show=False
        self.text_start=obj_grandactor(self,(640,360))# text message at start
        self.text_start.show=True
        # static
        self.staticactor.addpart( 'floor', draw.obj_image('floor1',(640,500),path='data/premade') )
        # if not self.intower:
            # self.staticactor.addpart( 'floor', draw.obj_image('floor1',(640,500),path='data/premade') )
            # self.staticactor.addpart( 'sun', draw.obj_image('sun',(470,190),scale=0.4) )
        # hero
        self.hero.addpart( 'stand', draw.obj_image('herobase',(200,500+self.yoff),scale=0.5) )
        self.hero.addpart( 'crouch', draw.obj_image('herocrouch',(200,500+50+self.yoff),scale=0.5) )
        self.hero.dict['stand'].show=True
        self.hero.dict['crouch'].show=False
        self.herocrouch=False# crouching or not
        self.heromayjump=True# hero can jump (not if in the air)
        self.herodt=1# hero time increment
        self.herofy=0# hero force
        self.herov=0# hero velocity
        self.herog=1# gravity rate
        self.herod=0.05# dissipation rate
        self.heroj=25# jump rate
        self.heroy0=self.hero.y# hero.y of ground
        # hero is hurt
        self.texthurt.addpart( 'text', draw.obj_textbox('ouch!',(400,360),scale=1.5) )
        self.texthurting=False# hero is hurting
        self.texthurt.show=False
        self.texthurttimer=tool.obj_timer(30)
        # hero hitbox
        self.herohitbox1=obj_grandactor(self,(200,self.hero.y))# standing
        self.herohitbox1.rx=50
        self.herohitbox1.ry=140
        self.herohitbox2=obj_grandactor(self,(200+10,self.hero.y+50))# crouching
        self.herohitbox2.rx=130
        self.herohitbox2.ry=70
        # hero dies
        self.herodead.addpart('anim',draw.obj_animation('ch3_herodies','herobase',(640,360)))
        self.herodead.show=False
        # boundaries
        self.ymax=self.hero.y
        # partner with villain
        if self.partnerisenemy:
            self.villain.addpart( 'partnerstand', draw.obj_image('partnerbaseangry',(1280-150+100,450+self.yoff),scale=0.5,fliph=True) )
        # villain
        self.villain.addpart( 'stand', draw.obj_image('villainbase',(1280-150,450+self.yoff),scale=0.5,fliph=True) )
        self.villain.addpart( 'standgun', draw.obj_image('gun',(1280-150-175,445+self.yoff),scale=0.25,fliph=True) )
        self.villain.addpart( 'standarm', draw.obj_image('stickshootarm',(1280-260,442+self.yoff),scale=0.5,path='data/premade') )# missing small piece
        self.villain.addpart( 'crouch', draw.obj_image('villainshootcrouch',(1280-150,500+50+40+30-50+self.yoff),scale=0.5) )
        self.villain.addpart( 'crouchgun', draw.obj_image('gun',(1280-150-175,500+50+40+30-50+self.yoff),scale=0.25,fliph=True) )
        self.villain.dict['stand'].show=True
        self.villain.dict['crouch'].show=False
        self.villain.dict['standgun'].show=True
        self.villain.dict['standarm'].show=True
        self.villain.dict['crouchgun'].show=False
        self.villaincrouch=True# villain is crouching or not (switch randomly every shot)
        self.villainshots=15# number of shots
        self.villaintimer=80# shot reload time
        self.villaintimermin=50# min time
        self.villaintimerm=0.98# timer fact each shot
        self.villaintimershoot=tool.obj_timer(self.villaintimer,cycle=True)#timer between shots
        if not self.dotutorial:# cant start game if villain doesnt shoot
            self.villaintimershoot.start()
        # cannonballs
        self.cannonballs=[]# empty list
        # health bar
        self.maxherohealth=5# starting hero health (reference=always 3)
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(640,360))
        if self.dotutorial:
            self.ybar=150# for health bars and text
        else:
            self.ybar=50
        self.healthbar.addpart('face', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.maxherohealth):
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )
        # bullet count
        self.maxvillainshots=12
        self.villainshots=self.maxvillainshots
        self.bulletbar=obj_grandactor(self,(640,360))
        self.bulletbar.addpart('face', draw.obj_image('villainhead',(1280-50,self.ybar),scale=0.2,fliph=True) )
        for i in range(self.maxvillainshots):
            if i>int(self.maxvillainshots/2)-1:
                self.bulletbar.addpart('bullet_'+str(i), draw.obj_image('bullet',(1280-130-(i-int(self.maxvillainshots/2))*50-10,self.ybar-25),scale=0.125) )
            else:
                self.bulletbar.addpart('bullet_'+str(i), draw.obj_image('bullet',(1280-130-i*50-10,self.ybar+25),scale=0.125) )
        # text
        self.text_undone.addpart( 'text1', \
        draw.obj_textbox('['+share.datamanager.controlname('up')+': jump] ['+share.datamanager.controlname('down')+': crouch]',(640,660),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('{hero_he} is the one!',(640,360),fontsize='huge') )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('you are dead',(640,360),fontsize='huge') )
        # fight message at beginning
        self.timerfightmessage=tool.obj_timer(80)
        if not self.dotutorial:
            self.text_start.addpart( 'fightmessage', draw.obj_animation('dodgebullets_fightmessage','messagefight',(640,360), path='data/premade') )
            self.timerfightmessage.start()
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(190)# goal to done
        #
        self.soundshoot=draw.obj_sound('dodgebullets_shoot')
        self.creator.addpart(self.soundshoot)
        self.soundhit=draw.obj_sound('dodgebullets_hit')
        self.creator.addpart(self.soundhit)
        self.sounddie=draw.obj_sound('dodgebullets_die')
        self.creator.addpart(self.sounddie)
        self.soundwin=draw.obj_sound('dodgebullets_win')
        self.creator.addpart(self.soundwin)
        self.soundjump=draw.obj_sound('dodgebullets_jump')
        self.creator.addpart(self.soundjump)
        self.soundcrouch=draw.obj_sound('dodgebullets_crouch')
        self.creator.addpart(self.soundcrouch)
        #
        if not self.dotutorial:
            self.soundstart=draw.obj_sound('dodgebullets_start')
            self.soundstart.play()# at start
        #
    def makecannonball(self,x,y):# shoot
        self.soundshoot.play()
        cannonball=obj_grandactor(self,(x,y))
        cannonball.addpart('img', draw.obj_image('bullet',(x,y),scale=0.25,fliph=True) )
        cannonball.rx=15# hitbox
        cannonball.ry=15
        cannonball.r=15
        cannonball.speed=12#8#tool.randint(2,8)
        self.cannonballs.append(cannonball)
    def killcannonball(self,cannonball):
        self.cannonballs.remove(cannonball)
        cannonball.kill()
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # fight message at beginning
            if self.timerfightmessage.on:
                self.timerfightmessage.update()
                if self.timerfightmessage.ring:
                    self.text_start.show=False
            # goal unreached state
            # hero dynamics
            self.herofy=0# force
            self.herofy += self.herog# gravity
            if self.heromayjump and (controls.gu and controls.guc):# jump
                self.soundjump.play()
                self.herofy -= self.heroj
                self.herov=0# reset velocity
                self.heromayjump=False# cant jump again
            # hero dynamics
            self.herov += self.herodt*(self.herofy-self.herod*self.herov)# dtv=g+flap-dv**2
            self.hero.movey(self.herodt*self.herov)# dty=v
            # boundaries
            if self.hero.y>self.ymax:
                self.hero.movetoy(self.ymax)
                self.herov = 0# just stall
                self.heromayjump=True# may jump from ground
            # hero crouch
            if controls.gdc:
                if controls.gd:# switch to crouch
                    self.herocrouch=True
                    self.hero.dict['stand'].show=False
                    self.hero.dict['crouch'].show=True
                    self.soundcrouch.play()
                else:# switch to stand/jump
                    self.herocrouch=False
                    self.hero.dict['stand'].show=True
                    self.hero.dict['crouch'].show=False
            # hero hitbox (two for stand/crouch)
            self.herohitbox1.movetoy(self.hero.y)
            self.herohitbox2.movetoy(self.hero.y+50)
            #villainshoot
            self.villaintimershoot.update()
            if self.villainshots > 0: # villain can still shoot
                if self.villaintimershoot.ring:
                    # faster consecutive shots after first one
                    self.villaintimershoot.amount=max(self.villaintimershoot.amount*self.villaintimerm,self.villaintimermin)
                    if self.dotrailer:
                        self.villaincrouch=not self.villaincrouch
                    else:
                        self.villaincrouch=tool.randbool()# villain stands or crouches

                    if self.villaincrouch:# crouches
                        self.makecannonball(860,600+self.yoff-50)
                        self.villainshots -= 1
                        if self.villainshots>-1:
                            self.bulletbar.dict['bullet_'+str(self.villainshots)].show=False
                        self.villain.dict['stand'].show=False
                        self.villain.dict['crouch'].show=True
                        self.villain.dict['standgun'].show=False
                        self.villain.dict['standarm'].show=False
                        self.villain.dict['crouchgun'].show=True
                    else:# stands
                        self.makecannonball(860,425+self.yoff)
                        self.villainshots -= 1
                        if self.villainshots>-1:
                            self.bulletbar.dict['bullet_'+str(self.villainshots)].show=False
                        self.villain.dict['stand'].show=True
                        self.villain.dict['crouch'].show=False
                        self.villain.dict['standgun'].show=True
                        self.villain.dict['standarm'].show=True
                        self.villain.dict['crouchgun'].show=False
            else:# villain cant shoot. wait for all bullets to disappear to end mini-game and win
                if not self.cannonballs:
                    self.goal=True# reached goal
                    self.win=True# won minigame
                    self.timerendwin.start()
                    self.text_undone.show=False
                    self.text_donewin.show=True
                    self.texthurting=False
                    self.texthurt.show=False
                    self.soundwin.play()
            #cannonballs
            if self.cannonballs:
                for i in self.cannonballs:
                    i.movex(-i.speed)
                    if i.x<-50: self.killcannonball(i)# disappears on left edge of screen
                    # collision with hero
                    if not self.herocrouch:
                        hitboxcheck=self.herohitbox1#hero is standing
                    else:
                        hitboxcheck=self.herohitbox2# hero is crouching
                    if tool.checkrectcollide(i,hitboxcheck):# cannonball hits hero
                        self.killcannonball(i)
                        # hurt text
                        self.texthurting=True
                        self.texthurt.show=True
                        self.texthurttimer.start()
                        # hero looses health
                        self.herohealth -= 1
                        if self.herohealth>0:
                            self.soundhit.play()
                            self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        else:
                            # hero dies
                            self.sounddie.play()
                            self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                            self.goal=True# end minigame
                            self.win=False# lost minigame
                            self.timerendloose.start()
                            self.text_undone.show=False
                            self.text_donelost.show=True
                            self.texthurt.show=False
                            self.texthurting=False
                            self.hero.show=False
                            self.herodead.show=True
                            self.herodead.dict['anim'].rewind()
            #texthurt
            if self.texthurting:
                self.texthurttimer.update()
                if self.texthurttimer.ring:
                    self.texthurting=False
                    self.texthurt.show=False
        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                if self.timerendwin.ring:
                    self.done=True# end of minigame
            else:# lost minigame
                self.timerendloose.update()
                if self.timerendloose.ring:
                    self.done=True# end of minigame


####################################################################################################################

# Mini Game: stomp on each other fight
#*STOMP *FIGHT
class obj_world_stompfight(obj_world):
    def setup(self,**kwargs):

        ##########################3
        # Premake necessary images
        # combine stickkick+villainhead=villainkick
        image1=draw.obj_image('stickkick',(640,460),path='data/premade')# snapshot
        image2=draw.obj_image('villainhead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,300,300),'villainkick')
        # combine stickkick+herohead=herokick
        image1=draw.obj_image('stickkick',(640,460),path='data/premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,300,300),'herokick')

        # default options
        self.heroisangry=False# hero is angry during fight
        self.partnerisenemy=False# parnter is alongside enemy during fight
        self.dotutorial=False# do the tutorial
        # scene tuning
        if kwargs is not None:
            if 'heroangry' in kwargs: self.heroisangry=kwargs["heroangry"]# OBSOLETE
            if 'partnerenemy' in kwargs: self.partnerisenemy=kwargs["partnerenemy"]# OBSOLETE
            if 'tutorial' in kwargs: self.dotutorial=kwargs["tutorial"]
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached (doesnt necessarily mean game is won)
        self.win=True# game is won when goal is reached or not
        self.xmin=50
        self.xmax=1280-50
        self.yground=580# ground
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.villain=obj_grandactor(self,(940,self.yground-12))
        self.hero=obj_grandactor(self,(340,self.yground))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_donewin.show=False
        self.text_donelost.show=False
        self.text_start=obj_grandactor(self,(640,360))# text message at start
        self.text_start.show=True
        # static
        self.staticactor.addpart( 'floor', draw.obj_image('floor2',(640,self.yground+90),path='data/premade') )
        # self.staticactor.addpart( 'sun', draw.obj_image('sun',(640,280),scale=0.4) )
        # hero
        self.hero.addpart( 'stand_right', draw.obj_image('herobase',(340,self.yground),scale=0.35) )
        self.hero.addpart( 'stand_left', draw.obj_image('herobase',(340,self.yground),scale=0.35,fliph=True) )
        self.hero.addpart( 'hurt', draw.obj_image('herobase',(340,self.yground+70),scale=0.35,rotate=90) )
        self.hero.addpart( 'kick_right', draw.obj_image('herokick',(340,self.yground),scale=0.35) )
        self.hero.addpart( 'kick_left', draw.obj_image('herokick',(340,self.yground),scale=0.35,fliph=True) )
        self.hero.addpart( 'hurttext', draw.obj_textbox('ouch!',(340,self.yground-120),scale=1) )
        self.hero.dict['stand_right'].show=True
        self.hero.dict['stand_left'].show=False
        self.hero.dict['kick_right'].show=False
        self.hero.dict['kick_left'].show=False
        self.hero.dict['hurt'].show=False
        self.hero.dict['hurttext'].show=False
        self.herofaceright=True# hero is facing the right
        self.herojumping=False# hero is jumping or not
        self.heromayjump=True# hero can jump (not if in the air)
        self.heromayholdjump=False# hero can hold to jump higher
        self.herokicking=False# hero is kicking or not
        self.herohurt=False# hurting state or not
        self.herodown=False# hero is down

        # self.heroinvultimer=tool.obj_timer(40)# how long
        self.herov=0#total velocity
        self.herovj=0# added velocity from jump (changes during jump)
        self.heroivj=4# initial velocity from jump (when starting jump)
        self.herodvj=0.9# velocity factor loss (when holding jump)
        self.herovg=1#1 velocity from gravity
        self.heromx=12# move rate horizontally
        self.heromxkick=5#15# move rate horizontally when kicking
        self.heroholdjumptimer=tool.obj_timer(100)# how long can hold jump button
        self.herokicktimer=tool.obj_timer(10)#10 how long hero kicks
        self.herodowntimer=tool.obj_timer(40)# how long hero is down
        self.herohurttimer=tool.obj_timer(150)# how long hero is hurting (make it longer then hero down)
        self.heroreloadtimer=tool.obj_timer(10)# reload time for hero kick (starts after kick finish)
        # hero hitboxes
        self.herohitbox1yoff=0
        self.herohitbox1=obj_grandactor(self,(340,self.yground+self.herohitbox1yoff))# for being hit (head)
        self.herohitbox1.rx=25#45
        self.herohitbox1.ry=60
        #
        self.herohitbox2xoff=30
        self.herohitbox2yoff=30
        self.herohitbox2=obj_grandactor(self,(340,self.yground+self.herohitbox2yoff))# for hitting (feets)
        self.herohitbox2.rx=70
        self.herohitbox2.ry=25

        # villain
        self.villain.addpart( 'stand_right', draw.obj_image('villainbase',(940,self.yground-12),scale=0.35) )
        self.villain.addpart( 'stand_left', draw.obj_image('villainbase',(940,self.yground-12),scale=0.35,fliph=True) )
        self.villain.addpart( 'kick_right', draw.obj_image('villainkick',(940,self.yground-12),scale=0.35) )
        self.villain.addpart( 'kick_left', draw.obj_image('villainkick',(940,self.yground-12),scale=0.35,fliph=True) )
        self.villain.addpart( 'rest_right', draw.obj_image('villainbaserest',(940,self.yground-12),scale=0.35) )
        self.villain.addpart( 'rest_left', draw.obj_image('villainbaserest',(940,self.yground-12),scale=0.35,fliph=True) )
        self.villain.addpart( 'hurt', draw.obj_image('villainbase',(940,self.yground-12+70),scale=0.35,rotate=90) )
        self.villain.addpart( 'hurttext', draw.obj_textbox('get that!',(940,self.yground-120),scale=1) )
        self.villainhurt=False# hurt or not
        self.villainstate='stand'# stand, kick, rest, jump (when no hurt)
        self.villaintimerstand=tool.obj_timer(5)#10 right before kicking or between jumps
        self.villaintimerkick=tool.obj_timer(20)#50 kick time
        self.villaintimerjump=tool.obj_timer(70)#70 jump time
        self.villaintimerfall=tool.obj_timer(50)#50 fall time (adjust with jump)
        self.villaintimerrest=tool.obj_timer(150)#50 rest time (when vulnerable)
        self.villaintimerhurt=tool.obj_timer(50)#50 down time (invulnerable)
        self.villainfaceright=False# villain faces right
        self.villainjumpright=True# villain jumps to right (can be different from facing direction)
        self.villainmx=5#20# move rate horizontally
        self.villainxmin=150#200 area where will face to right
        self.villainxmax=1280-150# area where will face to left
        self.villainmxjump=12#15 move rate when jumping
        self.villain_vj0=-20# jump rate (initial)
        self.villain_dv=0.7# jump rate increment (should go from positive to negative)
        self.villain_vj=self.villain_vj0# villain velocity v(t+dt)= v(t) + dv, v(0)=v0
        self.villainstaminamax=5# how many kicks before needs to rest
        self.villainstamina=self.villainstaminamax# start with max stamina

        # Assign state stand
        self.villain_tostand()

        # villlain hitboxes
        self.villainhitbox1yoff=0
        self.villainhitbox1=obj_grandactor(self,(940,self.yground-12+self.villainhitbox1yoff))# for being hit (head)
        self.villainhitbox1.rx=45
        self.villainhitbox1.ry=50
        #
        self.villainhitbox2xoff=30
        self.villainhitbox2yoff=40
        self.villainhitbox2=obj_grandactor(self,(940+50,self.yground-12+self.villainhitbox2yoff))# for hitting (villain kick)
        self.villainhitbox2.rx=30
        self.villainhitbox2.ry=50
        # health bar hero
        if self.dotutorial:
            self.ybar=150# for health bars and text
        else:
            self.ybar=50
        self.maxherohealth=5# starting hero health (reference=always 3)
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(640,360))
        self.healthbar.addpart('face', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.maxherohealth):
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )
        # health bar villain
        self.maxvillainhealth=9# starting villain health
        self.villainhealth=self.maxvillainhealth# updated one
        self.vealthbar=obj_grandactor(self,(640,360))
        self.vealthbar.addpart('face', draw.obj_image('villainhead',(1280-50,self.ybar),scale=0.2,fliph=True) )
        for i in range(self.maxvillainhealth):
            self.vealthbar.addpart('heart_'+str(i), draw.obj_image('lightningbolt',(1280-130-i*70,self.ybar),scale=0.2) )
        # text
        # tempo='['+share.datamanager.controlname('arrows')+': move/jump/kick]'
        tempo='['+share.datamanager.controlname('left')
        tempo +='/'+share.datamanager.controlname('right')+': move] '
        tempo +='['+share.datamanager.controlname('up')+': jump] '
        tempo +='['+share.datamanager.controlname('action')+': kick] '

        # self.text_undone.addpart( 'text1',draw.obj_textbox(tempo,(25,self.ybar+75),xleft=True,color=share.colors.instructions) )
        self.text_undone.addpart( 'text1',draw.obj_textbox(tempo,(640,self.ybar+75),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('fatality!',(640,360),fontsize='huge') )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('you are dead',(640,360),fontsize='huge') )
        # fight message at beginning
        self.timerfightmessage=tool.obj_timer(80)
        if not self.dotutorial:
            self.text_start.addpart( 'fightmessage', draw.obj_animation('dodgebullets_fightmessage','messagefight',(640,360), path='data/premade') )
            self.timerfightmessage.start()
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(120)# goal to done
        # audio
        self.soundjump=draw.obj_sound('stomp_jump')
        self.creator.addpart(self.soundjump)
        self.soundhit=draw.obj_sound('stomp_hit')
        self.creator.addpart(self.soundhit)
        self.soundkick=draw.obj_sound('stomp_kick')
        self.creator.addpart(self.soundkick)
        self.soundcontact=draw.obj_sound('stomp_contact')
        self.creator.addpart(self.soundcontact)
        self.soundstrike=draw.obj_sound('stomp_strike')
        self.creator.addpart(self.soundstrike)
        self.soundwin=draw.obj_sound('stomp_win')
        self.creator.addpart(self.soundwin)
        self.sounddie=draw.obj_sound('stomp_die')
        self.creator.addpart(self.sounddie)
        #
        if not self.dotutorial:
            self.soundstart=draw.obj_sound('stomp_start')
            self.soundstart.play()# at start

    #
    def villain_tostand(self):
        self.villainstate='stand'
        self.villaintimerstand.start()
        self.villain.movetoy(self.yground-12)# move to ground
        # choose next kick direction
        # self.villainfaceright = self.villain.x<self.hero.x# face the hero
        self.villain.dict['stand_right'].show=self.villainfaceright
        self.villain.dict['stand_left'].show=not self.villainfaceright
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['rest_right'].show=False
        self.villain.dict['rest_left'].show=False
        self.villain.dict['hurt'].show=False
        self.villain.dict['hurttext'].show=False
    def villain_tokick(self):
        self.villainstamina -= 1# loose stamina
        self.villainstate='kick'
        self.villaintimerkick.start()
        self.soundkick.play()
        self.villain.movetoy(self.yground-12)
        self.villain.dict['stand_right'].show=False
        self.villain.dict['stand_left'].show=False
        self.villain.dict['kick_right'].show=self.villainfaceright
        self.villain.dict['kick_left'].show=not self.villainfaceright
        self.villain.dict['rest_right'].show=False
        self.villain.dict['rest_left'].show=False
        self.villain.dict['hurt'].show=False
        self.villain.dict['hurttext'].show=False
    def villain_torest(self):
        self.villainstamina=self.villainstaminamax# regenerate stamina
        self.villainstate='rest'
        self.villaintimerrest.start()
        self.villain.movetoy(self.yground-12)
        self.villain.dict['stand_right'].show=False
        self.villain.dict['stand_left'].show=False
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['rest_right'].show=self.villainfaceright
        self.villain.dict['rest_left'].show=not self.villainfaceright
        self.villain.dict['hurt'].show=False
        self.villain.dict['hurttext'].show=False
    def villain_tojump(self):
        self.villainstate='jump'
        self.villaintimerjump.start()
        self.soundjump.play()
        self.villain_vj=self.villain_vj0# jump speed (initial)
        # choose next jump direction
        if self.villain.x<self.villainxmin:# it too left jump right
            self.villainjumpright=True
        elif self.villain.x>self.villainxmax:# if too right jump left
            self.villainjumpright=False
        else:
            self.villainjumpright = tool.randbool()# random direction
        self.villainfaceright = self.villain.x<self.hero.x# face the hero
        self.villain.dict['stand_right'].show=self.villainfaceright
        self.villain.dict['stand_left'].show=not self.villainfaceright
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['rest_right'].show=False
        self.villain.dict['rest_left'].show=False
        self.villain.dict['hurt'].show=False
        self.villain.dict['hurttext'].show=False
    def villain_tohurt(self):
        self.villainhurt=True
        self.villainstate='stand'
        self.villaintimerhurt.start()
        self.villain.dict['stand_right'].show=False
        self.villain.dict['stand_left'].show=False
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['rest_right'].show=False
        self.villain.dict['rest_left'].show=False
        self.villain.dict['hurt'].show=True
        self.villain.dict['hurttext'].show=True
    def villain_todead(self):
        self.villain.dict['stand_right'].show=False
        self.villain.dict['stand_left'].show=False
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['rest_right'].show=False
        self.villain.dict['rest_left'].show=False
        self.villain.dict['hurt'].show=True
        self.villain.dict['hurttext'].show=False
        self.herojumping=False
    def villain_orient(self):
        if self.villainstate=='kick':
            self.villain.dict['kick_right'].show=self.villainfaceright
            self.villain.dict['kick_left'].show=not self.villainfaceright
        elif self.villainstate=='rest':
            self.villain.dict['rest_right'].show=self.villainfaceright
            self.villain.dict['rest_left'].show=not self.villainfaceright
        else:
            self.villain.dict['stand_right'].show=self.villainfaceright
            self.villain.dict['stand_left'].show=not self.villainfaceright

    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # fight message at beginning
            if self.timerfightmessage.on:
                self.timerfightmessage.update()
                if self.timerfightmessage.ring:
                    self.text_start.show=False
            if not self.herodown:
                # hero dynamics y
                if self.heromayjump and (controls.gu and controls.guc):# start jump (click button)
                    self.herojumping=True
                    self.soundjump.play()
                    self.herov=0# reset velocity
                    self.herovj=self.heroivj# reset jump velocity
                    self.heromayjump=False# cant jump again
                    self.heromayholdjump=True# can hold this jump
                    self.heroholdjumptimer.start()
                if self.heromayholdjump and controls.gu:# hold jump (hold button)
                    self.herovj *= self.herodvj# factor jump velocity
                    self.herov -= self.herovj
                    self.heroholdjumptimer.update()
                    if self.heroholdjumptimer.ring:
                        self.heromayholdjump=False


                # hero kicks
                if not self.herokicking:
                    self.heroreloadtimer.update()
                    #
                    # hero dynamics x (always true except if hurt)
                    if controls.gl:#
                        self.hero.movex(-self.heromx)
                        if controls.glc:# flip left
                            self.herofaceright=False
                            self.hero.dict['stand_right'].show=False
                            self.hero.dict['stand_left'].show=True
                            self.hero.dict['hurt'].show=False
                            self.hero.dict['hurttext'].show=False
                    if controls.gr:#
                        self.hero.movex(self.heromx)
                        if controls.grc:# flip right
                            self.herofaceright=True
                            self.hero.dict['stand_right'].show=True
                            self.hero.dict['stand_left'].show=False
                            self.hero.dict['hurt'].show=False
                            self.hero.dict['hurttext'].show=False
                    if self.heroreloadtimer.off and controls.ga and controls.gac:
                        self.soundkick.play()
                        self.herokicking=True
                        self.hero.dict['kick_right'].show=self.herofaceright
                        self.hero.dict['kick_left'].show=not self.herofaceright
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=False
                        self.herokicktimer.start()
                        self.heroreloadtimer.start()# start reload (but wont reload during kick)
                else:# kicking
                    self.herokicktimer.update()
                    if self.herofaceright:
                        self.hero.movex(self.heromxkick)
                    else:
                        self.hero.movex(-self.heromxkick)
                    if self.herokicktimer.ring:
                        self.herokicking=False
                        self.hero.dict['kick_right'].show=False
                        self.hero.dict['kick_left'].show=False
                        self.hero.dict['stand_right'].show=self.herofaceright
                        self.hero.dict['stand_left'].show=not self.herofaceright
            else:
                # hero is down
                self.herodowntimer.update()
                if self.herodowntimer.ring:
                    self.herodown=False
                    self.hero.dict['stand_right'].show=True
                    self.hero.dict['stand_left'].show=False
                    self.hero.dict['hurt'].show=False
                    self.hero.dict['hurttext'].show=False
            if self.herohurt:# hero is hurt (and invincible temporarily)
                self.herohurttimer.update()
                if self.herohurttimer.ring:
                    self.herohurt=False

            # fall (even if hurt)
            self.herov += self.herovg# gravity
            self.hero.movey(self.herov)# dty=v (dt=1)
            if self.hero.y>self.yground:# hero is on ground
                self.herojumping=False
                self.hero.movetoy(self.yground)
                self.herov = 0# just stall
                self.heromayjump=True# may jump from ground again
            # boundaries
            if self.hero.x<self.xmin:# boundaries
                self.hero.movetox(self.xmin)
            elif self.hero.x>self.xmax:
                self.hero.movetox(self.xmax)
            # hero hitboxes move
            self.herohitbox1.movetoxy( (self.hero.x,self.hero.y+self.herohitbox1yoff) )
            self.herohitbox2.movetoxy( (self.hero.x+(2*self.herofaceright-1)*self.herohitbox2xoff,self.hero.y+self.herohitbox2yoff) )
            #
            # villain
            if not self.villainhurt:
                #
                if self.villainstate=='stand':# stand (very fast), to kick or jump
                    self.villaintimerstand.update()
                    if self.villaintimerstand.ring:# kick if close to player, else jump
                        dice=tool.randchoice(['kick','jump'],probas=[82,18])
                        if dice=='kick':
                            self.villain_tokick()
                        elif dice=='jump':
                            self.villain_tojump()
                #
                elif self.villainstate=='kick':
                    # kick one direction
                    if self.villainfaceright:
                        self.villain.movex(self.villainmx)
                    else:
                        self.villain.movex(-self.villainmx)
                    self.villaintimerkick.update()
                    if self.villaintimerkick.ring:# kick, to stand or rest
                        if self.villainstamina<0:# if out of stamina
                            dice=tool.randchoice(['stand','rest'],probas=[50,50])
                            if dice=='stand':
                                self.villain_tostand()
                            elif dice=='rest':
                                self.villain_torest()
                        else:
                            self.villain_tostand()
                #
                elif self.villainstate=='rest':
                    self.villaintimerrest.update()
                    if self.villaintimerrest.ring:# rest, to jump always
                        self.villain_tojump()
                #
                elif self.villainstate=='jump':
                    # jump one direction
                    if self.villainjumpright:
                        self.villain.movex(self.villainmxjump)
                    else:
                        self.villain.movex(-self.villainmxjump)
                    self.villain.movey(self.villain_vj)
                    self.villain_vj += self.villain_dv
                    if self.villain.y>self.yground-12:
                        self.villain.movetoy(self.yground-12)
                    self.villaintimerjump.update()
                    if self.villaintimerjump.ring:# jump, to stand always
                        self.villainfaceright = self.villain.x<self.hero.x# reface the hero
                        self.villain_tostand()
            else:# villain hurt
                    self.villaintimerhurt.update()
                    if self.villaintimerhurt.ring:
                        self.villainhurt=False
                        self.villain.dict['hurt'].show=False
                        self.villain.dict['hurttext'].show=False
                        self.villain_tokick()# hurt to kick always
            # villain boundaries
            if self.villain.x<self.xmin:# boundaries
                self.villain.movetox(self.xmin)
                self.villainfaceright=True# reverse direction
                self.villain_orient()
            elif self.villain.x>self.xmax:
                self.villain.movetox(self.xmax)
                self.villainfaceright=False# reverse direction
                self.villain_orient()
            # villain hitboxes move
            self.villainhitbox1.movetoxy( (self.villain.x,self.villain.y-12+self.villainhitbox1yoff) )
            self.villainhitbox2.movetoxy( (self.villain.x+(2*self.villainfaceright-1)*self.villainhitbox2xoff,self.villain.y-12+self.villainhitbox2yoff) )
            #
            #
            # Hero and Villain hit each other
            # villain hits hero (state kick and stand)
            if self.villainstate=='kick' and not self.herohurt:
            #
                if tool.checkrectcollide(self.villainhitbox2,self.herohitbox1):# villain hits hero
                    self.soundcontact.play()
                    if not self.dotutorial:# cant loose health on tutorial
                        self.herohealth -= 1
                    if self.herohealth>0:
                        self.soundhit.play()
                        if self.herohealth<self.maxherohealth:
                            self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        self.herohurt=True
                        self.herodown=True
                        self.hero.movetoy(self.yground)# put hero to ground
                        self.herov = 0# just stall
                        self.heromayjump=True# may jump from ground again
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=False
                        self.hero.dict['kick_right'].show=False
                        self.hero.dict['kick_left'].show=False
                        self.hero.dict['hurt'].show=True
                        self.hero.dict['hurttext'].show=True
                        self.herohurttimer.start()
                        self.herodowntimer.start()
                        self.herojumping=False
                    else:# dead hero
                        self.sounddie.play()
                        self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        self.goal=True
                        self.win=False
                        self.timerendloose.start()
                        self.text_undone.show=False
                        self.text_donelost.show=True
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=False
                        self.hero.dict['kick_right'].show=False
                        self.hero.dict['kick_left'].show=False
                        self.hero.dict['hurt'].show=True
                        self.hero.dict['hurttext'].show=False
                        self.herojumping=False
            #
            # hero hits the villain (only state rest)
            if not self.villainstate=='kick' and not self.villainhurt:
                if self.herokicking and tool.checkrectcollide(self.villainhitbox1,self.herohitbox2):# hero hits villain
                    self.soundcontact.play()
                    self.soundstrike.play()
                    self.villain.movetoy(self.yground-12)# move villain to ground (for safety)
                    if not self.dotutorial:# cant loose health on tutorial
                        self.villainhealth -= 1
                    if self.villainhealth>0:
                        if self.villainhealth<self.maxvillainhealth:
                            self.vealthbar.dict['heart_'+str(self.villainhealth)].show=False
                        self.villain_tohurt()

                    else:# dead villain (win)
                        self.vealthbar.dict['heart_'+str(self.villainhealth)].show=False
                        self.goal=True
                        self.win=True
                        self.timerendwin.start()
                        self.soundwin.play()
                        self.text_undone.show=False
                        self.text_donewin.show=True
                        self.villain_todead()

        #
        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                if self.timerendwin.ring:
                    self.done=True# end of minigame

                #
                # finish hero kick (only if winning)
                if self.herokicking:
                    self.herokicktimer.update()
                    if self.herofaceright:
                        self.hero.movex(self.heromxkick)
                    else:
                        self.hero.movex(-self.heromxkick)
                    if self.herokicktimer.ring:
                        self.herokicking=False
                        self.herofaceright = self.hero.x<self.villain.x# face the villain
                        self.hero.dict['kick_right'].show=False
                        self.hero.dict['kick_left'].show=False
                        self.hero.dict['stand_right'].show=self.herofaceright
                        self.hero.dict['stand_left'].show=not self.herofaceright

            else:# lost minigame
                self.timerendloose.update()
                if self.timerendloose.ring:
                    self.done=True# end of minigame


            # hero fall (even if already dead/won)
            self.herov += self.herovg# gravity
            self.hero.movey(self.herov)# dty=v (dt=1)
            if self.hero.y>self.yground:# hero is on ground
                self.hero.movetoy(self.yground)
                self.herov = 0# just stall

####################################################################################################################

# Mini Game: lying with bunny
# This is not a world per say but a holder for game data
#*LYING *BUNNY
class obj_world_lying(obj_world):
    def setup(self,**kwargs):
        #
        # parameters
        self.statements={}# full list of statements
        self.statdict={}# dictionary of 3 statements among full list
        self.statkeys=[]# the statement type(key) for the 3 statements
        self.stat01=[]# the statement boolean (True or False version) for the 3 statements
        self.fqstatdict={}# former question

        #
        # Statements Database
        self.statements={}# marked with key, statement negative (0), statement positive (1)
        self.statements['apple']=['I hate apples','I love apples']
        self.statements['banana']=['I hate bananas','I love bananas']
        self.statements['shower']=['I never shower','I always shower']
        self.statements['teeth']=['I never brush my teeth','I always brush my teeth']
        self.statements['spider']=['I am not scared of spiders','I am scared of spiders']
        self.statements['booger']=['I dont eat my boogers','I eat my boogers']
        self.statements['underwear']=['I never wear dirty underwears','I always wear dirty underwears']
        # Make 3 random statements upon creation
        self.makestatements()
        # Determine order in which statements will be used to make questions
        self.qcycle=tool.randsample([0,1,2],3)# cycle for asking questions
        self.iquestion=0# current index for question
        #
    def makestatements(self):
        # Pick up 3 statements from large database
        self.statkeys=[]# choose statements type (must be unique)
        self.statkeys=tool.randsample( list(self.statements)  , 3)
        self.stat01=[]# for each statement, select the True or False version (0,1)
        for i in range(3):
            self.stat01.append(tool.randchoice([0,1]))
        self.statdict={}
        for i in range(3):
            self.statdict[self.statkeys[i]]=self.stat01[i]
    def getstatement(self,index,lying=False):# index is 0,1,2, tells truth by default
        if index in [0,1,2]:
            if not lying:
                return self.statements[self.statkeys[index]][self.stat01[index]]
            else:
                return self.statements[self.statkeys[index]][1-self.stat01[index]]
        else:
            return 'wrong index'
        #
    def makequestion(self):
        # Get one of the 3 statements (following a cyclic order)
        # self.qstatkeys=tool.randsample( list(self.statkeys)  , 1)# old way, choose randomly
        # new way, cyclically use the questions
        self.qstatkeys=[]
        self.qstatkeys.append(self.statkeys[ self.qcycle[self.iquestion] ])
        self.iquestion +=1
        if self.iquestion>2:
            self.iquestion=0
        #
        self.qstat01=[]
        self.qstat01.append(tool.randchoice([0,1]))
        self.qstatdict={}
        self.qstatdict[self.qstatkeys[0]]=self.qstat01[0]
        # If question same as last one, change it slightly
        if  self.qstatdict.items() == self.fqstatdict.items():
            self.qstat01[0]=1-self.qstat01[0]# swap 0 1
            self.qstatdict[self.qstatkeys[0]]=self.qstat01[0]
        # Determine correct answer to question in advance
        if self.qstatdict.items() <= self.statdict.items():# dictionary is subset of larger one
            share.datamanager.setword('truth_yesno','yes')
        else:
            share.datamanager.setword('truth_yesno','no')
        # save current question for later
        self.fqstatdict=self.qstatdict
    def getquestion(self):
        return self.statements[self.qstatkeys[0]][self.qstat01[0]]

        if False:
            print('###')
            print('truth='+ str(self.statdict))
            print('statment='+ str(qstatdict))
            print('answer='+ str(self.nextpage_correctanswer()))
    def isanswercorrect(self,lying=False):
        if share.devmode:
            return True
        else:
            if not lying:
                return share.datamanager.getword('choice_yesno') == share.datamanager.getword('truth_yesno')
            else:
                return share.datamanager.getword('choice_yesno') != share.datamanager.getword('truth_yesno')

####################################################################################################################


# Mini Game: Climb Highest Peak
#*CLIMB *CLIMBING *PEAK
class obj_world_climbpeak(obj_world):
    def setup(self):
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached (doesnt necessarily mean game is won)
        self.xmin=50
        self.xmax=1280-50
        self.yground=720-120# ground
        self.heroxystart=(140,self.yground)# where hero starts
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.hero=obj_grandactor(self,self.heroxystart)
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_done.show=False
        # static
        self.staticactor.addpart( 'img1', draw.obj_image('sun',(218,233),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img4', draw.obj_image('floor1',(640,720-100),path='data/premade') )
        self.staticactor.addpart( 'img1a', draw.obj_image('arrowup',(1110,100),path='data/premade') )
        self.staticactor.addpart( 'img5',draw.obj_image('mountain',(779,624),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img6',draw.obj_image('mountain',(1070,605),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img7',draw.obj_image('mountain',(1203,585),scale=0.38,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'text1', draw.obj_textbox('Climb the Peak',(585,212)) )
        # platforms
        self.platforms=[]
        self.platformsxy=[(1110,195),(813,385),(457,575)]
        for c,xy in enumerate(self.platformsxy):
            platformi=obj_grandactor(self,xy)
            platformi.addpart( 'img', draw.obj_image('platform1',xy,path='data/premade') )
            platformi.rx=150
            platformi.ry=5
            self.platforms.append(platformi)
        # hero
        self.hero.addpart( 'stand_right', draw.obj_image('herobase',self.heroxystart,scale=0.35) )
        self.hero.addpart( 'stand_left', draw.obj_image('herobase',self.heroxystart,scale=0.35,fliph=True) )
        self.hero.dict['stand_right'].show=True
        self.hero.dict['stand_left'].show=False
        self.heromayjump=True# hero can jump (not if in the air)
        self.heromayholdjump=False# hero can hold to jump higher
        self.herov=0#total velocity
        self.herovj=0# added velocity from jump (changes during jump)
        self.heroivj=4# initial velocity from jump (when starting jump)
        self.herodvj=0.9# velocity factor loss (when holding jump)
        self.herovg=1.2#1 velocity from gravity
        self.heroholdjumptimer=tool.obj_timer(100)# how long can hold jump button
        self.heromx=12# move rate horizontally
        # hero hitboxes
        self.herohitbox1=obj_grandactor(self,(self.heroxystart[0],self.heroxystart[1]))# for being hit
        self.herohitbox1.rx=50
        self.herohitbox1.ry=100
        self.herohitbox2=obj_grandactor(self,(self.heroxystart[0],self.heroxystart[1]+75))# for hitting (is hero feets)
        self.herohitbox2.rx=50
        self.herohitbox2.ry=25
        # goal hitbox
        self.goalhitbox=obj_grandactor(self,(1110,100))
        # text
        self.text_undone.addpart( 'text1', \
        draw.obj_textbox('['+share.datamanager.controlname('arrows')+': move and jump]',(980,510),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox(' ',(980,510)) )
        # levels
        self.startlevel=False# start playing new level
        self.level=1# current level
        # timer for done part
        self.timerend=tool.obj_timer(0)# goal to done
        # self.setlevel2()# Test
        # self.setlevel3()# Test
        #
        self.soundjump=draw.obj_sound('climb_jump')
        self.creator.addpart(self.soundjump)
        self.soundfall=draw.obj_sound('climb_fall')
        self.creator.addpart(self.soundfall)

    def setlevel2(self):
        # clear stuff
        self.staticactor.clearparts()
        for i in self.platforms:
            i.clearparts()
            i.kill()
        # static
        self.staticactor.addpart( 'img1a', draw.obj_image('arrowup',(250,200),path='data/premade') )
        self.staticactor.addpart( 'img2',draw.obj_image('cloud',(1060,167),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img3',draw.obj_image('cloud',(533,329),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img4',draw.obj_image('cloud',(335,620),scale=0.41,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'img5',draw.obj_image('mountain',(111,676),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img6',draw.obj_image('mountain',(715,692),scale=0.26,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'img7',draw.obj_image('mountain',(862,671),scale=0.26,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'text1', draw.obj_textbox('Keep it up!',(850,347)) )
        # platforms
        self.platforms=[]
        # self.platformsxy=[(457,193),(813,385),(1110,575)]
        self.platformsxy=[(1110,675),(1111,485),(250,485),(250,295)]
        # ground (becomes a fall)
        self.yground=720+200
        # level
        self.startlevel=False
        self.level=2
        # platformes
        for c,xy in enumerate(self.platformsxy):
            platformi=obj_grandactor(self,xy)
            platformi.addpart( 'img', draw.obj_image('platform1',xy,path='data/premade') )
            platformi.rx=150
            platformi.ry=5
            self.platforms.append(platformi)
        # hero
        self.heroxystart=(1110+50,560)
        self.hero.movetoxy(self.heroxystart)
        self.heromayjump=True# hero can jump (not if in the air)
        self.heromayholdjump=False# hero can hold to jump higher
        # goal
        self.goalhitbox.movetoxy((250,200-100))
        # text
        self.text_undone.dict['text1'].movetoxy(640,580)

    def setlevel3(self):
        # clear stuff
        self.staticactor.clearparts()
        for i in self.platforms:
            i.clearparts()
            i.kill()
        # static
        self.staticactor.addpart( 'img0a', draw.obj_image('arrowup',(1110,50),path='data/premade') )
        self.staticactor.addpart( 'text1', draw.obj_textbox('Almost there!',(827,398)) )
        self.staticactor.addpart( 'img1b', draw.obj_image('cloud',(478,227),scale=0.66,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img2b', draw.obj_image('cloud',(1146,626),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img3b', draw.obj_image('cloud',(816,535),scale=0.43,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'img4b', draw.obj_image('lightningbolt',(496,385),scale=0.43,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'img5b', draw.obj_image('lightningbolt',(810,218),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img6b', draw.obj_image('cloud',(832,102),scale=0.46,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img7b', draw.obj_image('cloud',(117,262),scale=0.43,rotate=0,fliph=False,flipv=False) )
        # platforms
        self.platforms=[]
        # self.platformsxy=[(457,193),(813,385),(1110,575)]
        self.platformsxy=[(140,675),(680,675),(1110,490),(1110,320),(1110,160)]
        # ground (becomes a fall)
        self.yground=720+200
        # level
        self.startlevel=False
        self.level=3
        # platformes
        for c,xy in enumerate(self.platformsxy):
            platformi=obj_grandactor(self,xy)
            platformi.addpart( 'img', draw.obj_image('platform1',xy,path='data/premade') )
            platformi.rx=150
            platformi.ry=5
            self.platforms.append(platformi)
        # hero
        self.heroxystart=(140+50,560)
        self.hero.movetoxy(self.heroxystart)
        self.heromayjump=True# hero can jump (not if in the air)
        self.heromayholdjump=False# hero can hold to jump higher
        # goal
        self.goalhitbox.movetoxy((1110,-30))
        # text
        self.text_undone.dict['text1'].movetoxy(204,409)
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            #
            # hero
            # initial move (press one button to initiate movement in each level)
            if not self.startlevel:
                if controls.glc or controls.grc or controls.gdc or controls.guc:
                    self.startlevel=True
            if self.startlevel:
                # hero dynamics y
                if self.heromayjump and (controls.gu and controls.guc):# jump (click button)
                    self.herov=0# reset velocity
                    self.herovj=self.heroivj# reset jump velocity
                    self.heromayjump=False# cant jump again
                    self.heromayholdjump=True# can hold this jump
                    self.heroholdjumptimer.start()
                    self.soundjump.play()
                if self.heromayholdjump and controls.gu:# jump (hold button)
                    self.herovj *= self.herodvj# factor jump velocity
                    self.herov -= self.herovj
                    self.heroholdjumptimer.update()
                    if self.heroholdjumptimer.ring:
                        self.heromayholdjump=False
                self.herov += self.herovg# gravity
                # ground
                if self.hero.y+self.herov>self.yground:# hero is on ground
                    if self.level<2:# first level, ground is hard
                        self.hero.movetoy(self.yground)
                        self.herov = 0# just stall
                        self.heromayjump=True# may jump from ground again
                    else:# next levels, ground is a fall (restart level)
                        self.hero.movetoxy(self.heroxystart)
                        self.heromayjump=True# hero can jump (not if in the air)
                        self.startlevel=False
                        self.soundfall.play()
                # platforms
                for i in self.platforms:
                    if tool.checkrectcollide(self.herohitbox2,i):
                        self.herov=min(0,self.herov)# positive
                        self.heromayjump=True# may jump from ground again
                # apply movement
                self.hero.movey(self.herov)# dty=v
                # hero dynamics x
                if controls.gl:#
                    self.hero.movex(-self.heromx)
                    if controls.glc:# flip left
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=True
                if controls.gr:
                    self.hero.movex(self.heromx)
                    if controls.grc:# flip right
                        self.hero.dict['stand_right'].show=True
                        self.hero.dict['stand_left'].show=False
                if self.hero.x<self.xmin:# boundaries
                    self.hero.movetox(self.xmin)
                elif self.hero.x>self.xmax:
                    self.hero.movetox(self.xmax)
                # hero hitboxes move
                self.herohitbox1.movetoxy( (self.hero.x,self.hero.y) )
                self.herohitbox2.movetoxy( (self.hero.x,self.hero.y+75) )
                # hero reaches goal
                if tool.checkrectcollide(self.herohitbox1,self.goalhitbox):
                    if self.level==1:
                        self.setlevel2()
                    elif self.level==2:
                        self.setlevel3()
                    else:# end of all levels
                        self.goal=True
                        self.text_undone.show=False
                        self.text_done.show=True
                        self.timerend.start()
        else:
            # goal reached states
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame



####################################################################################################################


# Mini Game: Play Rock Paper Scissors
# *ROCK *PAPER *SCISSORS
class obj_world_rockpaperscissors(obj_world):
    def setup(self,**kwargs):
        ##########################3
        # Premake necessary images
        # combine herohead+stickwalk = herowalk
        image1=draw.obj_image('stickwalk',(640,460),path='data/premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herowalk')
        # combine elderhead+stickwalk=elderwalk
        image1=draw.obj_image('stickwalk',(640,460),path='data/premade')# snapshot
        image2=draw.obj_image('elderhead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'elderwalk')

        # default parameters
        self.elderalwayswin=False# elder always wins (chooses counter at last moment)
        self.elderalwaysloose=False# elder always looses (chooses bad counter at last moment)
        self.elderthinks=True# can see what the elder is thinking
        self.elderpeaks=False# elder peaks on last countdown to counter
        self.herohealthmax=5# health bar
        self.elderhealthmax=7#3#
        self.dotutorial=False# do tutorial
        self.dotutorialnothinks=False# remove what hero/elder is thinking (for extended tutorial)
        # scene tuning
        if kwargs is not None:
            if 'elderwins' in kwargs: self.elderalwayswin=kwargs["elderwins"]
            if 'elderlooses' in kwargs: self.elderalwaysloose=kwargs["elderlooses"]
            if 'elderthinks' in kwargs: self.elderthinks=kwargs["elderthinks"]
            if 'elderpeaks' in kwargs: self.elderpeaks=kwargs["elderpeaks"]
            if 'herohealth' in kwargs: self.herohealthmax=kwargs["herohealth"]
            if 'elderhealth' in kwargs: self.elderhealthmax=kwargs["elderhealth"]
            if 'tutorial' in kwargs: self.dotutorial=kwargs["tutorial"]
            if 'nothinks' in kwargs: self.dotutorialnothinks=kwargs["nothinks"]
        self.herohealth=self.herohealthmax
        self.elderhealth=self.elderhealthmax
        self.done=False# end of minigame
        self.goal=False# minigame goal reached (doesnt necessarily mean game is won)
        self.win=True# game is won
        # layering
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.hero=obj_grandactor(self,(640,360))
        self.elder=obj_grandactor(self,(640,360))
        self.countdown=obj_grandactor(self,(640,360))
        self.result=obj_grandactor(self,(640,360))
        self.healthbar=obj_grandactor(self,(640,360))
        self.instructions=obj_grandactor(self,(640,360))# text always in front
        self.endgame=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_donewin.show=False
        self.text_donelost.show=False
        self.text_start=obj_grandactor(self,(640,360))# text message at start
        self.text_start.show=True
        #
        # static
        self.staticactor.addpart( 'floor', draw.obj_image('floor5',(640,720-100),path='data/premade') )
        self.staticactor.addpart( 'hero', draw.obj_image('herobase',(640-240,530),scale=0.5) )
        self.staticactor.addpart( 'elder', draw.obj_image('elderbase2',(640+240,530),scale=0.5,fliph=True) )
        animation1=draw.obj_animation('rps_herowalk','herobase',(640-240,360))
        animation1.addimage('herowalk')
        self.staticactor.addpart( 'herowalk', animation1 )
        animation1=draw.obj_animation('rps_herowalk','elderbase2',(640+240,360),imgfliph=True)
        animation1.addimage('elderwalk',fliph=True)
        self.staticactor.addpart( 'elderwalk', animation1 )
        self.staticactor.dict['hero'].show=True
        self.staticactor.dict['elder'].show=True
        self.staticactor.dict['herowalk'].show=False
        self.staticactor.dict['elderwalk'].show=False
        # self.staticactor.addpart( 'img1a', draw.obj_image('mountain',(1212,666),scale=0.3,rotate=0,fliph=False,flipv=False) )
        # self.staticactor.addpart( 'img2a', draw.obj_image('mountain',(1096,627),scale=0.24,rotate=0,fliph=False,flipv=False) )
        # self.staticactor.addpart( 'img3a', draw.obj_image('cloud',(1207,536),scale=0.29,rotate=0,fliph=True,flipv=False) )
        # self.staticactor.addpart( 'img4a', draw.obj_image('mountain',(80,651),scale=0.34,rotate=0,fliph=True,flipv=False) )
        # self.staticactor.addpart( 'img5a', draw.obj_image('mountain',(198,621),scale=0.22,rotate=0,fliph=False,flipv=False) )
        # self.staticactor.addpart( 'img6a', draw.obj_image('cloud',(118,564),scale=0.2,rotate=0,fliph=True,flipv=False) )
        # instructions
        yrpsinfo=300
        # self.instructions.addpart( 'texta', draw.obj_textbox('['+share.datamanager.controlname('left')+']: rock',(640-80,yrpsinfo+50),fontsize='small',color=share.colors.instructions) )
        # self.instructions.addpart( 'textw', draw.obj_textbox('['+share.datamanager.controlname('up')+']: paper',(640,yrpsinfo),fontsize='small',color=share.colors.instructions) )
        # self.instructions.addpart( 'textd', draw.obj_textbox('['+share.datamanager.controlname('right')+']: scissors',(640+90,yrpsinfo+50),fontsize='small',color=share.colors.instructions) )
        self.instructions.addpart( 'texta', draw.obj_textbox('['+share.datamanager.controlname('left')+']: rock',(40,480),xleft=True,fontsize='small',color=share.colors.instructions) )
        self.instructions.addpart( 'textw', draw.obj_textbox('['+share.datamanager.controlname('up')+']: paper',(40,480+55),xleft=True,fontsize='small',color=share.colors.instructions) )
        self.instructions.addpart( 'textd', draw.obj_textbox('['+share.datamanager.controlname('right')+']: scissors',(40,480+55*2),xleft=True,fontsize='small',color=share.colors.instructions) )
        self.instructions.addpart( 'texts', draw.obj_textbox('['+share.datamanager.controlname('action')+']: start game',(640,yrpsinfo),color=share.colors.instructions) )
        self.instructions.addpart( 'textn', draw.obj_textbox('['+share.datamanager.controlname('action')+']: next round',(640,yrpsinfo),color=share.colors.instructions) )
        self.instructions.addpart( 'texte', draw.obj_textbox('['+share.datamanager.controlname('action')+']: end game',(640,yrpsinfo),color=share.colors.instructions) )
        self.instructions.dict['texta'].show=True
        self.instructions.dict['textw'].show=True
        self.instructions.dict['textd'].show=True
        self.instructions.dict['texts'].show=True
        self.instructions.dict['textn'].show=False
        self.instructions.dict['texte'].show=False
        if self.dotutorial:
            self.instructions.dict['texts'].show=False
        # hero
        # self.hero.addpart( 'thinkcloud', draw.obj_image('thinkcloud',(200,320),path='data/premade') )
        # self.hero.addpart( 'talkcloud', draw.obj_image('talkcloud',(200,320),path='data/premade') )
        self.hero.addpart( 'thinkcloud', draw.obj_rectangle((100+50,320),120,120,color=share.colors.drawing) )
        if self.dotutorial:
            self.hero.addpart( 'talkcloud', draw.obj_rectangle((100+50,320),120,120,color=share.colors.drawing) )
        else:
            self.hero.addpart( 'talkcloud', draw.obj_rectangle((100+50,320),120,120,color=(0,0,0)) )
        self.hero.addpart( 'rock', draw.obj_image('rock',(100+50,320),scale=0.5) )
        self.hero.addpart( 'paper', draw.obj_image('paper',(100+50,320),scale=0.5) )
        self.hero.addpart( 'scissors', draw.obj_image('scissors',(100+50,320),scale=0.5) )
        self.hero.show=True# show what the hero is thinking or not
        self.herochoice=0# 0,1,2 for rock, paper scissors
        self.hero.dict['rock'].show=self.herochoice==0
        self.hero.dict['paper'].show=self.herochoice==1
        self.hero.dict['scissors'].show=self.herochoice==2
        self.hero.dict['thinkcloud'].show=False
        self.hero.dict['talkcloud'].show=True
        # elder
        # self.elder.addpart( 'thinkcloud', draw.obj_image('thinkcloud',(1280-200,320),fliph=True,path='data/premade') )
        # self.elder.addpart( 'talkcloud', draw.obj_image('talkcloud',(1280-200,320),fliph=True,path='data/premade') )
        self.elder.addpart( 'thinkcloud', draw.obj_rectangle((1280-100-50,320),120,120,color=share.colors.drawing) )
        if self.dotutorial:
            self.elder.addpart( 'talkcloud', draw.obj_rectangle((1280-100-50,320),120,120,color=share.colors.drawing) )
        else:
            self.elder.addpart( 'talkcloud', draw.obj_rectangle((1280-100-50,320),120,120,color=(0,0,0)) )

        if self.elderthinks:# can see what elder is thinking
            self.elder.addpart( 'rock', draw.obj_image('rock',(1280-100-50,320),scale=0.5) )
            self.elder.addpart( 'paper', draw.obj_image('paper',(1280-100-50,320),scale=0.5) )
            self.elder.addpart( 'scissors', draw.obj_image('scissors',(1280-100-50,320),scale=0.5) )
        else:
            self.elder.addpart( 'rock', draw.obj_image('interrogationmark',(1280-100-50,320),scale=1,path='data/premade') )
            self.elder.addpart( 'paper', draw.obj_image('interrogationmark',(1280-100-50,320),scale=1,path='data/premade') )
            self.elder.addpart( 'scissors', draw.obj_image('interrogationmark',(1280-100-50,320),scale=1,path='data/premade') )
        self.elder.show=True# show what the elder is thinking or not
        self.elderchoice=tool.randchoice([0,1,2])# 0,1,2 for rock, paper scissors
        self.elder.dict['rock'].show=self.elderchoice==0
        self.elder.dict['paper'].show=self.elderchoice==1
        self.elder.dict['scissors'].show=self.elderchoice==2
        self.elder.dict['thinkcloud'].show=False
        self.elder.dict['talkcloud'].show=True
        if self.dotutorialnothinks:
            self.elder.dict['rock'].show=False
            self.elder.dict['paper'].show=False
            self.elder.dict['scissors'].show=False
        # show
        self.result.addpart( 'herorock', draw.obj_image('rock',(100+50,320),scale=0.5) )
        self.result.addpart( 'heropaper', draw.obj_image('paper',(100+50,320),scale=0.5) )
        self.result.addpart( 'heroscissors', draw.obj_image('scissors',(100+50,320),scale=0.5) )
        self.resulthero=0# 0,1,2 for rock, paper scissors
        self.result.dict['herorock'].show=False
        self.result.dict['heropaper'].show=False
        self.result.dict['heroscissors'].show=False
        self.result.addpart( 'elderrock', draw.obj_image('rock',(1280-100-50,320),scale=0.5) )
        self.result.addpart( 'elderpaper', draw.obj_image('paper',(1280-100-50,320),scale=0.5) )
        self.result.addpart( 'elderscissors', draw.obj_image('scissors',(1280-100-50,320),scale=0.5) )
        self.resultelder=0# 0,1,2 for rock, paper scissors
        self.result.dict['elderrock'].show=False
        self.result.dict['elderpaper'].show=False
        self.result.dict['elderscissors'].show=False
        self.computedresults=False# has computed results (one frame each round)
        self.result.addpart( 'win',  draw.obj_image('largecross',(1280-100-50,320),path='data/premade')  )
        self.result.addpart( 'loose', draw.obj_image('largecross',(100+50,320),path='data/premade')  )
        # self.result.addpart( 'paperrock', draw.obj_textbox('Paper Beats Rock',(640,350),fontsize='big',scale=0.9)  )
        # self.result.addpart( 'rockscissors', draw.obj_textbox('Rock Beats Scissors',(640,350),fontsize='big',scale=0.9)  )
        # self.result.addpart( 'scissorspaper', draw.obj_textbox('Scissors Beats Paper',(640,350),fontsize='big',scale=0.9)  )
        # self.result.addpart( 'tie', draw.obj_textbox('Its a tie',(640,350),fontsize='big')  )
        self.result.addpart( 'paperrock', draw.obj_textbox('Paper Beats Rock',(640,150),fontsize='huge',scale=0.9)  )
        self.result.addpart( 'rockscissors', draw.obj_textbox('Rock Beats Scissors',(640,150),fontsize='huge',scale=0.9)  )
        self.result.addpart( 'scissorspaper', draw.obj_textbox('Scissors Beats Paper',(640,150),fontsize='huge',scale=0.9)  )
        self.result.addpart( 'tie', draw.obj_textbox('Its a tie',(640,150),fontsize='huge')  )
        self.result.dict['win'].show=False
        self.result.dict['loose'].show=False
        self.result.dict['tie'].show=False
        self.result.dict['paperrock'].show=False
        self.result.dict['rockscissors'].show=False
        self.result.dict['scissorspaper'].show=False
        # countdown
        self.countdown.addpart( '3', draw.obj_textbox('3...',(640,150),fontsize='huge',color=share.colors.drawing)  )
        self.countdown.addpart( '2', draw.obj_textbox('2...',(640,150),fontsize='huge',color=share.colors.drawing)  )
        self.countdown.addpart( '1', draw.obj_textbox('1...',(640,150),fontsize='huge',color=share.colors.drawing)  )
        self.countdown.dict['3'].show=False
        self.countdown.dict['2'].show=False
        self.countdown.dict['1'].show=False
        self.checking=False# checking result or not
        self.countdowning=False# doing countdown or not #######!!!CHANGED
        self.icountdown=3
        self.countdowntime=80
        self.countdowntimelast=90# on last count, slightly more time to decide
        if self.elderalwayswin or self.elderalwaysloose:# if win/loose just hurry it
            self.countdowntimelast=self.countdowntime
        self.countdowntimer=tool.obj_timer(self.countdowntime)# timer
        # healthbars
        # health bar hero
        if self.dotutorial:
            self.ybar=150# for health bars and text
        else:
            self.ybar=50
        self.healthbar.addpart('face1', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.herohealthmax):
            self.healthbar.addpart('hero_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )
            self.healthbar.addpart('herocross_'+str(i), draw.obj_image('smallcrossred',(150+i*75,self.ybar),scale=0.5,path='data/premade') )
            self.healthbar.dict['herocross_'+str(i)].show=False
        self.healthbar.addpart('face2', draw.obj_image('elderhead',(1280-50,self.ybar),scale=0.2,fliph=True) )
        for i in range(self.elderhealthmax):
            self.healthbar.addpart('elder_'+str(i), draw.obj_image('lightningbolt',(1280-130-i*70,self.ybar),scale=0.2) )
            self.healthbar.addpart('eldercross_'+str(i), draw.obj_image('smallcrossred',(1280-130-i*70,self.ybar),scale=0.5,path='data/premade') )
            self.healthbar.dict['eldercross_'+str(i)].show=False
        # text
        self.text_donewin.addpart( 'text1', draw.obj_textbox('victory!',(640,150),fontsize='huge') )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('defeat!',(640,150),fontsize='huge') )
        # fight message at beginning
        self.timerfightmessage=tool.obj_timer(80)
        if not self.dotutorial:
            self.text_start.addpart( 'fightmessage', draw.obj_animation('dodgebullets_fightmessage','messagefight',(640,360), path='data/premade') )
            self.timerfightmessage.start()
        # endgame animations
        self.endgame.addpart( 'loose', draw.obj_animation('ch5_rpsloose','herobase',(640,360)) )
        self.endgame.addpart( 'win', draw.obj_animation('ch5_rpswin','elderbase',(640,360)) )
        self.endgame.dict['loose'].show=False
        self.endgame.dict['win'].show=False
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(120)# goal to done
        #
        # audio
        self.soundselect=draw.obj_sound('rps_select')
        self.creator.addpart(self.soundselect)
        self.soundstart=draw.obj_sound('rps_start')
        self.creator.addpart(self.soundstart)
        if not self.dotutorial:
            self.soundstart.play()# at start
        self.soundcount=draw.obj_sound('rps_count')
        self.creator.addpart(self.soundcount)
        if not self.dotutorial:
            self.soundcount.play()# at start
        self.soundhit=draw.obj_sound('rps_hit')
        self.creator.addpart(self.soundhit)
        self.soundstrike=draw.obj_sound('rps_strike')
        self.creator.addpart(self.soundstrike)
        self.soundtie=draw.obj_sound('rps_tie')
        self.creator.addpart(self.soundtie)
        self.sounddie=draw.obj_sound('rps_die')
        self.creator.addpart(self.sounddie)
        self.soundwin=draw.obj_sound('rps_win')
        self.creator.addpart(self.soundwin)

    def update(self,controls):
        super().update(controls)
        # goal unreached
        if not self.goal:
            # fight message at beginning
            if self.timerfightmessage.on:
                self.timerfightmessage.update()
                if self.timerfightmessage.ring:
                    self.text_start.show=False
            if not self.checking: # deciding state
                # print('VALUE='+str(self.icountdown)+'----:'+str(self.countdowntimer.t))
                if controls.gl and controls.glc:
                    if not self.herochoice==0: self.soundselect.play()
                    self.herochoice=0
                    self.hero.dict['rock'].show=self.herochoice==0
                    self.hero.dict['paper'].show=self.herochoice==1
                    self.hero.dict['scissors'].show=self.herochoice==2
                elif controls.gu and controls.guc:
                    if not self.herochoice==1: self.soundselect.play()
                    self.herochoice=1
                    self.hero.dict['rock'].show=self.herochoice==0
                    self.hero.dict['paper'].show=self.herochoice==1
                    self.hero.dict['scissors'].show=self.herochoice==2
                elif controls.gr and controls.grc:
                    if not self.herochoice==2: self.soundselect.play()
                    self.herochoice=2
                    self.hero.dict['rock'].show=self.herochoice==0
                    self.hero.dict['paper'].show=self.herochoice==1
                    self.hero.dict['scissors'].show=self.herochoice==2
                if not self.countdowning:# not countdown
                    if not self.dotutorial:
                        self.countdowning=True# flip to countdown
                        self.icountdown=3
                        self.countdowntimer.amount=self.countdowntime# default time
                        self.countdowntimer.start()
                        self.countdown.dict['3'].show=True
                        self.countdown.dict['2'].show=False
                        self.countdown.dict['1'].show=False
                        self.elderchoice=tool.randchoice([0,1,2])
                        self.elder.dict['rock'].show=self.elderchoice==0
                        self.elder.dict['paper'].show=self.elderchoice==1
                        self.elder.dict['scissors'].show=self.elderchoice==2
                        self.instructions.dict['texta'].show=True
                        self.instructions.dict['textw'].show=True
                        self.instructions.dict['textd'].show=True
                        self.instructions.dict['texts'].show=False
                        self.instructions.dict['textn'].show=False
                        self.instructions.dict['texte'].show=False
                        self.staticactor.dict['hero'].show=False
                        self.staticactor.dict['elder'].show=False
                        self.staticactor.dict['herowalk'].show=True
                        self.staticactor.dict['elderwalk'].show=True
                        self.hero.dict['thinkcloud'].show=True
                        self.hero.dict['talkcloud'].show=False
                        self.elder.dict['thinkcloud'].show=True
                        self.elder.dict['talkcloud'].show=False
                else:
                    self.countdowntimer.update()
                    if self.countdowntimer.ring:
                        if self.icountdown>1:# not the last round yet
                            self.soundcount.play()
                            self.icountdown -=1
                            if self.icountdown==1:# slightly more time to decide on last count
                                self.countdowntimer.amount=self.countdowntimelast
                            else:
                                self.countdowntimer.amount=self.countdowntime
                            self.countdowntimer.start()# reset timer
                            if self.elderpeaks and self.icountdown==1:# elder peaks on 1...
                                if self.herochoice==0:
                                    self.elderchoice=1
                                elif self.herochoice==1:
                                    self.elderchoice=2#
                                else:
                                    self.elderchoice=0
                            else:# random choice (but change)
                                if self.elderchoice==0:
                                    self.elderchoice=tool.randchoice([1,2])
                                elif self.elderchoice==1:
                                    self.elderchoice=tool.randchoice([0,2])
                                else:
                                    self.elderchoice=tool.randchoice([0,1])
                            self.elder.dict['rock'].show=self.elderchoice==0
                            self.elder.dict['paper'].show=self.elderchoice==1
                            self.elder.dict['scissors'].show=self.elderchoice==2
                            if self.icountdown==2:
                                self.countdown.dict['3'].show=False
                                self.countdown.dict['2'].show=True
                                self.countdown.dict['1'].show=False
                            elif self.icountdown==1:
                                self.countdown.dict['3'].show=False
                                self.countdown.dict['2'].show=False
                                self.countdown.dict['1'].show=True
                        else: # flip to checking state (elder doesnt choose anymore)
                            self.checking=True
                            if self.elderalwayswin:# elder counters last moment
                                if self.herochoice==0:
                                    self.elderchoice=1
                                elif self.herochoice==1:
                                    self.elderchoice=2#
                                else:
                                    self.elderchoice=0
                            elif self.elderalwaysloose:# elder bad counters las moment
                                if self.herochoice==0:
                                    self.elderchoice=2
                                elif self.herochoice==1:
                                    self.elderchoice=0#
                                else:
                                    self.elderchoice=1
                            self.resulthero=self.herochoice
                            self.resultelder=self.elderchoice
                            self.hero.dict['rock'].show=False
                            self.hero.dict['paper'].show=False
                            self.hero.dict['scissors'].show=False
                            self.elder.dict['rock'].show=False
                            self.elder.dict['paper'].show=False
                            self.elder.dict['scissors'].show=False
                            self.result.dict['herorock'].show=self.resulthero==0
                            self.result.dict['heropaper'].show=self.resulthero==1
                            self.result.dict['heroscissors'].show=self.resulthero==2
                            self.result.dict['elderrock'].show=self.resultelder==0
                            self.result.dict['elderpaper'].show=self.resultelder==1
                            self.result.dict['elderscissors'].show=self.resultelder==2
                            self.hero.dict['thinkcloud'].show=False
                            self.elder.dict['thinkcloud'].show=False
                            self.hero.dict['talkcloud'].show=True
                            self.elder.dict['talkcloud'].show=True
                            self.countdown.dict['3'].show=False
                            self.countdown.dict['2'].show=False
                            self.countdown.dict['1'].show=False
                            self.instructions.dict['texta'].show=False
                            self.instructions.dict['textw'].show=False
                            self.instructions.dict['textd'].show=False
                            self.instructions.dict['texts'].show=False
                            self.instructions.dict['textn'].show=True
                            self.instructions.dict['texte'].show=False
                            self.staticactor.dict['hero'].show=True
                            self.staticactor.dict['elder'].show=True
                            self.staticactor.dict['herowalk'].show=False
                            self.staticactor.dict['elderwalk'].show=False
            #
            else:#checking state
                # compute results once
                if not self.computedresults:
                    self.computedresults=True
                    outcome=2# outcome=0,1,2 for hero wins, elder wins, tie
                    if self.resultelder==self.resulthero:# tie
                        outcome=2
                    else:
                        if self.resultelder==0:# hero: rock, elder: paper
                            if self.resulthero==1:
                                outcome=0
                                self.result.dict['paperrock'].show=True
                            else:
                                outcome=1
                                self.result.dict['rockscissors'].show=True
                        elif self.resultelder==1:
                            if self.resulthero==2:
                                outcome=0
                                self.result.dict['scissorspaper'].show=True
                            else:
                                outcome=1
                                self.result.dict['paperrock'].show=True
                        elif self.resultelder==2:
                            if self.resulthero==0:
                                outcome=0
                                self.result.dict['rockscissors'].show=True
                            else:
                                outcome=1
                                self.result.dict['scissorspaper'].show=True
                    if outcome==0:# hero wins
                        self.elderhealth -= 1
                        self.soundstrike.play()
                        if self.elderhealth>-1:
                            self.healthbar.dict['elder_'+str(self.elderhealth)].show=False
                            self.healthbar.dict['eldercross_'+str(self.elderhealth)].show=True
                        self.result.dict['win'].show=True
                        self.result.dict['loose'].show=False
                        self.result.dict['tie'].show=False
                    elif outcome==1:# elder wins
                        self.herohealth -= 1
                        self.soundhit.play()
                        if self.herohealth>-1:
                            self.healthbar.dict['hero_'+str(self.herohealth)].show=False
                            self.healthbar.dict['herocross_'+str(self.herohealth)].show=True
                        self.result.dict['win'].show=False
                        self.result.dict['loose'].show=True
                        self.result.dict['tie'].show=False
                    else:# tie
                        self.soundtie.play()
                        self.result.dict['win'].show=False
                        self.result.dict['loose'].show=False
                        self.result.dict['tie'].show=True
                    if self.herohealth==0 or self.elderhealth==0:# endgame message
                        self.instructions.dict['textn'].show=False
                        self.instructions.dict['texte'].show=True
                if controls.ga and controls.gac:# flip back to deciding state (or to end of the game)
                    if self.herohealth==0:# elder won entire game
                        self.sounddie.play()
                        self.goal=True
                        self.win=False
                        self.timerendloose.start()
                        self.text_donelost.show=True
                        self.staticactor.dict['hero'].show=False
                        self.staticactor.dict['herowalk'].show=False
                        self.staticactor.dict['elderwalk'].show=False
                        self.endgame.dict['loose'].show=True
                        self.endgame.dict['loose'].rewind()
                    elif self.elderhealth==0:# hero won entire game
                        self.soundwin.play()
                        self.goal=True
                        self.win=True
                        self.timerendwin.start()
                        self.text_donewin.show=True
                        self.staticactor.dict['elder'].show=False
                        self.staticactor.dict['herowalk'].show=False
                        self.staticactor.dict['elderwalk'].show=False
                        self.endgame.dict['win'].show=True
                        self.endgame.dict['win'].rewind()
                    else:# keep playing
                        self.soundcount.play()
                        self.checking=False
                        self.countdowning=False
                        self.computedresults=False
                        # clean healthbars
                        for i in range(self.herohealthmax):
                            self.healthbar.dict['herocross_'+str(i)].show=False
                        for i in range(self.elderhealthmax):
                            self.healthbar.dict['eldercross_'+str(i)].show=False
                    # images shown
                    if self.goal:
                        self.hero.dict['rock'].show=False
                        self.hero.dict['paper'].show=False
                        self.hero.dict['scissors'].show=False
                        self.elder.dict['rock'].show=False
                        self.elder.dict['paper'].show=False
                        self.elder.dict['scissors'].show=False
                        self.hero.dict['thinkcloud'].show=False
                        self.elder.dict['thinkcloud'].show=False
                        self.instructions.dict['texta'].show=False
                        self.instructions.dict['textw'].show=False
                        self.instructions.dict['textd'].show=False
                        self.instructions.dict['texts'].show=False
                    else:
                        if self.elderchoice==0:# elder does a new random choice
                            self.elderchoice=tool.randchoice([1,2])
                        elif self.elderchoice==1:
                            self.elderchoice=tool.randchoice([0,2])
                        else:
                            self.elderchoice=tool.randchoice([0,1])
                        self.hero.dict['rock'].show=self.herochoice==0
                        self.hero.dict['paper'].show=self.herochoice==1
                        self.hero.dict['scissors'].show=self.herochoice==2
                        self.elder.dict['rock'].show=self.elderchoice==0
                        self.elder.dict['paper'].show=self.elderchoice==1
                        self.elder.dict['scissors'].show=self.elderchoice==2
                        self.hero.dict['thinkcloud'].show=True
                        self.elder.dict['thinkcloud'].show=True
                        self.instructions.dict['texta'].show=True
                        self.instructions.dict['textw'].show=True
                        self.instructions.dict['textd'].show=True
                        self.instructions.dict['texts'].show=True
                    self.result.dict['herorock'].show=False
                    self.result.dict['heropaper'].show=False
                    self.result.dict['heroscissors'].show=False
                    self.result.dict['elderrock'].show=False
                    self.result.dict['elderpaper'].show=False
                    self.result.dict['elderscissors'].show=False
                    self.result.dict['win'].show=False
                    self.result.dict['loose'].show=False
                    self.result.dict['tie'].show=False
                    self.hero.dict['talkcloud'].show=False
                    self.elder.dict['talkcloud'].show=False
                    self.result.dict['paperrock'].show=False
                    self.result.dict['rockscissors'].show=False
                    self.result.dict['scissorspaper'].show=False
                    self.instructions.dict['textn'].show=False
                    self.instructions.dict['texte'].show=False
                    for i in range(self.herohealth):
                        self.healthbar.dict['herocross_'+str(i)].show=False
                    for i in range(self.elderhealth):
                        self.healthbar.dict['eldercross_'+str(i)].show=False
        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                if self.timerendwin.ring:
                    self.done=True# end of minigame
            else:# lost minigame
                self.timerendloose.update()
                if self.timerendloose.ring:
                    self.done=True# end of minigame


####################################################################################################################
# *BUSH *STEALTH
#
# A skeleton grand actor for the bushstealth game
class obj_grandactor_bushstealthskeleton(obj_grandactor):
    def setup(self):
        super().setup()
        self.state=0# states=0,1,2,3 for standing, thinking, walking, busting
        self.faceright=True# looking right or left
        self.timer=tool.obj_timer(50)# timer for switch states (first switch is quick)
        self.timer.start()
        self.mx=3# move rate
        self.minvision=100# vision min distance (must be >)
        self.maxvision=500# vision max distance (must be <)
        # images
        self.makebaseimages()
        self.addpart('viewright', draw.obj_image('skeletonview',(self.x+250,self.y),path='data/premade') )
        self.addpart('viewleft', draw.obj_image('skeletonview',(self.x-250,self.y),path='data/premade',fliph=True) )
        self.dict['standing'].show=True
        self.dict['walking'].show=False
        self.dict['thinking'].show=False
        self.dict['busting'].show=False
        self.dict['bustingmark'].show=False
        self.dict['viewright'].show=self.faceright
        self.dict['viewleft'].show=not self.faceright
        # boundaries (for walking)
        self.xmin=200
        self.xmax=1280-200
        # audio
        self.makebasesounds()
    def makebaseimages(self):
        self.addpart('standing', draw.obj_image('skeletonbase',(self.x,self.y),scale=0.5) )
        # self.addpart('walking', draw.obj_animation('bushstealth_skeletonmove','skeletonbase',(self.x,self.y)) )
        animation1=draw.obj_animation('bushstealth_skeletonmove','skeletonbase',(self.x,self.y))
        animation1.addsound("skeleton1", [5])
        animation1.addsound("skeleton3", [40])
        self.addpart('walking', animation1)
        self.addpart('thinking', draw.obj_image('interrogationmark',(self.x,self.y-200),scale=1,path='data/premade') )
        self.addpart('busting', draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(self.x,self.y)) )
        self.addpart('bustingmark', draw.obj_image('exclamationmark',(self.x,self.y-200),scale=1,path='data/premade') )
    def makebasesounds(self):
        self.soundthink=draw.obj_sound('skeleton2')
        self.creator.creator.addpart(self.soundthink)# add to page (from hierarchy page>world>grandactor)
    def turnaround(self):
        if self.faceright:
            self.turnleft()
        else:
            self.turnright()
    def turnleft(self):
        self.faceright=False
        self.dict['standing'].ifliph()
        self.dict['walking'].ifliph()
        self.dict['busting'].ifliph()
        self.dict['viewright'].show=self.faceright
        self.dict['viewleft'].show=not self.faceright
    def turnright(self):
        self.faceright=True
        self.dict['standing'].ofliph()
        self.dict['walking'].ofliph()
        self.dict['busting'].ofliph()
        self.dict['viewright'].show=self.faceright
        self.dict['viewleft'].show=not self.faceright
    def cansee(self,x):# check if can see target
        if abs(x-self.x)<self.maxvision and abs(x-self.x)>self.minvision:# with min/max vision range
            if (x>self.x and self.faceright) or (x<self.x and not self.faceright):# correct direction
                return True
            else:
                return False
        else:
            return False
    def bust(self,x):# bust a target
        if x>self.x:
            self.turnright()
        else:
            self.turnleft()
        self.state=3# state 3=busting
        self.timer.end()
        self.dict['standing'].show=False
        self.dict['walking'].show=False
        self.dict['thinking'].show=False
        self.dict['busting'].show=True
        self.dict['bustingmark'].show=True
    def update(self,controls):
        super().update(controls)
        self.timer.update()
        if self.timer.ring:
            # if was thinking, then turn around
            # new state
            if self.state==0:# standing
                self.state=tool.randchoice([1,2],probas=[50,50])
            elif self.state==1:# thinking
                self.turnaround()# turn around
                self.state=tool.randchoice([0,2],probas=[50,50])
            elif self.state==2:# walking
                self.state=tool.randchoice([0,1],probas=[50,50])
            # new state duration
            if self.state==0:# standing
                self.timer.amount=150+tool.randint(0,100)
            elif self.state==1:# thinking
                self.timer.amount=50+tool.randint(0,100)
            elif self.state==2:# walking
                self.timer.amount=100+tool.randint(0,100)
            # start next timer
            self.timer.start()# next timer
            # switch to new state
            if self.state==0:# standing
                self.dict['standing'].show=True
                self.dict['walking'].show=False
                self.dict['thinking'].show=False
            elif self.state==1:# thinking
                self.dict['standing'].show=True
                self.dict['walking'].show=False
                self.dict['thinking'].show=True
                self.soundthink.play()
            elif self.state==2:
                self.dict['standing'].show=False
                self.dict['walking'].show=True
                self.dict['thinking'].show=False
        # movement
        if self.state==2:# walking
            if self.faceright:
                if self.x<self.xmax:
                    self.movex(self.mx)
                else:
                    self.timer.forcering()
            else:
                if self.x>self.xmin:
                    self.movex(-self.mx)
                else:
                    self.timer.forcering()


# same but with a sailor hat
class obj_grandactor_bushstealthskeleton_sailorhat(obj_grandactor_bushstealthskeleton):
    def makebaseimages(self):
        self.addpart('standing', draw.obj_image('skeletonbase_sailorhat',(self.x,self.y),scale=0.5) )
        # self.addpart('walking', draw.obj_animation('bushstealth_skeletonmove','skeletonbase_sailorhat',(self.x,self.y)) )
        animation1=draw.obj_animation('bushstealth_skeletonmove','skeletonbase_sailorhat',(self.x,self.y))
        animation1.addsound("skeleton1", [5])
        animation1.addsound("skeleton3", [40])
        self.addpart('walking', animation1)
        self.addpart('thinking', draw.obj_image('interrogationmark',(self.x,self.y-200),scale=1,path='data/premade') )
        self.addpart('busting', draw.obj_animation('bushstealth_skeletonalert','skeletonbase_sailorhat',(self.x,self.y)) )
        self.addpart('bustingmark', draw.obj_image('exclamationmark',(self.x,self.y-200),scale=1,path='data/premade') )
    def makebasesounds(self):
        self.soundthink=draw.obj_sound('skeleton4')
        self.creator.creator.addpart(self.soundthink)# add to page (from hierarchy page>world>grandactor)

# same but with partner hair
class obj_grandactor_bushstealthskeleton_partnerhair(obj_grandactor_bushstealthskeleton):
    def makebaseimages(self):
        self.addpart('standing', draw.obj_image('skeletonbase_partnerhair',(self.x,self.y),scale=0.5) )
        # self.addpart('walking', draw.obj_animation('bushstealth_skeletonmove','skeletonbase_partnerhair',(self.x,self.y)) )
        animation1=draw.obj_animation('bushstealth_skeletonmove','skeletonbase_partnerhair',(self.x,self.y))
        animation1.addsound("skeleton1", [5])
        animation1.addsound("skeleton3", [40])
        self.addpart('walking', animation1)
        self.addpart('thinking', draw.obj_image('interrogationmark',(self.x,self.y-200),scale=1,path='data/premade') )
        self.addpart('busting', draw.obj_animation('bushstealth_skeletonalert','skeletonbase_partnerhair',(self.x,self.y)) )
        self.addpart('bustingmark', draw.obj_image('exclamationmark',(self.x,self.y-200),scale=1,path='data/premade') )
    def makebasesounds(self):
        self.soundthink=draw.obj_sound('skeleton4')
        self.creator.creator.addpart(self.soundthink)# add to page (from hierarchy page>world>grandactor)

# # Mini Game: bush stealth
# *BUSH *STEALTH
class obj_world_bushstealth(obj_world):
    def setup(self,**kwargs):
        ####################################
        # these drawings are already made at drawing time...
        # combine skeletonhead+stickbody = skeletonbase
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
        # dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='data/premade') )
        # dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        # dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase')
        # skeleton with hair
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
        # dispgroup1.addpart('part2',draw.obj_image('partnerhair',(640,200)) )
        # dispgroup1.addpart('part3',draw.obj_image('stickheadnocontours',(640,200),path='data/premade') )
        # dispgroup1.addpart('part4',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        # dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_partnerhair')
        # skeleton with sailor hat
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
        # dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='data/premade') )
        # dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        # dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
        # dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_sailorhat')
        ####################################
        #
        # default parameters
        self.dowinsound=True# play a winning sound
        self.soundwinname='stealth_next'# name of winning sound if any
        # scene tuning
        if kwargs is not None:
            if 'winsound' in kwargs:# tell name of winning sound (or dont play if is None)
                if kwargs["winsound"]:
                    self.dowinsound=True
                    self.soundwinname=kwargs["winsound"]
                else:
                    self.dowinsound=False
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.win=False# won or not
        # default parameters
        self.heroxystart=(180,600)
        # layering
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.hero=obj_grandactor(self,self.heroxystart)
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_donewin.show=False
        self.text_donelost.show=False
        # background
        self.makebackground()# make the background
        self.staticactor.addpart( 'imgarrow', draw.obj_image('arrowup',(1280-100,600),rotate=-90,path='data/premade') )
        # hero
        self.hero.addpart( 'standing', draw.obj_image('bush',self.heroxystart,scale=0.5) )
        self.hero.addpart( 'moving', draw.obj_animation('bushstealth_bushmove','bush',self.heroxystart) )
        self.hero.addpart( 'movingspark', draw.obj_image('bushspark',(self.heroxystart[0],self.heroxystart[1]-100),path='data/premade') )
        self.hero.dict['moving'].show=False
        self.hero.dict['movingspark'].show=False
        self.hero.dict['standing'].show=True
        self.heromx=5# move rate
        self.heroxmin=100# boundaries
        self.heroxmax=1280-100
        self.herostanding=True# hero is standing or moving
        self.busted=False# hero has been busted
        self.xwin=1280-110# location to reach (with +-10)
        self.heromxwin=5# move rate (and direction) for animation when winning
        # skeleton(s)
        self.makeskeletons()
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('['+share.datamanager.controlname('arrows')+']: move',(640,660),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('Stealthy!',(640,200),fontsize='huge') )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('Busted!',(640,200),fontsize='huge') )
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(120)# goal to done
        #
        #audio
        self.soundmove1=draw.obj_sound('stealth_bush1')
        self.creator.addpart(self.soundmove1)
        self.soundmove2=draw.obj_sound('stealth_bush2')
        self.creator.addpart(self.soundmove2)
        self.soundmove3=draw.obj_sound('stealth_bush3')
        self.creator.addpart(self.soundmove3)
        self.timermovesound=tool.obj_timer(50)# timer for making sound when moving
        self.timermovesound.start()
        self.soundalarm=draw.obj_sound('stealth_alarm')
        self.creator.addpart(self.soundalarm)
        self.timeralarmsound=tool.obj_timer(80)# timer for repeating alarm sound
        self.timeralarmsound.start()
        if self.dowinsound:
            self.soundwin=draw.obj_sound(self.soundwinname)
            self.creator.addpart(self.soundwin)

    def makebackground(self):
        self.staticactor.addpart( 'img1', draw.obj_image('palmtree',(1148,291),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img2', draw.obj_image('palmtree',(1010,268),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( 'img3', draw.obj_image('floor6',(640,300),path='data/premade') )
        self.staticactor.addpart( "img1a", draw.obj_image('bush',(890,342),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img2a", draw.obj_image('bush',(307,363),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img3a", draw.obj_animation('bushstealth_moonmove','moon',(640,360),record=False) )

        # self.staticactor.addpart( 'img4', draw.obj_image('floor6',(640,720-50),path='data/premade') )
    def makeskeletons(self):
        self.skeletons=[]
        self.skeletons.append( obj_grandactor_bushstealthskeleton(self,(800,500),foreground=False)   )
    def makemovesound(self):# make a moving sound (choose randomly)
        i=tool.randchoice([self.soundmove1,self.soundmove2,self.soundmove3])
        i.play()

    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # move hero
            if controls.glc or controls.grc:# new input=change in stance
                if controls.gl or controls.gr:# flip to moving
                    self.herostanding=False
                    self.hero.dict['moving'].show=True
                    self.hero.dict['movingspark'].show=True
                    self.hero.dict['standing'].show=False
                    self.hero.dict['moving'].rewind()
                    self.timermovesound.start()
                    # flip orientation
                    if controls.gl and controls.glc:
                        self.makemovesound()
                        self.hero.dict['moving'].ifliph()
                        self.hero.dict['movingspark'].ifliph()
                        self.hero.dict['standing'].ifliph()
                    elif controls.gr and controls.grc:
                        self.makemovesound()
                        self.hero.dict['moving'].ofliph()
                        self.hero.dict['movingspark'].ofliph()
                        self.hero.dict['standing'].ofliph()
                else:# flip to standing
                    self.herostanding=True
                    self.hero.dict['moving'].show=False
                    self.hero.dict['movingspark'].show=False
                    self.hero.dict['standing'].show=True
                    self.timermovesound.start()# reset timer
            # move sounds
            if not self.herostanding:
                self.timermovesound.update()
            if self.timermovesound.ring:
                self.makemovesound()
                self.timermovesound.start()
            # hero move and boundaries
            if not self.herostanding:
                if controls.gl and self.hero.x>self.heroxmin:
                    self.hero.movex(-self.heromx)
                if controls.gr and self.hero.x<self.heroxmax:
                    self.hero.movex(self.heromx)
                # check if is seen by any skeleton
                for i in self.skeletons:
                    if i.cansee(self.hero.x):
                        self.busted=True
                        self.goal=True
                        self.win=False
                        self.timerendloose.start()
                        self.text_undone.show=False
                        self.text_donelost.show=True
                        self.soundalarm.play()
            # win if reach the location
            if abs(self.hero.x-self.xwin)<10:
                self.goal=True
                self.win=True
                self.timerendwin.start()
                self.text_undone.show=False
                self.text_donewin.show=True
                if self.dowinsound:
                    self.soundwin.play()
        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                if self.timerendwin.ring:
                    self.done=True# end of minigame
                # hero keeps going to the right
                self.hero.movex(self.heromxwin)

            else:# lost minigame
                self.timerendloose.update()
                if self.timerendloose.ring:
                    self.done=True# end of minigame
                # busted animation
                if self.busted:
                    for i in self.skeletons:
                        i.bust(self.hero.x)
                # alarm sound
                self.timeralarmsound.update()
                if self.timeralarmsound.ring:
                    self.soundalarm.play()
                    self.timeralarmsound.start()


# base one but no enemy
class obj_world_bushstealth0(obj_world_bushstealth):
    def makeskeletons(self):
        self.skeletons=[]

class obj_world_bushstealth2(obj_world_bushstealth):
    def makebackground(self):
        self.staticactor.addpart( "img1", draw.obj_image('palmtree',(157,267),scale=0.36,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img2", draw.obj_image('palmtree',(298,284),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img4", draw.obj_image('palmtree',(860,261),scale=0.52,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img5", draw.obj_image('bush',(1035,519),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img3a', draw.obj_image('floor7',(640,300),path='data/premade') )
        self.staticactor.addpart( "img3b", draw.obj_animation('bushstealth_moonmove','moon',(640+300,360+10),record=False) )
    def makeskeletons(self):
        self.skeletons=[]
        skeleton1=obj_grandactor_bushstealthskeleton_sailorhat(self,(800,500),foreground=False)
        skeleton1.turnaround()
        self.skeletons.append(skeleton1)

class obj_world_bushstealth3(obj_world_bushstealth):
    def makebackground(self):
        self.staticactor.addpart( "img1", draw.obj_image('palmtree',(157,267),scale=0.36,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img2", draw.obj_image('palmtree',(298,284),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img4", draw.obj_image('palmtree',(860,261),scale=0.52,rotate=0,fliph=True,flipv=False) )
        self.staticactor.addpart( "img5", draw.obj_image('bush',(1035,519),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img3a', draw.obj_image('floor7',(640,300),path='data/premade') )
        self.staticactor.addpart( "img3b", draw.obj_animation('bushstealth_moonmove','moon',(640+300,360+10),record=False) )
    def makeskeletons(self):
        self.skeletons=[]
        skeleton1=obj_grandactor_bushstealthskeleton(self,(800,500),foreground=False)
        self.skeletons.append(skeleton1)
        skeleton2=obj_grandactor_bushstealthskeleton_sailorhat(self,(400,500),foreground=False)
        skeleton2.turnaround()
        self.skeletons.append(skeleton2)

class obj_world_bushstealth4(obj_world_bushstealth):
    def makebackground(self):
        self.staticactor.addpart( "img1", draw.obj_image('mountain',(1157,236),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img2", draw.obj_image('mountain',(971,304),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img4", draw.obj_image('palmtree',(150,299),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( "img6", draw.obj_image('bush',(417,571),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.staticactor.addpart( 'img3a', draw.obj_image('floor8',(640,300),path='data/premade') )
        self.staticactor.addpart( "img3b", draw.obj_animation('bushstealth_moonmove','moon',(640-500,360+20),record=False) )
    def makeskeletons(self):
        self.skeletons=[]
        skeleton1=obj_grandactor_bushstealthskeleton(self,(800,500),foreground=False)
        skeleton1.turnaround()
        self.skeletons.append(skeleton1)
        skeleton2=obj_grandactor_bushstealthskeleton_partnerhair(self,(550,500),foreground=False)
        skeleton2.turnaround()
        self.skeletons.append(skeleton2)


####################################################################################################################
#
# # Mini Game: ride a cow
# *RIDE *COW
class obj_world_ridecow(obj_world):
    def setup(self,**kwargs):
        # default parameter
        self.dotutorial=False# is tutorial of that game (cant win/loose)
        self.dotrees=True# there are trees to hit (remove for tutorial parts)
        # scene tuning
        if kwargs is not None:
            if 'tutorial' in kwargs: self.dotutorial=kwargs["tutorial"]# tutorial of game
            if 'trees' in kwargs: self.dotrees=kwargs["trees"]
        #
        # combine herobase+cow=heroridecow
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('herobase',(640,360-100),scale=0.5) )
        dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecow')
        # combine herobase+cow=heroridecow
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('herobaseangry',(640,360-100),scale=0.5,flipv=True) )
        dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecowangry')
        # cow alone in combo
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecownohero')
        # hero alone in combo
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('herobaseangry',(640,360-100),scale=0.5,flipv=True) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecownocow')
        ##########################33
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.win=False# won/lost the game
        # default parameters
        self.heroxystart=(350,360)
        # layering
        self.staticactor=obj_grandactor(self,(640,360))
        self.hero=obj_grandactor(self,self.heroxystart)
        self.staticactor.show=True
        self.hero.show=True
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_donewin.show=False
        self.text_donelost.show=False
        self.text_start=obj_grandactor(self,(640,360))# text message at start
        self.text_start.show=True

        # static actor
        if not self.dotutorial:
            self.staticactor.addpart( 'anim1', draw.obj_animation('ch6_skeletonrun','skeletonbase',(640,360-200)) )
        self.staticactor.addpart( 'anim2', draw.obj_animation('ch6_skeletonrun','skeletonbase',(640,360-100)) )
        self.staticactor.addpart( 'anim3', draw.obj_animation('ch6_skeletonrun','skeletonbase',(640,360)) )
        #
        # self.staticactor.addpart( 'anim4', draw.obj_animation('ch6_skeletonrun','skeletonbase_sailorhat',(640,360+200)) )
        animation1=draw.obj_animation('ch6_skeletonrun','skeletonbase_sailorhat',(640,360+100))
        animation1.addsound( "skeleton4", [1])
        animation1.addsound( "skeleton2", [64],skip=3)# breathing (turned off if wins)
        self.staticactor.addpart( 'anim4', animation1 )
        #
        # self.staticactor.addpart( 'anim5', draw.obj_animation('ch6_skeletonrun','skeletonbase',(640,360-200)) )
        animation2=draw.obj_animation('ch6_skeletonrun','skeletonbase',(640,360+200))
        # animation2.addsound( "skeleton1", [1])
        # animation2.addsound( "skeleton3", [31])
        self.staticactor.addpart( 'anim5', animation2 )

        # hero
        self.yhero=50# offset hitbox images for hero
        # self.hero.addpart( 'img', draw.obj_image('heroridecow',(self.heroxystart[0],self.heroxystart[1]),scale=0.5) )
        self.hero.addpart( 'img', draw.obj_animation('gameheroridecow','heroridecow',(self.heroxystart[0],self.heroxystart[1]+self.yhero)) )
        # self.hero.addpart( 'hurt', draw.obj_image('heroridecowangry',(self.heroxystart[0],self.heroxystart[1]),scale=0.5) )
        self.hero.addpart( 'hurt', draw.obj_animation('gameheroridecow','heroridecowangry',(self.heroxystart[0],self.heroxystart[1]+self.yhero)) )
        self.hero.dict['img'].show=True
        self.hero.dict['hurt'].show=False
        self.hero.rx=25
        self.hero.ry=30#75#50# REDUCED
        self.heromx=5# move rate
        self.heromy=7#
        self.heroxmin=300# boundaries
        self.heroxmax=1280-200
        self.heroymin=50
        self.heroymax=720-50
        self.herohurting=False# hero is hurting or not
        self.timerhurting=tool.obj_timer(150)# animation for hero hurt (cant be hit during that time)
        # Speed and shot

        #
        # shots (they are actually obstacles)
        self.nshots=100#50# number of shots before winning
        self.ishots=self.nshots
        self.shooting=True# shoot new ones or not
        self.shots=[]# empty list
        self.shottimer=tool.obj_timer(20)#tool.obj_timer(20)# time between obstacles
        self.runspeed=8#7#5# moving speed of background and obstacles
        self.shottimer.start()
        self.shotx0=1280+200
        self.shoty0min=self.heroymin-50
        self.shoty0max=self.heroymax+50
        self.xkill=150# position at which they disappear
        # self.shotprobas=[40,0,60]# probas of palmtree, rock, bush...
        if self.dotrees:
            # self.shotprobas=[25,25,50]# probas of palmtree, rock, bush...
            self.shotprobas=[35,35,30]# probas of palmtree, rock, bush...
        else:
            self.shotprobas=[0,0,100]
        # health bar
        self.maxherohealth=5# starting hero health (reference=always 3)
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(640,360),foreground=False)
        if self.dotutorial:
            self.ybar=150# for health bars and text
        else:
            self.ybar=50
        self.healthbar.addpart('face', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.maxherohealth):
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )


        # for i in range(self.maxherohealth):
        #     if self.dotutorial:
        #         self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(50+i*75+130,150),scale=0.125) )
        #     else:
        #         self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(50+i*75,50),scale=0.125) )


        # timer for done part
        self.timerendwin=tool.obj_timer(180)# goal to done
        self.timerendloose=tool.obj_timer(180)# goal to done
        self.loosemx=7# skeleton move rate if loose
        self.winmx=3# hero move rate if wins
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('['+share.datamanager.controlname('arrows')+']: move',(640,660),color=share.colors.instructions) )
        self.text_undone.addpart( 'progress', draw.obj_textbox('0%',(1090,640)) )
        self.text_undone.addpart( 'progressimg', draw.obj_image('sailboat',(1280-75,720-75),scale=0.25) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('you made it!',(640,360),fontsize='huge') )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('you died!',(640,360),fontsize='huge') )
        # start message at beginning
        self.timerfightmessage=tool.obj_timer(80)
        if not self.dotutorial:
            self.text_start.addpart( 'startmessage', draw.obj_animation('dodgebullets_fightmessage','messagestart',(640,360), path='data/premade') )
            self.timerfightmessage.start()

        # devtool
        self.staticactor.addpart( 'dev1', draw.obj_textbox('shots='+str(self.ishots),(1200,680),color=share.colors.red) )
        self.staticactor.dict['dev1'].show=False
        # audio
        self.soundhit=draw.obj_sound('ridecow_hit')
        self.creator.addpart(self.soundhit)
        self.soundhitgasp=draw.obj_sound('ridecow_hitgasp')# add to hit sound
        self.creator.addpart(self.soundhitgasp)
        self.sounddie=draw.obj_sound('ridecow_die')
        self.creator.addpart(self.sounddie)
        self.soundwin=draw.obj_sound('ridecow_win')
        self.creator.addpart(self.soundwin)
        #
        if not self.dotutorial:
            self.soundstart=draw.obj_sound('ridecow_start')
            self.soundstart.play()# at start
        #
    def makeshot(self,x,y,s):
        shot=obj_grandactor(self,(x,y),foreground=False)
        dice=tool.randchoice(['palmtree','rock','bush'],probas=self.shotprobas)
        if dice=='palmtree':
            shot.addpart('img', draw.obj_image('palmtree',(x,y),scale=0.5,fliph=tool.randbool()) )
            shot.hurts=True# does the obstacle hurt the hero
            shot.rx,shot.ry=25,30# hitbox
        elif dice=='rock':
            shot.addpart('img', draw.obj_image('rock',(x,y),scale=0.25,fliph=tool.randbool()) )
            shot.hurts=True
            shot.rx,shot.ry=25,15# hitbox
        elif dice=='bush':
            shot.addpart('img', draw.obj_image('bush',(x,y),scale=0.25,fliph=tool.randbool()) )
            shot.hurts=False# harmless
            shot.rx,shot.ry=1,1# hitbox (irrelevant if harmless)
        shot.speed=s# speed
        self.shots.append(shot)
    def killshot(self,shot):
        self.shots.remove(shot)
        shot.kill()
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # start message at beginning
            if self.timerfightmessage.on:
                self.timerfightmessage.update()
                if self.timerfightmessage.ring:
                    self.text_start.show=False
            # progress bar
            textprogress=100-int(self.ishots/self.nshots*100)
            textprogress=min(textprogress,100)
            textprogress=max(textprogress,0)
            self.text_undone.dict['progress'].replacetext( str(textprogress)+'%' )
            # move hero
            if controls.gl and self.hero.x>self.heroxmin:
                self.hero.movex(-self.heromx)
            if controls.gr and self.hero.x<self.heroxmax:
                self.hero.movex(self.heromx)
            if controls.gu and self.hero.y>self.heroymin:
                self.hero.movey(-self.heromy)
            if controls.gd and self.hero.y<self.heroymax:
                self.hero.movey(self.heromy)
            # shots (obstacles)
            self.shottimer.update()
            if self.shooting and self.shottimer.ring:# generate
                if not self.dotutorial:# no shot depletion if tutorial
                    self.ishots -= 1
                self.shoty0=tool.randint(self.shoty0min,self.shoty0max)
                self.makeshot(self.shotx0,self.shoty0,-self.runspeed)
                self.shottimer.start()# restart for next shot
            if self.shots:# move left
                for i in self.shots:
                    i.movex(i.speed)
            if self.shots:# kill shots
                for i in self.shots:
                    if i.x<self.xkill:
                        self.killshot(i)
            if self.ishots<0:# shot depletion
                self.shooting=False
            # shots hit the hero
            if self.shots:# kill shots
                for i in self.shots:
                    # obstacle hits hero if: not hurting, obstacle hurts hero (not a bush), and they collide
                    if not self.herohurting and i.hurts and tool.checkrectcollide(self.hero,i):
                        self.killshot(i)# remove shot
                        if not self.dotutorial:# no health depletion if tutorial
                            self.herohealth -= 1# loose health
                        self.herohurting=True# to hurting state
                        self.timerhurting.start()
                        self.hero.dict['img'].show=False
                        self.hero.dict['hurt'].show=True
                        # hero looses health or dies
                        if self.herohealth>0:
                            self.soundhit.play()
                            self.soundhitgasp.play()
                            if not self.dotutorial:# no loosing hearts on tutorial
                                self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        else:
                            # switch to lost
                            self.soundhit.play()
                            self.sounddie.play()
                            self.goal=True
                            self.win=False
                            self.healthbar.dict['heart_0'].show=False
                            self.hero.dict['img'].show=True# hero on its own, stays static
                            self.hero.dict['hurt'].show=True# cow on its own, will keep running
                            self.hero.dict['img'].replaceimage('heroridecownocow',0)# beware this is instead an animation
                            self.hero.dict['hurt'].replaceimage('heroridecownohero',0)
                            self.timerendloose.start()
                            self.text_undone.show=False
                            self.text_donelost.show=True
                            # if self.shots:
                            #     for i in self.shots:
                            #         i.dict['img'].show=False
            # hero hurting
            if self.herohurting:
                self.timerhurting.update()
                if self.timerhurting.ring:
                    self.herohurting=False
                    self.hero.dict['img'].show=True
                    self.hero.dict['hurt'].show=False
            # winning (end all shots)
            if not self.shooting and len(self.shots)<1:# no more shots
                self.goal=True
                self.win=True
                self.timerendwin.start()
                self.healthbar.dict['heart_0'].show=True# in case lost on that frame
                self.hero.dict['img'].show=True
                self.hero.dict['hurt'].show=False
                self.text_undone.show=False
                self.text_donewin.show=True
                self.soundwin.play()
                # remove sounds from animations
                self.staticactor.dict['anim4'].removesound( "skeleton4")
                self.staticactor.dict['anim4'].removesound( "skeleton2")


            # devtool (show number of shots)
            if share.devmode:
                self.staticactor.dict['dev1'].show=True
                self.staticactor.dict['dev1'].replacetext('shots='+str(self.ishots))
            else:
                self.staticactor.dict['dev1'].show=False
        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                # hero moves to the right (??)
                self.hero.dict['img'].movex(self.winmx)
                self.hero.dict['hurt'].movex(self.winmx)
                # self.staticactor.dict['anim1'].movex(-self.winmx)
                # self.staticactor.dict['anim2'].movex(-self.winmx)
                # self.staticactor.dict['anim3'].movex(-self.winmx)
                # self.staticactor.dict['anim4'].movex(-self.winmx)
                # self.staticactor.dict['anim5'].movex(-self.winmx)
                if self.shots:# move all shots to the left
                    for i in self.shots:
                        i.movex(i.speed)
                self.staticactor.dict['dev1'].show=share.devmode
                if self.timerendwin.ring:
                    self.done=True# end of minigame
            else:# lost minigame
                self.timerendloose.update()
                # Move the skeletons to the right
                self.hero.dict['hurt'].movex(self.loosemx)# move the cow to right
                self.staticactor.dict['anim1'].movex(self.loosemx)
                self.staticactor.dict['anim2'].movex(self.loosemx)
                self.staticactor.dict['anim3'].movex(self.loosemx)
                self.staticactor.dict['anim4'].movex(self.loosemx)
                self.staticactor.dict['anim5'].movex(self.loosemx)
                self.staticactor.dict['dev1'].show=share.devmode
                if self.timerendloose.ring:
                    self.done=True# end of minigame


####################################################################################################################

# Mech fight
#*MECH *FIGHT
class obj_world_mechfight(obj_world):
    def setup(self,**kwargs):

        ##########################3
        # Premake necessary images (can be slow to load!)
        # (already done during drawing completion by datb.snapshotmanager)
        # villainmech armature
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
        # dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
        # dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        # dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        # dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640-200,400),path='data/premade') )
        # dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640+200,400),path='data/premade') )
        # dispgroup1.snapshot((640,360,300,220),'villainmecharmature')
        # villainmech complete
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('villainmecharmature',(640,360)) )
        # dispgroup1.addpart( 'part2', draw.obj_image('tower',(640,180),scale=0.35) )
        # dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
        # dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
        # dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
        # dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
        # dispgroup1.snapshot((640,360,410,330),'villainmechbase')
        #
        # villainmech
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        # dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        # dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640-200,400),path='data/premade') )
        # dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640+200,400),path='data/premade') )
        # dispgroup1.snapshot((640,360,300,220),'villainmecharmature_noface')
        # villainnech no face
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('villainmecharmature_noface',(640,360),path='data/premade') )
        # dispgroup1.addpart( 'part2', draw.obj_image('tower',(640,180),scale=0.35) )
        # dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
        # dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
        # dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
        # dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
        # dispgroup1.snapshot((640,360,410,330),'villainmechbase_noface')
        #
        # heromech armature
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5) )
        # dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade',fliph=True ) )
        # dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640+200,400),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640-200,400),path='data/premade',fliph=True) )
        # dispgroup1.snapshot((640,360,300,220),'heromecharmature')
        # heromech complete
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature',(640,360)) )
        # dispgroup1.addpart( 'part2', draw.obj_image('house',(640,180),scale=0.35) )
        # dispgroup1.addpart( 'part3', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part4', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('fish',(640-300,470),scale=0.3,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part6', draw.obj_image('flower',(640+300,470),scale=0.35,rotate=-45,flipv=True) )
        # dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
        # dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
        # dispgroup1.addpart( 'part9', draw.obj_image('villainmech_legs1',(640,520),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part10', draw.obj_image('villainmech_larm1',(640+200,400),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part11', draw.obj_image('villainmech_rarm1',(640-200,400),path='data/premade',fliph=True) )
        # dispgroup1.snapshot((640,360,410,330),'heromechbase')
        #
        # heromech basis (redundant with villainmecharmature_noface expcept maybe for fliph)
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade',fliph=True ) )
        # dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640+200,400),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640-200,400),path='data/premade',fliph=True) )
        # dispgroup1.snapshot((640,360,300,220),'heromecharmature_noface')# move to premade
        # heromech no face
        # dispgroup1=draw.obj_dispgroup((640,360))
        # dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature_noface',(640,360),path='data/premade') )
        # dispgroup1.addpart( 'part2', draw.obj_image('house',(640,180),scale=0.35) )
        # dispgroup1.addpart( 'part3', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part4', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        # dispgroup1.addpart( 'part5', draw.obj_image('fish',(640-300,470),scale=0.3,rotate=45,fliph=False) )
        # dispgroup1.addpart( 'part6', draw.obj_image('flower',(640+300,470),scale=0.35,rotate=-45,flipv=True) )
        # dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
        # dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
        # dispgroup1.addpart( 'part9', draw.obj_image('villainmech_legs1',(640,520),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part10', draw.obj_image('villainmech_larm1',(640+200,400),path='data/premade',fliph=True) )
        # dispgroup1.addpart( 'part11', draw.obj_image('villainmech_rarm1',(640-200,400),path='data/premade',fliph=True) )
        # dispgroup1.snapshot((640,360,410,330),'heromechbase_noface')
        #
        # The snapshots below are remade for the minigame, because they arent used anywhere else
        # villainmech punch
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part4', draw.obj_image('tower',(640,180),scale=0.35) )
        dispgroup1.addpart( 'part5', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part6', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part7', draw.obj_image('mechpunch',(640,360),path='data/premade') )
        dispgroup1.addpart( 'part8', draw.obj_image('gun',(233,373),scale=0.3,rotate=0,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part9', draw.obj_image('cave',(585,619),scale=0.35,rotate=0,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part10', draw.obj_image('cave',(838,617),scale=0.35,rotate=0,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part11', draw.obj_image('lightningbolt',(907,479),scale=0.35,rotate=54,fliph=False,flipv=False) )
        dispgroup1.snapshot((640-50,360,500-50,330),'villainmechpunch')
        # heromech punch
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part3', draw.obj_image('house',(640,180),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part4', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part5', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part6', draw.obj_image('mechpunch',(640,360),path='data/premade') )
        dispgroup1.addpart( 'part7', draw.obj_image('fish',(233,373),scale=0.3,rotate=0,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(585,619),scale=0.25,rotate=0,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part9', draw.obj_image('sailboat',(838,617),scale=0.25,rotate=0,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part10', draw.obj_image('flower',(907,479),scale=0.35,rotate=54,fliph=True,flipv=True) )
        dispgroup1.snapshot((640-50,360,500-50,330),'heromechpunch')
        # villainmech block
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        dispgroup1.addpart( 'part5', draw.obj_image('tower',(640,180),scale=0.35) )
        dispgroup1.addpart( 'part6', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part7', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part8', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part9', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
        dispgroup1.addpart( 'part10', draw.obj_image('mechblock',(640-200,360),path='data/premade') )
        dispgroup1.addpart( 'part11', draw.obj_image('gun',(242,316),scale=0.3,rotate=66,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part12', draw.obj_image('lightningbolt',(378,324),scale=0.35,rotate=174,fliph=True,flipv=False) )
        dispgroup1.snapshot((640-80,360,500-80,330),'villainmechblock')
        # heromech block
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        dispgroup1.addpart( 'part4', draw.obj_image('house',(640,180),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part5', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part6', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
        dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
        dispgroup1.addpart( 'part9', draw.obj_image('mechblock',(640-200,360),path='data/premade') )
        dispgroup1.addpart( 'part10', draw.obj_image('fish',(242,316),scale=0.3,rotate=-66,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part11', draw.obj_image('flower',(378,324),scale=0.35,rotate=174,fliph=False,flipv=True) )
        dispgroup1.snapshot((640-80,360,500-80,330),'heromechblock')
        # villainmech hit
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        dispgroup1.addpart( 'part5', draw.obj_image('tower',(640,180),scale=0.35) )
        dispgroup1.addpart( 'part6', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part7', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
        dispgroup1.addpart( 'part8', draw.obj_image('mechhit',(640,360-100),path='data/premade') )
        dispgroup1.addpart( 'part10', draw.obj_image('gun',(467,104),scale=0.3,rotate=90,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part11', draw.obj_image('lightningbolt',(821,102),scale=0.35,fliph=True,flipv=True) )
        dispgroup1.addpart( 'part12', draw.obj_image('mountain',(640-200,400),scale=0.4,rotate=115,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part13', draw.obj_image('mountain',(640+200,400),scale=0.4,rotate=115,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part14', draw.obj_image('mechsparks',(640+240,270),scale=1,rotate=0,fliph=False,flipv=False,path='data/premade') )
        dispgroup1.addpart( 'part15', draw.obj_image('mechsparks',(640-240,270),scale=1,rotate=0,fliph=True,flipv=False,path='data/premade') )
        dispgroup1.snapshot((640,360,300,350),'villainmechhit')
        # heromech hit
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('villainmechcase',(640,360),path='data/premade' ) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmech_legs1',(640,520),path='data/premade') )
        dispgroup1.addpart( 'part4', draw.obj_image('house',(640,180),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part5', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
        dispgroup1.addpart( 'part6', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
        dispgroup1.addpart( 'part7', draw.obj_image('mechhit',(640,360-100),path='data/premade') )
        dispgroup1.addpart( 'part8', draw.obj_image('fish',(467,104),scale=0.3,rotate=90,fliph=True,flipv=True) )
        dispgroup1.addpart( 'part9', draw.obj_image('flower',(821,102),scale=0.35,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part10', draw.obj_image('bush',(640-200,400),scale=0.4,rotate=115,fliph=False,flipv=False) )
        dispgroup1.addpart( 'part11', draw.obj_image('bush',(640+200,400),scale=0.4,rotate=115,fliph=True,flipv=False) )
        dispgroup1.addpart( 'part12', draw.obj_image('mechsparks',(640+240,270),scale=1,rotate=0,fliph=False,flipv=False,path='data/premade') )
        dispgroup1.addpart( 'part13', draw.obj_image('mechsparks',(640-240,270),scale=1,rotate=0,fliph=True,flipv=False,path='data/premade') )
        dispgroup1.snapshot((640,360,300,350),'heromechhit')
        # Prompt Images

        ##########################
        # default options
        self.dotutorial=False# do the tutorial
        self.doprompt=True# do prompt (if none, random outcome, for tutorial)
        self.dohealth=True# show healthbar (can be hidden for tutorial)
        # scene tuning
        if kwargs is not None:
            if 'tutorial' in kwargs: self.dotutorial=kwargs["tutorial"]
            if 'prompt' in kwargs: self.doprompt=kwargs["prompt"]
            if 'healthbar' in kwargs: self.dohealth=kwargs["healthbar"]
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached (doesnt necessarily mean game is won)
        self.win=False# game is won when goal is reached or not
        # layering
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.promptactor=obj_grandactor(self,(640,360))
        self.actionactor=obj_grandactor(self,(640,360))
        self.herohealthbar=obj_grandactor(self,(640,360))
        self.villainhealthbar=obj_grandactor(self,(640,360))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_donewin=obj_grandactor(self,(640,360))
        self.text_donelost=obj_grandactor(self,(640,360))
        self.text_undone.show=True
        self.text_donewin.show=False
        self.text_donelost.show=False
        self.text_start=obj_grandactor(self,(640,360))# text message at start
        self.text_start.show=True

        # background
        # self.staticactor.addpart( "img1", draw.obj_image('moon',(98,258),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.staticactor.addpart( "img3", draw.obj_image('cloud',(1199,234),scale=0.35,rotate=0,fliph=True,flipv=False) )
        # self.staticactor.addpart( "img4", draw.obj_image('cloud',(1209,647),scale=0.29,rotate=0,fliph=False,flipv=False) )
        #
        # tune difficult
        prompt_dt=30# between 0 and 79, increment from base difficulty# (50 was too hard for non-gamers, 30 seems ok)
        prompt_time=80-prompt_dt# time to react to prompt (reference=80 but kinda easy)
        self.prompt_frame=prompt_dt#None# rewind prompt circle animation to given frame <84(higher frame for faster prompt time)
        promptcircle_scale=1# scaling factor for the vanishing circle: if shorter prompt time, make it smaller (keep ref=1)
        promptarrows_scale=1# or make the arrows larger too if prompt time shorter (keep ref=1)

        y1=140#80# for text
        y1font='huge'# large
        dx1=0# text horizontal spacing
        y2=300# for the prompts
        y4=140#80# end game messages
        ###################
        # prompt phase
        self.promptactor.addpart( 'hero', draw.obj_image('heromechbase',(640-330,470),scale=0.75) )
        self.promptactor.addpart( 'villain',draw.obj_image('villainmechbase',(640+330,470),scale=0.75) )
        self.promptactor.addpart( 'prompt', draw.obj_textbox(' ',(640,y2),fontsize='large') )# put nothing
        # self.promptactor.addpart( 'prompt_w', draw.obj_textbox('U',(640,y2),fontsize='huge',color=share.colors.black) )
        # self.promptactor.addpart( 'prompt_s', draw.obj_textbox('D',(640,y2),fontsize='huge',color=share.colors.black) )
        # self.promptactor.addpart( 'prompt_a', draw.obj_textbox('L',(640,y2),fontsize='huge',color=share.colors.black) )
        # self.promptactor.addpart( 'prompt_d', draw.obj_textbox('R',(640,y2),fontsize='huge',color=share.colors.black) )
        self.promptactor.addpart( 'prompt_w', draw.obj_image('arrowpurple',(640,y2),path='data/premade',scale=promptarrows_scale) )
        self.promptactor.addpart( 'prompt_s', draw.obj_image('arrowpurple',(640,y2),path='data/premade',scale=promptarrows_scale,flipv=True) )
        self.promptactor.addpart( 'prompt_a', draw.obj_image('arrowpurple',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90) )
        self.promptactor.addpart( 'prompt_d', draw.obj_image('arrowpurple',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90,fliph=True) )
        animation1=draw.obj_animation('mechfight_circleskrink','mechfightcircle',(640,360-160+y2-200),path='data/premade',imgscale=promptcircle_scale)
        self.promptactor.addpart( 'shrink', animation1 )
        # self.promptactor.addpart( 'prompt', draw.obj_textbox('Prompt',(640,200),fontsize='huge',color=share.colors.red) )
        self.promptactor.dict['hero'].show=True
        self.promptactor.dict['villain'].show=True
        self.promptactor.dict['prompt'].show=self.doprompt
        self.promptactor.dict['shrink'].show=self.doprompt
        self.promptactor.dict['shrink'].rewind(self.prompt_frame)
        self.whichprompt=tool.randint(0,3)
        self.promptactor.dict['prompt_w'].show=self.whichprompt==0 and self.doprompt
        self.promptactor.dict['prompt_s'].show=self.whichprompt==1 and self.doprompt
        self.promptactor.dict['prompt_a'].show=self.whichprompt==2 and self.doprompt
        self.promptactor.dict['prompt_d'].show=self.whichprompt==3 and self.doprompt
        self.promptinput=False# an input has been entered for prompt
        self.promptmatch=False# the current prompt was matched
        self.promptphase=True# are we in countdown or action phase
        self.prompttimer=tool.obj_timer(prompt_time)# countdown time
        self.prompttimer.start()
        #
        #################
        # action phase
        animation1=draw.obj_animation('mechfight_heropunches1','heromechbase',(640,360))
        animation1.addimage('heromechpunch')
        self.actionactor.addpart('heropunch',animation1)
        animation1=draw.obj_animation('mechfight_villainpunches1','villainmechbase',(640,360))
        animation1.addimage('villainmechpunch')
        self.actionactor.addpart('villainpunch',animation1)
        animation1=draw.obj_animation('mechfight_heroblocks','heromechbase',(640,360))
        animation1.addimage('heromechblock')
        self.actionactor.addpart('heroblock',animation1)
        animation1=draw.obj_animation('mechfight_villainblocks','villainmechbase',(640,360))
        animation1.addimage('villainmechblock')
        self.actionactor.addpart('villainblock',animation1)
        #
        animation1=draw.obj_animation('mechfight_villainpunches2','heromechbase',(640,360))
        if not self.dotutorial:
            animation1.addimage('heromechhit')
            animation1.addsound( "mech_stomp", [10,105] )
            animation1.addsound( "mech_contact", [55] )
            animation1.addsound( "mech_hit", [55] )
        self.actionactor.addpart('herohit',animation1)
        #
        animation1=draw.obj_animation('mechfight_heropunches2','villainmechbase',(640,360))
        if not self.dotutorial:
            animation1.addimage('villainmechhit')
            animation1.addsound( "mech_stomp", [10,108] )
            animation1.addsound( "mech_contact", [58] )
            animation1.addsound( "mech_strike", [58] )
        self.actionactor.addpart('villainhit',animation1)
        #
        animation1=draw.obj_animation('mechfight_herocountered','heromechbase',(640,360))
        if not self.dotutorial:
            animation1.addimage('heromechpunch')
            animation1.addimage('heromechhit')
            animation1.addsound( "mech_stomp", [10,88] )
            animation1.addsound( "mech_counter", [38] )
            animation1.addsound( "mech_hit", [38] )
        self.actionactor.addpart('herocountered',animation1)
        #
        animation1=draw.obj_animation('mechfight_villaincountered','villainmechbase',(640,360))
        if not self.dotutorial:
            animation1.addimage('villainmechpunch')
            animation1.addimage('villainmechhit')
            animation1.addsound( "mech_stomp", [10,90] )
            animation1.addsound( "mech_counter", [40] )
            animation1.addsound( "mech_strike", [40] )
        self.actionactor.addpart('villaincountered',animation1)
        #
        if not self.dotutorial:
            self.actionactor.addpart('heroattacks_text', draw.obj_textbox('super-mech-hero hits',(640-dx1,y1),fontsize=y1font,color=share.colors.darkgreen) )
            self.actionactor.addpart('heroblocks_text', draw.obj_textbox('super-mech-hero counters',(640-dx1,y1),fontsize=y1font,color=share.colors.darkgreen) )
            self.actionactor.addpart('villainattacks_text', draw.obj_textbox('super-mech-villain hits',(640+dx1,y1),fontsize=y1font,color=share.colors.red) )
            self.actionactor.addpart('villainblocks_text', draw.obj_textbox('super-mech-villain counters',(640+dx1,y1),fontsize=y1font,color=share.colors.red) )
        else:
            self.actionactor.addpart('heroattacks_text', draw.obj_textbox(' ',(640-dx1,y1),fontsize=y1font,color=share.colors.darkgreen) )
            self.actionactor.addpart('heroblocks_text', draw.obj_textbox(' ',(640-dx1,y1),fontsize=y1font,color=share.colors.darkgreen) )
            self.actionactor.addpart('villainattacks_text', draw.obj_textbox(' ',(640+dx1,y1),fontsize=y1font,color=share.colors.red) )
            self.actionactor.addpart('villainblocks_text', draw.obj_textbox(' ',(640+dx1,y1),fontsize=y1font,color=share.colors.red) )
        # self.actionactor.addpart( 'prompt_wfail', draw.obj_textbox('U',(640,y2),fontsize='huge',color=share.colors.red) )
        # self.actionactor.addpart( 'prompt_sfail', draw.obj_textbox('D',(640,y2),fontsize='huge',color=share.colors.red) )
        # self.actionactor.addpart( 'prompt_afail', draw.obj_textbox('L',(640,y2),fontsize='huge',color=share.colors.red) )
        # self.actionactor.addpart( 'prompt_dfail', draw.obj_textbox('R',(640,y2),fontsize='huge',color=share.colors.red) )
        # self.actionactor.addpart( 'prompt_wwin', draw.obj_textbox('U',(640,y2),fontsize='huge',color=share.colors.darkgreen) )
        # self.actionactor.addpart( 'prompt_swin', draw.obj_textbox('D',(640,y2),fontsize='huge',color=share.colors.darkgreen) )
        # self.actionactor.addpart( 'prompt_awin', draw.obj_textbox('L',(640,y2),fontsize='huge',color=share.colors.darkgreen) )
        # self.actionactor.addpart( 'prompt_dwin', draw.obj_textbox('R',(640,y2),fontsize='huge',color=share.colors.darkgreen) )
        self.actionactor.addpart( 'prompt_wfail', draw.obj_image('arrowred',(640,y2),path='data/premade',scale=promptarrows_scale) )
        self.actionactor.addpart( 'prompt_sfail', draw.obj_image('arrowred',(640,y2),path='data/premade',scale=promptarrows_scale,flipv=True) )
        self.actionactor.addpart( 'prompt_afail', draw.obj_image('arrowred',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90) )
        self.actionactor.addpart( 'prompt_dfail', draw.obj_image('arrowred',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90,fliph=True) )
        self.actionactor.addpart( 'prompt_wwin', draw.obj_image('arrowdarkgreen',(640,y2),path='data/premade',scale=promptarrows_scale) )
        self.actionactor.addpart( 'prompt_swin', draw.obj_image('arrowdarkgreen',(640,y2),path='data/premade',scale=promptarrows_scale,flipv=True) )
        self.actionactor.addpart( 'prompt_awin', draw.obj_image('arrowdarkgreen',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90) )
        self.actionactor.addpart( 'prompt_dwin', draw.obj_image('arrowdarkgreen',(640,y2),path='data/premade',scale=promptarrows_scale,rotate=90,fliph=True) )
        self.actionactor.addpart( 'cross',draw.obj_image('largecrossblack',(640,y2),path='data/premade',scale=0.5*promptarrows_scale) )
        #
        self.actionactor.dict['heropunch'].show=False
        self.actionactor.dict['villainpunch'].show=False
        self.actionactor.dict['heroblock'].show=False
        self.actionactor.dict['villainblock'].show=False
        self.actionactor.dict['herohit'].show=False
        self.actionactor.dict['villainhit'].show=False
        self.actionactor.dict['herocountered'].show=False
        self.actionactor.dict['villaincountered'].show=False
        self.actionactor.dict['heroattacks_text'].show=False
        self.actionactor.dict['heroblocks_text'].show=False
        self.actionactor.dict['villainattacks_text'].show=False
        self.actionactor.dict['villainblocks_text'].show=False
        self.actionactor.dict['cross'].show=False
        self.actionactor.dict['prompt_wfail'].show=False
        self.actionactor.dict['prompt_sfail'].show=False
        self.actionactor.dict['prompt_afail'].show=False
        self.actionactor.dict['prompt_dfail'].show=False
        self.actionactor.dict['prompt_wwin'].show=False
        self.actionactor.dict['prompt_swin'].show=False
        self.actionactor.dict['prompt_awin'].show=False
        self.actionactor.dict['prompt_dwin'].show=False
        self.actionstate=0# 0,1,2,3 for hero hits, villain hits, hero blocks, villain blocks
        self.actiontimer=tool.obj_timer(150)# action time ( but can be shorter)
        self.actiontimer.start()
        #
        # healthbar hero
        self.maxherohealth=5# starting hero health (reference=always 3)
        self.herohealth=self.maxherohealth# updated one
        self.maxvillainhealth=9# starting villain health
        self.villainhealth=self.maxvillainhealth# updated one

        # health bar hero
        if self.dotutorial:
            self.ybar=150# for health bars and text
        else:
            self.ybar=50
        self.herohealthbar.addpart('face', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.maxherohealth):
            self.herohealthbar.addpart('heart_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )
            self.herohealthbar.addpart('heartcross_'+str(i), draw.obj_image('smallcrossred',(150+i*75,self.ybar),scale=0.75,path='data/premade') )
            self.herohealthbar.dict['heartcross_'+str(i)].show=False
        self.villainhealthbar.addpart('face', draw.obj_image('villainhead',(1280-50,self.ybar),scale=0.2,fliph=True) )
        for i in range(self.maxvillainhealth):
            self.villainhealthbar.addpart('heart_'+str(i), draw.obj_image('lightningbolt',(1280-130-i*70,self.ybar),scale=0.2) )
            self.villainhealthbar.addpart('heartcross_'+str(i), draw.obj_image('smallcrossred',(1280-130-i*70,self.ybar),scale=0.75,path='data/premade') )
            self.villainhealthbar.dict['heartcross_'+str(i)].show=False
        self.herohealthbar.show=self.dohealth
        self.villainhealthbar.show=self.dohealth
        # text for winning
        # self.text_undone.addpart( 'text1', draw.obj_textbox('Match the prompts',(640,680),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('super-mech-villain destroyed',(640,y4),fontsize='huge',color=share.colors.darkgreen) )
        self.text_donewin.addpart( 'cloud1', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(816,386)) )
        self.text_donewin.addpart( 'cloud2', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(1018,268)) )
        self.text_donewin.addpart( 'cloud3', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(1188,330)) )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('super-mech-hero destroyed',(640,y4),fontsize='huge',color=share.colors.red) )
        self.text_donelost.addpart( 'cloud1', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(416,318)) )
        self.text_donelost.addpart( 'cloud2', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(254,266)) )
        self.text_donelost.addpart( 'cloud3', draw.obj_animation('mechfight_villaindies_cloud1','cloud',(93,385)) )
        self.text_donewin.addpart( 'villaindies', draw.obj_animation('mechfight_villaindies','villainmechbase_noface',(640,360)) )
        self.text_donewin.addpart( 'herostands',draw.obj_image('heromechbase',(640-330,470),scale=0.75) )
        self.text_donelost.addpart( 'herodies', draw.obj_animation('mechfight_herodies','heromechbase_noface',(640,360)) )
        self.text_donelost.addpart( 'villainstands',draw.obj_image('villainmechbase',(640+330,470),scale=0.75) )
        # fight message at beginning
        self.timerfightmessage=tool.obj_timer(80)
        if not self.dotutorial:
            self.text_start.addpart( 'fightmessage', draw.obj_animation('dodgebullets_fightmessage','messagefight',(640,360), path='data/premade') )
            self.timerfightmessage.start()
        # timer for done part
        self.timerendwin=tool.obj_timer(220)# goal to done
        self.timerendloose=tool.obj_timer(240)# goal to done
        # audio
        self.soundcorrect=draw.obj_sound('mech_correct')
        self.creator.addpart(self.soundcorrect)
        self.soundwrong=draw.obj_sound('mech_wrong')
        self.creator.addpart(self.soundwrong)
        # self.soundstomp=draw.obj_sound('mech_stomp')# added directly to animations
        # self.creator.addpart(self.soundstomp)
        # self.soundcontact=draw.obj_sound('mech_contact')
        # self.creator.addpart(self.soundcontact)
        # self.soundcounter=draw.obj_sound('mech_counter')
        # self.creator.addpart(self.soundcontact)
        # self.soundhit=draw.obj_sound('mech_hit')
        # self.creator.addpart(self.soundhit)
        # self.soundstrike=draw.obj_sound('mech_strike')
        # self.creator.addpart(self.soundstrike)
        self.soundwin=draw.obj_sound('mech_win')
        self.creator.addpart(self.soundwin)
        self.sounddie=draw.obj_sound('mech_die')
        self.creator.addpart(self.sounddie)
        #
        if not self.dotutorial:
            self.soundstart=draw.obj_sound('mech_start')
            self.soundstart.play()# at start
        #
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # fight message at beginning
            if self.timerfightmessage.on:
                self.timerfightmessage.update()
                if self.timerfightmessage.ring:
                    self.text_start.show=False
            #
            if self.promptphase:
                self.prompttimer.update()
                #
                if self.doprompt:# only if prompt on
                    # Reflex : match correct input here
                    if self.whichprompt==0:# press w
                        if not self.promptinput:
                            if controls.gu and controls.guc:
                                self.promptmatch=True# won
                                self.promptinput=True
                                self.actionactor.dict['prompt_wwin'].show=True
                                self.promptactor.dict['prompt_w'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                            elif (controls.gd and controls.gdc) or (controls.gl and controls.glc) or (controls.gr and controls.grc):
                                self.promptmatch=False# lost
                                self.promptinput=True
                                self.actionactor.dict['prompt_wfail'].show=True
                                self.actionactor.dict['cross'].show=True
                                self.promptactor.dict['prompt_w'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                    elif self.whichprompt==1:# press s
                        if not self.promptinput:
                            if controls.gd and controls.gdc:
                                self.promptmatch=True# won
                                self.promptinput=True
                                self.actionactor.dict['prompt_swin'].show=True
                                self.promptactor.dict['prompt_s'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                            elif (controls.gu and controls.guc) or (controls.gl and controls.glc) or (controls.gr and controls.grc):
                                self.promptmatch=False# lost
                                self.promptinput=True
                                self.actionactor.dict['prompt_sfail'].show=True
                                self.actionactor.dict['cross'].show=True
                                self.promptactor.dict['prompt_s'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                    elif self.whichprompt==2:# press a
                        if not self.promptinput:
                            if controls.gl and controls.glc:
                                self.promptmatch=True# won
                                self.promptinput=True
                                self.actionactor.dict['prompt_awin'].show=True
                                self.promptactor.dict['prompt_a'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                            elif (controls.gu and controls.guc) or (controls.gd and controls.gdc) or (controls.gr and controls.grc):
                                self.promptmatch=False# lost
                                self.promptinput=True
                                self.actionactor.dict['prompt_afail'].show=True
                                self.actionactor.dict['cross'].show=True
                                self.promptactor.dict['prompt_a'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                    elif self.whichprompt==3:# press d
                        if not self.promptinput:
                            if controls.gr and controls.grc:
                                self.promptmatch=True# won
                                self.promptinput=True
                                self.actionactor.dict['prompt_dwin'].show=True
                                self.promptactor.dict['prompt_d'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                            elif (controls.gu and controls.guc) or (controls.gd and controls.gdc) or (controls.gl and controls.glc):
                                self.promptmatch=False# lost
                                self.promptinput=True
                                self.actionactor.dict['prompt_dfail'].show=True
                                self.actionactor.dict['cross'].show=True
                                self.promptactor.dict['prompt_d'].show=False
                                self.prompttimer.forcering()
                                self.promptactor.dict['shrink'].pause()
                #
                # end of countdown
                if self.prompttimer.ring:# flip to action
                    if not self.doprompt:# no prompt, random outcome
                        self.promptmatch=tool.randbool()
                    else:
                        # check if prompt was matched
                        if not self.promptinput: # no input was given=fail
                            self.promptmatch=False
                            self.actionactor.dict['cross'].show=self.doprompt
                            self.promptactor.dict['shrink'].pause()
                            if self.whichprompt==0:# press w
                                self.actionactor.dict['prompt_wfail'].show=self.doprompt
                            elif self.whichprompt==1:# press s
                                self.actionactor.dict['prompt_sfail'].show=self.doprompt
                            elif self.whichprompt==2:# press a
                                self.actionactor.dict['prompt_afail'].show=self.doprompt
                            elif self.whichprompt==3:# press d
                                self.actionactor.dict['prompt_dfail'].show=self.doprompt
                    # Action as result of prompt
                    if self.promptmatch:# won
                        if self.dotutorial:
                            self.actionstate=0# tutorial: hero always punch
                        else:
                            self.actionstate=tool.randchoice([0,2])# hero punches villain, or hero blocks villain
                        if self.doprompt:
                            self.soundcorrect.play()
                    else:# lost
                        if self.dotutorial:
                            self.actionstate=1# tutorial: hero gets hit (doesnt matter tho)
                        else:
                            self.actionstate=tool.randchoice([1,3])# villain punches hero, or villain blocks hero
                        if self.doprompt:
                            self.soundwrong.play()
                    # switch to action phase
                    self.promptphase=False
                    self.actiontimer.start()
                    self.promptactor.dict['hero'].show=False
                    self.promptactor.dict['villain'].show=False
                    self.promptactor.dict['prompt'].show=False
                    self.promptactor.dict['prompt_w'].show=False
                    self.promptactor.dict['prompt_a'].show=False
                    self.promptactor.dict['prompt_d'].show=False
                    self.promptactor.dict['prompt_s'].show=False
                    # play correct animation
                    if self.actionstate==0:# hero hits villain
                        self.actionactor.dict['heropunch'].show=True
                        self.actionactor.dict['villainhit'].show=True
                        self.actionactor.dict['heropunch'].rewind()
                        self.actionactor.dict['villainhit'].rewind()
                        self.actionactor.dict['heroattacks_text'].show=True
                    elif self.actionstate==1:# villain hits hero
                        self.actionactor.dict['villainpunch'].show=True
                        self.actionactor.dict['herohit'].show=True
                        self.actionactor.dict['villainpunch'].rewind()
                        self.actionactor.dict['herohit'].rewind()
                        self.actionactor.dict['villainattacks_text'].show=True
                    elif self.actionstate==2:# hero blocks villain
                        self.actionactor.dict['villaincountered'].show=True
                        self.actionactor.dict['heroblock'].show=True
                        self.actionactor.dict['villaincountered'].rewind()
                        self.actionactor.dict['heroblock'].rewind()
                        self.actionactor.dict['heroblocks_text'].show=True
                    if self.actionstate==3:# villain blocks hero
                        self.actionactor.dict['herocountered'].show=True
                        self.actionactor.dict['villainblock'].show=True
                        self.actionactor.dict['herocountered'].rewind()
                        self.actionactor.dict['villainblock'].rewind()
                        self.actionactor.dict['villainblocks_text'].show=True
                    # update health
                    if self.actionstate==0:# hero hits villain
                        if not self.dotutorial:
                            self.villainhealth -= 1
                        if self.villainhealth>=0 and self.villainhealth<self.maxvillainhealth:
                            self.villainhealthbar.dict['heartcross_'+str(self.villainhealth)].show=True
                    elif self.actionstate==1:# villain hits hero
                        if not self.dotutorial:
                            self.herohealth -= 1
                        if self.herohealth>=0 and self.herohealth<self.maxherohealth:
                            self.herohealthbar.dict['heartcross_'+str(self.herohealth)].show=True
                    elif self.actionstate==2:# hero blocks villain
                        if not self.dotutorial:
                            self.villainhealth -= 1
                        if self.villainhealth>=0 and self.villainhealth<self.maxvillainhealth:
                            self.villainhealthbar.dict['heartcross_'+str(self.villainhealth)].show=True
                    if self.actionstate==3:# villain blocks hero
                        if not self.dotutorial:
                            self.herohealth -= 1
                        if self.herohealth>=0 and self.herohealth<self.maxherohealth:
                            self.herohealthbar.dict['heartcross_'+str(self.herohealth)].show=True
            #
            else:# action phase
                self.actiontimer.update()
                if self.actiontimer.ring:# flip to countdown
                    self.promptphase=True
                    self.prompttimer.start()
                    self.promptactor.dict['hero'].show=True
                    self.promptactor.dict['villain'].show=True
                    self.promptactor.dict['prompt'].show=self.doprompt
                    self.promptactor.dict['shrink'].unpause()# unpause
                    self.promptactor.dict['shrink'].show=self.doprompt
                    self.promptactor.dict['shrink'].rewind(self.prompt_frame)
                    # random prompt
                    self.whichprompt=tool.randint(0,3)
                    self.promptactor.dict['prompt_w'].show=self.whichprompt==0 and self.doprompt
                    self.promptactor.dict['prompt_s'].show=self.whichprompt==1 and self.doprompt
                    self.promptactor.dict['prompt_a'].show=self.whichprompt==2 and self.doprompt
                    self.promptactor.dict['prompt_d'].show=self.whichprompt==3 and self.doprompt
                    self.promptmatch=False
                    self.promptinput=False
                    #
                    self.actionactor.dict['heropunch'].show=False
                    self.actionactor.dict['villainpunch'].show=False
                    self.actionactor.dict['heroblock'].show=False
                    self.actionactor.dict['villainblock'].show=False
                    self.actionactor.dict['herohit'].show=False
                    self.actionactor.dict['villainhit'].show=False
                    self.actionactor.dict['herocountered'].show=False
                    self.actionactor.dict['villaincountered'].show=False
                    self.actionactor.dict['heroattacks_text'].show=False
                    self.actionactor.dict['heroblocks_text'].show=False
                    self.actionactor.dict['villainattacks_text'].show=False
                    self.actionactor.dict['villainblocks_text'].show=False
                    self.actionactor.dict['prompt_wfail'].show=False
                    self.actionactor.dict['prompt_sfail'].show=False
                    self.actionactor.dict['prompt_afail'].show=False
                    self.actionactor.dict['prompt_dfail'].show=False
                    self.actionactor.dict['prompt_wwin'].show=False
                    self.actionactor.dict['prompt_swin'].show=False
                    self.actionactor.dict['prompt_awin'].show=False
                    self.actionactor.dict['prompt_dwin'].show=False
                    self.actionactor.dict['cross'].show=False
                    for i in range(self.maxherohealth):
                        self.herohealthbar.dict['heartcross_'+str(i)].show=False
                    for i in range(self.maxvillainhealth):
                        self.villainhealthbar.dict['heartcross_'+str(i)].show=False

                    # hero check health
                    if self.herohealth>0:
                        if self.herohealth<self.maxherohealth:
                            self.herohealthbar.dict['heart_'+str(self.herohealth)].show=False
                    else:# dead=hero lost
                        self.goal=True
                        self.win=False
                        self.timerendloose.start()
                        self.sounddie.play()
                        self.text_undone.show=False
                        self.text_donelost.show=True
                        self.promptactor.dict['hero'].show=False
                        self.promptactor.dict['villain'].show=False
                        self.promptactor.dict['prompt'].show=False
                        self.promptactor.dict['shrink'].show=False
                        self.promptactor.dict['prompt_w'].show=False
                        self.promptactor.dict['prompt_s'].show=False
                        self.promptactor.dict['prompt_a'].show=False
                        self.promptactor.dict['prompt_d'].show=False
                        if self.herohealth<self.maxherohealth:
                            self.herohealthbar.dict['heart_'+str(self.herohealth)].show=False

                    # villain check health
                    if self.villainhealth>0:
                        if self.villainhealth<self.maxvillainhealth:
                            self.villainhealthbar.dict['heart_'+str(self.villainhealth)].show=False
                    else:# dead=hero won
                        self.goal=True
                        self.win=True
                        self.timerendwin.start()
                        self.soundwin.play()
                        self.text_undone.show=False
                        self.text_donewin.show=True
                        self.promptactor.dict['hero'].show=False
                        self.promptactor.dict['villain'].show=False
                        self.promptactor.dict['prompt'].show=False
                        self.promptactor.dict['shrink'].show=False
                        self.promptactor.dict['prompt_w'].show=False
                        self.promptactor.dict['prompt_s'].show=False
                        self.promptactor.dict['prompt_a'].show=False
                        self.promptactor.dict['prompt_d'].show=False
                        if self.villainhealth<self.maxvillainhealth:
                            self.villainhealthbar.dict['heart_'+str(self.villainhealth)].show=False

        else:
            # goal reached state
            if self.win:# won minigame
                self.timerendwin.update()
                if self.timerendwin.ring:
                    self.done=True# end of minigame
            else:# lost minigame
                self.timerendloose.update()
                if self.timerendloose.ring:
                    self.done=True# end of minigame


####################################################################################################################


# Mini Game: play a serenade
# *SERENADE
class obj_world_serenade(obj_world):
    def setup(self,**kwargs):
        # default options
        self.addpartner=True# add the partnercd
        self.heroangry=False# hero is angry (and alone)
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# partner options
            if 'heroangry' in kwargs: self.heroangry=kwargs["heroangry"]# partner options
        #
        self.done=False# mini game is finished
        self.doneplaying=False# done playing serenade
        # hero on left
        self.hero=obj_grandactor(self,(640,360))
        if self.heroangry:
            self.hero.addpart( 'img_hero',draw.obj_image('herobaseangry',(140+20,470), scale=0.7) )# bit messy
        else:
            self.hero.addpart( 'img_hero',draw.obj_image('herobase',(140+20,470), scale=0.7) )# bit messy
        self.hero.addpart( 'img_instru',draw.obj_image('saxophone',(270+20,470),scale=0.5) )

        # partner on right
        self.partner=obj_grandactor(self,(640,360))
        if self.addpartner:
            self.partner.addpart( 'img_partner',draw.obj_image('partnerbase',(1280-200,450), scale=0.7,fliph=True) )
        # melody score
        if True:
            self.score=obj_grandactor(self,(640,380))
            self.score.addpart( 'img',draw.obj_image('musicscore',(640,380),path='data/premade') )
        ### melody to reproduce
        self.melody=obj_grandactor(self,(640,360))
        self.melody.melodylength=9#8# number of notes to play
        melodyx=[-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5,4.5]# x positions (scaled)
        melodydx=50# x-spacing notes
        melodydy=30#y-spacing notes
        self.melody.melodynotes=[]
        for i in range(self.melody.melodylength):
            inote=tool.randint(1,4)
            if inote==1:
                note='U'
                ynote=1.5
            elif inote==2:
                note='L'
                ynote=-0.5
            elif inote==3:
                note='D'
                ynote=-1.5
            elif inote==4:
                note='R'
                ynote=0.5
            self.melody.melodynotes.append(note)
            position=(640-15+melodyx[i]*melodydx,380-ynote*melodydy)
            self.melody.addpart("imgnotebase_"+str(i), draw.obj_image('musicnotesquare',position,path='data/premade') )
            self.melody.addpart("imgnoteplay_"+str(i), draw.obj_image('musicnotesquare_played',position,path='data/premade') )
            self.melody.dict["imgnoteplay_"+str(i)].show=False
            # self.melody.addpart("textboxnote_"+str(i), draw.obj_textbox(note,position) )
            if note=='U':
                self.melody.addpart("textboxnote_"+str(i), draw.obj_image('arrow',position,path='data/premade',scale=0.35) )
            elif note=='D':
                self.melody.addpart("textboxnote_"+str(i), draw.obj_image('arrow',position,path='data/premade',scale=0.35,flipv=True) )
            elif note=='L':
                self.melody.addpart("textboxnote_"+str(i), draw.obj_image('arrow',position,path='data/premade',scale=0.35,rotate=90) )
            elif note=='R':
                self.melody.addpart("textboxnote_"+str(i), draw.obj_image('arrow',position,path='data/premade',scale=0.35,rotate=90,fliph=True) )

        self.melody.melodyi=0# index of completed note (must reach melodylength)
        # floating notes
        self.floatingnotes=obj_grandactor(self,(640,360))
        self.floatingnotes.addpart('anim1', draw.obj_animation('ch2_musicnote1','musicnote',(640,500),scale=0.3))
        self.floatingnotes.addpart('anim2',draw.obj_animation('ch2_musicnote1','musicnote',(480,500),scale=0.3))
        self.floatingnotes.addpart('anim3',draw.obj_animation('ch2_musicnote1','musicnote',(800,500),scale=0.3))
        self.floatingnotes.addpart('anim4',draw.obj_animation('ch2_musicnote1','musicnote',(640,180),scale=0.3))
        self.floatingnotes.addpart('anim5',draw.obj_animation('ch2_musicnote1','musicnote',(480,180),scale=0.3))
        self.floatingnotes.addpart('anim6',draw.obj_animation('ch2_musicnote1','musicnote',(800,180),scale=0.3))
        # floating hearts
        self.floatinglove=obj_grandactor(self,(640,360))
        self.floatinglove.addpart('anim1', draw.obj_animation('ch2_musicnote1','love',(640,500),scale=0.3))
        self.floatinglove.addpart('anim2',draw.obj_animation('ch2_musicnote1','love',(480,500),scale=0.3))
        self.floatinglove.addpart('anim3',draw.obj_animation('ch2_musicnote1','love',(800,500),scale=0.3))
        self.floatinglove.addpart('anim4',draw.obj_animation('ch2_musicnote1','love',(640,180),scale=0.3))
        self.floatinglove.addpart('anim5',draw.obj_animation('ch2_musicnote1','love',(480,180),scale=0.3))
        self.floatinglove.addpart('anim6',draw.obj_animation('ch2_musicnote1','love',(800,180),scale=0.3))
        self.floatingnotes.show=True
        self.floatinglove.show=False
        # textbox under
        self.text1=obj_grandactor(self,(640,360))
        self.text1.addpart( 'textbox1',draw.obj_textbox('play melody with ['+share.datamanager.controlname('arrows')+']',(640,660),color=share.colors.instructions) )
        self.text2=obj_grandactor(self,(640,360))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Beautiful!',(640,660)) )
        self.text1.show=True
        self.text2.show=False
        # short timer after done playing
        self.timerend=tool.obj_timer(130)
        #
        self.soundnoted=draw.obj_sound('noted')
        self.creator.addpart(self.soundnoted)
        self.soundnotel=draw.obj_sound('notel')
        self.creator.addpart(self.soundnotel)
        self.soundnoter=draw.obj_sound('noter')
        self.creator.addpart(self.soundnoter)
        self.soundnoteu=draw.obj_sound('noteu')
        self.creator.addpart(self.soundnoteu)
        if self.heroangry:
            self.soundcheer=draw.obj_sound('serenade_cheeralone')
            self.creator.addpart(self.soundcheer)
        else:
            self.soundcheer=draw.obj_sound('serenade_cheer')
            self.creator.addpart(self.soundcheer)
        #
        # ambience sounds (add to page!)
        self.soundambience=draw.obj_sound('serenade_ambience')
        self.creator.addpart(self.soundambience)
        self.soundambience.play(loop=True)# should die when exit page



    def update(self,controls):
        super().update(controls)
        if not self.doneplaying:
            # current note played
            if controls.gu and controls.guc:
                playednote='U'
            elif controls.gl and controls.glc:
                playednote='L'
            elif controls.gd and controls.gdc:
                playednote='D'
            elif controls.gr and controls.grc:
                playednote='R'
            else:
                playednote=False
            # current melody
            cnote=self.melody.melodynotes[self.melody.melodyi]# current note to play
            if playednote==cnote:
                self.melody.dict["imgnotebase_"+str(self.melody.melodyi)].show=False
                self.melody.dict["imgnoteplay_"+str(self.melody.melodyi)].show=True
                self.melody.melodyi += 1
                if self.melody.melodyi > self.melody.melodylength-1:# completed melody
                    self.doneplaying=True
                    self.timerend.start()
                    self.soundcheer.play()
                if playednote=='U':
                    self.soundnoteu.play()
                elif playednote=='L':
                    self.soundnotel.play()
                elif playednote=='D':
                    self.soundnoted.play()
                elif playednote=='R':
                    self.soundnoter.play()

        else:# done playing
            self.text1.show=False
            self.text2.show=True
            self.floatingnotes.show=False
            self.floatinglove.show=True
            self.timerend.update()
            if self.timerend.ring:
                self.done=True


####################################################################################################################

# Mini Game: kiss
# *KISSING
class obj_world_kiss(obj_world):
    def setup(self,**kwargs):
        # default options
        self.noending=True# skip the completion part of minigame
        # scene tuning
        if kwargs is not None:
            if 'noending' in kwargs: self.noending=kwargs["noending"]
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.ungoing=False# ungoing or back to start
        # layering
        self.staticactor=obj_grandactor(self,(640,360))
        self.startactor=obj_grandactor(self,(640,360))
        self.ungoingactor=obj_grandactor(self,(640,360))
        self.finishactor=obj_grandactor(self,(640,360))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.staticactor.show=True
        self.startactor.show=True
        self.ungoingactor.show=False
        self.finishactor.show=False
        self.text_undone.show=True
        self.text_done.show=False
        # static actor
        # self.staticactor.addpart( 'img1',   )
        # start actor
        self.startactor.addpart( 'img1', draw.obj_image('herobase',(240,400),scale=0.7) )
        self.startactor.addpart( 'img2', draw.obj_image('partnerbase',(1040,400),fliph=True,scale=0.7) )
        # ungoing actor
        self.ungoingactor.addpart( 'anim2', draw.obj_animation('ch2_kiss2','partnerbase',(640,360)) )# partner first (background)
        self.animation=draw.obj_animation('ch2_kiss1','herobase',(640,360))
        self.ungoingactor.addpart( 'anim1', self.animation )
        self.animation.addsound('kiss_kiss',100)
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('partnerbase',(710,390),scale=0.7,rotate=15) )
        self.finishactor.addpart( 'img2', draw.obj_image('herobase',(580,400),scale=0.7,rotate=-15) )
        self.finishactor.addpart( 'anim1', draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4) )
        self.finishactor.addpart( 'anim2', draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4) )

        # text
        self.textboxclick=draw.obj_textbox(\
        'Hold ['+share.datamanager.controlname('left')\
        +']+['+share.datamanager.controlname('right')+'] to kiss',\
        (640,660),color=share.colors.instructions,hover=True)
        self.text_undone.addpart( 'text1', self.textboxclick )
        self.text_done.addpart( 'text1', draw.obj_textbox('So Much Tongue!',(640,660)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(180)# ungoing part
        self.timerend=tool.obj_timer(130)# goal to done
        self.timer.start()# reset ungoing timer
        #
        self.soundstart=draw.obj_sound('kiss_start')
        self.creator.addpart(self.soundstart)
        self.soundend=draw.obj_sound('kiss_cheer')
        self.creator.addpart(self.soundend)
        self.soundend2=draw.obj_sound('kiss_cheer2')
        self.creator.addpart(self.soundend2)

    def triggerungoing(self,controls):
        return ( (controls.gl and controls.gr) and (controls.glc or controls.grc) ) or (True and self.textboxclick.isclicked(controls))
    def triggerstart(self,controls):
        return not (controls.gl and controls.gr) and not self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.goal:
            # goal unreached state
            if not self.ungoing:
                # start substate
                if self.triggerungoing(controls):# flip to ungoing
                    self.ungoing=True
                    self.startactor.show=False
                    self.ungoingactor.show=True
                    self.finishactor.show=False
                    self.timer.start()# reset ungoing timer
                    self.ungoingactor.dict["anim1"].rewind()
                    self.ungoingactor.dict["anim2"].rewind()
                    self.soundstart.play()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                if self.timer.ring:# flip to goal reached
                    if self.noending:
                        self.goal=True
                        self.done=True
                    else:
                        self.goal=True
                        self.startactor.show=False
                        self.ungoingactor.show=False
                        self.finishactor.show=True
                        self.text_undone.show=False
                        self.text_done.show=True
                        self.timerend.start()
                        self.soundend.play()
                        self.soundend2.play()

        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: sunrise
# *SUNSET *NIGHTFALL
class obj_world_sunset(obj_world):
    def setup(self,**kwargs):
        # default options
        self.landtype='home'# default land type is hero home
        # scene tuning
        if kwargs is not None:
            if 'type' in kwargs: self.landtype=kwargs["type"]
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.ungoing=False# ungoing or back to start
        # layering
        self.startactor=obj_grandactor(self,(640,360))
        self.ungoingactor=obj_grandactor(self,(640,360))
        self.finishactor=obj_grandactor(self,(640,360))
        self.staticactor=obj_grandactor(self,(640,360))# static in front here
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.staticactor.show=True
        self.startactor.show=True
        self.ungoingactor.show=False
        self.finishactor.show=False
        self.text_undone.show=True
        self.text_done.show=False

        # static actor
        if self.landtype=='island':
            self.staticactor.addpart( 'imgref1', draw.obj_image('horizon',(640,720-150),path='data/premade') )
            self.staticactor.addpart( "img1", draw.obj_image('sailboat',(296,445),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img3", draw.obj_image('palmtree',(991,448),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img4", draw.obj_image('palmtree',(1105,506),scale=0.33,rotate=0,fliph=True,flipv=False) )
            self.staticactor.addpart( "img5", draw.obj_image('wave',(202,555),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img6", draw.obj_image('wave',(480,544),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img7", draw.obj_image('wave',(704,679),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img8", draw.obj_image('mountain',(671,438),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img9", draw.obj_image('islandsunset',(840,550),path='data/premade') )
            self.staticactor.addpart( "img2", draw.obj_image('skeletonhead',(837,456),scale=0.35,rotate=0,fliph=False,flipv=False) )
        else:
            self.staticactor.addpart( "img3", draw.obj_image('flower',(102,440),scale=0.28,rotate=0,fliph=True,flipv=False) )
            self.staticactor.addpart( 'imgref1', draw.obj_image('horizon',(640,720-150),path='data/premade') )
            self.staticactor.addpart( 'imgref2', draw.obj_image('house',(296,443),scale=0.5) )
            self.staticactor.addpart( "imgref3", draw.obj_image('pond',(650,611),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img1", draw.obj_image('bush',(827,452),scale=0.32,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img2", draw.obj_image('bush',(486,648),scale=0.32,rotate=0,fliph=True,flipv=False) )
            self.staticactor.addpart( "img4", draw.obj_image('flower',(186,615),scale=0.28,rotate=0,fliph=False,flipv=False) )
            self.staticactor.addpart( "img5", draw.obj_image('flower',(101,567),scale=0.28,rotate=0,fliph=True,flipv=False) )
        #
        # start actor
        self.startactor.addpart( 'img1', draw.obj_image('sun',(660,270),scale=0.5) )
        # ungoing actor
        animation1=draw.obj_animation('ch2_sunset','sun',(640,360))
        animation1.addimage('moon')
        self.ungoingactor.addpart( 'anim1', animation1 )
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('moon',(660,270),scale=0.5) )

        # text
        self.textboxclick=draw.obj_textbox('Hold ['+share.datamanager.controlname('down')\
        +'] to lower the sun',(1000,620),color=share.colors.instructions,hover=True)
        self.text_undone.addpart( 'text1', self.textboxclick )
        self.text_done.addpart( 'text1', draw.obj_textbox('Nighty Night!',(1000,620)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(80)# ungoing part
        self.timerend=tool.obj_timer(120)# goal to done
        self.timer.start()# reset ungoing timer
        #
        self.soundstart=draw.obj_sound('sunset_start')
        self.creator.addpart(self.soundstart)
        self.soundend=draw.obj_sound('sunset_end')
        self.creator.addpart(self.soundend)
        #
    def triggerungoing(self,controls):
        return controls.gd and controls.gdc or (True and self.textboxclick.isclicked(controls))
    def triggerstart(self,controls):
        return not controls.gd and not self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.goal:
            # goal unreached state
            if not self.ungoing:
                # start substate
                if self.triggerungoing(controls):# flip to ungoing
                    self.soundstart.play()
                    self.ungoing=True
                    self.startactor.show=False
                    self.ungoingactor.show=True
                    self.finishactor.show=False
                    self.timer.start()# reset ungoing timer
                    self.ungoingactor.dict["anim1"].rewind()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                if self.timer.ring:# flip to goal reached
                    self.goal=True
                    self.startactor.show=False
                    self.ungoingactor.show=False
                    self.finishactor.show=True
                    self.text_undone.show=False
                    self.text_done.show=True
                    self.timerend.start()
                    self.soundend.play()
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: go to bed
# *GOTOBED *BED *SLEEP
class obj_world_gotobed(obj_world):
    def setup(self,**kwargs):
        # default options
        self.addpartner=False
        self.addmoon=True# add the moon (must have been drawn)
        self.addsun=False# add the sun (must have been drawn)
        self.addalarmclock=False# add the alarm clock and night stand
        self.heroisangry=False# angry face on hero
        self.addbug=False# add bug alongside hero
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# partner options
            if 'bug' in kwargs: self.addbug=kwargs["bug"]# partner options
            if 'addmoon' in kwargs: self.addmoon=kwargs["addmoon"]#
            if 'addsun' in kwargs: self.addsun=kwargs["addsun"]#
            if 'alarmclock' in kwargs: self.addalarmclock=kwargs["alarmclock"]# partner options
            if 'heroangry' in kwargs: self.heroisangry=kwargs["heroangry"]# partner options
        #
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.ungoing=False# ungoing or back to start
        # layering
        self.staticactor=obj_grandactor(self,(640,360))
        self.startactor=obj_grandactor(self,(640,360))
        self.ungoingactor=obj_grandactor(self,(640,360))
        self.finishactor=obj_grandactor(self,(640,360))
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        self.staticactor.show=True
        self.startactor.show=True
        self.ungoingactor.show=False
        self.finishactor.show=False
        self.text_undone.show=True
        self.text_done.show=False
        # static actor
        self.staticactor.addpart( 'img1', draw.obj_image('bed',(440,500),scale=0.75)  )
        if self.addmoon:
            self.staticactor.addpart( 'annim',draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )
        if self.addsun:
            self.staticactor.addpart( 'annim',draw.obj_animation('ch1_sun','sun',(640,360),scale=0.5) )
        if self.addalarmclock:
            self.staticactor.addpart( 'img3',draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
            self.staticactor.addpart( 'img2',draw.obj_image('nightstand',(100,530),scale=0.5) )
        # start actor
        if self.addpartner:# add partner in love
            self.startactor.addpart( 'animadd1', draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )
        if self.heroisangry:
            self.startactor.addpart( 'anim1', draw.obj_animation('ch1_awaken','herobaseangry',(640,360),scale=0.7) )
        else:
            self.startactor.addpart( 'anim1', draw.obj_animation('ch1_awaken','herobase',(640,360),scale=0.7) )
        # ungoing actor
        if self.addpartner:
            self.ungoingactor.addpart( 'animadd1', draw.obj_animation('ch1_herotosleep','partnerbase',(640+100,360),scale=0.7) )
        if self.addbug:
            self.ungoingactor.addpart( 'animadd2', draw.obj_animation('ch1_herotosleepbug','bug',(640,360)) )
        if self.heroisangry:
            self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch1_herotosleep','herobaseangry',(640,360),scale=0.7) )
        else:
            self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch1_herotosleep','herobase',(640,360),scale=0.7) )
        # finish actor
        if self.addpartner:
            self.finishactor.addpart( 'imgadd1', draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        if self.heroisangry:
            self.finishactor.addpart( 'img1', draw.obj_image('herobaseangry',(420,490),scale=0.7,rotate=80) )
        else:
            self.finishactor.addpart( 'img1', draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.finishactor.addpart( 'anim1a', draw.obj_image('sleepZ',(700,400),path='data/premade'))
        self.finishactor.addpart( 'anim1b', draw.obj_image('sleepZ',(700+60,400-20),path='data/premade',scale=0.7))
        self.finishactor.addpart( 'anim1c', draw.obj_image('sleepZ',(700+100,400-30),path='data/premade',scale=0.5))

        # text
        self.textboxclick=draw.obj_textbox('hold ['+share.datamanager.controlname('left')+'] to go to sleep',(1100,480),color=share.colors.instructions,hover=True)
        self.text_undone.addpart( 'text1', self.textboxclick )
        self.text_done.addpart( 'text1', draw.obj_textbox('Sweet Dreams!',(1100,480)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(80)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
        self.timer.start()# reset ungoing timer
        # audio
        self.soundstart=draw.obj_sound('gotobed_start')
        self.creator.addpart(self.soundstart)
        self.sounddone=draw.obj_sound('gotobed_end')
        self.creator.addpart(self.sounddone)
        #
    def triggerungoing(self,controls):
        return controls.gl and controls.glc or (True and self.textboxclick.isclicked(controls))
    def triggerstart(self,controls):
        return not controls.gl and not self.textboxclick.isholdclicked(controls)
    def update(self,controls):
        super().update(controls)
        self.textboxclick.trackhover(controls)
        if not self.goal:
            # goal unreached state
            if not self.ungoing:
                # start substate
                if self.triggerungoing(controls):# flip to ungoing
                    self.soundstart.play()
                    self.ungoing=True
                    self.startactor.show=False
                    self.ungoingactor.show=True
                    self.finishactor.show=False
                    self.timer.start()# reset ungoing timer
                    self.ungoingactor.dict["anim1"].rewind()
                    if self.addpartner:
                        self.ungoingactor.dict["animadd1"].rewind()
                    if self.addbug:
                        self.ungoingactor.dict["animadd2"].rewind()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                    self.startactor.dict["anim1"].rewind()
                    if self.addpartner:
                        self.startactor.dict["animadd1"].rewind()
                if self.timer.ring:# flip to goal reached
                    self.goal=True
                    self.sounddone.play()
                    self.startactor.show=False
                    self.ungoingactor.show=False
                    self.finishactor.show=True
                    self.text_undone.show=False
                    self.text_done.show=True
                    self.timerend.start()
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################



















#
