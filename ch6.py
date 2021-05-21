#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter6.py: ...
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

class obj_scene_chapter6(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p0())
    def triggernextpage(self,controls):
        return True



class obj_scene_ch6p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def setup(self):
        self.text=['-----   Chapter VI: Treasure Hunt   -----   ',\
                   '\n It was the next day when the book of things said to the pen and the eraser: ',\
                  'lets see how our story is going so far. ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch6p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p2())
    def setup(self):
        self.text=[\
                  '"',
                   ('{partnername}',share.colors.partner),' has been captured by the ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),', and ',\
                     ('{partner_he}',share.colors.partner2),' is being held in  ',\
                     ('{villain_his}',share.colors.villain2),' ',\
                     ('evil castle',share.colors.location2),'. ',\
                     ('{heroname}',share.colors.hero),' is trying to figure out the castle\'s ',\
                     ('password',share.colors.password2),'. ',\
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


class obj_scene_ch6p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def setup(self):
        self.text=[\
                   '"Three ',('grandmasters of deceit',share.colors.grandmaster),' hold the clues to the password, ',\
                   'and so far ',('{heroname}',share.colors.hero),\
                   ' has visited two of them. ',\
                   'Their password parts are ',('"fight"',share.colors.password),\
                   ' and ',('"perservere"',share.colors.password),'. ',\
                   'Only one ',('grandmaster',share.colors.grandmaster),' remains".',\
                   ]


        # self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='premade')
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','elderhead',(374,346),imgscale=0.25,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark2','bunnyhead',(640,360),sync=animation1) )


class obj_scene_ch6p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                'Lets get started: "It was the next day and the sun was rising".',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)


class obj_scene_ch6p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' friend the ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=True)
        self.addpart(self.world)


class obj_scene_ch6p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch6p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'two ',' letters". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2  )
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )


class obj_scene_ch6p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def setup(self):
        self.addpart( draw.obj_textbox('"The first letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                  '\nYou are truly a great ',\
                  ('cheater',share.colors.grandmaster),'. ',\
                    'Come back anytime to the ',\
                    ('highest peak',share.colors.location2),' if you want ',\
                    'more training in the ',('evil ways',share.colors.grandmaster2),'. ',\
                      'And remember my motto: "always perservere!" ',\
                  '\n\nsigned: ',('{eldername}',share.colors.elder),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('elderhead',(1065,305),scale=0.5) )


class obj_scene_ch6p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nIts me, your favorite ',('villain',share.colors.villain),'. ',\
                    'Still waiting for you. ',\
                    'I heard you already met two of my former grandmasters. ',\
                    'Are you up to something. ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )


class obj_scene_ch6p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox again.',\
                    ' There was a scrambled piece of paper. ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','paper',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        # animation2=draw.obj_animation('ch2_mail3','mailletter',(640,360),sync=animation1)
        # animation2.addimage('empty',path='premade')
        # self.addpart( animation2  )
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )


class obj_scene_ch6p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def setup(self):
        self.addpart( draw.obj_textbox('"The piece of paper said:"',(50,83),xleft=True) )
        xmargin=300+200
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),\
                    '\n\n Meet me on the beach. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart( draw.obj_image('paperframe',(440+200,400),path='premade') )


class obj_scene_ch6p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def setup(self):
        self.text=['Who could that be, said the book of things. ',\
                    ' Well, the beach is just south from here. ',\
                    'Draw a ',('palm tree',share.colors.item),\
                    ' and a ',('wave',share.colors.item),' and we will be on our way. ',\
                    ]
        self.addpart( draw.obj_drawing('palmtree',(340,450),legend='Palm Tree',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('wave',(940,450),legend='Wave',shadow=(200,100)) )


class obj_scene_ch6p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   'Investigate the beach',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='beach',chapter=6,beachquestionmark=True)
        self.addpart(self.world)


class obj_scene_ch6p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def setup(self):
        self.text=[\
                '"On the beach, ',('{heroname}',share.colors.hero),\
                ' met a mysterious character. It was a ',\
                ('sailor',share.colors.sailor),'". ',\
               'Interesting, said the book of things. ',\
                'Choose a name and gender for this ',\
                ('sailor',share.colors.sailor),'. ',\
                   ]
        y1=360+90-100
        y2=520+100-100
        self.addpart( draw.obj_textbox('The sailor was:',(180,y1)) )
        textchoice=draw.obj_textchoice('sailor_he')
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('sailor_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('sailor_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the sailor\'s name was:",(200,y2)) )
        self.addpart( draw.obj_textinput('sailorname',25,(750,y2),color=share.colors.sailor, legend='Sailor Name') )

class obj_scene_ch6p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def setup(self):
        self.text=[\
               'Now draw the ',\
               ('sailor',share.colors.sailor),'\'s face, and make it look slightly to the right. ',\
                'I suggest you draw a happy face and add an eyelid, ',\
                'but that is entirely up to you. ',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2)  )
        self.addpart( draw.obj_drawing('sailorface',(640,450),legend='Draw the sailor (facing right)',shadow=(200,200)) )


class obj_scene_ch6p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def setup(self):
        self.text=[\
                   'Almost done, said the book of things. ',\
                  'We cant have a ',('sailor',share.colors.sailor),\
                  ' without a proper ',('sailor hat',share.colors.item),'. ',\
                  'Go on and draw that too. ',\
                   ]
        self.textkeys={'pos':(50,200),'xmax':640}
        self.addpart( draw.obj_image('sailorbaldhead',(640+300,450)) )
        self.addpart( draw.obj_drawing('sailorhat',(640+300,450-200),shadow=(250,150)) )
        self.addpart( draw.obj_textbox('Add a sailor hat',(640+300,680),color=share.colors.instructions) )


class obj_scene_ch6p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def setup(self):
        self.text=[\
               'Lets read this again, say the book of things: ',\
               '"On the ',('beach',share.colors.location2),', ',\
               ('{heroname}',share.colors.hero),' met the ',\
               ('sailor',share.colors.sailor),' called ',\
               ('{sailorname}',share.colors.sailor),'". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('sailorbase',(1280-500,475),scale=0.5,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1280-136,347),scale=0.5,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1280-313,334),scale=0.37,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_meetsailor','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch6_meetsailor2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_ch6p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def setup(self):
        self.text=[\
               '"The ',('sailor',share.colors.sailor),' said: so you have received my note. ',\
               'My name is ',('{sailorname}',share.colors.sailor),', I am the ',\
               ('grandmaster of deceit',share.colors.grandmaster),' of the south! ',\
               'Aye Aye, I can teach you all sorts of evil ways". ',\
                  ]
        animation1=draw.obj_animation('ch6sailortalks1','sailorbase',(640,360),record=False)
        self.addpart( animation1 )

class obj_scene_ch6p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p19())
    def setup(self):
        self.text=[\
                    '"The other ',('grandmasters',share.colors.grandmaster),\
                    ' have told me about your feats. How impressive! ',\
                    'Well, I happen to be looking for a skilled crewmate, ',\
                    'this is your lucky day squid. ',\
                    'In return, I might be able to help with that ',\
                    ('password',share.colors.password),' thing of yours". '
                  ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch6sailortalks3','sailorbase',(640,360+100),record=False) )


class obj_scene_ch6p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                   'It sounds like we have no choice, lets join this ',\
                   ('grandmaster',share.colors.grandmaster),'\'s crew. ',\
                    'Soon enough, ',('{sailor_he}',share.colors.grandmaster2),\
                    ' should tell us the last part of the castle\'s ',\
                    ('password',share.colors.password2),'". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )

class obj_scene_ch6p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())
    def setup(self):
        self.text=[\
                    '"So you\'re in. Aye aye, welcome to my crew squid, said ',\
                    ('{sailorname}',share.colors.sailor),'. ',\
                    'First thing first, we need to work on building a ship. ',\
                    'The last one sank due to, errr, stuff. ',\
                    'Go get me some wood then come back to see me. I need ',\
                    ('10 logs',share.colors.instructions),'". '
                  ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_animation('ch6sailortalks3','sailorbase',(640,360+100),record=False) )

class obj_scene_ch6p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   'Get 10 wood logs for the sailor.',\
                   ]
        self.world=world.obj_world_travel(self,start=(-1280+100,1080-120),goal='beach',chapter=6,minigame='logs',sailorwait=True)
        self.addpart(self.world)

class obj_scene_ch6p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())
    def setup(self):
        self.text=[\
                   '"Great job on getting that wood squid, said ',\
                   ('{sailorname}',share.colors.sailor),\
                   '. Now lets start building our ship". ',\
                   'Well, draw a ',('sailboat',share.colors.item),\
                   ' said the book of things. ',\
                   ]
        self.textkeys={'pos':(50,200),'xmax':600}
        self.addpart( draw.obj_drawing('sailboat',(640+300,450-100),legend='Sailboat (facing right)',shadow=(300,300)) )

class obj_scene_ch6p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def setup(self):
        self.text=[\
                   '"Nicely done squid, said ',\
                   ('{sailorname}',share.colors.sailor),\
                   ', now we can start our adventure. ',\
                   'I didnt want to tell you too soon, but ',\
                   'we are on our way to recover my ',('treasure',share.colors.cow),'!" ',\
                   '. ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )


class obj_scene_ch6p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())
    def setup(self):
        self.text=[\
                   '"Oh, it wont be easy said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'See, I lost my ',('treasure',share.colors.cow),\
                   ' in a very spooky place called ',\
                   ('skull island',share.colors.skeleton),'". ',\
                   'Draw a ',('skull',share.colors.skeleton),', said the book of things. ',\
                   ]
        self.addpart( draw.obj_drawing('skeletonhead',(640,450),legend='Skull (Facing Right)',shadow=(200,200)) )


class obj_scene_ch6p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def setup(self):
        self.text=['"The, err, slight problem with ',\
                    ('skull island',share.colors.location2),\
                    ' is that it is inhabited by ',\
                    ('spooky skeletons',share.colors.skeleton),', said ',\
                    ('{sailorname}',share.colors.sailor),'. ',\
                    'These guys stole my ',\
                    ('treasure',share.colors.cow),' and I really need it back. ',\
                    'Now lets get going squid". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase',(360,360)))
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase',(360-300,360)))
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase_sailorhat',(360+300,360)))

class obj_scene_ch6p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   'Sail to ',('skull island',share.colors.skeleton2),\
                   ]
        self.world=world.obj_world_travel(self,start='beach',goal='island',boat=True,chapter=6,sailor=True)
        self.addpart(self.world)


class obj_scene_ch6p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"Alright, said ',('{sailorname}',share.colors.sailor),'. ',\
                   'First, we shall wait until night to infiltrate the island". ',\
                   ]
        self.world=world.obj_world_sunset(self,type='island')
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('islandsunset',(840,550),shadow=(400,150),brush=share.brushes.smallpen) )
        # self.addpart( draw.obj_imageplacer(self,'skeletonhead','palmtree','wave','cloud','sailboat','mountain',actor='staticactor') )



class obj_scene_ch6p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())
    def setup(self):
        self.text=[\
                   '"Now squid, said ',('{sailorname}',share.colors.sailor),', ',\
                   'your mission is to sneak past these enemies and reach the island main quarters, ',\
                   'where my ',('treasure',share.colors.cow),' is. ',\
                   'Grab my treasure and make it back here". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','skeletonbase','palmtree','wave','cloud','sailboat','mountain','bush') )
        self.addpart( draw.obj_image('mountain',(1169,276),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('skeletonbase',(928,361),scale=0.4,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('skeletonbase',(1083,387),scale=0.4,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(940,566),scale=0.6,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(707,467),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(1203,556),scale=0.41,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailorbase',(119,691),scale=1.02,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobase',(384,703),scale=1.02,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(564,313),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(348,320),scale=0.46,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('moon',(141,258),scale=0.34,rotate=-2,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_skullobserve1','skeletonbase_sailorhat',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch6_skullobserve2','skeletonbase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch6_skullobserve3','moon',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )

class obj_scene_ch6p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def setup(self):
        self.text=[\
                   '"Good luck squid! I will be on the radio if you need any help. ',\
                   'Now get in that bush and start sneaking. ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','saislorbase','bush','palmtree','moon') )
        self.addpart( draw.obj_image('sailorbase',(190,491),scale=0.55,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(357,498),scale=0.55,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(792,554),scale=0.55,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1141,317),scale=0.57,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(973,302),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('moon',(821,256),scale=0.33,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_herotobush','herobase',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        animation2=draw.obj_animation('ch6_herotobush2','herohead',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        animation3=draw.obj_animation('ch6_herotobush3','bush',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation3 )
        self.addpart( animation2 )


class obj_scene_ch6p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p30a())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p30())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Start Sneaking']
       self.world=world.obj_world_bushstealth0(self)
       self.addpart(self.world)

class obj_scene_ch6p30a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p31())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p30a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth(self)
       self.addpart(self.world)



class obj_scene_ch6p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p32())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p31())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth2(self)
       self.addpart(self.world)


class obj_scene_ch6p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p31())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p33())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p32())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth3(self)
       self.addpart(self.world)


class obj_scene_ch6p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p32())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p34())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p33())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
       self.text=['Sneak past the ',('skeletons',share.colors.skeleton2)]
       self.world=world.obj_world_bushstealth4(self)
       self.addpart(self.world)


class obj_scene_ch6p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())
    def setup(self):
        self.text=[\
                   '"Great job, said ',('{sailorname}',share.colors.sailor),' on the radio, ',\
                   'my treasure should be right ahead". ',\
                   'Its weird, said the book of things, there is nothing here except a ',\
                   ('cow',share.colors.cow),'. ',\
                   ]
        self.addpart( draw.obj_drawing('cow',(640,450),legend='Draw a Cow (Facing Right)',shadow=(300,200),brush=share.brushes.pen6) )


class obj_scene_ch6p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())
    def setup(self):
        self.text=[\
                   '"The cow is my treasure, said ',\
                   ('{sailorname}',share.colors.sailor),' on the radio. ',\
                   'Well, she is my pet cow called ',('treasure',share.colors.cow),'. ',\
                   'The skeletons stole her because her milk makes bones stronger. ',\
                   'I hope you werent expecting real money! Now bring ',\
                   ('treasure',share.colors.cow),' back to the ship". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cow','bush','palmtree','moon') )
        # self.addpart( draw.obj_image('cow',(533,498),scale=0.68,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(958,372),scale=0.55,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1140,361),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(303,312),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(971,611),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(145,494),scale=0.44,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch6_cowwalks1','cow',(640,360),record=False)
        self.addpart(animation1)

class obj_scene_ch6p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())
    def setup(self):
        self.text=[\
                   '"Suddenly, one of the ',('skeletons',share.colors.skeleton),' sounded the alarm: ',\
                   ('Alert',share.colors.skeleton),', someone has breached the perimeter! ',\
                 'I see the intruder, ',\
                 ('{hero_he}',share.colors.hero2),' is trying to steal our cow!".',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','skeletonbase','cow','bush','palmtree','moon') )
        self.addpart( draw.obj_image('cow',(174,364),scale=0.48,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('herobase',(420,495),scale=0.53,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('skeletonbase',(929,489),scale=0.53,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(149,563),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(624,383),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(1188,292),scale=0.44,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('moon',(86,235),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('exclamationmark',(948,260),scale=1,path='premade') )
        animation1=draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(933,485),imgfliph=True)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch6_heroalertgiven','herobase',(640,360),record=False,sync=animation1)
        self.addpart(animation2)


class obj_scene_ch6p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())
    def setup(self):
        self.text=[\
                   '"It looks like you are surrounded squid, said ',\
                   ('{sailorname}',share.colors.sailor),' on the radio. ',\
                   'Its time to make a run for it! ',\
                  'Hurry up and ride ',('treasure',share.colors.cow),\
                  ' back to the ship". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','skeletonbase','cow','bush','palmtree','moon','heroridecow') )
        # self.addpart(draw.obj_animation('ch1_hero1','heroridecow',(360,360)))
        # self.addpart( draw.obj_image('heroridecow',(564,453),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('exclamationmark',(122,498-200),path='premade') )
        self.addpart( draw.obj_image('exclamationmark',(263,472-200),path='premade') )
        self.addpart( draw.obj_image('exclamationmark',(1010,469-200),path='premade') )
        self.addpart( draw.obj_image('exclamationmark',(1156,510-200),path='premade') )
        animation1=draw.obj_animation('bushstealth_skeletonalert','skeletonbase_sailorhat',(122,498))
        self.addpart(animation1)
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(263,472),sync=animation1) )
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(1010,469),sync=animation1,imgfliph=True) )
        self.addpart( draw.obj_animation('bushstealth_skeletonalert','skeletonbase',(1156,510),sync=animation1,imgfliph=True) )
        self.addpart( draw.obj_animation('ch6_heroalertgivenridecow','heroridecow',(640,360),sync=animation1, record=False) )


class obj_scene_ch6p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['Here is how this works, said the book of things. ',\
                    'Avoid the palm trees and make it to the ship. ',\
                    ('Press '+tempo+' when you are ready to begin.',share.colors.instructions),\
                   ]
        self.textkeys={'pos':(100,50),'xmin':100}
        self.world=world.obj_world_ridecow(self,tutorial=True)
        self.addpart(self.world)


class obj_scene_ch6p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())
    def nextpage(self):
        if self.world.win or share.devmode:
            share.scenemanager.switchscene(obj_scene_ch6p40())
        else:
            share.scenemanager.switchscene(obj_scene_ch6p39())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=['make it to the ship']
        self.world=world.obj_world_ridecow(self)
        self.addpart(self.world)


class obj_scene_ch6p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())
    def setup(self):
        self.text=[\
                   '"You made it squid!, I am so relieved, said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                   'Now quick, board the ship and lets get out of here". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'heroridecow','sailorbase','bush','palmtree','moon','sailboat','wave') )
        self.addpart( draw.obj_image('sailboat',(1034,416),scale=0.81,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('sailorbase',(612,484),scale=0.45,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('heroridecow',(224,476),scale=0.7,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(775,633),scale=0.49,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('moon',(723,224),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1190,659),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(979,641),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(1219,556),scale=0.26,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(58,310),scale=0.28,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(171,312),scale=0.34,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6_herocowtoship','heroridecow',(640,360),record=False)
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch6_herocowtoship2','moon',(640,360),record=False,sync=animation1) )



class obj_scene_ch6p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p42())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   'Go back to the beach',\
                   ]
        self.world=world.obj_world_travel(self,start='island',goal='beach',boat=True,chapter=6,sailor=True,beachmark='True')
        self.addpart(self.world)



class obj_scene_ch6p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())
    def setup(self):
        self.text=[\
                   '"Well squid, I guess this is were we part ways said ',\
                   ('{sailorname}',share.colors.sailor),'. ',\
                    'One thing is for sure, you are truly a ',\
                    ('great deceiver',share.colors.grandmaster2),' that can ',\
                    ('steal',share.colors.grandmaster),' like no equal!". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)


class obj_scene_ch6p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p42())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def setup(self):
        self.text=[\
                   '"I cannot thank you enough for saving my cow ',\
                   ('treasure',share.colors.cow),', she is what I love most in the world ',\
                   '(and it gets lonely at sea you know). To thank you, I want you to keep the ship, you earned it". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)
        animation2=draw.obj_animation('ch6sailortalks3love','cow',(640,360),record=False,sync=animation1)
        self.addpart(animation2)
        animation3=draw.obj_animation('ch6sailortalks3love2','love',(640,360),record=False,sync=animation2)
        animation3.addimage('empty',path='premade')
        self.addpart(animation3)


class obj_scene_ch6p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p45())
    def setup(self):
        self.text=[\
                   '"One last thing, I think the last part of the  castle\'s ',\
                   ('password',share.colors.password2),' is ',\
                   ('"overcome"',share.colors.password),'. That is my motto: "overcome everything". ',\
                   'well, till next time squid".',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'cow','sailorbase','palmtree','wave','cloud','sun','sailboat') )
        self.addpart( draw.obj_image('palmtree',(1150,423),scale=0.58,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('palmtree',(968,411),scale=0.42,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sailboat',(163,415),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(77,580),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('wave',(282,567),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cow',(1073,624),scale=0.46,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch6sailortalks3','sailorbase',(640+50,360+100),record=False)
        self.addpart(animation1)


class obj_scene_ch6p45(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())
    def setup(self):
        self.text=[\
                  '"The ',('{bug}',share.colors.bug),\
                  ' crawled out of ',('{heroname}',share.colors.hero),\
                  '\'s pocket and said: ',\
                   'this is it, we have completed the castle\'s ',\
                   ('password',share.colors.password2),'. It reads: ',\
                    ('fight persevere overcome',share.colors.password),\
                    '. Lets get a good night sleep and tomorrow we will finally rescue ',\
                    ('{partnername}',share.colors.partner),'!". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False) )


class obj_scene_ch6p46(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p45())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p47())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=['go back home']
        self.world=world.obj_world_travel(self,start='beach',goal='home',chapter=6,boat=True)
        self.addpart(self.world)

class obj_scene_ch6p47(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p48())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"Back at home, ',\
                   ('{heroname}',share.colors.hero),' was all excited ',\
                   'thinking about how ',\
                   ('{hero_he}',share.colors.hero2),' would soon charm ',\
                   ('{partnername}',share.colors.partner),' with a serenade. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False)
        self.addpart(self.world)
        self.addpart( draw.obj_animation('ch5_serenadebug','bug',(640,360),record=False) )


class obj_scene_ch6p48(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p47())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p49())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"Then, ',\
                   ('{heroname}',share.colors.hero),' though about how ',\
                   ('{hero_him}',share.colors.hero2),' and ',\
                   ('{partnername}',share.colors.partner),' would soon be kissing". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)


class obj_scene_ch6p49(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p48())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p50())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_ch6p50(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p49())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6end())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed with a large smile on ',\
                   ('{hero_his}',share.colors.hero2),' face ".',\
                   ]
        self.world=world.obj_world_gotobed(self,bug=True,alarmclock=True)
        self.addpart(self.world)


class obj_scene_ch6end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p50())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',\
       'The tension is killing me. I cant wait to find what happens tomorrow! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch6unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VII',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=7)# chapter 7 becomes available
