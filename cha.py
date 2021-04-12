#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# cha.py: arcade menu
#
##########################################################
##########################################################

# import core
import share
import tool
import draw
import page
import world
#

##########################################################
##########################################################

# Test Menu
class obj_scene_arcademenu(page.obj_page):
    def __init__(self):
        super().__init__()
    def setup(self):
        super().setup()
        share.ipage=1# current page number in chapter
        self.nrow=17# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Arcade Menu [Enter: Read] [Tab: Back]',(640,50),fontsize='medium'))
        self.addpart(draw.obj_textbox('[Space: Main Menu]',(1120,700),fontsize='smaller'))
        for i,test in enumerate(self.list[:self.nrow-1]):
            self.addpart(draw.obj_textbox(test.name,(250,130+i*30),fontsize='smaller'))
        for i,test in enumerate(self.list[self.nrow-1:]):
            self.addpart(draw.obj_textbox(test.name,(640,130+i*30),fontsize='smaller'))
        self.sprite_pointer=draw.obj_textbox('---',(640,360),fontsize='smaller')# moved around
        self.addpart(self.sprite_pointer)
    def page(self,controls):
        if share.itest<self.nrow-1:
            self.sprite_pointer.movetox(60)
            self.sprite_pointer.movetoy(130+share.itest*30)
        else:
            self.sprite_pointer.movetox(460)
            self.sprite_pointer.movetoy(130+(share.itest-self.nrow+1)*30)
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            share.itest += 1
            if share.itest == self.listlen: share.itest=0
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            share.itest -= 1
            if share.itest == -1: share.itest=self.listlen-1
        if (controls.enter and controls.enterc):
            share.scenemanager.switchscene(self.list[share.itest],init=True)
        if (controls.esc and controls.escc) or (controls.space and controls.spacec):
            share.scenemanager.switchscene(share.titlescreen)


    def loadtests(self):# load all mini-games
        #
        self.list.append(obj_scene_sunrise())
        self.list.append(obj_scene_wakeup())
        self.list.append(obj_scene_drinking())
        self.list.append(obj_scene_fishing())
        self.list.append(obj_scene_traveltolair())
        self.list.append(obj_scene_travelfromlair())
        self.list.append(obj_scene_traveltopeak())
        self.list.append(obj_scene_dodgebullets())
        self.list.append(obj_scene_stompfight())
        self.list.append(obj_scene_climbing())
        self.list.append(obj_scene_eating())
        self.list.append(obj_scene_serenade())
        self.list.append(obj_scene_kiss())
        self.list.append(obj_scene_nightfall())
        self.list.append(obj_scene_gotobed())
        #
        self.listlen=len(self.list)


# Template for test page = chapter page with slightly modified functionalities
class obj_testpage(page.obj_chapterpage):
    def __init__(self):
        self.name='Unamed'# needs name to display on test menu
        super().__init__()
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_arcademenu())
    def exitpage(self):
        share.scenemanager.switchscene(obj_scene_arcademenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_arcademenu())


#########################################################################
#########################################################################
# All Tests Here


class obj_scene_sunrise(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Sunrise'
        self.text=['Sunrise']
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_wakeup(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Wake Up'
        self.text=['Wake Up']
        self.world=world.obj_world_wakeup(self)
        # self.world=world.obj_world_wakeup(self,partner='inlove')
        # self.world=world.obj_world_wakeup(self,partner='inlove',angryfaces=True)
        # self.world=world.obj_world_wakeup(self,sun=False)
        self.addpart(self.world)


class obj_scene_drinking(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Drinking'
        self.text=['Drinking']
        self.world=world.obj_world_breakfastdrinking(self)
        self.addpart(self.world)


class obj_scene_fishing(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Fishing'
        self.text=['Fishing']
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_traveltolair(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Travel -> Lair'
        self.text=['Travel -> Lair']
        self.world=world.obj_world_traveltolair(self)
        self.addpart(self.world)


class obj_scene_travelfromlair(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Travel <- Lair'
        self.text=['Travel <- Lair']
        self.world=world.obj_world_traveltolair(self,tohome=True)
        # self.world=world.obj_world_traveltolair(self,tohome=True,partner=True)
        self.addpart(self.world)


class obj_scene_traveltopeak(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Travel -> Peak'
        self.text=['Travel -> Peak']
        self.world=world.obj_world_traveltopeak(self)
        self.addpart(self.world)



class obj_scene_dodgebullets(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Dodge Bullets'
        self.text=['Dodge Bullets']
        self.world=world.obj_world_dodgegunshots(self)
        # self.world=world.obj_world_dodgegunshots(self,heroangry=True)
        # self.world=world.obj_world_dodgegunshots(self,heroangry=True,partnerenemy=True)
        self.addpart(self.world)


class obj_scene_stompfight(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Stomp Fight'
        self.text=['Stomp Fight']
        self.world=world.obj_world_stompfight(self)
        # self.world=world.obj_world_stompfight(self,heroangry=True)
        # self.world=world.obj_world_stompfight(self,heroangry=True,partnerenemy=True)
        self.addpart(self.world)


class obj_scene_climbing(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Climbing'
        self.text=['Climbing']
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)


class obj_scene_eating(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Eating'
        self.text=['Eating']
        self.world=world.obj_world_eatfish(self)
        # self.world=world.obj_world_eatfish(self,partner='inlove')
        self.addpart(self.world)


class obj_scene_serenade(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Serenade'
        self.text=['Serenade']
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)


class obj_scene_kiss(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Kiss'
        self.text=['Kiss']
        self.world=world.obj_world_kiss(self)
        self.addpart(self.world)


class obj_scene_nightfall(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Nightfall'
        self.text=['Nightfall']
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_gotobed(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Go to Bed'
        self.text=['Go to Bed']
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)

####################################################################################################################
