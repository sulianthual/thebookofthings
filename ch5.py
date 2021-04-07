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
        self.text=['-----   Chapter V: Maybe Maybe Maybe    -----   ',\
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
        share.scenemanager.switchscene(obj_scene_ch5sunrise())
    def setup(self):
        self.text=[\
                  'Choices have consequences you see, and they lead to different outcomes in this story. ',\
                 'This is what happened yesterday when we changed the ',('hero',share.colors.hero),' and ',\
                 ('partner',share.colors.partner),'\'s relationship status to "its complicated". ',\
                 'Today we shall explore more choices until we change the ',\
                 ('evil ending',share.colors.villain),' from yesterday for a ',\
                ('redemptive ending',share.colors.hero),'. '\
                   ]
        y1=400
        self.addpart( draw.obj_textbox('The hero and the partner were:',(250,y1)) )
        self.addpart( draw.obj_textbox('1. in love',(630,y1)) )
        self.addpart( draw.obj_textbox('2. its complicated',(1060,y1)) )
        self.choice1=draw.obj_rectangle((630,y1),100,50,color=share.colors.textchoice)
        self.choice2=draw.obj_rectangle((1060,y1),150,50,color=share.colors.textchoice)
        self.addpart( self.choice1 )
        self.addpart( self.choice2 )
        self.choice1.show=False
        self.choice2.show=True

##########################################################
##########################################################
# From here we use unordered pages for the story with multiple choices


class obj_scene_ch5sunrise(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5wakeup())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'Remember, explore choices to obtain a ',\
               ('redemptive ending',share.colors.hero),' for this story, said the book of things. Lets start: ',\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' ',\
                'that lived in a  ',('house',share.colors.item),' ',\
                'with ',('trees',share.colors.item),'. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch5wakeup(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5sunrise())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosebreakfast())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' and ',\
                ('{partnername}',share.colors.partner),' woke up. ',\
                'They were angry because their relationship was complicated". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),scale=0.5))
        self.world=world.obj_world_wakeup(self,partner='inlove',angryfaces=True)
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # combine stickhead+angryface+stickbody = herobaseangry
        image1=draw.obj_image('stickbody',(640,460),path='premade')
        image2=draw.obj_image('stickhead',(640,200),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,300),'herobaseangry')
        # combine stickbase+angryface+partnerhair=partnerbaseangry
        image1=draw.obj_image('partnerhair',(640,200))
        image2=draw.obj_image('stickbase',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,330,200,330),'partnerbaseangry')
        # combine stickhead+angryface+partnerhair=partnerheadangry
        image1=draw.obj_image('partnerhair',(640,360))
        image2=draw.obj_image('stickhead',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,360),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,200),'partnerheadangry')



class obj_scene_ch5choosebreakfast(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5wakeup())
    def nextpage(self):
        if share.datamanager.getword('hero_breakfast')=='drink':
            share.scenemanager.switchscene(obj_scene_ch5breakfast_drinking())
        else:
            share.scenemanager.switchscene(obj_scene_ch5breakfast_notdrinking())
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'decided what to have for breakfast". ',\
                'This is it, said the book of things. Lets make a wise choice that will improve ',\
                ('{heroname}',share.colors.hero),' and ',\
                ('{partnername}',share.colors.partner),'\'s relationship. ',\
                   ]
        y1=400
        self.addpart( draw.obj_textbox('The hero decided to have:',(340,y1)) )
        textchoice=draw.obj_textchoice('hero_breakfast')
        textchoice.addchoice('1. A drink','drink',(640,y1))
        textchoice.addchoice('2. A cup of coffee','coffeecup',(940,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('herohead',(340,550),scale=0.35) )
        self.addpart( draw.obj_image('drink',(640,550),scale=0.35) )
        self.addpart( draw.obj_image('coffeecup',(940,550),scale=0.35) )


class obj_scene_ch5breakfast_drinking(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosebreakfast())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosefishing())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'got drunk at breakfast and made ',\
                ('{partnername}',share.colors.partner),' more angry".',\
                   ]
        self.world=world.obj_world_breakfastdrinking(self)
        self.addpart(self.world)


class obj_scene_ch5breakfast_notdrinking(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosebreakfast())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosefishing())
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'got coffee for breakfast. ',\
                ('{partnername}',share.colors.partner),' was a little ',\
                ('happier',share.colors.partner),'".',\
                   ]
        self.addpart( draw.obj_image('floor3',(640,720-100),path='premade') )
        self.addpart( draw.obj_image('coffeecup',(830,560),scale=0.5,fliph=False) )
        self.addpart( draw.obj_image('coffeecup',(495,560),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('herobaseangry',(150,540),scale=1.15,fliph=False) )
        self.addpart( draw.obj_image('stickbody',(1160-50,640+15),scale=1.15,fliph=True,path='premade') )
        animation1=draw.obj_animation('ch5_breakfastpartner1','partnerheadangry',(640,360),record=True)
        animation1.addimage('partnerhead')
        self.addpart( animation1 )


class obj_scene_ch5choosefishing(page.obj_chapterpage):
    def prevpage(self):
        if share.datamanager.getword('hero_breakfast')=='drink':
            share.scenemanager.switchscene(obj_scene_ch5breakfast_drinking())
        else:
            share.scenemanager.switchscene(obj_scene_ch5breakfast_notdrinking())
    def nextpage(self):
        if share.datamanager.getword('hero_fishing')=='pickuptrash':
            share.scenemanager.switchscene(obj_scene_ch5fishing_trashcleanup())
        else:
            share.scenemanager.switchscene(obj_scene_ch5fishing_withtrash())

    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'decided what to do next". ',\
                'Keep it on, said the book of things, remember to make wise choices ',\
                'for a ',('redemptive ending',share.colors.hero),'. ',\
                   ]
        y1=400
        self.addpart( draw.obj_textbox('The hero decided to:',(180,y1)) )
        textchoice=draw.obj_textchoice('hero_fishing')
        textchoice.addchoice('1. go fishing','fish',(540,y1))
        textchoice.addchoice('2. Pick up the trash in the river','pickuptrash',(940,y1))
        self.addpart( textchoice )



class obj_scene_ch5fishing_withtrash(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosefishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5default())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river, caught a fish and littered".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        self.addpart( draw.obj_image('drink',(99,649),scale=0.32,rotate=124,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('drink',(254,657),scale=0.32,rotate=244,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('guitar',(457,675),scale=0.32,rotate=250,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('coffeecup',(236,570),scale=0.32,rotate=146,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('drink',(69,544),scale=0.32,rotate=210,fliph=False,flipv=False) )


class obj_scene_ch5fishing_trashcleanup(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5choosefishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5default())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and picked up all the trash. ',\
                      'The fish was quite ',\
                      ('pleased',share.colors.partner),' with that".',\
                   ]
        animation1=draw.obj_animation('fishmove1','fish',(640,360),imgscale=0.25)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5_pickuptrash1','love',(640,360),record=True,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )


# 1) just fish
#) 2) pick up trash, fish is happy and comes to the rescue latter on (as a river god)!!!



#
class obj_scene_ch5default(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        pass
    def setup(self):
        self.text=[\
                'default page',\
                   ]



#
