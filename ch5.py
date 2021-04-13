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
                  'Well, lets try to change this story a bit today. ',\
                 'It looks like ',('{heroname}',share.colors.hero),' has quite a few issues that ',\
                 ('{hero_he}',share.colors.partner),' could work on. ',\
                   ]




class obj_scene_ch5p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
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


class obj_scene_ch5p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' woke up, but ',\
                ('{partnername}',share.colors.partner),' wasnt there. ',\
                   ]
        self.world=world.obj_world_wakeup(self,angryfaces=True)
        self.addpart(self.world)


class obj_scene_ch5p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p4())
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
        share.scenemanager.switchscene(obj_scene_ch5p7())
    def setup(self):
        self.text=[\
                  '"When',\
                    ('{heroname}',share.colors.hero),' came back home, ',\
                  ('{partnername}',share.colors.partner),' still wasnt there. ',\
                   'There were ',('two letters',share.colors.item),' in the mail. ',
                    'The first one said: ',\
                     '\n\nHe    `y looser, its ',('{partnername}',share.colors.partner),'. ',\
                      'Me and ',('{villainname}',share.colors.villain),' are madly in love ',\
                       'and I am dumping you. Btw, you have some issues. Dont ever call again. XOXO ',\
                    '\n\nThe second letter said: ',\
                     '\n\nHaving issues? Looking for meaning in life? ',\
                      'Come find answers at the Highest Peak ',\
                       '(Conveniently located just north of the hero\'s house). ',\
                   ]


class obj_scene_ch5p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p8())
    def setup(self):
        self.text=[\
                   'I think we are onto something, said the book of things.',\
                   ' Our ',('hero',share.colors.hero),' is probably a bit down right now, ',\
                  'so this ',('highest peak',share.colors.hero),' thing cant hurt. ',\
                  ' It is so high up in the sky it is always covered by stormy clouds. ',\
                 'So raw a ',('cloud',share.colors.item),' and a',\
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
                  ('highest peak',share.colors.hero),' to find meaning in life". ',\
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
                ' climbed the highest peak".',\
                   ]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('platform1',(340,450),shadow=(150,25)) )
        # self.addpart( draw.obj_drawing('arrowup',(340,450),shadow=(50,50)) )
        # self.addpart( draw.obj_imageplacer(self,'platform1','cloud','sun','mountain') )


class obj_scene_ch5p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p11())
    def setup(self):
        self.text=[\
                '" When ',('{heroname}',share.colors.hero),\
                ' reached the top of the highest peak, he encountered a mysterious character.',\
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
        self.addpart( draw.obj_drawing('elderhead',(640,450),legend='The Elder') )
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
               'Lets continue, say the book of things: "',\
               ('{heroname}',share.colors.hero),' met ',('{eldername}',share.colors.elder),', the ',\
               ('elder',share.colors.elder),' that lived at the top of the high peak. ',\
                'The ',('elder',share.colors.elder),\
                'said: "so you have come to seek wisdom, Hi Hi". ',\
                   ]
        self.text=[\
               '"The ',('elder',share.colors.elder),' said: so you have come here to seek wisdom.',\
               ' I, ',('{eldername}',share.colors.elder),', may give this to you. All you have to do is win one easy game, hi hi hi". ',\
                   ]
        self.addpart( draw.obj_image('elderbase',(964,325),scale=0.48,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(424,572),scale=0.49,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sun',(128,457),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(72,655),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(209,681),scale=0.22,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(667,300),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1198,468),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1176,246),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('floor4',(1280-500,720-140),path='premade') )
        self.addpart( draw.obj_animation('ch5_meetelder','herobase',(640,360),record=False) )
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','cloud','sun','mountain') )


class obj_scene_ch5p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p12())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch5p14())
    def setup(self):
        self.text=[\
               '"Well actually, said"',\
               ('{eldername}',share.colors.elder),', the story is unfinished and its stop here for now. ',\
               'Sorry about that. But do come back later for more. ',\
                   ]
        self.addpart( draw.obj_image('elderhead',(640,450),fliph=True) )



####################################################################################################################
####################################################################################################################

#
