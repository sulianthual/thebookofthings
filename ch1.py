#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter1.py: ...
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

# Chapter I: ...
# *CHAPTER I


class obj_scene_chapter1(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p1())
    def setup(self):
        self.text=['-----   Chapter I: The Hero   -----   ',\
                   '\n It was a new day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Today, we are going to write an amazing story. ',\
                  'Lets start by writing the first page." ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch1p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def setup(self):
        self.text=[\
                   'Lets write this, said the book of things: "Once upon a time, there was a ',('hero',share.colors.hero),'"." ',\
                   'Simple and to the point. ',\
                   'Well, lets give this ',('hero',share.colors.hero),' a proper name and gender.',\
                  '\n\n ',\
                  ('Hover over the name box below with [MOUSE] then type a name using the [KEYBOARD]. ',share.colors.instructions),\
                 ('Then, choose a gender with [LEFT MOUSE]. ',share.colors.instructions),\
                   ]
        self.addpart( draw.obj_textbox("The Hero\'s Name was:",(200,460)) )
        self.addpart( draw.obj_textinput('heroname',25,(750,460),color=share.colors.hero, legend='Hero Name') )
        self.addpart( draw.obj_textbox('and the hero was:',(180,580)) )
        textchoice=draw.obj_textchoice('hero_he')
        textchoice.addchoice('1. A guy','he',(440,580))
        textchoice.addchoice('2. A girl','she',(740,580))
        textchoice.addchoice('3. A thing','it',(1040,580))
        textchoice.addkey('hero_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('hero_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
        self.addpart(draw.obj_animation('ch1_pen2','pen',(1180,400),record=True,scale=0.5))



class obj_scene_ch1p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p3())
    def setup(self):
        self.text=['Now, said the book of things, lets see how this hero ',('{heroname}',share.colors.hero)," looks like. ",\
                   'Here is a basic template for ',('{heroname}',share.colors.hero),\
                   ', that I made all by myself. I call it the "Stickman".',\
                   ' It is near perfect, but you could still improve on it a little. ',\
                   ]
        # Creation of stickman from snapshot (combines head and body)
        if False:
            # self.addpart( draw.obj_drawing('stickhead',(640,360),shadow=(100,100)) )# draw
            # self.addpart( draw.obj_drawing('stickbody',(940,360),shadow=(200,200)) )
            image1=draw.obj_image('stickbody',(640,460),path='premade')# snapshot
            image2=draw.obj_image('stickhead',(640,200),path='premade')
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            # self.addpart(dispgroup1)# preview
            dispgroup1.snapshot((640,360,200,300),'stickbase',path='premade')
            # self.addpart(draw.obj_image('stickbase',(940,360),path='premade'))#
        #
        animation1=draw.obj_animation('ch1_stickbase1','stickbase',(640,360),scale=0.75,record=False,path='premade')
        self.addpart(animation1)




class obj_scene_ch1p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def setup(self):
        self.text=['Draw a happy face for ',('{heroname}',share.colors.hero),', said the book of things, ',\
                   'and make ', ('{hero_him}',share.colors.hero),' look slightly to the right. ',\
                   ('Draw with [Left Mouse] and erase with [Backspace]',share.colors.instructions),', but you should know this by now.',\
                   ]
        drawing=draw.obj_drawing('herohead',(640,450),legend='Draw a Happy Face')
        self.addpart( drawing )
    def endpage(self):
        super().endpage()
        # combine herohead+stickbody = herobase
        image1=draw.obj_image('stickbody',(640,460),path='premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herobase')


class obj_scene_ch1p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p5())
    def setup(self):
        self.text=['So this is what ',('{heroname}',share.colors.hero),' looks like. ',\
                    'Not bad, said the book of things. ',\
                   'Indeed, ',('{hero_he}',share.colors.hero),' looks very cool. ',\
                   'Lets move on to the next step. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','herobase',(360,360),record=True))




class obj_scene_ch1p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p6())
    def setup(self):
        self.text=['So far, our story goes as "Once upon a Time, There was a ',('Hero',share.colors.hero),'". ',\
                  'It aint much but its a start, said the book of things. ',\
                'Now, lets draw a ',('bed',share.colors.item),' ',\
                'such that our ',('hero',share.colors.hero),' can wake up.',\
                   ]
        drawing=draw.obj_drawing('bed',(640,450),legend='Draw a Bed',shadow=(400,200))
        self.addpart( drawing )



class obj_scene_ch1p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p7())
    def setup(self):
        self.text=['Well done, so lets write down: "It was morning when ',\
                  ('{heroname}',share.colors.hero),', the ',('hero',share.colors.hero),\
                  ', woke up from ',('bed',share.colors.item),\
                  '". We are off to a great start, said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        self.addpart( draw.obj_image('herobase',(420,490), scale=0.7,rotate=80) )
        # self.addpart(draw.obj_animation('ch1_heroawakes','herobase',(640,360),record=True,scale=0.7))
        # self.addpart( draw.obj_image('herobase',(903,452), scale=0.7) )


# mini game wake up
class obj_scene_ch1p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '... Huh...well, you actually need to hold [D] to wake ',\
                  ('{heroname}',share.colors.hero),\
                  ' from ',('bed',share.colors.item),', said the book of things. ',\
                  ('{hero_he}',share.colors.hero),' is quite lazy you know. ',\
                  ' And dont release [D] too soon or ',('{hero_he}',share.colors.hero),\
                  ' will go straight back to sleep. ',\
                  ' When ',('{hero_he}',share.colors.hero),' is fully awake, we will move on. ',\
                   ]
        self.world=world.obj_world_wakeup(self,sun=False)
        self.addpart(self.world)



class obj_scene_ch1p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p9())
    def setup(self):
        self.text=['Finally, ',('{heroname}',share.colors.hero),\
                    ' the ',('hero',share.colors.hero),' is awake. ',\
                    ' Well done, said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        # self.addpart( draw.obj_image('herobase',(903,452), scale=0.7) )
        # self.addpart( draw.obj_textbox('Good Morning!',(1100,480)) )
        self.addpart(draw.obj_animation('ch1_awaken','herobase',(640,360),record=False,scale=0.7))



class obj_scene_ch1p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p10())
    def setup(self):
        self.text=['Since it is the first day, today we will have ',('{heroname}',share.colors.hero), \
                  ' take it easy, said the book of things. Lets just go  fishing. ',\
                'All you need is to draw a ',('fish',share.colors.item),\
                ' and a ',('hook',share.colors.item),', ',\
                ' and we will be on our way. ',\
                   ]
        self.addpart(draw.obj_drawing('hook',(240,450),legend='Draw a Hook',shadow=(200,200)))
        self.addpart(draw.obj_drawing('fish',(940,450),legend='Draw a Fish (Facing Left)',shadow=(300,200)))
        if False:# not for player
            hookline=draw.obj_drawing('hookline',(540,360),legend='Hook',shadow=(30,360),brush=share.brushes.smallpen)
            self.addpart(hookline)
    def endpage(self):
        super().endpage()
        # combine hero+fish into: hero holding fish
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('herobase',(640,452), scale=0.7))
        dispgroup1.addpart('part2',draw.obj_image('fish',(776,486), scale=0.4,rotate=-90))
        dispgroup1.snapshot((700,452,200,260),'herobasefish')

class obj_scene_ch1p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    ' Lower the hook with [S] and catch a fish. ',\
                   ]
        self.world=world.obj_world_fishing(self)# fishing mini-game
        self.addpart(self.world)
        self.world.timerend.amount=100# longer cutscene for first time playing



class obj_scene_ch1p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p12())
    def setup(self):
        self.text=[\
                    'Nice Catch, said the book of thing. This ',\
                    ('{heroname}',share.colors.hero),' is going places. ',\
                    ' Lets write down in our story: "',\
                    ('{heroname}',share.colors.hero),' the ',('hero',share.colors.hero),\
                    ' went to the river and caught a ',('fish',share.colors.item),'". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_herofishmove','herobasefish',(640,360),record=True))



class obj_scene_ch1p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p13())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    ' Moving on, said the book of things. Lets write down: ',\
                    ' "The ',('hero',share.colors.hero),' ate the ',
                    ('fish',share.colors.item),' for dinner." ',\
                    'Do it by ',('alternating [A] and [D]',share.colors.black),'. ',\
                   ]
        self.world=world.obj_world_eatfish(self)# fishing mini-game
        self.addpart(self.world)
        self.world.timerend.amount=100# longer cutscene for first time playing
        # self.addpart( draw.obj_image('fish',(900,400), scale=1,rotate=-45) )
        # self.addpart( draw.obj_image('herobase',(340,400), scale=0.7) )
        # self.addpart(draw.obj_animation('ch1_heroeats1','herobase',(640,360),record=True,imgscale=0.7))
        # animation2=draw.obj_animation('ch1_eatsounds','says_crunch',(360,360),record=True,sync=self.world.animation1,path='premade')
        # animation2.addimage('says_miam')
        # animation2.addimage('says_gulp')
        # animation2.addimage('says_empty')
        # self.addpart(animation2)



class obj_scene_ch1p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p14())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    'Nicely done, said the book of things. ',\
                    'That wraps it up for our first day. Now, lets put the ',\
                    ('hero',share.colors.hero),' back to sleep. ',\
                    ' Hold [A], and dont release',\
                    ' or this procrastinator will stay awake all night. ',\
                   ]
        self.world=world.obj_world_gotobed(self,addmoon=False)
        self.addpart(self.world)


class obj_scene_ch1p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play())
    def setup(self):
        self.text=[\
                   'And we finish with: "At night, the ',('hero',share.colors.hero),' went to back to bed". ',\
                   'That wraps it nicely, says the book of things. ',\
                   'One last thing, lets draw the ',('sun',share.colors.item),\
                   ' and the ',('moon',share.colors.item),\
                   ' so we know when it is day and night. ',\
                   ]
        # self.addpart(draw.obj_drawing('sun',(340,450),legend='Sun',shadow=(200,200)))
        self.addpart(draw.obj_drawing('sun',(300+50,450),legend='Sun',shadow=(300,200)))
        self.addpart(draw.obj_drawing('moon',(1280-200-50,450),legend='Moon',shadow=(200,200)))


##########################################################
##########################################################
# PLAY CHAPTER


class obj_scene_ch1play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play1())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                   'Now, lets read again our story to summarize, said the book of things. ',\
                   'Press [S] to start. ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Start',(640,660),color=share.colors.instructions))
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch1play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"Once upon a Time, there was a ',('Hero',share.colors.hero),' ',\
                'named  ',('{heroname}',share.colors.hero),'. ',\
                'It was morning when ',('{hero_he}',share.colors.hero),' ',\
                'woke up from ',('bed',share.colors.item),'." ',\
                   ]
        # self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),record=False,scale=0.5))
        self.world=world.obj_world_wakeup(self)
        self.addpart(self.world)




class obj_scene_ch1play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)

class obj_scene_ch1play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"Then, ',\
                    ('{hero_he}',share.colors.hero),' ate the ',
                    ('fish',share.colors.item),' for dinner." ',\
                   ]
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)


class obj_scene_ch1play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play5())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"And finally, at night, ',('{hero_he}',share.colors.hero),' went to back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)



class obj_scene_ch1play5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def setup(self):
        self.text=[\
                   '"',('{hero_he}',share.colors.hero),' did that forever and was happy, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very basic story)',(640,280)) )

        self.addpart( draw.obj_image('bed',(400,530), scale=0.25) )
        self.addpart( draw.obj_image('herobase',(580,490), scale=0.25) )
        self.addpart( draw.obj_image('sun',(893,411), scale=0.25) )
        self.addpart( draw.obj_image('moon',(410,365), scale=0.25) )
        self.addpart( draw.obj_image('fish',(843,540), scale=0.15,rotate=90) )


class obj_scene_ch1playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1unlocknext())
    def setup(self):
        self.text=['And thats all the story for today, said the book of things. ',
                   'But tomorrow we will make this story even better! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )




class obj_scene_ch1unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def setup(self):
        self.text=['You have unlocked ',('Chapter II: The Partner',share.colors.instructions),'. ',\
                  'You can always redraw the hero, bed, sun and moon, fish and hook in ',\
                  ('Chapter I: The Hero',share.colors.instructions),'. '\
                   '',\
                   ]
        share.datamanager.updateprogress(chapter=2)# chapter 2 becomes available
        for c,value in enumerate(['herohead','bed','fish','hook','sun','moon']):
            self.addpart( draw.obj_image(value,(120+c*200,400), scale=0.4) )
















#
