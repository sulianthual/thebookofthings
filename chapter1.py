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
                   '\nOnce upon a time in the book of things, there was a hero. He was going to do a lot of things.',\
                   'The Hero was to be named, and its name was to be written using the [KEYBOARD].',\
                   '\nThe ',('Hero Name',share.colors.input),' was:',
                   '\n \n[Tab: Back]   [Enter: Continue]']
        self.textinput1=draw.obj_textinput('heroname',25,(650,260),color=share.colors.hero)# input keyword, max characters, position
        self.textinput1.legend='Hero Name'
    def page(self,controls):
        self.textinput1.update(controls)
    def prevpage(self):
        share.words.save()# resave (entire) dictionary of words in file
        super().prevpage()
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p1(self.creator)# next scene
        share.words.save()# resave (entire) dictionary of words in file


class obj_scene_ch1p1(utils.obj_page):
    def setup(self):         
        self.text=['In the beginning, ',('{heroname}',share.colors.hero),' the Hero was only a mere pair of legs. He was built from the ground up.',\
                   'When standing, the legs, facing slightly to the right, looked like this [draw].',\
                           '\n[Tab: Back]   [Enter: Continue]']
        self.drawing=draw.obj_drawing('herolegs_stand',(640,360))# new drawing 
        self.drawing.legend='Hero Legs (Standing)'
    def page(self,controls):
        self.drawing.display()
        self.drawing.update(controls)      
    def prevpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_chapter1(self.creator)
    def nextpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_ch1p2(self.creator)# next scene  


class obj_scene_ch1p2(utils.obj_page):
    def setup(self):         
        self.text=['and when going to the right, the legs looked like this [draw].',\
                           'When put together, this was how ',('{heroname}',share.colors.hero),' walked. [Tab: Back]   [Enter: Continue]']
        self.image=draw.obj_image('herolegs_stand',(340,360))   
        self.drawing=draw.obj_drawing('herolegs_walk',(940,360))# new drawing  
        self.drawing.legend='Hero Legs (Walking)'
    def page(self,controls):
        self.drawing.display()
        self.drawing.update(controls)
        self.image.display()
    def prevpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_ch1p1(self.creator)
    def nextpage(self):
        self.drawing.finish()# save drawing
        self.creator.scene=obj_scene_ch1p3(self.creator)# next scene 
                     

class obj_scene_ch1p3(utils.obj_page):
    def setup(self):       
        self.text=['The heros legs could walk around with the [arrows] or [WASD] keys.',\
                           'It was a little weird but it worked just fine. [Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        self.hero=actor.obj_actor_hero_v1(self.world,(640,360))# Hero in world
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p2(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p4(self.creator)  
            
        
class obj_scene_ch1p4(utils.obj_page):
    def setup(self):       
        self.text=['Soon ',('{heroname}',share.colors.hero),' remembered he had forgotten his head somewhere. ',\
            'The hero head, facing slightly to the right, looked like this [Draw].',\
            'Sometimes, the hero was very happy, and sometimes very angry. [Draw].',\
                   '[Tab: Back]   [Enter: Continue]']
        self.drawing1=draw.obj_drawing('herohead',(340,460))
        self.drawing1.legend='Hero Head'
        self.drawing2=draw.obj_drawing('herohead_happy',(640,460))
        self.drawing2.legend='Happy'
        self.drawing3=draw.obj_drawing('herohead_angry',(940,460))
        self.drawing3.legend='Angry'
    def page(self,controls):
        for i in [self.drawing1, self.drawing2, self.drawing3]:
            i.display()
            i.update(controls)
    def prevpage(self):
        for i in [self.drawing1, self.drawing2, self.drawing3]: i.finish()
        self.creator.scene=obj_scene_ch1p3(self.creator)
    def nextpage(self):
        for i in [self.drawing1, self.drawing2, self.drawing3]: i.finish()
        self.creator.scene=obj_scene_ch1p5(self.creator)# next scene   


class obj_scene_ch1p5(utils.obj_page):
    def setup(self):       
        self.text=['The head and legs attached together. They could walk with the [arrows] or [WASD] keys.',\
                           ('{heroname}',share.colors.hero),' was wondering why he had only a head and legs. It annoyed him.',\
                               'But he also felt it was less to carry around and that was still good. ',\
                                   '[Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        self.hero=actor.obj_actor_hero_v2(self.world,(640,360))  # Hero in world   
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
        self.drawing1=draw.obj_drawing('herothings_loved',(340,460))
        self.drawing1.legend='Favorite Thing'
        self.drawing2=draw.obj_drawing('herothings_hated',(940,460))
        self.drawing2.legend='Hated Thing'
        self.textinput1=draw.obj_textinput('itemloved',15,(340,260),color=share.colors.itemloved)# input keyword, max characters, position
        self.textinput1.legend='Favorite Thing Name'
        self.textinput2=draw.obj_textinput('itemhated',15,(940,260),color=share.colors.itemhated)# input keyword, max characters, position
        self.textinput2.legend='Hated Thing Name'
    def page(self,controls):
        for i in [self.drawing1, self.drawing2]:
            i.display()
            i.update(controls)
        self.textinput1.update(controls)
        self.textinput2.update(controls)
    def prevpage(self):
        share.words.save()# resave (entire) dictionary of words in file
        for i in [self.drawing1, self.drawing2]: i.finish()
        self.creator.scene=obj_scene_ch1p5(self.creator)
    def nextpage(self):
        share.words.save()# resave (entire) dictionary of words in file
        for i in [self.drawing1, self.drawing2]: i.finish()
        self.creator.scene=obj_scene_ch1p7(self.creator)# next scene 


class obj_scene_ch1p7(utils.obj_page):
    def setup(self):        
        self.text=[('{heroname}',share.colors.hero), ' the hero could walk with the [arrows] or [WASD] keys.',\
                   'Collecting ',('{itemloved}',share.colors.itemloved),\
                   ' that was his favorite thing made him very happy. ',\
                   'But seeing ',('{itemhated}',share.colors.itemhated),\
                   ' that was his most hated thing made him very angry [Tab: Back]   [Enter: Continue]']        
        self.world=actor.obj_world_v2(self)# world with hero/item pickup interactions
        self.hero=actor.obj_actor_hero_v3(self.world,(640,360))# Hero in world
        # Place several loved and hated items
        for i in [150,250,350,450]:
            for j in [350,450,550]:
                term=actor.obj_actor_item_loved(self.world,(i,j))
                term=actor.obj_actor_item_hated(self.world,(1280-i,j))#      
    def page(self,controls):           
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p6(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p8(self.creator) 

        
class obj_scene_ch1p8(utils.obj_page):
    def setup(self):        
        self.text=[('{heroname}',share.colors.hero),' was a fierce fighter with his favorite ',('weapon',share.colors.weapon),', that could strike things. ',\
            'The ',('weapon',share.colors.weapon),' was called like this [Write], and ',\
            'when striking things to the right it looked like this [Draw].',\
            ' [Tab: Back]   [Enter: Continue]']
        self.drawing=draw.obj_drawing('herostrike',(680,490))
        self.drawing.legend='Weapon Strike'
        self.image1=draw.obj_image('herohead_angry',(440,410))
        self.image2=draw.obj_image('herolegs_stand',(440,570))
        self.textinput1=draw.obj_textinput('weaponname',25,(650,260),color=share.colors.hero)# input keyword, max characters, position
        self.textinput1.legend='Weapon Name'
    def page(self,controls):
        self.image2.display()
        self.image1.display()
        self.drawing.display()
        self.drawing.update(controls)
        self.textinput1.update(controls)
    def prevpage(self):
        self.drawing.finish()
        share.words.save()# resave (entire) dictionary of words in file
        self.creator.scene=obj_scene_ch1p7(self.creator)
    def nextpage(self):
        self.drawing.finish()
        share.words.save()# resave (entire) dictionary of words in file
        self.creator.scene=obj_scene_ch1p9(self.creator)# next scene 
        
        
class obj_scene_ch1p9(utils.obj_page):
    def setup(self):        
        self.text=['With his weapon ',('{weaponname}',share.colors.weapon),', ',\
                   ('{heroname}',share.colors.hero),' could strike in the direction he was facing, by using [Left Mouse]. ',\
                   '\nIt could break things like his most hated thing ',('{itemhated}',share.colors.itemhated),', which was cool, ',\
                   'but it could also break his favorite thing ',('{itemloved}',share.colors.itemloved),\
                   ', so it was important to be a little careful. [Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v3(self)# Build world (interactions sword items)
        self.hero=actor.obj_actor_hero_v4(self.world,(640,360))# Hero in world
        for i in [150,350]:
            for j in [400,600]:
                term=actor.obj_actor_item_loved(self.world,(i,j))
                term=actor.obj_actor_item_hated(self.world,(1280-i,j))#  
    def page(self,controls):
        #
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p8(self.creator) 
    # def nextpage(self):
    #     self.creator.scene=obj_scene_ch1p10(self.creator) 
            