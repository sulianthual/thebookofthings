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
        share.scenemanager.switchscene(obj_scene_ch2p4())
        
        


## skipped two pages

# draw walls
class obj_scene_ch2p4(page.obj_chapterpage):
    def setup(self):         
        self.text=['Inside ',('{housename}',share.colors.house),' there were walls and they looked like this. ',\
                   'There were common walls that would be found elsewhere too. ',\
                   ]
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format        
        self.drawlist=[]
        self.drawlist.append(draw.obj_drawing('wall_west',(50,360)))
        self.drawlist.append(draw.obj_drawing('wall_east',(1280-50,360)))
        self.drawlist.append(draw.obj_drawing('wall_south',(640,720-50)))
        self.drawlist.append(draw.obj_drawing('wall_north',(640,50)))
        for i in self.drawlist: 
            i.brush.makebrush(share.brushes.smallpen)
            self.addpart( i )               
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(240,560-60+40),scale=0.25) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(240,560-60),scale=0.25) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())



# draw door
class obj_scene_ch2p1(page.obj_chapterpage):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house ",\
                   ('{housename}',share.colors.house),' had a door. '\
                   'It was a common door that would be found elsewhere too. '
                   'It would open when ',('{heroname}',share.colors.hero), ' entered, '\
                   'and close the rest of the time. ',\
                   ]
        # 
        self.addpart( draw.obj_drawing('door_closed',(340,460),legend='Door Closed') )
        self.addpart( draw.obj_drawing('door_open',(940,460),legend='Door Open') )
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(640,460-60+160)) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(640,460-60)) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())


# entrance, access first room
class obj_scene_ch2p5(page.obj_chapterpage):
    def setup(self):         
        self.text=[\
                   'To enter a regular door the hero would knock on it then stand by it. ',\
                   ]
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150,'fontsize':'small'}# change text format        
        self.addpart(draw.obj_image('wall_west',(50,360)))
        self.addpart(draw.obj_image('wall_east',(1280-50,360)))
        self.addpart(draw.obj_image('wall_south',(640,720-50)))
        self.addpart(draw.obj_image('wall_north',(640,50))) 
 
        #
        self.world=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(self.world,bounds=(100,1280-100,100-50,720-100-50))
        door=actor.obj_actor_door(self.world,(940,360),scale=0.5)
        hero=actor.obj_actor_hero_v4(self.world,(340,360),scale=0.5)
        self.goal=actor.obj_actor_goal_opendoor(self.world,(hero,door),timer=20)
    def page(self,controls):
        self.world.update(controls)
    def callnextpage(self,controls):# must reach goal
        if self.goal.reached or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page   
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
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
        self.addpart(draw.obj_image('wall_west',(50,360)))
        self.addpart(draw.obj_image('wall_east',(1280-50,360)))
        self.addpart(draw.obj_image('wall_south',(640,720-50)))
        self.addpart(draw.obj_image('wall_north',(640,50))) 
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
        self.addpart(draw.obj_image('wall_west',(50,360)))
        self.addpart(draw.obj_image('wall_east',(1280-50,360)))
        self.addpart(draw.obj_image('wall_south',(640,720-50)))
        self.addpart(draw.obj_image('wall_north',(640,50))) 
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
        
        