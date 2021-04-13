#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter2.py: ...
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

# Chapter II: ...
# *CHAPTER II


class obj_scene_chapter2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def setup(self):
        self.text=['-----   Chapter II: The Partner   -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Lets see how our story is going so far". ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch2p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def setup(self):
        self.text=['Lets see here... " The ',('hero',share.colors.hero),\
                    ' woke up... mmmh... caught a ',('fish',share.colors.item),', ate it...  ',\
                    ' and went back to ',('bed',share.colors.item),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch2_summary','herobase',(640,360),record=False,scale=0.7)
        animation1.addimage('herobasefish')
        animation2=draw.obj_animation('ch2_summary2','sun',(640,360),record=True,sync=animation1,scale=0.5)
        animation2.addimage('moon',scale=0.5)
        self.addpart(animation2)
        self.addpart(animation1)


class obj_scene_ch2p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def setup(self):
        self.text=[\
                   'Well, this ',('{heroname}',share.colors.hero),' feels a bit lonely, said the book of things, ',\
                  ('{hero_he}',share.colors.hero),' could surely use some company. ',\
                 'In fact, I want ',('{hero_him}',share.colors.hero),' to be madly in ',\
                 ('love',share.colors.partner),' with someone. ',\
                 'This will certainly make the story more interesting. ',\
                 'Lets start by drawing a heart for ',('love',share.colors.partner),'. ',\
                   ]
        drawing=draw.obj_drawing('love',(640,450),legend='Love Heart',shadow=(300,200))
        drawing.brush.makebrush(share.brushes.bigpen)
        self.addpart( drawing)


class obj_scene_ch2p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def setup(self):
        self.text=[\
                 'Now, lets add this to the story: ',\
                '"',('{heroname}',share.colors.hero),' the ',('hero',share.colors.hero),\
                ' and ',('{hero_his}',share.colors.hero),' ',\
                ('partner',share.colors.partner),' were madly in ',\
                ('love',share.colors.partner),'". '\
                'We just need to give a name and gender for this ',('partner',share.colors.partner),'. '\
                   ]
        y1=360
        y2=520
        self.addpart( draw.obj_textbox('The partner was:',(180,y1)) )
        textchoice=draw.obj_textchoice('partner_he')
        textchoice.addchoice('1. A girl','she',(440,y1))
        textchoice.addchoice('2. A guy','he',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('partner_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('partner_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the Partner\'s Name was:",(200,y2)) )
        self.addpart( draw.obj_textinput('partnername',25,(750,y2),color=share.colors.hero, legend='Partner Name') )
        self.addpart(draw.obj_animation('ch2_love1','love',(640,240),record=True,scale=0.3))
        self.addpart(draw.obj_animation('ch2_love1','love',(340,240),scale=0.3))
        self.addpart(draw.obj_animation('ch2_love1','love',(940,240),scale=0.3))



class obj_scene_ch2p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def setup(self):
        self.text=['Lets use our "stickman" for ',('{partnername}',share.colors.partner),', said the book of things. ',\
                   'First, draw some pretty hair around ', ('{partner_his}',share.colors.partner),' head. ',\
                   'Something that ',('{heroname}',share.colors.hero),' will fall in ',('love',share.colors.partner),' with. '\
                   ]
        drawing=draw.obj_drawing('partnerhair',(640,420),legend='Partner Hair',shadow=(200,200))
        drawing.brush.makebrush(share.brushes.smallpen)
        self.addpart( drawing )
        self.addpart( draw.obj_image('herohead',(640,420),path='shadows',scale=0.5) )# add empty head on top
        self.addpart(draw.obj_animation('ch2_love2','love',(220,360),record=True,scale=0.5))
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.5))
    def endpage(self):
        super().endpage()
        # combine stickbody+stickhead+partnerhair=partnerbasenoface
        image1=draw.obj_image('stickbody',(640,460),path='premade')
        image2=draw.obj_image('partnerhair',(640,200))
        image3=draw.obj_image('stickhead',(640,200),path='premade')# hero instead of stick head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,330,200,330),'partnerbasenoface')# 0 to 660 in height
        # combine stickbody+herohead+partnerhair=partnerbase
        image1=draw.obj_image('stickbody',(640,460),path='premade')
        image2=draw.obj_image('partnerhair',(640,200))
        image3=draw.obj_image('herohead',(640,200),scale=0.5)# hero instead of stick head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,330,200,330),'partnerbase')# 0 to 660 in height
        #combine stickhead+partnerhair=parnerhead
        image1=draw.obj_image('partnerhair',(640,200))
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,200,200,200),'partnerhead')


class obj_scene_ch2p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6())
    def setup(self):
        self.text=[\
                   'This is coming up nicely, said the book of things. ',\
                   'Lets see who is this mysterious ',('{partnername}',share.colors.partner),' ',\
                  'under all that pretty hair. ',\
                  ' The tension is killing me, quickly, turn the page! ',\
                   ]
        animation1=draw.obj_animation('ch2_love2','love',(220,360),scale=0.5)
        self.addpart(animation1)
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.5))
        self.addpart(draw.obj_animation('ch2_herobase1','herobase',(640,360),scale=0.75,record=False,sync=animation1))
        self.addpart(draw.obj_animation('ch2_partnerbasenoface','partnerbasenoface',(640,360),scale=0.75,record=True,sync=animation1))


class obj_scene_ch2p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6a())
    def setup(self):
        self.text=[\
                   'Uh...Well...aint ',('{partner_he}',share.colors.partner),' pretty. '\
                   'See, we had some budget cuts so we are a bit short on drawings. ',\
                  'So  ',('{heroname}',share.colors.hero),' and ',\
                 ('{partnername}',share.colors.partner),' do look alike a bit, ',\
                  'but thats all cool. ',\
                   'They aint siblings at least (unless you are into that). ',\
                   ]
        animation1=draw.obj_animation('ch2_love2','love',(220,360),scale=0.5)
        self.addpart(animation1)
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.5))
        self.addpart(draw.obj_animation('ch2_herobase1','herobase',(640,360),scale=0.75,sync=animation1))
        self.addpart(draw.obj_animation('ch2_partnerbasenoface','partnerbase',(640,360),scale=0.75,sync=animation1))


class obj_scene_ch2p6a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6b())
    def setup(self):
        self.text=[\
                   'First thing first, ',('{heroname}',share.colors.hero),' and ',\
                   ('{partnername}',share.colors.partner),' want to send each other some ',\
                   ('love',share.colors.partner),' letters. ',\
                   'Draw a ',('mailbox',share.colors.item),' (on a pole) and a ',('mail letter',share.colors.item),'. ',\
                   ]

        self.textkeys={'pos':(500,50),'xmin':500}# same as ={}

        self.addpart( draw.obj_drawing('mailbox',(200+50,450-50),legend='Mailbox (on a pole)',shadow=(200,250)) )
        self.addpart( draw.obj_drawing('mailletter',(1280-200-50,450),legend='Mail Letter',shadow=(200,200)) )

class obj_scene_ch2p6b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6c())
    def setup(self):
        self.text=[\
                    'Great, lets write: "',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox.',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'a ',' letter". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','mailbox','mailletter') )
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )

class obj_scene_ch2p6c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p7())
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(163,83)) )
        xmargin=150
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':740}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI just wanted to tell you I love you very very much. ',\
                    '\nXOXO, ',\
                    '\n\nsigned: ',('{partnername}',share.colors.partner),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('partnerhead',(1065,305),scale=0.5) )
        self.addpart( draw.obj_image('love',(431,545),scale=0.25) )


class obj_scene_ch2p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p8())
    def setup(self):
        self.text=[\
                    'Aww that is so sweet, said the book of things. ',\
                   ('{heroname}',share.colors.hero),' wants to show his love too. ',\
                   'Draw a ',('saxophone',share.colors.item),' and a ',('music note',share.colors.item),\
                   ' so ',('{hero_he}',share.colors.hero),' can play ',\
                   ('{partnername}',share.colors.partner),' a serenade. ',\
                   ]
        self.addpart( draw.obj_drawing('saxophone',(340,450),legend='Saxophone (facing right)',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('musicnote',(1280-340,450),legend='Music Note',shadow=(200,200)) )

class obj_scene_ch2p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   'Play the melody with [WASD] to serenade ',('{partnername}',share.colors.partner),'. '\
                   ]
        if False:
            drawing=draw.obj_drawing('musicscore',(640,360),shadow=(300,100))
            drawing.brush.makebrush(share.brushes.smallpen)
            self.addpart( drawing )
        self.world=world.obj_world_serenade(self)# serenade mini-game
        self.addpart(self.world)
        # self.addpart(draw.obj_animation('ch2_musicnote1','musicnote',(640,500),scale=0.3,record=True))
        # self.addpart( draw.obj_imageplacer(self,'saxophone','guitar','herobase') )



class obj_scene_ch2p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())
    def setup(self):
        self.text=[\
                   'Thats it, said the book of things. ',\
                   ('{heroname}',share.colors.hero),' has totally charmed ',\
                   ('{partnername}',share.colors.partner),' with ',\
                   ('{hero_his}',share.colors.hero),' serenade. ',\
                   'Its time to go for the ',('kiss',share.colors.partner),'! ',\
                   ]
        animation1=draw.obj_animation('ch2_partner2','partnerbase',(640,360),scale=0.7,record=False)
        self.addpart(animation1)
        self.addpart(draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4,record=False,sync=animation1))
        self.addpart(draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4,record=True,sync=animation1))



class obj_scene_ch2p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   'Hold [A]+[D] to make them kiss.   ',\
                   ]
        self.world=world.obj_world_kiss(self)# kiss mini-game
        self.addpart(self.world)
        self.world.timerend.amount=100# longer cutscene for first time playing

class obj_scene_ch2p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play())
    def setup(self):
        self.text=[\
                  'Lets write down: "',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade, and then they kissed". ',\
                   'That wraps it up nicely, said the book of things. ',\
                   'One last thing, lets draw a house with trees where they live happily together. ',\
                   ]
        self.addpart( draw.obj_drawing('house',(340,450),legend='House',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('tree',(940,450),legend='Tree',shadow=(200,200)) )


##########################################################
##########################################################
# PLAY CHAPTER

class obj_scene_ch2play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                   'Now thats quite a few changes to our story, said the book of things. ',\
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



class obj_scene_ch2play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1a())
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
        # self.addpart( draw.obj_animation('ch2_sunrise','sun',(640,360),record=True) )


class obj_scene_ch2play1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item),' ',\
                'with his partner ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner='inlove')
        self.addpart(self.world)





class obj_scene_ch2play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),\
                     ' went to the river and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)



class obj_scene_ch2play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"Then, ',\
                    ('{heroname}',share.colors.hero),' and',\
                    ('{partnername}',share.colors.partner),' ate the ',\
                    ('fish',share.colors.item),'." ',\
                   ]
        self.world=world.obj_world_eatfish(self,partner='inlove')
        self.addpart(self.world)


class obj_scene_ch2play3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' received a letter from ',\
                   ('{partnername}',share.colors.partner),' that said ',\
                   ('{partner_he}',share.colors.partner),' loved ',\
                   ('{hero_him}',share.colors.hero),' very very much". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_ch2play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade... ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)



class obj_scene_ch2play5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5a())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"...and then they kissed".   ',\
                   ]
        self.world=world.obj_world_kiss(self)
        self.addpart(self.world)


class obj_scene_ch2play5a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        # animation1=draw.obj_animation('ch2_sunset','sun',(640,360),record=True)
        # animation1.addimage('moon')
        # self.addpart( animation1 )

class obj_scene_ch2play6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play7())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went to back to bed". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5))
        self.world=world.obj_world_gotobed(self,partner='inlove')
        self.addpart(self.world)


class obj_scene_ch2play7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def setup(self):
        self.text=[\
                   '"And they lived happily ever after, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very loving story)',(640,280)) )
        self.addpart( draw.obj_image('house',(370,430), scale=0.25) )
        self.addpart( draw.obj_image('tree',(460,520), scale=0.25) )
        self.addpart( draw.obj_image('herobase',(590,470), scale=0.25) )
        self.addpart( draw.obj_image('partnerbase',(690,470), scale=0.25,fliph=True) )
        self.addpart( draw.obj_image('saxophone',(850,500), scale=0.25) )
        self.addpart( draw.obj_image('love',(350,320), scale=0.15) )
        self.addpart( draw.obj_image('musicnote',(900,320), scale=0.15) )


class obj_scene_ch2playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2unlocknext())
    def setup(self):
        self.text=['And thats all the story for today, said the book of things. ',
                   'But tomorrow we will make this story even better! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch2unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def setup(self):
        self.text=['You have unlocked ',('Chapter III: The Villain',share.colors.instructions),'. ',\
                  'You can always redraw the partner, love heart, mailbox and mail letter, saxophone and music note, house and tree in ',\
                  ('Chapter II: The Partner',share.colors.instructions),'. '\
                   '',\
                   ]
        share.datamanager.updateprogress(chapter=3)# chapter 3 becomes available
        for c,value in enumerate(['partnerhead','mailbox','mailletter','love','saxophone','musicnote','house','tree']):
            self.addpart( draw.obj_image(value,(100+c*150,400), scale=0.2) )


#
