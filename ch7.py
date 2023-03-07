#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter7.py: ...
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

# Chapter VII: ...
# *CHAPTER VII


class obj_scene_chapter7(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p1())
    def setup(self):
        share.datamanager.setbookmark('ch7_start')
        self.text=['-----   Chapter VII: Showtime   -----   ',\
                   '\n It was the next day when the book of things said to the pen and the eraser: ',\
                  'well, this is it, we are reaching the climax of our story. ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','pen','eraser') )
        animation1.addsound( "book1", [120] )
        animation1.addsound( "pen", [199] )
        animation1.addsound( "eraser", [185],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p2())
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' has visited all the ',\
                    ('grandmasters',share.colors.grandmaster2),' and figured the tower\'s ',\
                    ('password',share.colors.password),'. ',\
                    'Today ',('{hero_he}',share.colors.hero2),' can finally confront ',\
                    ('{villainname}',share.colors.villain),' and rescue ',\
                    ('{partnername}',share.colors.partner),'." ',\
                   ]

        # self.addpart( draw.obj_image('mountain',(1177,324),scale=0.46,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(996,367),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(74,361),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(1120,228),scale=0.37,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart(draw.obj_image('cluesparkles',(754,418),scale=1,path='data/premade'))
        animation1=draw.obj_animation('ch3_bugtalks3intmark','herohead',(137,564),imgscale=0.25)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','villainhead',(374,346),imgscale=0.25,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','partnerhead',(1080,460),sync=animation1,imgscale=0.5) )

        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4') )
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "hero2", [40] )
        animation1.addsound( "villain1", [80] )
        animation1.addsound( "partner2", [151],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p3())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch7_startstory')
        self.text=[\
                'Better be ready for this!: "It was the next day and the sun was rising."',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p5())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' and ',\
                ('{bug}',share.colors.bug),\
                ' woke up." '\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch7') )



class obj_scene_ch7p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p7())
    def setup(self):
        share.datamanager.setbookmark('ch7_checkmail')
        self.text=[\
                  '"',\
                    # ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'two ',' letters." ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2  )
        # animation3=draw.obj_animation('ch2_mail4add','mailletter',(640,360),sync=animation1,record=False)
        # animation3.addimage('empty',path='data/premade')
        # self.addpart( animation3 )
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero2','mailjump') )
        animation1.addsound( "hero2", [80,120,190] )
        animation1.addsound( "mailjump", [10,50,100],skip=1 )
        #
        self.addpart( draw.obj_music('ch7') )




class obj_scene_ch7p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p8())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nCongratulations on completing all our challenges, that was cool. ',\
                    'Good luck fighting ',('{villainname}',share.colors.villain),'. ',\
                  '\n\nsigned: ',('the evil grandmasters',share.colors.grandmaster),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        # self.addpart( draw.obj_image('bunnyhead',(1065+60,305+50),scale=0.3) )
        # self.addpart( draw.obj_image('sailorhead',(1065-100,305),scale=0.3) )
        # self.addpart( draw.obj_image('elderhead',(1065,305-50),scale=0.3) )
        #
        self.addpart( draw.obj_animation('ch2_mailhead','bunnyhead',(640+60,360+50),imgscale=0.5) )
        self.addpart( draw.obj_animation('ch2_mailhead','sailorhead',(640-100,360),imgscale=0.5) )
        animation1=draw.obj_animation('ch2_mailhead','elderhead',(640,360-50),imgscale=0.5)
        self.addpart(animation1)
        #
        animation1.addsound( "bunny2", [40] )
        animation1.addsound( "elder1", [80] )
        animation1.addsound( "sailor2", [151],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #

        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p10())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI heard you cracked my tower\'s ',('password',share.colors.password),'. ',\
                    'Well done, whatever. ',\
                    'Come face me if you dare, I will be waiting for you. ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        # self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        #
        animation1=draw.obj_animation('ch2_mailhead','villainhead',(640,360),imgscale=0.7)
        self.addpart(animation1)
        animation1.addsound( "villain2", [100],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch7') )





class obj_scene_ch7p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p11())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch7_gototower')
        self.text=['go to the tower in the west']
        self.world=world.obj_world_travel(self,start='home',goal='tower',chapter=7,boat=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def setup(self):
        share.datamanager.setbookmark('ch7_putpassword1')
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' arrived at the evil tower. ',\
                  'The  tower\'s a.s.s. (automated security system) blasted: ',\
                  'oh, it is you again. Have you figured out the password." ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        #
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
        self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'tower1','tower2','tower3','tower4','tower5','tower6') )
        animation1.addsound( "tower1", [48] )
        animation1.addsound( "tower2", [30] )
        animation1.addsound( "tower4", [42] )
        #
        self.addpart( draw.obj_music('ch7') )

class obj_scene_ch7p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p11())
    def nextpage(self):
        trypassword=share.datamanager.getword('towerpassword')
        shouldpassword='abracada'+share.datamanager.getword('passwordend')
        if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
            share.scenemanager.switchscene(obj_scene_ch7p19())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p18fail())
    def textboxset(self):
        self.textboxopt={'xy':(380,300),'text':'[enter]','align':'center'}
    def setup(self):
        shouldpassword='abracada'+share.datamanager.getword('passwordend')
        self.text=[\
                  '"Go on, input something blasted the tower\'s a.s.s. (automated security system). ',\
                'I cannot wait to fry you again."'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
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
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p18fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def setup(self):
        trypassword=share.datamanager.getword('towerpassword')
        self.text=[\
                  '"You have entered: ',('"'+trypassword+'"',share.colors.password),' . ',\
                  'Wrong password, blasted the ',('tower',share.colors.location2),\
                  '\'s a.s.s., zapping engaged!" ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('towersparks',(1000,310),path='data/premade') )
        #
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
        self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
        # self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
        #
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
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p19(page.obj_chapterpage):# NB: jump to here from first password input in chapt 7
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p20())
    def setup(self):
        share.datamanager.setbookmark('ch7_putpassword2')
        trypassword=share.datamanager.getword('towerpassword')
        self.text=[\
                '"You have entered: ',(trypassword,share.colors.password),\
                ', blasted the ',('tower',share.colors.location2),\
                '\'s a.s.s. That is correct, you may now enter." '\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('towersparks',(1000,310),path='data/premade') )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        #
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
        self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
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
        self.addpart( draw.obj_music('tension') )



class obj_scene_ch7p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21())
    def setup(self):
        self.text=[\
                  '"Now lets get in and kick ',\
                ('{villainname}',share.colors.villain),'\'s butt, said ',\
                ('{bug}',share.colors.bug),'." ',\

                   ]
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        #
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
        self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch7_heroenterstower','herobase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21a())
    def setup(self):
        self.text=[\
                  '"',\
                    'Well well, you have finally figured out the password, ',\
                  'said ',('{villainname}',share.colors.villain),'. ',\
                  'Fool, you have just earned yourself a beating." ',\
                   ]
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        # self.addpart( draw.obj_imageplacer(self,'mountain') )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain3", [40] )
        animation1.addsound( "villain1", [140],skip=1 )
        #
        self.addpart( draw.obj_music('ch7') )


class obj_scene_ch7p21a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21b())
    def setup(self):
        share.datamanager.setbookmark('ch7_startdodge')
        self.text=[\
                  '"I will not let you win this time, said ',\
                  ('{villainname}',share.colors.villain),'."',\
                   ]
        self.addpart( draw.obj_image('floor1',(640,500),path='data/premade') )
        self.addpart( draw.obj_image('herobase',(200,500-50),scale=0.5) )
        self.addpart( draw.obj_image('villainbase',(1280-150,450-50),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('gun',(1280-150-175,445-50),scale=0.25,fliph=True) )
        self.addpart( draw.obj_image('stickshootarm',(1280-260,442-50),scale=0.5,path='data/premade') )# missing small piece
        #
        self.sound=draw.obj_sound('villain2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p21b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p22())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=[' Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_dodgegunshots(self,tutorial=True,intower=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )

class obj_scene_ch7p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21b())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch7p23())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p22death())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_dodgegunshots(self,intower=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch7p22death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21b())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch7p21b())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p23())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24())
    def setup(self):
        self.text=[\
                  '"This isnt over yet, said ',\
                    ('{villainname}',share.colors.villain),\
                    '. I am going to crush you with my bare hands." ',\
                   ]
        animation1=draw.obj_animation('ch7_villainsays1','villainbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('revealscary')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain1", [172],skip=1 )
        #
        self.addpart( draw.obj_music(None) )


class obj_scene_ch7p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24a())
    def textboxset(self):
        self.textboxopt={'xy':(1230-80,620)}
    def setup(self):
        share.datamanager.setbookmark('ch7_startstomp')
        self.text=[\
                  'Instructions: ',\
                    'move with ','['+share.datamanager.controlname('arrows')+'/',\
                    share.datamanager.controlname('right')+']',', ',\
                    ' jump with ','['+share.datamanager.controlname('up')+']',\
                    ' and kick with ','['+share.datamanager.controlname('action')+']','. ',\
                   ]
        self.world=world.obj_world_stompfight(self,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        self.world.text_undone.show=False
        #
        self.addpart( draw.obj_music('fistfight') )


class obj_scene_ch7p24a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24b())
    def textboxset(self):
        self.textboxopt={'xy':(1230-80,620)}
    def setup(self):
        self.text=[\
                  'Kick ',\
                  ('{villainname}',share.colors.villain),' to bring ',\
                  ('{villain_his}',share.colors.villain2),' health down. ',\
                   ]
        self.world=world.obj_world_stompfight(self,tutorial=True)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show1',(1130,360),path='data/premade',flipv=True))
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('fistfight') )


class obj_scene_ch7p24b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p25())
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


class obj_scene_ch7p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24b())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch7p26())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p25death())
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


class obj_scene_ch7p25death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24b())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch7p24b())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p26())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )



class obj_scene_ch7p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27())
    def setup(self):
        share.datamanager.setbookmark('ch7_winstomp')
        self.text=[\
                  '"',\
                  ('{heroname}',share.colors.hero),' was victorious. ', \
                  ('{villainname}',share.colors.villain),' shouted: I will have my revenge! ', \
                  'And ',('{villain_he}',share.colors.villain2),\
                  ' disappeared into the mountains." ', \
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_image('cloud',(1189,210),scale=0.33,rotate=2,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(360,245),scale=0.32,rotate=2,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )
        #
        self.addpart( draw.obj_music('victory') )

class obj_scene_ch7p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27a())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{heroname}',share.colors.hero),' reunited with ',\
                  ('{partnername}',share.colors.partner),'. ',\
                  ' and they were so excited." ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_image('cloud',(1189,210),scale=0.33,rotate=2,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(360,245),scale=0.32,rotate=2,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
        #
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('victory') )


class obj_scene_ch7p27a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p28())
    def setup(self):
        self.text=[\
                  '"',('{bug}',share.colors.bug),\
                  ' emerged and said: ',\
                  'it looks like my job is done, but i really like it here. ',\
                   'Could I stay and live with you." ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_image('cloud',(1189,210),scale=0.33,rotate=2,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        #
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_bugtalks','bug',(840,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 100] )
        animation1.addsound( "bug2", [116])
        #
        self.addpart( draw.obj_music('victory') )


class obj_scene_ch7p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p29())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{partnername}',share.colors.partner),' said: ',\
                  'this little thing is ',\
                  ('soooo cuuuute',share.colors.partner),'! ',\
                  'Of course you can stay with us." ',\
                   ]
        # self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_image('cloud',(1189,210),scale=0.33,rotate=2,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        self.addpart( draw.obj_image('partnerbase',(382,612+20),scale=1.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(140,646+20),scale=1.2,rotate=0,fliph=False,flipv=False) )
        #
        animation1=draw.obj_animation('ch7_bugtalks','bug',(840,360),record=False)
        self.addpart( animation1 )
        #
        animation2=draw.obj_animation('ch7_bugtalkslove','love',(840,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart(animation2)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2','partner1','partner2') )
        animation1.addsound( "bug1", [15, 100] )
        animation1.addsound( "bug2", [116])
        animation1.addsound( "partner1", [154] )
        animation1.addsound( "partner2", [252] )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('victory') )


class obj_scene_ch7p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p30())
    def setup(self):
        self.text=[\
                    'Well, it looks like everything is working out, said the book of things. ',
                   'You made it, congratulations! ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_image('cloud',(1189,210),scale=0.33,rotate=2,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(360,245),scale=0.32,rotate=2,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch5whatbook1','book',(640-200,360+40),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','exclamationmark',(640-200,360+40),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('victory') )


class obj_scene_ch7p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p31())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch7_gohome')
        self.text=[\
                'go back home ',\
                   ]
        self.world=world.obj_world_travel(self,start='tower',goal='home',chapter=7,boat=True,partner=True)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music(None) )


class obj_scene_ch7p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p32())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' and ',\
                    ('{partnername}',share.colors.partner),' were so happy to be home. ',\
                    'They ate a ',\
                    # ('{heroname}',share.colors.hero),' and ',\
                    # ('{partnername}',share.colors.partner),' ate the ',\
                    ('fish',share.colors.item2),' for dinner." ',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p33())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade... ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p34())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"...and then they kissed. It was the ',\
                   ('best kiss ever',share.colors.partner),'!"   ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p35())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"It was already night."',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p36())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),', ',('{partnername}',share.colors.partner),\
                   ' and ',('{bug}',share.colors.bug),\
                   ' went to bed." ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True,alarmclock=False,bug=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p37())
    def setup(self):
        self.text=[\
                   '"Then, right before falling asleep, ',\
                   ('{heroname}',share.colors.hero),' made the biggest smile ever." ',\
                   ]
        # self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p38())
    def setup(self):
        self.text=[\
                '"',('{hero_he}',share.colors.hero),' was reunited with ',\
                ('{partnername}',share.colors.partner),' and they would live happily ever after. ',\
               ' It was almost the end of the story..." ',\
                   ]
        self.addpart(  draw.obj_image('horizon',(640,720-150),path='data/premade') )
        self.addpart(  draw.obj_image('house',(296,443),scale=0.5) )
        self.addpart(  draw.obj_image('bush',(827,452),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart(  draw.obj_image('bush',(486,648),scale=0.32,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(186,615),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(101,567),scale=0.28,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(102,440),scale=0.28,rotate=0,fliph=True,flipv=False) )
        #
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p39())
    def setup(self):
        self.text=[\
                   '"...when ',\
                   ('{heroname}',share.colors.hero),' heard a knock on the door. ',\
                   'Who could it possibly be at this hour."',\
                   ]
        # self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        animation1= draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5)
        self.addpart(animation1)
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase') )
        animation2=draw.obj_animation('ch7_knockondoor','interrogationmark',(840,360),record=False,sync=animation1,path='data/premade')
        self.addpart(animation2)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero_what','wakeup_wake1','villain_bangdoor') )
        animation1.addsound( "villain_bangdoor", [43, 61, 81, 203, 221, 241],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p40())
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' woke back up and went to open the door." ',\
                   ]
        # self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        # self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        animation1= draw.obj_animation('ch7_knockondoor2','herobase',(640,360),record=False)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch7_knockondoor2aa','interrogationmark',(840,360),record=False,sync=animation1,path='data/premade')
        animation2.addimage('empty',path='data/premade')
        self.addpart(animation2)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero_what','wakeup_wake1','villain_bangdoor') )
        animation1.addsound( "hero_what", [5] )
        # animation1.addsound( "villain_bangdoor", [43, 61, 81],skip=1 )
        animation1.addsound( "villain_bangdoor", [43, 61, 81, 203, 221, 241],skip=1 )
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p41())
    def setup(self):
        share.datamanager.setbookmark('ch7_villainagain')
        self.text=[\
                  '"',\
                    ('{villainname}',share.colors.villain),' was outside the house! ',\
                    ('{villain_he}',share.colors.villain2),' said: ',\
                    'muahaha, I told you I would be back. I have one last trick up my sleeve for you." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'house','bush','cloud','moon','mailbox') )
        self.addpart( draw.obj_image('moon',(235,250),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1201,342),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(464,228),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1060,286),scale=0.29,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1201,193),scale=0.22,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainsays1','villainbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain2", [140],skip=2 )
        #
        self.sound=draw.obj_sound('revealscary')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p42())
    def setup(self):
        self.text=['"Now watch this: ',('super-mech-{villainname}',share.colors.villain),', assemble!" ']
        # Mech buildup
        animation1=draw.obj_animation('ch7_villainmech_assemble1','villainbase',(640,360),record=False)
        animation1.addimage('villainmecharmature')
        self.addpart( animation1 )

        animation2=draw.obj_animation('ch7_villainmech_assemble_larm','gun',(640,360),record=False)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_assemble_rarm','lightningbolt',(640,360),record=False)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch7_villainmech_assemble_lleg','cave',(640,360),record=False)
        animation4.addimage('empty',path='data/premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch7_villainmech_assemble_rleg','cave',(640,360),record=False)
        animation5.addimage('empty',path='data/premade')
        self.addpart( animation5 )
        animation6=draw.obj_animation('ch7_villainmech_assemble_lshoulder','mountain',(640,360),record=False)
        animation6.addimage('empty',path='data/premade')
        self.addpart( animation6 )
        animation7=draw.obj_animation('ch7_villainmech_assemble_rshoulder','mountain',(640,360),record=False)
        animation7.addimage('empty',path='data/premade')
        self.addpart( animation7 )
        animation8=draw.obj_animation('ch7_villainmech_assemble_tpp','tower',(640,360),record=False)
        animation8.addimage('empty',path='data/premade')
        self.addpart( animation8 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_transform1','mech_transform2') )
        animation8.addsound( "villain1", [2] )
        animation8.addsound( "mech_transform1", [70] )
        animation8.addsound( "mech_transform2", [170],skip=1 )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p43())
    def setup(self):
        self.text=['"and now: ',\
                ('super-mech-villain',share.colors.villain),', expand!" ']
        #
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','cloud','moon') )
        # self.addpart( draw.obj_image('herobase',(503,629),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('house',(101,617),scale=0.41,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('moon',(317,239),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(283,467),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(90,405),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(543,430),scale=0.3,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_grow','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_grow2','herobase',(640-50,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_grow3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        #
        # animation1.addsound( "villain1", [2] )
        animation1.addsound( "mech_transform1", [1] )
        animation1.addsound( "mech_transform2", [101] )
        animation1.addsound( "villain4", [201],skip=1 )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p42())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p44())
    def setup(self):
        self.text=['"Muahaha, this is too easy, said ',('{villainname}',share.colors.villain),\
                    '. My ',('super-mech-villain',share.colors.villain),\
                    ' is going to crush you like a worm!" ']
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','cloud','moon') )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain2", [150] )
        animation1.addsound( "mech_stomp", [21, 85, 151, 251, 309, 371] )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p45())
    def setup(self):
        self.text=[\
            '"Suddendly, the  ',('evil grandmasters',share.colors.grandmaster),' appeared and said: ',\
            'not so fast ',('{villainname}',share.colors.villain),'! ',\
            ('{heroname}',share.colors.hero),' deserves a fair fight, ',\
            'surely you wont mind if we help  ',\
            ('{hero_him}',share.colors.hero2),' a bit." ',\
                ]
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','bush','cloud','moon','bunnybase','elderbase','sailorbase') )
        # self.addpart( draw.obj_image('bunnybase',(723,512),scale=0.65,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('elderbase',(500,431),scale=0.65,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('sailorbase',(277,449),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('house',(1041,376),scale=0.48,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(869,277),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(81,478),scale=0.38,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_masters1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_masters2','elderbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_masters3','sailorbase',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        #
        animation1.addsound( "bunny2", [60] )
        animation1.addsound( "elder4", [100] )
        animation1.addsound( "sailor5", [171],skip=1 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p45(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p46())
    def setup(self):
        self.text=['"Lets goooo, said the grandmasters: ',('super-mech-hero',share.colors.hero),', assemble!" ']

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


class obj_scene_ch7p46(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p45())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p47())
    def setup(self):
        self.text=['"and now: ',('super-mech-hero',share.colors.hero),', expand!" ']
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','heromechbase','house','cloud','moon') )
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('heromechbase',(303,412),scale=0.81,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heromech_expand','heromechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # animation1.addsound( "villain1", [2] )
        animation1.addsound( "mech_transform1", [1] )
        animation1.addsound( "mech_transform2", [101] )
        animation1.addsound( "hero5", [201],skip=1 )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p47(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p46())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48())
    def setup(self):
        self.text=['"Muahaha, said ',\
                ('{villainname}',share.colors.villain),', even like this you dont stand a chance. ',\
                'Now bring it on!" ']
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','cloud','moon') )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain2", [150] )
        animation1.addsound( "mech_stomp", [21, 85, 151, 251, 309, 371] )
        #
        self.addpart( draw.obj_music('mechs') )


class obj_scene_ch7p48(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p47())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48a())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,220)}
    def setup(self):
        share.datamanager.setbookmark('ch7_startmech')
        self.text=[\
                    'Oh boy, that is one epic fight, said the book of things. ',\
                    'Lets get started. ',\
                   ]
        self.world=world.obj_world_mechfight(self,tutorial=True,prompt=False)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('(not the actual fight)',(250,220),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('mechfight') )


class obj_scene_ch7p48a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48b())
    def textboxset(self):
        self.textboxopt={'xy':(1280-180,220)}
    def setup(self):
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
                    'Instructions: using '+tempo+', ',\
                    'enter the correct command quickly when prompted. ',\
                   ]
        self.world=world.obj_world_mechfight(self,tutorial=True)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show3',(440,270),scale=1,path='data/premade',fliph=True))
        self.addpart( draw.obj_textbox('(not the actual fight)',(250,220),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('mechfight') )


class obj_scene_ch7p48b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48c())
    def textboxset(self):
        self.textboxopt={'xy':(1280-180,220)}
    def setup(self):
        self.text=[\
                  'Hit ',\
                  ('{villainname}',share.colors.villain),' to bring ',\
                  ('{villain_his}',share.colors.villain2),' health down. '\
                   ]
        self.world=world.obj_world_mechfight(self,tutorial=True)#,prompt=False)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show1',(487,232),scale=0.75,fliph=True,flipv=True,path='data/premade'))
        self.addpart( draw.obj_textbox('(not the actual fight)',(250,220),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('mechfight') )


class obj_scene_ch7p48c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p49())
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


class obj_scene_ch7p49(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48c())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch7p50())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p49death())
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


class obj_scene_ch7p49death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48c())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch7p48c())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p50())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )



class obj_scene_ch7p50(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p49())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p51())
    def setup(self):
        share.datamanager.setbookmark('ch7_winmech')
        self.text=[\
            '"The  ',('super-mech-villain',share.colors.villain),\
            ' fell over and started smoking. ',\
            'Ugh, I guess you won, said ',('{villainname}',share.colors.villain),'. Well played, I admit my defeat."',\
                ]
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase_noface','villainbase','moon','heromechbase','cloud','house','bush') )
        self.addpart( draw.obj_image('villainmechbase_noface',(1029,524),scale=0.73,rotate=-118,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7villainfrommec','villainbase',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        self.addpart( animation1 )
        self.addpart( draw.obj_image('bush',(129,606),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(760,582),scale=0.23,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(539,601),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(195,310),scale=0.46,rotate=0,fliph=False,flipv=False) )
        # animation2=draw.obj_animation('ch7villainfrommec_cloud1','cloud',(640,360),record=False,sync=animation1)
        # self.addpart( animation2 )
        self.addpart( draw.obj_animation('ch7villainfrommec_cloud1','cloud',(820,300),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch7villainfrommec_cloud1','cloud',(980,222),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch7villainfrommec_cloud1','cloud',(1202,320),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','mech_stomp') )
        animation1.addsound( "villain1", [115] )
        animation1.addsound( "villain4", [181],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch7p51(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p50())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p52())
    def setup(self):
        self.text=[\
            '"The  ',('grandmasters',share.colors.grandmaster),' shouted: ',\
            'Loooser, loooser! ',\
            'You still have a lot to learn about the evil ways ',('{villainname}',share.colors.villain),', ',\
            'go back to training immediately." ',\
                ]
        self.addpart( draw.obj_image('house',(1041,376),scale=0.48,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(869,277),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(81,478),scale=0.38,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_masters1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_masters2','elderbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_masters3','sailorbase',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        #
        animation1.addsound( "bunny2", [60] )
        animation1.addsound( "elder4", [100] )
        animation1.addsound( "sailor5", [171],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p52(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p51())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p53())
    def setup(self):
        self.text=[\
            '"Now its time to party, said the  ',('grandmasters',share.colors.grandmaster),'. ',\
            'Absolutely everyone is here! ',\
            'Why because it is the end of the story silly." ',\
                ]
        self.addpart( draw.obj_image('fish',(1177,642),scale=0.28,rotate=15,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_endwobble1','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch7_endwobble2','sailorbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble','bunnybase',(640-160,360+80),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble3','skeletonbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble3','skeletonbase_sailorhat',(640+100,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble4','cow',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble6','partnerbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble5','herobase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble7','villainbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble8','bug',(640,360),sync=animation1,record=False) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'cheer') )
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        # self.addpart( draw.obj_soundplacer(animation1,'partner1','partner2','partner3') )
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        # self.addpart( draw.obj_soundplacer(animation1,'tower1','tower2','tower3','tower4','tower5','tower6') )
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5','bunny6') )
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4','elder5','elder6') )
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5','sailor6') )
        # self.addpart( draw.obj_soundplacer(animation1,'cow') )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7p53(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p52())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7ending())
    def setup(self):
        share.datamanager.setbookmark('ch7_drawcake')
        self.text=[\
            'Draw a ',('cake',share.colors.item),', said the book of things. Lets celebrate! ',\
                ]
        self.addpart( draw.obj_drawing('cakedraw',(640,450-50),legend='Cake',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7ending(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p53())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7ending2())
    def gameendingtext(self):
        self.addpart( draw.obj_textbox('Thank you for playing',(640,100),fontsize='large') )
    def setup(self):
        self.text=[' ']
        #
        # background
        # self.addpart( draw.obj_image('mountain',(80,190),scale=0.29,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tower',(220,200),scale=0.25,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('house',(325,201),scale=0.3,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(357,273),scale=0.16,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(50,235),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(142,259),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(215,255),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(309,278),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('house',(449,289),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(248,309),scale=0.15,rotate=0,fliph=True,flipv=False) )
 #
        self.addpart( draw.obj_image('moon',(1035,72),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,161),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1135,145),scale=0.2,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1015,178),scale=0.2,rotate=0,fliph=False,flipv=False) )
 #


        y1=60
        self.addpart( draw.obj_image('cave',(856,228+y1),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(762,245+y1),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(701,210+y1),scale=0.2,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(941,235+y1),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(902,175+y1),scale=0.15,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(1209,163+y1),scale=0.15,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1168,223+y1),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1257,210+y1),scale=0.2,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1108,185+y1),scale=0.15,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1045,213+y1),scale=0.2,rotate=0,fliph=True,flipv=False) )
        #
        # foreground
        self.addpart( draw.obj_image('fish',(1177,642),scale=0.3,rotate=15,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_endwobble1','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch7_endwobble2','sailorbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble','bunnybase',(640-160,360+80),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble3','skeletonbase_sailorhat',(640,360+50),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble3','skeletonbase',(640+100,360+50),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble4','cow',(640+20,360+20),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble6','partnerbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble5','herobase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble7','villainbase',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_animation('ch7_endwobble8','bug',(640,360),sync=animation1,record=False) )
        self.addpart( draw.obj_image('cake',(680,549),scale=0.51,rotate=0,fliph=False,flipv=False) )
        # self.addpart(draw.obj_imageplacer(self,'house','bush','tower','tree','mountain','cave','tree','palmtree','sailboat','wave','skeletonhead','moon','cloud'))
        #
        # text
        self.gameendingtext()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7ending2(obj_scene_ch7ending):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7ending())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7end())
    def gameendingtext(self):
        self.addpart( draw.obj_textbox('The End',(640,100),fontsize='huge') )

class obj_scene_ch7end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7ending2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7endend())
    def setup(self):
        self.text=['This is goodbye, said the book of things. ',\
                   'But come back anytime! ',\
                   ]
        animation1=draw.obj_animation('bookmove','book',(640,360))
        self.addpart( animation1 )
        #
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book1", [149] )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7endend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7end())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7unlocknext())
    def setup(self):
        self.text=['The book vanished... ']
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch7unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7end())
    def setup(self):
        share.datamanager.setbookmark('ch7_endunlock')
        self.text=['You have unlocked the ',\
                    ('epilogue',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=8)# chapter 8 (epilogue))
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )


#########################################################################


# remove fishing (repetitive)
# class obj_scene_ch7p4(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p3())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p5())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                     '        ',\
#                     '"',('{hero_he}',share.colors.hero),\
#                      ' went to the lake and caught an electric fish.',\
#                        '"\n ',\
#                    ]
#         self.world=world.obj_world_fishing_withgun(self,electricfish=True)# fish shoots lightning bolts
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('ch7') )


# class obj_scene_ch7p6(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p5())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p7())
#     def textboxset(self):
#         self.textboxopt={'xy':(1230-180,55)}
#     def setup(self):
#         self.addpart( draw.obj_textbox('"The first letter said:"',(50,53),xleft=True) )
#         xmargin=100
#         ymargin=230
#         self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
#         self.text=[\
#                     'Dear ',('{heroname}',share.colors.hero),', ',\
#                   '\nThanks again for finding my ',\
#                   ('treasure',share.colors.cow),\
#                   ', we should really get drunk sometime burp. ',\
#                   '\n\nsigned: ',('{sailorname}',share.colors.sailor),\
#                    ]
#         self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
#         # self.addpart( draw.obj_image('sailorhead',(1065,305),scale=0.5) )
#         #
#         animation1=draw.obj_animation('ch2_mailhead','sailorhead',(640,360),imgscale=0.7)
#         self.addpart(animation1)
#         animation1.addsound( "sailor2", [100],skip=1 )
#         #
#         self.sound=draw.obj_sound('mailopen')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch7') )

# class obj_scene_ch7p9(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p8())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p10())
#     def setup(self):
#         self.text=[\
#                   '"The ',('{bug}',share.colors.bug),\
#                   ' crawled out of ',('{heroname}',share.colors.hero),\
#                   '\'s pocket and said: ',\
#                    'What are we waiting for, lets hurry up to the ',\
#                    ('evil tower',share.colors.location2),' and rescue ',\
#                     ('{partnername}',share.colors.partner),'."',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )
#         #
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch7') )

#
# class obj_scene_ch7p12(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p11())
#     def nextpage(self):
#         trypassword=share.datamanager.getword('towerpassword')
#         shouldpassword='fight persevere overcome'
#         if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
#             share.scenemanager.switchscene(obj_scene_ch7p13())
#         else:
#             trypassword=share.datamanager.getword('towerpassword')
#             earlypassword='lie cheat steal'
#             if share.devmode or tool.comparestringparts(trypassword,earlypassword):
#                 share.scenemanager.switchscene(obj_scene_ch7p19())# shortcut
#             else:
#                 share.scenemanager.switchscene(obj_scene_ch7p12fail())
#     def textboxset(self):
#         self.textboxopt={'xy':(380,300),'text':'[enter]','align':'center'}
#     def setup(self):
#         self.text=[\
#                   '"Please enter ',('password',share.colors.password),', blasted the tower\'s a.s.s. ',\
#                 'Remember it is ',('"fight persevere overcome"',share.colors.password),\
#                 ', whispered the ',('{bug}',share.colors.bug),'". ',\
#                    ]
#         # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
#         # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         self.textinput=draw.obj_textinput('towerpassword',30,(380,180), legend='tower password',default='...')
#         self.addpart( self.textinput )
#         #
#         animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
#         self.addpart( animation1 )
#         animation1.addsound( "tower1", [16, 79] )
#         animation1.addsound( "tower2", [91] )
#         animation1.addsound( "tower4", [99] )
#         #
#         self.addpart( draw.obj_music('ch7') )
#
#
# class obj_scene_ch7p12fail(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p12())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p12())
#     def setup(self):
#         trypassword=share.datamanager.getword('towerpassword')
#         self.text=[\
#                   '"You have entered: ',('"'+trypassword+'"',share.colors.password),' . ',\
#                   'Wrong password, blasted the ',('tower',share.colors.location2),\
#                   '\'s a.s.s., zapping engaged!" ',\
#                    ]
#         # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
#         # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('towersparks',(1000,310),path='data/premade') )
#         #
#         # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
#         self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
#         #
#         animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
#         animation1.addimage('herozapped')
#         self.addpart( animation1 )
#         #
#         self.sound=draw.obj_sound('tower5')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'tower_elec','tower_hurt') )
#         animation1.addsound( "tower_elec", [1, 115,261] )
#         animation1.addsound( "tower_hurt", [0,115,261],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch7') )
#
#
#
# class obj_scene_ch7p13(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p12())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p14())
#     def setup(self):
#         self.text=[\
#                 '"You have entered: ',('"fight persevere overcome"',share.colors.password),' . ',\
#                 'Wait a minute, said the tower\'s a.s.s. ',\
#                 'These are the mottos from the ',('evil grandmasters',share.colors.grandmaster),'". ',\
#                    ]
#         # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
#         # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         #
#         # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
#         self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
#         self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
#         #
#         animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
#         self.addpart( animation1 )
#         #
#         animation1.addsound( "tower1", [48] )
#         animation1.addsound( "tower2", [30] )
#         animation1.addsound( "tower4", [42] )
#         #
#         self.sound=draw.obj_sound('bookscene')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('tension') )
#
#
#
# class obj_scene_ch7p14(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p13())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p15())
#     def setup(self):
#         self.text=[\
#                   '"WAHAAA, blasted the ',('tower',share.colors.location2),'\'s a.s.s., ',\
#                   ('"fight persevere overcome"',share.colors.password),\
#                   ' is not the correct password! ',\
#                   'It looks like the ',('grandmasters',share.colors.grandmaster),' have deceived you well". ',\
#                    ]
#         # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
#         # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('towersparks',(1000,310),path='data/premade') )
#         #
#         # self.addpart(draw.obj_imageplacer(self,'sun','cloud'))
#         self.addpart( draw.obj_image('cloud',(415,303),scale=0.27,rotate=4,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cloud',(576,242),scale=0.38,rotate=4,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
#         #
#         animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
#         animation1.addimage('herozapped')
#         self.addpart( animation1 )
#         #
#         self.sound=draw.obj_sound('tower5')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'tower_elec','tower_hurt') )
#         animation1.addsound( "tower_elec", [1, 115,261] )
#         animation1.addsound( "tower_hurt", [0,115,261],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch7') )
#
#
# class obj_scene_ch7p15(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p14())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p16())
#     def setup(self):
#         self.text=[\
#                   '"The ',('{bug}',share.colors.bug),\
#                   ' crawled out of ',('{heroname}',share.colors.hero),\
#                   '\'s pocket and whispered: ',\
#                    'This cannot be, lets review what we did wrong." ',\
#                    ]
#         self.addpart( draw.obj_image('herobaseangry',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )
#         #
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch7') )
#
#
# class obj_scene_ch7p16(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p15())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p17())
#     def setup(self):
#         self.text=[\
#                   '"The mottos from the ',('evil grandmasters',share.colors.grandmaster),\
#                   ' are: fight, persevere and overcome. ',\
#                   'These are the teachings that the grandmasters gave to ',('{villainname}',share.colors.villain),\
#                    ', and that ',('{villain_he}',share.colors.villain2),\
#                     ' has used for ',('{villain_his}',share.colors.villain2),\
#                     ' password. ',\
#                     '"']
#         x1=640
#         y1=360
#         dy1=55
#         self.addpart( draw.obj_textbox('fight',(x1-20,y1),xright=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox(' in any situation',(x1-20,y1),xleft=True) )
#         self.addpart( draw.obj_textbox('always',(x1,y1+dy1),xright=True) )
#         self.addpart( draw.obj_textbox(' persevere',(x1,y1+dy1),xleft=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox('overcome',(x1+32,y1+2*dy1),xright=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox(' everything',(x1+32,y1+2*dy1),xleft=True) )
#         # self.addpart(draw.obj_imageplacer(self,'bunnyhead','elderhead','sailorhead'))
#         self.addpart( draw.obj_image('bunnyhead',(369,544),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('elderhead',(259,351),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('sailorhead',(131,511),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch7_bugthinks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch7_bugthinks2','interrogationmark',(840,360),record=False,sync=animation1,path='data/premade')
#         animation2.addimage('empty',path='data/premade')
#         self.addpart( animation2 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [56, 140, 159] )
#         #
#         self.sound=draw.obj_sound('bookscene')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch7') )
#
#
# class obj_scene_ch7p17(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p16())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch7p18())
#     def setup(self):
#         self.text=[\
#                   '"Wait a minute, said the ',('{bug}',share.colors.bug),'. ',\
#                   'What the ',('grandmasters',share.colors.grandmaster),\
#                   ' really taught us is quite different. ',\
#                   'We learned to lie with the bunny, cheat with the elder, and steal with the sailor. ',\
#                   'Yes, thats it: ',\
#                   ('"lie cheat steal"',share.colors.grandmaster),\
#                   ' . That is the password!" ',\
#                   ]
#         x1=640-30
#         y1=360
#         dy1=55
#         self.addpart( draw.obj_textbox('lie',(x1-20,y1),xright=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox(' in any situation',(x1-20,y1),xleft=True) )
#         self.addpart( draw.obj_textbox('always',(x1+30,y1+dy1),xright=True) )
#         self.addpart( draw.obj_textbox(' cheat',(x1+30,y1+dy1),xleft=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox('steal',(x1+7,y1+2*dy1),xright=True,color=share.colors.grandmaster) )
#         self.addpart( draw.obj_textbox(' everything',(x1+7,y1+2*dy1),xleft=True) )
#         self.addpart( draw.obj_image('bunnyhead',(369,544),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('elderhead',(259,351),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('sailorhead',(131,511),scale=0.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch7_bugthinks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch7_bugthinks2','exclamationmark',(840,360),record=False,sync=animation1,path='data/premade')
#         animation2.addimage('empty',path='data/premade')
#         self.addpart( animation2 )
#         #
#         self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [50, 65, 144] )
#         animation1.addsound( "bug2", [158] )
#         #
#         self.sound=draw.obj_sound('unlock')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch7') )
