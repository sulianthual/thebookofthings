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
        share.scenemanager.switchscene(obj_scene_ch4p0())
    def triggernextpage(self,controls):
        return True


class obj_scene_ch4p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def setup(self):
        self.text=['-----   Chapter IV: Something East   -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: well, lets continue our story where we left. ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)

class obj_scene_ch4p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def setup(self):
        self.text=[\
                  '"',
                   ('{partnername}',share.colors.partner),' has been captured by the ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),', and ',\
                     ('{partner_he}',share.colors.partner),' is being held in  ',\
                     ('{villain_his}',share.colors.villain),' ',\
                     ('evil castle',share.colors.location),'. ',\
                     ('{heroname}',share.colors.hero),' is trying to figure out the castle\'s ',\
                     ('password',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        self.addpart( draw.obj_image('castle',(1156,312),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(981,265),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(866,243),scale=0.23,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch4_villaincapture1','villainbase',(640,360),record=False)
        animation1.addimage('villainholdspartner')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_villaincapture2','partnerbase',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        # self.addpart( draw.obj_imageplacer(self,'castle','mountain') )
    def presetup(self):
        super().presetup()
        # villainbase+partnerbase=villainholdspartner
        image1=draw.obj_image('villainbase',(640,360))
        image2=draw.obj_image('partnerbase',(640-70,360+80),rotate=90)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,400,330),'villainholdspartner')

class obj_scene_ch4p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2a())
    def setup(self):
        self.text=[\
                  '"Luckily, ',('{heroname}',share.colors.hero),\
                   ' befriended a terrifying ',('{bug}',share.colors.bug),\
                    ' who may know how to crack the castle\'s ',('password',share.colors.item),'. ',\
                    'Today, they are on their way to meet the ',\
                    ('Grandmaster of Deceit',share.colors.villain),\
                    ' that lives in the east."',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch4p2a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        self.text=[\
                   'First, lets make sure ',('{heroname}',share.colors.hero),' wakes up on time for ', \
                   ('{hero_his}',share.colors.hero),' adventure, said the book of things.',\
                   'Draw a ',('night stand',share.colors.item),\
                   ' and an ',('alarm clock',share.colors.item),\
                   ' to wake ',('{hero_him}',share.colors.hero),'. ',\
                   ]
        self.addpart( draw.obj_drawing('nightstand',(200+50,450),legend='Night Stand',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('alarmclockext',(940,450),legend='Alarm Clock (draw the exterior)',shadow=(200,200)) )
        self.addpart( draw.obj_image('alarmclockfill',(940,450),path='premade') )
        self.addpart( draw.obj_image('alarmclockcenter8am',(940,450),path='premade') )
    def endpage(self):
        super().endpage()
        # combine alarmclockext+alarmclockfill=alarmclock (no hour shown)
        image1=draw.obj_image('alarmclockext',(640,360))
        image2=draw.obj_image('alarmclockfill',(640,360),path='premade')
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,200),'alarmclock')
        # combine alarmclock+alarmclockcenter8am=alarmclock8am (morning)
        image1=draw.obj_image('alarmclock',(640,360))
        image2=draw.obj_image('alarmclockcenter8am',(640,360),path='premade')
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,200),'alarmclock8am')
        # combine alarmclock+alarmclockcenter8am=alarmclock8am (night)
        image1=draw.obj_image('alarmclock',(640,360))
        image2=draw.obj_image('alarmclockcenter12am',(640,360),path='premade')
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,200),'alarmclock12am')

class obj_scene_ch4p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               'Alright lets go, said the book of things: ',\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' that lived in a house. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch4p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from bed with ',\
                ('{hero_his}',share.colors.hero),\
                ' new friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=True)
        self.addpart(self.world)
        # self.addpart( draw.obj_image('bed',(440,500),scale=0.75) )
        # self.addpart( draw.obj_textbox('Hold [D] to Wake up',(1100,480),color=share.colors.instructions) )
        # animation1=draw.obj_animation('ch1_heroawakes','herobase',(640,360),scale=0.7)
        # self.addpart(animation1)
        # animation2=draw.obj_animation('ch4_heroawakesbug','bug',(640,360),record=False,sync=animation1)
        # animation2.addimage('empty',path='premade')
        # self.addpart(animation2)
        # self.addpart( draw.obj_imageplacer(self,'bug') )
        # self.addpart( draw.obj_image('bug',(1168,595),scale=0.33,rotate=0,fliph=False,flipv=False) )

class obj_scene_ch4p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked his ',\
                    ('{hero_his}',share.colors.hero),' mailbox. ',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'a ',' letter". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(163,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nWasup. Last time I checked, ',('{partnername}',share.colors.partner),\
                    ' is still being held hostage in my ',\
                     ('evil lair',share.colors.location),'. Come save ',\
                     ('{partner_him}',share.colors.partner),' if you dare. ',\
                     'Whenever. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch4p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                   ' Alright, today we need to head east and meet the first ',\
                   ('Grandmaster of Deceit',share.colors.villain),'. ',\
                    'From what I heard in ',('{villainname}',share.colors.villain),\
                    '\'s sleep, this grandmaster ',\
                    'holds the first clue to the evil castle\'s ',\
                    ('password',share.colors.item),'". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )

class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def setup(self):
        self.text=['This grandmaster lives in a magical cave in a dark forest,',\
                    ' said the book of things. ',\
                    'Draw a ',('cave',share.colors.item),\
                    ' and a ',('tree',share.colors.item),' and we will be on our way. ',\
                   ]
        self.addpart( draw.obj_drawing('cave',(340,450),legend='Cave',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('tree',(940,450),legend='Tree',shadow=(200,200)) )

class obj_scene_ch4p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'Moving on: "',\
                ('{heroname}',share.colors.hero),' travelled to the ',\
                ('magical cave',share.colors.location),' in the east". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='forest',chapter=4)
        self.addpart(self.world)

class obj_scene_ch4p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def setup(self):
        self.text=[\
                '"Arrived at the ',('magical cave',share.colors.location),', ',\
                ('{heroname}',share.colors.hero),' met a curious character. ',\
                'It was an extremely cute ',('bunny',share.colors.bunny),'". ',\
                'Well, there\'s never ever been anything wrong with that, ',\
                'said the book of things. ',\
                'Go on, draw the ',('bunny',share.colors.bunny),'\'s head. ',\
                   ]
        self.textkeys={'pos':(50,200),'xmax':720}
        self.addpart( draw.obj_image('stickhead',(980,360+150-10),path='premade',scale=1.5) )
        self.addpart( draw.obj_drawing('bunnyface',(980,360-10),legend='Bunny Head (facing right)',shadow=(200,300)) )
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybase') )
        # self.addpart( draw.obj_image('herobase',(165-50,571),scale=0.37,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(359-50,498),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(665-50,651),scale=0.35,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('cave',(540-50,473),scale=0.57,rotate=0,fliph=False,flipv=False) )
    def endpage(self):
        super().endpage()
        # save bunny head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360+150),scale=1.5,path='premade'))
        dispgroup1.addpart('part2',draw.obj_image('bunnyface',(640,360)))
        dispgroup1.snapshot((640,360,200,300),'bunnyhead')

class obj_scene_ch4p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def setup(self):
        self.text=[\
                'Great. Now draw the ',('bunny',share.colors.bunny),'\'s body, said the book of things. ',\
                'Remember to make it very cute! ',\
                'And finish by naming it. ',\
                   ]
        self.textkeys={'pos':(50,100),'xmax':720}
        self.addpart( draw.obj_drawing('bunnybody',(980,360+65),legend='Bunny body (facing right)',shadow=(200,105),brush=share.brushes.pen6) )
        self.addpart( draw.obj_image('bunnyhead',(980,360-150),scale=0.5) )
        self.addpart( draw.obj_textinput('bunnyname',25,(380,360),color=share.colors.bunny, legend='Bunny Name') )
    def endpage(self):
        super().endpage()
        # save angry head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('bunnybody',(640,360+65)))
        dispgroup1.addpart('part2',draw.obj_image('bunnyhead',(640,360-150),scale=0.5))
        dispgroup1.snapshot((640,295,200,235),'bunnybase')

class obj_scene_ch4p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def setup(self):
        self.text=[\
                'Lets move on, said the book of things. ',\
                '"',('{heroname}',share.colors.hero),\
                ' met a ',('bunny',share.colors.bunny),' called ',\
                ('{bunnyname}',share.colors.bunny),\
                ' at the ',('magical cave',share.colors.location),'. ',\
                ('{heroname}',share.colors.hero),' said: ',\
                ' wow, you are so cute, can I pet you". ',\
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

class obj_scene_ch4p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def setup(self):
        self.text=[\
                '"Ha! You think I am cute!, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'Well, look carefully at all these trees. Poof, they are all gone! ',\
                'I just chopped them with my ',('little paw',share.colors.bunny),'. ',\
                'Do you still want to pet me now". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bunnybase',(867,525),scale=0.62,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('tree',(618,439),scale=1.28,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_bunnyeats1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_bunnyeats2','tree',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        animation2.addimage('poof',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch4_bunnyeats3','tree',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        animation3.addimage('poof',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_bunnyeats4','tree',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='premade')
        animation4.addimage('poof',path='premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch4_bunnyeats5','tree',(640,360),record=False,sync=animation1)
        animation5.addimage('empty',path='premade')
        animation5.addimage('poof',path='premade')
        self.addpart( animation5 )




class obj_scene_ch4p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def setup(self):
        self.text=[\
                '"Hahaha, said the ',('bunny',share.colors.bunny),'. ',\
                'Do not underestimate me. ',\
                'I am ',('{bunnyname}',share.colors.bunny),\
                ', the ',('grandmaster of deceit',share.colors.villain),\
                ' from the east! ',\
                'Tremble before me". ',\
                   ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch4p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def setup(self):
        self.text=[\
                '"Well, I also teach some great evil ways, said ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                'Tell you what, if you manage to win my ',('lying game',share.colors.villain),\
                ' you can ask me anything". ',\
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

class obj_scene_ch4p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingstart())
    def setup(self):
        self.text=[\
                '"The ',('{bug}',share.colors.bug),\
                ' crawled out of ',('{heroname}',share.colors.hero),\
                '\'s pocket and whispered: ',\
                'I think we are onto something, lets win this ',\
                ('lying game',share.colors.villain),' then ask for the evil lair\'s ',\
                ('password',share.colors.item),'". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


#############
# Lying game
# *LYING
# NB: ONE CANNOT QUICK ACCESS THE MIDDLE/END OF THE GAME, BECAUSE THEN TEMP DATA IS NOT LOADED
class obj_scene_lyingstart(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingdatabase())
    def setup(self):
        self.text=[\
                '"Alright, said ',\
                ('{bunnyname}',share.colors.bunny),'. ',\
                'here is how the ',('lying game',share.colors.villain),\
                ' works. It is all about having a good memory and mastering the ',\
                ('art of lying',share.colors.villain),'". ',\
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


class obj_scene_lyingdatabase(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def triggernextpage(self,controls):
        return True
    def setup(self):
        # Statements Database
        self.statements={}# marked with key, statement negative (0), statement positive (1)
        self.statements['apple']=['I hate apples','I love apples']
        self.statements['banana']=['I hate bananas','I love bananas']
        self.statements['shower']=['I never shower','I always shower']
        self.statements['teeth']=['I never brush my teeth','I always brush my teeth']
        self.statements['spider']=['I am not scared of spiders','I am scared of spiders']
        self.statements['booger']=['I dont eat my boogers','I eat my boogers']
        #
        ########################################
        # Save the database in datamanger temp object
        share.datamanager.temp.statements=self.statements# full database


class obj_scene_lyingpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingstart())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingrule())
    def setup(self):
        # Pick up statements from large database
        self.statements=share.datamanager.temp.statements# full database
        self.statkeys=[]# choose 3 keys for statements (must be unique)
        self.statkeys=tool.randsample( list(self.statements)  , 3)
        self.stat01=[]# for each key, select the True or False statement (0,1)
        for i in range(3):
            self.stat01.append(tool.randchoice([0,1]))
        self.statdict={}
        for i in range(3):
            self.statdict[self.statkeys[i]]=self.stat01[i]
        # Save in the datamanager.temp:
        share.datamanager.temp.statdict=self.statdict# compact dict of subset
        share.datamanager.temp.statkeys=self.statkeys# keys of subset
        share.datamanager.temp.stat01=self.stat01# bool of subset
        share.datamanager.temp.fqstatdict={}# former questions asked (for later)
        # Page Text
        self.text=[\
                    'This game plays in three rounds. For the first round, ',\
                    'here are three ',\
                    ('correct statements',share.colors.darkgreen),' you need to remember. ',\
                    'You can even take some notes at the bottom of the screen to help your memory. '
                   ]
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][self.stat01[0]],(400,220),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][self.stat01[1]],(400,290),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][self.stat01[2]],(400,360),xleft=True,color=share.colors.darkgreen  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        drawing.clear()# erase drawing
        self.addpart( drawing )
        # self.addpart( draw.obj_imageplacer(self,'bunnyhead') )
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )


class obj_scene_lyingrule(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q1())
    def setup(self):
        # load from data manager
        self.statements=share.datamanager.temp.statements
        self.statdict=share.datamanager.temp.statdict
        self.statkeys=share.datamanager.temp.statkeys
        self.stat01=share.datamanager.temp.stat01
        fqstatdict=share.datamanager.temp.fqstatdict# former question asked
        ###################
        self.text=[\
                    'Remember this too: ',\
                    # '"to be ',('correct',share.colors.darkgreen),\
                    # ', a statement must be ',('entirely correct',share.colors.darkgreen),'. ',\
                    # ' A statement that is ',(' partly correct',share.colors.darkgreen),\
                    # ' and ',(' partly wrong',share.colors.red),\
                    # ' is ',('wrong',share.colors.red),'". ',\
                    '"to be correct, a statement must be entirely correct. ',\
                    ' A statement that is partly correct and partly wrong is wrong". ',\
                    'For example: ',\
                    '\n\n ',\
                    '"',(self.statements[self.statkeys[0]][self.stat01[0]],share.colors.darkgreen),\
                    (' and ',share.colors.item),\
                    (self.statements[self.statkeys[1]][self.stat01[1]],share.colors.darkgreen),\
                    '": this is ',('correct',share.colors.darkgreen),'. ',\
                    '\n "',(self.statements[self.statkeys[0]][self.stat01[0]],share.colors.darkgreen),\
                    (' and ',share.colors.item),\
                    (self.statements[self.statkeys[1]][1-self.stat01[1]],share.colors.red),\
                    '": this is ',('wrong',share.colors.red),'. ',\
                   ]

        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        self.addpart( drawing )
        # self.addpart( draw.obj_imageplacer(self,'bunnyhead') )
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )


class obj_scene_lyingfailpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def setup(self):
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    ' You gave me the wrong answer. ',\
                    'If your memory is that bad you can always ',\
                    ('take some notes',share.colors.darkgreen),' at the bottom of the screen. ',\
                    'Now go back and win this first round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_lyingp1q1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        if self.nextpage_correctanswer():# custom correct answer function
            self.nextpage_lyinggame()# custom progression function
        else:
            self.nextpage_lyingfail()# custom progression function
    def nextpage_correctanswer(self):
        if share.devmode:
            return True
        else:
            return share.datamanager.getword('choice_yesno')==share.datamanager.getword('truth_yesno')
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q2())
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart1())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (1/3):   ']
    def setup(self):
        # load from data manager
        self.statements=share.datamanager.temp.statements
        self.statdict=share.datamanager.temp.statdict
        self.statkeys=share.datamanager.temp.statkeys
        self.stat01=share.datamanager.temp.stat01
        fqstatdict=share.datamanager.temp.fqstatdict# former question asked
        # random question (must be different form previous one)
        qstatkeys=tool.randsample( list(self.statkeys)  , 2)# choose two statements
        qstat01=[]
        for i in range(2):
            qstat01.append(tool.randchoice([0,1]))
        qstatdict={}
        for i in range(2):
            qstatdict[qstatkeys[i]]=qstat01[i]
        if fqstatdict.items() == qstatdict.items():# if same as last question, change it slightly
            qstat01[1]=1-qstat01[1]# swap 0 1
            qstatdict[qstatkeys[1]]=qstat01[1]
        share.datamanager.temp.fqstatdict=qstatdict# save question asked for later
        # Correct answer
        if qstatdict.items() <= self.statdict.items():# dictionary is subset of larger one
            share.datamanager.setword('truth_yesno','yes')
        else:
            share.datamanager.setword('truth_yesno','no')
        # Page text
        self.text=self.text_lyinggame()# from function
        #
        y1=190
        self.addpart( draw.obj_textbox( '" '+self.statements[qstatkeys[0]][qstat01[0]],(640-40,y1),xright=True ) )
        self.addpart( draw.obj_textbox( ' and ',(640,y1),color=share.colors.item ) )
        self.addpart( draw.obj_textbox( self.statements[qstatkeys[1]][qstat01[1]]+' "',(640+40,y1),xleft=True ) )
        #
        y2=310
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Yes','yes',(640-100,y2))
        textchoice.addchoice('No','no',(640+100,y2))
        self.addpart( textchoice )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Use your notes',brush=share.brushes.smallpen)
        self.addpart( drawing )
        # self.addpart( draw.obj_image('lyingnote',(640,530)) )
        # self.addpart( draw.obj_textbox( 'Use your notes',(640,685),color=share.colors.instructions  ) )
        # self.addpart( draw.obj_rectangle((640,530),500,120,color=(0,0,0)) )
        # if share.devmode:# check correct answer
        if False:
            print('###')
            print('truth='+ str(self.statdict))
            print('statment='+ str(qstatdict))
            print('answer='+ str(self.nextpage_correctanswer()))
        # page animation
        animation1=draw.obj_animation('ch3_bunnheadwobble','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bunnheadwobble2','herohead',(640,360),record=False, sync=animation1) )



class obj_scene_lyingp1q2(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q3())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (2/3):   ']

class obj_scene_lyingp1q3(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1win())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (3/3):   ']

class obj_scene_lyingpart1win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won the ',\
                    ('first round',share.colors.villain),'! ',\
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

class obj_scene_lyingpart2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1win())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q1())
    def setup(self):
        # Pick up statements from large database
        self.statements=share.datamanager.temp.statements# full database
        self.statkeys=[]# choose 3 keys for statements (must be unique)
        self.statkeys=tool.randsample( list(self.statements)  , 3)
        self.stat01=[]# for each key, select the True or False statement (0,1)
        for i in range(3):
            self.stat01.append(tool.randchoice([0,1]))
        self.statdict={}
        for i in range(3):
            self.statdict[self.statkeys[i]]=self.stat01[i]
        # Save in the datamanager.temp:
        share.datamanager.temp.statdict=self.statdict# compact dict of subset
        share.datamanager.temp.statkeys=self.statkeys# keys of subset
        share.datamanager.temp.stat01=self.stat01# bool of subset
        share.datamanager.temp.fqstatdict={}# former questions asked (for later)
        # Page Text
        self.text=['For the second round, ',('I will now be lying',share.colors.red),'. ',\
                    ' Here are three ',\
                    ('wrong statements',share.colors.red),' to remember. ',\
                    'Once again, you can take some notes to help your memory. '
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][1-self.stat01[0]],(400,220),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][1-self.stat01[1]],(400,290),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][1-self.stat01[2]],(400,360),xleft=True,color=share.colors.red  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        drawing.clear()# erase drawing
        self.addpart( drawing )
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )

class obj_scene_lyingfailpart2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    ' You gave me the wrong answer. ',\
                    'For this second round, remember that ',\
                    ('all my statements are wrong',share.colors.red),'. ',\
                    'And I may suggest that you take some notes ',\
                    'at the bottom of the screen. ',\
                    'Now go back and win this second round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_lyingp2q1(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q2())
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart2())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (1/3):   ']


class obj_scene_lyingp2q2(obj_scene_lyingp2q1):# child of lying 2
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q3())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (2/3):   ']

class obj_scene_lyingp2q3(obj_scene_lyingp2q1):# child of lying 2
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2win())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following statement is ',('Correct',share.colors.darkgreen),' (3/3):   ']

class obj_scene_lyingpart2win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won the ',\
                    ('second round',share.colors.villain),'! ',\
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

class obj_scene_lyingpart3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2win())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q1())
    def setup(self):
        # Pick up statements from large database
        self.statements=share.datamanager.temp.statements# full database
        self.statkeys=[]# choose 3 keys for statements (must be unique)
        self.statkeys=tool.randsample( list(self.statements)  , 3)
        self.stat01=[]# for each key, select the True or False statement (0,1)
        for i in range(3):
            self.stat01.append(tool.randchoice([0,1]))
        self.statdict={}
        for i in range(3):
            self.statdict[self.statkeys[i]]=self.stat01[i]
        # Save in the datamanager.temp:
        share.datamanager.temp.statdict=self.statdict# compact dict of subset
        share.datamanager.temp.statkeys=self.statkeys# keys of subset
        share.datamanager.temp.stat01=self.stat01# bool of subset
        share.datamanager.temp.fqstatdict={}# former questions asked (for later)
        # Page Text
        self.text=['For the last round, ',('I will be lying and so will you',share.colors.red),'! ',\
                    'Remember these three ',\
                    ('wrong statements',share.colors.red),'. ',\
                    'But then, when answering my questions, always give me the ',\
                    ('wrong answer',share.colors.red),'. ',\
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][1-self.stat01[0]],(400,220),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][1-self.stat01[1]],(400,290),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][1-self.stat01[2]],(400,360),xleft=True,color=share.colors.red  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
        drawing.clear()# erase drawing
        self.addpart( drawing )
        self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )

class obj_scene_lyingfailpart3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),'. ',\
                    ' You gave me the wrong answer. ',\
                    'For this third round, remember that ',\
                    ('all my statements are wrong',share.colors.red),'. ',\
                    'Then, remember to ',\
                    ('always give me the wrong answer',share.colors.red),'. ',\
                    'I may also suggest that you take some notes ',\
                    'at the bottom of the screen. ',\
                    'Now go back and win this third round, I know you can do it! ',\
                                ]
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_lyingp3q1(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q2())
    def nextpage_correctanswer(self):# must give wrong answer
        if share.devmode:
            return True
        else:
            return share.datamanager.getword('choice_yesno') != share.datamanager.getword('truth_yesno')
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart3())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following is "correct" ',\
                    '(but ',\
                    ('lie',share.colors.red),' and give me the ',\
                    ('wrong answer',share.colors.red),') (1/3): ',\
                    ]


class obj_scene_lyingp3q2(obj_scene_lyingp3q1):# child of lying 3
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q3())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following is "correct" ',\
                    '(but ',\
                    ('lie',share.colors.red),' and give me the ',\
                    ('wrong answer',share.colors.red),') (2/3): ',\
                    ]

class obj_scene_lyingp3q3(obj_scene_lyingp3q1):# child of lying 3
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingend())
    def text_lyinggame(self):# question count (1/3, 2/3, 3/3)
        return ['Now tell me if the following is "correct" ',\
                    '(but ',\
                    ('lie',share.colors.red),' and give me the ',\
                    ('wrong answer',share.colors.red),') (3/3): ',\
                    ]

class obj_scene_lyingend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def setup(self):
        self.text=[\
                    'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
                    'you won my ',('lying game',share.colors.villain),'! ',\
                    ' You are truly a ',\
                    ('great deceiver',share.colors.villain),' that can ',\
                    ('lie',share.colors.villain),' like no equal. ',\
                    'Now ask me anything".',\
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


class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingend())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def setup(self):
        self.text=[\
                    '"Oh, you want to know the  ',('password',share.colors.item),\
                    ' of ',('{villainname}',share.colors.villain),'\'s ',\
                    ('castle',share.colors.location),'. ',\
                    'Well sorry, I dont really know. ',\
                    ('{villainname}',share.colors.villain),' was a former student of mine, ',\
                    'a bit mediocre but quite dedicated". ',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny3inter','interrogationmark',(640,360),record=False,sync=animation2,path='premade')
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )


class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19a())
    def setup(self):
        self.text=[\
                    '"I guess if the ',('password',share.colors.item),\
                    ' is related to me, then it must be ',('"bunny"',share.colors.item),'. ',\
                    'That\'s how smart ',\
                    ('{villainname}',share.colors.villain),' is, for real. Well, goodbye now". ',\
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
        animation3=draw.obj_animation('ch4_herowalkbunny3inter','interrogationmark',(640,360),record=False,sync=animation2,path='premade')
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )


class obj_scene_ch4p19a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())

    def setup(self):
        self.text=[\
                '"The ',('{bug}',share.colors.bug),\
                ' crawled out of ',('{heroname}',share.colors.hero),\
                '\'s pocket and whispered: ',\
                'Well done, ',('{heroname}',share.colors.hero),'. ',\
                'Now that we know the first part of the ',('password',share.colors.item),\
                ', we can return home. ',\
                'Tomorrow, we will visit the second ',\
                ('grandmaster of Deceit',share.colors.villain),\
                ', and very soon we will be able to rescue ',\
                ('{partnername}',share.colors.partner),'". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch4p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' travelled back ',
                ('home',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='forest',goal='home',chapter=4)
        self.addpart(self.world)



class obj_scene_ch4p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p22())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"Back at home, ',\
                   ('{heroname}',share.colors.hero),' was sad again. ',\
                   ('{hero_he}',share.colors.hero), ' though about how ',\
                   ('{hero_he}',share.colors.hero),' used to charm ',\
                   ('{partnername}',share.colors.partner),' with a serenade. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
        self.addpart(self.world)

class obj_scene_ch4p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p23())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"Then, ',\
                   ('{heroname}',share.colors.hero),' remembered how ',\
                   ('{hero_him}',share.colors.hero),' and ',\
                   ('{partnername}',share.colors.partner),' used to kiss". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=True)
        self.addpart(self.world)


class obj_scene_ch4p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p24())
    def setup(self):
        self.text=[\
                   '"But ',\
                   ('{partnername}',share.colors.partner),' wasnt there, and ',\
                   ('{heroname}',share.colors.hero),' was only kissing the ',\
                   ('{bug}',share.colors.bug),' that had crawled out of ',\
                   ('{hero_his}',share.colors.hero),' pocket". ',\
                   ]

        # self.addpart( draw.obj_image('partnerbase',(710,390),scale=0.7,rotate=15) )
        # self.addpart( draw.obj_image('fish',(785,467),scale=0.84,rotate=-68,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bug',(730,440),scale=0.5,rotate=30,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobaseangry',(580,400),scale=0.7,rotate=-15) )
        # self.addpart( draw.obj_imageplacer(self,'fish','bug'))
        self.addpart( draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4) )
        self.addpart( draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4) )


class obj_scene_ch4p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p25())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"In the evening, ',\
                    ('{heroname}',share.colors.hero),\
                    ' ate the ',\
                    ('fish',share.colors.item),' that ',\
                    ('{hero_he}',share.colors.hero),' had caught in the pond".',\
                   ]
        self.world=world.obj_world_eatfish(self,heroangry=True)
        self.addpart(self.world)

class obj_scene_ch4p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p26())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)

class obj_scene_ch4p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p27())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,heroangry=True,bug=True)
        self.addpart(self.world)

class obj_scene_ch4p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        self.text=[\
                   '"Then, right before falling asleep, ',\
                   ('{heroname}',share.colors.hero),' smiled thinking about how ',\
                   ('{hero_he}',share.colors.hero),' might be able to rescue ',\
                   ('{partnername}',share.colors.partner),' the next day".',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )


class obj_scene_ch4end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=[\
                    'And thats all for today, said the book of things. ',
                   'The tension is killing me. I cant wait to find what happens tomorrow! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter V',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available
#





####################################################################################
####################################################################################
