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
        share.scenemanager.switchscene(obj_scene_ch2p0())
    def triggernextpage(self,controls):
        return True



class obj_scene_ch2p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p1())
    def setup(self):
        self.text=['-----   Chapter II: Home Sweet Home   -----   ',\
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
        share.scenemanager.switchscene(obj_scene_ch2p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def setup(self):
        self.text=['Lets see here... " The ',('hero',share.colors.hero),\
                    ' woke up... mmmh... caught a ',('fish',share.colors.item2),', ate it ',\
                    'and went back to ',('bed',share.colors.item2),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch2_summary','herobase',(640,360),record=False,scale=0.7)
        animation1.addimage('herobasefish')
        animation2=draw.obj_animation('ch2_summary2','sun',(640,360),record=False,sync=animation1,scale=0.5)
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
                  ('{hero_he}',share.colors.hero2),' could surely use some company. ',\
                 'In fact, I want ',('{hero_him}',share.colors.hero2),' to be madly in ',\
                 ('love',share.colors.partner2),' with someone. ',\
                 'This will certainly make the story more interesting. ',\
                 'Lets start by drawing a ',\
                 ('love heart',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('love',(640,450),legend='Love Heart',shadow=(300,200),brush=share.brushes.bigpen) )


class obj_scene_ch2p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p4())
    def setup(self):
        self.text=[\
                 'Now, lets add this to the story: ',\
                '"',('{heroname}',share.colors.hero),' the ',('hero',share.colors.hero2),\
                ' and ',('{hero_his}',share.colors.hero2),' ',\
                ('partner',share.colors.partner),' were madly in ',\
                ('love',share.colors.partner2),'". '\
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
        self.addpart(draw.obj_animation('ch2_love1','love',(640,240),record=False,scale=0.3))
        self.addpart(draw.obj_animation('ch2_love1','love',(340,240),scale=0.3))
        self.addpart(draw.obj_animation('ch2_love1','love',(940,240),scale=0.3))


#*PARTNERBASE
class obj_scene_ch2p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def setup(self):
        self.text=['Lets use our "stickman" for ',('{partnername}',share.colors.partner),', said the book of things. ',\
                   'First, draw some pretty hair around ', ('{partner_his}',share.colors.partner2),' head. ',\
                   'Something that ',('{heroname}',share.colors.hero),' will fall in ',('love',share.colors.partner2),' with. '\
                   ]
        self.addpart( draw.obj_drawing('partnerhair',(640,420),legend='Partner\'s Hair',shadow=(200,200),brush=share.brushes.smallpen) )
        self.addpart( draw.obj_image('herohead',(640,420),path='shadows',scale=0.5) )# add empty head on top
        self.addpart(draw.obj_animation('ch2_love2','love',(220,360),record=False,scale=0.5))
        self.addpart(draw.obj_animation('ch2_love2','love',(1280-220,360),scale=0.5))


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
        self.addpart(draw.obj_animation('ch2_partnerbasenoface','partnerbasenoface',(640,360),scale=0.75,record=False,sync=animation1))


class obj_scene_ch2p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6a())
    def setup(self):
        self.text=[\
                   'Uh...Well...aint ',('{partner_he}',share.colors.partner2),' pretty. '\
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
                   ('love',share.colors.partner2),' letters. ',\
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
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
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
        self.addpart( draw.obj_textbox('"The letter said:"',(50,83),xleft=True) )
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
        self.addpart( draw.obj_image('love',(716,546),scale=0.25) )


class obj_scene_ch2p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p6c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p8())
    def setup(self):
        self.text=[\
                    'Aww that is so sweet, said the book of things. ',\
                   ('{heroname}',share.colors.hero),' wants to show ',\
                   ('{hero_his}',share.colors.hero2),' love too. ',\
                   'Draw a ',('saxophone',share.colors.item),' and ',('music notes',share.colors.item),\
                   ' so ',('{hero_he}',share.colors.hero2),' can play ',\
                   ('{partnername}',share.colors.partner),' a serenade. ',\
                   ]
        self.addpart( draw.obj_drawing('saxophone',(340,450),legend='Saxophone (facing right)',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('musicnote',(1280-340,450),legend='Music Notes',shadow=(200,200)) )

class obj_scene_ch2p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done
    def setup(self):
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
                   'Play the melody with the '+tempo+' to serenade ',('{partnername}',share.colors.partner),'. '\
                   ]
        if False:
            drawing=draw.obj_drawing('musicscore',(640,360),shadow=(300,100),brush=share.brushes.smallpen)
            self.addpart( drawing )
        self.world=world.obj_world_serenade(self)# serenade mini-game
        self.addpart(self.world)
        # self.addpart(draw.obj_animation('ch2_musicnote1','musicnote',(640,500),scale=0.3,record=False))
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
                   ('{hero_his}',share.colors.hero2),' serenade. ',\
                   'Its time to go for the ',('kiss',share.colors.partner2),'! ',\
                   ]
        animation1=draw.obj_animation('ch2_partner2','partnerbase',(640,360),scale=0.7,record=False)
        self.addpart(animation1)
        self.addpart(draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4,record=False,sync=animation1))
        self.addpart(draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4,record=False,sync=animation1))



class obj_scene_ch2p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def triggernextpage(self,controls):
        return (controls.ga and controls.gac) or self.world.done# quick skip
    def setup(self):
        tempol='['+share.datamanager.controlname('left')+']'
        tempor='['+share.datamanager.controlname('right')+']'
        self.text=[\
                   'Hold '+tempol+'+'+tempor+' to make them kiss.   ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)# kiss mini-game
        self.addpart(self.world)

class obj_scene_ch2p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p12())
    def setup(self):
        self.text=[\
                  'Lets write down: "',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade, and then they kissed". ',\
                   'One last thing, lets draw a ',\
                   ('house',share.colors.item),' with a ',\
                   ('pond',share.colors.item),' where they live happily together. ',\
                   ]
        self.addpart( draw.obj_drawing('house',(340,450),legend='House',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('pond',(940,450),legend='Pond',shadow=(200,200)) )

class obj_scene_ch2p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p13())
    def setup(self):
        self.text=[\
                  'This is what the house looks like. Move around to check it out. ',\
                   ]
        self.world=world.obj_world_travel(self,start=(-140,-110),goal='nowhere',chapter=2,remove=['flower','bush','garden'])
        self.addpart(self.world)


class obj_scene_ch2p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p14())
    def setup(self):
        self.text=[\
                   'Still a bit basic. Lets also add a few ',\
                   ('bushes',share.colors.item),' around the pond, and some ',\
                   ('flowers',share.colors.item),' to make a nice garden. ',\
                   ]
        self.addpart( draw.obj_drawing('bush',(340,450),legend='Bush',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('flower',(940,450),legend='Flower',shadow=(200,200)) )

class obj_scene_ch2p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play())
    def setup(self):
        self.text=[\
                  'Great, said the book of things. What a lovely home. ',\
                   ]
        self.world=world.obj_world_travel(self,start=(-140,-110),goal='nowhere',chapter=2)
        self.addpart(self.world)

##########################################################
##########################################################
# PLAY CHAPTER

class obj_scene_ch2play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def setup(self):
        self.text=[\
                    'That wraps it up nicely, said the book of things. ',\
                  'Lets read our story again to summarize. ',\
                   ]
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
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),' ',\
                'that lived in a house with a pond and a garden. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)
        # self.addpart( draw.obj_animation('ch2_sunrise','sun',(640,360),record=False) )


class obj_scene_ch2play1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item2),' ',\
                'with ',('{hero_his}',share.colors.hero2),\
                ' ',('partner',share.colors.partner),\
                ' called ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner=True)
        self.addpart(self.world)





class obj_scene_ch2play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)



class obj_scene_ch2play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def setup(self):
        self.text=[\
                   '"Then, ',('{heroname}',share.colors.hero),' received a letter from ',\
                   ('{partnername}',share.colors.partner),' that said ',\
                   ('{partner_he}',share.colors.partner2),' loved ',\
                   ('{hero_him}',share.colors.hero2),' very very much". ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )


class obj_scene_ch2play3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3b())
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' and ',\
                    ('{partnername}',share.colors.partner),' spent the day talking and walking around the house". ',\
                   ]
        self.world=world.obj_world_travel(self,start=(-140,-110),goal='nowhere',chapter=2,partner=True)
        self.addpart(self.world)


class obj_scene_ch2play3b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                    '"In the evening, ',\
                    ('{heroname}',share.colors.hero),' and ',\
                    ('{partnername}',share.colors.partner),' ate the ',\
                    ('fish',share.colors.item2),' for dinner". ',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)


class obj_scene_ch2play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
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
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"...and then they kissed".   ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=False)
        self.addpart(self.world)


class obj_scene_ch2play5a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)
        # animation1=draw.obj_animation('ch2_sunset','sun',(640,360),record=False)
        # animation1.addimage('moon')
        # self.addpart( animation1 )

class obj_scene_ch2play6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play5a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went to back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True)
        self.addpart(self.world)


class obj_scene_ch2playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2play6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch2unlocknext())
    def setup(self):
        self.text=[\
                   '"And they lived happily ever after, the end". ',\
                    'And thats all the story for today, said the book of things. ',
                   'But tomorrow we will make this story even better! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch2unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch2playend())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter III',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=3)# chapter 3 becomes available



#
