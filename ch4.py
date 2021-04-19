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

# name house
class obj_scene_chapter4(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def setup(self):
        self.text=['-----   Chapter IV: The Elder  -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Lets see how our story is going so far". ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch4p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def setup(self):
        self.text=['" The ',('villain',share.colors.villain),\
                   ' captured ',('{partnername}',share.colors.partner),'. ',
                   ('{heroname}',share.colors.hero),\
                    ' rescued ',('{partner_him}',share.colors.partner),' after a long ',\
                 ('fight',share.colors.villain),' at the evil lair. ',\
                'They came back home, kissed and went to bed". ',\
                   ]
        self.addpart( draw.obj_image('tower',(1180,230), scale=0.35) )
        self.addpart( draw.obj_image('mountain',(1030,245), scale=0.4) )
        self.addpart( draw.obj_image('sun',(138,258),scale=0.4) )
        animation1=draw.obj_animation('ch4_hero1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch4_partner1','partnerbase',(640,360),record=False,sync=animation1)
        animation3=draw.obj_animation('ch4_villain1','villainbasegun',(640,360),record=False,sync=animation1)
        animation4=draw.obj_animation('ch4_love','love',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='premade')
        self.addpart(animation4)
        self.addpart(animation2)
        self.addpart(animation3)
        self.addpart(animation1)
        # self.addpart(draw.obj_imageplacer(self,'sun'))


class obj_scene_ch4p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        self.text=[\
                   'Today, lets add a ',('quest',share.colors.item),\
                   ' that will empower ', ('{heroname}',share.colors.hero),'. ',\
                  ('{hero_he}',share.colors.hero),' will go the ',('Highest Peak',share.colors.location),'. ',\
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
               '"I may grant you the gift of ',('agility',share.colors.item),\
               ', said ',('{eldername}',share.colors.elder),'. ',\
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
        share.scenemanager.switchscene(obj_scene_ch4p9())
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


class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def setup(self):
        self.text=[\
               'You can ',('peek',share.colors.hero),\
               ' at other\'s ',('bubble',share.colors.instructions),' to know what they are thinking. ',\
              'Be quick and counter their hand ',('at the last moment',share.colors.hero),\
              ' to win. ',\
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

class obj_scene_ch4p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4play())
        else:
            share.scenemanager.switchscene(obj_scene_ch410fail())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"Now lets play".',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
class obj_scene_ch4p10fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
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



##########################################################
##########################################################
# PLAY CHAPTER

class obj_scene_ch4play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_sunrise())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                   'Thats quite a few changes to our story, said the book of things. ',\
                  'Lets read it again to summarize. ',\
                   'Press [S] to start. ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Start',(640,660),color=share.colors.instructions))
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)

class obj_scene_sunrise(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' ',\
                'that lived in a  ',('house',share.colors.item),' ',\
                'with ',('trees',share.colors.item),'. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_wakeup(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_sunrise())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item),' ',\
                'with ',('{hero_his}',share.colors.hero),\
                ' partner ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner=True)
        self.addpart(self.world)


class obj_scene_fishing(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_mailbox(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromvillain())
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
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_letterfromvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_mailboxagain())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(163,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI have captured ',('{partnername}',share.colors.partner),'. ',\
                     '\nCome to my ',('evil lair',share.colors.location),' to save ',\
                     ('{partner_him}',share.colors.partner),' if you dare. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))



class obj_scene_mailboxagain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromelder())
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
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )



class obj_scene_letterfromelder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailboxagain())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travelhomepeak())
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
                      '\nDo you need to rescue someone. ',\
                      'Fight a ',('villain',share.colors.villain),'. ',\
                     'Come find help at the  ',\
                    ('highest peak',share.colors.location),'. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('interrogationmark',(1065,305),path='premade',scale=1.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_travelhomepeak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromelder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_climbpeak())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '" And so ',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('highest peak',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='peak',chapter=5)
        self.addpart(self.world)


class obj_scene_climbpeak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travelhomepeak())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_meetelder())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{hero_he}',share.colors.hero),\
                ' climbed the ',('highest peak',share.colors.location),'".',\
                   ]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)



class obj_scene_meetelder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_climbpeak())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_elderoffer())
    def setup(self):
        self.text=[\
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


class obj_scene_elderoffer(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_meetelder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())

    def setup(self):
        self.text=[\
               '"I may grant you the gift of ',('agility',share.colors.item),\
               ', said ',('{eldername}',share.colors.elder),'. ',\
               'All you have to do is win a game of ',('rock-paper-scissors',share.colors.item),\
               '". ',\
                  ]
        self.addpart( draw.obj_image('sun',(188,298),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(71,576),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(221,630),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1053,226),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1192,383),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(313,444),scale=0.32,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'cloud','sun','mountain') )
        animation1=draw.obj_animation('ch5eldertalks1','elderbase',(640,360),record=False)
        self.addpart( animation1 )



class obj_scene_rpselder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_elderoffer())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_elderwon())
        else:
            share.scenemanager.switchscene(obj_scene_rpselderfail())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"And so they played".',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
class obj_scene_rpselderfail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' lost."',\
                'Well, that doesnt sound right, said the book of things. ',\
               ('Peek',share.colors.hero),' at what your opponent is thinking and ',\
               ('counter',share.colors.hero),' at the ',\
               ('last moment',share.colors.hero),'. ',\
                'Now try again. ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_elderwon(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travelpeaklair())
    def setup(self):
        self.text=[\
                '"You won! said ',('{eldername}',share.colors.elder),'. ',\
               'As a reward, I shall grant you the gift of ',('agility',share.colors.item),'.', \
               'With this, you will even be able to dodge bullets".',\
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



class obj_scene_travelpeaklair(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_elderwon())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_meetvillain())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '" And so ',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('evil lair',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='peak',goal='tower',chapter=5)
        self.addpart(self.world)




class obj_scene_meetvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travelpeaklair())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                    ('{heroname}',share.colors.hero),' confronted ',\
                  ('{villainname}',share.colors.villain),' at the ',('evil lair',share.colors.location),', ',\
                'and they started to ',('fight',share.colors.villain),' for ',\
              ('{partnername}',share.colors.partner),'. ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))



class obj_scene_dodgebullets(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_meetvillain())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_defeatvillain())
        else:
            share.scenemanager.switchscene(obj_scene_dodgebulletsdeath())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"They fought with guns". ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)
class obj_scene_dodgebulletsdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )



class obj_scene_defeatvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travellairhome())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.a and controls.d)
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' defeated ',\
                  ('{villainname}',share.colors.villain),' and rescued ',\
                  ('{partnername}',share.colors.partner),'. ',\
                  ('{villainname}',share.colors.villain),' said "I will have my revenge" ',\
                  'and disappeared in the mountains". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )
        self.addpart(draw.obj_textbox('Press [A]+[D] to Continue',(640,660),color=share.colors.instructions))




class obj_scene_travellairhome(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_defeatvillain())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dinner())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' and ',\
                  ('{partnername}',share.colors.partner),' went back home". ',\
                   ]
        self.world=world.obj_world_travel(self,start='tower',goal='home',chapter=3,partner=True)
        self.addpart(self.world)




class obj_scene_dinner(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travellairhome())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_serenade())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"They  ate ',\
                    ('fish',share.colors.item),' for dinner".',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)


class obj_scene_serenade(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dinner())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_kiss())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade..." ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)


class obj_scene_kiss(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_serenade())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"...and then they kissed".   ',\
                   ]
        self.world=world.obj_world_kiss(self)
        self.addpart(self.world)


class obj_scene_nightfall(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_kiss())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_gotobed())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_gotobed(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4playend())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True)
        self.addpart(self.world)




class obj_scene_ch4playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_gotobed())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=[\
                   '"And they lived happily ever after, the End". ',\
                    'And thats it for today, said the book of things. ',
                   'That is quite a story, well done! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4playend())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter V',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available





















































#
