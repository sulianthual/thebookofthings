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
import core
import draw


####################################################################################################################
# World
#* WORLD


# World Template
class obj_world:
    def __init__(self,creator,**kwargs):
        self.type='world'
        self.creator=creator# created by scene
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
# *TEMPLATE *ACTOR *GRANDACTOR *RIGIDBODY

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
class obj_grandactor():
    def __init__(self,creator,xy,scale=1,rotate=0,fliph=False,flipv=False,fliphv=False):
        # Creation
        self.creator=creator# created by world
        self.xini=xy[0]# initial position
        self.yini=xy[1]
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
    def birth(self):# add to world
        self.creator.addactor(self)
        self.alive=True
    def kill(self):# remove from world
        self.creator.removeactor(self)
        self.alive=False
    def destroy(self):# kill with additional funcionalities (e.g. leave trailing smoke)
        self.kill()
    def hit(self,hitter):# hit by something
        pass
    def addpart(self,name,element):# add element
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )
    def removepart(self,name):# remove element
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
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
class obj_world_sunrise(obj_world):
    def setup(self):
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
        self.staticactor.addpart( 'img1', draw.obj_image('tree',(1029,449),scale=0.5) )
        self.staticactor.addpart( 'img2', draw.obj_image('tree',(81,434),scale=0.5) )
        self.staticactor.addpart( 'img3', draw.obj_image('horizon',(640,720-150),path='premade') )
        self.staticactor.addpart( 'img4', draw.obj_image('house',(296,443),scale=0.5) )
        self.staticactor.addpart( 'img5', draw.obj_image('tree',(826,466),scale=0.5) )
        self.staticactor.addpart( 'img6', draw.obj_image('tree',(671,590),scale=0.5) )
        self.staticactor.addpart( 'img7', draw.obj_image('tree',(441,642),scale=0.5) )
        self.staticactor.addpart( 'img8', draw.obj_image('tree',(116,584),scale=0.5) )
        # start actor
        # self.startactor.addpart( 'img1', draw.obj_image('sun',(660,300),scale=0.5) )
        # ungoing actor
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch2_sunrise','sun',(640,360)) )
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('sun',(660,300),scale=0.5) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [W] to rise the sun',(1000,620),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Morning Time!',(1000,620)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(100)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
    def triggerungoing(self,controls):
        return controls.w and controls.wc
    def triggerstart(self,controls):
        return not controls.w
    def update(self,controls):
        super().update(controls)
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
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: wakeup
class obj_world_wakeup(obj_world):
    def setup(self,**kwargs):
        # default options
        self.partner=False# add partner alongside hero
        self.angryfaces=False# replace happy faces with angry faces
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.partner=kwargs["partner"]# partner options
            if 'angryfaces' in kwargs: self.angryfaces=kwargs["angryfaces"]# partner options
        #
        # change base picture
        self.herobaseimg='herobase'
        self.partnerbaseimg='partnerbase'
        if self.angryfaces:# replace with angry characters
            self.herobaseimg='herobaseangry'
            self.partnerbaseimg='partnerbaseangry'


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
        self.staticactor.addpart( 'img1', draw.obj_image('bed',(440,500),scale=0.75) )
        # start actor
        if self.partner == 'inlove':# add partner in love
            self.startactor.addpart( 'imgadd1', draw.obj_image(self.partnerbaseimg,(420+100,490-50),scale=0.7,rotate=80) )
        self.startactor.addpart( 'img1', draw.obj_image(self.herobaseimg,(420,490),scale=0.7,rotate=80) )

        # ungoing actor
        if self.partner == 'inlove':# add partner in love
            self.ungoingactor.addpart( 'animadd1', draw.obj_animation('ch1_heroawakes',self.partnerbaseimg,(640+100,360-50),scale=0.7) )
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch1_heroawakes',self.herobaseimg,(640,360),scale=0.7) )
        # finish actor
        if self.partner == 'inlove':# add partner in love
            self.finishactor.addpart( 'imgadd1', draw.obj_image(self.partnerbaseimg,(903+100,452-50),scale=0.7) )
        self.finishactor.addpart( 'img1', draw.obj_image(self.herobaseimg,(903,452),scale=0.7) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [D] to Wake up',(1100,480),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Good Morning!',(1150,480)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(100)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
    def triggerungoing(self,controls):
        return controls.d and controls.dc
    def triggerstart(self,controls):
        return not controls.d
    def update(self,controls):
        super().update(controls)
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
                    if self.partner == 'inlove':
                        self.ungoingactor.dict["animadd1"].rewind()
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
class obj_world_breakfastdrinking(obj_world):
    def setup(self):
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.progressbar=obj_grandactor(self,(640,360))# progress bar
        self.hero=obj_grandactor(self,(145,515))# hero
        self.partner=obj_grandactor(self,(1160,490))# partner
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        # static
        self.staticactor.addpart( 'img1', draw.obj_image('floor3',(640,720-100),path='premade') )
        self.staticactor.addpart( 'img2', draw.obj_image('coffeecup',(830,560),scale=0.5,fliph=True) )
        self.staticactor.addpart( 'img3', draw.obj_image('coffeecup',(495,560),scale=0.5,fliph=False) )
        # progress bar
        self.progressbar.addpart( 'bar', draw.obj_image('completion1fill',(640,250),path='premade') )
        self.progressbar.addpart( 'slide', draw.obj_image('completion1slide',(640,250),path='premade') )
        self.progressbar.addpart( 'borders', draw.obj_image('completion1',(640,250),path='premade') )
        self.progressbar.addpart( 'textbox', draw.obj_textbox('0%',(640,320)) )
        self.progressmx=2#1# move rate of progressbar (respect to self.progress)
        self.progressmax=int(567/self.progressmx)# max progress
        self.progress=0# 0 to max progress
        # hero
        self.hero.addpart( 'waiting', draw.obj_image('herobaseangry',(150,540),scale=1.15,fliph=False) )
        self.hero.addpart( 'happy', draw.obj_image('herobase',(150,540),scale=1.15,fliph=False) )
        self.hero.addpart( 'drinkinghero', draw.obj_animation('ch4_herodrinks1','herobase',(640,360)) )
        self.hero.addpart( 'drinkingdrink', draw.obj_animation('ch4_herodrinks2','drink',(640,360)) )
        self.hero.addpart( 'busted', draw.obj_image('herobaseangry',(195,620),scale=1.2,rotate=26) )
        self.hero.addpart( 'finished', draw.obj_animation('world_breakfastdrinking3','herobase',(640,360)) )
        self.hero.dict['waiting'].show=True
        self.hero.dict['happy'].show=False
        self.hero.dict['drinkinghero'].show=False
        self.hero.dict['drinkingdrink'].show=False
        self.hero.dict['busted'].show=False
        self.hero.dict['finished'].show=False
        self.herostate=0# 0,1,2 for neutral,drinking,happy (excludes busted from partnerbusting)
        self.herohappytimer=tool.obj_timer(100)# timer for happy after drinking
        # partner
        self.partner.addpart( 'waiting_base', draw.obj_image('stickbody',(1160-50,640+15),scale=1.15,fliph=True,path='premade') )
        self.partner.addpart( 'waiting_headleft', draw.obj_image('partnerheadangry',(1160-50,340+15),scale=1.15,fliph=True) )
        self.partner.addpart( 'waiting_headright', draw.obj_image('partnerheadangry',(1160-50+30,340+15),scale=1.15,fliph=False) )
        self.partner.addpart( 'waiting_headrightup', draw.obj_image('partnerheadangry',(1160-50+20,340+15),scale=1.15,rotate=15,fliph=False) )
        self.partner.addpart( 'waiting_headrightbobble', draw.obj_animation('world_breakfastdrinking1','partnerheadangry',(640,360)) )
        self.partner.addpart( 'busting', draw.obj_animation('world_breakfastdrinking2','partnerbaseangry',(640,360)) )
        self.partner.addpart( 'bustedtext', draw.obj_textbox('Busted!',(940,300),fontsize='huge') )
        self.partner.dict['waiting_base'].show=True
        self.partner.dict['waiting_headleft'].show=True
        self.partner.dict['waiting_headright'].show=False
        self.partner.dict['waiting_headrightup'].show=False
        self.partner.dict['waiting_headrightbobble'].show=False
        self.partner.dict['busting'].show=False
        self.partner.dict['bustedtext'].show=False
        self.partnerbusting=False# busting or not (2 states)
        self.partnerstate=0# while not busting, state 0,1,2,3 for headleft,headright,headrightup,headrightbobble
        self.partnertimer=tool.obj_timer(50)# timer for switch states
        self.partnertimer.start()
        self.partnertimerbusting=tool.obj_timer(100)# timer for busting
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [W] to Sneak Drink',(640,690),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Wasted!',(640,690)) )
        self.text_undone.show=True
        self.text_done.show=False
        # timer for end
        self.timerend=tool.obj_timer(180)# goal to done
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            if self.progress>self.progressmax-1:
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
                self.partner.dict['waiting_base'].show=True
                self.partner.dict['waiting_headleft'].show=True
                self.partner.dict['waiting_headright'].show=False
                self.partner.dict['waiting_headrightup'].show=False
                self.partner.dict['waiting_headrightbobble'].show=False
                self.partner.dict['busting'].show=False
                self.partner.dict['bustedtext'].show=False
            #
            # partner is busting hero
            if self.partnerbusting:
                self.partnertimerbusting.update()
                if self.partnertimerbusting.ring:# switch back to normal
                    self.partnerbusting=False
                    self.herostate=0
                    self.partnerstate=0
                    self.partnertimer.amount=100
                    self.partnertimer.start()
                    self.hero.dict['waiting'].show=True
                    self.hero.dict['drinkinghero'].show=False
                    self.hero.dict['drinkingdrink'].show=False
                    self.hero.dict['busted'].show=False
                    self.hero.dict['finished'].show=False
                    self.partner.dict['waiting_base'].show=True
                    self.partner.dict['waiting_headleft'].show=True
                    self.partner.dict['waiting_headright'].show=False
                    self.partner.dict['waiting_headrightup'].show=False
                    self.partner.dict['waiting_headrightbobble'].show=False
                    self.partner.dict['busting'].show=False
                    self.partner.dict['bustedtext'].show=False

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
                    self.hero.dict['drinkingdrink'].show=False
                    self.hero.dict['busted'].show=True
                    self.hero.dict['finished'].show=False
                    self.partner.dict['waiting_base'].show=False
                    self.partner.dict['waiting_headleft'].show=False
                    self.partner.dict['waiting_headright'].show=False
                    self.partner.dict['waiting_headrightup'].show=False
                    self.partner.dict['waiting_headrightbobble'].show=False
                    self.partner.dict['busting'].show=True
                    self.partner.dict['bustedtext'].show=True
                # hero behavior
                if self.herostate==0:# neutral
                    if controls.w and controls.wc:# switch to drinking
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
                    if not controls.w and controls.wc:# switch to happy
                        self.herostate=2#
                        self.herohappytimer.start()
                        self.hero.dict['waiting'].show=False
                        self.hero.dict['happy'].show=True
                        self.hero.dict['drinkinghero'].show=False
                        self.hero.dict['drinkingdrink'].show=False
                        self.hero.dict['busted'].show=False
                        self.hero.dict['finished'].show=False
                elif self.herostate==2:# happy
                    if controls.w and controls.wc:# switch to drinking
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
                    elif self.partnerstate==1:# headright
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=True
                        self.partner.dict['waiting_headrightup'].show=False
                        self.partner.dict['waiting_headrightbobble'].show=False
                        self.partner.dict['busting'].show=False
                    elif self.partnerstate==2:# headrightup
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=False
                        self.partner.dict['waiting_headrightup'].show=True
                        self.partner.dict['waiting_headrightbobble'].show=False
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
                    elif self.partnerstate==3:# headrightbobble
                        self.partner.dict['waiting_base'].show=True
                        self.partner.dict['waiting_headleft'].show=False
                        self.partner.dict['waiting_headright'].show=False
                        self.partner.dict['waiting_headrightup'].show=False
                        self.partner.dict['waiting_headrightbobble'].show=True
                        self.partner.dict['waiting_headrightbobble'].rewind()
                        self.partner.dict['busting'].show=False
                        self.partner.dict['bustedtext'].show=False
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
class obj_world_fishing(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        # hook
        self.hook=obj_grandactor(self,(640,100))
        self.hook.actortype='hook'
        self.hook.rx=30
        self.hook.ry=30
        self.hook.r=30
        self.hook.addpart( 'line',draw.obj_image('hookline',(640,100-390),path='premade') )
        self.hook.addpart( 'img_fish',draw.obj_image('fish',(640,100+50),scale=0.25,rotate=-90) )
        self.hook.dict['img_fish'].show=False
        self.hook.addpart( 'img_hook',draw.obj_image('hook',(640,100),scale=0.25) )
        self.dydown=5
        self.dyup=2
        # fish status
        self.fishfree=True# fish not caugth (yet)
        # fish animation
        self.fish=obj_grandactor(self,(640,360))
        self.fish.addpart( 'anim_fish',draw.obj_animation('fishmove1','fish',(640,360),imgscale=0.25) )
        # fish hit box
        self.fishbox=obj_grandactor(self,(340,360))
        self.fishbox.actortype='fish'
        self.fishbox.rx=30
        self.fishbox.ry=30
        self.fishbox.r=30
        # short timer at end
        self.timerend=tool.obj_timer(100)
        # textbox when caught
        self.text1=obj_grandactor(self,(840,500))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Hold [S] to lower Hook',(1100,480),color=share.colors.instructions) )
        self.text2=obj_grandactor(self,(840,500))
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


# Mini Game: travel to evil lair (or back from it)
class obj_world_traveltolair(obj_world):
    def setup(self,**kwargs):
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        self.gotolair=True# go to or from lair
        self.addpartner=False# add partner walking with hero
        # scene tuning
        if kwargs is not None:
            if 'tohome' in kwargs: self.gotolair=not kwargs["tohome"]# option go back home
            if 'partner' in kwargs: self.addpartner=kwargs["partner"]# option partner walks with hero
        if self.gotolair:# initial hero position
            self.heroxstart=180
        else:
            self.heroxstart=1280-180
        self.staticactor=obj_grandactor(self,(640,360))# background
        self.hero=obj_grandactor(self,(self.heroxstart,400))# hero
        self.text_undone=obj_grandactor(self,(640,360))# text always in front
        self.text_done=obj_grandactor(self,(640,360))
        # static
        self.staticactor.addpart( 'img1', draw.obj_image('house',(100,340),scale=0.5) )
        self.staticactor.addpart( 'img2', draw.obj_image('tower',(1280-100,340),scale=0.5) )
        self.staticactor.addpart( 'text1', draw.obj_textbox('home',(100,470)) )
        self.staticactor.addpart( 'text2', draw.obj_textbox('evil lair',(1280-100,470)) )
        self.staticactor.addpart( 'img3', draw.obj_image('tree',(230,570),scale=0.5) )
        self.staticactor.addpart( 'img4', draw.obj_image('tree',(100,720-100),scale=0.5) )
        self.staticactor.addpart( 'img5', draw.obj_image('tree',(300,235),scale=0.35) )
        self.staticactor.addpart( 'img6', draw.obj_image('mountain',(1280-100,580),scale=0.4) )
        self.staticactor.addpart( 'img7', draw.obj_image('mountain',(990,720-100),scale=0.5) )
        self.staticactor.addpart( 'img8', draw.obj_image('mountain',(1160,170),scale=0.35) )
        self.staticactor.addpart( 'img9', draw.obj_image('mountain',(1030,120),scale=0.3) )
        # hero
        # optional partner (same actor as hero)
        if self.addpartner:
            self.pxoff=30# offset relative to hero
            self.pyoff=-30
            self.hero.addpart( 'pface_right', draw.obj_image('partnerbase',(self.heroxstart+self.pxoff,400+self.pyoff),scale=0.25) )
            self.hero.addpart( 'pface_left', draw.obj_image('partnerbase',(self.heroxstart+self.pxoff,400+self.pyoff),scale=0.25,fliph=True) )
            self.hero.addpart( 'pwalk_right', draw.obj_image('partnerwalk',(self.heroxstart+self.pxoff,400+self.pyoff),scale=0.25) )
            self.hero.addpart( 'pwalk_left', draw.obj_image('partnerwalk',(self.heroxstart+self.pxoff,400+self.pyoff),scale=0.25,fliph=True) )
        self.hero.addpart( 'face_right', draw.obj_image('herobase',(self.heroxstart,400),scale=0.25) )
        self.hero.addpart( 'face_left', draw.obj_image('herobase',(self.heroxstart,400),scale=0.25,fliph=True) )
        self.hero.addpart( 'walk_right', draw.obj_image('herowalk',(self.heroxstart,400),scale=0.25) )
        self.hero.addpart( 'walk_left', draw.obj_image('herowalk',(self.heroxstart,400),scale=0.25,fliph=True) )
        self.herofaceright=self.gotolair
        self.herowalking=False# hero walking or standing
        self.hero.dict['face_right'].show=self.herofaceright and not self.herowalking
        self.hero.dict['face_left'].show=not self.herofaceright and not self.herowalking
        self.hero.dict['walk_right'].show=self.herofaceright and self.herowalking
        self.hero.dict['walk_left'].show=not self.herofaceright and self.herowalking
        if self.addpartner:
            self.hero.dict['pface_right'].show=self.hero.dict['face_right'].show
            self.hero.dict['pface_left'].show=self.hero.dict['face_left'].show
            self.hero.dict['pwalk_right'].show=self.hero.dict['walk_right'].show
            self.hero.dict['pwalk_left'].show=self.hero.dict['walk_left'].show
        self.herowalktimer=tool.obj_timer(10)# timer to alternate walk slides
        self.herowalkframe1=True# alternate True/False for two frames
        self.heromx=8# moving rate
        self.heromy=8# moving rate

        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Move with [W][A][S][D]',(640,680),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('We made it!',(640,680)) )
        self.text_undone.show=True
        self.text_done.show=False
        # area to reach
        if self.gotolair:
            self.goalarea=obj_grandactor(self,(1280-100,340))# reach lair
            self.goalarea.rx=100
            self.goalarea.ry=100
        else:
            self.goalarea=obj_grandactor(self,(100,340))# reach house
            self.goalarea.rx=100
            self.goalarea.ry=100
        # timer
        self.timerend=tool.obj_timer(80)# goal to done
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # hero walk motion
            if controls.d or controls.a or controls.w or controls.s:
                self.herowalking=True
            else:
                self.herowalking=False
                self.herowalktimer.start()# reset timer
            if self.herowalking:
                self.herowalktimer.update()
                if self.herowalktimer.ring:
                    self.herowalkframe1=not self.herowalkframe1
                    self.herowalktimer.start()
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
            # move hero
            if controls.a:
                self.hero.movex(-self.heromx)
                if controls.ac:
                    self.herofaceright=False
            if controls.d:
                self.hero.movex(self.heromx)
                if controls.dc:
                    self.herofaceright=True
            if controls.w:
                self.hero.movey(-self.heromy)
            if controls.s:
                self.hero.movey(self.heromy)
            # partner visuals
            if self.addpartner:
                self.hero.dict['pface_right'].show=self.hero.dict['face_right'].show
                self.hero.dict['pface_left'].show=self.hero.dict['face_left'].show
                self.hero.dict['pwalk_right'].show=self.hero.dict['walk_right'].show
                self.hero.dict['pwalk_left'].show=self.hero.dict['walk_left'].show

            # reach goal
            if tool.checkrectcollide(self.hero,self.goalarea):
                self.goal=True
                self.timerend.start()
                self.text_undone.show=False
                self.text_done.show=True
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame



####################################################################################################################

# Mini Game: dodge gun shots
class obj_world_dodgegunshots(obj_world):
    def setup(self):
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
        # static
        self.staticactor.addpart( 'floor', draw.obj_image('floor1',(640,500),path='premade') )
        self.staticactor.addpart( 'sun', draw.obj_image('sun',(800,250),scale=0.4) )
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
        # villain
        self.villain.addpart( 'stand', draw.obj_image('villainbase',(1280-150,450+self.yoff),scale=0.5,fliph=True) )
        self.villain.addpart( 'standgun', draw.obj_image('gun',(1280-150-175,445+self.yoff),scale=0.25,fliph=True) )
        self.villain.addpart( 'standarm', draw.obj_image('stickshootarm',(1280-260,442+self.yoff),scale=0.5,path='premade') )# missing small piece
        self.villain.addpart( 'crouch', draw.obj_image('villainshootcrouch',(1280-150,500+50+40+30-50+self.yoff),scale=0.5) )
        self.villain.addpart( 'crouchgun', draw.obj_image('gun',(1280-150-175,500+50+40+30-50+self.yoff),scale=0.25,fliph=True) )
        self.villain.dict['stand'].show=True
        self.villain.dict['crouch'].show=False
        self.villain.dict['standgun'].show=True
        self.villain.dict['standarm'].show=True
        self.villain.dict['crouchgun'].show=False
        self.villaincrouch=False# villain is crouching or not (switch randomly every shot)
        self.villainshots=15# number of shots
        self.villaintimer=80# shot reload time
        self.villaintimermin=50# min time
        self.villaintimerm=0.98# timer fact each shot
        self.villaintimershoot=tool.obj_timer(self.villaintimer,cycle=True)#timer between shots
        self.villaintimershoot.start()
        # cannonballs
        self.cannonballs=[]# empty list
        # health bar
        self.maxherohealth=5# starting hero health
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(640,360))
        for i in range(self.maxherohealth):
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(50+i*75,650),scale=0.125) )
        # bullet count
        self.maxvillainshots=12
        self.villainshots=self.maxvillainshots
        self.bulletbar=obj_grandactor(self,(640,360))
        for i in range(self.maxvillainshots):
            if i>int(self.maxvillainshots/2)-1:
                self.bulletbar.addpart('bullet_'+str(i), draw.obj_image('bullet',(1280-25-(i-int(self.maxvillainshots/2))*50-10,720-25-5),scale=0.125) )
            else:
                self.bulletbar.addpart('bullet_'+str(i), draw.obj_image('bullet',(1280-25-i*50-10,720-25-50-5),scale=0.125) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('[W: Jump] [S: Crouch]',(640,660),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('He is the one!',(640,660)) )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('You are Dead',(640,360),scale=1.5) )
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(300)# goal to done
    def makecannonball(self,x,y):
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
            # goal unreached state
            # hero dynamics
            self.herofy=0# force
            self.herofy += self.herog# gravity
            if self.heromayjump and (controls.w and controls.wc):# jump
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
            if controls.sc:
                if controls.s:# switch to crouch
                    self.herocrouch=True
                    self.hero.dict['stand'].show=False
                    self.hero.dict['crouch'].show=True
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
                            self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        else:
                            # hero dies
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
class obj_world_stompfight(obj_world):
    def setup(self):
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
        # static
        self.staticactor.addpart( 'floor', draw.obj_image('floor2',(640,self.yground+90),path='premade') )
        # self.staticactor.addpart( 'sun', draw.obj_image('sun',(640,280),scale=0.4) )
        # hero
        self.hero.addpart( 'stand_right', draw.obj_image('herobase',(340,self.yground),scale=0.35) )
        self.hero.addpart( 'stand_left', draw.obj_image('herobase',(340,self.yground),scale=0.35,fliph=True) )
        self.hero.addpart( 'hurt', draw.obj_image('herobase',(340,self.yground+70),scale=0.35,rotate=90) )
        self.hero.addpart( 'hurttext', draw.obj_textbox('ouch!',(340,self.yground-120),scale=1) )
        self.hero.dict['stand_right'].show=True
        self.hero.dict['stand_left'].show=False
        self.hero.dict['hurt'].show=False
        self.hero.dict['hurttext'].show=False
        self.heromayjump=True# hero can jump (not if in the air)
        self.heromayholdjump=False# hero can hold to jump higher
        self.herohurt=False# hurting state or not
        self.herohurttimer=tool.obj_timer(100)# how long hero is hurting (and invincible). Make it just >kicking time,<rest+stand time
        self.herodt=1# hero time increment
        self.herofy=0# hero force
        self.herov=0# hero velocity
        self.herog=1# gravity rate
        self.herod=0.07# dissipation rate
        self.heroj=1# jump rate (click button)
        self.herojh=3.5# jump rate (hold button)
        self.heroholdjumptimer=tool.obj_timer(12)# how long can hold jump button
        self.heromx=12# move rate horizontally
        # hero hitboxes
        self.herohitbox1=obj_grandactor(self,(340,self.yground))# for being hit
        self.herohitbox1.rx=50
        self.herohitbox1.ry=100
        self.herohitbox2=obj_grandactor(self,(340,self.yground+75))# for hitting (is hero feets)
        self.herohitbox2.rx=50
        self.herohitbox2.ry=25
        # villain
        self.villain.addpart( 'stand_right', draw.obj_image('villainbase',(940,self.yground-12),scale=0.35) )
        self.villain.addpart( 'stand_left', draw.obj_image('villainbase',(940,self.yground-12),scale=0.35,fliph=True) )
        self.villain.addpart( 'kick_right', draw.obj_image('villainkick',(940,self.yground-12),scale=0.35) )
        self.villain.addpart( 'kick_left', draw.obj_image('villainkick',(940,self.yground-12),scale=0.35,fliph=True) )
        self.villain.addpart( 'hurt', draw.obj_image('villainbase',(940,self.yground-12+70),scale=0.35,rotate=90) )
        self.villain.addpart( 'hurttext', draw.obj_textbox('get that!',(940,self.yground-120),scale=1) )
        self.villain.dict['stand_right'].show=False
        self.villain.dict['stand_left'].show=True
        self.villain.dict['kick_right'].show=False
        self.villain.dict['kick_left'].show=False
        self.villain.dict['hurt'].show=False
        self.villain.dict['hurttext'].show=False
        self.villainhurt=False# hurt or not
        self.villainstate='stand'# stand, kick, rest (when no hurt)
        self.villaintimerstand=tool.obj_timer(40)
        self.villaintimerkick=tool.obj_timer(80)
        self.villaintimerrest=tool.obj_timer(100)#
        self.villaintimerhurt=tool.obj_timer(100)
        self.villaintimerstand.start()
        self.villainfaceright=False# direction facing (changes)
        self.villainmx=18# move rate horizontally
        self.villainxmin=200# area where will face to right
        self.villainxmax=1280-200# area where will face to left
        # villlain hitboxes
        self.villainhitbox1=obj_grandactor(self,(940,self.yground-12-50))# for being hit
        self.villainhitbox1.rx=30
        self.villainhitbox1.ry=25
        self.villainhitbox2=obj_grandactor(self,(940+50,self.yground-12+50))# for hitting (villain kick)
        self.villainhitbox2.rx=50
        self.villainhitbox2.ry=70
        # health bar hero
        self.ybar=200# for health bars and text
        self.maxherohealth=5# starting hero health
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(640,360))
        self.healthbar.addpart('face', draw.obj_image('herohead',(50,self.ybar),scale=0.2) )
        for i in range(self.maxherohealth):
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(150+i*75,self.ybar),scale=0.125) )
        # health bar villain
        self.maxvillainhealth=3# starting villain health
        self.villainhealth=self.maxvillainhealth# updated one
        self.vealthbar=obj_grandactor(self,(640,360))
        self.vealthbar.addpart('face', draw.obj_image('villainhead',(1280-50,self.ybar),scale=0.2,fliph=True) )
        for i in range(self.maxvillainhealth):
            self.vealthbar.addpart('heart_'+str(i), draw.obj_image('love',(1280-150-i*75,self.ybar),scale=0.125) )
            self.vealthbar.addpart('heartscar_'+str(i), draw.obj_image('scar',(1280-150-i*75,self.ybar),scale=0.125) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('[A,D: Move] [W: Jump]',(640,self.ybar),color=share.colors.instructions) )
        self.text_donewin.addpart( 'text1', draw.obj_textbox('Victory!',(640,self.ybar)) )
        self.text_donelost.addpart( 'text1', draw.obj_textbox('You are Dead',(640,360),scale=1.5) )
        # timer for done part
        self.timerendwin=tool.obj_timer(120)# goal to done
        self.timerendloose=tool.obj_timer(120)# goal to done
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            #
            if not self.herohurt:
                # hero dynamics y
                self.herofy=0# force
                self.herofy += self.herog# gravity
                if self.heromayjump and (controls.w and controls.wc):# jump (click button)
                    self.herofy -= self.heroj
                    self.herov=0# reset velocity
                    self.heromayjump=False# cant jump again
                    self.heromayholdjump=True# can hold this jump
                    self.heroholdjumptimer.start()
                if self.heromayholdjump and controls.w:# jump (hold button)
                    self.herofy -= self.herojh
                    self.heroholdjumptimer.update()
                    if self.heroholdjumptimer.ring:
                        self.heromayholdjump=False
                self.herov += self.herodt*(self.herofy-self.herod*self.herov)# dtv=g+flap-dv**2
                self.hero.movey(self.herodt*self.herov)# dty=v
                if self.hero.y>self.yground:# hero is on ground
                    self.hero.movetoy(self.yground)
                    self.herov = 0# just stall
                    self.heromayjump=True# may jump from ground again
                # hero dynamics x
                if controls.a:#
                    self.hero.movex(-self.heromx)
                    if controls.ac:# flip left
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=True
                        self.hero.dict['hurt'].show=False
                        self.hero.dict['hurttext'].show=False
                if controls.d:
                    self.hero.movex(self.heromx)
                    if controls.dc:# flip right
                        self.hero.dict['stand_right'].show=True
                        self.hero.dict['stand_left'].show=False
                        self.hero.dict['hurt'].show=False
                        self.hero.dict['hurttext'].show=False
            else:
                self.herohurttimer.update()
                if self.herohurttimer.ring:
                    self.herohurt=False
                    self.hero.dict['stand_right'].show=True
                    self.hero.dict['stand_left'].show=False
                    self.hero.dict['hurt'].show=False
                    self.hero.dict['hurttext'].show=False
            if self.hero.x<self.xmin:# boundaries
                self.hero.movetox(self.xmin)
            elif self.hero.x>self.xmax:
                self.hero.movetox(self.xmax)
            # hero hitboxes move
            self.herohitbox1.movetoxy( (self.hero.x,self.hero.y) )
            self.herohitbox2.movetoxy( (self.hero.x,self.hero.y+75) )
            # villain
            if not self.villainhurt:
                if self.villainstate=='stand':
                    self.villaintimerstand.update()
                    if self.villaintimerstand.ring:
                        self.villainstate='kick'
                        self.villaintimerkick.start()
                        self.villain.dict['stand_right'].show=False
                        self.villain.dict['stand_left'].show=False
                        self.villain.dict['kick_right'].show=self.villainfaceright
                        self.villain.dict['kick_left'].show=not self.villainfaceright
                        self.villain.dict['hurt'].show=False
                        self.villain.dict['hurttext'].show=False
                #
                elif self.villainstate=='kick':
                    # kick one direction
                    if self.villainfaceright:
                        self.villain.movex(self.villainmx)
                    else:
                        self.villain.movex(-self.villainmx)
                    self.villaintimerkick.update()
                    if self.villaintimerkick.ring:
                        self.villainstate='rest'
                        self.villaintimerrest.start()
                        self.villain.dict['stand_right'].show=self.villainfaceright
                        self.villain.dict['stand_left'].show=not self.villainfaceright
                        self.villain.dict['kick_right'].show=False
                        self.villain.dict['kick_left'].show=False
                        self.villain.dict['hurt'].show=False
                        self.villain.dict['hurttext'].show=False
                #
                elif self.villainstate=='rest':
                    self.villaintimerrest.update()
                    if self.villaintimerrest.ring:# flip to stand (choose direction)
                        self.villainstate='stand'
                        self.villaintimerstand.start()
                        # choose next kick direction
                        self.villainfaceright = self.villain.x<self.hero.x# just face hero
                        # if self.villain.x<self.villainxmin:# villain left edge of screen
                        #     self.villainfaceright=True
                        # elif self.villain.x>self.villainxmax:# villain left edge of screen
                        #     self.villainfaceright=False
                        # else:
                        #     self.villainfaceright=tool.randbool()# random facing direction
                        self.villain.dict['stand_right'].show=self.villainfaceright
                        self.villain.dict['stand_left'].show=not self.villainfaceright
                        self.villain.dict['kick_right'].show=False
                        self.villain.dict['kick_left'].show=False
                        self.villain.dict['hurt'].show=False
                        self.villain.dict['hurttext'].show=False
            #
            else:# villain hurt
                    self.villaintimerhurt.update()
                    if self.villaintimerhurt.ring:# flip to stand (choose direction)
                        self.villainhurt=False
                        self.villainstate='stand'
                        self.villaintimerstand.start()
                        if self.villain.x<self.villainxmin:# villain left edge of screen
                            self.villainfaceright=True
                        elif self.villain.x>self.villainxmax:# villain left edge of screen
                            self.villainfaceright=False
                        else:
                            self.villainfaceright=tool.randbool()# random facing direction
                        self.villain.dict['stand_right'].show=self.villainfaceright
                        self.villain.dict['stand_left'].show=not self.villainfaceright
                        self.villain.dict['kick_right'].show=False
                        self.villain.dict['kick_left'].show=False
                        self.villain.dict['hurt'].show=False
                        self.villain.dict['hurttext'].show=False
            # villain boundaries
            if self.villain.x<self.xmin:# boundaries
                self.villain.movetox(self.xmin)
                self.villainfaceright=True# reverse direction
                if self.villainstate=='kick':
                    self.villain.dict['kick_right'].show=self.villainfaceright
                    self.villain.dict['kick_left'].show=not self.villainfaceright
                else:
                    self.villain.dict['stand_right'].show=self.villainfaceright
                    self.villain.dict['stand_left'].show=not self.villainfaceright
            elif self.villain.x>self.xmax:
                self.villain.movetox(self.xmax)
                self.villainfaceright=False# reverse direction
                if self.villainstate=='kick':
                    self.villain.dict['kick_right'].show=self.villainfaceright
                    self.villain.dict['kick_left'].show=not self.villainfaceright
                else:
                    self.villain.dict['stand_right'].show=self.villainfaceright
                    self.villain.dict['stand_left'].show=not self.villainfaceright
            # villain hitboxes move
            self.villainhitbox1.movetoxy( (self.villain.x,self.villain.y-50) )
            if self.villainfaceright:
                self.villainhitbox2.movetoxy( (self.villain.x+50,self.villain.y+50) )
            else:
                self.villainhitbox2.movetoxy( (self.villain.x-50,self.villain.y+50) )
            # villain hits hero or reverse
            if not self.herohurt and self.villainstate=='kick':
                if tool.checkrectcollide(self.villainhitbox2,self.herohitbox1):# villain hits hero
                    self.herohealth -= 1
                    if self.herohealth>0:
                        self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        self.herohurt=True
                        self.hero.movetoy(self.yground)# put hero to ground
                        self.herov = 0# just stall
                        self.heromayjump=True# may jump from ground again
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=False
                        self.hero.dict['hurt'].show=True
                        self.hero.dict['hurttext'].show=True
                        self.herohurttimer.start()
                    else:# dead hero
                        self.healthbar.dict['heart_'+str(self.herohealth)].show=False
                        self.goal=True
                        self.win=False
                        self.timerendloose.start()
                        self.text_undone.show=False
                        self.text_donelost.show=True
                        self.hero.dict['stand_right'].show=False
                        self.hero.dict['stand_left'].show=False
                        self.hero.dict['hurt'].show=True
                        self.hero.dict['hurttext'].show=False

            if not self.villainhurt and self.herov>0:
                if tool.checkrectcollide(self.villainhitbox1,self.herohitbox2):# hero hits villain
                    self.villainhealth -= 1
                    if self.villainhealth>0:
                        self.vealthbar.dict['heart_'+str(self.villainhealth)].show=False
                        self.vealthbar.dict['heartscar_'+str(self.villainhealth)].show=False
                        self.villainhurt=True
                        self.villainstate='stand'
                        self.villaintimerhurt.start()
                        self.villain.dict['stand_right'].show=False
                        self.villain.dict['stand_left'].show=False
                        self.villain.dict['kick_right'].show=False
                        self.villain.dict['kick_left'].show=False
                        self.villain.dict['hurt'].show=True
                        self.villain.dict['hurttext'].show=True
                    else:# dead villain
                        self.vealthbar.dict['heart_'+str(self.villainhealth)].show=False
                        self.vealthbar.dict['heartscar_'+str(self.villainhealth)].show=False
                        self.goal=True
                        self.win=True
                        self.timerendwin.start()
                        self.text_undone.show=False
                        self.text_donewin.show=True
                        self.villain.dict['stand_right'].show=False
                        self.villain.dict['stand_left'].show=False
                        self.villain.dict['kick_right'].show=False
                        self.villain.dict['kick_left'].show=False
                        self.villain.dict['hurt'].show=True
                        self.villain.dict['hurttext'].show=False
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

# Mini Game: Eat Fish
class obj_world_eatfish(obj_world):
    def setup(self,**kwargs):
        # default options
        self.partner=False
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.partner=kwargs["partner"]# partner options
        #
        self.done=False# mini game is finished
        self.doneeating=False# done eating
        self.bites=6# total number of bites
        self.alternate_LR=True# alternate Left-Right pattern to eat
        self.eating=False

        # fish
        self.fish=obj_grandactor(self,(640,360))
        self.fishscale=1# initial size of fish
        self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,450), scale=self.fishscale,rotate=-45) )
        # hero eating or not eating
        self.herostand=obj_grandactor(self,(640,360))
        if self.partner == 'inlove':# add partner in love
            self.herostand.addpart( 'imgadd1', draw.obj_image('partnerbase',(340-100,400-50), scale=0.7) )
        self.herostand.addpart( 'img_stand',draw.obj_image('herobase',(340,400), scale=0.7) )
        self.heroeat=obj_grandactor(self,(640,360))
        if self.partner == 'inlove':# add partner in love
            self.heroeat.addpart( 'imgadd1', draw.obj_animation('ch1_heroeats1','partnerbase',(640-100,360-50),imgscale=0.7) )
        self.animation1=draw.obj_animation('ch1_heroeats1','herobase',(640,360),imgscale=0.7)
        self.heroeat.addpart('anim_eat', self.animation1)
        self.herostand.show=True
        self.heroeat.show=False
        # text
        self.text1=obj_grandactor(self,(640,360))
        self.text1.addpart( 'textbox1',draw.obj_textbox('Alternate [A] and [D] to Eat',(640,660),color=share.colors.instructions) )
        self.text2=obj_grandactor(self,(640,360))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Burp!',(800,390)) )
        self.text1.show=True
        self.text2.show=False
        # textbox crunch
        self.text3=obj_grandactor(self,(640,360))
        self.text3.addpart( 'textbox1', draw.obj_textbox('Crunch!',(860,180),scale=1.5) )
        self.text3.show=False
        # timer for eating
        self.timer=tool.obj_timer(50)
        # short timer after done eating
        self.timerend=tool.obj_timer(100)
    def eatfood(self):
        self.eating=True
        self.timer.start()
        self.bites -=1
        self.fishscale *= 0.8
        self.fish.removepart( 'img_fish')
        self.fish.addpart( 'img_fish',draw.obj_image('fish',(800,450), scale=self.fishscale,rotate=-45) )
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


# Mini Game: play a serenade
class obj_world_serenade(obj_world):
    def setup(self):
        self.done=False# mini game is finished
        self.doneplaying=False# done playing serenade
        # hero on left
        self.hero=obj_grandactor(self,(640,360))
        # self.hero.addpart( 'img_hero',draw.obj_image('herobase',(200,450), scale=0.7) )# bit messy
        self.hero.addpart( 'img_herohead',draw.obj_image('herohead',(200,354), scale=0.35) )
        self.hero.addpart( 'img_guitar',draw.obj_image('guitar',(200,500), scale=0.5,rotate=60) )
        # partner on right
        self.partner=obj_grandactor(self,(640,360))
        self.partner.addpart( 'img_partner',draw.obj_image('partnerbase',(1280-200,450), scale=0.7,fliph=True) )
        # melody score
        if True:
            self.score=obj_grandactor(self,(640,380))
            self.score.addpart( 'img',draw.obj_image('musicscore',(640,380),path='premade') )
        ### melody to reproduce
        self.melody=obj_grandactor(self,(640,360))
        self.melody.melodylength=8# number of notes to play
        melodyx=[-3.5,-2.5,-1.5,-0.5,0.5,1.5,2.5,3.5]# x positions (scaled)
        melodydx=50# x-spacing notes
        melodydy=30#y-spacing notes
        self.melody.melodynotes=[]
        for i in range(self.melody.melodylength):
            inote=tool.randint(1,4)
            if inote==1:
                note='W'
                ynote=1.5
            elif inote==2:
                note='A'
                ynote=-0.5
            elif inote==3:
                note='S'
                ynote=-1.5
            elif inote==4:
                note='D'
                ynote=0.5
            self.melody.melodynotes.append(note)
            position=(640+melodyx[i]*melodydx,380-ynote*melodydy)
            self.melody.addpart("imgnotebase_"+str(i), draw.obj_image('musicnotesquare',position,path='premade') )
            self.melody.addpart("imgnoteplay_"+str(i), draw.obj_image('musicnotesquare_played',position,path='premade') )
            self.melody.dict["imgnoteplay_"+str(i)].show=False
            self.melody.addpart("textboxnote_"+str(i), draw.obj_textbox(note,position) )
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
        self.text1.addpart( 'textbox1',draw.obj_textbox('Play Melody with [W][A][S][D]',(640,660),color=share.colors.instructions) )
        self.text2=obj_grandactor(self,(640,360))
        self.text2.addpart( 'textbox2',draw.obj_textbox('Beautiful!',(640,660)) )
        self.text1.show=True
        self.text2.show=False
        # short timer after done playing
        self.timerend=tool.obj_timer(100)
    def update(self,controls):
        super().update(controls)
        if not self.doneplaying:
            # current note played
            if controls.w and controls.wc:
                playednote='W'
            elif controls.a and controls.ac:
                playednote='A'
            elif controls.s and controls.sc:
                playednote='S'
            elif controls.d and controls.dc:
                playednote='D'
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
        else:# done playing
            self.text1.show=False
            self.text2.show=True
            self.floatingnotes.show=False
            self.floatinglove.show=True
            self.timerend.update()
            if self.timerend.ring: self.done=True


####################################################################################################################

# Mini Game: kiss
class obj_world_kiss(obj_world):
    def setup(self):
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
        # ungoing actor)
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch2_kiss1','herobase',(640,360)) )
        self.ungoingactor.addpart( 'anim2', draw.obj_animation('ch2_kiss2','partnerbase',(640,360)) )
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('partnerbase',(710,390),scale=0.7,rotate=15) )
        self.finishactor.addpart( 'img2', draw.obj_image('herobase',(580,400),scale=0.7,rotate=-15) )
        self.finishactor.addpart( 'anim1', draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4) )
        self.finishactor.addpart( 'anim2', draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [A]+[D] to kiss',(640,660),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('So Much Tongue!',(640,660)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(180)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
    def triggerungoing(self,controls):
        return (controls.a and controls.d) and (controls.ac or controls.dc)
    def triggerstart(self,controls):
        return not (controls.a and controls.d)
    def update(self,controls):
        super().update(controls)
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
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: sunrise
class obj_world_sunset(obj_world):
    def setup(self):
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
        self.staticactor.addpart( 'img1', draw.obj_image('tree',(1029,449),scale=0.5) )
        self.staticactor.addpart( 'img2', draw.obj_image('tree',(81,434),scale=0.5) )
        self.staticactor.addpart( 'img3', draw.obj_image('horizon',(640,720-150),path='premade') )
        self.staticactor.addpart( 'img4', draw.obj_image('house',(296,443),scale=0.5) )
        self.staticactor.addpart( 'img5', draw.obj_image('tree',(826,466),scale=0.5) )
        self.staticactor.addpart( 'img6', draw.obj_image('tree',(671,590),scale=0.5) )
        self.staticactor.addpart( 'img7', draw.obj_image('tree',(441,642),scale=0.5) )
        self.staticactor.addpart( 'img8', draw.obj_image('tree',(116,584),scale=0.5) )
        # start actor
        self.startactor.addpart( 'img1', draw.obj_image('sun',(660,270),scale=0.5) )
        # ungoing actor
        animation1=draw.obj_animation('ch2_sunset','sun',(640,360))
        animation1.addimage('moon')
        self.ungoingactor.addpart( 'anim1', animation1 )
        # finish actor
        self.finishactor.addpart( 'img1', draw.obj_image('moon',(660,270),scale=0.5) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [S] to lower the sun',(1000,620),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Nighty Night!',(1000,620)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(80)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
    def triggerungoing(self,controls):
        return controls.s and controls.sc
    def triggerstart(self,controls):
        return not controls.s
    def update(self,controls):
        super().update(controls)
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
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame

####################################################################################################################

# Mini Game: go to bed
class obj_world_gotobed(obj_world):
    def setup(self,**kwargs):
        # default options
        self.partner=False
        # scene tuning
        if kwargs is not None:
            if 'partner' in kwargs: self.partner=kwargs["partner"]# partner options
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
        # start actor
        if self.partner == 'inlove':# add partner in love
            self.startactor.addpart( 'animadd1', draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )
        self.startactor.addpart( 'anim1', draw.obj_animation('ch1_awaken','herobase',(640,360),scale=0.7) )
        # ungoing actor
        if self.partner == 'inlove':# add partner in love
            self.ungoingactor.addpart( 'animadd1', draw.obj_animation('ch1_herotosleep','partnerbase',(640+100,360),scale=0.7) )
        self.ungoingactor.addpart( 'anim1', draw.obj_animation('ch1_herotosleep','herobase',(640,360),scale=0.7) )
        # finish actor
        if self.partner == 'inlove':# add partner in love
            self.finishactor.addpart( 'imgadd1', draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        self.finishactor.addpart( 'img1', draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        # text
        self.text_undone.addpart( 'text1', draw.obj_textbox('Hold [A] to go to Sleep',(1100,480),color=share.colors.instructions) )
        self.text_done.addpart( 'text1', draw.obj_textbox('Sweet Dreams!',(1100,480)) )
        # timer for ungoing part
        self.timer=tool.obj_timer(80)# ungoing part
        self.timerend=tool.obj_timer(80)# goal to done
    def triggerungoing(self,controls):
        return controls.a and controls.ac
    def triggerstart(self,controls):
        return not controls.a
    def update(self,controls):
        super().update(controls)
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
                    if self.partner == 'inlove':
                        self.ungoingactor.dict["animadd1"].rewind()
            else:
                # ungoing substate
                self.timer.update()
                if self.triggerstart(controls):# flip to start
                    self.ungoing=False
                    self.startactor.show=True
                    self.ungoingactor.show=False
                    self.finishactor.show=False
                    self.startactor.dict["anim1"].rewind()
                    if self.partner == 'inlove':
                        self.startactor.dict["animadd1"].rewind()
                if self.timer.ring:# flip to goal reached
                    self.goal=True
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
