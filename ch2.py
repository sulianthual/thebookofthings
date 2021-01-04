#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter2.py: a house
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

# Chapter II: A House
# *CHAPTER II

# name house
class obj_scene_chapter2(page.obj_chapterpage):
    def setup(self):
        self.text=['-----   Chapter II: A House   -----   ',\
                   '\nIn the book of things, ',('{heroname}',share.colors.hero),' lived in a house, '\
                   'and there would be a lot of things to do in that house. ',\
                   'The ',('house',share.colors.house),' was to be named using the [KEYBOARD].',\
                   ]
        self.addpart( draw.obj_textinput('housename',25,(650,360),color=share.colors.house,legend='House Name') )
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())



# draw door
class obj_scene_ch2p1(page.obj_chapterpage):
    def setup(self):
        self.text=['To build ',('{heroname}',share.colors.hero),"\'s house ",\
                   ('{housename}',share.colors.house),', one first needed doors. ',\
                   'Doors that could be opened by ',('{heroname}',share.colors.hero),', ',\
                   'that could be closed, and that could be locked with keys. ',\
                   ]
        #
        self.addpart( draw.obj_drawing('door_closed',(240,460),legend='Door Closed') )
        self.addpart( draw.obj_drawing('door_open',(1040,460),legend='Door Open') )
        # self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(640,460-60+160)) )
        # self.addpart( draw.obj_animation('herohead_lookaround','herohead',(640,460-60)) )
        self.addpart( draw.obj_drawing('door_lock',(530,460),legend='Door Lock'))#,shadow=(100,100)) )
        self.addpart( draw.obj_drawing('door_key',(750,460),legend='Door Key'))#,shadow=(100,100)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())


# entrance, access first room
class obj_scene_ch2p2(page.obj_chapterpage):
    def setup(self):
        self.text=[\
                   'To enter a regular door, ',('{heroname}',share.colors.hero),\
                   ' would knock on it then stand just in front of it. ',\
                   ]
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format
        #
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww,bounds=(100,1280-100,100-50,720-100-50))
        door=actor.obj_actor_door(ww,(940,360),scale=0.5)
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.5)
        self.goal=actor.obj_actor_goal_opendoor(ww,(hero,door),timer=20)
        self.addpart( ww )

    def callnextpage(self,controls):# must reach goal
        if self.goal.reached or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())

# draw door lock
class obj_scene_ch2p3(page.obj_chapterpage):
    def setup(self):
        self.text=[\
                   'To enter a locked door, ',('{heroname}',share.colors.hero),\
                    ' would first have to find the key. ',\
                   ]
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format
        #
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww,bounds=(100,1280-100,100-50,720-100-50))
        door=actor.obj_actor_doorwithlock(ww,(940,360),scale=0.5)
        key=actor.obj_actor_doorkey(ww,(640,360),scale=0.5)
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.5)
        self.goal=actor.obj_actor_goal_opendoor(ww,(hero,door),timer=20)
        self.addpart( ww )
    def callnextpage(self,controls):# must reach goal
        if self.goal.reached or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())


## skipped two pages

# draw walls
class obj_scene_ch2p4(page.obj_chapterpage):
    def setup(self):
        self.text=['Next, to build ',('{housename}',share.colors.house),' some walls were needed. ',\
                   'Walls that would not be penetrated. And panels. And pots. ',\
                   ]
        drawing=draw.obj_drawing('wall_ext',(840,360),legend='Wall')#,shadow=(50,270))
        drawing.brush.makebrush(share.brushes.smallpen)
        self.addpart( drawing )
        drawing=draw.obj_drawing('wall_corner',(1040,360+270-50),legend='CornerStone')#,shadow=(50,50))
        drawing.brush.makebrush(share.brushes.smallpen)
        self.addpart( drawing )
        drawing=draw.obj_drawing('wall_in',(640,360+270-130),legend='Panel',shadow=(25,135))
        drawing.brush.makebrush(share.brushes.smallpen)
        self.addpart( drawing )
        drawing=draw.obj_drawing('pot',(340,360+270-100),legend='Pot')#,shadow=(100,100))
        self.addpart( drawing )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())

# room with walls
class obj_scene_ch2p5(page.obj_chapterpage):
    def setup(self):
        self.text=['Going through the rooms looked like this. ',\
                   ]
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
        #
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww,bounds=(100,1280-100,100-50,720-100-50))
        panel=actor.obj_actor_wall(ww,(640,360))
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.5)
        self.addpart( ww )

        #
        self.addpart( draw.obj_image('pot',(1280-100-50,100+50),scale=0.5) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())


class obj_scene_ch2p9(page.obj_chapterpage):
    def setup(self):
        self.text=['In the laboratory, ',('{heroname}',share.colors.hero),' studied critters. ',\
                   ('{hero_his}',share.colors.hero),' first critter looked like this when facing right. ',\
                   'When alerted, would get very angry and throw something. ',\
                   ]
        self.addpart( draw.obj_textinput('critterspitname',25,(640,220),color=share.colors.hero, legend='Critter Name') )
        self.addpart( draw.obj_drawing('critterspit',(200,500),legend='Critter'))#,shadow=(150,150)) )
        self.addpart( draw.obj_drawing('alert',(450,350),legend='Alert',shadow=(50,50)) )
        self.addpart( draw.obj_drawing('critterspit_strike',(800,500),legend='Angry Critter'))#,shadow=(150,150)) )
        self.addpart( draw.obj_drawing('critterspit_spit',(1100,500),legend='Throw'))#,shadow=(100,100)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())


class obj_scene_ch2p10(page.obj_chapterpage):
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
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())


class obj_scene_ch2p11(page.obj_chapterpage):
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
        share.scenemanager.switchscene(obj_scene_ch2p10())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch2p11())
