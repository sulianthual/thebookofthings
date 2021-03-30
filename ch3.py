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
                   'and ',('{hero_his}',share.colors.hero),' ',('partner',share.colors.partner),\
                    ' woke up... mmmh... caught a ',('fish',share.colors.item),', ate it...  ',\
                     'played a serenade, ',('kissed',share.colors.partner),\
                    ' and went back to ',('bed',share.colors.item),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch3_summary','herobase',(640,360),record=False,scale=0.7)
        animation1.addimage('herobasefish')
        animation2=draw.obj_animation('ch3_summary2','partnerbase',(640,360),record=False,sync=animation1,scale=0.7)
        animation3=draw.obj_animation('ch3_summary3','love',(640,360),record=False,sync=animation1)
        animation3.addimage('guitar')
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
                 ' so lets start him by drawing a ',('scar',share.colors.villain),' on our stickman. ',\
                   ]
        self.addpart( draw.obj_image('herohead',(640,450)) )
        drawing=draw.obj_drawing('scar',(640,450),legend='Add a scar',shadow=(200,200))
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
                   ('{partner_he}',share.colors.partner),' had been captured by the evil ',\
                    ('villain',share.colors.villain),' called ',('{villainname}',share.colors.villain),'". '\
                   ]
        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        animation1=draw.obj_animation('ch3_villaincapture','villainbase',(640,360),record=False,scale=0.7)
        animation2=draw.obj_animation('ch3_villaincapture2','partnerbase',(640,360),record=True,sync=animation1,scale=0.7)
        self.addpart( animation1 )
        self.addpart( animation2 )

class obj_scene_ch3p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p7())
    def setup(self):
        self.text=[\
                  'Now lets write this: "',\
                    ('{heroname}',share.colors.hero),' travelled to the  ',\
                  ('villain',share.colors.villain),'\'s evil lair to rescue ',\
                   ('{partnername}',share.colors.partner),'. ',\
                 ' The evil lair was a',('tower',share.colors.item),' in the ',('mountains',share.colors.item),'".'\
                 ' Draw an ',('evil tower',share.colors.item),\
                 ' and a ',('mountain',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('tower',(340,450),legend='Evil Tower',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('mountain',(940,450),legend='Mountain',shadow=(200,200)) )

class obj_scene_ch3p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  'Travel to the ',('evil lair',share.colors.villain),' with [WASD]. ',\
                   ]
        self.world=world.obj_world_traveltolair(self)# Wake up hero mini-game
        self.addpart(self.world)
        # self.addpart( draw.obj_drawing('grid',(640,400),shadow=(400,280)) )


class obj_scene_ch3p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p9())
    def setup(self):
        self.text=[\
                  'Great, said the book of things, now lets add: "',\
                    ('{heroname}',share.colors.hero),' arrived at the evil lair. ',\
                  ('{villainname}',share.colors.villain),' said: you will have to',\
                  ('fight',share.colors.villain),' me if you want ',\
                   ('{partnername}',share.colors.partner),' back". ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('partnerbase',(1100,530), scale=0.4,rotate=90) )
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
                  ' in the lower left show how much',('life',share.colors.partner),\
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
        self.addpart(draw.obj_image('circle1',(200,640),path='premade'))
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
                  'This is how much ',('bullets',share.colors.villain),\
                  ('{villainname}',share.colors.villain),' has left. ',\
                  ' Survive the fight until ',('{villain_he}',share.colors.villain),\
                  ' is out. Press [Enter] when are ready to start. '
                   ]
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
        self.addpart(self.world)
        self.world.villaintimershoot.end()# stop villain timer (never shoots)
        self.world.text_undone.show=False
        # self.addpart(draw.obj_drawing('show2',(880,530),shadow=(100,150)))
        self.addpart(draw.obj_image('circle2',(1080,720-70),path='premade'))
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
        self.world=world.obj_world_dodgegunshots(self)# Wake up hero mini-game
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
              'Try not to do that again, it messes my story. ',\
                'Its ok for this time, just go back and act more "heroic" next time. ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )



class obj_scene_ch3p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def setup(self):
        self.text=[\
                  'The villain is out of projectiles....(WIP) ',\
                   ]

# evil helicopter crashes in the mountains

class obj_scene_ch3p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())


class obj_scene_ch3p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())


class obj_scene_ch3p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())


class obj_scene_ch3p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p16())


class obj_scene_ch3p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p15())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch3p17())




#
