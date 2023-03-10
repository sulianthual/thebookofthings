#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter3.py: ...
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

# Chapter III: ...
# *CHAPTER III


class obj_scene_chapter3(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def setup(self):
        share.datamanager.setbookmark('ch3_start')
        self.text=['-----   Chapter III: In Another Castle   -----   ',\
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



class obj_scene_ch3p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1a())
    def setup(self):
        self.text=['Lets see here... " the ',('hero',share.colors.hero2),\
                   ' and ',('{hero_his}',share.colors.hero2),' ',('partner',share.colors.partner2),\
                    ' were madly in love. They would just eat fish and kiss all day." '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation=draw.obj_animation('ch3_summary','herobase',(640,360),record=False,scale=0.7)
        animation.addimage('herobasefish')
        animation2=draw.obj_animation('ch3_summary2','partnerbase',(640,360),record=False,sync=animation,scale=0.7)
        animation3=draw.obj_animation('ch3_summary3','love',(640,360),record=False,sync=animation)
        animation3.addimage('empty',path='data/premade')# was guitar, obsolete
        animation3.addimage('empty',path='data/premade')
        animation4=draw.obj_animation('ch3_summary4','sun',(640,360),record=False,sync=animation)
        animation4.addimage('moon')
        animation4.addimage('empty',path='data/premade')
        self.addpart(animation4)
        self.addpart(animation2)
        self.addpart(animation)
        self.addpart(animation3)
        #
        # self.addpart( draw.obj_soundplacer(animation,'wake1','wake2','snore1','snore2') )
        # self.addpart( draw.obj_soundplacer(animation,'eat','eatend') )
        self.addpart( draw.obj_soundplacer(animation,'hero2','eat','eatend','kiss_kiss','wakeup_snore1','wakeup_snore2') )
        animation.addsound( "wakeup_wake1", [5, 470] )
        animation.addsound( "hero2", [90] )
        animation.addsound( "eat", [201] )
        animation.addsound( "eatend", [217] )
        animation.addsound( "kiss_kiss", [350] )
        animation.addsound( "wakeup_snore1", [619] )
        animation.addsound( "wakeup_snore2", [623] )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3p1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())
    def setup(self):
        self.text=[\
                   'Well, this story reads too much like a ',\
                   ('chick flick',share.colors.partner2),', said the book of things, ',\
                   'It needs more action, more suspense! ',\
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


class obj_scene_ch3p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())
    def textboxset(self):
        self.textboxopt={'xy':(640,510),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch3_writevillain')
        self.text=[\
                   'Let\'s add a ',\
                   ('villain',share.colors.villain), ' to our story that is pure hatred and evil. ',\
                'First, choose a name and gender for this ',('villain',share.colors.villain),'. '\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the villain\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('villainname',20,(750,yref), legend='villain name') )
        #
        self.addpart( draw.obj_textbox('and the villain was:',(180,yref+dyref)) )
        textchoice=draw.obj_textchoice('villain_he',suggested='he')
        textchoice.addchoice('1. A guy','he',(440,yref+dyref))
        textchoice.addchoice('2. A girl','she',(740,yref+dyref))
        textchoice.addchoice('3. A thing','it',(1040,yref+dyref))
        textchoice.addkey('villain_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('villain_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3a())
    def setup(self):
        self.text=[\
                    'Now draw an ',('angry face',share.colors.item),' for ',\
                    ('{villainname}',share.colors.villain),\
                    ', and make ',('{villain_him}',share.colors.villain2),\
                    ' look slightly to the right. ',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450-50),path='data/premade',scale=2.5) )
        self.addpart( draw.obj_drawing('angryfacedraw',(640,450-50),legend='draw an angry face (facing right)',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4())
    def setup(self):
        self.text=[\
                 ('{villainname}',share.colors.villain),' has probably been hurt a lot, ',\
                 'so lets add a big ',('scar',share.colors.item),' on ',\
                 ('{villain_his}',share.colors.villain2),' face. ',\
                   ]
        self.addpart( draw.obj_image('angryhead',(640,450-50),scale=1.25) )
        self.addpart( draw.obj_drawing('scardraw',(640,450-50),legend='add a big scar',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4a())
    def setup(self):
        self.text=[\
                    'This is what ',('{villainname}',share.colors.villain),' looks like. ',\
                   'Indeed, ',('{villain_he}',share.colors.villain2),' looks very scary! ',\
                   ]
        animation1=draw.obj_animation('ch1_hero1','villainbase',(360,360),record=False)
        self.addpart(animation1)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain1", [5] )
        animation1.addsound( "villain2", [135] )
        animation1.addsound( "villain3", [85] )
        #
        self.addpart( draw.obj_music('villain') )



class obj_scene_ch3p4a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def setup(self):
        self.text=[\
                   'This should get interesting, said the book of things. ',\
                   'Lets continue our story. ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)

        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [46] )
        animation.addsound( "book2", [55] )
        animation.addsound( "pen", [189] )
        animation.addsound( "eraser", [199] )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch3p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch3_startstory')
        self.text=[\
                '"Once upon a Time, there was a ',('hero',share.colors.hero2),' ',\
                'called  ',('{heroname}',share.colors.hero),'. ',\
                'It was morning and the sun was rising." ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item2),' ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' partner ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner=True)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero2),\
                     ' went to the lake and caught a fish."\n ',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9a())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch3_checkmail')
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home but ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                    ('{hero_he}',share.colors.hero2),' checked ',\
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
        # self.addpart( draw.obj_imageplacer(self,'herobase','mailbox','mailletter') )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6','mailjump') )
        animation1.addsound( "hero2", [82] )
        animation1.addsound( "mailjump", [7] )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3p9a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9b())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' carefully opened the letter and started reading." ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailletter',(333,442),scale=0.33,rotate=6,fliph=False,flipv=False) )
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
        #
        self.addpart( draw.obj_music('piano') )




class obj_scene_ch3p9b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def setup(self):
        self.text=[\
                  '"Suddendly, ',\
                    ('{heroname}',share.colors.hero),' shouted: No, No, No, this cannot be!" ',\
                   ]
        # self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mailletter',(333,442),scale=0.33,rotate=6,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail2','sun',(640,360))
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch3_herodesperate','herobase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        self.addpart( draw.obj_animation('ch3_mailfails','mailletter',(640,360),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'partner_scared') )
        animation1.addsound( "revealscary", [1] )
        # animation1.addsound( "partner_scared", [140],skip=2 )
        animation1.addsound( "partner_scared", [40],skip=2 )
        #
        self.addpart( draw.obj_music('tension') )
        #



class obj_scene_ch3p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI have captured ',('{partnername}',share.colors.partner),'. ',\
                    ('{partner_he}',share.colors.partner2),\
                     ' is in my evil lair. ',\
                     'Come rescue ',\
                     ('{partner_him}',share.colors.partner2),' if you dare. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        # self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        #
        animation1=draw.obj_animation('ch2_mailhead','villainhead',(640,360),imgscale=0.7)
        self.addpart(animation1)
        animation1.addsound( "villain2", [100],skip=1 )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def setup(self):
        self.text=[\
                  '"Indeed, ',\
                  ('{villainname}',share.colors.villain),' had managed to capture ',\
                  ('{partnername}',share.colors.partner),' while ',('{heroname}',share.colors.hero),' was gone fishing." ',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
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
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def setup(self):
        share.datamanager.setbookmark('ch3_drawmountain')
        self.text=[\

                 'Lets continue: "the evil lair was a tower in the mountains." '\
                 'Draw an ',('tower',share.colors.item),\
                 ' and a ',('mountain',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('towerdraw',(340,450-50),legend='evil tower',shadow=(250,250)) )
        self.addpart( draw.obj_drawing('mountaindraw',(940,450-50),legend='mountain',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                'go to the evil tower in the west',\
                   ]
        # self.world=world.obj_world_travel(self,start='home',goal='tower',chapter=3,ambience=False)
        self.world=world.obj_world_travel(self,start='home',goal='tower',chapter=3)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('villain') )
        # self.addpart( draw.obj_music(None) )


class obj_scene_ch3p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{heroname}',share.colors.hero),\
                    ' arrived at the ',('evil tower',share.colors.location2),'. ',\
                  ('{villainname}',share.colors.villain),' said: muahaha, ',\
                  'get ready to ',\
                  ('fight',share.colors.villain2),'!" ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        # self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        self.addpart( draw.obj_image('mountain',(881,292),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(709,245),scale=0.29,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'mountain') )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain1", [40] )
        animation1.addsound( "villain2", [140],skip=1 )
        #
        self.addpart( draw.obj_music('villain') )



class obj_scene_ch3p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15a())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch3_drawgun')
        self.text=[\
                  'This is going to be epic, said the book of things. ',\
                 ' Draw a ',('gun',share.colors.item),' and a ',\
                ('bullet',share.colors.item),' for the fight. ',\
                   ]
        drawing1=draw.obj_drawing('gun',(300+50,450),legend='Gun (facing right)',shadow=(300,200))
        drawing1.brush.makebrush(share.brushes.bigpen)
        self.addpart(drawing1)
        drawing2=draw.obj_drawing('bullet',(1280-200-50,450),legend='Bullet (facing right)',shadow=(200,200))
        drawing2.brush.makebrush(share.brushes.bigpen)
        self.addpart(drawing2)
        #
        self.addpart( draw.obj_music('villain') )


class obj_scene_ch3p15a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p16())
    def setup(self):
        self.text=[\
                  '"This will be too easy, said ',\
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


class obj_scene_ch3p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p17())
    def setup(self):
        share.datamanager.setbookmark('ch3_startdodge')
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=['Instructions: ',\
        'Jump and crouch with the '+tempo+'. ',\
                    ]
        self.world=world.obj_world_dodgegunshots(self,tutorial=True)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show1',(560,540),path='data/premade',fliph=True))
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch3p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18())
    def setup(self):
        self.text=[\
                  'This is ',\
                  ('{heroname}',share.colors.hero),'\'s health. ',\
                  'Dont get hit or ',('{hero_he}',share.colors.hero2),' will die. ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self,tutorial=True)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show1',(390,290),path='data/premade',flipv=True))
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch3p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18a())
    def setup(self):
        self.text=[\
                  'This is how much bullets are left. ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self,tutorial=True)
        self.addpart(self.world)
        #
        self.addpart(draw.obj_image('show1',(857,313),path='data/premade',fliph=True,flipv=True))
        self.addpart( draw.obj_textbox('(not the actual fight)',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch3p18a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_dodgegunshots(self,tutorial=True)
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,300),color=share.colors.instructions) )
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch3p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18a())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3p20())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p19death())
    def triggernextpage(self,controls):
        return self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['\n ']# non empty for browser adjustment
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('gunfight') )


class obj_scene_ch3p19death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18a())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch3p18a())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p20())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero2),' died." ',\
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



class obj_scene_ch3p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p21())
    def setup(self):
        share.datamanager.setbookmark('ch3_windodge')
        self.text=[\
                  'Well done, said the book of things. Lets write down: ',\
                  '"',\
                  ('{villainname}',share.colors.villain),\
                  ' ran out of bullets and headed towards ',\
                  ('{villain_his}',share.colors.villain2),' ',\
                  ('evil tower',share.colors.location2),'." ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('tower',(1143,318),scale=0.67) )
        # self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        self.addpart( draw.obj_animation('ch3_villainretreatssun','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        # self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain'))
        #
        # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
        animation1.addsound( "villain1", [17] )
        animation1.addsound( "villain3", [45],skip=1 )
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch3p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22())
    def setup(self):
        share.datamanager.setbookmark('ch3_trypwd')
        self.text=[\
                  '"',\
                  ('{villainname}',share.colors.villain),' entered ',\
                  ('{villain_his}',share.colors.villain2),' ',\
                  ('evil tower',share.colors.location2),' and said: ',\
                  'muahaha, my ',\
                  ('tower',share.colors.location2),' is locked tight and protected by a ',\
                  ('password',share.colors.password),'. ',\
                  'You will never get in!"  ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
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
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch3p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p21())
    def nextpage(self):
        trypassword=share.datamanager.getword('towerpassword')
        earlypassword='abracadabra'
        if share.devmode or tool.comparestringparts(trypassword,earlypassword):
            share.scenemanager.switchscene(obj_scene_ch3p22easteregg())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p23())
    def soundnextpage(self):
        pass# no sound
    def textboxset(self):
        self.textboxopt={'xy':(380,300),'text':'[enter]','align':'center'}
    def setup(self):
        self.text=[\
                  '"The  ',('tower',share.colors.location2),'\'s a.s.s.',\
                  ' (automated security system) blasted: ',\
                  'lockdown engaged, password required. Please enter ',\
                  ('password',share.colors.password),'." ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('towerpassword',30,(380,180), legend='tower password',default='...')
        self.addpart( self.textinput )
        #
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation1.addsound( "tower1", [16, 79] )
        animation1.addsound( "tower2", [91] )
        animation1.addsound( "tower4", [99] )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'tower1','tower2','tower3','tower4','tower5') )
        self.addpart( draw.obj_music('tower') )


# easter egg: correct password entered too early
class obj_scene_ch3p22easteregg(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22easteregg2())
    def setup(self):
        self.text=[\
                '"You have entered: ',('"abracadabra"',share.colors.password),' . ',\
                'That... that is correct, said the tower\'s a.s.s. ',\
                'But how... how could you possibly know. ',\
                'I... I guess you may come in then." ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
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


class obj_scene_ch3p22easteregg2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22easteregg())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def setup(self):
        self.text=[\
                  '"Just joking, blasted the ',('tower',share.colors.location2),'\'s a.s.s., ',\
                  ' there is ',('NOOOO WAAAAY',share.colors.red),' i am letting you in this early in the game! ',\
                  'Nice try you little cheat." ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
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


class obj_scene_ch3p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def setup(self):
        trypassword=share.datamanager.getword('towerpassword')
        self.text=[\
                  '"You have entered: ',('"'+trypassword+'"',share.colors.password),' . ',\
                  'Wrong password, blasted the ',('tower',share.colors.location2),\
                  '\'s a.s.s.! And it zapped ',\
                  ('{heroname}',share.colors.hero),' with an electric shock." ']
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
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

########################

# OPTION TO REENTER PASSWORD SEVERAL TIMES
class obj_scene_ch3p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p23())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch3p25())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p24a())
    def textboxset(self):
        self.textboxopt={'xy':(330,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"Leave or dare to try another password, blasted the  ',\
                  ('tower',share.colors.location2),'\'s a.s.s. (automated security system).']
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation1.addsound( "tower1", [16, 79] )
        animation1.addsound( "tower2", [91] )
        animation1.addsound( "tower4", [99] )
        #
        y1=170
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Leave','yes',(330-100,y1))
        textchoice.addchoice('Try Again','no',(330+100,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch3p24a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def nextpage(self):
        trypassword=share.datamanager.getword('towerpassword')
        earlypassword='abracadabra'
        if share.devmode or tool.comparestringparts(trypassword,earlypassword):
            share.scenemanager.switchscene(obj_scene_ch3p22easteregg())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p24fail())
    def textboxset(self):
        self.textboxopt={'xy':(380,300),'text':'[enter]','align':'center'}
    def setup(self):
        self.text=[\
                  '"Please enter password, said the  ',('tower',share.colors.location2),'\'s a.s.s."',\
                   ]
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_towertalk','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation1.addsound( "tower1", [16, 79] )
        animation1.addsound( "tower2", [91] )
        animation1.addsound( "tower4", [99] )
        #
        self.textinput=draw.obj_textinput('towerpassword',30,(380,180), legend='tower password',default='...')
        self.addpart( self.textinput )
        #
        self.addpart( draw.obj_music('tower') )

class obj_scene_ch3p24fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def setup(self):
        trypassword=share.datamanager.getword('towerpassword')
        randolist=['Wrooooong','Failed again','Haha, I bet you are enjoying this']
        randotext=tool.randchoice(randolist)
        self.text=[\
                  '"You have entered: ',('"'+trypassword+'"',share.colors.password),' . ',\
                  ''+randotext+', blasted the ',('tower',share.colors.location2),\
                  '\'s a.s.s. , zapping engaged! AGAIN! ',\
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
        animation1.addsound( "tower_elec", [1, 115,261] )
        animation1.addsound( "tower_hurt", [115,261],skip=1 )
        #
        self.addpart( draw.obj_music('tower') )

########################

class obj_scene_ch3p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30a())
    def setup(self):
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' gave up. ',\
                'Till next time looser, blasted the tower\'s a.s.s." ',\
                   ]
        self.addpart( draw.obj_image('tower',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_suntower','sun',(640,360),record=False) )
        #
        animation1=draw.obj_animation('ch3_heroabandons','herobase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'tower1','tower2','tower3','tower4','tower5','tower6') )
        animation1.addsound( "tower2", [3] )
        animation1.addsound( "tower3", [18] )
        animation1.addsound( "tower6", [20],skip=1 )
        #
        self.addpart( draw.obj_music('tower') )



class obj_scene_ch3p30a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30b())
    def textboxset(self):
        self.textboxopt={'xy':(640,410),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch3_startbug')
        self.text=[\
                   'Alright, said the book of things, it looks like our ',\
                   ('hero',share.colors.hero2),' is stuck. ',\
                   'Lets  make ',('{hero_him}',share.colors.hero2),' a small ',('sidekick',share.colors.bug),\
                   ' to gives ',('{hero_him}',share.colors.hero2),' some hints. ',\
                   'First, choose a name for the sidekick.'
                   ]
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        # animation1.addsound( "bug1", [26, 37, 208],skip=1 )
        #
        self.addpart( draw.obj_textinput('bug',20,(640,260), legend='The small sidekick name') )
        #
        self.addpart( draw.obj_music('tower') )

class obj_scene_ch3p30b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30c())
    def setup(self):
        self.text=[\
                   '"Now draw ',('{bug}',share.colors.bug),' the sidekick. ',\
                   'It will be hovering and very small, like a flying pet." ',\
                   ]
        animation1=draw.obj_animation('ch1_sun','empty',(640,360),path='data/premade')
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        # animation1.addsound( "bug1", [24, 49, 166],skip=1 )
        #
        bugword=share.datamanager.getword('bug')
        # self.addpart( draw.obj_drawing('bug',(640,450),legend='draw a '+bugword+' (facing right)',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('bugdraw',(640,450-50),legend='draw '+bugword+' (facing right)',shadow=(250,250)) )
        #
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch3p30c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p31())
    def setup(self):
        self.text=[\
                   '"', \
                   ('{bug}',share.colors.bug),' the sidekick emerged and said:',\
                   ' its dangerous to go alone. Quick, take this ',('clue',share.colors.password),'! ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sun','mountain'))
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sun',(1135,203),scale=0.51,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1154,475),scale=0.51,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(979,536),scale=0.38,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks1','bug',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 100, 180, 200] )
        animation1.addsound( "bug2", [116] )
        #
        self.addpart( draw.obj_music('tower') )


class obj_scene_ch3p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p32())
    def triggernextpage(self,controls):
        return self.world.done# quick skip
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch3_getclue')
        self.text=[\
                   'Alright, now raise your arms and receive the ',('clue',share.colors.password),'. '\
                   ]
        self.world=world.obj_world_getitem(self,item='tower')
        self.addpart(self.world)
        # background
        self.addpart( draw.obj_image('mountain',(1146,405),scale=0.46,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1056,559),scale=0.45,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(119,361),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(1148,226),scale=0.42,rotate=0,fliph=True,flipv=False) )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch3p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p36())
    def setup(self):
        self.text=[\
                 'You have received a ',('clue',share.colors.password),' from ',('{bug}',share.colors.bug),\
                 '! Here it goes... ']
        # background
        self.addpart( draw.obj_image('mountain',(1146,405),scale=0.46,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1056,559),scale=0.45,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(119,361),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(1148,226),scale=0.42,rotate=0,fliph=True,flipv=False) )
        # raise arms
        self.addpart(draw.obj_image('heroarmsfaceup',(620,513),scale=0.69,rotate=0,fliph=False,flipv=False))
        self.addpart(draw.obj_image('tower',(618,230),scale=0.4,rotate=0,fliph=False,flipv=False))
        self.addpart(draw.obj_image('cluesparkles',(618,230),scale=0.7,path='data/premade'))
        animation1=draw.obj_animation('bughovertoright1','bug',(640,360))
        self.addpart( animation1 )

        self.addpart( draw.obj_music('piano') )

class obj_scene_ch3p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p37())
    def setup(self):
        self.text=[\
                 'To unlock the ',('evil tower',share.colors.location2),', ',\
                 'you need to visit three ',('evil grandmasters',share.colors.grandmaster),\
                 ' that used to teach ',('{villainname}',share.colors.villain),'.',\
                 ' Each one will reveal a part of the ',\
                 ('password',share.colors.password),'. ']
        # self.addpart( draw.obj_image('mountain',(1177,324),scale=0.46,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(996,367),scale=0.37,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(74,361),scale=0.34,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('moon',(988,238),scale=0.37,rotate=0,fliph=False,flipv=False) )
        #
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart(draw.obj_image('cluesparkles',(754,418),scale=1,path='data/premade'))
        animation1=draw.obj_animation('ch3_bugtalks1aaa','bug',(340,360))
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade'))
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='data/premade') )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [15, 120, 140])
        # animation1.addsound( "bug2", [116],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch3p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3end())
    def setup(self):
        self.text=[\
                'It will be very scary and dangerous with 99 percent chance to fail but good luck anyways. ']
        # self.addpart( draw.obj_image('mountain',(1177,324),scale=0.46,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(996,367),scale=0.37,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('mountain',(74,361),scale=0.34,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('moon',(988,238),scale=0.37,rotate=0,fliph=False,flipv=False) )
        #
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart(draw.obj_image('cluesparkles',(754,418),scale=1,path='data/premade'))
        animation1=draw.obj_animation('ch3_bugtalks1aaa','bug',(340,360))
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade'))
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='data/premade') )
        # animation2=draw.obj_animation('ch3_bugtalks1aaa','bug',(340,360),record=True)
        # self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        animation1.addsound( "bug1", [45] )
        animation1.addsound( "bug2", [70, 130, 150])
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch3end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3unlocknext())
    def setup(self):
        self.text=[\
                    'A quest! Now thats what im talking about, said the book of things. ',
                   'The tension is killing me, I cant wait to find what happens in the next chapter. ',\
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


class obj_scene_ch3unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3end())
    def setup(self):
        share.datamanager.setbookmark('ch3_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter IV',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=4)# chapter 4 becomes available
        #
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )

###############################################3



#
# class obj_scene_ch3p25a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p25())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p26())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         share.datamanager.setbookmark('ch3_gohome')
#         self.text=['go back home']
#         self.world=world.obj_world_travel(self,start='tower',goal='home',chapter=3)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music(None) )
#
#
# class obj_scene_ch3p26(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p25a())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p29())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"Back at home, ',('{heroname}',share.colors.hero),' was very sad. ',\
#                    ('{hero_he}',share.colors.hero2), ' played a serenade all alone, but it made ',\
#                    ('{hero_him}',share.colors.hero2),' even sader.']
#                    # ('{hero_he}',share.colors.hero2), ' thought about how ',\
#                    # ('{hero_he}',share.colors.hero2),' used to charm ',\
#                    # ('{partnername}',share.colors.partner),' with a serenade." ',\
#         self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )

# skip to shorten text
# class obj_scene_ch3p27(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p26())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p29())
#     def triggernextpage(self,controls):
#         return self.world.done# quick skip
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"Then, ',\
#                    ('{hero_he}',share.colors.hero2),' remembered how ',\
#                    ('{hero_he}',share.colors.hero2),' used to kiss ',\
#                    ('{partnername}',share.colors.partner),'. ',\
#                    'But ',\
#                   ('{heroname}',share.colors.hero),' was only kissing the ',\
#                   ('fish',share.colors.item2),' that ',\
#                   ('{hero_he}',share.colors.hero2),' had caught earlier". ',\
#                    ]
#         # self.world=world.obj_world_kiss(self,noending=True)
#         self.world=world.obj_world_kiss(self,withfish=True,noending=False)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )

#
#
# class obj_scene_ch3p29(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p26())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p30())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                 '"It was already night". ',\
#                    ]
#         self.world=world.obj_world_sunset(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
#
#
# class obj_scene_ch3p30(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p29())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p30a())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"',\
#                    ('{heroname}',share.colors.hero),\
#                    ' went to back to bed sad and lonely, longing for ',('{partnername}',share.colors.partner),'". ',\
#                    ]
#         self.world=world.obj_world_gotobed(self,heroangry=True)
#         self.addpart(self.world)
#         #
        # self.addpart( draw.obj_music('piano') )


# class obj_scene_ch3p38(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p36())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p39())
#     def setup(self):
#         self.text=[\
#                    '"', \
#                    ('{villainname}',share.colors.villain),\
#                    ' has learned ',('{villain_his}',share.colors.villain2),\
#                    ' evil ways from three ',('evil grandmasters',share.colors.grandmaster),'. ',\
#                     'Each of them knows one part of the tower\'s ',\
#                     ('password',share.colors.password),'." ',\
#                    ]
#         #
#         # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade')
#         self.addpart( animation1 )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade') )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='data/premade') )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4') )
#         # animation1.addsound( "villain2", [111],skip=1 )
#         #
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('bug') )
#
# # remove to shorten
# class obj_scene_ch3p39(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p38())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p39a())
#     def soundnextpage(self):
#         pass# no sound
#     def setup(self):
#         self.text=[\
#                    '"If we visit all three ',\
#                    ('evil grandmasters',share.colors.grandmaster),\
#                    ', we will be able to ',\
#                    ('put the password together',share.colors.password),'! ',\
#                    'Tomorrow, I will show you where to go". ',\
#                    ]
#         #
#         self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
#         animation2=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade')
#         self.addpart( animation2 )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='data/premade') )
#         self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='data/premade') )
#
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(340,360))
#         self.addpart( animation1 )
#         #
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         sound1=draw.obj_sound('unlock')
#         self.addpart(sound1)
#         sound1.play()
#         #
#         self.addpart( draw.obj_music('bug') )




#
# class obj_scene_ch3p36a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p36())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p40())
#     def setup(self):
#         share.datamanager.setbookmark('ch3_endbug')
#         self.text=[\
#                    '"We will start tomorrow after some sleep, said the ',('{bug}',share.colors.bug),\
#                    ', I dont work overtime. And it crawled back in ',('{heroname}',share.colors.hero),'\'s pocket." ',\
#                    ]
#         self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
#         self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )
#         animation1=draw.obj_animation('ch1_awaken','herobase',(640,360),scale=0.7)
#         self.addpart(animation1)
#         #
#         self.sound=draw.obj_sound('bookscene')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('tension') )

#
# class obj_scene_ch3p40(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3p39())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch3end())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"',\
#                    ('{heroname}',share.colors.hero),\
#                    ' went back to bed a little happier, for tomorrow ',\
#                    ('{hero_he}',share.colors.hero2),' may be able to rescue ',\
#                    ('{partnername}',share.colors.partner),'".',\
#                    ]
#         self.world=world.obj_world_gotobed(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
