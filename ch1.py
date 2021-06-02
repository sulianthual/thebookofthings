record=Falserecord=False#!/usr/bin/env python3
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
        share.scenemanager.switchscene(obj_scene_ch1p0())
    def triggernextpage(self,controls):
        return True
    def soundnextpage(self):
        pass# no sound

class obj_scene_ch1p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p1())
    def setup(self):
        self.text=['-----   Chapter I: The Hero   -----   ',\
                   '\n It was a new day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Today, we are going to write an amazing story. ',\
                  'Lets start by writing the first page." ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)
        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [46, 95] )
        animation.addsound( "book2", [63] )
        animation.addsound( "pen", [199] )
        animation.addsound( "eraser", [185],skip=1 )
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch1p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def setup(self):
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempom='['+share.datamanager.controlname('mouse')+']'
        tempok='['+share.datamanager.controlname('keyboard')+']'
        self.text=[\
                   'Lets write this, said the book of things: "Once upon a time, there was a ',('hero',share.colors.hero),'". ',\
                   'Simple and to the point. ',\
                   'Well, lets give this ',('hero',share.colors.hero2),' a proper name and gender.',\
                  '\n\n ',\
                  ('Hover over the name box below with the '+tempom+' then type a name using the '+tempok+'. ',share.colors.instructions),\
                 ('Then, choose a gender with '+tempo1+'. ',share.colors.instructions),\
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
        self.addpart(draw.obj_animation('ch1_pen2','pen',(1180,400),record=False,scale=0.5))
        #
        self.addpart( draw.obj_music('ch1') )



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
        animation=draw.obj_animation('ch1_stickbase1','stickbase',(640,360),scale=0.75,record=False,path='premade')
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'tadah') )
        animation.addsound( "tadah", [10] )
        #
        self.addpart( draw.obj_music('ch1') )



#*HEROHEAD *HEROBASE
class obj_scene_ch1p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def setup(self):
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempo2='['+share.datamanager.controlname('mouse2')+']'
        self.text=['Draw a happy face for ',('{heroname}',share.colors.hero),', said the book of things, ',\
                   'and make ', ('{hero_him}',share.colors.hero2),' look slightly to the right. ',\
                   ('Draw with '+tempo1+' and erase with '+tempo2+'',share.colors.instructions),', but you should know this by now.',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2)  )
        drawing=draw.obj_drawing('happyface',(640,450),legend='Draw a Happy Face',shadow=(200,200))
        self.addpart( drawing )
        #
        self.addpart( draw.obj_music('ch1') )

class obj_scene_ch1p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p5())
    def setup(self):
        self.text=['So this is what ',('{heroname}',share.colors.hero),' looks like. ',\
                    'Not bad, said the book of things. ',\
                   'Indeed, ',('{hero_he}',share.colors.hero2),' looks very cool. ',\
                   'Lets move on to the next step. ',\
                   ]
        animation=draw.obj_animation('ch1_hero1','herobase',(360,360),record=False)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3') )
        animation.addsound( "hero1", [28] )
        animation.addsound( "hero2", [222] )
        animation.addsound( "hero3", [124] )
        #
        self.addpart( draw.obj_music('ch1') )




class obj_scene_ch1p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p6())
    def setup(self):
        self.text=['So far, our story goes as "Once upon a Time, There was a ',('hero',share.colors.hero),'". ',\
                  'It aint much but its a start, said the book of things. ',\
                'Now, lets draw a ',('bed',share.colors.item),' ',\
                'such that our ',('hero',share.colors.hero2),' can wake up.',\
                   ]
        drawing=draw.obj_drawing('bed',(640,450),legend='Draw a Bed',shadow=(400,200))
        self.addpart( drawing )
        #
        self.addpart( draw.obj_music('ch1') )



class obj_scene_ch1p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p7())
    def setup(self):
        self.text=['Well done, so lets write down: "It was morning when ',\
                  ('{heroname}',share.colors.hero),' the ',('hero',share.colors.hero2),\
                  ' woke up from ',('bed',share.colors.item2),\
                  '". We are off to a great start, said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        # self.addpart( draw.obj_image('herobase',(420,490), scale=0.7,rotate=80) )
        # self.addpart(draw.obj_animation('ch1_heroawakes','herobase',(640,360),record=False,scale=0.7))
        # self.addpart( draw.obj_image('herobase',(903,452), scale=0.7) )
        # self.addpart( draw.obj_soundplacer(animation,'cute1','cute2') )
        animation=draw.obj_animation('ch1_hero1inbed','herobase',(360,360),record=False)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'snore1','snore2') )
        animation.addsound( "snore1", [14] )
        animation.addsound( "snore2", [134] )
        #
        self.addpart( draw.obj_music('ch1') )



# mini game wake up
class obj_scene_ch1p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p8())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempor='['+share.datamanager.controlname('right')+']'
        self.text=[\
                  '... Huh...well, you actually need to hold '+tempor+' to wake ',\
                  ('{heroname}',share.colors.hero),\
                  ' from ',('bed',share.colors.item2),', said the book of things. ',\
                  ('{hero_he}',share.colors.hero2),' is quite lazy you know. ',\
                  ' And dont release '+tempor+' too soon or ',('{hero_he}',share.colors.hero2),\
                  ' will go straight back to sleep. ',\
                  ' When ',('{heroname}',share.colors.hero),' is fully awake, we will move on. ',\
                   ]
        self.world=world.obj_world_wakeup(self,sun=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1') )



class obj_scene_ch1p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p9())
    def setup(self):
        self.text=['Finally, ',('{heroname}',share.colors.hero),' is awake. ',\
                    ' Well done, said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        animation=draw.obj_animation('ch1_awaken','herobase',(640,360),record=False,scale=0.7)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3') )
        animation.addsound( "hero1", [17] )
        animation.addsound( "hero2", [265] )
        animation.addsound( "hero3", [220] )
        #
        self.addpart( draw.obj_music('ch1') )




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
        #
        self.addpart( draw.obj_music('ch1') )


class obj_scene_ch1p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p11())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempo='['+share.datamanager.controlname('down')+']'
        self.text=[\
                    ' Lower the hook with '+tempo+' and catch a fish. ',\
                   ]
        self.world=world.obj_world_fishing(self)# fishing mini-game
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1') )




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
                    ('{heroname}',share.colors.hero),' the ',('hero',share.colors.hero2),\
                    ' went fishing and caught a ',('fish',share.colors.item2),'". ',\
                   ]
        animation=draw.obj_animation('ch1_herofishmove','herobasefish',(640,360),record=False)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3','hero4') )
        animation.addsound( "hero2", [22] )
        animation.addsound( "hero3", [193] )
        animation.addsound( "hero4", [82,240],skip=1 )
        #
        self.addpart( draw.obj_music('ch1') )



class obj_scene_ch1p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p13())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempol='['+share.datamanager.controlname('left')+']'
        tempor='['+share.datamanager.controlname('right')+']'
        self.text=[\
                    ' Moving on, said the book of things. Lets write down: ',\
                    ' "',('{heroname}',share.colors.hero),' ate the ',
                    ('fish',share.colors.item2),' for dinner." ',\
                    'Do it by ',('alternating '+tempol+' and '+tempor+'',share.colors.black),'. ',\
                   ]
        self.world=world.obj_world_eatfish(self)# fishing mini-game
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1') )


class obj_scene_ch1p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p14())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempol='['+share.datamanager.controlname('left')+']'
        self.text=[\
                    'Nicely done, said the book of things. ',\
                    'That wraps it up for our first day. Now, lets put our ',\
                    ('hero',share.colors.hero),' back to sleep. ',\
                    ' Hold '+tempol+', and dont release',\
                    ' or this procrastinator will stay awake all night. ',\
                   ]
        self.world=world.obj_world_gotobed(self,addmoon=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1') )


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
        #
        self.addpart( draw.obj_music('ch1') )


##########################################################
##########################################################
# PLAY CHAPTER


class obj_scene_ch1play(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play1())
    def setup(self):
        self.text=[\
                   'Now, lets read again our story to summarize, said the book of things. ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)
        #
        self.addpart( draw.obj_music('tension') )
        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [46] )
        animation.addsound( "book2", [55] )
        animation.addsound( "pen", [189] )
        animation.addsound( "eraser", [199] )


class obj_scene_ch1play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                '"Once upon a Time, there was a ',('hero',share.colors.hero),' ',\
                'named  ',('{heroname}',share.colors.hero),'. ',\
                'It was morning when ',('{hero_he}',share.colors.hero2),' ',\
                'woke up from ',('bed',share.colors.item2),'." ',\
                   ]
        # self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),record=False,scale=0.5))
        self.world=world.obj_world_wakeup(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1play') )




class obj_scene_ch1play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went fishing and caugth a ',\
                     ('fish',share.colors.item2),'."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1play') )

class obj_scene_ch1play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' ate the ',
                    ('fish',share.colors.item2),' for dinner." ',\
                   ]
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1play') )


class obj_scene_ch1play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                   '"And at night, ',('{heroname}',share.colors.hero),' went back to ',\
                   ('bed',share.colors.item2),'". ',\
                   ]
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch1play') )


class obj_scene_ch1playend(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1unlocknext())
    def setup(self):
        self.text=[\
                   '"',('{hero_he}',share.colors.hero2),' did that forever and was happy, the end". ',\
                    'And thats all the story for today, said the book of things. ',
                   'But tomorrow we will make this story even better! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )
        #
        self.addpart( draw.obj_music('tension') )




class obj_scene_ch1unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter II',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=2)# chapter 2 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('tension') )
















#
