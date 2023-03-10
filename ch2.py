#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter2.py: ...
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

# Chapter II: ...
# *CHAPTER II



class obj_scene_chapter2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def setup(self):
        share.datamanager.setbookmark('ch2_start')
        self.text=['-----   Chapter II: Home Sweet Home   -----   ',\
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



class obj_scene_ch2p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1a())
    def setup(self):
        self.text=['Lets see here... "the ',('hero',share.colors.hero2),\
                    ' woke up... mmmh... caught a ',('fish',share.colors.item2),', ate it ',\
                    'and went back to ',('bed',share.colors.item2),'." '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation=draw.obj_animation('ch2_summary','herobase',(640,360),record=False,scale=0.7)
        animation.addimage('herobasefish')
        animation2=draw.obj_animation('ch2_summary2','sun',(640,360),record=False,sync=animation,scale=0.5)
        animation2.addimage('moon',scale=0.5)
        self.addpart(animation2)
        self.addpart(animation)

        # self.addpart( draw.obj_soundplacer(animation,'wake1','wake2','snore1','snore2') )
        # self.addpart( draw.obj_soundplacer(animation,'eat','eatend') )
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3','hero4','hero5','hero6') )
        animation.addsound( "wakeup_wake1", [2, 410] )
        animation.addsound( "wakeup_wake2", [74] )
        animation.addsound( "wakeup_snore1", [539] )
        animation.addsound( "wakeup_snore2", [557] )
        animation.addsound( "eat", [279] )
        animation.addsound( "eatend", [288] )
        # animation.addsound( "hero1", [122] )
        animation.addsound( "hero2", [135] )
        #
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch2p1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def setup(self):
        self.text=[\
                   'Well, this ',('{heroname}',share.colors.hero),' feels a bit lonely. ',\
                  ('{hero_he}',share.colors.hero2),' could surely use some company. ',\
                   ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','exclamationmark',(640,360),record=False,path='data/premade',sync=animation1)
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [13] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch2p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def setup(self):
        share.datamanager.setbookmark('ch2_drawlove')
        self.text=[\
               'I want ',('{heroname}',share.colors.hero),\
               ' to  be madly in love with someone. First draw a ',\
                 ('love heart',share.colors.item),'. ',\
                   ]
        # self.addpart( draw.obj_drawing('love',(640,450),legend='love heart',shadow=(300,200),brush=share.brushes.bigpen) )
        self.addpart( draw.obj_drawing('lovedraw',(640,450),legend='love heart',shadow=(225,150),brush=share.brushes.pen12) )#smaller
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def textboxset(self):
        self.textboxopt={'xy':(640,510),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch2_writepartner')
        self.text=[\
                 'Great, lets write: ',\
                '"',('{heroname}',share.colors.hero),\
                ' and ',('{hero_his}',share.colors.hero2),' ',\
                ('partner',share.colors.partner2),' were madly in ',\
                ('love',share.colors.partner2),'." '\
                'Choose a name and gender for this ',('partner',share.colors.partner),'. '\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the partner\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('partnername',20,(750,yref), legend='partner name') )
        #
        self.addpart( draw.obj_textbox('and the partner was:',(180,yref+dyref)) )
        textchoice=draw.obj_textchoice('partner_he',suggested='she')
        textchoice.addchoice('1. A guy','he',(440,yref+dyref))
        textchoice.addchoice('2. A girl','she',(740,yref+dyref))
        textchoice.addchoice('3. A thing','it',(1040,yref+dyref))
        textchoice.addkey('partner_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('partner_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        #
        self.addpart(draw.obj_animation('ch2_love1','love',(220,540),scale=0.3))
        self.addpart(draw.obj_animation('ch2_love1','love',(1280-220,540),scale=0.3))
        #
        self.addpart( draw.obj_music('partner') )



class obj_scene_ch2p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def setup(self):
        self.text=['Now draw some pretty hair for ',\
                    ('{partnername}',share.colors.partner),'\'s hair, said the book of things. ',\
                   ]
        self.addpart( draw.obj_drawing('partnerhairdraw',(640,450-50),legend='draw the partner\'s hair',shadow=(250,250),brush=share.brushes.pen5) )

        self.addpart( draw.obj_image('herohead',(640,450-50),path='data/premade',scale=0.625) )# add empty head on top
        self.addpart(draw.obj_animation('ch2_love2','love',(220,360),record=False,scale=0.3))
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.3))
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                   'Lets see who is this mysterious ',('{partnername}',share.colors.partner),' ',\
                  'under all that pretty hair. ',\
                  ' The tension is killing me! ',\
                   ]
        animation=draw.obj_animation('ch2_love2','love',(220,360),scale=0.3)
        self.addpart(animation)
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.3))
        self.addpart(draw.obj_animation('ch2_herobase1','herobase',(640,360),scale=0.75,record=False,sync=animation))
        self.addpart(draw.obj_animation('ch2_partnerbasenoface','partnerbasenoface',(640,360),scale=0.75,record=False,sync=animation))
        #
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3','hero4') )
        animation.addsound( "hero1", [12] )
        animation.addsound( "hero4", [115],skip=1 )
        #
        self.addpart( draw.obj_music('partner') )

class obj_scene_ch2p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6a())
    def setup(self):
        self.text=[\
                   'Uh...Well... ',\
                  ('{heroname}',share.colors.hero),' and ',\
                 ('{partnername}',share.colors.partner),' do look a bit alike, but thats cool. ',\
                   'They aint siblings at least (unless you are into that). ',\
                   ]
        animation=draw.obj_animation('ch2_love2','love',(220,360),scale=0.3)
        self.addpart(animation)
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.3))
        self.addpart(draw.obj_animation('ch2_herobase1','herobase',(640,360),scale=0.75,sync=animation))
        self.addpart(draw.obj_animation('ch2_partnerbasenoface','partnerbase',(640,360),scale=0.75,sync=animation))
        #
        #
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        animation.addsound( "partner1", [20] )
        animation.addsound( "partner2", [160],skip=1 )
        #
        self.addpart( draw.obj_music('partner') )

class obj_scene_ch2p6a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6b())
    def setup(self):
        share.datamanager.setbookmark('ch2_drawmail')
        self.text=[\
                   'Alright, our lovers want to send passionate letters to each other. ',\
                   'Draw a ',('mailbox on a pole',share.colors.item),' and a ',('mail letter',share.colors.item),'. ',\
                   ]
        # self.textkeys={'pos':(500,20),'xmin':500}# same as ={}
        self.addpart( draw.obj_drawing('mailbox',(340,450-50),legend='Mailbox on a pole',shadow=(200,250)) )
        self.addpart( draw.obj_drawing('mailletter',(1280-340,450),legend='Mail Letter',shadow=(200,200)) )
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p6b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6c())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                    'Great, lets write: "',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'a ',' letter." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','mailbox','mailletter') )
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
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p6c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p7())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(50,53),xleft=True) )
        xmargin=150
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':740}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI just wanted to tell you I love you very very much. ',\
                    '\nXOXO, ',\
                    '\n\nsigned: ',('{partnername}',share.colors.partner),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        # self.addpart( draw.obj_image('partnerhead',(1065,305),scale=0.5) )
        self.addpart( draw.obj_image('love',(716,546),scale=0.25) )
        #
        animation1=draw.obj_animation('ch2_mailhead','partnerhead',(640,360))
        self.addpart(animation1)
        animation1.addsound( "partner1", [100],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p8())
    def setup(self):
        share.datamanager.setbookmark('ch2_drawmusic')
        self.text=[\
                    'Aww that is so sweet. ',\
                   ('{heroname}',share.colors.hero),' wants to show ',\
                   ('{hero_his}',share.colors.hero2),' love too. ',\
                   'Draw a ',('saxophone',share.colors.item),' and a ',('music note',share.colors.item),\
                   ' so ',('{hero_he}',share.colors.hero2),' can play ',\
                   ('{partnername}',share.colors.partner),' a serenade. ',\
                   ]
        self.addpart( draw.obj_drawing('saxophone',(340,450),legend='Saxophone (facing right)',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('musicnote',(1280-340,450),legend='Music Note',shadow=(200,200)) )
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def triggernextpage(self,controls):
        return self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
                   'Play the melody with the '+tempo+' to serenade ',('{partnername}',share.colors.partner),'. '\
                   ]
        self.world=world.obj_world_serenade(self)# serenade mini-game
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music(None) )


class obj_scene_ch2p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())
    def setup(self):
        self.text=[\
                   'Thats it, said the book of things. ',\
                   ('{heroname}',share.colors.hero),' has totally charmed ',\
                   ('{partnername}',share.colors.partner),' with ',\
                   ('{hero_his}',share.colors.hero2),' serenade. ',\
                   'Its time to go for the ',('kiss',share.colors.partner2),'! ',\
                   ]
        animation=draw.obj_animation('ch2_partner2','partnerbase',(640,360),scale=0.7,record=False)
        self.addpart(animation)
        self.addpart(draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4,record=False,sync=animation))
        self.addpart(draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4,record=False,sync=animation))
        #
        # self.addpart( draw.obj_soundplacer(animation,'partner1','partner2','partner3') )
        animation.addsound( "partner1", [65] )
        animation.addsound( "partner2", [189] )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def triggernextpage(self,controls):
        return self.world.done# quick skip
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempol='['+share.datamanager.controlname('left')+']'
        tempor='['+share.datamanager.controlname('right')+']'
        self.text=[\
                   'Hold '+tempol+'+'+tempor+' to make them kiss.   ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)# kiss mini-game
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('partner') )


class obj_scene_ch2p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play())
    def setup(self):
        share.datamanager.setbookmark('ch2_drawhouse')
        self.text=[\
                   'Ewww gross, get some privacy next time. ',\
                   'Moving on, lets draw a ',\
                   ('house',share.colors.item),' with some big ',\
                   ('bushes',share.colors.item),' where they live happily together. ',\
                   ]
        # self.addpart( draw.obj_drawing('house',(940,450),legend='House',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('housedraw',(340,450-50),legend='House',shadow=(250,250)) )
        self.addpart( draw.obj_drawing('bushdraw',(940,450-50),legend='Big Bush',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('partner') )




##########################################################
##########################################################
# PLAY CHAPTER

class obj_scene_ch2play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def setup(self):
        share.datamanager.setbookmark('ch2_startplay')
        self.text=[\
                    'That wraps it nicely, says the book of things. ',\
                   'Now, lets read our story one more time. ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)

        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [120] )
        animation.addsound( "pen", [199] )
        animation.addsound( "eraser", [185],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch2play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1a())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"Once upon a time, there was a ',('hero',share.colors.hero2),' ',\
                'called ',('{heroname}',share.colors.hero),' ',\
                'that lived in a house with some bushes. ',\
                'It was morning and the sun was rising." ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch2play1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item2),' ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' ',('partner',share.colors.partner2),\
                ' ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch2play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' caught a ',\
                    ('fish',share.colors.item2),' and they ate it for breakfast."',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )




class obj_scene_ch2play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '"',\
                    'They spent the day talking and walking, then went back home."',\
                   ]
        self.world=world.obj_world_travel(self,start=(-610,-330),goal='home',chapter=2,partner=True)
        self.addpart(self.world)
        #
        # self.addpart( draw.obj_drawing('textbanner',(640,70),shadow=(600,70)) )
        # self.addpart( draw.obj_image('textbanner',(640,70),path='data/premade') )
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch2play3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def nextpage(self):
        # share.scenemanager.switchscene(obj_scene_ch2play4())
        share.scenemanager.switchscene(obj_scene_ch2play6())
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

# class obj_scene_ch2play4(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play3a())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play5())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                     '"In the evening, ',\
#                    '"',('{heroname}',share.colors.hero),' charmed ',\
#                    ('{partnername}',share.colors.partner),' with a serenade..." ',\
#                    ]
#         self.world=world.obj_world_serenade(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )


# shorten the story, remove this
# class obj_scene_ch2play5(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play4())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play6())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"...and then they kissed."   ',\
#                    ]
#         self.world=world.obj_world_kiss(self,noending=False)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )


# class obj_scene_ch2play5a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play5())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2play6())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                 '"It was already night."',\
#                    ]
#         self.world=world.obj_world_sunset(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )


class obj_scene_ch2play6(page.obj_chapterpage):
    def prevpage(self):
        # share.scenemanager.switchscene(obj_scene_ch2play5())
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' kissed and went to back to bed. They were very happy." ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch2playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2unlocknext())
    def setup(self):
        self.text=[\
                    'Well, thats all for today, said the book of things. ',
                   'This story looks really perfect, ',\
                   'but maybe something really really bad will happen tommorrow. Who knows! ',\
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


class obj_scene_ch2unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def setup(self):
        share.datamanager.setbookmark('ch2_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter III',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=3)# chapter 3 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )


#######################################################################


# class obj_scene_ch2p12(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2p11())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2p13())
#     def setup(self):
#         self.text=[\
#                   'This is what the house looks like. Move around to check it out. ',\
#                    ]
#         self.world=world.obj_world_travel(self,start=(-140,-110),goal='nowhere',chapter=2,remove=['bush','pond'])
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('partner') )


# class obj_scene_ch2p12(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2p11())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch2p13())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                   'This is what the house looks like. Go to the garden and pick up a flower for ',\
#                   ('{partnername}',share.colors.partner),'. ',\
#                    ]
#         self.world=world.obj_world_travel(self,start=(240-640,540-360),\
#         goal='atpartner',chapter=2,minigame='flowers',remove=['bush','pond'])
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('partner') )
