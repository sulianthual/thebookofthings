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


class obj_scene_chapter8(page.obj_chapterpage):# just go to next page directly
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam())
    def triggernextpage(self,controls):
        return True
    def textboxset(self):
        self.textboxopt={'do':False}
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch8_start')
        self.text=[' ']
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music(None) )


###########
# roam to different locations
class obj_scene_ch8roam(page.obj_chapterpage):
    def prevpage(self):
        pass
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
        elif self.world.goalname=='tower':
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def soundnextpage(self):
        pass# no sound
    def setup(self,**kwargs):
        # starting position
        if (kwargs is not None) and ('start' in kwargs):
            self.start=kwargs["start"]
        else:
            self.start="home"
        self.text=[' ']
        self.world=world.obj_world_travel(self,start=self.start,goal='everywhere',chapter=8,boat=True,noending=True)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music(None) )

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
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{bug}',share.colors.bug),'. ',\
                'Do you want to sleep." ']
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        # self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        animation1=draw.obj_animation('ch1_awaken','bug',(640+100,360),scale=0.7,imgscale=0.5)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [47, 67],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch8homesleep(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep2())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch8homesleep2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep3())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_gotobed(self,bug=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch8homesleep3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homesleep4())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch8homesleep4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8homebye())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch8homebye(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='home'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='home'))
    def setup(self):
        self.text=[\
                '"Have a nice day, said ',\
                ('{bug}',share.colors.bug),'." ']
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        # self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        animation1=draw.obj_animation('ch1_awaken','bug',(640+100,360),scale=0.7,imgscale=0.5)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [47, 67, 120] )
        animation1.addsound( "bug2", [125],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


###########
# cake (credits)
class obj_scene_ch8atcake(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='cake'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='cake'))
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def presetup(self):
        super().presetup()
        # self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def setup(self):
        credits=share.gamecredits.gettext()# game credits from database
        self.text=[credits]
        self.world=world.obj_world_eatfish(self,cake=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch7') )


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
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{partnername}',share.colors.partner),'. ',\
                'Do you want to serenade me. " ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        # self.addpart(draw.obj_imageplacer(self,'mailbox,'cloud'))
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'partner1','partner2','partner3') )
        animation1.addsound( "partner1", [54],skip=1 )
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch8atpartnerserenade(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerkiss())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch8atpartnerkiss(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8atpartnerreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"That was beautiful, lets kiss said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch8atpartnerreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8atpartnerserenade())
        else:
            share.scenemanager.switchscene(obj_scene_ch8atpartnerbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Do you want to play again, said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'partner1','partner2','partner3') )
        animation1.addsound( "partner1", [50] )
        animation1.addsound( "partner2", [110],skip=1 )
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch8atpartnerbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='atpartner'))
    def setup(self):
        self.text=[\
                '"Aright bye, said ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        self.addpart( draw.obj_image('mailbox',(167,347),scale=0.44,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','partnerbase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'partner1','partner2','partner3') )
        animation1.addsound( "partner3", [51],skip=1 )
        #
        self.addpart( draw.obj_music('partner') )


###########
# pond

class obj_scene_ch8pond(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8pondfish())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8pondfish_withgun())
        elif share.datamanager.getword('numchoice')=='3':
            share.scenemanager.switchscene(obj_scene_ch8pondfish_withscissors())
        else:
            share.scenemanager.switchscene(obj_scene_ch8pondbye())
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"',\
                'Do you want to fish. " ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='1')
        textchoice.addchoice('1. Hook','1',(640-450,y1))
        textchoice.addchoice('2. Gun','2',(640-200,y1))
        textchoice.addchoice('3. Electric Fish','3',(640+70,y1))
        textchoice.addchoice('4. Nevermind','4',(640+400,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero1", [15] )
        animation1.addsound( "hero2", [140] )
        animation1.addsound( "hero3", [50],skip=1 )
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )


class obj_scene_ch8pondfish(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondeat())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )

class obj_scene_ch8pondfish_withgun(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondeat())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_fishing_withgun(self)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )

# Replaced with electric fish scene
class obj_scene_ch8pondfish_withscissors(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondeat())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        # self.world=world.obj_world_fishing_withscissors(self)
        self.world=world.obj_world_fishing_withgun(self,electricfish=True)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )


class obj_scene_ch8pondeat(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8pondreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )


class obj_scene_ch8pondreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8pondfish())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8pondfish_withgun())
        elif share.datamanager.getword('numchoice')=='3':
            share.scenemanager.switchscene(obj_scene_ch8pondfish_withscissors())
        else:
            share.scenemanager.switchscene(obj_scene_ch8pondbye())
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"',\
                '"Do you want to fish again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='1')
        textchoice.addchoice('1. Hook','1',(640-300,y1))
        textchoice.addchoice('2. Gun','2',(640-100,y1))
        textchoice.addchoice('3. Electric Fish','3',(640+100,y1))
        textchoice.addchoice('4. Nevermind','4',(640+300,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero1", [101],skip=1 )
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )


class obj_scene_ch8pondbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='pond'))
    def setup(self):
        self.text=['"Alright bye". ']
        #
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch1_awaken','herobase',(640+100,360),scale=0.7)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero3", [35] )
        animation1.addsound( "hero5", [105],skip=1 )
        #
        # self.addpart( draw.obj_music('piano') )
        self.addpart( draw.obj_music('hero') )


###########
# mech
class obj_scene_ch8mech(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='mech'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech2())
    def setup(self):
        self.text=['"',('super-mech-hero',share.colors.hero),', assemble!" ']
        # Mech buildup
        animation1=draw.obj_animation('ch7_villainmech_assemble1','herobase',(640,360),record=False,imgfliph=True)
        animation1.addimage('heromecharmature')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_assemble_larm','fish',(640,360),record=False,imgfliph=True)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_assemble_rarm','scissors',(640,360),record=False,imgfliph=True,imgflipv=True)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch7_villainmech_assemble_lleg','sailboat',(640-10,360),record=False,imgscale=0.7)
        animation4.addimage('empty',path='data/premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch7_villainmech_assemble_rleg','sailboat',(640+10,360),record=False,imgscale=0.7)
        animation5.addimage('empty',path='data/premade')
        self.addpart( animation5 )
        animation6=draw.obj_animation('ch7_villainmech_assemble_lshoulder','bush',(640,360),record=False)
        animation6.addimage('empty',path='data/premade')
        self.addpart( animation6 )
        animation7=draw.obj_animation('ch7_villainmech_assemble_rshoulder','bush',(640,360),record=False)
        animation7.addimage('empty',path='data/premade')
        self.addpart( animation7 )
        animation8=draw.obj_animation('ch7_villainmech_assemble_tpp','house',(640,360),record=False)
        animation8.addimage('empty',path='data/premade')
        self.addpart( animation8 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_transform1','mech_transform2') )
        animation8.addsound( "hero2", [2] )
        animation8.addsound( "mech_transform1", [70] )
        animation8.addsound( "mech_transform2", [170],skip=1 )
        # animation8.addsound( "villain2", [270],skip=1 )
        #
        self.addpart( draw.obj_music('mechs') )

class obj_scene_ch8mech2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech3())
    def setup(self):
        self.text=['"',('super-mech-hero',share.colors.hero),', expand!" ']
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heromech_expand','heromechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # animation1.addsound( "villain1", [2] )
        animation1.addsound( "mech_transform1", [1] )
        animation1.addsound( "mech_transform2", [101] )
        animation1.addsound( "hero5", [201],skip=1 )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch8mech3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mech2())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8mechfightstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8mechbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=['"Do you want to replay the mech fight". ']
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain2", [150] )
        animation1.addsound( "mech_stomp", [21, 85, 151, 251, 309, 371] )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch8mechfightstandby(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechfight())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_mechfight(self,tutorial=True,prompt=False)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,230),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('mechfight') )


class obj_scene_ch8mechfight(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8mechreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_mechfight(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('mechfight') )


class obj_scene_ch8mechreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8mechfightstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8mechbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=['"That was a nice fight. Do you want to play again". ']
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain2", [150] )
        animation1.addsound( "mech_stomp", [21, 85, 151, 251, 309, 371] )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch8mechbye(page.obj_chapterpage):
    def prevpage(self):
        pass
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
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain4", [150] )
        animation1.addsound( "mech_stomp", [21, 85, 151, 251, 309, 371] )
        #
        self.addpart( draw.obj_music('mechs') )


###########
# west tower

class obj_scene_ch8west(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='tower'))
    def nextpage(self):
        trypassword=share.datamanager.getword('towerpassword')
        shouldpassword='abracada'+share.datamanager.getword('passwordend')
        if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
            share.scenemanager.switchscene(obj_scene_ch8westcorrectpassword())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westwrongpassword())
    def textboxset(self):
        self.textboxopt={'xy':(380,300),'text':'[enter]','align':'center'}
    def setup(self):
        shouldpassword='abracada'+share.datamanager.getword('passwordend')
        self.text=[\
                  '"Welcome back, blasted the tower\'s a.s.s. (automated security system). ',\
                  'Please enter the ',('password',share.colors.password),
                '". ',\
                   ]
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('towerpassword',30,(380,180), legend='tower password',default=shouldpassword)
        self.addpart( self.textinput )
        #
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation1.addsound( "tower1", [16, 79] )
        animation1.addsound( "tower2", [91] )
        animation1.addsound( "tower4", [99] )
        #
        self.addpart( draw.obj_music('tower') )

class obj_scene_ch8westwrongpassword(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8west())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8west())
    def setup(self):
        self.text=[\
                  '"Wrong, blasted the tower\'s ',\
                  'a.s.s., zapping engaged! Now try again". ',\
                   ]
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('towersparks',(1000,310),path='data/premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('tower5')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'tower_elec','tower_hurt') )
        animation1.addsound( "tower_elec", [1, 115,261] )
        animation1.addsound( "tower_hurt", [0,115,261],skip=1 )
        #
        self.addpart( draw.obj_music('tower') )

class obj_scene_ch8westcorrectpassword(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='tower'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westinside())
    def setup(self):
        self.text=[\
                  '"Password is correct. You may enter, said the tower\'s a.s.s."',\
                   ]
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heroenterstower','herobase',(640,360),record=False)
        self.addpart( animation1 )
        #
        animation1.addsound( "tower1", [48] )
        animation1.addsound( "tower2", [30,93] )
        animation1.addsound( "tower4", [42,] )
        animation1.addsound( "tower3", [108] )
        animation1.addsound( "tower6", [110],skip=1 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch8westinside(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='tower'))
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8westdodgebulletsstandby())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8weststompstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westbye())
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{villainname}',share.colors.villain),'. ',\
                'Do you want to fight again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='1')
        textchoice.addchoice('1. Guns','1',(420,y1))
        textchoice.addchoice('2. Fists','2',(640,y1))
        textchoice.addchoice('3. Not Really','3',(900,y1))
        self.addpart( textchoice )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        #
        self.addpart( draw.obj_music('villain') )



class obj_scene_ch8westdodgebulletsstandby(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westdodgebullets())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=[' Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_dodgegunshots(self,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch8westdodgebullets(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch8weststompstandby(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8weststomp())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_stompfight(self,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('fistfight') )



class obj_scene_ch8weststomp(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8westreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('fistfight') )


class obj_scene_ch8westreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('numchoice')=='1':
            share.scenemanager.switchscene(obj_scene_ch8westdodgebulletsstandby())
        elif share.datamanager.getword('numchoice')=='2':
            share.scenemanager.switchscene(obj_scene_ch8weststompstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8westbye())
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Nicely done, said ',\
                ('{villainname}',share.colors.villain),'. ',\
                'Do you to want to fight again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('numchoice',default='3')
        textchoice.addchoice('1. Guns','1',(420,y1))
        textchoice.addchoice('2. Fists','2',(640,y1))
        textchoice.addchoice('3. Nope','3',(900,y1))
        self.addpart( textchoice )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch8westbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='tower'))
    def setup(self):
        self.text=[\
                '"Alright bye, said ',\
                ('{villainname}',share.colors.villain),'." ',\
                   ]
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        #
        self.addpart( draw.obj_music('villain') )


###########
# east forest
class obj_scene_ch8east(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='forest'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8eastshoot())
        else:
            share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                'Do you want to play the shooting game. '\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny4", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch8eastshoot(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8eastreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['shoot all the ',('monsters',share.colors.bunny),'.']
        self.world=world.obj_world_3dforest_rabbitshoot(self)# fishing mini-game
        self.addpart(self.world)
        self.world.addstartfightmessage()# add start fight message
        self.addpart( draw.obj_music('bunny') )

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
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [128] )
        animation1.addsound( "bunny2", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch8eastreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8eastshoot())
        else:
            share.scenemanager.switchscene(obj_scene_ch8eastbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"That was fun. Do you want to play again'\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        #
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [128] )
        animation1.addsound( "bunny2", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )

###########
# north peak
class obj_scene_ch8north(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='peak'))
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northtop())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )

class obj_scene_ch8northtop(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8north_rpsstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8northbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{eldername}',share.colors.elder),'. ',\
                'Do you want to play rock-paper-scissors." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
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
        self.addpart( draw.obj_image('floor4',(1280-500,720-140),path='data/premade') )
        animation1=draw.obj_animation('ch5_meetelder','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch5_meetelder2','sun',(640,360),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [111],skip=1 )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch8north_rpsstandby(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8north_rps())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch8north_rps(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8northreplay())
    def triggernextpage(self,controls):
        return self.world.done# CANT SKIP THIS ONE
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch8northreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8north_rpsstandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8northbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"That was a nice game, said ',\
                ('{eldername}',share.colors.elder),'. Do you want to play again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks3','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder5", [36] )
        animation1.addsound( "elder4", [200], skip=1 )
        #
        self.addpart( draw.obj_music('elder') )


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
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks3','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder2", [200], skip=1 )
        animation1.addsound( "elder3", [36] )
        #
        self.addpart( draw.obj_music('elder') )


###########
# south beach
class obj_scene_ch8south(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='beach'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8southridestandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8southbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"Welcome back, said ',\
                ('{sailorname}',share.colors.sailor),'. ',\
                'Do you want to ride ',('treasure',share.colors.cow),' again." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [169] )
        animation1.addsound( "sailor4", [110] )
        animation1.addsound( "sailor5", [32],skip=1 )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch8southridestandby(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southride())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.textkeys={'pos':(100,20),'xmin':100}
        self.world=world.obj_world_ridecow(self,tutorial=True,trees=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('racing') )


class obj_scene_ch8southride(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southreplay())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8southreplay())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[' ']
        self.world=world.obj_world_ridecow(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('cow')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('racing') )


class obj_scene_ch8southreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8southridestandby())
        else:
            share.scenemanager.switchscene(obj_scene_ch8southbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"That was nice. Do you want to play again".',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch6sailortalks3love','cow',(640,360),record=False,sync=animation1)
        self.addpart(animation2)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5','cow') )
        animation1.addsound( "sailor4", [40] )
        animation1.addsound( "cow", [110],skip=1 )
        #
        self.addpart( draw.obj_music('sailor') )


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
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [41, 153] )
        animation1.addsound( "sailor4", [261] )
        #
        self.addpart( draw.obj_music('sailor') )


###########
# skull island
class obj_scene_ch8island(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='island'))
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"',\
                'Do you want to sneak around." ',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
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
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero1", [15] )
        animation1.addsound( "hero3", [50],skip=1 )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandsneak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak1())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
       self.text=[' ']
       self.world=world.obj_world_bushstealth0(self)
       self.addpart(self.world)
       #
       self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandsneak1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak2())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak1())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
       self.text=[' ']
       self.world=world.obj_world_bushstealth(self)
       self.addpart(self.world)
       #
       self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandsneak2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak3())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak2())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
       self.text=[' ']
       self.world=world.obj_world_bushstealth2(self)
       self.addpart(self.world)
       #
       self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandsneak3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak4())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak3())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
       self.text=[' ']
       self.world=world.obj_world_bushstealth3(self)
       self.addpart(self.world)
       #
       self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandsneak4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch8islandreplay())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch8islandreplay())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandsneak4())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
       self.text=[' ']
       self.world=world.obj_world_bushstealth4(self,winsound='stealth_win')
       self.addpart(self.world)
       #
       self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandreplay(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch8islandsneak())
        else:
            share.scenemanager.switchscene(obj_scene_ch8islandbye())
    def textboxset(self):
        self.textboxopt={'xy':(550,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                '"That was fun. Do you want to play again".',\
                   ]
        y1=200
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(450,y1))
        textchoice.addchoice('2. No','no',(650,y1))
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
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero3", [15] )
        animation1.addsound( "hero5", [80],skip=1 )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch8islandbye(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch8roam(start='island'))
    def setup(self):
        self.text=[\
                '"Alright, bye".',\
                   ]
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
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero1", [30] )
        animation1.addsound( "hero2", [100],skip=1 )
        #
        self.addpart( draw.obj_music('stealth') )


#################################################################
#################################################################







#
