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
                   ' uh my head... I dont remember much about last night. Lets read our story again. ',\
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


class obj_scene_ch4p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())



class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())



class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())




class obj_scene_ch4p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())




class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p8())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch4p10())






































#
