#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter6.py: ...
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

# Chapter VI: ...
# *CHAPTER VI



class obj_scene_chapter6(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def setup(self):
        share.datamanager.setbookmark('ch6_start')
        self.text=['-----   Chapter VI: Treasure Hunt   -----   ',\
                   '\n It was the next day when the book of things said to the pen and the eraser: ',\
                  'lets continue our story where we left. ',\
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

# class obj_scene_ch6p3(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_chapter6())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p4())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def soundnextpage(self):
#         pass# no sound
#     def setup(self):
#         share.datamanager.setbookmark('ch6_startstory')
#         self.text=[\
#                 '"',\
#                 ('{partnername}',share.colors.partner),' was captive in the ',\
#                 ('evil tower',share.colors.location2),', and ',\
#                 ('{heroname}',share.colors.hero),' needed to visit one last ',\
#                 ('evil grandmaster',share.colors.grandmaster),'. ',\
#                 ' It was the next day and the sun was rising." ']
#         self.world=world.obj_world_sunrise(self)
#         self.addpart(self.world)
#         # #
#         self.addpart( draw.obj_music('ch6') )
#
#
# class obj_scene_ch6p4(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p3())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p6())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                 ('{heroname}',share.colors.hero),' ',\
#                 'woke up ',\
#                 'with ',('{hero_his}',share.colors.hero2),\
#                 ' loyal sidekick ',('{bug}',share.colors.bug),'." ',\
#                    ]
#         self.world=world.obj_world_wakeup(self,bug=True,alarmclock=False)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('ch6') )

class obj_scene_ch6p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def setup(self):
        share.datamanager.setbookmark('ch6_checkmail')
        # self.text=[\
        #           '"',\
        #             ('{heroname}',share.colors.hero),' came back home and checked ',\
        #             ('{hero_his}',share.colors.hero2),' mailbox. ',\
        #             ('{hero_he}',share.colors.hero2),' had received ',\
        #             'two ',' letters." ',\
        #            ]
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' needed to visit only one last ',\
                ('evil grandmaster',share.colors.grandmaster),'. ',\
                ('{hero_he}',share.colors.hero2),' woke up, checked ',\
                ('{hero_his}',share.colors.hero2),' mailbox ',\
                'and there were two  letters."',\
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
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nCome back anytime to the ',\
                    ('highest peak',share.colors.location2),' to play some games, ',\
                    'but no cheating next time. ',\
                    'Good luck in your quest. ',\
                  '\n\nsigned: ',('{eldername}',share.colors.elder),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        #
        animation1=draw.obj_animation('ch2_mailhead','elderhead',(640,360),imgscale=0.7)
        self.addpart(animation1)
        animation1.addsound( "elder1", [100],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nIts me, your favorite ',('villain',share.colors.villain),'. ',\
                    'I am loooonging to kick your butt again, come back quick muahaha. ',\
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
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox again.',\
                    'There was also a scrambled piece of paper. ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','paper',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6','mailjump') )
        animation1.addsound( "hero2", [82] )
        animation1.addsound( "mailjump", [7] )
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def setup(self):
        self.text=[\
                  '"',\
                    'The piece of paper said: ',\
                    'dear ',('{heroname}',share.colors.hero),\
                    ', meet me on the beach. ',\
                    'signed: unknown. "',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('paper',(333,442),scale=0.33,rotate=6,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail2','sun',(640,360))
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        #
        self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation1.addsound( "hero1", [70,180],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def setup(self):
        share.datamanager.setbookmark('ch6_drawwave')
        self.text=['Who could that possibly be, said the book of things. ',\
                    'Draw a ',('palm tree',share.colors.item),\
                    ' and a ',('wave',share.colors.item),' and we will be on our way. ',\
                    ]
        self.addpart( draw.obj_drawing('palmtreedraw',(340,450-50),legend='palm tree',shadow=(250,250),brush=share.brushes.pen10) )
        self.addpart( draw.obj_drawing('wave',(940,400),legend='wave',shadow=(200,100)) )
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Investigate the beach',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='beach',chapter=6,beachquestionmark=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def textboxset(self):
        self.textboxopt={'xy':(640,510),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch6_writesailor')
        self.text=[\
                '"On the beach, ',('{heroname}',share.colors.hero),\
                ' met a mysterious ',\
                ('sailor',share.colors.sailor),'." ',\
                'Choose a name and gender for the ',\
                ('sailor',share.colors.sailor),'. ',\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the sailor\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('sailorname',20,(750,yref), legend='sailor name') )
        #
        self.addpart( draw.obj_textbox('and the sailor was:',(180,yref+dyref)) )
        textchoice=draw.obj_textchoice('sailor_he',suggested='he')
        textchoice.addchoice('1. A guy','he',(440,yref+dyref))
        textchoice.addchoice('2. A girl','she',(740,yref+dyref))
        textchoice.addchoice('3. A thing','it',(1040,yref+dyref))
        textchoice.addkey('sailor_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('sailor_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def setup(self):
        self.text=[\
               'Now draw the ',\
               ('sailor',share.colors.sailor),'\'s face, and make ',('{sailor_him}',share.colors.sailor),' look slightly to the right. ',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450-50),path='data/premade',scale=2*1.25)  )
        self.addpart( draw.obj_drawing('sailorfacedraw',(640,450-50),legend='Draw the sailor (facing right)',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('ch6') )



class obj_scene_ch6p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def setup(self):
        self.text=[\
                  'We cant have a ',('sailor',share.colors.sailor),\
                  ' without a proper ',('sailor hat',share.colors.item),', ',\
                  'so draw that too. ',\
                   ]
        yref=460

        # self.addpart( draw.obj_drawing('sailorhat',(640,yref-200),shadow=(250,150)) )
        self.addpart( draw.obj_drawing('sailorhat',(640,yref-200),shadow=(400,150)) )# WIDER
        self.addpart( draw.obj_image('sailorbaldhead',(640,yref)) )
        self.addpart( draw.obj_textbox('Add a sailor hat',(640,yref+230),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('ch6') )


class obj_scene_ch6p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def setup(self):
        self.text=[\
               'Lets read this again, say the book of things: ',\
               '"On the ',('beach',share.colors.location2),', ',\
               ('{heroname}',share.colors.hero),' met the ',\
               ('sailor',share.colors.sailor),' called ',\
               ('{sailorname}',share.colors.sailor),'." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('sailorbase',(1280-500,475),scale=0.5,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1280-136,347),scale=0.5,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1280-313,334),scale=0.37,rotate=0,fliph=False,flipv=False) )

        animation1=draw.obj_animation('ch6_meetsailor','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch6_meetsailor2','sun',(640,360),record=False) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor4", [74] )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch6p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def setup(self):
        self.text=[\
               '"The ',('sailor',share.colors.sailor),' said: so you have received my note. ',\
               'My name is ',('{sailorname}',share.colors.sailor),', I am the ',\
               ('evil grandmaster',share.colors.grandmaster),' of the south! ',\
               'Aye Aye, I can teach you all sorts of evil ways." ',\
                  ]
        animation1=draw.obj_animation('ch6sailortalks1','sailorbase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [169] )
        animation1.addsound( "sailor4", [110] )
        animation1.addsound( "sailor5", [32],skip=1 )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())
    def setup(self):
        self.text=[\
                    '"I happen to be looking for a skilled crewmate. ',\
                    'If you prove yourself helpful, I might even give you a ',\
                    ('clue',share.colors.password),'!" '
                  ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640,360+100),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [41, 153] )
        animation1.addsound( "sailor4", [261] )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())
    def setup(self):
        share.datamanager.setbookmark('ch6_getlogs')
        self.text=[\
                    '"First, we need to build a ship. ',\
                    'Go get me some wood, I need ',\
                    ('10 logs',share.colors.instructions),'." '
                  ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640,360+100),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [41, 153] )
        animation1.addsound( "sailor4", [261] )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Get 10 wood logs for the sailor.',\
                   ]
        self.world=world.obj_world_travel(self,start=(-1280+100,1080-120),\
        goal='beach',chapter=6,minigame='logs',sailorwait=True,noending='True')
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())
    def setup(self):
        share.datamanager.setbookmark('ch6_drawship')
        self.text=[\
                   '"Great job on getting that wood, said ',\
                   ('{sailorname}',share.colors.sailor),\
                   ', lets start building." ',\
                   'Draw a ',('sailboat',share.colors.item),'. ',\
                   '\n ',\
                   ]
        self.textkeys={'pos':(50,200),'xmax':600}
        self.addpart( draw.obj_drawing('sailboat',(640+300,450-100),legend='Sailboat (facing right)',shadow=(300,300)) )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def setup(self):
        self.text=[\
                   '"Nicely done, said ',\
                   ('{sailorname}',share.colors.sailor),\
                   ', now we can start our adventure. ',\
                   'We are going to recover my ',('treasure',share.colors.cow),'!" '\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [169] )
        animation1.addsound( "sailor4", [110] )
        animation1.addsound( "sailor5", [32] )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())
    def setup(self):
        share.datamanager.setbookmark('ch6_drawskull')
        self.text=[\
                   '"You see, I lost my ',('treasure',share.colors.cow),\
                   ' in a very scary place called skull island." ',\
                   ]
        self.addpart( draw.obj_drawing('skeletonheaddraw',(640,450-50),legend='draw a skull (facing right)',shadow=(250,250)) )
        #
        self.addpart( draw.obj_music('sailor') )
        #


class obj_scene_ch6p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def setup(self):
        self.text=[\
                   '"Oh but it wont be easy! ',\
                    'There are ',\
                    ('spooky skeletons',share.colors.skeleton),' that guard the place. ',\
                    'Now lets get going, ',\
                    'said ',('{sailorname}',share.colors.sailor),'." ',\
                   ]
        animation1=draw.obj_animation('ch1_hero1','skeletonbase',(360,360))
        self.addpart(animation1)
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase',(360-300,360)))
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase_sailorhat',(360+300,360)))
        #
        # self.addpart( draw.obj_soundplacer(animation1,'skeleton1','skeleton2','skeleton3','skeleton4','skeleton5') )
        animation1.addsound( "skeleton1", [22, 121, 215, 336] )
        animation1.addsound( "skeleton3", [66, 165, 282, 387] )
        animation1.addsound( "skeleton4", [22] )
        animation1.addsound( "skeleton2", [121] )
        # animation1.addsound( "skeleton5", [1] )
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Sail to ',('skull island',share.colors.skeleton2),\
                   ]
        self.world=world.obj_world_travel(self,start='beach',goal='island',boat=True,chapter=6,sailor=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch6_startskullisland')
        self.text=[\
                   '"Alright, said ',('{sailorname}',share.colors.sailor),'. ',\
                   'First, we shall wait until night to infiltrate the island." ',\
                   ]
        self.world=world.obj_world_sunset(self,type='island')
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('islandsunset',(840,550),shadow=(400,150),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_imageplacer(self,'skeletonhead','palmtree','wave','cloud','sailboat','mountain',actor='staticactor') )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )



class obj_scene_ch6p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())
    def setup(self):
        self.text=[\
                   '"Now listen, ',\
                   'your mission is to sneak past these skeletons, grab my ',\
                   ('treasure',share.colors.cow),' and make it back to the ship. Easy-peasy!"',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','skeletonbase','palmtree','wave','cloud','sailboat','mountain','bush') )
        self.addpart( draw.obj_image('mountain',(1169,276),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(940,566),scale=0.6,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(707,467),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(409,661),scale=0.68,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailorbase',(155,634),scale=0.68,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(564,313),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(348,320),scale=0.46,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('moon',(141,258),scale=0.34,rotate=-2,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_skullobserve1','skeletonbase_sailorhat',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch6_skullobserve2','skeletonbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch6_skullobserve3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
        animation1.addsound( "sailor2", [173] )
        animation1.addsound( "sailor4", [114] )
        animation1.addsound( "sailor5", [36] )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def setup(self):
        share.datamanager.setbookmark('ch6_startsneak')
        self.text=[\
                   '"I will be on the radio if you need any help, ',\
                   'now get in that bush and start sneaking." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','saislorbase','bush','palmtree','moon') )
        self.addpart( draw.obj_image('sailorbase',(190,491),scale=0.55,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(357,498),scale=0.55,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(792,554),scale=0.55,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1141,317),scale=0.57,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(973,302),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('moon',(821,256),scale=0.33,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_herotobush','herobase',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        animation2=draw.obj_animation('ch6_herotobush2','herohead',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        animation3=draw.obj_animation('ch6_herotobush3','bush',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation3 )
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'stealth_jumpinbush','hero2','stealth_bush1','stealth_bush2','stealth_bush3') )
        animation1.addsound( "stealth_jumpinbush", [75] )
        animation1.addsound( "hero2", [250] )
        animation1.addsound( "stealth_bush1", [149] )
        animation1.addsound( "stealth_bush1", [149] )
        animation1.addsound( "stealth_bush2", [384] )
        animation1.addsound( "stealth_bush3", [321, 461] )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p30a())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p30())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['"You are doing great, said ',\
                   ('{sailorname}',share.colors.sailor),' on the radio. ',\
                   'Keep moving right." ',\
                   ]
        self.world=world.obj_world_bushstealth0(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('sailor_radio')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p30a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p31())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p30a())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch6_sneak1')
        self.text=['"Uh oh, we have company! Stand still when you are in its field of vision."',\
                   ]
        self.world=world.obj_world_bushstealth(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('sailor_radio')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('stealth') )



class obj_scene_ch6p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30a())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p32())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p31())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch6_sneak2')
        self.text=['"Well done, now just keep going. ',\
                    ('{sailorname}',share.colors.sailor),' out. "',\
                   ]
        self.world=world.obj_world_bushstealth2(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('sailor_radio')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p31())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p33())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p32())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch6_sneak3')
        self.text=[' ']
        self.world=world.obj_world_bushstealth3(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p32())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p34())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p33())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch6_sneak4')
        self.text=[' ']
        self.world=world.obj_world_bushstealth4(self,winsound='stealth_win')# modified win sound
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())
    def setup(self):
        share.datamanager.setbookmark('ch6_drawcow')
        self.text=[\
                   '"My ',('treasure',share.colors.cow),' should be right ahead, said ',('{sailorname}',share.colors.sailor),' on the radio." ',\
                   'Its weird, there is nothing here except a ',\
                   ('cow',share.colors.item),'. ',\
                   ]
        # self.addpart( draw.obj_drawing('cow',(640,450),legend='draw a cow (facing right)',shadow=(300,200),brush=share.brushes.pen6) )
        self.addpart( draw.obj_drawing('cowdraw',(640,450-50),legend='draw a cow (facing right)',shadow=(375,250)) )
        self.sound=draw.obj_sound('sailor_radio')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('stealth') )
        #


class obj_scene_ch6p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())
    def setup(self):
        self.text=[\
                   '"Well, is this actually my pet cow called ',('treasure',share.colors.cow),', said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'I hope you werent expecting real money!" ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cow','bush','palmtree','moon') )
        # self.addpart( draw.obj_image('cow',(533,498),scale=0.68,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(958,372),scale=0.55,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1140,361),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(303,312),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(971,611),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(145,494),scale=0.44,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6_cowwalks1','cow',(640,360),record=False)
        self.addpart(animation1)
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_soundplacer(animation1,'cow') )
        animation1.addsound( "cow", [50] )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())
    def setup(self):
        self.text=[\
                   '"Suddenly, one of the ',('skeletons',share.colors.skeleton),' sounded the alarm: ',\
                   ('Alert',share.colors.skeleton),', someone has breached the perimeter! ',\
                 'The intruder is trying to steal our cow!"',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','skeletonbase','cow','bush','palmtree','moon') )
        self.addpart( draw.obj_image('cow',(174,364),scale=0.48,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(420,495),scale=0.53,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('skeletonbase',(929,489),scale=0.53,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(149,563),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(624,383),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1188,292),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('moon',(480,235),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('exclamationmark',(948,260),scale=1,path='data/premade') )
        animation1=draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(933,485),imgfliph=True)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch6_heroalertgiven','herobase',(640,360),record=False,sync=animation1)
        self.addpart(animation2)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'skeleton1','skeleton2','skeleton3','skeleton4','skeleton5','cow') )
        animation1.addsound( "stealth_alarm", [5] )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())
    def setup(self):
        self.text=[\
                   '"It looks like you are surrounded, said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'Its time to make a run for it! ',\
                  'Ride ',('treasure',share.colors.cow),\
                  ' and make it back to the ship." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','skeletonbase','cow','bush','palmtree','moon','heroridecow') )
        # self.addpart(draw.obj_animation('ch1_hero1','heroridecow',(360,360)))
        # self.addpart( draw.obj_image('heroridecow',(564,453),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('exclamationmark',(122,498-200),path='data/premade') )
        self.addpart( draw.obj_image('exclamationmark',(263,472-200),path='data/premade') )
        self.addpart( draw.obj_image('exclamationmark',(1010,469-200),path='data/premade') )
        self.addpart( draw.obj_image('exclamationmark',(1156,510-200),path='data/premade') )
        animation1=draw.obj_animation('bushstealth_skeletonalert','skeletonbase_sailorhat',(122,498))
        self.addpart(animation1)
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(263,472),sync=animation1) )
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(1010,469),sync=animation1,imgfliph=True) )
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(1156,510),sync=animation1,imgfliph=True) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'skeleton1','skeleton2','skeleton3','skeleton4','skeleton5','cow') )
        animation1.addsound( "stealth_alarm", [5] )
        #
        # self.addpart( draw.obj_animation('ch6_heroalertgivenridecow','heroridecow',(640,360),sync=animation1, record=False) )
        animation2=draw.obj_animation('ch6_heroalertgivenridecow','heroridecow',(640,360),sync=animation1, record=False)
        self.addpart(animation2)
        animation2.addsound( "cow", [80])
        animation2.addsound( "skeleton2", [1,6,11,16], skip=3 )
        #
        self.addpart( draw.obj_music('stealth') )


class obj_scene_ch6p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38a())
    def setup(self):
        share.datamanager.setbookmark('ch6_startride')
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=['Instructions: ',\
                    'move ',('treasure',share.colors.cow),' around with the '+tempo+'. ',\
                   ]
        self.textkeys={'pos':(100,20),'xmin':100}
        self.world=world.obj_world_ridecow(self,tutorial=True,trees=False)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('skeleton2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_image('show1',(760,540),fliph=False,flipv=False,path='data/premade') )
        self.addpart( draw.obj_textbox('(not the actual chase)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('racing') )


class obj_scene_ch6p38a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38b())
    def setup(self):
        self.text=[\
                    'Trees and rocks will hurt the ',\
                    ('hero',share.colors.hero),\
                    ' (but not ',\
                    ('treasure',share.colors.cow),\
                    '!). ',\
                   ]
        self.textkeys={'pos':(100,20),'xmin':100}
        self.world=world.obj_world_ridecow(self,tutorial=True,trees=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_image('show3',(830,160),scale=1,fliph=False,flipv=True,path='data/premade') )
        self.addpart( draw.obj_textbox('(not the actual chase)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('racing') )




class obj_scene_ch6p38b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38c())
    def setup(self):
        self.text=[\
                    'Ride until bar reaches 100%. ',\
                   ]
        self.textkeys={'pos':(100,20),'xmin':100}
        self.world=world.obj_world_ridecow(self,tutorial=True,trees=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_image('show1',(970,520),fliph=True,flipv=False,path='data/premade') )
        self.addpart( draw.obj_textbox('(not the actual chase)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('racing') )


class obj_scene_ch6p38c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())
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


class obj_scene_ch6p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38c())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p40())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p39death())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False, 'xy':(530-180,50)}
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


class obj_scene_ch6p39death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38c())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch6p38c())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p40())# skip
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




class obj_scene_ch6p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())
    def setup(self):
        share.datamanager.setbookmark('ch6_winride')
        self.text=[\
                   '"I am so relieved that you made it, said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'Quick, board the ship and lets get out of here." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'heroridecow','sailorbase','bush','palmtree','moon','sailboat','wave') )
        self.addpart( draw.obj_image('sailboat',(1034,416),scale=0.81,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailorbase',(612,484),scale=0.45,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('heroridecow',(224,476),scale=0.7,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(775,633),scale=0.49,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('moon',(723,224),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1190,659),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(979,641),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1219,556),scale=0.26,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(58,310),scale=0.28,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(171,312),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch6_herocowtoship2','moon',(640,360),record=False) )
        animation1=draw.obj_animation('ch6_herocowtoship','heroridecow',(640,360),record=False)
        self.addpart(animation1)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5','cow') )
        animation1.addsound( "sailor4", [1] )
        animation1.addsound( "cow", [40],skip=1 )
        #
        self.addpart( draw.obj_music('racing') )



class obj_scene_ch6p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Go back to the beach',\
                   ]
        self.world=world.obj_world_travel(self,start='island',goal='beach',boat=True,chapter=6,sailor=True,beachmark='True')
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('sailor') )


class obj_scene_ch6p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def setup(self):
        share.datamanager.setbookmark('ch6_choosepwd')
        self.text=[\
                   '"I cannot thank you enough for saving ',\
                   ('treasure',share.colors.cow),', said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'I will give you the final ',('clue',share.colors.password),\
                   ' and you can even keep the ship." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
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
        animation3=draw.obj_animation('ch6sailortalks3love2','love',(640,360),record=False,sync=animation2)
        animation3.addimage('empty',path='data/premade')
        self.addpart(animation3)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5','cow') )
        animation1.addsound( "sailor4", [40] )
        animation1.addsound( "cow", [110],skip=1 )
        #
        self.addpart( draw.obj_music('sailor') )

class obj_scene_ch6p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p45())
    def triggernextpage(self,controls):
        return self.world.done# quick skip
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Put your hands up in the air to receive the final ',
                   ('clue',share.colors.password),'! '\
                   ]
        self.world=world.obj_world_getitem(self,item='sailorhead',imgscale=0.6,imgxy=(0,0))
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('sailorbase',(144,398),scale=0.47,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('sailboat',(107,314),scale=0.36,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('wave',(295,369),scale=0.36,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('wave',(419,385),scale=0.36,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1074,557),scale=0.6,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1192,387),scale=0.46,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('palmtree',(105,399),scale=0.46,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sun',(1153,205),scale=0.41,rotate=0,fliph=True,flipv=True) )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch6p45(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())
    def textboxset(self):
        self.textboxopt={'xy':(640,410),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                   'The last part of the ',('password',share.colors.password),\
                   ' is actually up to you, said ',('{sailorname}',share.colors.sailor),\
                   '. It goes like this: ',\
                   ('abracada...',share.colors.password),' '\
                   ]
        #
        self.addpart( draw.obj_textinput('passwordend',20,(640,260), legend='The last part of the password') )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch6p46(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6end())
    def setup(self):
        self.text=[\
                'Alright, the full password to the ',\
                 ('evil tower',share.colors.location2),' is: ',\
                 ('"abracada{passwordend}"',share.colors.password),'. ',\
                 'That\'s it, said ',('{bug}',share.colors.bug),\
                 ', you can finally go rescue ',('{partnername}',share.colors.partner),'!" ']
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart(draw.obj_image('cluesparkles',(754,418),scale=1,path='data/premade'))

        animation1=draw.obj_animation('ch3_bugtalks3intmark','elderhead',(374,346-100),scale=0.25)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','bunnyhead',(137,564-150),scale=0.3) )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','sailorhead',(1099,444-150),scale=0.2) )
        # self.addpart( draw.obj_textbox('abra',(137,564+50),color=share.colors.password) )
        # self.addpart( draw.obj_textbox('cada',(374,346+50),color=share.colors.password) )
        # self.addpart( draw.obj_textbox('{passwordend}',(1099,444+50),color=share.colors.password) )
        self.addpart( draw.obj_textbox('abracada{passwordend}',(754,418+200),color=share.colors.password) )
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        # animation1.addsound( "bug1", [15, 120, 140])
        animation2=draw.obj_animation('ch3_bugtalks1aaa','bug',(340,360))
        self.addpart( animation2 )
        animation2.addsound( "bug1", [45] )
        animation2.addsound( "bug2", [70, 130, 150])
        self.addpart( draw.obj_music('piano') )





class obj_scene_ch6end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',\
       'The tension is killing me. I cant wait to find what happens tomorrow! ',\
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

class obj_scene_ch6unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6end())
    def setup(self):
        share.datamanager.setbookmark('ch6_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VII',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=7)# chapter 7 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )



#####################################################################

# class obj_scene_ch6p1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_chapter6())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p2())
#     def setup(self):
#         self.text=[\
#                   '"',
#                    ('{partnername}',share.colors.partner),' is being held captive in ',\
#                     ('{villainname}',share.colors.villain),'\'s ',\
#                      ('evil tower',share.colors.location2),', and ',\
#                      ('{heroname}',share.colors.hero),' is trying to figure out the tower\'s ',\
#                      ('password',share.colors.password2),'. ',\
#                    ]
#         self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
#         self.addpart( draw.obj_image('tower',(1156,312),scale=0.54,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(981,265),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(866,243),scale=0.23,rotate=0,fliph=True,flipv=False) )
#         animation1=draw.obj_animation('ch4_villaincapture1','villainbase',(640,360),record=False)
#         animation1.addimage('villainholdspartner')
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch4_villaincapture2','partnerbase',(640,360),record=False,sync=animation1)
#         animation2.addimage('empty',path='data/premade')
#         self.addpart( animation2 )
#         # self.addpart( draw.obj_imageplacer(self,'tower','mountain') )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','partner_scared') )
#         animation1.addsound( "villain1", [20] )
#         animation1.addsound( "villain2", [300] )
#         animation1.addsound( "villain3", [155] )
#         animation1.addsound( "partner_scared", [228] )
#         #
#         self.addpart( draw.obj_music('piano') )
#
#
# class obj_scene_ch6p2(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p1())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p3())
#     def setup(self):
#         self.text=[\
#                   '"',\
#                 'So far, the tower\'s password is ',('"fight persevere"',share.colors.password),'. ',\
#                      ('{heroname}',share.colors.hero),' must visit one last ',\
#                      ('evil grandmaster',share.colors.grandmaster),\
#                      ' to figure out the last part." ',\
#                    ]
#         # self.addpart( draw.obj_image('mountain',(1177,324),scale=0.46,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('mountain',(996,367),scale=0.37,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(74,361),scale=0.34,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('sun',(988,238),scale=0.37,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade')
#         self.addpart( animation1 )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark','elderhead',(374,346),imgscale=0.25,sync=animation1) )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark2','bunnyhead',(640,360),sync=animation1) )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4') )
#         animation1.addsound( "bunny2", [40] )
#         animation1.addsound( "elder1", [80],skip=1 )
#         #
#         self.sound=draw.obj_sound('bookscene')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('piano') )

        # animation1=draw.obj_animation('fishmovescissors1','scissors',(640,360),record=True)
        # self.addpart( animation1 )

# class obj_scene_ch6p19(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p18())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p20())
#     def setup(self):
#         self.text=[\
#                   '"The ',('{bug}',share.colors.bug),\
#                   ' crawled out of ',('{heroname}',share.colors.hero),\
#                   '\'s pocket and whispered: ',\
#                    'It sounds like we have no choice, lets join the ',\
#                    ('grandmaster',share.colors.grandmaster),'\'s crew and hope for the best." ',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('sailor') )

# class obj_scene_ch6p42(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p41())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p43())
#     def setup(self):
#         share.datamanager.setbookmark('ch6_byesailor')
#         self.text=[\
#                    '"Squid, I guess this is where we part ways said ',\
#                    ('{sailorname}',share.colors.sailor),'. ',\
#                     'One thing is for sure, you are truly a great deceiver!"',\
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
#         self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
#         self.addpart(animation1)
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
#         animation1.addsound( "sailor2", [169] )
#         animation1.addsound( "sailor4", [110] )
#         animation1.addsound( "sailor5", [32],skip=1 )
#         #
#         self.addpart( draw.obj_music('sailor') )

# class obj_scene_ch6p44(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p43())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p45())
#     def setup(self):
#         self.text=[\
#                    '"One last thing, the last part of the  tower\'s password is: ',\
#                    ('"overcome"',share.colors.password),'. ',\
#                     'That\'s my motto: "overcome everything". ',\
#                     'Till next time squid".',\
#
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
#         self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
#         self.addpart(animation1)
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'sailor1','sailor2','sailor3','sailor4','sailor5') )
#         animation1.addsound( "sailor2", [41, 153] )
#         animation1.addsound( "sailor4", [261] )
#         #
#         self.addpart( draw.obj_music('sailor') )
#
#
# class obj_scene_ch6p45(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p44())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p46())
#     def setup(self):
#         self.text=[\
#                   '"The ',('{bug}',share.colors.bug),\
#                   ' crawled out of ',('{heroname}',share.colors.hero),\
#                   '\'s pocket and whispered: ',\
#                    'this is it, we have completed the tower\'s ',\
#                    ('password',share.colors.password2),'. It reads: ',\
#                     ('"fight persevere overcome"',share.colors.password),\
#                     '. Lets get a good night sleep and tomorrow we will finally rescue ',\
#                     ('{partnername}',share.colors.partner),'!". ',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.sound=draw.obj_sound('unlock')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('sailor') )
#
#
# class obj_scene_ch6p46(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p45())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p47())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         share.datamanager.setbookmark('ch6_gohome')
#         self.text=['go back home']
#         self.world=world.obj_world_travel(self,start='beach',goal='home',chapter=6,boat=True)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music(None) )
#
#
# class obj_scene_ch6p47(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p46())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p48())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"Back at home, ',\
#                    ('{heroname}',share.colors.hero),' was all excited ',\
#                    'thinking about how ',\
#                    ('{hero_he}',share.colors.hero2),' would soon charm ',\
#                    ('{partnername}',share.colors.partner),' with a serenade." ',\
#                    ]
#         self.world=world.obj_world_serenade(self,partner=False)
#         self.addpart(self.world)
#         self.addpart( draw.obj_animation('ch5_serenadebug','bug',(640,360),record=False) )
#         #
#         self.addpart( draw.obj_music('piano') )
#
#
# class obj_scene_ch6p48(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p47())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p49())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"',\
#                    ('{hero_he}',share.colors.hero),' thought about how ',\
#                    ('{hero_him}',share.colors.hero2),' and ',\
#                    ('{partnername}',share.colors.partner),' would soon be kissing". ',\
#                    ]
#         self.world=world.obj_world_kiss(self,noending=False)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
#
# # no need for sunset (already done on skull island)
# class obj_scene_ch6p49(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6p48())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch6end())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"',\
#                    ('{heroname}',share.colors.hero),\
#                    ' went back to bed with a large smile on ',\
#                    ('{hero_his}',share.colors.hero2),' face ".',\
#                    ]
#         self.world=world.obj_world_gotobed(self,bug=True,alarmclock=False)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
