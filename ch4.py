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

# name house
class obj_scene_chapter4(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def setup(self):
        self.text=['-----   Chapter IV: A Perfect Story   -----   ',\
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
                   'captured ',('{partnername}',share.colors.partner),'. ',
                   ('{heroname}',share.colors.hero),\
                    ' rescued ',('{partner_him}',share.colors.partner),' after a long ',\
                 ('fight',share.colors.villain),' at the evil lair. ',\
                'They came back home, kissed and went to bed". ',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        self.addpart( draw.obj_image('tower',(1180,230), scale=0.35) )
        self.addpart( draw.obj_image('mountain',(1030,245), scale=0.4) )
        animation1=draw.obj_animation('ch4_hero1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch4_partner1','partnerbase',(640,360),record=False,sync=animation1)
        animation3=draw.obj_animation('ch4_villain1','villainbasegun',(640,360),record=False,sync=animation1)
        animation4=draw.obj_animation('ch4_love','love',(640,360),record=False,sync=animation1)
        animation4.addimage('empty',path='premade')
        animation5=draw.obj_animation('ch4_sunmoon','sun',(640,360),record=True,sync=animation1)
        animation5.addimage('moon')
        self.addpart(animation5)
        self.addpart(animation4)
        self.addpart(animation2)
        self.addpart(animation3)
        self.addpart(animation1)



class obj_scene_ch4p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def setup(self):
        self.text=[\
                   'I say this story is just ',('perfect',share.colors.hero),', said the book of things. ',\
                   'It has love, action, suspense, just everything! ',\
                   'I propose we celebrate, just draw a  ',('party hat',share.colors.item),\
                     'and a ',('drink',share.colors.item),'.',\
                   ]
        self.addpart( draw.obj_drawing('partyhat',(340,450),legend='Party Hat') )# use shadow
        self.addpart( draw.obj_drawing('drink',(940,450),legend='Drink',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        # 1) book+partyhat+drink =bookparty
        image1=draw.obj_image('book',(640,360))
        image2=draw.obj_image('partyhat',(640,210),scale=0.5)
        image3=draw.obj_image('drink',(390,480),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((290,850,110,580),'bookparty',edges=True)# 0 to 660 in height
        # 1) pen+partyhat+drink =penparty
        image1=draw.obj_image('pen',(640,360))
        image2=draw.obj_image('partyhat',(590,180),scale=0.45)
        image3=draw.obj_image('drink',(800,530),scale=0.45,fliph=True)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        # dispgroup1.snapshot((615,320,125,240),'penparty')# 0 to 660 in height
        dispgroup1.snapshot((490,890,80,620),'penparty',edges=True)# 0 to 660 in height
        # 1) eraser+partyhat+drink =eraserparty
        image1=draw.obj_image('eraser',(640,360))
        image2=draw.obj_image('partyhat',(720,210),scale=0.4,fliph=True)
        image3=draw.obj_image('drink',(470,350),scale=0.35)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((400,800,130,500),'eraserparty',edges=True)# 0 to 660 in height
        # 1) book+partyhat =bookpartyhat
        image1=draw.obj_image('book',(640,360))
        image2=draw.obj_image('partyhat',(640,210),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((290,850,110,580),'bookpartyhat',edges=True)# 0 to 660 in height


class obj_scene_ch4p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def setup(self):
        self.text=[\
                   'This is the best party ever, said the book of things. For the ',\
                   ('best story ever',share.colors.hero),'! ',\
                   'The book, pen and eraser partied all night. ',\
                   ]
        # self.addpart( draw.obj_image('book',(640,360), scale=1) )
        # self.addpart( draw.obj_image('partyhat',(640,210), scale=0.5) )
        # self.addpart( draw.obj_image('drink',(390,480), scale=0.5) )
        # self.addpart( draw.obj_image('pen',(640,360), scale=1) )
        # self.addpart( draw.obj_image('partyhat',(590,180), scale=0.5) )
        # self.addpart( draw.obj_image('drink',(800,530), scale=0.45) )
        # self.addpart( draw.obj_image('eraser',(640,360), scale=1) )
        # self.addpart( draw.obj_image('partyhat',(720,210), scale=0.4,fliph=True) )
        # self.addpart( draw.obj_image('drink',(470,350), scale=0.35) )
        # self.addpart( draw.obj_image('bookpartyhat',(640,360), scale=1) )
        # self.addpart( draw.obj_image('penpartyhat',(340,360), scale=1) )
        # self.addpart( draw.obj_image('eraserpartyhat',(940,360), scale=1) )
        animation1=draw.obj_animation('ch4_bookparty','bookparty',(640,360),record=False)
        animation2=draw.obj_animation('ch4_penparty','penparty',(900,480),record=False,sync=animation1)
        animation3=draw.obj_animation('ch4_eraserparty','eraserparty',(900,480),record=False,sync=animation1)
        animation4=draw.obj_animation('ch4_musicparty','musicnote',(640,360),record=False,sync=animation1)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)
        self.addpart(animation4)



class obj_scene_ch4p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def setup(self):
        self.text=[\
                   'The next morning, the book of things woke up and said: ',\
                   ' uh my head... I dont remember much about last night.',\
                   'But I am super excited to read our ',('perfect story',share.colors.hero),\
                   'all over again. ',\
                   ]
        self.addpart( draw.obj_image('eraser',(194,457), scale=0.7,rotate=-110) )
        self.addpart( draw.obj_image('partyhat',(292,551), scale=0.3,rotate=-140) )
        self.addpart( draw.obj_image('pen',(1067,550), scale=0.6,rotate=95) )
        self.addpart( draw.obj_image('partyhat',(1042,670), scale=0.35,rotate=-110,fliph=True) )
        self.addpart( draw.obj_image('drink',(985,362), scale=0.25,rotate=50) )
        self.addpart( draw.obj_image('drink',(744,669), scale=0.4,rotate=95) )
        self.addpart( draw.obj_image('drink',(151,643), scale=0.3,rotate=-70) )
        animation1=draw.obj_animation('ch4_bookwakeup','bookpartyhat',(640,360),record=False)
        self.addpart(animation1)
        # self.addpart( draw.obj_imageplacer(self,'eraser','partyhat','pen','drink') )





class obj_scene_ch4p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
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
        self.world=world.obj_world_sunrise(self)# Wake up hero mini-game
        self.addpart(self.world)




class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item),' ',\
                'with his partner ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),scale=0.5))
        self.world=world.obj_world_wakeup(self,partner='inlove',angryfaces=True)
        self.addpart(self.world)
        self.world.timerend.amount=50
        # self.addpart( draw.obj_imageplacer(self, 'herobaseangry','partnerbaseangry' ) )
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
        # combine stickbase+angryface+partnerhair=partnerbaseangry
        image1=draw.obj_image('partnerhair',(640,200))
        image2=draw.obj_image('stickbase',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,330,200,330),'partnerbaseangry')# 0 to 660 in height
        # combine stickhead+angryface+partnerhair=partnerheadangry
        image1=draw.obj_image('partnerhair',(640,360))
        image2=draw.obj_image('stickhead',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,360),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,200),'partnerheadangry')# 0 to 660 in height


class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def setup(self):
        self.text=[\
                   'Wait a minute, I think something is wrong, said the book of things. ',\
                ('{heroname}',share.colors.hero),' and ',\
                 ('{partnername}',share.colors.partner),' are arguing! ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        self.addpart( draw.obj_image('sun',(350,260),scale=0.45,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_heroargue','herobaseangry',(640,360),record=False)
        self.addpart( animation1)
        self.addpart(draw.obj_animation('ch4_partnerargue','partnerbaseangry',(640,360),record=False,sync=animation1))
        # self.addpart( draw.obj_imageplacer(self, 'sun' ) )
        # self.addpart( draw.obj_drawing('test',(990,180), shadow=(150,150)) )



class obj_scene_ch4p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def setup(self):
        self.text=[\
                   'Oh I see what has happened, said the book of things: ',\
                    'we have changed ',\
                ('{heroname}',share.colors.hero),' and ',\
                 ('{partnername}',share.colors.partner),'\'s relationship status from "',\
                  ('in love',share.colors.partner),'" to "',('its complicated',share.colors.villain),'". ',\
                'To be fair i am so hangover i dont remember anything of what we did last night. ',\
                   ]

        self.addpart( draw.obj_textbox('The hero and the partner were:',(250,320)) )
        self.addpart( draw.obj_textbox('1. in love',(630,320)) )
        self.addpart( draw.obj_textbox('2. its complicated',(1060,320)) )
        self.choice1=draw.obj_rectangle((630,320),100,50,color=share.colors.textchoice)
        self.choice2=draw.obj_rectangle((1060,320),150,50,color=share.colors.textchoice)
        self.addpart( self.choice1 )
        self.addpart( self.choice2 )
        self.choice1.show=False
        self.choice2.show=True
        self.addpart( draw.obj_image('love',(630,452),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herohead',(556,600),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('angryhead',(963,599),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerheadangry',(1131,594),scale=0.56,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('partnerhead',(724,605),scale=0.56,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self, 'herohead','partnerhead','angryhead','partnerheadangry','love' ) )





class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def setup(self):
        self.text=[\
                   'Maybe we can improve this situation at breakfast. ',\
                  'Quick, draw a ',('coffee cup',share.colors.item),' and an ',\
                  ('alarm clock',share.colors.item),' (draw around the clock panel). '
                   ]
        self.addpart( draw.obj_drawing('coffeecup',(340,450),legend='Coffee Cup',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('alarmclock',(940,450),legend='Alarm Clock',shadow=(200,200)) )
        self.addpart( draw.obj_image('alarmclockcenter',(940,450),path='premade') )
        self.addpart( draw.obj_image('alarmclock8am',(940,450),path='premade') )


class obj_scene_ch4p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'What in the... our ',('hero',share.colors.hero),' is getting drunk at breakfast! Hold [W] to sneak drink ',\
                'when ',('{partnername}',share.colors.partner),' isnt looking. ',\
                   ]
        self.world=world.obj_world_breakfastdrinking(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_animation('world_breakfastdrinking3','herobase',(640,360),record=False) )

        # self.addpart( draw.obj_drawing('completion1fill',(640,250),shadow=(300,50)) )

class obj_scene_ch4p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())



class obj_scene_ch4p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())



class obj_scene_ch4p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())



class obj_scene_ch4p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())



class obj_scene_ch4p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())



class obj_scene_ch4p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())



class obj_scene_ch4p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())



class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())



class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())



class obj_scene_ch4p920(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())



class obj_scene_ch4p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    # def nextpage(self):
        # share.scenemanager.switchscene(obj_scene_ch4p22())





































#
