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
        share.datamanager.setbookmark('ch5_start')
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
                     ('{heroname}',share.colors.hero),' is visiting the ',\
                     ('grandmasters of deceit',share.colors.grandmaster),\
                     ' to figure out the tower\'s ',\
                     ('password',share.colors.password2),'. ',\
                   'So far, the first part of the password is ',('"fight"',share.colors.password),'. ',\
                   ]
        # self.addpart( draw.obj_image('mountain',(1177,324),scale=0.46,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(996,367),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(74,361),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(988,238),scale=0.37,rotate=0,fliph=False,flipv=False) )
        #
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade')
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark2','bunnyhead',(640,360),record=False,sync=animation1) )
        #
        self.addpart( draw.obj_image('herohead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
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
                  '"Today, ',('{heroname}',share.colors.hero),\
                   ' and ',('{hero_his}',share.colors.hero2),\
                   ' friend the ',('{bug}',share.colors.bug),\
                    ' are on their way to meet the second ',\
                    ('grandmaster',share.colors.grandmaster),\
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch5_startstory')
        self.text=[\
                'Ok here we go, lets write: "It was the next day and the sun was rising."',\
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"',\

                ('{heroname}',share.colors.hero),' ',\
                'woke up ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '        ',\
                    '"',('{hero_he}',share.colors.hero),\
                     ' went to the pond and caught a fish".\n ',
                   ]
        self.world=world.obj_world_fishing_withgun(self)
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
        share.datamanager.setbookmark('ch5_checkmail')
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
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI am still waiting for you, but boy are you slow to pay me a visit. ',\
                    'I heard you met my former grandmaster the ',\
                    ('bunny',share.colors.bunny),'. Good for you, whatever. ',\
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
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,53),xleft=True) )
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
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
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
        share.datamanager.setbookmark('ch5_drawcloud')
        self.text=[\
                  'The second  ',('grandmaster',share.colors.grandmaster),\
                  ' lives in the north, on top of the ',\
                  ('highest peak',share.colors.location2),', It is always covered by stormy clouds, so ',\
                  'draw a ',('cloud',share.colors.item),' and a ',\
                  ('lightning bolt',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('clouddraw',(340,450-50),legend='cloud',shadow=(250,250),brush=share.brushes.pen10) )
        self.addpart( draw.obj_drawing('lightningboltdraw',(940,450-50),legend='lightning bolt',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('ch5') )


class obj_scene_ch5p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch5_climb')
        self.text=[]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('winds') )


class obj_scene_ch5p14(page.obj_chapterpage):
    def prevpage(self):
        # share.scenemanager.switchscene(obj_scene_ch5p13())
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p15())
    def textboxset(self):
        self.textboxopt={'xy':(640,510),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch5_writeelder')
        self.text=[\
                '"When ',('{heroname}',share.colors.hero),\
                ' reached the top of the ',('peak',share.colors.location2),\
                ', ',('{hero_he}',share.colors.hero2),\
                ' encountered a mysterious ',\
                ('elder',share.colors.elder),'". ',\
                'Choose a name and gender for this ',\
                ('elder',share.colors.elder),'. ',\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the elder\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('eldername',20,(750,yref), legend='elder name') )
        #
        self.addpart( draw.obj_textbox('and the elder was:',(180,yref+dyref)) )
        textchoice=draw.obj_textchoice('elder_he',suggested='he')
        textchoice.addchoice('1. A guy','he',(440,yref+dyref))
        textchoice.addchoice('2. A girl','she',(740,yref+dyref))
        textchoice.addchoice('3. A thing','it',(1040,yref+dyref))
        textchoice.addkey('elder_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('elder_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
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
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450-50),path='data/premade',scale=2.5)  )
        self.addpart( draw.obj_drawing('elderheaddraw',(640,450-50),legend='draw the elder (facing right)',shadow=(250,250),brush=share.brushes.pen10) )
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
               ('{heroname}',share.colors.hero),' met a mysterious ',('elder',share.colors.elder),'." ',\
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
        self.addpart( draw.obj_image('floor4',(1280-500,720-140),path='data/premade') )
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
               'I can teach you all sorts of evil ways, he he he". ',\
                  ]
        animation1=draw.obj_animation('ch5eldertalks1','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder1", [16] )
        animation1.addsound( "elder2", [110],skip=1 )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p19())
    def setup(self):
        self.text=[\
                '"So you want to know ',\
                ('my part of the tower\'s password',share.colors.password),'. ',\
                    ' Well I might certainly help, said ',\
                    ('{eldername}',share.colors.elder),'. ',\
                    'he he he". ',\
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


class obj_scene_ch5p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p20())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '"First, lets cover my fee. ',\
                    'I see you have caught a yummy ',\
                    ('fish',share.colors.item2),', so that will be my lunch he he he".',\
                   ]
        self.world=world.obj_world_eatfish(self,eldereats=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('herobase',(1172,376),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('interrogationmark',(1214,167),scale=1.2,path='data/premade') )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p21())
    def setup(self):
        self.text=[\
               '"Burp, that was nice thanks. Now all you have to do is win my game of rock paper scissors ',\
               'and I will tell you ',\
               ('my part of the password',share.colors.password),', he he he. ',\
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
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p22())
    def setup(self):
        share.datamanager.setbookmark('ch5_drawrock')
        self.text=[\
               'That sounds rather easy, said the book of things. Draw a ',\
               ('large rock',share.colors.item),', a ',\
               ('piece of paper',share.colors.item),' and a ',\
               ('pair of scissors',share.colors.item),'. ',\
                  ]
        self.addpart( draw.obj_drawing('rock',(200+20,450),legend='large rock',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('paper',(640,450),legend='piece of paper',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('scissors',(1280-200-20,450),legend='pair of scissors',shadow=(200,200),brush=share.brushes.pen) )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23())
    def setup(self):
        share.datamanager.setbookmark('ch5_rps1')
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
               'Instructions: change selection with the '+tempo+'. ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('show3',(380,300),path='data/premade') )
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('elder') )



class obj_scene_ch5p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23a())
    def setup(self):
        self.text=[\
               '"These are the healthbars. You loose a round, you loose a health. ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_image('show3',(280,150),scale=0.65,fliph=False,flipv=True,path='data/premade') )
        self.addpart( draw.obj_image('show3',(620,150),scale=0.65,fliph=True,flipv=True,path='data/premade') )
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.sound=draw.obj_sound('elder3')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('elder') )



class obj_scene_ch5p23a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p24())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=[' Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,herohealth=1,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.sound=draw.obj_sound('bookscene')
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True,herohealth=1)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p24())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p26())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p25fail())
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch5_lostrps1')
        self.text=[\
               '"Oh, you lost, said ',('{eldername}',share.colors.elder),'. ',\
               'Better luck next time, he he he. ',\
               'Do you want to play again". ',\
                  ]
        y1=200
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
               ('persevere',share.colors.grandmaster),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True,herohealth=2)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p26())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p28())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p27fail())
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch5_lostrps2')
        self.text=[\
               '"Oh noooo, you lost again, said ',('{eldername}',share.colors.elder),'. ',\
               'But you are getting better, he he he. ',\
               'Do you want to play one last time". ',\
                  ]
        y1=200
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
               ('persevere',share.colors.grandmaster),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
        share.scenemanager.switchscene(obj_scene_ch5p28a())
    def setup(self):
        share.datamanager.setbookmark('ch5_strongwilled')
        self.text=[\
                '"What a strong willed character, said ',('{eldername}',share.colors.elder),'. ',\
                'Even when you were loosing, you never gave up. You had it in you all the time!" ',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
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
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p28a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p29())
    def setup(self):
        self.text=[\
                '"I am so impressed that I will tell you the second part of the password. It is:',\
                ('"persevere"',share.colors.password),'. ',\
                'That\'s my motto: "always persevere!" I taught it to ',\
                ('{villainname}',share.colors.villain),' when ',\
                ('{villain_he}',share.colors.villain2),' was my student." ',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
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
        self.addpart( draw.obj_music('elder') )



class obj_scene_ch5p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p28a())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p30())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p29fail())
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
               '"Well that was fun, said ',\
               ('{eldername}',share.colors.elder),'. ',\
               'But you gotta go now, goodbye!" ',\
                  ]
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360)) )
        y1=200
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
               'You have just been taught how important it is to ',\
               ('"persevere"',share.colors.grandmaster),', ',\
               'so you should do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
               '"Oh I am really sorry, said ',('{eldername}',share.colors.elder),\
               ', but I dont have much time left for playing. ',\
               'Well its getting late, bye now!" ',\
                  ]
        y1=200
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
               'That doesnt seem to be the story, said the book of things. ',\
               'You have just been taught how important it is to ',\
               ('"persevere"',share.colors.grandmaster),', ',\
               'so you should do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
               '"You are starting to get on my nerves, said ',('{eldername}',share.colors.elder),'. ',\
               'It is near my bed time, so lets call it a day. ',\
               'Now scram! ". ',\
                  ]
        y1=200
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
               'That doesnt seem to be the story, said the book of things. ',\
               'You have just been taught how important it is to ',\
               ('"persevere"',share.colors.grandmaster),', ',\
               'so you should do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
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
        share.datamanager.setbookmark('ch5_eldercheatsecret')
        self.text=[\
               '"Owwwwww, you young punks have no respect! ',\
               'Fine, I will teach you my real secret. ',\
               ('perseverance',share.colors.grandmaster),' will only get you so far, what you really need is ',\
               ('cheating',share.colors.grandmaster),'". ',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
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
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p34())
    def textboxset(self):
        self.textboxopt={'xy':(1230-100,660)}
    def setup(self):
        self.text=[\
                   'Peek at others\'s selection and ',\
                  ('counter them at the last moment',share.colors.instructions),'. ',\
                 'That is how you ',('cheat',share.colors.grandmaster),'. ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,tutorial=True,nothinks=True,herohealth=2)
        self.addpart(self.world)
        animation1=draw.obj_animation('ch5_eldershufflerps','rock',(640,360),record=False)
        animation1.addimage('paper')
        animation1.addimage('scissors')
        self.addpart( animation1 )
        self.addpart( draw.obj_image('show3',(640+220+40,246+70),path='data/premade',fliph=True) )
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35())
    def setup(self):
        self.text=[\
               '"Well, that is the reason you havent won a single time, ',\
               'said ',('{eldername}',share.colors.elder),'. ',\
                'I was peeking at your selection the whole time, he he he".',\
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
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35a())
    def setup(self):
        self.text=[\
               '"Tell you what, before you leave lets play one last game of ',\
               'rock paper scissors. ',\
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


class obj_scene_ch5p35a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch5_rps3')
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('winds') )



class obj_scene_ch5p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35a())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch5p37())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p36fail())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p36fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p35a())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch5p35a())
        else:
            share.scenemanager.switchscene(obj_scene_ch5p37())
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
               'OWWWW you really dont listen, said ',('{eldername}',share.colors.elder),'. ',\
               'You need to ',\
               ('peek',share.colors.instructions),' at my selection and ',\
               ('counter me at the last moment',share.colors.instructions),'. ',\
               'Now lets play again before I loose my patience. ',\
                  ]
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        #
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(540,y1))
        textchoice.addchoice('Abandon (skip)','no',(740,y1))
        self.addpart( textchoice )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4','elder5','elder6') )
        animation1.addsound( "elder1", [84] )
        animation1.addsound( "elder2", [319] )
        animation1.addsound( "elder5", [115] )
        animation1.addsound( "elder6", [9] )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p38())
    def textboxset(self):
        self.textboxopt={'xy':(440,280),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch5_winrps3')
        self.text=[\
               '"Congratulations, you really won this time said ',('{eldername}',share.colors.elder),'. ',\
               'You need to respect the elders more, you know. ',\
               'Oh what is the world going to, back in my time..." ',\
                  ]
        y1=200
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
        # self.addpart( draw.obj_soundplacer(animation1,'elder1','elder2','elder3','elder4') )
        animation1.addsound( "elder2", [200], skip=1 )
        animation1.addsound( "elder3", [36] )
        #
        self.addpart( draw.obj_music('elder') )


class obj_scene_ch5p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p39())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch5_gohome')
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
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"Back at home, ',\
                   ('{heroname}',share.colors.hero),' was feeling a little better. ',\
                   ('{hero_he}',share.colors.hero2), ' played a serenade ',\
                   ' thinking about ',\
                   ('{partnername}',share.colors.partner),'. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
        self.addpart(self.world)
        self.addpart( draw.obj_animation('ch5_serenadebug','bug',(640,360),record=False) )
        #
        self.addpart( draw.obj_music('piano') )

#
# class obj_scene_ch5p40(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p39())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch5p41())
#     def setup(self):
#         self.text=[\
#                    '"But when it was time for dinner, ',\
#                    ('{heroname}',share.colors.hero),' remembered that ',\
#                    ('{hero_he}',share.colors.hero2),' had given ',\
#                    ('{hero_his}',share.colors.hero2),' fish to ',\
#                    ('{eldername}',share.colors.elder),'". ',\
#                    ]
#         animation1=draw.obj_animation('ch5_herohungry','fish',(640,360),record=False)
#         animation1.addimage('elderhead')
#         self.addpart( animation1 )
#         #
#         animation2=draw.obj_animation('ch5_herohungry2','interrogationmark',(640,360),record=False,sync=animation1,path='data/premade')
#         animation2.addimage('exclamationmark',path='data/premade')
#         animation2.addimage('empty',path='data/premade')
#         self.addpart( animation2 )
#         #
#         animation3=draw.obj_animation('ch5_herohungry3','herobase',(640,360),record=False,sync=animation1)
#         self.addpart( animation3 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'hero1','elder1','elder2','elder3','elder4','elder5') )
#         animation1.addsound( "hero1", [69] )
#         animation1.addsound( "elder1", [200] )
#         animation1.addsound( "elder4", [330],skip=1 )
#         #
#         self.addpart( draw.obj_music('piano') )
#         #


class obj_scene_ch5p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p41())
    def setup(self):
        self.text=[\
                   '"But when it was time for dinner, ',\
                   ('{heroname}',share.colors.hero),' remembered that ',\
                   ('{hero_he}',share.colors.hero2),' had given ',\
                   ('{hero_his}',share.colors.hero2),' fish to ',\
                   ('{eldername}',share.colors.elder),'". ',\
                   ]

        animation1=draw.obj_animation('ch5_herohungry2','interrogationmark',(640,360),record=False,path='data/premade')
        animation1.addimage('exclamationmark',path='data/premade')
        animation1.addimage('empty',path='data/premade')
        self.addpart( animation1 )
        #
        animation1=draw.obj_animation('ch5_herohungry3','herobase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        #
        animation4=draw.obj_animation('ch5_herohungry1','elderhead',(640,360),record=False,sync=animation1)
        self.addpart( animation4 )
        #
        # self.addpart( draw.obj_imageplacer(self,'fish') )
        self.addpart( draw.obj_image('fish',(1050,351),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('largecross',(1050,351),scale=1.3,path='data/premade') )
        animation1.addsound( "hero1", [20] )
        animation1.addsound( "elder1", [100] )
        animation1.addsound( "elder4", [140] )
        #
        self.addpart( draw.obj_music('piano') )




class obj_scene_ch5p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p42())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"So ',\
                   ('{heroname}',share.colors.hero),\
                   ' went straight to bed starving and angry." ',\
                   ]
        self.world=world.obj_world_gotobed(self,bug=True,addmoon=False,addsun=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5end())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"The night fell, and tomorrow would be another day."',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch5end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p42())
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
        share.datamanager.setbookmark('ch5_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VI',share.colors.instructions),'! ',\
                   ]
        share.datamanager.updateprogress(chapter=6)# chapter 6 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )













#
