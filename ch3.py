#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter3.py: critters
#
##########################################################
###########################################################

import share
import tool
import draw
import page
import actor
import world

##########################################################
##########################################################

# Chapter III: Critters
# *CHAPTER III

# name house
class obj_scene_chapter3(page.obj_chapterpage):
    def setup(self):
        self.text=['-----   Chapter III: Critters   -----   ',\
                   '\nIn the book of things, ',('{heroname}',share.colors.hero),' that lived in a house, '\
                   'was creating critters in his laboratory. There would be many critters to do. ',\
                   ]
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())



class obj_scene_ch3p1(page.obj_chapterpage):
    def setup(self):
        self.text=['The first critter looked like this when facing right. ',\
                   'When alerted, it would get very angry and throw something. ',\
                   ]
        self.addpart( draw.obj_textinput('critterspitname',25,(640,220),color=share.colors.hero, legend='Critter Name') )
        self.addpart( draw.obj_drawing('critterspit',(200,500),legend='Critter'))#,shadow=(150,150)) )
        self.addpart( draw.obj_drawing('alert',(450,350),legend='Alert',shadow=(50,50)) )
        self.addpart( draw.obj_drawing('critterspit_strike',(800,500),legend='Angry Critter'))#,shadow=(150,150)) )
        self.addpart( draw.obj_drawing('critterspit_spit',(1100,500),legend='Throw'))#,shadow=(100,100)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())


class obj_scene_ch3p2(page.obj_chapterpage):
    def setup(self):
        self.text=['Most of the time, the critters would leave ',('{heroname}',share.colors.hero),' alone. ',\
                   'But if ',('{hero_he}',share.colors.hero),' got too close, ',\
                   'then the critters would throw and throw at ',('{hero_him}',share.colors.hero),'. ',\
                   'Luckily, ',('{heroname}',share.colors.hero),'could hit the critters several time with ',\
                  ('{weaponname}',share.colors.weapon),' until they vanished. ',\
                   ('{hero_he}',share.colors.hero),' needed to do so to exit the room. '
                   ]

        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format
        self.addpart( draw.obj_image('wall_ext',(50,360),fliph=True) )
        self.addpart( draw.obj_image('wall_ext',(1280-50,360)) )
        self.addpart( draw.obj_image('wall_ext',(100+270,50),rotate=90) )
        self.addpart( draw.obj_image('wall_ext',(1280-100-270,50),rotate=90,fliph=True) )
        self.addpart( draw.obj_image('wall_ext',(100+270,720-50),rotate=90,flipv=True) )
        self.addpart( draw.obj_image('wall_ext',(1280-100-270,720-50),rotate=90,fliph=True,flipv=True) )
        self.addpart( draw.obj_image('wall_corner',(50,50),fliphv=True) )
        self.addpart( draw.obj_image('wall_corner',(1280-50,50),flipv=True) )
        self.addpart( draw.obj_image('wall_corner',(50,720-50),fliph=True) )
        self.addpart( draw.obj_image('wall_corner',(1280-50,720-50)) )
        textbox=draw.obj_textbox('Exit',(1280-120,360),fontsize='small')
        textbox.rotate90(-90)
        self.addpart(textbox)
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww,bounds=(50,1280-50,100,720-100))
        door=actor.obj_actor_door(ww,(1280-50,360),scale=0.25)
        door.rotate90(-90)
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.5)
        self.goaldoor=actor.obj_actor_goal_opendoor(ww,(hero,door),timer=20)
        self.goalkill=actor.obj_actor_goal_alldead(ww)# all critters must be dead
        critter=actor.obj_actor_critterspit(ww,(940,360),scale=0.5 )
        self.goalkill.addactor(critter)
        self.addpart( ww )
    def callnextpage(self,controls):# must reach goal
        if (self.goalkill.reached and self.goaldoor.reached) or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())


class obj_scene_ch3p3(page.obj_chapterpage):
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),\
                   'needed to clear the room to progress. '
                   ]

        self.textkeys={'pos':(150,5),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format
        self.addpart( draw.obj_image('wall_ext',(50,360),fliph=True) )
        self.addpart( draw.obj_image('wall_ext',(1280-50,360)) )
        self.addpart( draw.obj_image('wall_ext',(100+270,50),rotate=90) )
        self.addpart( draw.obj_image('wall_ext',(1280-100-270,50),rotate=90,fliph=True) )
        self.addpart( draw.obj_image('wall_ext',(100+270,720-50),rotate=90,flipv=True) )
        self.addpart( draw.obj_image('wall_ext',(1280-100-270,720-50),rotate=90,fliph=True,flipv=True) )
        self.addpart( draw.obj_image('wall_corner',(50,50),fliphv=True) )
        self.addpart( draw.obj_image('wall_corner',(1280-50,50),flipv=True) )
        self.addpart( draw.obj_image('wall_corner',(50,720-50),fliph=True) )
        self.addpart( draw.obj_image('wall_corner',(1280-50,720-50)) )
        textbox=draw.obj_textbox('Exit',(1280-120,360),fontsize='small')
        textbox.rotate90(-90)
        self.addpart(textbox)
        #
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww,bounds=(50,1280-50,100,720-100))
        door=actor.obj_actor_door(ww,(1280-50,360),scale=0.25)
        door.rotate90(-90)
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.25)
        self.goaldoor=actor.obj_actor_goal_opendoor(ww,(hero,door),timer=20)
        self.goalkill=actor.obj_actor_goal_alldead(ww)# all critters must be dead
        for i in range(7):
            critter=actor.obj_actor_critterspit(ww,(tool.randint(100,1180),tool.randint(100,620)),scale=0.25 )
            self.goalkill.addactor(critter)
        self.addpart( ww )
    def callnextpage(self,controls):# must reach goal
        if (self.goalkill.reached and self.goaldoor.reached) or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch2p11())
