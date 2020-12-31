#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# ideas.py: menu with some ideas
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

# Test Menu
class obj_scene_ideamenu(page.obj_page):
    def __init__(self):
        super().__init__()
    def setup(self):
        super().setup() 
        share.ipage=1# current page number in chapter    
        self.nrow=17# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Appendix Ideas [Enter: Read] [Tab: Back]',(640,50),fontsize='medium'))
        self.addpart(draw.obj_textbox('[Esc: Main Menu]',(1120,700),fontsize='smaller'))
        for i,test in enumerate(self.list[:self.nrow-1]):
            self.addpart(draw.obj_textbox(test.name,(250,130+i*30),fontsize='smaller'))
        for i,test in enumerate(self.list[self.nrow-1:]):
            self.addpart(draw.obj_textbox(test.name,(640,130+i*30),fontsize='smaller'))            
        self.sprite_pointer=draw.obj_textbox('---',(640,360),fontsize='smaller')# moved around
        self.addpart(self.sprite_pointer)                
    def page(self,controls):
        if share.iidea<self.nrow-1:
            self.sprite_pointer.movetox(60)
            self.sprite_pointer.movetoy(130+share.iidea*30)
        else:
            self.sprite_pointer.movetox(460)
            self.sprite_pointer.movetoy(130+(share.iidea-self.nrow+1)*30)
        if (controls.s and controls.sc) or (controls.down and controls.downc): 
            share.iidea += 1
            if share.iidea == self.listlen: share.iidea=0
        if (controls.w and controls.wc) or (controls.up and controls.upc): 
            share.iidea -= 1
            if share.iidea == -1: share.iidea=self.listlen-1
        if (controls.enter and controls.enterc):
            share.scenemanager.switchscene(self.list[share.iidea],init=True)
        if controls.esc and controls.escc: 
            share.scenemanager.switchscene(share.titlescreen)            
            
    def loadtests(self):# load all tests 
        # developper

        self.list.append(obj_scene_idea4()) 

        self.list.append(obj_scene_ideatodo())    
        self.list.append(obj_scene_idea1())    
        self.list.append(obj_scene_idea2())     
        self.list.append(obj_scene_idea3())    
   
        self.list.append(obj_scene_idea5())    
        self.list.append(obj_scene_idea6())    
        self.list.append(obj_scene_idea7())    
        self.list.append(obj_scene_idea8())    
        self.list.append(obj_scene_idea9())    
        self.list.append(obj_scene_idea10()) 
        #
        self.listlen=len(self.list)


# Template for test page = chapter page with slightly modified functionalities
class obj_ideapage(page.obj_chapterpage):
    def __init__(self):
        self.name='Unamed'# needs name to display on test menu
        super().__init__()
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_ideamenu())
    def exitpage(self):
        share.scenemanager.switchscene(obj_scene_ideamenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_ideamenu())  

#########################################################################
#########################################################################

class obj_scene_ideatodo(obj_ideapage):
    def setup(self):       
        self.name='Todo List'  
        self.text=['Todo List:',\
                   '\nx) Hero house=museum (artifact recurrent in world), laboratory (critters reccurent in world), no bedroom, no outside view. ',\
                   '\nx) Allow hero to strike up or down (but only face left or right)',\
                   '\nx) Make custom critters in the lab: use classmethods to build from template what methods they have',\
                   '\nx) Game now supports 60,30 or 20 fps but many movement (based on 60 fps) becomes incorrect. ',\
                   'Correct this eventually (look at movex,movey, obj_timer, share.dtf..., animation load and save). ',\
                   '\nx) split actor file into multiple files ',\
                   '\nx)',\
                   '\nx)',\
                   '\nx)',\
                   ] 
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting

class obj_scene_idea1(obj_ideapage):
    def setup(self):       
        self.name='Sunrise'  
        self.text=['draw',\
                   ] 
        self.addpart( draw.obj_drawing('sun',(640,210),legend='The Sun') )
        self.addpart( draw.obj_drawing('horizon',(640,560),legend='The Horizon') )
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_idea1p2())  
class obj_scene_idea1p2(obj_ideapage):
    def setup(self):         
        self.name='Sunrise p2'
        self.text=['sunrise (using an imagefill)',\
                   ] 
        self.addpart( draw.obj_animation('sunrise','sun',(640,210),record=True) )
        
        self.addpart(draw.obj_imagefill((share.colors.background,630,100),(640,670)))# filler
        self.addpart( draw.obj_image('horizon',(640,560)) )  
    

class obj_scene_idea2(obj_ideapage):
    def setup(self):       
        self.name='Talking '  
        self.text=['Hero talks',\
                   ] 
        animation=draw.obj_animation('herotalks1','herohead',(640,360),record=True) 
        animation.addimage('herohead_happy')
        self.addpart(animation)
    

class obj_scene_idea3(obj_ideapage):
    def setup(self):       
        self.name='Critter'  
        self.text=['create a critter that spit/throws',\
                   ] 
        self.addpart( draw.obj_drawing('alert',(400,350),legend='Alert',shadow=(50,50)) )
        self.addpart( draw.obj_drawing('critterspit',(200,450),legend='Critter',shadow=(100,100)) )
        self.addpart( draw.obj_drawing('critterspit_strike',(800,450),legend='Critter Strike',shadow=(100,100)) )
        self.addpart( draw.obj_drawing('critterspit_spit',(1000,450),legend='Spit',shadow=(50,50)) )


class obj_scene_idea4(obj_ideapage):
    def setup(self):       
        self.name='Critter behavior'  
        self.text=['Takes 3 hits to kill',\
                   ] 
        ww=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(ww)
        hero=actor.obj_actor_hero_v4(ww,(340,360),scale=0.5)
        critter=actor.obj_actor_critterspit(ww,(tool.randint(100,1180),tool.randint(100,620)),scale=0.5 )
        self.addpart( ww )


class obj_scene_idea5(obj_ideapage):
    def setup(self):       
        self.name='Hero hits up and down too'  
        self.text=['could hero hit up and down like ZLTTP.',\
                   'it should then have 4 facing directions (and ability to stay in them). ',\
                   'and we should be able to tell when facing up or down (maybe rotate the head?). ',\
                   'not working because replace image in animation with different size ',\
                   ] 
        ww=world.obj_world_ch1(self)
        hero=actor.obj_actor_hero_v5(ww,(640,360))# with up and down
        hero.addpart("instructions", draw.obj_textbox('Strike with [Left Mouse] or [Space]',(640,680)) )
        hero.scale(0.5)# scale actor hero
        self.addpart( ww ) 

class obj_scene_idea6(obj_ideapage):
    def setup(self):       
        self.name='Save new image'  
        self.text=['save image from existing one (works)',\
                   '. ',\
                   ] 
        a=draw.obj_image('herohead',(640,360))
        a.rotate(45)
        a.save('herohead_r45')
    

class obj_scene_idea7(obj_ideapage):
    def setup(self):       
        self.name='Idea'  
        self.text=['comment here',\
                   '. ',\
                   ] 
        self.addpart( draw.obj_image('horizon',(640,560)) )
    

class obj_scene_idea8(obj_ideapage):
    def setup(self):       
        self.name='Idea'  
        self.text=['comment here',\
                   '. ',\
                   ] 
        self.addpart( draw.obj_image('horizon',(640,560)) )
    

class obj_scene_idea9(obj_ideapage):
    def setup(self):       
        self.name='Idea'  
        self.text=['comment here',\
                   '. ',\
                   ] 
        self.addpart( draw.obj_image('horizon',(640,560)) )
    

class obj_scene_idea10(obj_ideapage):
    def setup(self):       
        self.name='Idea'  
        self.text=['comment here',\
                   '. ',\
                   ] 
        self.addpart( draw.obj_image('horizon',(640,560)) )
        
        

# draw hero house
class obj_scene_ch2p2(page.obj_chapterpage):
    def setup(self):         
        self.text=[('{heroname}',share.colors.hero),"\'s house, ",\
                   'that was named',('{housename}',share.colors.house),\
                   'looked like this from the outside. ',\
                   ]
        drawing=draw.obj_drawing('house',(640,400),legend='House from outside')
        drawing.brush.makebrush(share.brushes.smallpen)# draw with smaller pen
        self.addpart( drawing )
        self.addpart( draw.obj_image('door_closed',(640,500),scale=0.25) )
        self.addpart( draw.obj_animation('herolegs_stand','herolegs_stand',(240,500+40),scale=0.25) )
        self.addpart( draw.obj_animation('herohead_lookaround','herohead',(240,500),scale=0.25) )
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())


# hero opens door to enter house
class obj_scene_ch2p3(page.obj_chapterpage):
    def setup(self):         
        self.text=['To enter ',('{housename}',share.colors.house),', ',\
                   ('{heroname}',share.colors.hero),' needed to knock on the door with ',\
                   ('{weaponname}',share.colors.weapon),\
                   ', then stand in front of the door. ',\
                   ]
        self.addpart( draw.obj_image('house',(640,400)) )
        self.world=world.obj_world_ch2(self)
        bdry=actor.obj_actor_bdry(self.world,bounds=(50,1280-50,500,720-50))
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
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
        
        