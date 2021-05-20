#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter8.py: ...
#
##########################################################
###########################################################

import share
import tool
import draw
import page
import world

##########################################################
##########################################################

# Chapter VIII: ...
# *CHAPTER VIII

class obj_scene_chapter8(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8p0())
    def triggernextpage(self,controls):
        return True

class obj_scene_ch8p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam())
    def setup(self):
        self.text=['-----   Epilogue   -----   ',\
                   '\n Welcome back, said the book of things. Here you can roam the world freely and replay all the games. Have fun!  ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)

###########
# roam to different locations
class obj_scene_ch8roam(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if self.world.goalname=='home':
            share.scenemanager.switchscene(obj_scene_ch8home())
        elif self.world.goalname=='pond':
            share.scenemanager.switchscene(obj_scene_ch8pond())
        elif self.world.goalname=='atpartner':
            share.scenemanager.switchscene(obj_scene_ch8atpartner())
        elif self.world.goalname=='mech':
            share.scenemanager.switchscene(obj_scene_ch8mech())
        elif self.world.goalname=='castle':
            share.scenemanager.switchscene(obj_scene_ch8west())
        elif self.world.goalname=='forest':
            share.scenemanager.switchscene(obj_scene_ch8east())
        elif self.world.goalname=='peak':
            share.scenemanager.switchscene(obj_scene_ch8north())
        elif self.world.goalname=='beach':
            share.scenemanager.switchscene(obj_scene_ch8south())
        else:
            share.scenemanager.switchscene(obj_scene_ch8roam())# reload same scene

    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self,**kwargs):
        # starting position
        if (kwargs is not None) and ('start' in kwargs):
            self.start=kwargs["start"]
        else:
            self.start="home"
        self.text=[]
        self.world=world.obj_world_travel(self,start=self.start,goal='everywhere',chapter=8,boat=True)
        self.addpart(self.world)
###########
# home
class obj_scene_ch8home(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='home'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8homesleep())
        else:
            share.scenemanager.switchscene(obj_scene_ch8homebye())
    def setup(self):
        self.text=[\
                '"Welcome back, said the ',\
                ('{bug}',share.colors.bug),'. ',\
                'Do you want to sleep. " ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_animation('ch1_awaken','bug',(640+100,360),scale=0.7,imgscale=0.5) )

class obj_scene_ch8homesleep(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep2())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)

class obj_scene_ch8homesleep2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep3())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_gotobed(self,bug=True,partner=True,alarmclock=True)
        self.addpart(self.world)

class obj_scene_ch8homesleep3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep4())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)

class obj_scene_ch8homesleep4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_wakeup(self,bug=True,partner=True,alarmclock=True)
        self.addpart(self.world)

class obj_scene_ch8homebye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='home'))
    def setup(self):
        self.text=[\
                '"Have a nice day, said the ',\
                ('{bug}',share.colors.bug),'." ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_animation('ch1_awaken','bug',(640+100,360),scale=0.7,imgscale=0.5) )

###########
# partner

class obj_scene_ch8atpartner(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='atpartner'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8atpartnerserenade())
        else:
            share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{partnername}',share.colors.partner),'. ',\
                'Do you want to serenade me. " ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1201,342),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1048,611),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1133,519),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1165,675),scale=0.33,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(1257,558),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1201,193),scale=0.22,rotate=0,fliph=False,flipv=False) )

class obj_scene_ch8atpartnerserenade(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerkiss())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)

class obj_scene_ch8atpartnerkiss(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerreplay())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"That was beautiful, lets kiss said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)

class obj_scene_ch8atpartnerreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='atpartner'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8atpartnerserenade())
        else:
            share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def setup(self):
        self.text=[\
                '"Do you want to play again, said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1201,342),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1048,611),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1133,519),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1165,675),scale=0.33,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(1257,558),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1201,193),scale=0.22,rotate=0,fliph=False,flipv=False) )

class obj_scene_ch8atpartnerbye(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='home'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='atpartner'))
    def setup(self):
        self.text=[\
                '"Aright bye, said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1201,342),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1048,611),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1133,519),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1165,675),scale=0.33,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(1257,558),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1201,193),scale=0.22,rotate=0,fliph=False,flipv=False) )


###########
# pond

class obj_scene_ch8pond(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8pondfish())
        else:
            share.scenemanager.switchscene(obj_scene_ch8pondbye())
    def setup(self):
        self.text=[\
                '"',\
                'Do you want to fish. " ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7) )


class obj_scene_ch8pondfish(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondeat())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch8pondeat(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondreplay())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)

class obj_scene_ch8pondreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8pondfish())
        else:
            share.scenemanager.switchscene(obj_scene_ch8pondbye())
    def setup(self):
        self.text=[\
                '"',\
                '"Do you want to fish again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7) )

class obj_scene_ch8pondbye(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def setup(self):
        self.text=['"Alright bye". ']
        #
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7) )

###########
# mech
class obj_scene_ch8mech(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech2())
    def setup(self):
        self.text=['"',('super-mech-hero',share.colors.hero),', assemble!". ']
        # Mech buildup
        animation1=draw.obj_animation('ch7_villainmech_assemble1','herobase',(640,360),record=False,imgfliph=True)
        animation1.addimage('heromecharmature')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_assemble_larm','fish',(640,360),record=False,imgfliph=True)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_assemble_rarm','flower',(640,360),record=False,imgfliph=True,imgflipv=True)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch7_villainmech_assemble_lleg','sailboat',(640-10,360),record=False,imgscale=0.7)
        animation4.addimage('empty',path='premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch7_villainmech_assemble_rleg','sailboat',(640+10,360),record=False,imgscale=0.7)
        animation5.addimage('empty',path='premade')
        self.addpart( animation5 )
        animation6=draw.obj_animation('ch7_villainmech_assemble_lshoulder','bush',(640,360),record=False)
        animation6.addimage('empty',path='premade')
        self.addpart( animation6 )
        animation7=draw.obj_animation('ch7_villainmech_assemble_rshoulder','bush',(640,360),record=False)
        animation7.addimage('empty',path='premade')
        self.addpart( animation7 )
        animation8=draw.obj_animation('ch7_villainmech_assemble_tpp','house',(640,360),record=False)
        animation8.addimage('empty',path='premade')
        self.addpart( animation8 )

class obj_scene_ch8mech2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech3())
    def setup(self):
        self.text=['"',('super-mech-hero',share.colors.hero),', expand!". ']
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heromech_expand','heromechbase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch8mech3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8mechfight())
        else:
            share.scenemanager.switchscene(obj_scene_ch8mechbye())
    def setup(self):
        self.text=['"Do you want to replay the mech fight". ']
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('heromechbase',(300,414),scale=0.81,rotate=0,fliph=False,flipv=False) )


class obj_scene_ch8mechfight(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechreplay())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_mechfight(self)
        self.addpart(self.world)

class obj_scene_ch8mechreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8mechfight())
        else:
            share.scenemanager.switchscene(obj_scene_ch8mechbye())
    def setup(self):
        self.text=['"That was a nice fight. Do you want to play again". ']
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('heromechbase',(300,414),scale=0.81,rotate=0,fliph=False,flipv=False) )


class obj_scene_ch8mechbye(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def setup(self):
        self.text=['"Alright bye". ']
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('heromechbase',(300,414),scale=0.81,rotate=0,fliph=False,flipv=False) )


###########
# west castle
class obj_scene_ch8west(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{villainname}',share.colors.villain),'. ',\
                'What game do you want to replay today." ',\
                   ]
        self.addpart( draw.obj_image('castle',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(881,292),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(709,245),scale=0.29,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )


class obj_scene_ch8westbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def setup(self):
        self.text=[\
                '"Alright bye, said ',\
                ('{villainname}',share.colors.villain),'." ',\
                   ]
        self.addpart( draw.obj_image('castle',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(881,292),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(709,245),scale=0.29,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )

###########
# east forest
class obj_scene_ch8east(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='forest'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                'What game do you want to replay today." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation2=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation2 )


class obj_scene_ch8eastbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='forest'))
    def setup(self):
        self.text=[\
                '"Alright bye, said ',\
                ('{bunnyname}',share.colors.bunny),'." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation2=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation2 )

###########
# north peak
class obj_scene_ch8north(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='peak'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northtop())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)

class obj_scene_ch8northtop(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8north_rps())
        else:
            share.scenemanager.switchscene(obj_scene_ch8northbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{eldername}',share.colors.elder),'. ',\
                'Do you want to play rock-paper-scissors." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('elderbase',(964,325),scale=0.48,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(72,655),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(209,681),scale=0.22,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(530,603),scale=0.55,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(266,557),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(84,527),scale=0.24,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1184,487),scale=0.42,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1219,584),scale=0.32,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(339,663),scale=0.22,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('floor4',(1280-500,720-140),path='premade') )
        animation1=draw.obj_animation('ch5_meetelder','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch5_meetelder2','sun',(640,360),record=False,sync=animation1) )

class obj_scene_ch8north_rps(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northreplay())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=['"Alright lets play, said ',('{eldername}',share.colors.elder),'". ']
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)

class obj_scene_ch8northreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8north_rps())
        else:
            share.scenemanager.switchscene(obj_scene_ch8northbye())
    def setup(self):
        self.text=[\
                '"That was a nice game, said ',\
                ('{eldername}',share.colors.elder),'. Do you want to play again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360),record=False) )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )



class obj_scene_ch8northbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='peak'))
    def setup(self):
        self.text=[\
                '"Bye then, said ',\
                ('{eldername}',share.colors.elder),'." ',\
                   ]
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360),record=False) )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )

###########
# south beach
class obj_scene_ch8south(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='beach'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{sailorname}',share.colors.sailor),'. ',\
                'What game do you want to replay today." ',\
                   ]
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)


class obj_scene_ch8southbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='beach'))
    def setup(self):
        self.text=[\
                '"Alright bye, said ',\
                ('{sailorname}',share.colors.sailor),'." ',\
                   ]
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)

###########
