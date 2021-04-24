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
    # def setup(self):
    #     self.text=['-----   Chapter IV: Something East   -----   ',\
    #                '\n In this chapter introduce the first part of quest. ',\
    #               '\n Must go east to enchanted forest, learn to lie from a bunny in a cave ',\
    #                ]


class obj_scene_ch4p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p1())
        # share.scenemanager.switchscene(obj_scene_lyingstart())
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
        share.scenemanager.switchscene(obj_scene_ch4p3())
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


class obj_scene_ch4p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p2())
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
                'woke up from ',('bed',share.colors.item),' ',\
                'with ',('{hero_his}',share.colors.hero),\
                ' new friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True)
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
                'Well, draw the ',('bunny',share.colors.bunny),'\'s head, said the book of things. ',\
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
                '"So you think I am cute, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'Well, look carefully at all these trees. Poof, they are all gone, I just chopped them with my little paw. ',\
                'Do you still want to pet me now". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
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
                ', the ',('Grandmaster of Deceit',share.colors.villain),\
                ' from the east! ',\
                'Tremble before me and my evil ways". ',\
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
                'Tell you what, if you win my ',('lying game',share.colors.villain),\
                ' I might even tell you a secret". ',\
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
        share.scenemanager.switchscene(obj_scene_ch4p18())


class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())


class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch4p20())


############
#
#
# class obj_scene_ch4p6(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p5())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p7())
#
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingstart())
#     def setup(self):
#         self.text=['The bunny said, I am the grandmaster of deceit from the east.',\
#                     ' Win my lying game to receive my evil teachings. ',\
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'herobase','bunny') )
#         self.addpart( draw.obj_image('herobase',(328,465),scale=0.63,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('bunnybase',(919,481),scale=0.63,rotate=0,fliph=True,flipv=False) )


############################

class obj_scene_ch4end(page.obj_chapterpage):
    # def prevpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch4p1())
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
# Lying game

class obj_scene_lyingstart(page.obj_chapterpage):
    # def prevpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch4p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingdatabase())
    def setup(self):
        self.text=[\
                    'Welcome to the lying game, said the bunny. ',\
                   ]

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
        self.statements['spider']=['I am not afraid of spiders','I am scared of spiders']
        self.statements['booger']=['I dont eat my boogers','I eat my boogers']
        #
        ########################################
        # Save the database in datamanger temp object
        share.datamanager.temp.statements=self.statements# full database


class obj_scene_lyingpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingstart())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q1())
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
                    ('true statements',share.colors.darkgreen),' you need to remember. ',\
                    'You can even draw some notes at the bottom of the screen to help your memory. '
                   ]
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][self.stat01[0]],(400,220),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][self.stat01[1]],(400,290),xleft=True,color=share.colors.darkgreen  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][self.stat01[2]],(400,360),xleft=True,color=share.colors.darkgreen  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(500,120),legend='Take some notes')
        drawing.clear()# erase drawing
        self.addpart( drawing )

class obj_scene_lyingfailpart1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1())
    def setup(self):
        self.text=['Sorry, you gave me the wrong answer. ',\
                    'If your memory is that bad you can always ',\
                    ('draw some notes',share.colors.darkgreen),' at the bottom of the screen. ',\
                    'Now go back and win this first round, I know you can do it! ',\
                                ]


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
        self.text=['Now tell me if the following is ',('True',share.colors.darkgreen),':   ']
        self.addpart( draw.obj_textbox( \
        self.statements[qstatkeys[0]][qstat01[0]]+' and '+\
        self.statements[qstatkeys[1]][qstat01[1]],(640,220) ) )
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('True','yes',(640-100,290))
        textchoice.addchoice('False','no',(640+100,290))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('lyingnote',(640,530)) )
        self.addpart( draw.obj_textbox( 'Use your notes',(640,685),color=share.colors.instructions  ) )
        # if share.devmode:# check correct answer
        if True:
            print('###')
            print('truth='+ str(self.statdict))
            print('statment='+ str(qstatdict))
            print('answer='+ str(self.nextpage_correctanswer()))


class obj_scene_lyingp1q2(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q3())

class obj_scene_lyingp1q3(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart1win())

class obj_scene_lyingpart1win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp1q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        self.text=[\
                    'Well done. You won the first round! ',\
                   ]

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
                    ('False',share.colors.red),' statements, remember them well. ',\
                    'Once again, you can draw some notes to help your memory. '
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][1-self.stat01[0]],(400,220),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][1-self.stat01[1]],(400,290),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][1-self.stat01[2]],(400,360),xleft=True,color=share.colors.red  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(500,120),legend='Take some notes')
        drawing.clear()# erase drawing
        self.addpart( drawing )

class obj_scene_lyingfailpart2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def setup(self):
        self.text=['Sorry, you gave me the wrong answer. ',\
                    'For this second round, remember that ',\
                    ('all my statements are False',share.colors.red),'. ',\
                    'I may suggest that you figure out the ',\
                    ('True statements',share.colors.darkgreen),\
                    ' and draw them at the bottom of the screen. ',\
                    'Now go back and win this second round, I know you can do it! ',\
                                ]

class obj_scene_lyingp2q1(obj_scene_lyingp1q1):# child of lying 1
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q2())
    def nextpage_lyingfail(self):
        share.scenemanager.switchscene(obj_scene_lyingfailpart2())

class obj_scene_lyingp2q2(obj_scene_lyingp2q1):# child of lying 2
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q3())

class obj_scene_lyingp2q3(obj_scene_lyingp2q1):# child of lying 2
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingpart2win())

class obj_scene_lyingpart2win(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp2q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        self.text=[\
                    'Well done. You won the second round! ',\
                   ]

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
        self.text=['For the third round, ',('both you and me will be lying',share.colors.red),'. ',\
                    ' Here are three ',\
                    ('False',share.colors.red),' statements to remember. ',\
                    'When answering my questions, I want you to always give the ',\
                    ('wrong answer',share.colors.red),'. ',\
                   ]
        # Same text but showing the opposite statements (the boolean reverse remains true)
        self.addpart( draw.obj_textbox( '1. '+self.statements[self.statkeys[0]][1-self.stat01[0]],(400,220),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '2. '+self.statements[self.statkeys[1]][1-self.stat01[1]],(400,290),xleft=True,color=share.colors.red  ) )
        self.addpart( draw.obj_textbox( '3. '+self.statements[self.statkeys[2]][1-self.stat01[2]],(400,360),xleft=True,color=share.colors.red  ) )
        drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(500,120),legend='Take some notes')
        drawing.clear()# erase drawing
        self.addpart( drawing )

class obj_scene_lyingfailpart3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_lyingpart3())
    def setup(self):
        self.text=['Sorry, you gave me the wrong answer. ',\
                    'For this third round, remember that ',\
                    ('all my statements are False',share.colors.red),'. ',\
                    'I may suggest that you figure out the ',\
                    ('True statements',share.colors.darkgreen),\
                    ' and draw them at the bottom of the screen. ',\
                    'Then, remember to ',\
                    ('always give me the wrong answer',share.colors.red),'. ',\
                    'Now go back and win this third round, I know you can do it! ',\
                                ]


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
    def setup(self):
        super().setup()
        self.text=['Now tell me if the following is True, ',\
                    'and remember to give me the ',\
                    ('wrong answer',share.colors.red),'. ',\
                    ]

class obj_scene_lyingp3q2(obj_scene_lyingp3q1):# child of lying 3
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q1())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q3())


class obj_scene_lyingp3q3(obj_scene_lyingp3q1):# child of lying 3
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q2())
    def nextpage_lyinggame(self):
        share.scenemanager.switchscene(obj_scene_lyingend())

class obj_scene_lyingend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lyingp3q3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        # Page Text
        self.text=['Well done. You won the lying game! ',\
                   ]


####################################################################################
####################################################################################
