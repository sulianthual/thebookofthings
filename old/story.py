#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# story.py: the story
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


# Progress (unlock some scenes/contents depending on current progress)
def event_unlocked(eventname):
    #
    # Scenes unlock (main progression)
    if eventname=='scene_maincharacter':# hero exists after completing story once
        return True#share.datamanager.unlocked('scene_end')
    elif eventname=='scene_startlocation':# location after completing one day
        return share.datamanager.unlocked('make_gotobed')
    #
    # Make Stuff
    elif eventname=='make_hero':
        return share.datamanager.unlocked('make_hero')
    elif eventname=='make_wakeup':
        return share.datamanager.unlocked('make_wakeup')
    elif eventname=='make_fishing':
        return share.datamanager.unlocked('make_fishing')
    elif eventname=='make_gotobed':
        return share.datamanager.unlocked('make_gotobed')
    elif eventname=='make_house':
        return share.datamanager.unlocked('make_house')
    elif eventname=='play_sunrise':# sunrise needs house+trees
        return share.datamanager.unlocked('make_house')
    elif eventname=='play_nightfall':# nightfall too
        return share.datamanager.unlocked('make_house')
##########################################################
##########################################################


# Story main events
# *STORY

# beginning
class obj_scene_story(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_maincharacter())
    def setup(self):
        self.text=['Once upon a time ',\
                   ]


#### CHOOSE MAIN CHARACTER (SETTING OF STORY)
# (for now we only have one main character)
class obj_scene_maincharacter(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('scene_maincharacter'):
            share.scenemanager.switchscene(obj_scene_maincharacter_hero())
        else:
            share.scenemanager.switchscene(obj_scene_end())
    def setup(self):
        if event_unlocked('scene_maincharacter'):
            if event_unlocked('make_hero'):
                self.text=['There was a hero called ',('{heroname}',share.colors.hero)]
            else:
                self.text=['There was a hero ']
        else:
            self.text=['There was nothing ']


#### CHOOSE START LOCATION (SETTING OF STORY)
class obj_scene_startlocation(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('scene_startlocation'):
            share.scenemanager.switchscene(obj_scene_startlocation_house())# make house
        else:
            share.scenemanager.switchscene(obj_scene_startday())# skip entirely
    def triggernextpage(self,controls):
        return True


#### START THE DAY (SETTING OF STORY)
class obj_scene_startday(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_startday_sunrise())
    def triggernextpage(self,controls):
        return True


#### CHOOSE MORNING ACTIVITY (SETTING OF STORY)
class obj_scene_morningactivity(page.obj_chapterpage):
    def nextpage(self):
        if share.datamanager.getword('choice_morningactivity')=='fishing':
            share.scenemanager.switchscene(obj_scene_fishing())
        else:
            share.scenemanager.switchscene(obj_scene_end())
    def setup(self):
        self.text=['During the morning, ',('{heroname}',share.colors.hero),': ']
        textchoice=draw.obj_textchoice('choice_morningactivity')
        y1=150
        textchoice.addchoice('1. went fishing','fishing',(150,y1))
        self.addpart( textchoice )


#### CHOOSE MIDDAY EVENT (DISRUPTIVE EVENT)
class obj_scene_middayevent(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_eveningactivity())
    def setup(self):
        self.text=['A great day went by. ']


#### CHOOSE EVENING ACTIVITY (RESOLUTION AFTER CLIMAX)
class obj_scene_eveningactivity(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_endday())
    def triggernextpage(self,controls):
        return True


#### END THE DAY (END OF STORY)
class obj_scene_endday(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall())
    def triggernextpage(self,controls):
        return True


##########################################################
##########################################################
# The Hero

class obj_scene_maincharacter_hero(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('make_hero'):
            share.scenemanager.switchscene(obj_scene_startlocation())
        else:
            share.scenemanager.switchscene(obj_scene_make_hero())
    def triggernextpage(self,controls):
        return True


###########
# make the hero
class obj_scene_make_hero(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_make_hero2())
    def setup(self):
        self.text=[]
        y1=200
        self.addpart( draw.obj_textbox("The Hero\'s Name was:",(200,y1)) )
        self.addpart( draw.obj_textinput('heroname',25,(750,y1),color=share.colors.hero, legend='Hero Name') )
        self.addpart( draw.obj_textbox('and the hero was:',(180,y1+100)) )
        textchoice=draw.obj_textchoice('hero_he')
        textchoice.addchoice('1. A guy','he',(440,y1+100))
        textchoice.addchoice('2. A girl','she',(740,y1+100))
        textchoice.addchoice('3. A thing','it',(1040,y1+100))
        textchoice.addkey('hero_his',{'he':'his','she':'her','it':'its'})
        textchoice.addkey('hero_him',{'he':'him','she':'her','it':'it'})
        self.addpart( textchoice )

class obj_scene_make_hero2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_make_hero3())
    def setup(self):
        self.text=[\
                    ('{heroname}',share.colors.hero),' looked like this. ',\
                   ]
        self.addpart( draw.obj_drawing('herohead',(640,450),legend='Draw a happy face (facing right) ') )
    def endpage(self):
        super().endpage()
        # combine herohead+stickbody = herobase
        image1=draw.obj_image('stickbody',(640,460),path='premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herobase')
        # combine herohead+stickwalk = herowalk
        image1=draw.obj_image('stickwalk',(640,460),path='premade')# snapshot
        image2=draw.obj_image('herohead',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((640,360,200,300),'herowalk')

class obj_scene_make_hero3(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_maincharacter_hero())# loop back
    def setup(self):
        self.text=['This is what ',('{heroname}',share.colors.hero),' looked like. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','herobase',(360,360),record=True))
    def endpage(self):
        super().endpage()
        share.datamanager.unlock('make_hero')

##########################################################
##########################################################
# The House

class obj_scene_startlocation_house(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('make_house'):
            share.scenemanager.switchscene(obj_scene_startday())
        else:
            share.scenemanager.switchscene(obj_scene_make_house())
    def triggernextpage(self,controls):
        return True



class obj_scene_make_house(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_startlocation_house())
    def setup(self):
        self.text=[('{hero_he}',share.colors.hero),' lived in a house with trees. ']
        self.addpart( draw.obj_drawing('house',(340,450),legend='Draw a House',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('tree',(940,450),legend='Draw a Tree',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        share.datamanager.unlock('make_house')

##########################################################
##########################################################
# Sunrise

class obj_scene_startday_sunrise(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('play_sunrise'):
            share.scenemanager.switchscene(obj_scene_play_sunrise())
        else:
            share.scenemanager.switchscene(obj_scene_wakeup())
    def triggernextpage(self,controls):
        return True


class obj_scene_play_sunrise(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=['It was morning and the sun was rising. ']
        self.world=world.obj_world_sunrise(self)
        self.addpart(self.world)

##########################################################
##########################################################
# Wake Up

class obj_scene_wakeup(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('make_wakeup'):
            share.scenemanager.switchscene(obj_scene_play_wakeup())
        else:
            share.scenemanager.switchscene(obj_scene_make_wakeup())
    def triggernextpage(self,controls):
        return True


class obj_scene_make_wakeup(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_make_wakeup2())
    def setup(self):
        self.text=['It was morning. ']
        self.addpart(draw.obj_drawing('sun',(640,450),legend='Draw the Sun',shadow=(300,200)))

class obj_scene_make_wakeup2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())# loop back
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' was in bed. ']
        self.addpart( draw.obj_drawing('bed',(640,450),legend='Draw a Bed',shadow=(400,200)) )
    def endpage(self):
        super().endpage()
        share.datamanager.unlock('make_wakeup')


class obj_scene_play_wakeup(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_play_wakeup2())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' woke up. ']
        self.world=world.obj_world_wakeup(self)
        self.addpart(self.world)


class obj_scene_play_wakeup2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_morningactivity())
    def setup(self):
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        self.addpart(draw.obj_animation('ch1_awaken','herobase',(640,360),record=False,scale=0.7))



##########################################################
##########################################################
# Fishing

class obj_scene_fishing(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('make_fishing'):
            share.scenemanager.switchscene(obj_scene_play_fishing())
        else:
            share.scenemanager.switchscene(obj_scene_make_fishing())
    def page(self,controls):
        super().page(controls)
        self.nextpage()


class obj_scene_make_fishing(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())# loop back
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' went fishing. ']
        self.addpart(draw.obj_drawing('hook',(240,450),legend='Draw a Hook',shadow=(200,200)))
        self.addpart(draw.obj_drawing('fish',(940,450),legend='Draw a Fish (Facing Left)',shadow=(300,200)))
    def endpage(self):
        super().endpage()
        share.datamanager.unlock('make_fishing')


class obj_scene_play_fishing(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_caughtfish())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[]
        self.world=world.obj_world_fishing(self)# fishing mini-game
        self.addpart(self.world)

class obj_scene_caughtfish(page.obj_chapterpage):
    def nextpage(self):
        if share.datamanager.getword('choice_caughtfish')=='eat':
            share.scenemanager.switchscene(obj_scene_eatfish())
        else:
            share.scenemanager.switchscene(obj_scene_middayevent())
    def presetup(self):
        super().presetup()
        # combine hero+fish into: hero holding fish
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('herobase',(640,452), scale=0.7))
        dispgroup1.addpart('part2',draw.obj_image('fish',(776,486), scale=0.4,rotate=-90))
        dispgroup1.snapshot((700,452,200,260),'herobasefish')
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' caught a fish. ',\
                    ('{hero_he}',share.colors.hero),' decided to: ',\
                    ]
        self.addpart(draw.obj_animation('ch1_herofishmove','herobasefish',(640,360),record=True))
        y1=150
        textchoice=draw.obj_textchoice('choice_caughtfish')
        textchoice.addchoice('1. Eat the fish','eat',(440,y1))
        textchoice.addchoice('2. Keep the fish','keep',(740,y1))
        self.addpart( textchoice )


class obj_scene_eatfish(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_middayevent())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' ate the fish. ']
        self.world=world.obj_world_eatfish(self)# fishing mini-game
        self.addpart(self.world)

##########################################################
##########################################################
# Nightfall

class obj_scene_nightfall(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('play_nightfall'):
            share.scenemanager.switchscene(obj_scene_play_nightfall())
        else:
            share.scenemanager.switchscene(obj_scene_gotobed())
    def triggernextpage(self,controls):
        return True


class obj_scene_play_nightfall(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_gotobed())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=['It was already night. ']
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)

##########################################################
##########################################################
# Go to bed

class obj_scene_gotobed(page.obj_chapterpage):
    def nextpage(self):
        if event_unlocked('make_gotobed'):
            share.scenemanager.switchscene(obj_scene_play_gotobed())
        else:
            share.scenemanager.switchscene(obj_scene_make_gotobed())
    def triggernextpage(self,controls):
        return True


class obj_scene_make_gotobed(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_gotobed())# loop back
    def setup(self):
        self.text=['It was night. ']
        self.addpart(draw.obj_drawing('moon',(640,450),legend='Draw the Moon',shadow=(200,200)))
    def endpage(self):
        super().endpage()
        share.datamanager.unlock('make_gotobed')


class obj_scene_play_gotobed(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_end())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[('{heroname}',share.colors.hero),' went to bed. ']
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)





##########################################################
##########################################################

class obj_scene_end(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_end2())
    def setup(self):
        self.text=['The end']
        share.datamanager.unlock('scene_end')

class obj_scene_end2(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_story())# loop back
    def setup(self):
        self.text=['...']

##########################################################
##########################################################
