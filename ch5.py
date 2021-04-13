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

# name house
class obj_scene_chapter5(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def setup(self):
        self.text=['-----   Chapter V: The Highest Peak    -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Lets see how our story is going so far". ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch5p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' found out that ',\
                    ('{partnername}',share.colors.partner),' and ',\
                    ('{villainname}',share.colors.villain),\
                    ' were lovers, so he burned the place down and left them to die". ',\
                   'That is quite ',('evil',share.colors.villain),\
                   ', said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(1151,596),scale=0.61,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(877,605),scale=0.54,rotate=90,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(660,490),scale=0.51,rotate=90,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_evillairburns1','herobaseangry',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch4_evillairburns2','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns3','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns4','flame',(640,360),record=False,sync=animation1) )


class obj_scene_ch5p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p3())
    def setup(self):
        self.text=[\
                 'Well, it looks like ',('{heroname}',share.colors.hero),' has quite a few issues that ',\
                 ('{hero_he}',share.colors.hero),' could work on, said the book of things. ',\
                   'Lets try help ',('{hero_him}',share.colors.hero),' a little. ',\
                   'Start by drawing a ',('night stand',share.colors.item),\
                   'and an ',('alarm clock',share.colors.item),\
                   'to wake ',('{hero_him}',share.colors.hero),' up on time. ',\

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



class obj_scene_ch5p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'Ok here we go: "Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' ',\
                'that lived in a  ',('house',share.colors.item),' ',\
                'with ',('trees',share.colors.item),'. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch5p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' woke up, but ',\
                ('{partnername}',share.colors.partner),' wasnt there. ',\
                   ]
        self.world=world.obj_world_wakeup(self,angryfaces=True,sun=True,alarmclock=True)
        self.addpart(self.world)
        # self.addpart (draw.obj_imageplacer(self,'nightstand','alarmclock'))
        # self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5,rotate=0,fliph=False,flipv=False) )
        # animation1=draw.obj_animation('wakeup_alarmclock','alarmclock',(640,360),record=False)
        # animation2=draw.obj_animation('wakeup_sun','sun',(640,360),record=True,sync=animation1)
        # self.addpart( animation1 )
        # self.addpart( animation2 )



class obj_scene_ch5p4a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"The ',('hero',share.colors.hero),' got drunk for breakfast". ',\
                'Well that isnt too hard to do with ',('{partnername}',share.colors.partner),' gone, said the book of things. ',\
                   ]
        self.world=world.obj_world_breakfastdrinking(self,partner=False)
        self.addpart(self.world)


class obj_scene_ch5p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch5p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox.',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    ('two',share.colors.item),' letters". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobaseangry',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),record=True,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart(animation2)
        # self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )



class obj_scene_ch5p6a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6b())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(163+30,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Hey ',('looser',share.colors.hero),', ',\
                      '\nYou really need to work on your issues. ',\
                     'I am dumping you and I am going to live with ',\
                    ('{villainname}',share.colors.villain),' in ',\
                    ('{villain_his}',share.colors.villain),' ',('evil lair',share.colors.location),'. '\
                      'Dont ever call me again. XOXO, ',\
                    '\n\nsigned: ',('{partnername}',share.colors.partner),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('partnerhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch5p6b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p7())
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
                      '\nAre you having issues. Are you looking for meaning in life. ',\
                     'Come find the solution to all your problems at the  ',\
                    ('highest peak',share.colors.location),'. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('interrogationmark',(1065,305),path='premade',scale=1.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))





class obj_scene_ch5p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p8())
    def setup(self):
        self.text=[\
                   'I think we are onto something, said the book of things.',\
                   ' Our ',('hero',share.colors.hero),' is so down right now that ',\
                  'this ',('highest peak',share.colors.location),' thing cant hurt. ',\
                  ' It is so high up in the sky it is always covered by stormy clouds. ',\
                 'So draw a ',('cloud',share.colors.item),' and a',\
                 ('lightning bolt',share.colors.hero),'. ',\
                   ]
        self.addpart( draw.obj_drawing('cloud',(340,450),legend='Cloud',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('lightningbolt',(940,450),legend='Lightning Bolt',shadow=(200,200)) )


class obj_scene_ch5p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Great, now lets write: "',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('highest peak',share.colors.location),' to find meaning in life". ',\
                   ]
        self.world=world.obj_world_traveltopeak(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'house','tree','tower','mountain','cloud','lightningbolt') )


class obj_scene_ch5p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p10())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                ' climbed the ',('highest peak',share.colors.location),'".',\
                   ]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('platform1',(340,450),shadow=(150,25)) )
        # self.addpart( draw.obj_drawing('arrowup',(340,450),shadow=(50,50)) )
        # self.addpart( draw.obj_imageplacer(self,'platform1','cloud','lightningbolt','sun','mountain') )


class obj_scene_ch5p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def setup(self):
        self.text=[\
                '" When ',('{heroname}',share.colors.hero),\
                ' reached the top of ',('highest peak',share.colors.location),\
                ', he encountered a mysterious character.',\
                'It was an ',('elder',share.colors.elder),' that granted wisdom".',\
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
        self.addpart( draw.obj_textinput('eldername',25,(750,y2),color=share.colors.hero, legend='Villain Name') )


class obj_scene_ch5p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p12())
    def setup(self):
        self.text=[\
               'Now draw the ',\
               ('elder',share.colors.elder),'\'s face, and make it look slightly to the right. ',\
                'I suggest you draw a happy face and add some wrinkles and maybe a beard, ',\
                'but that is entirely up to you. ',\
                   ]
        # self.addpart( draw.obj_image('herohead',(640,450)) )
        self.addpart( draw.obj_drawing('elderhead',(640,450),legend='Draw the Elder') )
    def endpage(self):
        super().endpage()
        # save elder full body
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'elderbase')

class obj_scene_ch5p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p13())
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
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','cloud','sun','mountain') )


class obj_scene_ch5p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p14())
    def setup(self):
        self.text=[\
               '"The ',('elder',share.colors.elder),' said: oh, a visitor, did you receive my mail. ',\
               ' My name is ',('{eldername}',share.colors.elder),\
               ' and I may grant you the wisdom to solve all your problems, hi hi hi. ',\
                  ]
        # self.addpart( draw.obj_image('elderhead',(640,450),fliph=True) )
        animation1=draw.obj_animation('ch5eldertalks1','elderbase',(640,360),record=False)
        self.addpart( animation1 )



class obj_scene_ch5p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p15())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"First, lets cover my fee, said the ',('elder',share.colors.elder),'. ',\
                    'I see you have caught a yummy ',\
                    ('fish',share.colors.item),'. I am starving, so that will be my lunch hi hi hi".',\
                   ]
        self.world=world.obj_world_eatfish(self,eldereats=True)
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'herobaseangry','interrogationmark') )
        self.addpart( draw.obj_image('herobaseangry',(1172,376),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('interrogationmark',(1214,167),scale=1.2,path='premade') )


class obj_scene_ch5p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p16())
    def setup(self):
        self.text=[\
               '"Now, lets grant you the wisdom, said ',('{eldername}',share.colors.elder),'. ',\
               'All you have to do is win one easy game of ',('rock-paper-scissors',share.colors.item),\
               ', hi hi hi". ',\
               'Well, that sounds rather easy, said the book of things. Just draw each ',\
               ('item',share.colors.item),'. ',\
                  ]
        drawing1=draw.obj_drawing('rock',(200+20,450),legend='Large Rock',shadow=(200,200))
        # drawing1.brush.makebrush(share.brushes.smallpen)
        self.addpart(drawing1)
        drawing2=draw.obj_drawing('paper',(640,450),legend='Piece of Paper',shadow=(200,200))
        # drawing2.brush.makebrush(share.brushes.smallpen)
        self.addpart(drawing2)
        drawing3=draw.obj_drawing('scissors',(1280-200-20,450),legend='Scissors',shadow=(200,200))
        # drawing3.brush.makebrush(share.brushes.smallpen)
        self.addpart(drawing3)

class obj_scene_ch5p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p17())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               'Alright, said the book of things. ',\
               'Select rock, paper or scissors with [A][W][D], and ',\
               'press [S] when you are ready to start the countdown with the ',('elder',share.colors.elder),'. ',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self,elderthinks=True)
        self.addpart(self.world)
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','rock','paper','scissors') )
        # self.addpart( draw.obj_drawing('smallcross',(640,240),shadow=(50,50),brush=share.brushes.pen) )
        # self.addpart( draw.obj_animation('ch5_rpsloose','herobase',(640,360),record=False) )
        # self.addpart( draw.obj_animation('ch5_rpswin','elderbase',(640,360),record=False) )

class obj_scene_ch5p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p18())


class obj_scene_ch5p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p19())



class obj_scene_ch5p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p18())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch5p20())

# ' The elder said: very well, now lets grant you this wisdom. To get it, all you have to do is win one easy game, hi hi hi". ',\


























####################################################################################################################
####################################################################################################################

#
