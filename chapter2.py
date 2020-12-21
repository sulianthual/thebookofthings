#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# chapter2.py: a house
#
##########################################################
##########################################################

import sys
import os
import pygame
#
import share
import draw
import utils
import menu
import actor

##########################################################
##########################################################

# Chapter I: A House
# *CHAPTER II

# 
class obj_scene_chapter2(utils.obj_page):
    def setup(self):
        self.text=['-----   Chapter II: A House   -----   ',\
                   '\nIn the book of things, the Hero ',('{heroname}',share.colors.hero),' lived in a house, '\
                   'and there would be a lot of things to do in that house. ',\
                   'The ',('house',share.colors.house),' was to be named using the [KEYBOARD].',\
                   '[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_textinput('housename',25,(650,260),color=share.colors.house,legend='House Name') )
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p1(self.creator)# next scene
        
        
class obj_scene_ch2p1(utils.obj_page):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house, ",\
                   'that was named',('{housename}',share.colors.house),' had a door. '\
                   'It was a very common door, that could be found everywhere. '
                   'It would open when ',('{heroname}',share.colors.hero), ' entered, '\
                   'and close the rest of the time. ',\
                   '[Tab: Back]   [Enter: Continue]']
        # 
        self.addpart( draw.obj_drawing('housedoor_closed',(340,460),legend='Door Closed') )
        self.addpart( draw.obj_drawing('housedoor_open',(940,460),legend='Door Open') )
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(640,460-60+160)) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(640,460-60)) )
    def prevpage(self):
        self.creator.scene=obj_scene_chapter2(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p2(self.creator)# next scene  


class obj_scene_ch2p2(utils.obj_page):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house, ",\
                   'that was named',('{housename}',share.colors.house),\
                   'looked like this from the outside. ',\
                   '[Tab: Back]   [Enter: Continue]']
        drawing=draw.obj_drawing('house',(640,400),legend='House from outside')
        drawing.brush=share.brushes.smallpen# draw with smaller pen
        self.addpart( drawing )
        self.addpart( draw.obj_image('housedoor_closed',(640,500),scale=0.25) )
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(240,500+40),scale=0.25) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(240,500),scale=0.25) )
    def prevpage(self):
        self.creator.scene=obj_scene_ch2p1(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p3(self.creator)# next scene  

# hero opens door to enter house
class obj_scene_ch2p3(utils.obj_page):
    def setup(self):         
        self.text=['To enter ',('{housename}',share.colors.house),', ',\
                   ('{heroname}',share.colors.hero),' needed to knock with ',('{weaponname}',share.colors.weapon),\
                   ', then stand in front of the door. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_image('house',(640,400)) )
        self.world=actor.obj_world_v4(self)
        bdry=actor.obj_actor_bdry(self.world)# custom bdry
        bdry.bdry_lim=(50,1280-50,500,720-50)# split at midscreen
        door=actor.obj_actor_door(self.world,(640,500),scale=0.25)
        # some items (use middle mouse to quickly get mouse coordinates in dev mode)
        for i in [j+940+25 for j in [0,50,100,150,200,250]]:
            term=actor.obj_actor_item_loved(self.world,(i,500+40),scale=0.25)
        for i in [-j+340-25 for j in [150,200,250]]:
            term=actor.obj_actor_item_loved(self.world,(i,500+40),scale=0.25)
        hero=actor.obj_actor_hero_v4(self.world,(240,500),scale=0.25)# Hero in world
        self.goal=actor.obj_actor_goal_opendoor(self.world,(hero,door),timer=20)
    def callnextpage(self,controls):# must reach goal
        if self.goal.reached or (controls.enter and controls.enterc):
            share.ipage += 1
            self.nextpage()# switch to next page      
    def page(self,controls):        
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch2p2(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p4(self.creator)# next scene  

# first room of house, draw the walls
class obj_scene_ch2p4(utils.obj_page):
    def setup(self):         
        self.text=['Inside the house there were walls and they looked like this. ',\
                   'There were the same walls in all the rooms. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150}# change text format        
        self.drawlist=[]
        self.drawlist.append(draw.obj_drawing('housewall_west',(50,360)))
        self.drawlist.append(draw.obj_drawing('housewall_east',(1280-50,360)))
        self.drawlist.append(draw.obj_drawing('housewall_south',(640,720-50)))
        self.drawlist.append(draw.obj_drawing('housewall_northw',(740/2,50)))
        self.drawlist.append(draw.obj_drawing('housewall_northe',(1280-440/2,50)))
        for i in self.drawlist: 
            i.brush=share.brushes.smallpen
            self.addpart( i )        
        self.addpart( draw.obj_image('housedoor_closed',(790,50),scale=0.25) )
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(240,560-60+40),scale=0.25) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(240,560-60),scale=0.25) )
    def prevpage(self):
        self.creator.scene=obj_scene_ch2p3(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p5(self.creator)# next scene  


# entrance, access other doors
class obj_scene_ch2p5(utils.obj_page):
    def setup(self):         
        self.text=['The Entrance had doors to the house rooms...enter bedroom... ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150}# change text format        
        self.addpart(draw.obj_image('housewall_west',(50,360)))
        self.addpart(draw.obj_image('housewall_east',(1280-50,360)))
        self.addpart(draw.obj_image('housewall_south',(640,720-50)))
        self.addpart(draw.obj_image('housewall_northw',(740/2,50)))
        self.addpart(draw.obj_image('housewall_northe',(1280-440/2,50)))  
        self.addpart(draw.obj_image('housewall_northe',(1280-440/2,50)))  
        self.world=actor.obj_world(self)
        self.world.addrule('rule_world_bdry', actor.obj_rule_world_bdry(self.world))# bdry rule
        self.world.addrule('rule_weapon_door', actor.obj_rule_weapon_opens_door(self.world))# door rule
        bdry=actor.obj_actor_bdry(self.world)# custom bdry
        bdry.bdry_lim=(100,1280-100,100-50,720-100-50)
        # outside fake door
        self.addpart( draw.obj_image('housedoor_closed',(790,50),scale=0.25) )
        self.addpart( draw.obj_textbox('Outside',(790,50+70),fontsize='small') )
        # fake doors
        for i in [540,740,940]:
            self.addpart( draw.obj_image('housedoor_closed',(i,460),scale=0.25) )
        # door to open
        door=actor.obj_actor_door(self.world,(340,460),scale=0.25)
        self.addpart( draw.obj_textbox('Bedroom',(340,460-70),fontsize='small') )    
        hero=actor.obj_actor_hero_v4(self.world,(240,680),scale=0.25)
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch2p4(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch2p6(self.creator)# next scene  




# first room of house, draw the walls
class obj_scene_ch2p6(utils.obj_page):
    def setup(self):         
        self.text=['Bedroom...draw 3 furnitures (can be pushed around), will reappear... ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.textkeys={'pos':(150,150),'xmin':150,'xmax':1280-150}
        #
        self.addpart( draw.obj_drawing('housewall_west',(50,360)) ) 

    def prevpage(self):
        self.creator.scene=obj_scene_ch2p5(self.creator)
    # def nextpage(self):
    #     self.creator.scene=obj_scene_ch2p7(self.creator)# next scene  











