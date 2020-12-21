#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# chapter1.py: the hero
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

# Chapter I: The Hero
# *CHAPTER I

# Notes on the Hero:
# Proportions: 360x200 for head, for body, for legs, with 160 vertical spacing (40 overlap) between each
# head draws over body, body draws over legs
# 
class obj_scene_chapter1(utils.obj_page):
    def setup(self):
        self.text=['-----   Chapter I: The Hero   -----   ',\
                   '\nOnce upon a time in the book of things, there was a ',('hero',share.colors.hero),' ',\
                   'that was going to do a lot of things. ',\
                   'The ',('hero',share.colors.hero),' was to be named using the [KEYBOARD]. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_textbox("The Hero\'s Name was:",(200,360)) )
        self.addpart( draw.obj_textinput('heroname',25,(750,360),color=share.colors.hero, legend='Hero Name') )
        self.addpart( draw.obj_textbox('and the hero was:',(180,560)) )
        textchoice=draw.obj_textchoice('hero_he')
        textchoice.addchoice('1. A guy','he',(440,560))
        textchoice.addchoice('2. A girl','she',(740,560))
        textchoice.addchoice('3. A thing','it',(1040,560))
        textchoice.addkey('hero_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('hero_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p1(self.creator)# next scene
        


class obj_scene_ch1p1(utils.obj_page):
    def setup(self):         
        self.text=['In the beginning, ',('{heroname}',share.colors.hero),\
                   ' the hero was only a mere pair of legs because ',('{hero_he}',share.colors.hero),' was built from the ground up.',\
                   'When standing, ',('{heroname}',share.colors.hero),"\'s ",'legs, facing slightly to the right, looked like this [draw]. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_drawing('herolegs_stand',(640,360), legend='Hero Legs (Standing)') )
    def prevpage(self):
        self.creator.scene=obj_scene_chapter1(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p2(self.creator)# next scene  


class obj_scene_ch1p2(utils.obj_page):
    def setup(self):         
        self.text=['and when going to the right, ',('{heroname}',share.colors.hero),"\'s legs looked like this [draw].",\
                           'When put together, this was how ',('{heroname}',share.colors.hero),' walked. [Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_image('herolegs_stand',(340,360))  ) 
        self.addpart( draw.obj_drawing('herolegs_walk',(940,360),legend='Hero Legs (Walking)') )
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p1(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p3(self.creator)# next scene 
                     

class obj_scene_ch1p3(utils.obj_page):
    def setup(self):       
        self.text=['the legs of ',('{heroname}',share.colors.hero),' could walk around with the [arrows] or [WASD] keys.',\
                   'It was a little weird but it worked just fine. [Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        hero=actor.obj_actor_hero_v1(self.world,(640,360))# Hero in world
        hero.addpart("instructions",draw.obj_textbox('Move with [arrows] or [WASD]',(640,680),fontsize='large'))
        hero.scale(0.5)# scale actor hero
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p2(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p4(self.creator)  
            
        
class obj_scene_ch1p4(utils.obj_page):
    def setup(self):       
        self.text=['Soon ',('{heroname}',share.colors.hero),' remembered ',\
                   ('{hero_he}',share.colors.hero),' had forgotten ',('{hero_his}',share.colors.hero),' head somewhere. ',\
            ('{heroname}',share.colors.hero),"\'s head, facing slightly to the right, looked like this, ",\
            'and',('{hero_he}',share.colors.hero),' could sometimes be very happy or angry.',\
            '[Tab: Back]   [Enter: Continue]',\
            '\n\nIt was easier to first draw the head contours then draw all the faces on top of it. ']

        drawing=draw.obj_drawing('herohead_contours',(190,460),legend='Head Contours')
        self.addpart( drawing )
        self.addpart( draw.obj_drawing('herohead',(490,460),base=drawing,legend='Normal Face') )
        self.addpart( draw.obj_drawing('herohead_happy',(790,460),base=drawing,legend='Happy Face') )
        self.addpart( draw.obj_drawing('herohead_angry',(1090,460),base=drawing,legend='Angry Face') )
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p3(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p5(self.creator)# next scene   


class obj_scene_ch1p5(utils.obj_page):
    def setup(self):       
        self.text=['The head and legs attached together. They could walk with the [arrows] or [WASD] keys.',\
                           ('{heroname}',share.colors.hero),' was wondering why he had only a head and legs. It annoyed him.',\
                               'But he also felt it was less to carry around and that was still good. ',\
                                   '[Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        hero=actor.obj_actor_hero_v2(self.world,(640,360))  # Hero in world   
        hero.addpart("instructions",draw.obj_textbox('Move with [arrows] or [WASD]',(640,680),fontsize='large'))
        hero.scale(0.5)# scale actor hero
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p4(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p6(self.creator)   
                        

class obj_scene_ch1p6(utils.obj_page):
    def setup(self):       
        self.text=[('{heroname}',share.colors.hero),' had a ',('favorite thing',share.colors.itemloved),' in the world',\
            ' and a ',('most hated thing',share.colors.itemhated),' in the world. ',\
            'These things were called like this [Write] and they looked like this [Draw]. ',\
            '\n[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_drawing('herothings_loved',(340,460),legend='Favorite Thing') )
        self.addpart( draw.obj_drawing('herothings_hated',(940,460),legend='Hated Thing') )
        self.addpart( draw.obj_textinput('itemloved',15,(340,260),color=share.colors.itemloved,legend='Favorite Thing Name') )
        self.addpart( draw.obj_textinput('itemhated',15,(940,260),color=share.colors.itemhated,legend='Hated Thing Name') )
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p5(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p7(self.creator)# next scene 


class obj_scene_ch1p7(utils.obj_page):
    def setup(self):        
        self.text=[('{heroname}',share.colors.hero), ' could walk with the [arrows] or [WASD] keys.',\
                   'Collecting ',('{itemloved}',share.colors.itemloved),\
                   ' that was his favorite thing made him very happy. ',\
                   'But seeing ',('{itemhated}',share.colors.itemhated),\
                   ' that was his most hated thing made him very angry [Tab: Back]   [Enter: Continue]']        
        self.world=actor.obj_world_v2(self)# world with hero/item pickup interactions
        hero=actor.obj_actor_hero_v3(self.world,(640,360),scale=0.5)# Hero in world
        for i in [150,250,350,450]:
            for j in [350,450,550]:
                term=actor.obj_actor_item_loved(self.world,(i,j))
                term.scale(0.5)
                term=actor.obj_actor_item_hated(self.world,(1280-i,j))
                term.scale(0.5)
    def page(self,controls):           
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p6(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p8(self.creator) 

        
class obj_scene_ch1p8(utils.obj_page):
    def setup(self):        
        self.text=[('{heroname}',share.colors.hero),' was a fierce fighter. ',\
            ('{hero_his}',share.colors.hero),' ',('weapon',share.colors.weapon),\
            ' could strike things to the right like this [Draw]. '\
            'When destroyed things would leave behind a trail of ',('smoke',share.colors.weapon),'. '\
            '[Tab: Back]   [Enter: Continue]']
        self.addpart( draw.obj_drawing('herostrike',(480,490),legend='Weapon Strike') )
        self.addpart( draw.obj_drawing('smoke',(880,490),legend='Smoke') )
        self.addpart( draw.obj_image('herohead_angry',(240-100,410)) )
        self.addpart( draw.obj_image('herolegs_stand',(240-100,570)) )
        self.addpart( draw.obj_textinput('weaponname',25,(650,260),color=share.colors.hero,legend='Weapon Name') )
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p7(self.creator)
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p9(self.creator)# next scene 
        
        
class obj_scene_ch1p9(utils.obj_page):
    def setup(self):        
        self.text=['With ',('{hero_his}',share.colors.hero),' weapon ',('{weaponname}',share.colors.weapon),', ',\
                   ('{heroname}',share.colors.hero),' could strike in the direction ',('{hero_he}',share.colors.hero),\
                   ' was facing, by using [Left Mouse] or [Space]. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v3(self)
        hero=actor.obj_actor_hero_v4(self.world,(640,360))
        hero.addpart("instructions", draw.obj_textbox('Strike with [Left Mouse] or [Space]',(640,680)) )
        hero.scale(0.5)# scale actor hero
        for i in [150,350]:
            for j in [200,400,600]:
                term=actor.obj_actor_item_loved(self.world,(i,j),scale=0.5)
                term=actor.obj_actor_item_hated(self.world,(1280-i,j),scale=0.5)# 
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p8(self.creator) 
    def nextpage(self): 
        self.creator.scene=obj_scene_ch1p10(self.creator)# next scene
            
class obj_scene_ch1p10(utils.obj_page):
    def setup(self):        
        self.text=['That was what, in the book of things, ',('{heroname}',share.colors.hero),' the hero was, ',\
                   'and ',('{heroname}',share.colors.hero),' the hero was going to do a lot of things in the book of things. '
                   '\n[Tab: Back]   [Enter: Continue]']
        animation=draw.obj_animation('herozoom','herohead',(640,360))# head anim
        animation.addimage('herohead_happy')
        self.addpart( animation )
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p9(self.creator) 
    def nextpage(self): 
        share.savefile.chapter=max(share.savefile.chapter,2)# update progress to chapter 2
        share.savefile.save()# save progress in file
        super().nextpage()