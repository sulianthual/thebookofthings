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

# Chapter VI: ...
# *CHAPTER VI

class obj_scene_chapter4(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p0())
    def setup(self):
        self.text=['-----   Chapter III: Higher and Higher   -----   ',\
                   '\n In this chapter introduce the first part of quest (elder on mountain). ',\
                  '\n put back text dialogue where learn to cheat ',\
                  '\n add minigame (like training) ',\
                  '\n add requirements to bring more food to elder ',\
                   ]

class obj_scene_ch4p0(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def setup(self):
        self.text=['-----   Chapter IV: Higher and Higher  -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: lets see how our story is going so far. ',\
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
        share.scenemanager.switchscene(obj_scene_ch4p1a())
    def setup(self):
        self.text=[\
                  '"',
                   ('{partnername}',share.colors.partner),' has been captured by the ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),'. ',\
                     ('{partner_he}',share.colors.partner),' is being held in  ',\
                     ('{villain_his}',share.colors.villain),' ',\
                     ('evil lair',share.colors.location),'. ',\
                     ('{heroname}',share.colors.hero),' is on a quest to find a way in. ',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch3_villaincapture','villainbase',(640,360),record=False,scale=0.7)
        animation2=draw.obj_animation('ch3_villaincapture2','partnerbase',(640,360),record=False,sync=animation1,scale=0.7)
        self.addpart( animation1 )
        self.addpart( animation2 )


class obj_scene_ch4p1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1b())
    def setup(self):
        self.text=[\
                   'First, lets make sure ',('{heroname}',share.colors.hero),' wakes up on time for ', \
                   ('{hero_his}',share.colors.hero),' quest, said the book of things.',\
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
        # combine alarmclock+alarmclockcenter8am=alarmclock8am
        image1=draw.obj_image('alarmclock',(640,360))
        image2=draw.obj_image('alarmclockcenter8am',(640,360),path='premade')
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,200),'alarmclock8am')

class obj_scene_ch4p1b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1c())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'Ok here we go, lets write: "It was the next day and the sun was rising".',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch4p1c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1d())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' woke up, but ',\
                ('{partnername}',share.colors.partner),' wasnt there. ',\
                   ]
        self.world=world.obj_world_wakeup(self,heroangry=True,sun=True,alarmclock=True)
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # combine stickhead+angryface+stickbody = herobaseangry
        image1=draw.obj_image('stickbody',(640,460),path='premade')# snapshot
        image2=draw.obj_image('stickhead',(640,200),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,300),'herobaseangry')


class obj_scene_ch4p1d(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1e())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)

class obj_scene_ch4p1e(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1d())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1f())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',\
                    ('{hero_he}',share.colors.hero),' ate the ',
                    ('fish',share.colors.item),' for breakfast, but the heart wasnt there." ',\
                   ]
        self.world=world.obj_world_eatfish(self,heroangry=True)
        self.addpart(self.world)



class obj_scene_ch4p1f(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1e())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1g())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox.',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'a ',' letter". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobaseangry',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_ch4p1g(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1f())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1h())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(163,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nWasup. ',('{partnername}',share.colors.partner),\
                    ' is still being held hostage in my . ',\
                     ('evil lair',share.colors.location),', so come save ',\
                     ('{partner_him}',share.colors.partner),' if you dare. ',\
                     ' Take your time. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))




class obj_scene_ch4p1h(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1g())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1i())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox again.',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'another ',' letter". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobaseangry',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )



class obj_scene_ch4p1i(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1h())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(163+30,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',\
                    ('[Current resident at the House with Trees]',share.colors.hero),', ',\
                      '\nCome see me for your quest at the ',\
                    ('highest peak',share.colors.location),'. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('interrogationmark',(1065,305),path='premade',scale=1.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))



class obj_scene_ch4p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1i())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        self.text=[\
                   'Today, ',\
                  ('{heroname}',share.colors.hero),' must go to the ',('Highest Peak',share.colors.location),'. ',\
                  ' It is so high up in the sky it is always covered by stormy clouds. ',\
                  'Draw a ',('cloud',share.colors.item),' and a ',\
                  ('lightning bolt',share.colors.hero),'. ',\
                   ]
        self.addpart( draw.obj_drawing('cloud',(340,450),legend='Cloud',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('lightningbolt',(940,450),legend='Lightning Bolt',shadow=(200,200)) )


class obj_scene_ch4p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Great, now lets write: "',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('highest peak',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='peak',chapter=5)
        self.addpart(self.world)



class obj_scene_ch4p3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3b())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                ' climbed the ',('highest peak',share.colors.location),'".',\
                   ]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)


class obj_scene_ch4p3b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def setup(self):
        self.text=[\
                '" When ',('{heroname}',share.colors.hero),\
                ' reached the top of ',('highest peak',share.colors.location),\
                ', he encountered a mysterious character.',\
                'It was an ',('elder',share.colors.elder),'".',\
               'Fascinating, said the book of things. ',\
                'Choose a name and gender for this ',\
                ('elder',share.colors.elder),'. ',\
                   ]
        y1=360+90-100
        y2=520+100-100
        self.addpart( draw.obj_textbox('The Elder was:',(180,y1)) )
        textchoice=draw.obj_textchoice('elder_he')
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('elder_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('elder_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the Elder\'s Name was:",(200,y2)) )
        self.addpart( draw.obj_textinput('eldername',25,(750,y2),color=share.colors.hero, legend='Elder Name') )



class obj_scene_ch4p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def setup(self):
        self.text=[\
               'Now draw the ',\
               ('elder',share.colors.elder),'\'s face, and make it look slightly to the right. ',\
                'I suggest you draw a happy face and add some wrinkles and maybe a beard, ',\
                'but that is entirely up to you. ',\
                   ]
        self.addpart( draw.obj_drawing('elderhead',(640,450),legend='Draw the Elder') )
    def endpage(self):
        super().endpage()
        # save elder full body
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'elderbase')



class obj_scene_ch4p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def setup(self):
        self.text=[\
               'Lets continue, say the book of things: ',\
               '"At the top of the ',('highest peak',share.colors.location),', above the clouds, ',\
               ('{heroname}',share.colors.hero),' met the ',('elder',share.colors.elder),' called ',\
               ('{eldername}',share.colors.elder),'. ',\
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
        self.addpart( draw.obj_animation('ch5_meetelder2','sun',(640,360),record=True,sync=animation1) )
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','cloud','sun','mountain') ) )



class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def setup(self):
        self.text=[\
                '"He said: my name is ',('{eldername}',share.colors.elder),\
               'and I may grant you useful teachings for your quest". ',\
               'All you have to do is win a game of ',('rock-paper-scissors',share.colors.item),\
               ', hi hi hi". ',\
               'Well, that sounds rather easy, said the book of things. Just draw each ',\
               ('item',share.colors.item),'. ',\
                  ]
        self.addpart( draw.obj_drawing('rock',(200+20,450),legend='Large Rock',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('paper',(640,450),legend='Piece of Paper',shadow=(200,200),brush=share.brushes.pen) )
        self.addpart( draw.obj_drawing('scissors',(1280-200-20,450),legend='Scissors',shadow=(200,200),brush=share.brushes.pen) )




class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def setup(self):
        self.text=[\
               '"Alright, said ',('{eldername}',share.colors.elder),', this is how it works. ',\
               'This ',('bubble',share.colors.instructions),\
               ' above your head shows what you are thinking about. ',\
               'Select rock, paper or scissors with [A][W][D]". ',\
                  ]
        self.dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup1.addpart( 'floor', draw.obj_image('floor5',(640,720-100),path='premade') )
        self.dispgroup1.addpart( 'hero', draw.obj_image('herobase',(640-240,530),scale=0.5,) )
        self.dispgroup1.addpart( 'elder', draw.obj_image('elderbase',(640+240,530),scale=0.5,fliph=True) )
        self.dispgroup1.addpart( 'texta', draw.obj_textbox('[A]: rock',(640-80,530+50),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'textw', draw.obj_textbox('[W]: paper',(640,530),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'textd', draw.obj_textbox('[D]: scissors',(640+90,530+50),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'thinkcloud', draw.obj_image('thinkcloud',(200,320),path='premade') )
        self.dispgroup1.addpart( 'rock', draw.obj_image('rock',(100+50,320),scale=0.5) )
        self.dispgroup1.addpart( 'paper', draw.obj_image('paper',(100+50,320),scale=0.5) )
        self.dispgroup1.addpart( 'scissors', draw.obj_image('scissors',(100+50,320),scale=0.5) )
        self.addpart(self.dispgroup1)
        self.herochoice=0
        self.dispgroup1.dict['rock'].show=self.herochoice==0
        self.dispgroup1.dict['paper'].show=self.herochoice==1
        self.dispgroup1.dict['scissors'].show=self.herochoice==2
        # self.addpart(draw.obj_drawing('floor5',(640,720-100),shadow=(500,100),brush=share.brushes.smallpen))
        # self.addpart(draw.obj_imageplacer(self,'show3'))
        self.addpart( draw.obj_image('show3',(418,246),path='premade') )
        #
        # self.addpart( draw.obj_imageplacer(self,'cloud','sun','mountain') )
        self.addpart( draw.obj_image('sun',(1120,285),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1212,666),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1096,627),scale=0.24,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1207,536),scale=0.29,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(80,651),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(198,621),scale=0.22,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(118,564),scale=0.2,rotate=0,fliph=True,flipv=False) )
    def page(self,controls):
        super().page(controls)
        if controls.a and controls.ac:
            self.herochoice=0
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2
        elif controls.w and controls.wc:
            self.herochoice=1
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2
        elif controls.d and controls.dc:
            self.herochoice=2
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2

class obj_scene_ch4p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp18())
    def setup(self):
        self.text=[\
               '"This is your health and mine. If you loose a round, you loose a ',\
               ('heart',share.colors.partner),'. The first one that runs out of ',\
               ('hearts',share.colors.partner),' looses the game. '
                  ]
        self.dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup1.addpart( 'floor', draw.obj_image('floor5',(640,720-100),path='premade') )
        self.dispgroup1.addpart( 'hero', draw.obj_image('herobase',(640-240,530),scale=0.5,) )
        self.dispgroup1.addpart( 'elder', draw.obj_image('elderbase',(640+240,530),scale=0.5,fliph=True) )
        self.dispgroup1.addpart( 'texta', draw.obj_textbox('[A]: rock',(640-80,530+50),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'textw', draw.obj_textbox('[W]: paper',(640,530),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'textd', draw.obj_textbox('[D]: scissors',(640+90,530+50),fontsize='small',color=share.colors.instructions) )
        self.dispgroup1.addpart( 'thinkcloud', draw.obj_image('thinkcloud',(200,320),path='premade') )
        self.dispgroup1.addpart( 'rock', draw.obj_image('rock',(100+50,320),scale=0.5) )
        self.dispgroup1.addpart( 'paper', draw.obj_image('paper',(100+50,320),scale=0.5) )
        self.dispgroup1.addpart( 'scissors', draw.obj_image('scissors',(100+50,320),scale=0.5) )
        self.addpart(self.dispgroup1)
        self.herochoice=0
        self.dispgroup1.dict['rock'].show=self.herochoice==0
        self.dispgroup1.dict['paper'].show=self.herochoice==1
        self.dispgroup1.dict['scissors'].show=self.herochoice==2
        for i in range(3):
            self.dispgroup1.addpart('hero_'+str(i), draw.obj_image('love',(640-300+i*75,240),scale=0.125) )
            self.dispgroup1.addpart('elder_'+str(i), draw.obj_image('love',(640+300-i*75,240),scale=0.125) )
            self.dispgroup1.addpart('herocross_'+str(i), draw.obj_image('smallcross',(640-300+i*75,240),path='premade') )
            self.dispgroup1.addpart('eldercross_'+str(i), draw.obj_image('smallcross',(640+300-i*75,240),path='premade') )
            self.dispgroup1.dict['herocross_'+str(i)].show=False
            self.dispgroup1.dict['eldercross_'+str(i)].show=False
        # self.addpart(draw.obj_imageplacer(self,'show1'))
        self.addpart( draw.obj_image('show1',(510,348),scale=0.65,fliph=False,flipv=True,path='premade') )
        self.addpart( draw.obj_image('show1',(744,347),scale=0.65,fliph=True,flipv=True,path='premade') )
        #
        # self.addpart( draw.obj_imageplacer(self,'cloud','sun','mountain') )
        self.addpart( draw.obj_image('sun',(1120,285),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1212,666),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1096,627),scale=0.24,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1207,536),scale=0.29,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(80,651),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(198,621),scale=0.22,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(118,564),scale=0.2,rotate=0,fliph=True,flipv=False) )
    def page(self,controls):
        super().page(controls)
        if controls.a and controls.ac:
            self.herochoice=0
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2
        elif controls.w and controls.wc:
            self.herochoice=1
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2
        elif controls.d and controls.dc:
            self.herochoice=2
            self.dispgroup1.dict['rock'].show=self.herochoice==0
            self.dispgroup1.dict['paper'].show=self.herochoice==1
            self.dispgroup1.dict['scissors'].show=self.herochoice==2



#########################################3



class obj_scene_ch4pp18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp19())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"Now lets play, said ',('{eldername}',share.colors.elder),'". ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True)
        self.addpart(self.world)


class obj_scene_ch4pp19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp18())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4pp20())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp19fail())
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
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360),record=False) )
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
class obj_scene_ch4pp19fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp19())
    def setup(self):
        self.text=[\
               'Giving up already. ',\
               'Well, that doesnt seem to be the story, said the book of things.  ',\
               'It looks like you should just go back and ',\
               ('perservere',share.colors.hero),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )


class obj_scene_ch4pp20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp21())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"Alright, lets play again, said ',('{eldername}',share.colors.elder),'". ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=False,elderwins=True)
        self.addpart(self.world)


class obj_scene_ch4pp21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp20())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4pp23())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp21fail())
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
        self.addpart( draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False) )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
class obj_scene_ch4pp21fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp21())
    def setup(self):
        self.text=[\
               'Oh, you want to give up. ',\
               'Sorry, that doesnt seem to be in the story, said the book of things.  ',\
               'It looks like you should just go back and ',\
               ('perservere',share.colors.hero),' a little more. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )




class obj_scene_ch4pp23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp24())
    def setup(self):
        self.text=[\
                '"What a ',('strong willed',share.colors.hero),' character, said ',('{eldername}',share.colors.elder),'. ',\
               'Receive my ',('teaching',share.colors.hero),'! ',\
               'In order to beat ',('{villainame}',share.colors.villain),\
               ' what you will need is ',('perseverance',share.colors.hero),'. ',\
               ('PER-SE-VE-RANCE',share.colors.hero),'! ','Look, you came all the way here, you climbed this ',('peak',share.colors.location),', ',\
               'and even when you were loosing you never gave up. You had it in you all this time!"',\
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




class obj_scene_ch4pp24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp23())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4pp25())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp24fail())
    def setup(self):
        self.text=[\
               '"May that be an important lesson for you, said ',('{eldername}',share.colors.elder),'. ',\
               'Ok, now that you got all this wisdom you gotta go. Goodbye!" ',\
                  ]
        self.addpart( draw.obj_animation('ch5eldertalks3','elderbase',(640,360)) )
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
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
class obj_scene_ch4pp24fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp24())
    def setup(self):
        self.text=[\
               'That doesnt seem to be the story, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('perservere',share.colors.hero),' in life. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )



class obj_scene_ch4pp25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp24())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4pp26())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp25fail())
    def setup(self):
        self.text=[\
               '"Oh I am really sorry, said ',('{eldername}',share.colors.elder),\
               ', but I dont have much time left for playing. ',\
               'Well its getting late, bye now!" ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Yes!','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
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
class obj_scene_ch4pp25fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp25())
    def setup(self):
        self.text=[\
               'Nope, that doesnt look like the story, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('perservere',share.colors.hero),' in life. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )


class obj_scene_ch4pp26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp25())
    def nextpage(self):
        if share.datamanager.getword('yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4pp27())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp26fail())
    def setup(self):
        self.text=[\
               '"You are starting to get on my nerves, said ',('{eldername}',share.colors.elder),'. ',\
               'It is near my bed time, so lets call it a day. ',\
               'Now scram! ". ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Play again:',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. YEEEES!','yes',(340,y1))
        textchoice.addchoice('2. No','no',(540,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_animation('ch5eldertalks4','elderbase',(640,360),record=False) )
        self.addpart( draw.obj_image('sun',(1062,324),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1195,633),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1044,667),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(68,662),scale=0.25,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(173,679),scale=0.19,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(109,486),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(920,560),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(279,571),scale=0.42,rotate=0,fliph=True,flipv=False) )
class obj_scene_ch4pp26fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp26())
    def setup(self):
        self.text=[\
               'Well, that is not how the story should go, said the book of things. ',\
               'Apparently, you have just been taught how important it is to ',\
               ('perservere',share.colors.hero),' in life. ',\
               'So I suggest you go back and do just that. ',\
                  ]
        animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5whatbook2','interrogationmark',(640,360),record=False,path='premade',sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )



class obj_scene_ch4pp27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp28())
    def setup(self):
        self.text=[\
               '"OWWWW, said ',('{eldername}',share.colors.elder),', you young punks have no respect! ',\
               'Fine, I will teach you my ',('real secret',share.colors.hero),'. ',\
               ('perseverance',share.colors.hero),' will only get you so far, what you really need is ',\
               ('cheating',share.colors.hero),'. ',\
               ('CHEA-TING',share.colors.hero),'! It\'s that simple. ',\
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

class obj_scene_ch4pp28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp29())
    def setup(self):
        self.text=[\
               'Seriously, when playing you can ',('peek',share.colors.hero),\
               ' at other\'s ',('bubble',share.colors.instructions),' to know what they are thinking. ',\
              'You can even counter ',('at the last moment',share.colors.hero),\
              ' and win ',('every time',share.colors.hero),', but you gotta be quick. ',\
                  ]
        self.dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup1.addpart( 'floor', draw.obj_image('floor5',(640,720-100),path='premade') )
        self.dispgroup1.addpart( 'hero', draw.obj_image('herobase',(640-240,530),scale=0.5,) )
        self.dispgroup1.addpart( 'elder', draw.obj_image('elderbase',(640+240,530),scale=0.5,fliph=True) )
        self.dispgroup1.addpart( 'thinkcloud2', draw.obj_image('thinkcloud',(1280-200,320),fliph=True,path='premade') )
        self.dispgroup1.addpart( 'elderrock', draw.obj_image('rock',(1280-100-50,320),scale=0.5) )
        self.dispgroup1.addpart( 'elderpaper', draw.obj_image('paper',(1280-100-50,320),scale=0.5) )
        self.dispgroup1.addpart( 'elderscissors', draw.obj_image('scissors',(1280-100-50,320),scale=0.5) )
        self.elderchoice=tool.randchoice([0,1,2])# 0,1,2 for rock, paper scissors
        self.dispgroup1.dict['elderrock'].show=self.elderchoice==0
        self.dispgroup1.dict['elderpaper'].show=self.elderchoice==1
        self.dispgroup1.dict['elderscissors'].show=self.elderchoice==2
        self.addpart(self.dispgroup1)
        self.timerswitch=tool.obj_timer(100)
        self.timerswitch.start()
        self.addpart( draw.obj_image('show3',(640+220,246),path='premade',fliph=True) )
        self.addpart( draw.obj_image('mountain',(1212,666),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1096,627),scale=0.24,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1207,536),scale=0.29,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(80,651),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(198,621),scale=0.22,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(118,564),scale=0.2,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(168,289),scale=0.37,rotate=0,fliph=False,flipv=False) )
    def page(self,controls):
        super().page(controls)
        self.timerswitch.update()
        if self.timerswitch.ring:# change elderly thinking
            self.timerswitch.start()
            if self.elderchoice==0:
                self.elderchoice=tool.randchoice([1,2])
            elif self.elderchoice==1:
                self.elderchoice=tool.randchoice([0,2])
            else:
                self.elderchoice=tool.randchoice([0,1])
            self.dispgroup1.dict['elderrock'].show=self.elderchoice==0
            self.dispgroup1.dict['elderpaper'].show=self.elderchoice==1
            self.dispgroup1.dict['elderscissors'].show=self.elderchoice==2


class obj_scene_ch4pp29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp28())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4pp30())
        else:
            share.scenemanager.switchscene(obj_scene_ch4pp29fail())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"Now lets play one last time, and if you ',('cheat',share.colors.hero),\
               ' fair and square you will be on your way". ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
class obj_scene_ch4pp29fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp29())
    def setup(self):
        self.text=[\
               'OWWWW you really dont listen, said ',('{eldername}',share.colors.elder),'. ',\
               'You need to ',\
               ('peek',share.colors.hero),' at what I am thinking and ',\
               ('counter',share.colors.hero),' me at the ',\
               ('last moment',share.colors.hero),'. ',\
               'Lets do this again before I loose my patience. ',\
                  ]
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )



class obj_scene_ch4pp30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp31())
    def setup(self):
        self.text=[\
               '"Alright, you really ',('won',share.colors.hero),' this time, said ',('{eldername}',share.colors.elder),'. ',\
               'You need to respect the elders more, you know. ',\
               'Owww, what is the world going to. Back in my time... ',\
                  ]
        y1=240
        self.addpart( draw.obj_textbox('Well :',(130,y1)) )
        textchoice=draw.obj_textchoice('yesno',default='yes')
        textchoice.addchoice('1. Goodbye','yes',(340,y1))
        textchoice.addchoice('2. Bye!','no',(540,y1))
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




class obj_scene_ch4pp31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp33())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"And so ',('{heroname}',share.colors.hero),', having learned a useful lesson, ',\
               'went back home".'
                  ]
        self.world=world.obj_world_travel(self,start='peak',goal='home',chapter=5)
        self.addpart(self.world)



class obj_scene_ch4pp33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp34())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_ch4pp34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed, hoping to defeat ',\
                   ('{villainname}',share.colors.villain),' and rescue ',\
                   ('{partnername}',share.colors.partner),' the next day".',\
                   ]
        self.world=world.obj_world_gotobed(self,alarmclock=True)
        self.addpart(self.world)


class obj_scene_ch4end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4pp34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',
                   'But we will be back tomorrow for more! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3playend())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter V',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available















#
