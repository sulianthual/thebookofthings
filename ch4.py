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
                  'Draw a ',('coffee cup',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('coffeecup',(640,450),legend='Coffee Cup',shadow=(200,200)) )
        # self.addpart( draw.obj_drawing('alarmclock',(940,450),legend='Alarm Clock',shadow=(200,200)) )
        # self.addpart( draw.obj_image('alarmclockcenter',(940,450),path='premade') )
        # self.addpart( draw.obj_image('alarmclock8am',(940,450),path='premade') )


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
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    'Lets keep on reading, said the book of things. "',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish." Uh,',
                     ('{hero_he}',share.colors.hero),' is even littering. '\
                   ]
        self.world=world.obj_world_fishing(self)# fishing mini-game
        self.addpart(self.world)
        self.world.timerend.amount=50
        # self.addpart( draw.obj_imageplacer(self, 'drink','guitar','coffeecup' ) )
        self.addpart( draw.obj_image('drink',(99,649),scale=0.32,rotate=124,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('drink',(254,657),scale=0.32,rotate=244,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('guitar',(457,675),scale=0.32,rotate=250,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('coffeecup',(236,570),scale=0.32,rotate=146,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('drink',(69,544),scale=0.32,rotate=210,fliph=False,flipv=False) )


class obj_scene_ch4p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"When',\
                    ('{heroname}',share.colors.hero),' came back home, ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                'So ',('{hero_he}',share.colors.hero),' travelled to ',
                ('{villainname}',share.colors.villain),'\'s evil lair in the mountains". ',\
                   ]
        self.world=world.obj_world_traveltolair(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('grid',(640,400),shadow=(400,280)) )


class obj_scene_ch4p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' arrived at the evil lair. ',\
                    'No one was around so ',('{hero_he}',share.colors.hero),' went inside". ',\
                    'Its weird, I didnt remember the story exactly like this, said the book of things.',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(869,244),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1151,596),scale=0.61,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_heroevillair','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation1=draw.obj_animation('ch4_heroevillair2','empty',(640,360),record=False,path='premade',sync=animation1)
        animation1.addimage('interrogationmark',path='premade')
        self.addpart( animation1 )
        # self.addpart( draw.obj_drawing('interrogationmark',(640,360),shadow=(50,50)) )

        # self.addpart( draw.obj_imageplacer(self, 'mountain' ) )


class obj_scene_ch4p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),' stumbled on ',\
                    ('{partnername}',share.colors.partner),' and ',('{villainname}',share.colors.villain),\
                    '... in bed! ',\
                    ('{partnername}',share.colors.partner),' said: ',
                    'what are you doing here ',('{heroname}',share.colors.hero),'. ',\
                    'I hate ',('you',share.colors.hero),\
                    ' and I love ',('{villain_him}',share.colors.villain),\
                    ' so get lost !"',\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch4_herowalkson1','herobaseangry',(640,360),record=False)
        animation1.addimage('herobase')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_herowalkson2','partnerbaseangry',(640,360),record=False,sync=animation1)
        animation2.addimage('partnerbase')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch4_herowalkson3','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_herowalkson4','empty',(640,360),record=False,path='premade',sync=animation1)
        animation4.addimage('love')
        self.addpart( animation4 )

class obj_scene_ch4p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def setup(self):
        self.text=[\
                    '"I hate ',('you',share.colors.partner),' even more, said ',\
                    ('{heroname}',share.colors.hero),'. I am so angry right now, I guess I will just fight ',\
                    ('both of you',share.colors.villain),'!". ',\
                    'Huh this doesnt look too good, said the book of things. ',\
                   ]
        animation1=draw.obj_animation('ch4_herotalks1','herobaseangry',(640,360),record=True)
        animation1.addimage('herobase')
        self.addpart( animation1 )


class obj_scene_ch4p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p17())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"And so they fought with guns". ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self,heroangry=True,partnerenemy=True)
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # heroheadangry+stickcrouch =herocrouchangry
        image1=draw.obj_image('stickcrouch',(940,360),path='premade')
        image2=draw.obj_image('angryhead',(800,360),scale=0.5,rotate=90)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((940,360,300,200),'herocrouchangry')# 0 to 660 in height


class obj_scene_ch4p16death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobaseangry',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )



class obj_scene_ch4p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p18())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p17death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"... and then they fought with fists." ',\
                   ]
        self.world=world.obj_world_stompfight(self,heroangry=True,partnerenemy=True)
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # combine partnerheadangry+stickkick =partnerkickangry
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickkick',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('partnerheadangry',(640,200)) )
        dispgroup2.snapshot((640,330,300,330),'partnerkickangry')


class obj_scene_ch4p17death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobaseangry',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),\
                  ' defeated ',('{villainname}',share.colors.villain),\
                  ' and ',('{partnername}',share.colors.villain),'. ',\
                  'Suddendly, the evil lair took fire". ',\
                  'Quick, draw a ',('flame',share.colors.item),\
                  ', said the book of things. ',\
                   ]
        self.addpart( draw.obj_drawing('flame',(640,450),legend='Flame',shadow=(200,200)) )



class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    def setup(self):
        self.text=[\
                  '"',('{partnername}',share.colors.partner),\
                  ' and ',('{villainname}',share.colors.villain),\
                  ' laid unconscious in the burning ',('evil lair',share.colors.villain),'. ',\
                  ('{heroname}',share.colors.hero),' said: I hate you both so much now die!".',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(869,244),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1151,596),scale=0.61,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(877,605),scale=0.54,rotate=90,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(660,490),scale=0.51,rotate=90,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_evillairburns1','herobaseangry',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch4_evillairburns2','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns3','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns4','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns5','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns6','flame',(640,360),record=False,sync=animation1) )
        # self.addpart( draw.obj_imageplacer(self,'flame','partnerbaseangry') )


class obj_scene_ch4p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def setup(self):
        self.text=[\
                  '"Suddenly, ',('{heroname}',share.colors.hero),\
                  ' realized he had been hurt during the fight. ',\
                  'A large ',('scar',share.colors.villain),' was splitting his face. ',\
                  'He had become the ',('villain',share.colors.villain),'. ',\
                  'He erupted into a maniacal laughter and swore to do ',('evil',share.colors.villain),\
                  'for as long as he would breathe".',\
                   ]
        animation1=draw.obj_animation('ch4_heroisevil','angryhead',(640,360),record=False)
        animation1.addimage( 'angryheadscar' )
        animation1.addimage( 'heroheadscar' )
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch4_heroisevil2','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_heroisevil3','flame',(640,360),record=False,sync=animation1) )
    def presetup(self):
        super().presetup()
        # angryhead+scar=angryheadscar (not necessarily=villain if has hair)
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('angryhead',(640,360)) )
        dispgroup2.addpart('part2',draw.obj_image('scar',(640,360)) )
        dispgroup2.snapshot((640,360,200,200),'angryheadscar')
        # herohead+scar=heroheadscar
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('herohead',(640,360)) )
        dispgroup2.addpart('part2',draw.obj_image('scar',(640,360)) )
        dispgroup2.snapshot((640,360,200,200),'heroheadscar')

class obj_scene_ch4p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4playend())
    def setup(self):
        self.text=[\
                   '"And ',('{hero_he}',share.colors.hero),' lived evily ever after, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very evil story)',(640,280)) )
        self.addpart( draw.obj_image('house',(320,430), scale=0.25) )
        self.addpart( draw.obj_image('tree',(340,560), scale=0.25) )
        self.addpart( draw.obj_image('tower',(950,430), scale=0.25) )
        self.addpart( draw.obj_image('mountain',(910,540), scale=0.25) )
        self.addpart( draw.obj_image('herobaseangry',(538,439),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(732,570),scale=0.3,rotate=92,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(808,462),scale=0.27,rotate=92,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flame',(467,582),scale=0.21,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(417,331),scale=0.21,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flame',(850,347),scale=0.21,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(972,347),scale=0.16,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'flame','herobaseangry','partnerbaseangry','villainbase') )

class obj_scene_ch4playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=['This...this is quite terrifying, said the book of things. ',
                   'I really hope we can change this story tomorrow!',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4playend())
    def setup(self):
        self.text=['You have unlocked ',('Chapter V: Choices',share.colors.instructions),'. ',\
                  'You can always redraw the party hat, drink, coffee cup and flame in ',\
                  ('Chapter IV: A Perfect Story',share.colors.instructions),'. '\
                   '',\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available
        for c,value in enumerate(['partyhat','drink','coffeecup','flame']):
            self.addpart( draw.obj_image(value,(150+c*200,400), scale=0.25) )






































#