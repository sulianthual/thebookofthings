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
        self.textinput1.makelegend('Hero Name')
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
        self.drawing.makelegend('Hero Legs (Standing)')
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
        self.drawing.makelegend('Hero Legs (Walking)')
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
        self.text=['the legs of ',('{heroname}',share.colors.hero),' could walk around with the [arrows] or [WASD] keys.',\
                   'It was a little weird but it worked just fine. [Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        self.hero=actor.obj_actor_hero_v1(self.world,(640,360))# Hero in world
        self.textbox=draw.obj_textbox('Move with [arrows] or [WASD]',(640,680),fontsize='large')
        self.hero.addpart("instructions",self.textbox)
        self.hero.scale(0.5)# scale actor hero
    def page(self,controls):
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p2(self.creator) 
    def nextpage(self):
        self.creator.scene=obj_scene_ch1p4(self.creator)  
            
        
class obj_scene_ch1p4(utils.obj_page):
    def setup(self):       
        self.text=['Soon ',('{heroname}',share.colors.hero),' remembered he had forgotten his head somewhere. ',\
            'The hero head, facing slightly to the right, looked like this, ',\
            'and was sometimes very happy or angry.',\
            '\n\nIt was easier to first draw the head contours then draw all the faces. ',\
                   '\n[Tab: Back]   [Enter: Continue]']
        self.drawing0=draw.obj_drawing('herohead_contours',(190,460))
        self.drawing0.makelegend('Head Contours')  
        self.drawing1=draw.obj_drawing('herohead',(490,460),base=self.drawing0)
        self.drawing1.makelegend('Normal Face')
        self.drawing2=draw.obj_drawing('herohead_happy',(790,460),base=self.drawing0)
        self.drawing2.makelegend('Happy Face')
        self.drawing3=draw.obj_drawing('herohead_angry',(1090,460),base=self.drawing0)
        self.drawing3.makelegend('Angry Face')
        self.drawlist=[self.drawing0,self.drawing1, self.drawing2, self.drawing3]
    def page(self,controls):
        for i in self.drawlist:
            i.display()
            i.update(controls)
    def prevpage(self):
        for i in self.drawlist: i.finish()
        self.creator.scene=obj_scene_ch1p3(self.creator)
    def nextpage(self):
        for i in self.drawlist: i.finish()
        self.creator.scene=obj_scene_ch1p5(self.creator)# next scene   


class obj_scene_ch1p5(utils.obj_page):
    def setup(self):       
        self.text=['The head and legs attached together. They could walk with the [arrows] or [WASD] keys.',\
                           ('{heroname}',share.colors.hero),' was wondering why he had only a head and legs. It annoyed him.',\
                               'But he also felt it was less to carry around and that was still good. ',\
                                   '[Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v1(self)# Build world
        self.hero=actor.obj_actor_hero_v2(self.world,(640,360))  # Hero in world   
        self.textbox=draw.obj_textbox('Move with [arrows] or [WASD]',(640,680),fontsize='large')
        self.hero.addpart("instructions",self.textbox)
        self.hero.scale(0.5)# scale actor hero
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
        self.drawing1.makelegend('Favorite Thing')
        self.drawing2=draw.obj_drawing('herothings_hated',(940,460))
        self.drawing2.makelegend('Hated Thing')
        self.textinput1=draw.obj_textinput('itemloved',15,(340,260),color=share.colors.itemloved)# input keyword, max characters, position
        self.textinput1.makelegend('Favorite Thing Name')
        self.textinput2=draw.obj_textinput('itemhated',15,(940,260),color=share.colors.itemhated)# input keyword, max characters, position
        self.textinput2.makelegend('Hated Thing Name')
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
        self.hero.scale(0.5)# scale actor hero
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
        self.text=[('{heroname}',share.colors.hero),' was a fierce fighter. ',\
            'His ',('weapon',share.colors.weapon),' could strike things to the right like this [Draw]. '\
            ' When destroyed things would leave behind a trail of ',('smoke',share.colors.weapon),'. '\
            ' [Tab: Back]   [Enter: Continue]']
        self.drawing=draw.obj_drawing('herostrike',(480,490))
        self.drawing.makelegend('Weapon Strike')
        self.drawing2=draw.obj_drawing('smoke',(880,490))
        self.drawing2.makelegend('Smoke')

        self.image1=draw.obj_image('herohead_angry',(240,410))
        self.image2=draw.obj_image('herolegs_stand',(240,570))
        self.textinput1=draw.obj_textinput('weaponname',25,(650,260),color=share.colors.hero)# input keyword, max characters, position
        self.textinput1.makelegend('Weapon Name')
    def page(self,controls):
        self.image2.display()
        self.image1.display()
        for i in [self.drawing,self.drawing2]:
            i.display()
            i.update(controls)
        self.textinput1.update(controls)
    def prevpage(self):
        for i in [self.drawing,self.drawing2]: i.finish()
        share.words.save()# resave (entire) dictionary of words in file
        self.creator.scene=obj_scene_ch1p7(self.creator)
    def nextpage(self):
        for i in [self.drawing,self.drawing2]: i.finish()
        share.words.save()# resave (entire) dictionary of words in file
        self.creator.scene=obj_scene_ch1p9(self.creator)# next scene 
        
        
class obj_scene_ch1p9(utils.obj_page):
    def setup(self):        
        self.text=['With his weapon ',('{weaponname}',share.colors.weapon),', ',\
                   ('{heroname}',share.colors.hero),' could strike in the direction he was facing, by using [Left Mouse] or [Space]. ',\
                   '[Tab: Back]   [Enter: Continue]']
        self.world=actor.obj_world_v3(self)# Build world (interactions sword items)
        self.hero=actor.obj_actor_hero_v4(self.world,(640,360))# Hero in world
        self.textbox=draw.obj_textbox('Strike with [Left Mouse] or [Space]',(640,680),fontsize='huge')
        self.hero.addpart("instructions",self.textbox)
        self.hero.scale(0.25)# scale actor hero
        for i in [150,350]:
            for j in [200,400,600]:
                term=actor.obj_actor_item_loved(self.world,(i,j))
                term=actor.obj_actor_item_hated(self.world,(1280-i,j))#  
    def page(self,controls):
        #
        self.world.update(controls)
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p8(self.creator) 
    def nextpage(self): 
        self.creator.scene=obj_scene_ch1p10(self.creator)# next scene
            
class obj_scene_ch1p10(utils.obj_page):
    def setup(self):        
        self.text=['That was what, in the book of things, the hero ',('{heroname}',share.colors.hero),' was, ',\
                   'and ',('{heroname}',share.colors.hero),' the hero was going to do a lot of things in the book of things. '
                   '\n[Tab: Back]   [Enter: Continue]']
        self.animation1=draw.obj_animation('herozoom','herohead',(640,360))# head anim
        self.animation1.addimage('herohead_happy')# 
    def page(self,controls):
        self.animation1.update(controls)# used when recording anim
    def prevpage(self):
        self.creator.scene=obj_scene_ch1p9(self.creator) 
    def nextpage(self): 
        share.savefile.chapter=max(share.savefile.chapter,2)# update progress to chapter 2
        share.savefile.save()# save progress in file
        super().nextpage()