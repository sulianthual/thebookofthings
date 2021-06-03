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
    def soundnextpage(self):
        pass# no sound

class obj_scene_ch8p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam())
    def setup(self):
        self.text=['-----   Epilogue   -----   ',\
                   '\n Welcome back, said the book of things. Here you can roam the world freely and replay all the games. Have fun!  ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)
        #
        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [46] )
        animation.addsound( "book2", [63] )
        animation.addsound( "pen", [199] )
        animation.addsound( "eraser", [185],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


###########
# roam to different locations
class obj_scene_ch8roam(page.obj_chapterpage):
    def triggerprevpage(self,controls):# (prefer over an empty prevpage)
        return False
    def nextpage(self):
        if self.world.goalname=='home':
            share.scenemanager.switchscene(obj_scene_ch8home())
        elif self.world.goalname=='cake':
            share.scenemanager.switchscene(obj_scene_ch8atcake())
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
        elif self.world.goalname=='island':
            share.scenemanager.switchscene(obj_scene_ch8island())
        else:
            share.scenemanager.switchscene(obj_scene_ch8roam())# reload same scene

    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
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
        return (controls.ga and controls.gac) or self.world.done
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
        return (controls.ga and controls.gac) or self.world.done
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
        return (controls.ga and controls.gac) or self.world.done
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
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_wakeup(self,bug=True,partner=True,alarmclock=True)
        self.addpart(self.world)

class obj_scene_ch8homebye(page.obj_chapterpage):
    def triggerprevpage(self,controls):# (prefer over an empty prevpage)
        return False
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
# cake (credits)
class obj_scene_ch8atcake(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='cake'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='cake'))
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                'Thank you for playing the book of things. See full list of credits in the settings menu. ',\
                   ]
        self.world=world.obj_world_eatfish(self,cake=True)
        self.addpart(self.world)
        # self.addpart( draw.obj_image('cake',(640,450)) )


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
        # self.addpart(draw.obj_imageplacer(self,'mailbox','flower','cloud'))
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(138,627),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(268,559),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(438,636),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1186,633),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1008,560),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )

class obj_scene_ch8atpartnerserenade(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerkiss())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
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
        return (controls.ga and controls.gac) or self.world.done
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
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(138,627),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(268,559),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(438,636),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1186,633),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1008,560),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )

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
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(138,627),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(268,559),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(438,636),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1186,633),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1008,560),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7) )


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
        return (controls.ga and controls.gac) or self.world.done
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
        return (controls.ga and controls.gac) or self.world.done
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
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch8mechfight(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechreplay())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
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
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_ch8mechbye(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def setup(self):
        self.text=['"Alright bye". ']
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )


###########
# west castle

class obj_scene_ch8west(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def nextpage(self):
        trypassword=share.datamanager.getword('castlepassword')
        shouldpassword='lie cheat steal'
        if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
            share.scenemanager.switchscene(obj_scene_ch8westcorrectpassword())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westwrongpassword())
    def setup(self):
        self.text=[\
                  '"Welcome back, blasted the castle\'s A.S.S. (automated security system). ',\
                  'Please enter the ',('password',share.colors.password),
                '". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('castlepassword',30,(380,260), legend='Castle Password',default=' ')
        self.addpart( self.textinput )


class obj_scene_ch8westwrongpassword(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8west())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8west())
    def setup(self):
        self.text=[\
                  '"Wrong, blasted the castle\'s ',\
                  'A.S.S., zapping engaged! In case you already forgot, the password is ',\
                ('"lie cheat steal"',share.colors.password),\
                '. Now try again". ',\
                   ]
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )

class obj_scene_ch8westcorrectpassword(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westinside())
    def setup(self):
        self.text=[\
                  '"You may enter, blasted the castle\'s ',\
                  'A.S.S.". ',\
                   ]
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heroenterscastle','herobase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_ch8westinside(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8westdodgebullets())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8weststomp())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{villainname}',share.colors.villain),'. ',\
                'How do you want to fight." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='1')
        textchoice.addchoice('1. Guns','1',(310,y1))
        textchoice.addchoice('2. Fists','2',(580,y1))
        textchoice.addchoice('3. Nothing Really','3',(840,y1))
        self.addpart( textchoice )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )


class obj_scene_ch8westdodgebullets(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)


class obj_scene_ch8weststomp(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)

class obj_scene_ch8westreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='castle'))
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8westdodgebullets())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8weststomp())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westbye())
    def setup(self):
        self.text=[\
                '"Nicely done, said ',\
                ('{villainname}',share.colors.villain),'. ',\
                'Do you to want to fight again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='3')
        textchoice.addchoice('1. Guns','1',(310,y1))
        textchoice.addchoice('2. Fists','2',(580,y1))
        textchoice.addchoice('3. Nope','3',(840,y1))
        self.addpart( textchoice )
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
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_lyingpart1())
        else:
            share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                'Do you want to replay my lying game." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation2=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation2 )



class obj_scene_ch8eastreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='forest'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_lyingpart1())
        else:
            share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def setup(self):
        self.text=[\
                '"Do you want to play again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
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
        return (controls.ga and controls.gac) or self.world.done
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
        return (share.devmode and controls.ga and controls.gac) or self.world.done
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
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8southride())
        else:
            share.scenemanager.switchscene(obj_scene_ch8southbye())
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{sailorname}',share.colors.sailor),'. ',\
                'Do you want to ride ',('treasure',share.colors.cow),' again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)


class obj_scene_ch8southride(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southreplay())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                '"Make it to the boat".',\
                   ]
        self.world=world.obj_world_ridecow(self)
        self.addpart(self.world)

class obj_scene_ch8southreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='beach'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8southride())
        else:
            share.scenemanager.switchscene(obj_scene_ch8southbye())
    def setup(self):
        self.text=[\
                '"That was nice. Do you want to play again".',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
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
# skull island
class obj_scene_ch8island(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='island'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
        else:
            share.scenemanager.switchscene(obj_scene_ch8roam(start='island'))
    def setup(self):
        self.text=[\
                '"',\
                'Do you want to sneak around." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('mountain',(1169,276),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(940,566),scale=0.6,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(707,467),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(1203,556),scale=0.41,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('herobase',(384,703),scale=1.02,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(130,549),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(348,320),scale=0.46,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6_skullobserve1','skeletonbase_sailorhat',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch6_skullobserve2','skeletonbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch6_skullobserve3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )

class obj_scene_ch8islandsneak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak1())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Start Sneaking']
       self.world=world.obj_world_bushstealth0(self)
       self.addpart(self.world)


class obj_scene_ch8islandsneak1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak2())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak1())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth(self)
       self.addpart(self.world)

class obj_scene_ch8islandsneak2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak3())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth2(self)
       self.addpart(self.world)

class obj_scene_ch8islandsneak3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak4())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth3(self)
       self.addpart(self.world)

class obj_scene_ch8islandsneak4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandreplay())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth4(self)
       self.addpart(self.world)


class obj_scene_ch8islandreplay(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='beach'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
        else:
            share.scenemanager.switchscene(obj_scene_ch8roam(start='island'))
    def setup(self):
        self.text=[\
                '"That was nice. Do you want to play again".',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(660,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('mountain',(1169,276),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(940,566),scale=0.6,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(707,467),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(1203,556),scale=0.41,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('herobase',(384,703),scale=1.02,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(130,549),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(348,320),scale=0.46,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6_skullobserve1','skeletonbase_sailorhat',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch6_skullobserve2','skeletonbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch6_skullobserve3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )


#################################################################
#################################################################
# the entire lying game put back here


##########################
class obj_scene_lyingpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8eastreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q1(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        # Page Text
        self.text=[\
                    'This game plays in three rounds. For the first round, ',\
                    'here are three ',\
                    ('true statements',share.colors.darkgreen),' you need to remember. ',\
                    'You can even take some notes at the bottom of the screen to help your memory. '
                   ]
        self.addpart( draw.obj_textbox( '1. '+self.world.getstatement(0),(400,220),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '2. '+self.world.getstatement(1),(400,290),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '3. '+self.world.getstatement(2),(400,360),xleft=True,color=share.colors.darkgreen  ) )
        # Page drawing
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        if (kwargs is not None) and ('world' in kwargs):
            pass
        else:
            drawing.clear()# erase drawing
        self.addpart( drawing )
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )


class obj_scene_lyingp1q1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
    def nextpage(self):
        if self.world.isanswercorrect():
            self.nextpage_lyinggame()
        else:
            self.nextpage_lyingfail()
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q2(world=self.world))
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart1(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (1/3):']
    def textchoice_lyinggame(self):
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('True','yes',(640-100,310))
        textchoice.addchoice('False','no',(640+100,310))
        self.addpart( textchoice )
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        self.world.makequestion()
        # Page text
        self.text=self.text_lyinggame()
        self.addpart( draw.obj_textbox( '" '+self.world.getquestion()+'"',(640,190)) )
        self.textchoice_lyinggame()
        # Drawing
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        self.addpart( drawing )
        # animation
        animation1=draw.obj_animation('ch3_bunnheadwobble','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bunnheadwobble2','herohead',(640,360),record=False, sync=animation1) )


class obj_scene_lyingp1q2(obj_scene_lyingp1q1):# child of lying 1
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q3(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (2/3):']

class obj_scene_lyingp1q3(obj_scene_lyingp1q1):# child of lying 1
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1win())# forget lying game database
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (3/3):']


class obj_scene_lyingfailpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    ' You gave me the wrong answer. ',\
                    'If your memory is that bad you can always ',\
                    ('take some notes',share.colors.instructions),' at the bottom of the screen. ',\
                    'Now go back and win this first round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_lyingpart1win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won the ',\
                    ('first round',share.colors.grandmaster2),'! ',\
                   ]
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation2=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation2)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )


##########################
class obj_scene_lyingpart2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1win())# forget lying game database
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q1(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        # Page Text
        self.text=['For the second round, ',('I will now be lying',share.colors.red),'. ',\
                    'Let me tell you three statements. They are ',\
                    ('all false ',share.colors.red),' because I am lying. ',\
                    'Once again, you can take some notes to help your memory. '
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.world.getstatement(0,lying=True),(400,220),xleft=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox( '2. '+self.world.getstatement(1,lying=True),(400,290),xleft=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox( '3. '+self.world.getstatement(2,lying=True),(400,360),xleft=True,color=share.colors.red) )
        # Drawing
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        if (kwargs is not None) and ('world' in kwargs):
            pass
        else:
            drawing.clear()# erase drawing
        self.addpart(drawing)
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )


class obj_scene_lyingp2q1(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q2(world=self.world))
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart2(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (1/3):']


class obj_scene_lyingp2q2(obj_scene_lyingp2q1):# child of lying 2
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q3(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (2/3):']

class obj_scene_lyingp2q3(obj_scene_lyingp2q1):# child of lying 2
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2win())# forget lying game database
    def text_lyinggame(self):
        return ['Now tell me if this is true or false (3/3):']


class obj_scene_lyingfailpart2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    ' You gave me the wrong answer. ',\
                    'For this second round, remember that ',\
                    ('all my statements are false',share.colors.red),'. ',\
                    'And I may suggest that you take some notes ',\
                    'at the bottom of the screen. ',\
                    'Now go back and win this second round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_lyingpart2win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won the ',\
                    ('second round',share.colors.grandmaster2),'! ',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation2)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_herowalkbunny2love2','love',(640,360),record=False,sync=animation2)
        animation4.addimage('empty',path='premade')
        self.addpart( animation4 )


##########################
class obj_scene_lyingpart3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2win())# forget lying game database
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q1(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        # Page Text
        self.text=['For the last round, ',('I will be lying and so will you',share.colors.red),'! ',\
                    'I am giving you three ',\
                    ('false statements',share.colors.red),', and ',\
                    'you will only give me ',\
                    ('wrong answers',share.colors.red),'. ',\
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.world.getstatement(0,lying=True),(400,220),xleft=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox( '2. '+self.world.getstatement(1,lying=True),(400,290),xleft=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox( '3. '+self.world.getstatement(2,lying=True),(400,360),xleft=True,color=share.colors.red) )
        # Drawing
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        if (kwargs is not None) and ('world' in kwargs):
            pass
        else:
            drawing.clear()# erase drawing
        self.addpart(drawing)
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )


class obj_scene_lyingp3q1(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3(world=self.world))
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q2(world=self.world))
    def nextpage(self):
        if self.world.isanswercorrect(lying=True):# hero must lie too
            self.nextpage_lyinggame()
        else:
            self.nextpage_lyingfail()
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart3(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false ',\
                ' (but lie and give me the ',\
                ('wrong answer',share.colors.red),') (1/3): ']
    def textchoice_lyinggame(self):# textchoice is "ironic"
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('"True"','yes',(640-100,310))
        textchoice.addchoice('"False"','no',(640+100,310))
        self.addpart( textchoice )

class obj_scene_lyingp3q2(obj_scene_lyingp3q1):# child of lying 3
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q3(world=self.world))
    def text_lyinggame(self):
        return ['Now tell me if this is true or false ',\
                ' (but lie and give me the ',\
                ('wrong answer',share.colors.red),') (2/3): ']

class obj_scene_lyingp3q3(obj_scene_lyingp3q1):# child of lying 3
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingend())# forget lying game database
    def text_lyinggame(self):
        return ['Now tell me if this is true or false ',\
                ' (but lie and give me the ',\
                ('wrong answer',share.colors.red),') (3/3): ']


class obj_scene_lyingfailpart3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3(world=self.world))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3(world=self.world))
    def setup(self,**kwargs):
        # inherit world
        if (kwargs is not None) and ('world' in kwargs):
            self.world=kwargs["world"]# inherit lying database
        else:
            self.world=world.obj_world_lying(self)# or remake it
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    'Well, you actually gave me the correct answer, but that isnt what I wanted. ',\
                    'For this third round, remember that ',\
                    ('all my statements are false',share.colors.red),' (I am lying), ',\
                    'and that you must ',\
                    ('always give me the wrong answer',share.colors.red),' (you are lying too). ',\
                    'Now go back and win this third round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_lyingend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8eastreplay())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won my ',('lying game',share.colors.grandmaster2),'! ',\
                    '".',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation2)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_herowalkbunny2love2','love',(640,360),record=False,sync=animation2)
        animation4.addimage('empty',path='premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch4_herowalkbunny2love3','love',(640,360),record=False,sync=animation2)
        animation5.addimage('empty',path='premade')
        self.addpart( animation5 )




#################################################################
#################################################################
