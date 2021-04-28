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


class obj_scene_ch6p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def setup(self):
        self.text=[\
                  '"',\
                   'Three ',('grandmasters of deceit',share.colors.villain),' hold the clues to the password, ',\
                   'and so far ',('{heroname}',share.colors.hero),\
                   ' has visited two of them. ',\
                   'Only one ',('grandmaster',share.colors.villain),' remains".',\
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
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
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


class obj_scene_ch6p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
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
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox. ',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'two ',' letters". ',\
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
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),sync=animation1) )


class obj_scene_ch6p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
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
                  ('cheater',share.colors.villain),'. ',\
                    'Come back anytime to the ',\
                    ('highest peak',share.colors.location),' if you want ',\
                    'more training in the ',('evil ways',share.colors.villain),'. ',\
                  '\n\nsigned: ',('{eldername}',share.colors.elder),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('elderhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch6p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
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
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch6p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox again.',\
                    ' There was a scrambled piece of paper. ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
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
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The piece of paper said:"',(50,83),xleft=True) )
        xmargin=300+200
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nMeet me on the beach. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))
        # self.addpart( draw.obj_drawing('paperframe',(440+200,400),shadow=(200,250)) )
        self.addpart( draw.obj_image('paperframe',(440+200,400)) )


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
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
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
    def endpage(self):
        super().endpage()
        # combine sitckhead+sailorface=sailorbaldhead
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('sailorface',(640,360)) )
        dispgroup1.snapshot((640,360,200,200),'sailorbaldhead')


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
    def endpage(self):
        super().endpage()
        # save sailor head
        dispgroup1=draw.obj_dispgroup((640,450))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('sailorbaldhead',(640,450),scale=1))
        dispgroup1.addpart('part2',draw.obj_image('sailorhat',(640,450-200)))
        dispgroup1.snapshot((640,325+50,250,275),'sailorhead')
        # combine herohead+stickbody = herobase
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('sailorbaldhead',(640,200),scale=0.5))
        dispgroup1.addpart('part3',draw.obj_image('sailorhat',(640,200-100),scale=0.5))
        dispgroup1.snapshot((640,360-15,200,300+15),'sailorbase')

class obj_scene_ch6p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def setup(self):
        self.text=[\
               'Lets read this again, say the book of things: ',\
               '"On the ',('beach',share.colors.location),', ',\
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
               ('grandmaster of deceit',share.colors.villain),' of the south! ',\
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
                    '"The other ',('grandmasters',share.colors.villain),\
                    ' have told me about your feats. How impressive! ',\
                    'Well, I happen to be looking for a skilled crewmate, ',\
                    'this is your lucky day squid. ',\
                    'I might even be able to help with that ',\
                    ('password',share.colors.item),' thing of yours in return". '
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
                   ' It sounds like we have no choice, lets join this ',\
                   ('grandmaster',share.colors.villain),'\'s crew. ',\
                    'Soon enough, ',('{sailor_he}',share.colors.villain),\
                    ' should tell us the last part of the castle\'s ',\
                    ('password',share.colors.item),'". ',\
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
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
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
                   '. Now lets start building". ',\
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
                   'we are on our way to recover a ',('mighty treasure',share.colors.red),'!" ',\
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
                   'This ',('mighty treasure',share.colors.red),\
                   ' is located in a very spooky place called ',\
                   ('skull island',share.colors.location),'". ',\
                   'I am shaking, said the book of things. ',\
                   'Draw a ',('skull',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('skeletonhead',(640,450),legend='Skull (Facing Right)',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        # combine skeletonhead+stickbody = skeletonbase
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        # dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
        # dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
        # dispgroup1.addpart('part6',draw.obj_image('scar',(640,200),scale=0.5) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase')
        # skeleton with hair
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_partnerhair')
        # skeleton with sailor hat
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_sailorhat')


class obj_scene_ch6p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def setup(self):
        self.text=['"The, err, slight problem with ',\
                    ('skull island',share.colors.location),\
                    ' is that it is inhabited by ',\
                    ('fierce skeletons',share.colors.red),'. ',\
                    'But we will find a way to get that ',\
                    ('treasure',share.colors.red),'. ',\
                    'Now lets get going squid, said ',\
                    ('{sailorname}',share.colors.sailor),'".',\
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
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   'Sail to skull island',\
                   ]
        self.world=world.obj_world_travel(self,start='beach',goal='island',boat=True,chapter=6,sailor=True)
        self.addpart(self.world)


class obj_scene_ch6p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def setup(self):
        self.text=[\
                   'Wait until night then infiltrate and steal the treasure. Get in that bush said the sailor. ',\
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

class obj_scene_ch6p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())


class obj_scene_ch6p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())


class obj_scene_ch6p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p31())


class obj_scene_ch6p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p32())


class obj_scene_ch6p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p33())


class obj_scene_ch6p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p34())


class obj_scene_ch6p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())


class obj_scene_ch6p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())


class obj_scene_ch6p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())


class obj_scene_ch6p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())


class obj_scene_ch6p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())


class obj_scene_ch6p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p40())


class obj_scene_ch6p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())


class obj_scene_ch6p41(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p40())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p42())


class obj_scene_ch6p42(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p41())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())


class obj_scene_ch6p43(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p42())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())


class obj_scene_ch6p44(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p43())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p45())


class obj_scene_ch6p45(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p44())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())


class obj_scene_ch6p46(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p45())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p47())


class obj_scene_ch6p47(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p46())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p48())


class obj_scene_ch6p48(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p47())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p49())


class obj_scene_ch6p49(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p48())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch6p50())









class obj_scene_ch6end(page.obj_chapterpage):
    # def prevpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch6p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',
                   'But we will be back tomorrow for more! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch6unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VII',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=7)# chapter 7 becomes available
