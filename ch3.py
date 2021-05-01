#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter3.py: ...
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

# Chapter III: ...
# *CHAPTER III

class obj_scene_chapter3(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p0())
    def triggernextpage(self,controls):
        return True


class obj_scene_ch3p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def setup(self):
        self.text=['-----   Chapter III: Where are you   -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Lets see how our story is going so far". ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch3p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())
    def setup(self):
        self.text=['Lets see here... " The ',('hero',share.colors.hero),\
                   ' and ',('{hero_his}',share.colors.hero),' ',('partner',share.colors.partner),\
                    ' woke up... mmmh... caught a ',('fish',share.colors.item),', ate it...  ',\
                     'played a serenade, ',('kissed',share.colors.partner),\
                    ' and went back to ',('bed',share.colors.item),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch3_summary','herobase',(640,360),record=False,scale=0.7)
        animation1.addimage('herobasefish')
        animation2=draw.obj_animation('ch3_summary2','partnerbase',(640,360),record=False,sync=animation1,scale=0.7)
        animation3=draw.obj_animation('ch3_summary3','love',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')# was guitar, obsolete
        animation3.addimage('empty',path='premade')
        animation4=draw.obj_animation('ch3_summary4','sun',(640,360),record=False,sync=animation1)
        animation4.addimage('moon')
        animation4.addimage('empty',path='premade')
        self.addpart(animation4)
        self.addpart(animation2)
        self.addpart(animation1)
        self.addpart(animation3)


class obj_scene_ch3p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())
    def setup(self):
        self.text=[\
                   'Well this story looks a lot like a  ',('chick flick',share.colors.partner),', said the book of things. ',\
                   'I want more action, more suspense! ',\
                   'Lets just add a ',('villain',share.colors.villain), '. ',\
                 'This ',('villain',share.colors.villain),' has probably been hurt a lot,',\
                 ' so lets start him by drawing a big ',('scar',share.colors.villain),' on our stickman. ',\
                   ]
        self.addpart( draw.obj_image('herohead',(640,450)) )
        drawing=draw.obj_drawing('scar',(640,450),legend='Add a big scar',shadow=(200,200))
        self.addpart( drawing)

class obj_scene_ch3p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3a())
    def setup(self):
        self.text=[\
                  'Something isnt right, said the book of things. ',\
                'This ',('villain',share.colors.villain),' is so evil he should be angry all the time. ',\
                   'Draw an ',('angry face',share.colors.villain),' and make it look slightly to the right. ',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2) )
        self.addpart( draw.obj_image('scar',(640,450)) )
        drawing=draw.obj_drawing('angryface',(640,450),legend='Draw an angry face',shadow=(200,200))
        self.addpart( drawing)
    def endpage(self):
        super().endpage()
        # save angry head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade'))
        dispgroup1.addpart('part2',draw.obj_image('angryface',(640,360)))
        dispgroup1.snapshot((640,360,200,200),'angryhead')
        # save villain head drawing
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('angryhead',(640,360)) )
        dispgroup1.addpart('part2',draw.obj_image('scar',(640,360)) )
        dispgroup1.snapshot((640,360,200,200),'villainhead')
        # save villain full body (slightly different than hero, because originally we could include partnerhair)
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('villainhead',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'villainbase')
        # heroangry+zapaura=herozapped
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('angryhead',(640,200),scale=0.5) )
        dispgroup2.addpart('part3',draw.obj_image('zapaura',(640,360),path='premade') )
        dispgroup2.snapshot((640,360,200,300),'herozapped')


class obj_scene_ch3p3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4())
    def setup(self):
        self.text=['This is what the ',('villain',share.colors.villain),' looks like. ',\
                   'Pretty scary! ',\
                   'Lets move on to the next step. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','villainbase',(360,360),record=True))


class obj_scene_ch3p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def setup(self):
        self.text=[\
                 'Now, said the book of things. ',\
                'we just need to give a name and gender to this ',('villain',share.colors.villain),'. '\
                   ]
        y1=360+90-200
        y2=520+100-200
        self.addpart( draw.obj_textbox('The villain was:',(180,y1)) )
        textchoice=draw.obj_textchoice('villain_he')
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('villain_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('villain_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the Villain\'s Name was:",(200+30,y2)) )
        self.addpart( draw.obj_textinput('villainname',25,(750,y2),color=share.colors.villain, legend='Villain Name') )
        # self.addpart( draw.obj_image('angryhead',(1150,y2),scale=0.5) )
        # self.addpart( draw.obj_image('scar',(1150,y2),scale=0.5) )




class obj_scene_ch3p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               'Lets read our story again, said the book of things: ',\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'called  ',('{heroname}',share.colors.hero),'. ',\
                'It was morning and the sun was rising". ',\
                   ]
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)

class obj_scene_ch3p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item),' ',\
                'with ',('{hero_his}',share.colors.hero),\
                ' partner ',('{partnername}',share.colors.partner),'." ',\
                   ]
        self.world=world.obj_world_wakeup(self,partner=True)
        self.addpart(self.world)


class obj_scene_ch3p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the pond and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_ch3p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def setup(self):
        self.text=[\
                  'Now lets write this: "',\
                    ('{heroname}',share.colors.hero),' came back home but ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                   ('{partner_he}',share.colors.partner),' had been captured by the ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch4_villaincapture1','villainbase',(640,360),record=False)
        animation1.addimage('villainholdspartner')
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_villaincapture2','partnerbase',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
    def presetup(self):
        super().presetup()
        # villainbase+partnerbase=villainholdspartner
        image1=draw.obj_image('villainbase',(640,360))
        image2=draw.obj_image('partnerbase',(640-70,360+80),rotate=90)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,400,330),'villainholdspartner')


class obj_scene_ch3p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
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


class obj_scene_ch3p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(50,83),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI have captured ',('{partnername}',share.colors.partner),'. ',\
                    ('{partner_he}',share.colors.partner),\
                     ' is in my evil lair. ',\
                     '\nDont even think about coming to rescue ',\
                     ('{partner_him}',share.colors.partner),'. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch3p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def setup(self):
        self.text=[\
                  'Fantastic, said the book of things. A great disruptive event for our story. ',\
                 'Let continue: "The evil lair was a castle in the mountains". '\
                 'Draw an ',('castle',share.colors.item),\
                 ' and a ',('mountain',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('castle',(340,450),legend='Evil Castle',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('mountain',(940,450),legend='Mountain',shadow=(200,200)) )




class obj_scene_ch3p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                'go to the castle in the west',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='castle',chapter=3)
        self.addpart(self.world)

class obj_scene_ch3p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())
    def setup(self):
        self.text=[\
                  'Great, said the book of things, now lets add: "',\
                    'At the ',('evil lair',share.colors.location),', ',\
                  ('{villainname}',share.colors.villain),' said: I told you not to come here. ',\
                  'Now leave or get ready to ',\
                  ('fight',share.colors.villain),'!". ',\
                   ]
        self.addpart( draw.obj_image('castle',(1100,310), scale=0.7) )
        # self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        self.addpart( draw.obj_image('mountain',(881,292),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(709,245),scale=0.29,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'mountain') )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )



class obj_scene_ch3p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p16())
    def setup(self):
        self.text=[\
                  'This is going to be epic, said the book of things. ',\
                 ' Draw a ',('gun',share.colors.item),' and a ',\
                ('bullet',share.colors.item),' for the fight. ',\
                   ]
        drawing1=draw.obj_drawing('gun',(300+50,450),legend='Gun (facing right)',shadow=(300,200))
        drawing1.brush.makebrush(share.brushes.bigpen)
        self.addpart(drawing1)
        drawing2=draw.obj_drawing('bullet',(1280-200-50,450),legend='Bullet (facing right)',shadow=(200,200))
        drawing2.brush.makebrush(share.brushes.bigpen)
        self.addpart(drawing2)
    def endpage(self):
        super().endpage()
        # herohead+stickcrouch =herocrouch
        image1=draw.obj_image('stickcrouch',(940,360),path='premade')
        image2=draw.obj_image('herohead',(800,360),scale=0.5,rotate=90)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((940,360,300,200),'herocrouch')# 0 to 660 in height
        # villainhead+stickshootcrouch =villainshootcrouch (beware larger if girl)
        image1=draw.obj_image('stickshootcrouch',(640,360+100),path='premade')
        image2=draw.obj_image('villainhead',(640,360),scale=0.5,fliph=True)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360+100-50,300,250),'villainshootcrouch')# 0 to 660 in height
        # villainbase+gun =villainbasegun (for cutscenes)
        image1=draw.obj_image('villainbase',(640,330))
        image2=draw.obj_image('gun',(640+180,330),scale=0.4)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640+50,330,200+50,330),'villainbasegun')# 0 to 660 in height


class obj_scene_ch3p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p17())
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.text=[\
                  'This is how the ',('gunfight',share.colors.villain),\
                  ' works, said the book of things. Make ',\
                  ('{heroname}',share.colors.hero),' jump with [W] and crouch with [S].',\
                   ]
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
        self.addpart(self.world)
        self.world.villaintimershoot.end()# stop villain timer (never shoots)
        # self.world.text_undone.show=False
        self.world.healthbar.show=False
        self.world.bulletbar.show=False


class obj_scene_ch3p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18())
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.text=[\
                  'The ',('hearts',share.colors.partner),\
                  ' in the lower left show how much ',('life',share.colors.partner),' ',\
                  ('{heroname}',share.colors.hero),' has. ',\
                  'If ',('{hero_he}',share.colors.hero),' gets hit, ',\
                  ('{hero_he}',share.colors.hero),' will loose life and eventually ',\
                  ('die',share.colors.villain),', so dont let that happen. '
                   ]
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
        self.addpart(self.world)
        self.world.villaintimershoot.end()# stop villain timer (never shoots)
        self.world.text_undone.show=False
        self.world.bulletbar.show=False
        # self.addpart(draw.obj_drawing('show1',(480,530),shadow=(100,150)))
        # self.addpart(draw.obj_drawing('circle1',(200,640),shadow=(200,70),brush=share.brushes.smallpen))
        # self.addpart(draw.obj_image('circle1',(200,640),path='premade'))
        self.addpart(draw.obj_image('show1',(480,530),path='premade'))


class obj_scene_ch3p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.text=[\
                  'This is how much bullets ',\
                  ('{villainname}',share.colors.villain),' has left. ',\
                  ' Survive the fight until ',('{villain_he}',share.colors.villain),\
                  ' is out. Press [Enter] when are ready to start. '
                   ]
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
        self.addpart(self.world)
        self.world.villaintimershoot.end()# stop villain timer (never shoots)
        self.world.text_undone.show=False
        # self.addpart(draw.obj_drawing('show2',(880,530),shadow=(100,150)))
        # self.addpart(draw.obj_image('circle2',(1080,720-70),path='premade'))
        self.addpart(draw.obj_image('show2',(880,530),path='premade'))


class obj_scene_ch3p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p18())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3p20())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p19death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Survive the gun fight. ',\
                   ]
        # drawing=draw.obj_drawing('floor1',(640,500),shadow=(640,100))
        # drawing.brush.makebrush(share.brushes.smallpen)
        # self.addpart(drawing)
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)
        # self.addpart(draw.obj_image('villainshootcrouch',(840,500+50),scale=0.5) )
        # self.addpart(draw.obj_image('villainbase',(1140,500+50),scale=0.5,fliph=True) )
        # self.addpart(draw.obj_image('herobase',(140,500+50),scale=0.5) )
        # self.addpart(draw.obj_image('herocrouch',(440,500+50),scale=0.5) )
        # animation1=draw.obj_animation('ch3_herodies','herobase',(640,360),record=True)
        # self.addpart( animation1 )

class obj_scene_ch3p19death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())

    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),fontsize='large') )



class obj_scene_ch3p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p21())
    def setup(self):
        self.text=[\
                  'Well done, said the book of things. Lets write down: ',\
                  '"',\
                  ('{villainname}',share.colors.villain),' ran out of bullets. ',\
                  ('{villain_he}',share.colors.villain),' said: this isnt over! ',\
                  ' and headed towards ',\
                  ('{villain_his}',share.colors.villain),' ',\
                  ('evil castle',share.colors.location),'". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('castle',(1143,318),scale=0.67) )
        # self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        # self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain'))

class obj_scene_ch3p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22())
    def setup(self):
        self.text=[\
                  '"',\
                  ('{villainname}',share.colors.villain),' entered ',\
                  ('{villain_his}',share.colors.villain),' ',\
                  ('evil castle',share.colors.location),' and said: ',\
                  'Muahaha, my ',\
                  ('castle',share.colors.location),' is locked tight and protected by a ',\
                  ('password',share.colors.password),'. ',\
                  'You will never get in!".  ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'tower','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_drawing('towersparks',(1000,310),shadow=(280,200)) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )

class obj_scene_ch3p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p23())
    def setup(self):
        self.text=[\
                  '"The  ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),' (automated security system) blasted: ',\
                  'Lockdown Engaged. Password Required to open castle. Please Enter ',\
                  ('password',share.colors.password),'". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('castlepassword',30,(380,260),color=share.colors.villain, legend='Castle Password',default=' ')
        self.addpart( self.textinput )

class obj_scene_ch3p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def setup(self):
        self.text=[\
                  '"Wrong password, blasted the ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),', zapping engaged! ',\
                  'And it zapped ',\
                  ('{heroname}',share.colors.hero),' with an electric shock". ',\
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


class obj_scene_ch3p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p23())
    def nextpage(self):
        if share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch3p25())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p24fail())
    def setup(self):
        self.text=[\
                  '"The  ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),' blasted: ',\
                  'You may leave or dare try again". ',\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'castle','mountain','herobase','villainbase'))
        self.addpart( draw.obj_image('herobase',(175,542),scale=0.47,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.textinput=draw.obj_textinput('castlepassword',30,(380,260),color=share.colors.villain, legend='Castle Password',default=' ')
        self.addpart( self.textinput )
        y1=170
        # self.addpart( draw.obj_textbox('Leave:',(90,y1),xleft=True) )
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Leave','yes',(240,y1))
        textchoice.addchoice('Try Again','no',(460,y1))
        self.addpart( textchoice )

class obj_scene_ch3p24fail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def setup(self):
        randolist=['Wrooooong','Failed Again','Haha, I bet you are enjoying this']
        randotext=tool.randchoice(randolist)
        self.text=[\
                  '"'+randotext+', blasted the ',('castle',share.colors.location),'\'s ',\
                  ('ass',share.colors.item),', zapping engaged! ',\
                  'And it zapped ',\
                  ('{heroname}',share.colors.hero),' with an electric shock". ',\
                   ]
        self.addpart( draw.obj_image('castle',(1000,450),scale=1.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(631,464),scale=0.56,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(465,427),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castlesparks',(1000,310),path='premade') )
        animation1=draw.obj_animation('ch3_herozapped','herobase',(640,360),record=False)
        animation1.addimage('herozapped')
        self.addpart( animation1 )


class obj_scene_ch3p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p26())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"Having failed to unlock the  ',('castle',share.colors.location),', ',\
                ('{heroname}',share.colors.hero),' travelled back ',
                ('home',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='castle',goal='home',chapter=3,heroangry=True)
        self.addpart(self.world)

class obj_scene_ch3p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p27())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' was very sad. ',\
                   ('{hero_he}',share.colors.hero), ' though about how ',\
                   ('{hero_he}',share.colors.hero),' used to charm ',\
                   ('{partnername}',share.colors.partner),' with a serenade. ',\
                   ]
        self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
        self.addpart(self.world)

class obj_scene_ch3p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p28())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"Then, ',\
                   ('{heroname}',share.colors.hero),' remembered how ',\
                   ('{hero_him}',share.colors.hero),' and ',\
                   ('{partnername}',share.colors.partner),' used to kiss". ',\
                   ]
        self.world=world.obj_world_kiss(self,noending=True)
        self.addpart(self.world)

class obj_scene_ch3p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p29())
    def setup(self):
        self.text=[\
                   '"But ',\
                   ('{partnername}',share.colors.partner),' wasnt there, and ',\
                   ('{heroname}',share.colors.hero),' was only kissing the ',\
                   ('fish',share.colors.item),' that ',\
                   ('{hero_he}',share.colors.hero),' had caught earlier". ',\
                   ]

        # self.addpart( draw.obj_image('partnerbase',(710,390),scale=0.7,rotate=15) )
        self.addpart( draw.obj_image('fish',(785,467),scale=0.84,rotate=-68,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('herobaseangry',(580,400),scale=0.7,rotate=-15) )
        # self.addpart( draw.obj_imageplacer(self,'fish'))
        self.addpart( draw.obj_animation('ch2_lovem2','love',(340,360),scale=0.4) )
        self.addpart( draw.obj_animation('ch2_lovem3','love',(940,360),scale=0.4) )

class obj_scene_ch3p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_ch3p30(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p29())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p31())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went to back to bed sad and lonely". ',\
                   ]
        self.world=world.obj_world_gotobed(self,heroangry=True)
        self.addpart(self.world)

class obj_scene_ch3p31(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p30())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p32())
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' was almost asleep, ',\
                  'when a small voice started whispering. "',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        self.addpart( draw.obj_image('herobaseangry',(420,490), scale=0.7,rotate=80) )
        self.addpart( draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5) )

class obj_scene_ch3p32(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p31())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p33())
    def setup(self):
        self.text=[\
                   '"The small voice whispered: ',\
                   'please tell me. ',\
                  'Please answer me honestly. ',\
                  'Of all the ',('bugs',share.colors.bug),\
                  ' in the world, which ',('bug',share.colors.bug),' is the one that ',\
                  ('TERRIFIES',share.colors.hero),' you the most." ',\
                   ]
        self.addpart( draw.obj_textinput('bug',25,(640,260),color=share.colors.hero, legend='Most Terrifying Bug') )


class obj_scene_ch3p33(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p32())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p34())
    def setup(self):
        self.text=[\
                   '"A ',('{bug}',share.colors.bug),'!, whispered the small voice. ',\
                   'That is indeed so ',('TERRIFYING',share.colors.hero),'! ',\
                  'Please show me what a ',('{bug}',share.colors.bug),' looks like ',\
                  ' and I will bother you no more." ',\
                   ]
        bugword=share.datamanager.getword('bug')
        self.addpart( draw.obj_drawing('bug',(640,450),legend='Draw a '+bugword+' ',shadow=(200,200)) )


class obj_scene_ch3p34(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p33())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p35())
    def setup(self):
        self.text=[\
                   '"Well, I have a small confession to make, whispered the small voice. ',\
                  'Then, something cold and sticky crawled on ',('{heroname}',share.colors.hero),\
                  '\'s back." ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobaseangry','bug'))
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        # self.addpart( draw.obj_image('herobaseangry',(420,490), scale=0.7,rotate=80) )
        animation1=draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herobuginbed','herobaseangry',(640,360),record=False,sync=animation1) )


class obj_scene_ch3p35(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p34())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p36())
    def setup(self):
        self.text=[\
                   '"Just like ',('{heroname}',share.colors.hero),' had feared, a small ', \
                   ('{bug}',share.colors.bug),' emerged from ',\
                   ('{hero_his}',share.colors.hero),' bed. ',\
                  'Please, please do not crush me said the ',('{bug}',share.colors.bug),'! ',\
                  'I am here to help you!". ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobaseangry','bug'))
        self.addpart( draw.obj_image('herobaseangry',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(640,360),record=False) )


class obj_scene_ch3p36(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p35())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p37())
    def setup(self):
        self.text=[\
                   '"I was in your pocket the whole time, said the ',('{bug}',share.colors.bug),'. ',\
                  'I am terribly sorry to ',('terrify',share.colors.hero),' you, this wasnt my intention at all. ',\
                 'I can help you unlock ',('{villainname}',share.colors.villain),\
                 '\'s ',('evil castle',share.colors.location),' and rescue ',\
                 ('{partnername}',share.colors.partner),'. ',\
                   ]
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(440,360),record=False) )


class obj_scene_ch3p37(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p36())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p38())
    def setup(self):
        self.text=[\
                   '"See, before this I used to crawl under ',('{villainname}',share.colors.villain),'\'s bed. ',\
                  'And I even heard ',('{villain_him}',share.colors.villain),' talk in ',\
                  ('{villain_his}',share.colors.villain),' sleep! ', \
                   ]
        self.addpart( draw.obj_image('bed',(1280-440,500), scale=0.75,fliph=True) )
        self.addpart( draw.obj_image('villainbase',(1280-420,490), scale=0.7,rotate=80,fliph=True) )
        animation1=draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks2','bug',(640,360),record=True,sync=animation1) )


class obj_scene_ch3p38(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p37())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p39())
    def setup(self):
        self.text=[\
                   '"It turns out that ', \
                   ('{villainname}',share.colors.villain),\
                   ' learned all ',('{villain_his}',share.colors.villain),\
                   ' evil ways from three ',('Grandmasters of Deceit',share.colors.villain),'. ',\
                   ' Apparently, theses ',('grandmasters',share.colors.villain),' hold the clues to the evil castle\'s ',\
                   ('password',share.colors.password),'". ',\
                   ]
        self.addpart( draw.obj_image('villainhead',(524,530),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('castle',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(640,360),record=True,path='premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(137,564),path='premade') )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='premade') )
        # self.addpart( draw.obj_imageplacer(self,'castle','villainhead') )

class obj_scene_ch3p39(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p38())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p40())
    def setup(self):
        self.text=[\
                   '"The first ', ('Grandmaster of Deceit',share.colors.villain),\
                   ' lives not too far from here in the east. ',\
                   'Tomorrow, I will show you how to get there". ',\
                   ]
        self.addpart( draw.obj_animation('ch3_bugtalks1','bug',(440,360),record=False) )


class obj_scene_ch3p40(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3end())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"The ',('{bug}',share.colors.bug),\
                   ' crawled back in ',('{heroname}',share.colors.hero),'\'s pocket. ',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed a little happier, for tomorrow he may be able to rescue ',\
                   ('{partnername}',share.colors.partner),'".',\
                   ]
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)

class obj_scene_ch3end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p39())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3unlocknext())
    def setup(self):
        self.text=[\
                    'And thats all for today, said the book of things. ',
                   'The tension is killing me. I cant wait to find what happens tomorrow! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch3unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter IV',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=4)# chapter 4 becomes available
#
