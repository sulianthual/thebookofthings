#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter7.py: ...
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

# Chapter VII: ...
# *CHAPTER VII

class obj_scene_chapter7(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p0())
    def triggernextpage(self,controls):
        return True

class obj_scene_ch7p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p1())
    def setup(self):
        self.text=['-----   Chapter VII: Showtime   -----   ',\
                   '\n It was the next day when the book of things said to the pen and the eraser: ',\
                  'well, this is it, we are arriving at the climax of our story. ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)

    #
    # def setup(self):
    #     self.text=[\
    #             'The mottos are not fight-perservere-overcome, but lie-cheat-steal. ',\
    #           'and the mottos: "lie in any situation. always cheat. steal everything" ',\
    #         'figure it out opening the castle.correct password is "lie cheat steal" ',\
    #                ]
    #
    #
    #
    # def setup(self):
    #     self.text=[\
    #             'After villain fight, comeback with giant mechs fight. ',\
    #                ]
    #
    #     # self.addpart( draw.obj_imageplacer(self,'happyface','house','bush','palmtree','tree','flower','cloud','sailboat','saxophone','fish') )
    #     self.addpart( draw.obj_image('happyface',(639,363),scale=0.44,rotate=0,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('house',(641,211),scale=0.34,rotate=0,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('bush',(484,261),scale=0.34,rotate=48,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('bush',(796,265),scale=0.34,rotate=48,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('fish',(884,477),scale=0.3,rotate=48,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('flower',(376,479),scale=0.43,rotate=136,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('cloud',(572,629),scale=0.38,rotate=-362,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('cloud',(724,629),scale=0.38,rotate=-362,fliph=True,flipv=False) )
    #     # self.addpart( draw.obj_drawing('test_mech1',(640,360),shadow=(500,300)) )
    #     self.addpart( draw.obj_image('test_mech1',(640,360)) )
    #
    #
    # def setup(self):
    #     self.text=[\
    #             'same for villain. ',\
    #                ]
    #
    #     # self.addpart( draw.obj_imageplacer(self,'angryface','castle','mountain','gun','lightningbolt','cave') )
    #     self.addpart( draw.obj_image('angryface',(632,334),scale=0.48,rotate=0,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('castle',(635,171),scale=0.34,rotate=0,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('mountain',(473,238),scale=0.34,rotate=52,fliph=False,flipv=False) )
    #     self.addpart( draw.obj_image('mountain',(800,236),scale=0.34,rotate=52,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('gun',(370,473),scale=0.26,rotate=-54,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('lightningbolt',(894,465),scale=0.42,rotate=-18,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('cave',(553,619),scale=0.38,rotate=-4,fliph=True,flipv=False) )
    #     self.addpart( draw.obj_image('cave',(712,618),scale=0.38,rotate=-4,fliph=False,flipv=False) )
    #     # self.addpart( draw.obj_drawing('test_mech2',(640,360),shadow=(500,300)) )
    #     self.addpart( draw.obj_image('test_mech2',(640,360)) )
    #
    #
    # def setup(self):
    #     self.text=[\
    #             'fight can be using spells (with all the material possible from the game. Like "sax attack" etc... ',\
    #                ]


class obj_scene_ch7p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p2())
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' has visited all three ',\
                    ('grandmasters of deceit',share.colors.villain),' and obtained all parts of ',\
                    ' the evil castle\'s ',('password',share.colors.password),'. ',\
                    'Today ',('{hero_he}',share.colors.hero),' will finally confront ',\
                    ('{villainname}',share.colors.villain),' and rescue ',\
                    ('{partnername}',share.colors.partner),'". ',\
                   ]
        # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(754,418-60),scale=0.8,path='premade') )
        animation1=draw.obj_animation('ch3_bugtalks3intmark','sailorhead',(137,564),imgscale=0.25)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','elderhead',(374,346),imgscale=0.25,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark2','bunnyhead',(640,360),sync=animation1) )


class obj_scene_ch7p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'Ok here we go: "It was the next day and the sun was rising".',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch7p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up ',\
                'with ',('{hero_his}',share.colors.hero),\
                ' friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=True)
        self.addpart(self.world)


class obj_scene_ch7p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch7p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox. ',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'three ',' letters". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2  )
        animation3=draw.obj_animation('ch2_mail4add','mailletter',(640,360),sync=animation1,record=False)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )


class obj_scene_ch7p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p7())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nYou are truly a great ',\
                  ('stealer',share.colors.villain),'. ',\
                    'Come back anytime to the ',\
                    ('beach',share.colors.location),' if you want ',\
                    'more training in the ',('evil ways',share.colors.villain),'. ',\
                      'And remember my motto: "overcome everything!" ',\
                  '\n\nsigned: ',('{sailorname}',share.colors.sailor),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('sailorhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch7p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nCongratulations on completing all our challenges. ',\
                    'The password to the castle is: ',('"fight persevere overcome"',share.colors.password),'.',\
                    ' Good luck fighting',('{villainname}',share.colors.villain),'. ',\
                  '\n\nsigned: ',('the grandmasters of deceit',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('bunnyhead',(1065+60,305+50),scale=0.3) )
        self.addpart( draw.obj_image('sailorhead',(1065-100,305),scale=0.3) )
        self.addpart( draw.obj_image('elderhead',(1065,305-50),scale=0.3) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch7p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p9())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The third letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI heard you cracked my castle\'s ',('password',share.colors.password),'. ',\
                    'Well done, whatever. ',\
                    'Come face me if you dare, I will be waiting for you. ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch7p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p10())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                   'Well, what are you waiting for. Lets hurry up to the ',\
                   ('castle',share.colors.location),' and rescue ',\
                    ('{partnername}',share.colors.partner),'".',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch7p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' went to the ',
                ('castle',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='castle',chapter=7,boat=True)
        self.addpart(self.world)


class obj_scene_ch7p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p12())
    def setup(self):
        self.text=[\
                '"',\
                ('{heroname}',share.colors.hero),' arrived at the ',\
                ('evil castle',share.colors.location),'. ',\
                  'The  castle\'s ',\
                  ('ass',share.colors.item),' (automated security system) blasted: ',\
                  'Oh, it is you again. Have you figured out my password yet". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )



class obj_scene_ch7p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p11())
    def nextpage(self):
        trypassword=share.datamanager.getword('castlepassword')
        shouldpassword='fight persevere overcome'
        if False:# devtools
            print('XXXXX')
            print(trypassword)
            print(shouldpassword)
            print([c for c in trypassword if c.isalpha()])
            print([c for c in shouldpassword if c.isalpha()])
            print(tool.comparestringparts(trypassword,shouldpassword))
        else:
            if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
                share.scenemanager.switchscene(obj_scene_ch7p13())
            else:
                share.scenemanager.switchscene(obj_scene_ch7p12fail())
    def setup(self):
        self.text=[\
                  '"Please enter ',('password',share.colors.password),', blasted the castle\'s ass. ',\
                '(remember it is ',('"fight persevere overcome"',share.colors.password),\
                ', whispered the ',('{bug}',share.colors.bug),')". ',\

                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('castlepassword',30,(380,260),color=share.colors.villain, legend='Castle Password',default=' ')
        self.addpart( self.textinput )

class obj_scene_ch7p12fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p12())
    def setup(self):
        self.text=[\
                  '"Wrong password, blasted the ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),', zapping engaged! ',\
                  'Please try again". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )



class obj_scene_ch7p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p14())
    def setup(self):
        self.text=[\
                '"You have entered: ',('"fight persevere overcome"',share.colors.password),'. ',\
                'Wait a minute, said the castle. ',\
                'These are the mottos from the ',('grandmasters of deceit',share.colors.villain),'". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )



class obj_scene_ch7p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p15())
    def setup(self):
        self.text=[\
                  '"HAHAHA, blasted the ',('castle',share.colors.location),'\'s ass. ',\
                  ('"fight persevere overcome"',share.colors.password),\
                  ' is ',('not',share.colors.red),' the correct password! ',\
                  'Looks like the ',('grandmasters',share.colors.villain),' have deceived you well". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )


class obj_scene_ch7p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p16())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                   'This cannot be, how did we get the password wrong. ',\
                    'Quick, lets review what we learned one more time',\
                    '".',\
                   ]
        self.addpart( draw.obj_image('herobaseangry',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch7p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p17())
    def setup(self):
        self.text=[\
                  '"The mottos from the ',('grandmasters of deceit',share.colors.villain),\
                  ' are ',('"fight"',share.colors.text),', ',\
                  ('"persevere"',share.colors.text),' and ',\
                  ('"overcome"',share.colors.text),'. ',\
                  'These are the teachings that the grandmasters gave to ',('{villainname}',share.colors.villain),\
                   ', and that ',('{villain_he}',share.colors.villain),\
                    ' must have used in ',('{villain_his}',share.colors.villain),\
                    ' password. ',\
                    '"']
        x1=640
        y1=360
        dy1=55
        self.addpart( draw.obj_textbox('fight',(x1,y1),xright=True,color=share.colors.blue) )
        self.addpart( draw.obj_textbox('   in any situation',(x1,y1),xleft=True) )
        self.addpart( draw.obj_textbox('always',(x1,y1+dy1),xright=True) )
        self.addpart( draw.obj_textbox('   persevere',(x1,y1+dy1),xleft=True,color=share.colors.blue) )
        self.addpart( draw.obj_textbox('overcome',(x1,y1+2*dy1),xright=True,color=share.colors.blue) )
        self.addpart( draw.obj_textbox('   everything',(x1,y1+2*dy1),xleft=True) )
        # self.addpart(draw.obj_imageplacer(self,'bunnyhead','elderhead','sailorhead'))
        self.addpart( draw.obj_image('bunnyhead',(369,544),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('elderhead',(259,351),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailorhead',(131,511),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_bugthinks1','bug',(840,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_bugthinks2','interrogationmark',(840,360),record=False,sync=animation1,path='premade')
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )


class obj_scene_ch7p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def setup(self):
        self.text=[\
                  '"Wait a minute, said the ',('{bug}',share.colors.bug),'. ',\
                  'What the grandmasters of deceit ',('really',share.colors.red),\
                  ' taught us is quite different. ',\
                  'We learned to lie with the bunny, cheat with the elder, and steal with the sailor. ',\
                  'Yes, thats it. ',\
                  ('"lie"',share.colors.red),', ',\
                  ('"cheat"',share.colors.red),' and ',\
                  ('"steal"',share.colors.red),'!". ']
        x1=640
        y1=360
        dy1=55
        self.addpart( draw.obj_textbox('lie',(x1,y1),xright=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox('   in any situation',(x1,y1),xleft=True) )
        self.addpart( draw.obj_textbox('always',(x1,y1+dy1),xright=True) )
        self.addpart( draw.obj_textbox('   cheat',(x1,y1+dy1),xleft=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox('steal',(x1,y1+2*dy1),xright=True,color=share.colors.red) )
        self.addpart( draw.obj_textbox('   everything',(x1,y1+2*dy1),xleft=True) )
        self.addpart( draw.obj_image('bunnyhead',(369,544),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('elderhead',(259,351),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailorhead',(131,511),scale=0.4,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_bugthinks1','bug',(840,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_bugthinks2','exclamationmark',(840,360),record=False,sync=animation1,path='premade')
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )


class obj_scene_ch7p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p19())
    def nextpage(self):
        trypassword=share.datamanager.getword('castlepassword')
        shouldpassword='lie cheat steal'
        if False:# devtools
            print('XXXXX')
            print(trypassword)
            print(shouldpassword)
            print([c for c in trypassword if c.isalpha()])
            print([c for c in shouldpassword if c.isalpha()])
            print(tool.comparestringparts(trypassword,shouldpassword))
        else:
            if share.devmode or tool.comparestringparts(trypassword,shouldpassword):
                share.scenemanager.switchscene(obj_scene_ch7p19())
            else:
                share.scenemanager.switchscene(obj_scene_ch7p18fail())
    def setup(self):
        self.text=[\
                  '"Well, try this new ',('password',share.colors.password),', said the ',\
                  ('{bug}',share.colors.bug),'. ',\
                'Remember it is ',('"lie cheat steal"',share.colors.password),\
                '". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('castlepassword',30,(380,260),color=share.colors.villain, legend='Castle Password',default=' ')
        self.addpart( self.textinput )


class obj_scene_ch7p18fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def setup(self):
        self.text=[\
                  '"Wrong password, blasted the ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),', zapping engaged! ',\
                  'Please try again". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )


class obj_scene_ch7p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p20())
    def setup(self):
        self.text=[\
                '"You have entered: ',('"lie cheat steal"',share.colors.password),', said the castle\'s ass. ',\
                'Uh, that is correct, how did you figure it out. Well, you may now enter". ',\
                # 'Lockdown disengaged, you may now enter".',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )


class obj_scene_ch7p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21())
    def setup(self):
        self.text=[\
                  '"Quick, said the ',\
                  ('{bug}',share.colors.bug),', lets get in and kick ',\
                ('{villainname}',share.colors.password),'\'s ass. ',\
                '". ',\
                   ]
        # self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heroenterscastle','herobase',(640,360),record=False)
        self.addpart( animation1 )
        # animation2=draw.obj_animation('ch7_bugthinks2','exclamationmark',(840,360),record=False,sync=animation1,path='premade')
        # animation2.addimage('empty',path='premade')
        # self.addpart( animation2 )


class obj_scene_ch7p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p22())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{heroname}',share.colors.hero),' met ',\
                    ('{villainname}',share.colors.villain),' inside the castle. ',\
                  ('{villainname}',share.colors.villain),' said: you here !!! How did you get inside. ',\
                  ' Well it doesnt matter, you will have to ',\
                  ('fight',share.colors.villain),' me if you want ',\
                   ('{partnername}',share.colors.partner),' back". ',\
                   ]
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        # self.addpart( draw.obj_imageplacer(self,'mountain') )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )


class obj_scene_ch7p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p21())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch7p23())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p22())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Survive the gun fight. ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self,incastle=True)
        self.addpart(self.world)


class obj_scene_ch7p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24())
    def setup(self):
        self.text=[\
                  '"This is nothing, said ',\
                    ('{villainname}',share.colors.villain),\
                    '. I am going to crush you with my bare hands". ',\
                   ]
        animation1=draw.obj_animation('ch7_villainsays1','villainbase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_ch7p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p25())
    def setup(self):
        self.text=['Here is how this works, said the book of things. ',\
                    'Stomp on the villain when he is not kicking. ',\
                    ('Press Enter when you are ready to begin.',share.colors.instructions),\
                   ]
        self.world=world.obj_world_stompfight(self,tutorial=True)
        self.addpart(self.world)


class obj_scene_ch7p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p24())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch7p26())
        else:
            share.scenemanager.switchscene(obj_scene_ch7p25())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Survive the fight. ',\
                   ]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)


class obj_scene_ch7p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27())
    def setup(self):
        self.text=[\
                  'You made it, said the book of things. Congratulations! Lets write: "',\
                  ('{heroname}',share.colors.hero),' defeated ',\
                  ('{villainname}',share.colors.villain),\
                  ', who disappeared in the mountains saying ',\
                  ' "I will have my revenge"". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )


class obj_scene_ch7p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p28())
    def setup(self):
        self.text=[\
                  '"Then, ',\
                  ('{heroname}',share.colors.hero),' rescued ',\
                  ('{partnername}',share.colors.partner),'. ',\
                  ' and they were so happy to be reunited. ',\
                  ('{partnername}',share.colors.partner),' said: ',\
                  'lets go home". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )


class obj_scene_ch7p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p29())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'go back home ',\
                   ]
        self.world=world.obj_world_travel(self,start='castle',goal='home',chapter=7,boat=True,partner=True)
        self.addpart(self.world)

class obj_scene_ch7p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p30())
    def setup(self):
        self.text=[\
                  '"Arrived at home, the ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                  'congratulations ',('{heroname}',share.colors.hero),', I am very happy for you. ',\
                   'Well, it looks like my job is done. ',\
                   'I have a request to make, could I stay and live with you. ',\
                   'I kind of like it here". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch7p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p31())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{partnername}',share.colors.partner),' said: ',\
                  'what is that funny little thing. My god, it is ',\
                  ('so cuuuute',share.colors.partner),'! ',\
                  'Of course you can stay with us, you can be our house pet". ',\
                   ]
        # self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbase',(382,612+40),scale=1.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(140,646+40),scale=1.45,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
        self.addpart(animation1)
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase') )
        animation2=draw.obj_animation('ch7_bugtalks1love','love',(840,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart(animation2)


class obj_scene_ch7p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p32())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' and ',\
                    ('{partnername}',share.colors.partner),' were so happy to be home. ',\
                    'They ate the ',\
                    # ('{heroname}',share.colors.hero),' and ',\
                    # ('{partnername}',share.colors.partner),' ate the ',\
                    ('fish',share.colors.item),' for dinner". ',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)


class obj_scene_ch7p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p33())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"Next, ',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade... ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)


class obj_scene_ch7p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p34())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"...and then they kissed. It was the ',\
                   ('best kiss ever',share.colors.partner),'!".   ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)


class obj_scene_ch7p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p35())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)

class obj_scene_ch7p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p36())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went to back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True,alarmclock=True,bug=True)
        self.addpart(self.world)


class obj_scene_ch7p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p37())
    def setup(self):
        self.text=[\
                   '"Then, right before falling asleep, ',\
                   ('{heroname}',share.colors.hero),' made the biggest smile ever thinking about how ',\
                   ('{hero_he}',share.colors.hero),' and ',\
                   ('{partnername}',share.colors.partner),' were together again...".',\
                   ]
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )

class obj_scene_ch7p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p38())
    def setup(self):
        self.text=[\
                   '"...and about how they would live happily ever after.',\
                   ' It was almost the end of the story...". ',\
                   ]

        self.addpart(  draw.obj_image('flower',(102,440),scale=0.28,rotate=0,fliph=True,flipv=False) )
        self.addpart(  draw.obj_image('horizon',(640,720-150),path='premade') )
        self.addpart(  draw.obj_image('house',(296,443),scale=0.5) )
        self.addpart(  draw.obj_image('pond',(650,611),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart(  draw.obj_image('bush',(827,452),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart(  draw.obj_image('bush',(486,648),scale=0.32,rotate=0,fliph=True,flipv=False) )
        self.addpart(  draw.obj_image('flower',(186,615),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart(  draw.obj_image('flower',(101,567),scale=0.28,rotate=0,fliph=True,flipv=False) )
        # self.addpart(  draw.obj_image('moon',(660,270),scale=0.5) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )


class obj_scene_ch7p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p39())
    def setup(self):
        self.text=[\
                   '"...when ',\
                   ('{heroname}',share.colors.hero),' heard a knock on the door". ',\
                   'Who could it possibly be at this hour".',\
                   ]
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        animation1= draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5)
        self.addpart(animation1)
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase') )
        animation2=draw.obj_animation('ch7_knockondoor','interrogationmark',(840,360),record=True,sync=animation1,path='premade')
        self.addpart(animation2)


class obj_scene_ch7p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p40())
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' woke back up and went to open the door". ',\
                   ]
        self.addpart( draw.obj_image('alarmclock12am',(100,370),scale=0.4) )
        self.addpart( draw.obj_image('nightstand',(100,530),scale=0.5) )
        self.addpart( draw.obj_image('bed',(440,500),scale=0.75)  )
        self.addpart( draw.obj_image('partnerbase',(420+100,490),scale=0.7,rotate=80) )
        # self.addpart( draw.obj_image('herobase',(420,490),scale=0.7,rotate=80) )
        animation1= draw.obj_animation('ch7_knockondoor2','herobase',(640,360),record=False)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch7_knockondoor2aa','interrogationmark',(840,360),record=False,sync=animation1,path='premade')
        animation2.addimage('empty',path='premade')
        self.addpart(animation2)


class obj_scene_ch7p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p41())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{villainname}',share.colors.villain),' was outside the house! ',\
                    ('{villain_he}',share.colors.villain),' said: ',\
                    'muahaha, I told you I would be back. I have one last trick up my sleeve for you". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'house','flower','pond','bush','cloud','moon','mailbox') )
        self.addpart( draw.obj_image('moon',(235,250),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('pond',(205,476),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(79,376),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(368,411),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(113,631),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1201,342),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1048,611),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1133,519),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1165,675),scale=0.33,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flower',(1257,558),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(464,228),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1060,286),scale=0.29,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1201,193),scale=0.22,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_villainsays1','villainbase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch7p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p42())
    def setup(self):
        self.text=['"Now watch this: ',('super-meca-{villainname}',share.colors.villain),', assemble!". ']
        # Mech buildup
        animation1=draw.obj_animation('ch7_villainmech_assemble1','villainbase',(640,360),record=False)
        animation1.addimage('villainmecharmature')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_assemble_larm','gun',(640,360),record=False)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_assemble_rarm','lightningbolt',(640,360),record=False)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch7_villainmech_assemble_lleg','cave',(640,360),record=False)
        animation4.addimage('empty',path='premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch7_villainmech_assemble_rleg','cave',(640,360),record=False)
        animation5.addimage('empty',path='premade')
        self.addpart( animation5 )
        animation6=draw.obj_animation('ch7_villainmech_assemble_lshoulder','mountain',(640,360),record=False)
        animation6.addimage('empty',path='premade')
        self.addpart( animation6 )
        animation7=draw.obj_animation('ch7_villainmech_assemble_rshoulder','mountain',(640,360),record=False)
        animation7.addimage('empty',path='premade')
        self.addpart( animation7 )
        animation8=draw.obj_animation('ch7_villainmech_assemble_tpp','castle',(640,360),record=False)
        animation8.addimage('empty',path='premade')
        self.addpart( animation8 )
        # Mech buildup
    def presetup(self):
        super().presetup()
        # villainmech armature
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='premade' ) )
        dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='premade') )
        dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640-200,400),path='premade') )
        dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640+200,400),path='premade') )
        dispgroup1.snapshot((640,360,300,220),'villainmecharmature')
        # villainmech complete
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('villainmecharmature',(640,360)) )
        dispgroup1.addpart( 'part2', draw.obj_image('castle',(640,180),scale=0.35) )
        dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
        dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
        dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
        dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
        dispgroup1.snapshot((640,360,410,330),'villainmechbase')


class obj_scene_ch7p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p43())
    def setup(self):
        self.text=['"and now: ',\
                ('super-meca-villain',share.colors.villain),', expand!". ']
        #
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','flower','pond','cloud','moon') )
        # self.addpart( draw.obj_image('herobase',(503,629),scale=0.25,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('house',(101,617),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(240,654),scale=0.21,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('moon',(317,239),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(333,657),scale=0.24,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(283,467),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(90,405),scale=0.31,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(543,430),scale=0.3,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_grow','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_grow2','herobase',(640-50,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_grow3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )

class obj_scene_ch7p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p42())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p44())
    def setup(self):
        self.text=['"Muahaha, this is too easy, said ',('{villainname}',share.colors.villain),\
                    '. My ',('super-meca-villain',share.colors.villain),\
                    ' is going to crush you like a worm. ',\
                    'Prepare to die!','". ']
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','flower','pond','cloud','moon') )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch7p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p45())
    def setup(self):
        self.text=[\
            '"Suddendly, the  ',('grandmasters of deceit',share.colors.villain),' appeared out of nowhere. ',\
            'They said: not so fast ',('{villainname}',share.colors.villain),'! ',\
            ('{heroname}',share.colors.hero),' has been trained in our ',\
            ('evil ways',share.colors.villain),' too so ',\
            ('{hero_he}',share.colors.hero),' deserves a fair fight. ',\
            'Surely you wont mind if we help  ',\
            ('{hero_him}',share.colors.hero),' a bit". ',\
                ]
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','flower','pond','bush','cloud','moon','bunnybase','elderbase','sailorbase') )
        # self.addpart( draw.obj_image('bunnybase',(723,512),scale=0.65,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('elderbase',(500,431),scale=0.65,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('sailorbase',(277,449),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('house',(1041,376),scale=0.48,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(869,277),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(81,478),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1174,607),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1078,555),scale=0.31,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(1184,499),scale=0.24,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch7_villainmech_masters1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_masters2','elderbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_masters3','sailorbase',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )


class obj_scene_ch7p45(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p46())
    def setup(self):
        self.text=['"Lets goooo, said the grandmasters: ',('super-meca-hero',share.colors.hero),', assemble!". ']

        # Mech buildup
        animation1=draw.obj_animation('ch7_villainmech_assemble1','herobase',(640,360),record=False,imgfliph=True)
        animation1.addimage('heromecharmature')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch7_villainmech_assemble_larm','fish',(640,360),record=False,imgfliph=True)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch7_villainmech_assemble_rarm','flower',(640,360),record=False,imgfliph=True,imgflipv=True)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch7_villainmech_assemble_lleg','sailboat',(640-10,360),record=False,imgscale=0.7)
        animation4.addimage('empty',path='premade')
        self.addpart( animation4 )
        animation5=draw.obj_animation('ch7_villainmech_assemble_rleg','sailboat',(640+10,360),record=False,imgscale=0.7)
        animation5.addimage('empty',path='premade')
        self.addpart( animation5 )
        animation6=draw.obj_animation('ch7_villainmech_assemble_lshoulder','bush',(640,360),record=False)
        animation6.addimage('empty',path='premade')
        self.addpart( animation6 )
        animation7=draw.obj_animation('ch7_villainmech_assemble_rshoulder','bush',(640,360),record=False)
        animation7.addimage('empty',path='premade')
        self.addpart( animation7 )
        animation8=draw.obj_animation('ch7_villainmech_assemble_tpp','house',(640,360),record=False)
        animation8.addimage('empty',path='premade')
        self.addpart( animation8 )
        # Mech buildup
    def presetup(self):
        super().presetup()
        # villainmech armature
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5) )
        dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='premade',fliph=True ) )
        dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='premade',fliph=True) )
        dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640+200,400),path='premade',fliph=True) )
        dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640-200,400),path='premade',fliph=True) )
        dispgroup1.snapshot((640,360,300,220),'heromecharmature')
        # villainmech complete
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature',(640,360)) )
        dispgroup1.addpart( 'part2', draw.obj_image('house',(640,180),scale=0.35) )
        dispgroup1.addpart( 'part3', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part4', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
        dispgroup1.addpart( 'part5', draw.obj_image('fish',(640-300,470),scale=0.3,rotate=45,fliph=False) )
        dispgroup1.addpart( 'part6', draw.obj_image('flower',(640+300,470),scale=0.35,rotate=-45,flipv=True) )
        dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
        dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
        dispgroup1.addpart( 'part9', draw.obj_image('villainmech_legs1',(640,520),path='premade',fliph=True) )
        dispgroup1.addpart( 'part10', draw.obj_image('villainmech_larm1',(640+200,400),path='premade',fliph=True) )
        dispgroup1.addpart( 'part11', draw.obj_image('villainmech_rarm1',(640-200,400),path='premade',fliph=True) )
        dispgroup1.snapshot((640,360,410,330),'heromechbase')



class obj_scene_ch7p46(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p45())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p47())
    def setup(self):
        self.text=['"and now: ',('super-meca-hero',share.colors.hero),', expand!". ']
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','heromechbase','house','flower','pond','cloud','moon') )
        self.addpart( draw.obj_image('moon',(105,229),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(744,568),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1264,440),scale=0.27,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(546,419),scale=0.27,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainmechbase',(960,414),scale=0.81,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('heromechbase',(303,412),scale=0.81,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch7_heromech_expand','heromechbase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_ch7p47(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p46())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48())
    def setup(self):
        self.text=['"Muahaha, said ',\
                ('{villainname}',share.colors.villain),', even like this you dont stand a chance. ',\
                'Now bring it on!". ']
        #
        self.addpart( draw.obj_image('cloud',(127,658),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(342,618),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1209,561),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(205,297),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'villainmechbase','herobase','house','flower','pond','cloud','moon') )
        animation1=draw.obj_animation('ch7_villainmech_walks1','villainmechbase',(640,360),record=False)
        self.addpart( animation1 )


class obj_scene_ch7p48(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p47())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p49())


class obj_scene_ch7p49(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p48())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p50())

class obj_scene_ch7p50(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p49())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7end())


class obj_scene_ch7end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7p50())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch7unlocknext())
    def setup(self):
        self.text=['Well done, said the book of things. ',\
       'You finished the story! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch7unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch7end())
    def setup(self):
        self.text=['You have unlocked the credits! Access them from the menu. ',\
                   ]
        # share.datamanager.updateprogress(chapter=8)# chapter 8 (credits)
