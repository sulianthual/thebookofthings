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
        share.datamanager.setbookmark('ch1_start')
        self.text=['-----   Chapter I: The Hero   -----   ',\
                   '\n It was a new day for the book of things, the pen and the eraser. ',\
                  'The book of things said: today, we are going to write an amazing story. ',\
                  'Lets start by writing the first page. ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','pen','eraser') )
        animation1.addsound( "book1", [120] )
        animation1.addsound( "pen", [199] )
        animation1.addsound( "eraser", [185],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch1p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def soundnextpage(self):
        pass# no sound
    def textboxplace(self):
        self.textboxprevpage_xy=(1050,660)
        self.textboxnextpage_xy=(1230,660)
    def setup(self):
        share.datamanager.setbookmark('ch1_writehero')
        self.text=[\
                   'Lets write this, said the book of things: ',\
                   '"Once upon a time, there was a ',('hero',share.colors.hero),'". ',\
                   'Simple and to the point. ',\
                   'Well, lets give this ',('hero',share.colors.hero2),' a proper name and gender.',\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the hero\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('heroname',20,(750,yref), legend='hero name') )
        #
        self.addpart( draw.obj_textbox('and the hero was:',(180,yref+dyref)) )
        textchoice=draw.obj_textchoice('hero_he')
        textchoice.addchoice('1. A guy','he',(440,yref+dyref))
        textchoice.addchoice('2. A girl','she',(740,yref+dyref))
        textchoice.addchoice('3. A thing','it',(1040,yref+dyref))
        textchoice.addkey('hero_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('hero_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )
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
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch1') )



#*HEROHEAD *HEROBASE
class obj_scene_ch1p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def setup(self):
        share.datamanager.setbookmark('ch1_drawhero')
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempo2='['+share.datamanager.controlname('mouse2')+']'
        self.text=['Draw a happy face for ',('{heroname}',share.colors.hero),', said the book of things, ',\
                   'and make ', ('{hero_him}',share.colors.hero2),' look slightly to the right. ',\
                   ('Draw with '+tempo1+' and erase with '+tempo2+'',share.colors.instructions),', but you should know this by now.',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2)  )
        drawing=draw.obj_drawing('happyface',(640,450),legend='draw a happy face',shadow=(200,200))
        self.addpart( drawing )
        #
        self.addpart( draw.obj_music('ch1') )

class obj_scene_ch1p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p5())
    def setup(self):
        self.text=[\
                    'This is what ',('{heroname}',share.colors.hero),' looks like. ',\
                    'Not bad, said the book of things. ',\
                   'Indeed, ',('{hero_he}',share.colors.hero2),' looks very cool. ',\
                   'Lets move on to the next step. ',\
                   ]
        animation=draw.obj_animation('ch1_hero1','herobase',(360,360),record=False)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3') )
        animation.addsound( "hero1", [28] )
        animation.addsound( "hero2", [170] )
        animation.addsound( "hero3", [132] )
        #
        self.addpart( draw.obj_music('ch1') )




class obj_scene_ch1p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p6())
    def setup(self):
        share.datamanager.setbookmark('ch1_drawbed')
        self.text=['So far, our story goes as "Once upon a time, there was a ',('hero',share.colors.hero),'". ',\
                  'It aint much but its a start, said the book of things. ',\
                'Now, lets draw a ',('bed',share.colors.item),' ',\
                'such that our ',('hero',share.colors.hero2),' can wake up.',\
                   ]
        drawing=draw.obj_drawing('bed',(640,450),legend='draw a bed',shadow=(400,200))
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
        animation1=draw.obj_animation('ch1_hero1inbed','herobase',(360,360),record=False)
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch1_heroinbedZ','sleepZ',(700,400),record=True,sync=animation1,path='premade'))
        self.addpart( draw.obj_animation('ch1_heroinbedZ','sleepZ',(700+60,400-20),sync=animation1,path='premade',imgscale=0.7))
        self.addpart( draw.obj_animation('ch1_heroinbedZ','sleepZ',(700+100,400-30),sync=animation1,path='premade',imgscale=0.5))
        #
        # self.addpart( draw.obj_soundplacer(animation1,'wakeup_snore1','wakeup_snore2') )
        animation1.addsound( "wakeup_snore1", [14] )
        animation1.addsound( "wakeup_snore2", [134] )
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
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        tempor='['+share.datamanager.controlname('right')+']'
        self.text=[\
                  '... Huh...well, you actually need to hold '+tempor+' to wake up ',\
                  ('{heroname}',share.colors.hero),', said the book of things. ',\
                  ('{hero_he}',share.colors.hero2),' is quite lazy you know. ',\
                  ' And dont release '+tempor+' too soon or ',('{hero_he}',share.colors.hero2),\
                  ' will go straight back to sleep. ',\
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
        animation.addsound( "hero1", [28] )
        animation.addsound( "hero2", [170] )
        animation.addsound( "hero3", [132] )
        #
        self.addpart( draw.obj_music('ch1') )




class obj_scene_ch1p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p10())
    def setup(self):
        share.datamanager.setbookmark('ch1_drawfish')
        self.text=['Today we will have ',('{heroname}',share.colors.hero), \
                  ' take it easy, said the book of things. Lets just go  fishing. ',\
                'Draw a ',('fish',share.colors.item),' and a ',\
                ('hook',share.colors.item),' and we will be on our way. ',\

                   ]
        self.addpart(draw.obj_drawing('hook',(240,450),legend='draw a hook',shadow=(200,200)))
        self.addpart(draw.obj_drawing('fish',(940,450),legend='draw a fish (facing left)',shadow=(300,200)))
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
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        tempo='['+share.datamanager.controlname('down')+']. '
        self.text=['Lower the hook with '+tempo]
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
        share.datamanager.setbookmark('ch1_gotfish')
        self.text=[\
                    'Nice catch, said the book of thing, this ',\
                    ('{heroname}',share.colors.hero),' is going places. ',\
                    'Lets write down in our story: "',\
                    'the ',('hero',share.colors.hero),\
                    ' went fishing and caught a ',('fish',share.colors.item2),'". ',\
                   ]
        animation=draw.obj_animation('ch1_herofishmove','herobasefish',(640,360),record=False)
        self.addpart(animation)
        # self.addpart( draw.obj_soundplacer(animation,'hero1','hero2','hero3','hero4') )
        animation.addsound( "hero2", [22] )
        animation.addsound( "hero3", [193] )
        animation.addsound( "hero5", [82,240],skip=1 )
        #
        self.addpart( draw.obj_music('ch1') )



class obj_scene_ch1p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1p13())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def textboxnextpage(self):
        pass# no textbox for nextpage
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
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        tempol='['+share.datamanager.controlname('left')+']'
        self.text=[\
                    'That wraps it up for our first day, said the book of things. ',\
                    'Now, lets put our ',\
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
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch1_drawsun')
        self.text=[\
                   'And we finish with: "At night, the ',('hero',share.colors.hero),' went to back to bed". ',\
                   'One last thing, draw the ',('sun',share.colors.item),\
                   ' and the ',('moon',share.colors.item),\
                   ' so we know when it is day or night. ',\
                   ]
        # self.addpart(draw.obj_drawing('sun',(340,450),legend='Sun',shadow=(200,200)))
        self.addpart(draw.obj_drawing('sun',(300+50,450),legend='sun',shadow=(300,200)))
        self.addpart(draw.obj_drawing('moon',(1280-200-50,450),legend='moon',shadow=(200,200)))
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
        share.datamanager.setbookmark('ch1_startplay')
        self.text=[\
                    'That wraps it nicely, says the book of things. ',\
                   'Now, lets read our story one more time. ',\
                   ]
        animation=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation,scale=0.5)
        self.addpart(animation)
        self.addpart(animation2)
        self.addpart(animation3)

        # self.addpart( draw.obj_soundplacer(animation,'book1','book2','pen','eraser') )
        animation.addsound( "book1", [120] )
        animation.addsound( "pen", [199] )
        animation.addsound( "eraser", [185],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )



class obj_scene_ch1play1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                '"Once upon a time, there was a ',('hero',share.colors.hero),' ',\
                'named  ',('{heroname}',share.colors.hero),'. ',\
                'It was morning when ',('{hero_he}',share.colors.hero2),' ',\
                'woke up from ',('bed',share.colors.item2),'." ',\
                   ]
        # self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),record=False,scale=0.5))
        self.world=world.obj_world_wakeup(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('sunrise_end')# rooster
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )




class obj_scene_ch1play2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),\
                     ' went fishing and caught a ',\
                     ('fish',share.colors.item2),'."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch1play3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play4())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                    '"',\
                    ('{heroname}',share.colors.hero),' ate the ',
                    ('fish',share.colors.item2),' for dinner." ',\
                   ]
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch1play4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1play3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def triggernextpage(self,controls):
        return (share.devmode and controls.ga and controls.gac) or self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        self.text=[\
                   '"And at night, ',('{heroname}',share.colors.hero),' went back to ',\
                   ('bed',share.colors.item2),'." ',\
                   ]
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('sunset_end')# rooster
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


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
        animation1=draw.obj_animation('bookmove','book',(640,360))
        self.addpart( animation1 )
        #
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [170] )
        animation1.addsound( "book1", [149] )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )




class obj_scene_ch1unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch1playend())
    def setup(self):
        share.datamanager.setbookmark('ch1_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter II',share.colors.instructions),'! ',\
                   ]
        share.datamanager.updateprogress(chapter=2)# chapter 2 becomes available
        #
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )
















#
