#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter4.py: ...
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

# Chapter IV: ...
# *CHAPTER IV



class obj_scene_chapter4(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def setup(self):
        share.datamanager.setbookmark('ch4_start')
        self.text=['-----   Chapter IV: Down the Rabbit Hole   -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: well, lets continue our story where we left. ',\
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



class obj_scene_ch4p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def setup(self):
        self.text=[\
                  '"',
                   ('{partnername}',share.colors.partner),' is being held captive in ',\
                    ('{villainname}',share.colors.villain),'\'s ',\
                     ('evil tower',share.colors.location2),', and ',\
                     ('{heroname}',share.colors.hero),' is trying to figure out the tower\'s ',\
                     ('password',share.colors.password2),'. ',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        self.addpart( draw.obj_image('tower',(1156,312),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(981,265),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(866,243),scale=0.23,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch4_villaincapture1','villainbase',(640,360),record=False)
        animation1.addimage('villainholdspartner')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_villaincapture2','partnerbase',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','partner_scared') )
        animation1.addsound( "villain1", [20] )
        animation1.addsound( "villain2", [300] )
        animation1.addsound( "villain3", [155] )
        animation1.addsound( "partner_scared", [228] )
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch4p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2a())
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),\
                   ' has befriended a terrifying ',('{bug}',share.colors.bug),\
                    ', and they need to visit three ',\
                    ('grandmaster of deceit',share.colors.grandmaster),\
                    ' that know parts of the tower\'s password."',\
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


class obj_scene_ch4p2a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        share.datamanager.setbookmark('ch4_drawalarm')
        self.text=[\
                   'First, lets make sure ',('{heroname}',share.colors.hero),\
                   ' wakes up on time today, said the book of things. ',\
                   'Draw a ',('night stand',share.colors.item),\
                   ' and an ',('alarm clock',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('nightstand',(200+50,450),legend='night stand',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('alarmclockext',(940,450),legend='alarm clock (draw the exterior)',shadow=(200,200)) )
        self.addpart( draw.obj_image('alarmclockfill',(940,450),path='data/premade') )
        self.addpart( draw.obj_image('alarmclockcenter8am',(940,450),path='data/premade') )
        #
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch4p2a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        share.datamanager.setbookmark('ch4_drawalarm')
        self.text=[\
                   'First, lets make sure ',('{heroname}',share.colors.hero),\
                   ' wakes up on time today, said the book of things. ',\
                   'Draw a ',('night stand',share.colors.item),\
                   ' and an ',('alarm clock',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('nightstanddraw',(340,450-50),legend='night stand',shadow=(250,250)) )
        self.addpart( draw.obj_drawing('alarmclockextdraw',(940,450-50),legend='alarm clock (draw the exterior)',shadow=(250,250)) )
        self.addpart( draw.obj_image('alarmclockfill',(940,450-50),path='data/premade',scale=1.25) )
        self.addpart( draw.obj_image('alarmclockcenter8am',(940,450-50),path='data/premade',scale=1.25) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch4p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def triggernextpage(self,controls):
        return self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        share.datamanager.setbookmark('ch4_startstory')
        self.text=[\
               'Lets do this, said the book of things: ',\
                '"once upon a time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' that lived in a house. ',\
                'It was morning and the sun was rising." ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from bed with ',\
                ('{hero_his}',share.colors.hero2),\
                ' new friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )

class obj_scene_ch4p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),\
                     ' went to the pond and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch4_checkmail')
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'a ',' letter". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6','mailjump') )
        animation1.addsound( "hero2", [82] )
        animation1.addsound( "mailjump", [7] )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def textboxplace(self):
        self.textboxprevpage_xy=(1050,55)
        self.textboxnextpage_xy=(1230,55)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nWasup. Last time I checked, ',('{partnername}',share.colors.partner),\
                    ' is still being held hostage in my ',\
                     ('evil tower',share.colors.location2),'. Come save ',\
                     ('{partner_him}',share.colors.partner2),' if you dare. ',\
                     'Whenever, muahahahaha. ',\
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
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: the first ',\
                   ('grandmaster of deceit',share.colors.grandmaster),\
                    ' lives in the east not far from here. Lets get going." ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 100] )
        animation1.addsound( "bug2", [116],skip=1 )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def setup(self):
        share.datamanager.setbookmark('ch4_drawcave')
        self.text=['The ',\
                    ('grandmaster',share.colors.grandmaster),\
                    '\'s home is a magical cave in a dark forest,',\
                    ' said the book of things. ',\
                    'Draw a ',('cave',share.colors.item),\
                    ' and a ',('tree',share.colors.item),' and we will be on our way. ',\
                   ]
        self.addpart( draw.obj_drawing('cavedraw',(340,450-50),legend='cave',shadow=(250,250),brush=share.brushes.pen10) )
        self.addpart( draw.obj_drawing('treedraw',(940,450-50),legend='tree',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                'go to the magical cave in the east',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='forest',chapter=4)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def setup(self):
        share.datamanager.setbookmark('ch4_writebunny')
        self.text=[\
                '"Arrived at the ',('magical cave',share.colors.location2),', ',\
                ('{heroname}',share.colors.hero),\
                ' met an extremely cute ',('bunny',share.colors.bunny),'." ',\
                'Awww, how nice said the book of things. Choose a name for the ',('bunny',share.colors.bunny),'. ',\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the bunny\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('bunnyname',20,(750,yref), legend='bunny name') )
        #
        self.addpart( draw.obj_music('ch4') )
        #


class obj_scene_ch4p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12a())
    def setup(self):
        self.textboxnextpage_xy=(1280-100,360)
        self.text=[]
        self.addpart( draw.obj_image('bunnystickhead',(640,360+150-10),scale=0.75,path='data/premade') )
        self.addpart( draw.obj_drawing('bunnyfacedraw',(640,360-10),legend='draw a bunny head (facing right)',shadow=(400,300)) )
        #
        self.addpart( draw.obj_music('ch4') )


# class obj_scene_ch4p12a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p12())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p13())
#     def setup(self):
#         self.text=[\
#                 'Now draw ',('{bunnyname}',share.colors.bunny),'\'s body. ',\
#                 'Remember to make it very cute! ',\
#                    ]
#         yref=400
#         self.addpart( draw.obj_drawing('bunnybody',(640,yref+65),legend='bunny body (facing right)',shadow=(200,105+50),brush=share.brushes.pen6) )
#         self.addpart( draw.obj_image('bunnyhead',(640,yref-150),scale=0.5) )
#         #
#         self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p12a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def setup(self):
        self.text=[' ']
        self.addpart( draw.obj_drawing('bunnybodydraw',(640,400+98-100),legend='draw the bunny\'s body (facing right)',shadow=(300,233)) )
        self.addpart( draw.obj_image('bunnyhead',(640,400-225-100),scale=0.75) )
        #
        self.addpart( draw.obj_music('ch4') )



class obj_scene_ch4p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                'Moving on, said the book of things: ',\
                '"',('{heroname}',share.colors.hero),\
                ' met a ',('bunny',share.colors.bunny),' called ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                ('{hero_he}',share.colors.hero),' said: ',\
                ' wow, you are so cute, can I pet you." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        # self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bunnybase',(867,525),scale=0.62,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_herowalkbunny1','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny3", [43],skip=1 )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def setup(self):
        self.text=[\
                '"Ha! You think I am cute, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'Look at these trees, poof, I chopped them all ',\
                'with my ',('LITTLE PAWS',share.colors.bunny),'!" ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bunnybase',(867,525),scale=0.62,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(618,439),scale=1.28,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_bunnyeats1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_bunnyeats2','tree',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='data/premade')
        animation2.addimage('poof',path='data/premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch4_bunnyeats3','tree',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
        animation3.addimage('poof',path='data/premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_bunnyeats4','tree',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='data/premade')
        animation4.addimage('poof',path='data/premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch4_bunnyeats5','tree',(640,360),record=False,sync=animation1)
        animation5.addimage('empty',path='data/premade')
        animation5.addimage('poof',path='data/premade')
        self.addpart( animation5 )
        #
        self.sound=draw.obj_sound('revealscary')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5','bunny_scream') )
        animation1.addsound( "bunny2", [0] )
        animation1.addsound( "bunny5", [160] )
        animation1.addsound( "bunny_hit", [159, 203, 243, 264] )
        #
        self.addpart( draw.obj_music('tension') )




class obj_scene_ch4p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def setup(self):
        self.text=[\
                '"Hahaha, said the ',('bunny',share.colors.bunny),'. ',\
                'Do not underestimate me. ',\
                'I am ',('{bunnyname}',share.colors.bunny),\
                ', the ',('grandmaster of deceit',share.colors.grandmaster),\
                ' from the east! ',\
                'Tremble before me." ',\
                   ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny3", [16] )
        animation1.addsound( "bunny4", [73] )
        animation1.addsound( "bunny5", [103],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingstart())
    def setup(self):
        self.text=[\
                '"So you want to know ',\
                ('my part of the tower\'s password',share.colors.password),'. ',\
                'Tell you what, I will give it to you if you win my ',('lying game',share.colors.grandmaster2),\
                '." ',\
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
        animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny3", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )


#################################################################
# Lying game
# *LYING
#
class obj_scene_lyingstart(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def setup(self):
        share.datamanager.setbookmark('ch4_startlying')
        self.text=[\
                '"The lying game is all about having a good memory and mastering the art of deception, said ',\
                ('{bunnyname}',share.colors.bunny),'. Now lets get started."',\

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
        animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny3", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )


##########################
class obj_scene_lyingpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingstart())
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
                    'You can even take some notes at the bottom of the screen. '
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
        #
        self.sound=draw.obj_sound('bunny2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


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
        #
        self.sound=draw.obj_sound('bunny3')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


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
    def firstsound(self):
        self.sound=draw.obj_sound('bunny2')
        self.addpart(self.sound)
        self.sound.play()

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
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you gave me the wrong answer. ',\
                    'Now go back and win this first round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('bunny5')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_lyingpart1win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        share.datamanager.setbookmark('ch4_winlying1')
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
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny4", [128] )
        animation1.addsound( "bunny3", [43] )
        #
        self.addpart( draw.obj_music('bunny') )


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
        #
        self.sound=draw.obj_sound('bunny2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


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
                    'Now go back and win this second round. ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('bunny5')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_lyingpart2win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        share.datamanager.setbookmark('ch4_winlying2')
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
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_herowalkbunny2love2','love',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='data/premade')
        self.addpart( animation4 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny4", [43,128] )
        # animation1.addsound( "bunny3", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )


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
        #
        self.sound=draw.obj_sound('bunny2')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


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
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you actually gave me the correct answer. ',\
                    'For this third round, remember that ',\
                    ('all my statements are false',share.colors.red),\
                    ', and that you must ',\
                    ('always give me the wrong answer',share.colors.red),'. ',\
                    'Now go back and win this third round. ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        self.sound=draw.obj_sound('bunny5')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_lyingend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def setup(self):
        share.datamanager.setbookmark('ch4_winlying3')
        self.text=[\
                    '"Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won my ',('lying game',share.colors.grandmaster2),'! ',\
                    ' You are truly a great deceiver!"',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_herowalkbunny2love2','love',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='data/premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch4_herowalkbunny2love3','love',(640,360),record=False,sync=animation1)
        animation5.addimage('empty',path='data/premade')
        self.addpart( animation5 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.sound=draw.obj_sound('serenade_cheer')
        self.addpart(self.sound)
        self.sound.play()
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [128] )
        animation1.addsound( "bunny4", [43] )
        #
        self.addpart( draw.obj_music('bunny') )


# End of lying minigame
#################################################################

class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingend())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def setup(self):
        self.text=[\
                    '"The first part of the tower\'s password is: ',\
                    ('"fight"',share.colors.password),'. ',\
                    'That\'s my motto: fight in any situation, that I taught to ',\
                    ('{villainname}',share.colors.villain),' when ',\
                    ('{villain_he}',share.colors.villain2),' was my student." ',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny3inter','interrogationmark',(640,360),record=False,sync=animation1,path='data/premade')
        animation3.addimage('empty',path='data/premade')
        self.addpart( animation3 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny4", [43],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    def setup(self):
        self.text=[\
                '"The ',('{bug}',share.colors.bug),\
                ' crawled out of ',('{heroname}',share.colors.hero),\
                '\'s pocket and whispered: ',\
                'Well done, soon we will be able to figure out the entire password! ',\
                'Now lets scram." ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 100] )
        animation1.addsound( "bug2", [116],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )




class obj_scene_ch4p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        share.datamanager.setbookmark('ch4_gohome')
        self.text=[\
                'go back home',\
                   ]
        self.world=world.obj_world_travel(self,start='forest',goal='home',chapter=4)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music(None) )



class obj_scene_ch4p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p22())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                   '"Back at home, ',\
                   ('{heroname}',share.colors.hero), ' remembered how ',\
                   ('{hero_he}',share.colors.hero2),' used to charm ',\
                   ('{partnername}',share.colors.partner),' with a serenade. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch4p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p23())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                   '"This made ',('{hero_him}',share.colors.hero2),\
                   ' so sad that ',\
                   ('{hero_he}',share.colors.hero),\
                   ' went straight to bed." ',\
                   ]
        self.world=world.obj_world_gotobed(self,bug=True,addmoon=False,addsun=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch4p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                '"The night fell, but tomorrow would be another day."',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch4end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=[\
                    'And thats all for today, said the book of things. ',\
                   'Lets wait and find what happens tomorrow. ',\
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


class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        share.datamanager.setbookmark('ch4_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter V',share.colors.instructions),'! ',\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )
#





####################################################################################
####################################################################################
