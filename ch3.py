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

# name house
class obj_scene_chapter3(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p1())
    def setup(self):
        self.text=['-----   Chapter III: The Villain   -----   ',\
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
        share.scenemanager.switchscene(obj_scene_chapter3())
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
        share.scenemanager.switchscene(obj_scene_ch3p4())
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



class obj_scene_ch3p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def setup(self):
        self.text=[\
                 'Perfect, said the book of things. ',\
                'We just need to give a name and gender to this ',('villain',share.colors.villain),'. '\
               'And if you choose a girl we will add some hair for effect. ',
                   ]
        y1=360+90
        y2=520+100
        self.addpart( draw.obj_textbox('The villain was:',(180,y1)) )
        textchoice=draw.obj_textchoice('villain_he')
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(740,y1))
        textchoice.addchoice('3. A thing','it',(1040,y1))
        textchoice.addkey('villain_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('villain_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart( draw.obj_textbox("and the Villain\'s Name was:",(200,y2)) )
        self.addpart( draw.obj_textinput('villainname',25,(750,y2),color=share.colors.hero, legend='Villain Name') )
        #
        self.addpart( draw.obj_image('angryhead',(440,310),scale=0.25) )
        self.addpart( draw.obj_image('scar',(440,310),scale=0.25) )
        self.addpart( draw.obj_image('angryhead',(740,310),scale=0.25) )
        self.addpart( draw.obj_image('scar',(740,310),scale=0.25) )
        self.addpart( draw.obj_image('partnerhair',(740,310),scale=0.5) )
        self.addpart( draw.obj_image('angryhead',(1040,310),scale=0.25) )
        self.addpart( draw.obj_image('scar',(1040,310),scale=0.25) )
    def endpage(self):
        super().endpage()
        # save villain head drawing
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('angryhead',(640,360)) )
        dispgroup1.addpart('part2',draw.obj_image('scar',(640,360)) )
        if share.datamanager.dictwords["villain_he"]=='she':
            dispgroup1.addpart( 'part3',draw.obj_image('partnerhair',(640,360),scale=2) )
            dispgroup1.snapshot((640,360,400,400),'villainhead')
        else:
            dispgroup1.snapshot((640,360,200,200),'villainhead')
        # save villain full body
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('villainhead',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'villainbase')

class obj_scene_ch3p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def setup(self):
        self.text=[\
                  'Now lets write this: "',\
                    ('{heroname}',share.colors.hero),' came back home and ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                   ('{partner_he}',share.colors.partner),' had been captured by the ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch3_villaincapture','villainbase',(640,360),record=False,scale=0.7)
        animation2=draw.obj_animation('ch3_villaincapture2','partnerbase',(640,360),record=False,sync=animation1,scale=0.7)
        self.addpart( animation1 )
        self.addpart( animation2 )

class obj_scene_ch3p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' travelled to the  ',\
                  ('villain',share.colors.villain),'\'s ',('evil lair',share.colors.location),' to rescue ',\
                   ('{partnername}',share.colors.partner),'. ',\
                 ' The ',('evil lair',share.colors.location),\
                 ' was a',('tower',share.colors.item),' in the ',('mountains',share.colors.item),'".'\
                 ' Draw an ',('evil tower',share.colors.item),\
                 ' and a ',('mountain',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('tower',(340,450),legend='Evil Tower',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('mountain',(940,450),legend='Mountain',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        # combine herohead+stickwalk = herowalk
        image1=draw.obj_image('stickwalk',(640,460),path='premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herowalk')
        # combine partnerhead+stickwalk = partnerwalk
        image1=draw.obj_image('stickwalk',(640,460),path='premade')# snapshot
        image2=draw.obj_image('partnerhair',(640,200))
        image3=draw.obj_image('herohead',(640,200),scale=0.5)# hero instead of stick head
        dispgroup2=draw.obj_dispgroup((640,360))
        dispgroup2.addpart('part1',image1)
        dispgroup2.addpart('part2',image2)
        dispgroup2.addpart('part3',image3)
        dispgroup2.snapshot((640,330,200,330),'partnerwalk')


class obj_scene_ch3p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def setup(self):
        self.text=[\
                  'Great, said the book of things, now lets add: "',\
                    'At the ',('evil lair',share.colors.location),', ',\
                  ('{villainname}',share.colors.villain),' said: you will have to ',\
                  ('fight',share.colors.villain),' me if you want ',\
                   ('{partnername}',share.colors.partner),' back". ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        self.addpart( draw.obj_image('mountain',(881,292),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(709,245),scale=0.29,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'mountain') )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )



class obj_scene_ch3p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start())
    def setup(self):
        self.text=[\
                  'This is going to be epic, said the book of things. ',\
                 ' Draw a ',('gun',share.colors.item),'and a ',\
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

class obj_scene_ch3p10start(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start2())
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.text=[\
                  'Alright, here is how the ',('gunfight',share.colors.villain),\
                  ' works, said the book of things. Make ',\
                  ('{heroname}',share.colors.hero),' jump with [W] and crouch with [S].',\
                   ]
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
        self.addpart(self.world)
        self.world.villaintimershoot.end()# stop villain timer (never shoots)
        # self.world.text_undone.show=False
        self.world.healthbar.show=False
        self.world.bulletbar.show=False

class obj_scene_ch3p10start2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start3())
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


class obj_scene_ch3p10start3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
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

class obj_scene_ch3p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10start3())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3p11())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p10death())
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

class obj_scene_ch3p10death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())

    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )



class obj_scene_ch3p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12start())
    def setup(self):
        self.text=[\
                  'Well done!, said the book of things. ',('{villainname}',share.colors.villain),\
                ' has ran out of bullets. ',\
                'But it isnt over yet. ',\
                ('{villainname}',share.colors.villain),\
                ' has started to fight ',('{heroname}',share.colors.hero),\
                ' in hand-to-hand combat. ',\
                   ]
        self.addpart( draw.obj_image('floor2',(640,580+90),path='premade') )
        self.addpart( draw.obj_image('herobase',(340,580),scale=0.35) )
        self.addpart( draw.obj_image('villainbase',(940,580-12),scale=0.35,fliph=True) )
    def endpage(self):
        super().endpage()
        # combine villainhead+stickkick for villain kick
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickkick',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('villainhead',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,300,330),'villainkick')


class obj_scene_ch3p12start(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12start2())
    def setup(self):
        self.text=[\
                  'These are the ',('hero',share.colors.hero),\
                  '\'s and the ',('villain',share.colors.villain),\
                  '\'s healthbars.',\
                   ]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)
        self.world.villainhurt=True# hurt so cannot evolve
        self.world.villain.dict['hurt'].show=False
        self.world.text_undone.show=False
        # self.addpart(draw.obj_image('circle1',(300,200),path='premade'))
        self.addpart(draw.obj_image('show1',(480,370),path='premade',flipv=True))
        # self.addpart(draw.obj_image('circle2',(990,200),path='premade'))
        self.addpart(draw.obj_image('show2',(880,370),path='premade',flipv=True))

class obj_scene_ch3p12start2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12start())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def triggernextpage(self,controls):
        return controls.enter and controls.enterc
    def setup(self):
        self.text=[\
                  'Move with [A][D] and jump with [W]. ',\
                'Stomp on ',('{villainname}',share.colors.villain),\
                ' but beware of ',('{villain_his}',share.colors.villain),\
              ' kick. Press [Enter] to start the fight. ',\
                   ]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)
        self.world.villainhurt=True# hurt so cannot evolve
        self.world.villain.dict['hurt'].show=False
        self.world.text_undone.show=False
        self.addpart(draw.obj_textbox('[A,D: Move] [W: Jump]',(640,200),color=share.colors.instructions) )


class obj_scene_ch3p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12start2())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3p13())
        else:
            share.scenemanager.switchscene(obj_scene_ch3p12death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Stomp the villain. ',\
                   ]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)
        # drawing=draw.obj_drawing('floor2',(640,720-50),shadow=(640,50))
        # drawing.brush.makebrush(share.brushes.smallpen)
        # self.addpart(drawing)


class obj_scene_ch3p12death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())

    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_ch3p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play())
    def setup(self):
        self.text=[\
                  'Well done, said the book of things. Lets write down: ',\
                  '"After a long fight, ',\
                  ('{heroname}',share.colors.hero),' defeated ',\
                  ('{villainname}',share.colors.villain),' and rescued ',\
                  ('{partnername}',share.colors.partner),'. ',\
                  ('{villainname}',share.colors.villain),' said "I will have my revenge" ',\
                  'and disappeared in the mountains". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )

##########################################################
##########################################################
# PLAY CHAPTER

class obj_scene_ch3play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play1())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                   'Thats quite a few changes to our story, said the book of things. ',\
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


class obj_scene_ch3play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play1a())
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


class obj_scene_ch3play1a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play2())
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


class obj_scene_ch3play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play1a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),\
                     ' went to the river and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)



class obj_scene_ch3play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play3a())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' came back home and checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox.',\
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


class obj_scene_ch3play3a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(163,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nI have captured ',('{partnername}',share.colors.partner),'. ',\
                     '\nCome to my ',('evil lair',share.colors.location),' to save ',\
                     ('{partner_him}',share.colors.partner),' if you dare. ',\
                    '\nMuahahahaha, ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_ch3play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play3a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"So ',('{heroname}',share.colors.hero),'" travelled to ',
                ('{villainname}',share.colors.villain),'\'s ',\
                ('evil lair',share.colors.location),' in the mountains". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='tower',chapter=3)
        self.addpart(self.world)


class obj_scene_ch3play5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play6())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                    ('{heroname}',share.colors.hero),' confronted ',\
                  ('{villainname}',share.colors.villain),' at the ',('evil lair',share.colors.location),', ',\
                'and they started to ',('fight',share.colors.villain),' for ',\
              ('{partnername}',share.colors.partner),'. ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
        animation1=draw.obj_animation('ch3_villainconfront1','herobase',(640,360),record=False)
        animation2=draw.obj_animation('ch3_villainconfront2','villainbase',(640,360),record=False,sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))


class obj_scene_ch3play6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play5())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3play7())
        else:
            share.scenemanager.switchscene(obj_scene_ch3play6death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"They fought with guns". ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)


class obj_scene_ch3play6death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play6())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_ch3play7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play6())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_ch3play8())
        else:
            share.scenemanager.switchscene(obj_scene_ch3play7death())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"..then they fought with fists." ',\
                   ]
        self.world=world.obj_world_stompfight(self)
        self.addpart(self.world)

class obj_scene_ch3play7death(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play7())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_ch3play8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play9())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.a and controls.d)
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' defeated ',\
                  ('{villainname}',share.colors.villain),' and rescued ',\
                  ('{partnername}',share.colors.partner),'. ',\
                  ('{villainname}',share.colors.villain),' said "I will have my revenge" ',\
                  'and disappeared in the mountains". ',\
                   ]
        self.addpart( draw.obj_image('mountain',(840,390),scale=0.5) )
        self.addpart( draw.obj_image('mountain',(930,290),scale=0.4) )
        self.addpart( draw.obj_image('mountain',(1110,380),scale=0.8,fliph=True) )
        animation1=draw.obj_animation('ch3_herowins','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_herowins2','partnerbase',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch3_herowins3','villainbase',(640,360),record=False,sync=animation1) )
        self.addpart(draw.obj_textbox('Press [A]+[D] to Continue',(640,660),color=share.colors.instructions))



class obj_scene_ch3play9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play10())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' and ',\
                  ('{partnername}',share.colors.partner),' went back home". ',\
                   ]
        self.world=world.obj_world_travel(self,start='tower',goal='home',chapter=3,partner=True)
        self.addpart(self.world)

class obj_scene_ch3play10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"They  ate ',\
                    ('fish',share.colors.item),' for dinner".',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)


class obj_scene_ch3play11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play12())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade..." ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)


class obj_scene_ch3play12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play13())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"...and then they kissed".   ',\
                   ]
        self.world=world.obj_world_kiss(self)
        self.addpart(self.world)


class obj_scene_ch3play13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play14())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_ch3play14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play15())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner='inlove')
        self.addpart(self.world)


class obj_scene_ch3play15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3playend())
    def setup(self):
        self.text=[\
                   '"And they lived happily ever after, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very perfect story)',(640,280)) )
        self.addpart( draw.obj_image('house',(320,430), scale=0.25) )
        self.addpart( draw.obj_image('tree',(340,560), scale=0.25) )
        self.addpart( draw.obj_image('tower',(950,430), scale=0.25) )
        self.addpart( draw.obj_image('mountain',(910,540), scale=0.25) )
        self.addpart( draw.obj_image('herobase',(620,450), scale=0.25) )
        self.addpart( draw.obj_image('partnerbase',(509,476), scale=0.25) )
        self.addpart( draw.obj_image('villainbase',(772,474), scale=0.25,fliph=True) )
        self.addpart( draw.obj_image('gun',(380,270), scale=0.15) )
        self.addpart( draw.obj_image('bullet',(890,270), scale=0.15) )


class obj_scene_ch3playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3play15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',
                   'That is quite a story, well done! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch3unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3playend())
    def setup(self):
        self.text=['You have unlocked ',('Chapter IV: Marital Issues',share.colors.instructions),'. ',\
                  'You can always redraw the villain, tower and mountain, gun and bullet in ',\
                  ('Chapter III: The Villain',share.colors.instructions),'. '\
                   '',\
                   ]
        share.datamanager.updateprogress(chapter=4)# chapter 4 becomes available
        for c,value in enumerate(['villainhead','tower','mountain','gun','bullet']):
            self.addpart( draw.obj_image(value,(240+c*200,400), scale=0.25) )

















#
