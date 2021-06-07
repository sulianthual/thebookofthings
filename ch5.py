#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter5.py: ...
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

# Chapter V: ...
# *CHAPTER V



class obj_scene_chapter5(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def setup(self):
        self.text=['-----   Chapter V: Higher and Higher  -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: lets see how our story is going so far. ',\
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



class obj_scene_ch5p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{heroname}',share.colors.hero),' is on a quest to ',\
                  ' figure out the password to ',('{villainname}',share.colors.villain),'\'s  ',\
                  ('castle',share.colors.location2),' and rescue ',\
                   ('{partnername}',share.colors.partner),'. ',\
                   'Three ',('grandmasters of deceit',share.colors.grandmaster),' hold the clues to the password, ',\
                   'and so far ',('{heroname}',share.colors.hero),\
                   ' has visited one of them".',\
                   ]
        # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='premade')
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark2','bunnyhead',(640,360),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4') )
        animation1.addsound( "bunny2", [40],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch5p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p3())
    def setup(self):
        self.text=[\
                  '"The first part of the password is ',('"fight"',share.colors.password),'. ',\
                  'Today, ',('{heroname}',share.colors.hero),\
                   ' and ',('{hero_his}',share.colors.hero2),\
                   ' friend the ',('{bug}',share.colors.bug),\
                    ' are on their way to meet the ',\
                    ('grandmaster of deceit',share.colors.grandmaster),\
                    ' that lives in the north". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 100] )
        animation1.addsound( "bug2", [116],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch5p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                'Ok here we go, lets write: "It was the next day and the sun was rising".',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p7())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'two ',' letters". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2  )
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero2','mailjump') )
        animation1.addsound( "hero2", [82,121] )
        animation1.addsound( "mailjump", [7,51] )
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p8())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nIts me again. ',\
                    'I am still waiting for you, but boy are you slow to pay me a visit. ',\
                    'I heard you met my former grandmaster the ',\
                    ('bunny',share.colors.bunny),'. Good for you, whatever. ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
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
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nYou are truly a great ',\
                  ('liar',share.colors.grandmaster),'. ',\
                    'Come back anytime to my ',\
                    ('magical cave',share.colors.location2),' if you want ',\
                    'more training in the ',('evil ways',share.colors.grandmaster2),'. ',\
                      'And remember my motto, "fight in any situation". ',\
                  '\n\nsigned: ',('{bunnyname}',share.colors.bunny),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        # self.addpart( draw.obj_image('bunnyhead',(1065,305-50),scale=0.5) )
        #
        animation1=draw.obj_animation('ch2_mailhead','bunnyhead',(640,360),imgscale=0.7)
        self.addpart(animation1)
        animation1.addsound( "bunny2", [100],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p10())
    def setup(self):
        self.text=[\
                   'Today, ',\
                  ('{heroname}',share.colors.hero),' must seek the ',\
                  ('grandmaster of deceit',share.colors.grandmaster),' of the north. ',\
                  'This  ',('grandmaster',share.colors.grandmaster2),' lives on top of the ',\
                  ('highest peak',share.colors.location2),'. ',\
                  ' It is so high up in the sky it is always covered by stormy clouds. ',\
                  'Draw a ',('cloud',share.colors.item),' and a ',\
                  ('lightning bolt',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('cloud',(340,450),legend='Cloud',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('lightningbolt',(940,450),legend='Lightning Bolt',shadow=(200,200)) )
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                  'go to the highest peak in the north',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='peak',chapter=5)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p10())
    def nextpage(self):
        # share.scenemanager.switchscene(obj_scene_ch5p12())
        share.scenemanager.switchscene(obj_scene_ch5p14())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )

# keep this for more climbing minigame scenes
# class obj_scene_ch5p12(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p11())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p13())
#
#
# class obj_scene_ch5p13(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p12())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p14())


class obj_scene_ch5p14(page.obj_chapterpage):
    def prevpage(self):
        # share.scenemanager.switchscene(obj_scene_ch5p13())
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p15())
    def setup(self):
        self.text=[\
                '"When ',('{heroname}',share.colors.hero),\
                ' reached the top of the ',('highest peak',share.colors.location2),\
                ', ',('{hero_he}',share.colors.hero2),\
                ' encountered a mysterious ',\
                ('elder',share.colors.elder),'".',\
               'Fascinating, said the book of things. ',\
                'Choose a name and gender for this ',\
                ('elder',share.colors.elder),'. ',\
                   ]
        y1=360+90-100
        y2=520+100-100
        self.addpart( draw.obj_textbox('The elder was:',(180,y1)) )
        textchoice=draw.obj_textchoice('elder_he')
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('elder_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('elder_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the elder\'s name was:",(200,y2)) )
        self.addpart( draw.obj_textinput('eldername',25,(750,y2), legend='Elder Name') )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p16())
    def setup(self):
        self.text=[\
               'Now draw the ',\
               ('elder',share.colors.elder),'\'s face, and make it look slightly to the right. ',\
                'I suggest you draw a happy face and add some wrinkles and maybe a beard, ',\
                'but that is entirely up to you. ',\
                   ]
        self.addpart( draw.obj_drawing('elderhead',(640,450),legend='Draw the elder (facing right)') )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p17())
    def setup(self):
        self.text=[\
               'Lets continue, say the book of things: ',\
               '"At the top of the ',('highest peak',share.colors.location2),', above the clouds, ',\
               ('{heroname}',share.colors.hero),' met the ',('elder',share.colors.elder),' called ',\
               ('{eldername}',share.colors.elder),'". ',\
                   ]
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
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','cloud','sun','mountain') ) )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [111],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p18())
    def setup(self):
        self.text=[\
               '"The ',('elder',share.colors.elder),' said: oh, a visitor. ',\
               'I am ',('{eldername}',share.colors.elder),' the ',\
               ('grandmaster of deceit',share.colors.grandmaster),' of the north! ',\
               'I can teach you all sorts of evil ways, hi hi hi". ',\
                  ]
        animation1=draw.obj_animation('ch5eldertalks1','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [16] )
        animation1.addsound( "elder2", [110],skip=1 )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p19())
    def setup(self):
        self.text=[\
                    '"Oh, so you want to know the  ',('password',share.colors.password2),\
                    ' that opens ',('{villainname}',share.colors.villain),'\'s ',\
                    ('castle',share.colors.location2),'. ',\
                    ' Well I might certainly help, said ',\
                    ('{eldername}',share.colors.elder),'. ',\
                    'hi hi hi". ',\
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
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p20())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                    '"First, lets cover my fee, said ',('{eldername}',share.colors.elder),'. ',\
                    'I see you have caught a yummy ',\
                    ('fish',share.colors.item2),'. I am starving, so that will be my lunch hi hi hi".',\
                   ]
        self.world=world.obj_world_eatfish(self,eldereats=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('herobase',(1172,376),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('interrogationmark',(1214,167),scale=1.2,path='premade') )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p21())
    def setup(self):
        self.text=[\
               '"Now, lets figure out that ',\
               ('password',share.colors.password2),', said ',('{eldername}',share.colors.elder),'. ',\
               'Tell you what, i will tell it to you if you win my game of ',\
               ('rock-paper-scissors',share.colors.grandmaster2),', hi hi hi". ',\
                  ]
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [22] )
        animation1.addsound( "elder3", [67],skip=1 )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p22())
    def setup(self):
        self.text=[\
               'Well, that sounds rather easy, said the book of things. Just draw a ',\
               ('rock',share.colors.item),' a ',\
               ('paper',share.colors.item),' and a ',\
               ('scissor',share.colors.item),'. ',\
                  ]
        self.addpart( draw.obj_drawing('rock',(200+20,450),legend='Large Rock',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('paper',(640,450),legend='Piece of Paper',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('scissors',(1280-200-20,450),legend='Scissors',shadow=(200,200),brush=share.brushes.pen) )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23())
    def setup(self):
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
               '"Alright, said ',('{eldername}',share.colors.elder),', this is how it works. ',\
               'The ',('bubble',share.colors.instructions),\
               ' above your head shows what you are thinking about. ',\
               'Change it with the '+tempo+'". ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,elderhealth=1,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('show3',(418,300),path='premade') )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23a())
    def setup(self):
        self.text=[\
               '"This is your health and mine. If you loose a round, you loose a heart. ',\
               'The first one that runs out of hearts looses the game". ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,elderhealth=1,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('show1',(510,348),scale=0.65,fliph=False,flipv=True,path='premade') )
        self.addpart( draw.obj_image('show1',(744,347),scale=0.65,fliph=True,flipv=True,path='premade') )
        #
        self.sound=draw.obj_sound('elder3')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p23a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p24())
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=[\
                  ' This is it. ',\
                  ('Press '+tempo+' when you are ready.',share.colors.instructions),\
                   ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,elderhealth=1,tutorial=True)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('elder2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p25())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True,herohealth=1,elderhealth=1)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p24())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p26())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p25fail())
    def setup(self):
        self.text=[\
               '"Oh, you lost, said ',('{eldername}',share.colors.elder),'. ',\
               'Better luck next time, hi hi hi. ',\
               'Do you want to play again". ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
        self.addpart( textchoice )
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        # self.addpart( draw.obj_image('elderbase',(627,638),scale=1.37,rotate=0,fliph=True,flipv=False) )
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
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder2", [200], skip=1 )
        animation1.addsound( "elder3", [36] )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p25fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p25())
    def setup(self):
        self.text=[\
               'Giving up already. ',\
               'Well, that doesnt seem to be the story, said the book of things.  ',\
               'It looks like you should just go back and ',\
               ('perservere',share.colors.grandmaster),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p27())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True,herohealth=2,elderhealth=1)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p26())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p28())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p27fail())
    def setup(self):
        self.text=[\
               '"Oh noooo, you lost again, said ',('{eldername}',share.colors.elder),'. ',\
               'But you are getting better, hi hi hi. ',\
               'Do you want to play one last time". ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
        self.addpart( textchoice )
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        # self.addpart( draw.obj_image('elderbase',(627,638),scale=1.37,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [22] )
        animation1.addsound( "elder3", [67],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p27fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p27())
    def setup(self):
        self.text=[\
               'Oh, you want to give up. ',\
               'Sorry, that doesnt seem to be in the story, said the book of things.  ',\
               'It looks like you should just go back and ',\
               ('perservere',share.colors.grandmaster),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p29())
    def setup(self):
        self.text=[\
                '"What a STRONG WILLED character, said ',('{eldername}',share.colors.elder),'. ',\
               'Hear my motto: ',('"always perservere!"',share.colors.grandmaster),'. ',\
               'That is what you did, you came all the way here, you climbed this peak ',\
               ' and even when you were loosing you never gave up.',\
               ' You had it in you all this time!"',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4','elder5','elder6') )
        animation1.addsound( "elder1", [47] )
        animation1.addsound( "elder3", [302] )
        animation1.addsound( "elder4", [190,406] )
        animation1.addsound( "elder5", [76] )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p28())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p30())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p29fail())
    def setup(self):
        self.text=[\
               '"So yeah, I am pretty sure the second part of the castle\'s',\
               ' password is ',\
               ('"perservere"',share.colors.password),', said ',\
               ('{eldername}',share.colors.elder),'. ',\
               'Thats my motto, "always perservere!". ',\
               'Ok you gotta go now, goodbye!" ',\
                  ]
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360)) )
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
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
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder2", [200], skip=1 )
        animation1.addsound( "elder3", [36] )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p29fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p29())
    def setup(self):
        self.text=[\
               'That doesnt seem to be the story, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('"always perservere"',share.colors.grandmaster),'. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p29())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p31())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p30fail())
    def setup(self):
        self.text=[\
               '"Oh I am really sorry, said ',('{eldername}',share.colors.elder),\
               ', but I dont have much time left for playing. ',\
               'Well its getting late, bye now!" ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. Yes!','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
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
        animation1.addsound( "elder2", [200], skip=1 )
        animation1.addsound( "elder3", [36] )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p30fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p30())
    def setup(self):
        self.text=[\
               'Nope, that doesnt seem to be the story, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('"always perservere"',share.colors.grandmaster),'. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p30())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p32())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p31fail())
    def setup(self):
        self.text=[\
               '"You are starting to get on my nerves, said ',('{eldername}',share.colors.elder),'. ',\
               'It is near my bed time, so lets call it a day. ',\
               'Now scram! ". ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='no')
        textchoice.addchoice('1. YEEEES!','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [22] )
        animation1.addsound( "elder3", [67],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p31fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p31())
    def setup(self):
        self.text=[\
               'Well, that is not how the story should go, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('"always perservere"',share.colors.grandmaster),'. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p33())
    def setup(self):
        self.text=[\
               '"OWWWW, said ',('{eldername}',share.colors.elder),', you young punks have no respect! ',\
               'Fine, I will teach you my secret. ',\
               ('perseverance',share.colors.grandmaster),' will only get you so far, what you really need is ',\
               ('cheating',share.colors.grandmaster),'". ',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4','elder5','elder6') )
        animation1.addsound( "elder1", [47] )
        animation1.addsound( "elder3", [302] )
        animation1.addsound( "elder4", [190,406] )
        animation1.addsound( "elder5", [76] )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p34())
    def setup(self):
        self.text=[\
                ('Cheat',share.colors.grandmaster),' by ',\
               ('peeking at other\'s bubble',share.colors.instructions),\
               ' to know what they are thinking. ',\
              'You can then ',('counter their hand at the last moment',share.colors.instructions),\
              ', but you gotta be quick. ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,tutorial=True,nothinks=True)
        self.addpart(self.world)
        animation1=draw.obj_animation('ch5_eldershufflerps','rock',(640,360),record=False)
        animation1.addimage('paper')
        animation1.addimage('scissors')
        self.addpart( animation1 )
        self.addpart( draw.obj_image('show3',(640+220,246+70),path='premade',fliph=True) )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35())
    def setup(self):
        self.text=[\
               '"Well, that is the reason you havent won a single time, ',\
               'said ',('{eldername}',share.colors.elder),'. ',\
                'I was peeking at your bubble the whole time, hi hi hi ".',\
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
        animation1.addsound( "elder5", [36] )
        animation1.addsound( "elder4", [200], skip=1 )
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def setup(self):
        self.text=[\
               '"Tell you what, lets play one last game of ',\
               ('rock-paper-scissors',share.colors.grandmaster2),'. ',\
               'If you ',('cheat',share.colors.grandmaster),\
               ' fair and square you will at least learn something useful". ',\
                  ]
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [22] )
        animation1.addsound( "elder4", [67],skip=1 )
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch5p37())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p36fail())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p36fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def setup(self):
        self.text=[\
               'OWWWW you really dont listen, said ',('{eldername}',share.colors.elder),'. ',\
               'You need to ',\
               ('peek',share.colors.instructions),' at what I am thinking and ',\
               ('counter my hand at the last moment',share.colors.instructions),'. ',\
               'Now lets play again before I loose my patience. ',\
                  ]
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4','elder5','elder6') )
        animation1.addsound( "elder1", [84] )
        animation1.addsound( "elder2", [319] )
        animation1.addsound( "elder5", [115] )
        animation1.addsound( "elder6", [9] )
        #

        self.addpart( draw.obj_music('ch5play') )


class obj_scene_ch5p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p38())
    def setup(self):
        self.text=[\
               '"Alright, you really won this time, said ',('{eldername}',share.colors.elder),'. ',\
                'Congratulations, you are truly a ',\
                ('great deceiver',share.colors.grandmaster2),' that can ',\
                ('cheat',share.colors.grandmaster),' like no equal! ',\
               'You need to respect the elders more, you know. ',\
               'Owww, what is the world going to. Back in my time..." ',\
                  ]
        y1=240+60
        self.addpart( draw.obj_textbox('Well :',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Goodbye','yes',(340,y1))
        textchoice.addchoice('2. Bye!','no',(540,y1))
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
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p39())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=['go back home']
        self.world=world.obj_world_travel(self,start='peak',goal='home',chapter=5)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music(None) )


class obj_scene_ch5p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p40())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"Back at home, ',\
                   ('{heroname}',share.colors.hero),' was sad again. ',\
                   ('{hero_he}',share.colors.hero2), ' though about how ',\
                   ('{hero_he}',share.colors.hero2),' used to charm ',\
                   ('{partnername}',share.colors.partner),' with a serenade. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
        self.addpart(self.world)
        self.addpart( draw.obj_animation('ch5_serenadebug','bug',(640,360),record=False) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p41())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"Then, ',\
                   ('{heroname}',share.colors.hero),' remembered how ',\
                   ('{hero_he}',share.colors.hero2),' and ',\
                   ('{partnername}',share.colors.partner),' used to kiss". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p42())
    def setup(self):
        self.text=[\
                   '"But ',\
                   ('{partnername}',share.colors.partner),' wasnt there, and ',\
                   ('{heroname}',share.colors.hero),' was only kissing ',\
                   ('{hero_him}',share.colors.hero2),('self',share.colors.hero2),'." ',\
                   ]
        self.addpart( draw.obj_image('herobaseangry',(580,400),scale=0.7,rotate=-15) )
        self.addpart( draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4) )
        self.addpart( draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p43())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p42())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p44())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,heroangry=True,bug=True,alarmclock=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5end())
    def setup(self):
        self.text=[\
                   '"Then, right before falling asleep, ',\
                   ('{heroname}',share.colors.hero),' smiled hoping that ',\
                   ('{hero_he}',share.colors.hero2),' would soon rescue ',\
                   ('{partnername}',share.colors.partner),'".',\
                   ]
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )
        #
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch5end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',
                   'But we will be back tomorrow for more! ',\
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



class obj_scene_ch5unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VI',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=6)# chapter 6 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )













#
