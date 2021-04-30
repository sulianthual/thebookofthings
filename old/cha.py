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
        self.list.append(obj_scene_pickflowers())
        self.list.append(obj_scene_travel())
        self.list.append(obj_scene_dodgebullets())
        self.list.append(obj_scene_stompfight())
        self.list.append(obj_scene_lying())
        self.list.append(obj_scene_climbing())
        self.list.append(obj_scene_rockpaperscissors())
        self.list.append(obj_scene_bushstealth())
        self.list.append(obj_scene_ridecow())
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
        # self.addpart( draw.obj_imageplacer(self,'pond','flower','bush',actor='staticactor') )


class obj_scene_wakeup(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Wake Up'
        self.text=['Wake Up']
        self.world=world.obj_world_wakeup(self,bug=True)
        # self.world=world.obj_world_wakeup(self,partner=True,addsun=False)
        # self.world=world.obj_world_wakeup(self,partner=True,heroangry=True,partnerangry=True)
        # self.world=world.obj_world_wakeup(self,sun=False)
        self.addpart(self.world)


class obj_scene_drinking(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Drinking'
        self.text=['Drinking']
        self.world=world.obj_world_breakfastdrinking(self)
        # self.world=world.obj_world_breakfastdrinking(self,partner=False)
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'herobaseangry',actor='hero') )


class obj_scene_fishing(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Fishing'
        self.text=['Fishing']
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_pickflowers(obj_testpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_pickflowers2())
    def setup(self):
        self.name='Pickup Flowers (draw)'
        self.text=['Pickup Flowers (draw)']
        self.addpart( draw.obj_drawing('bush',(210,450),legend='Bush',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('flower',(640,450),legend='Flower',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('pond',(1280-210,450),legend='Pond',shadow=(200,200)) )

class obj_scene_pickflowers2(obj_testpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_pickflowers())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=['Pickup Flowers (play)']
        self.world=world.obj_world_travel(self,start='home',goal='home',chapter=3,minigame='flowers')
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'flower','bush','pond',actor='staticactor11') )

class obj_scene_travel(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Travel'
        self.text=['Travel']
        self.world=world.obj_world_travel(self)# default=chapter1, home area only, no goal
        # self.world=world.obj_world_travel(self,start='home',goal='castle',chapter=3)
        # self.world=world.obj_world_travel(self,start='home',goal='castle',chapter=3,partner=True)
        self.world=world.obj_world_travel(self,start='home',goal='nowhere',chapter=7)
        # self.world=world.obj_world_travel(self,start='home',goal='peak',chapter=5)
        # self.world=world.obj_world_travel(self,start='peak',goal='home',chapter=5)
        # self.world=world.obj_world_travel(self,start='home',goal='nowhere',chapter=7)
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'mailbox','bush','flower',actor='staticactor11') )
        # self.addpart( draw.obj_imageplacer(self,'tree',actor='staticactor21') )
        # self.addpart( draw.obj_imageplacer(self,'tower','mountain') )
        # self.addpart( draw.obj_imageplacer(self,'cloud','mountain','lightningbolt','tree') )
        # self.addpart( draw.obj_imageplacer(self,'cloud','mountain','tree','sun') )
        # self.addpart( draw.obj_imageplacer(self,'tree','mountain','cloud','sun','bush',actor='staticactor10') )
        # self.addpart( draw.obj_drawing('path2',(640,360),shadow=(540,200),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('horizon1',(640,360),shadow=(640,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('horizon2',(640+320,360),shadow=(320,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('horizon3',(640+320,360+180),shadow=(320,200),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('beach1',(640,360),shadow=(640,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('beach2',(640,360),shadow=(320,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('beach3',(640,360-180),shadow=(320,200),brush=share.brushes.smallpen)
        # self.addpart( draw.obj_drawing('beach4',(640,360),shadow=(320,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('horizon4',(640,360),shadow=(320,50),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_drawing('island1',(640,360),shadow=(600,250),brush=share.brushes.smallpen) )

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


class obj_scene_lying(obj_testpage):
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.name='Lying'
        self.text=['Lying: this game is not in a world but in a serie of pages']


class obj_scene_climbing(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Climbing'
        self.text=['Climbing']
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)


class obj_scene_rockpaperscissors(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Rock-Paper-Scissors'
        self.text=['Rock-Paper-Scissors']
        if True:
            self.world=world.obj_world_rockpaperscissors(self)
            # self.world=world.obj_world_rockpaperscissors(self,elderwins=True)# elder always wins
            # self.world=world.obj_world_rockpaperscissors(self,elderlooses=True)# elder always looses
            # self.world=world.obj_world_rockpaperscissors(self,elderpeaks=True)# elder peaks on 1...
            # self.world=world.obj_world_rockpaperscissors(self,elderthinks=False)# cant see elder choice
            self.addpart(self.world)

        # self.addpart( draw.obj_image('herobase',(640-240,530),scale=0.5) )
        # self.addpart( draw.obj_image('elderbase',(640+240,530),scale=0.5,fliph=True) )
        else:
            self.addpart( draw.obj_image('herobase',(640,530),scale=0.5) )
            animation1=draw.obj_animation('rps_herowalk','herobase',(640,360),record=True)
            animation1.addimage('herowalk')
            self.addpart(animation1)
        # animation1=draw.obj_animation('rps_elderwalk','elderbase',(640,360),record=True)
        # animation1.addimage('elderwalk')
        # self.addpart(animation1)


class obj_scene_bushstealth(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def nextpage(self):
        if not self.world.win:
            share.scenemanager.switchscene(obj_scene_bushstealth())
    def setup(self):
        self.name='Bush Stealth'
        self.text=['Bush Stealth']
        self.world=world.obj_world_bushstealth(self)
        # self.world=world.obj_world_bushstealth2(self)
        # self.world=world.obj_world_bushstealth3(self)
        # self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'skeletonbase','bush','palmtree','moon') )
        # self.addpart( draw.obj_image('skeletonbase',(775,505),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('skeletonbase',(640,360),scale=0.5) )
        self.addpart( draw.obj_drawing('skeletonview',(640+250,360),shadow=(250,100),brush=share.brushes.tinypen) )
        # self.addpart( draw.obj_drawing('bushspark',(640,360-100),shadow=(150,50)) )
        # self.addpart( draw.obj_animation('bushstealth_skeletonmove','skeletonbase',(640,360),record=True) )
        # self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(640,360),record=True) )
        # self.addpart( draw.obj_drawing('floor6',(640,720-50),shadow=(640,50),brush=share.brushes.smallpen) )
       # self.addpart( draw.obj_animation('bushstealth_moonmove','moon',(640,360),record=True) )
       # self.addpart( draw.obj_imageplacer(self,'bush','palmtree','moon',actor='staticactor') )
       # self.addpart( draw.obj_drawing('floor6',(640,300),shadow=(640,50),brush=share.brushes.smallpen) )
       # self.addpart( draw.obj_image('floor6',(640,300)) )
#
class obj_scene_ridecow(obj_testpage):
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Ride Cow'
        self.text=['Ride Cow']
        self.world=world.obj_world_ridecow(self)
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
    # def triggernextpage(self,controls):
    #     return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.name='Go to Bed'
        self.text=['Go to Bed']
        self.world=world.obj_world_gotobed(self,bug=True)
        # self.world=world.obj_world_gotobed(self,partner=True,heroangry=True,addmoon=False)
        self.addpart(self.world)
        # self.addpart( draw.obj_animation('ch4_heroawakesbug','bug',(640,360)) )
        # self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        # animation1=draw.obj_animation('ch1_herotosleep','herobase',(640,360),scale=0.7)
        # animation2=draw.obj_animation('ch1_herotosleepbug','bug',(640,360),record=False,sync=animation1)
        # animation2.addimage('empty',path='premade')
        # self.addpart( animation1 )
        # self.addpart( animation2 )





####################################################################################################################
