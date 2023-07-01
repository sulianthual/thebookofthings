#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter4.py: ...
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

# Chapter IV: ...
# *CHAPTER IV



class obj_scene_chapter4(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def setup(self):
        share.datamanager.setbookmark('ch4_start')
        self.text=['-----   Chapter IV: Cave Dwellers   -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: well, lets continue our story where we left. ',\
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




# class obj_scene_ch4p3(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_chapter4())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p4())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def soundnextpage(self):
#         pass# no sound
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         share.datamanager.setbookmark('ch4_startstory')
#         self.text=[\
#                '"',\
#                ('{partnername}',share.colors.partner),' was captive in the ',\
#                  ('evil tower',share.colors.location2),', and ',\
#                  ('{heroname}',share.colors.hero),' needed to visit three ',\
#                  ('evil grandmasters',share.colors.grandmaster),'. ',\
#                 'It was morning and the sun was rising." ',\
#                    ]
#         self.world=world.obj_world_sunrise(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter4())
    def nextpage(self):
        # share.scenemanager.switchscene(obj_scene_ch4p5())
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=['"',\
                ('{heroname}',share.colors.hero),' ',\
                'woke up from bed with ',\
                ('{hero_his}',share.colors.hero2),\
                ' loyal sidekick ',('{bug}',share.colors.bug),'." ',\
                   ]
        self.text=[\
               '"',\
               ('{partnername}',share.colors.partner),' was captive in the ',\
                 ('evil tower',share.colors.location2),', and ',\
                 ('{heroname}',share.colors.hero),' needed to visit three ',\
                 ('evil grandmasters',share.colors.grandmaster),'. ',\
                ('{hero_he}',share.colors.hero2),' ',\
                'woke up with ',\
                ('{hero_his}',share.colors.hero2),\
                ' loyal sidekick ',('{bug}',share.colors.bug),'." ',\
                   ]


        self.world=world.obj_world_wakeup(self,bug=True,alarmclock=False)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p6(page.obj_chapterpage):
    def prevpage(self):
        # share.scenemanager.switchscene(obj_scene_ch4p5())
        share.scenemanager.switchscene(obj_scene_ch4p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch4_checkmail')
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero2),' mailbox. ',\
                    ('{hero_he}',share.colors.hero2),' had received ',\
                    'a ',' letter." ',\
                   ]
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='data/premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'hero1','hero2','hero3','hero4','hero5','hero6','mailjump') )
        animation1.addsound( "hero2", [82] )
        animation1.addsound( "mailjump", [7] )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def textboxset(self):
        self.textboxopt={'xy':(1230-180,55)}
    def setup(self):
        self.addpart( draw.obj_textbox('"The letter said:"',(50,53),xleft=True) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',('{heroname}',share.colors.hero),', ',\
                    '\nWasup. Last time I checked, ',('{partnername}',share.colors.partner),\
                    ' is still in my ',\
                     ('evil tower',share.colors.location2),'. Come save ',\
                     ('{partner_him}',share.colors.partner2),' if you dare. ',\
                     'Whenever, muahahahaha. ',\
                    '\n\nsigned: ',('{villainname}',share.colors.villain),\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='data/premade') )
        # self.addpart( draw.obj_image('villainhead',(1065,305),scale=0.5) )
        #
        animation1=draw.obj_animation('ch2_mailhead','villainhead',(640,360),imgscale=0.7)
        self.addpart(animation1)
        animation1.addsound( "villain2", [100],skip=1 )
        #
        self.sound=draw.obj_sound('mailopen')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def setup(self):
        share.datamanager.setbookmark('ch4_drawcave')
        self.text=['"',\
                    ('{heroname}',share.colors.hero),' went to seek the first ',\
                    ('evil grandmaster',share.colors.grandmaster),\
                    ' that lived in a magical cave in a dark forest." ',\
                    'Draw a ',('cave',share.colors.item),\
                    ' and a ',('tree',share.colors.item),'. ',\
                   ]
        self.addpart( draw.obj_drawing('cavedraw',(340,450-50),legend='cave',shadow=(250,250),brush=share.brushes.pen10) )
        self.addpart( draw.obj_drawing('treedraw',(940,450-50),legend='tree',shadow=(250,250),brush=share.brushes.pen10) )
        #
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10aa())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                'go to the magical cave in the east',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='forest',chapter=4)
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('ch4') )

class obj_scene_ch4p10aa(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10a())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):

        self.text=[\
                '"It was always night in the dark forest. ',
                ' As soon as ',('{heroname}',share.colors.hero),' stepped in, the sun disappeared." ',\
                   ]
        self.addpart( draw.obj_image('tree',(99,411),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.world=world.obj_world_sunset(self,type='forest')
        self.addpart(self.world)
        #
        self.addpart( draw.obj_image('tree',(1156,430),scale=0.4,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(870,422),scale=0.35,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(273,424),scale=0.42,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(452,598),scale=0.38,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,560),scale=0.4,rotate=0,fliph=False,flipv=False) )

        self.addpart( draw.obj_music('ch4') )

#########################
#### 3d minigame sequence
class obj_scene_ch4p10a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10aa())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10b())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        share.datamanager.setbookmark('ch4_enterforest')
        self.text=['"The dark forest was all 3D with next generation graphics, Wow. ',\
            'Go to the ',('marker',share.colors.red),'. ']
        self.world=world.obj_world_3dforest_enter(self)# fishing mini-game
        self.addpart(self.world)
        self.addpart( draw.obj_music('ch4') )


class obj_scene_ch4p10b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10c())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['go to the next ',('marker',share.colors.red),'.']
        self.world=world.obj_world_3dforest_enter2(self)# fishing mini-game
        self.addpart(self.world)
        self.addpart( draw.obj_music('ch4') )

class obj_scene_ch4p10c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10d())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['check the ',('magical cave',share.colors.red),'.']
        self.world=world.obj_world_3dforest_checkcave(self)# fishing mini-game
        self.addpart(self.world)
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p10d(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10c())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' checked the magical cave. ',\
                'An outwordly voice shouted from inside: who dares disturb me from my slumber."',\
                   ]

        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(1076,187),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_cavestatic','cave',(640,360),record=False)
        self.addpart( animation1 )
        # self.addpart( draw.obj_imageplacer(self,'moon','cave','tree','bunnybody') )
        #
        animation1.addsound( "bunny_cave", [1])
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p10d())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def textboxset(self):
        self.textboxopt={'xy':(750,410),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch4_writebunny')
        self.text=[\
                '"Inside the ',('magical cave',share.colors.location2),' ',\
                'was a terrifying ',('monster',share.colors.bunny),'." ',\
                'Uh oh, this doesnt look too good, said the book of things. ',\
                'Choose a name for the ',('monster',share.colors.bunny),'. ',\
                   ]
        yref=260
        dyref=120
        self.addpart( draw.obj_textbox("the monster\'s name was:",(200,yref)) )
        self.addpart( draw.obj_textinput('bunnyname',20,(750,yref), legend='monster name') )
        #
        self.addpart( draw.obj_music('bunny') )
        #


class obj_scene_ch4p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12a())
    def setup(self):
        self.text=['"The ',('monster',share.colors.bunny),\
            '\'s face had a weird everything. ',\
            'It may have been some eyes, fangs, horns, hair or gills, but something clearly wasn\'t right." ']
        # self.addpart( draw.obj_image('bunnystickhead',(640,360+150-10),scale=0.75,path='data/premade') )
        # self.addpart( draw.obj_drawing('bunnyfacedraw',(640,360-10),legend='draw a bunny head (facing right)',shadow=(400,300)) )
        self.addpart( draw.obj_image('bunnystickheadnew',(640,260-10),path='data/premade') )
        self.addpart( draw.obj_drawing('bunnyfacedraw',(640,260+100-10),legend='draw the monster head (facing right)',shadow=(200,200)) )
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p12a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def setup(self):
        self.text=['"The ',('monster',share.colors.bunny),\
            '\'s body was even worse. ',\
            'It may have been some hairy legs, scales, wings or tentacles, but it was clearly beyond description." ']
        self.textkeys={'pos':(50,200),'xmax':600}
        self.addpart( draw.obj_drawing('bunnybodydraw',(640+300,400+98-100),legend='draw the monster\'s body (facing right)',shadow=(300,233)) )
        self.addpart( draw.obj_image('bunnyhead',(640+300,400-225-100),scale=0.75) )
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p12a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        self.text=[\
                'Lets do this: "',\
                '"The ',('monster',share.colors.bunny2),' called ',\
                ('{bunnyname}',share.colors.bunny),' emerged from the magical cave." ',\
                ' Dont be fooled by its short size, said the book of things, this thing is nasty. ',\
                   ]
        # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
        self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(1076,187),scale=0.35,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bunnybase',(867,525),scale=0.62,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        # animation1.addsound( "bunny2", [128] )
        animation1.addsound( "bunny4", [43,128],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )




class obj_scene_ch4p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16tuto())
    def setup(self):
        self.text=[\
                '"The ',('monster',share.colors.bunny2),\
                ' said: I am ',('{bunnyname}',share.colors.bunny),', ',\
                ' the ',('evil grandmaster',share.colors.grandmaster),\
                ' of the east, and I will break your bones!"']
        animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [80] )
        animation1.addsound( "bunny2", [16],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16tuto(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16tuto2())
    def setup(self):
        share.datamanager.setbookmark('ch4_fightsmallbunny')
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=['This is your health. Dont loose it or you will die.']
        self.world=world.obj_world_3dforest_rabbitescape(self)# fishing mini-game
        self.world.freezeworld=True# freeze the world
        self.world.staticactor.dict["cross"].show=False# hide cross
        self.addpart(self.world)
        self.addpart(draw.obj_image('show1',(900,200),path='data/premade',fliph=True,flipv=True))
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16tuto2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16tuto())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16a())
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        tempo='['+share.datamanager.controlname('action')+']'
        self.text=[' Press ',\
                    (tempo,share.colors.instructions),\
                    ' when you are ready. ']
        self.world=world.obj_world_3dforest_rabbitescape(self)# fishing mini-game
        self.world.freezeworld=True# freeze the world
        self.world.staticactor.dict["cross"].show=False# hide cross
        self.addpart(self.world)
        self.addpart( draw.obj_textbox('press '+tempo+' to start',(640,150),color=share.colors.instructions) )
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16a(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16tuto2())
    def nextpage(self):
        if share.devmode or self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p16b())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16adeath())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['Find an ',('exit',share.colors.red),'.']
        self.world=world.obj_world_3dforest_rabbitescape(self)# fishing mini-game
        self.addpart(self.world)
        self.world.addstartfightmessage()# add start fight message
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p16adeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16a())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4p16a())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16b())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p16b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16a())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16c())
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' valiantly retreated into the bushes. ',\
                'Look, said ',('{bug}',share.colors.bug),\
                ', its a gun right there! Better grab it.'\
                   ]
        self.addpart( draw.obj_image('gun',(640,500), scale=0.5,rotate=90) )
        self.addpart( draw.obj_image('bush',(841,376),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(361,418),scale=0.55,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(143,511),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(517,235),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(311,243),scale=0.45,rotate=0,fliph=True,flipv=False) )

        animation1=draw.obj_animation('ch4_heroinbushes','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_buginbushes','bug',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        # animation1.addsound( "bunny2", [25,75,125,175,225])
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16c(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16d())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['Get the ',('gun',share.colors.item),'.']
        self.world=world.obj_world_3dforest_findgun(self)# fishing mini-game
        self.addpart(self.world)
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p16d(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16c())
    def nextpage(self):
        if share.devmode or self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p16e())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16ddeath())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['shoot ',('{bunnyname}',share.colors.bunny),'.']
        self.world=world.obj_world_3dforest_rabbitshootone(self)# fishing mini-game
        self.addpart(self.world)
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p16ddeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16d())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4p16d())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16e())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch4p16e(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16d())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16f())
    def setup(self):
        self.text=[\
                'Ouch, that hurt, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'You will pay me for this.'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'moon','bunnybase','tree','bush','sun','cave'))
        self.addpart( draw.obj_image('herobase',(261,390),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(995,193),scale=0.33,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(519,402),scale=0.41,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('bush',(1172,530),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1166,318),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(660,285),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(469,271),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(92,258),scale=0.39,rotate=0,fliph=False,flipv=False) )

        animation1=draw.obj_animation('ch4_bunnygetsbackupe','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [19, 138],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16f(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16e())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16g())
    def setup(self):
        share.datamanager.setbookmark('ch4_shootrabbits')
        self.text=[\
                'Now witness my power, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'Demultiply and attack!'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'herobase','bunnybase','tree','bush','sun','cave'))
        self.addpart( draw.obj_image('bunnybase',(615,370),scale=0.69,rotate=0,fliph=True,flipv=False) )

        animation1=draw.obj_animation('ch4_bunnydemult1','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_bunnydemult2','bunnybase',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch4_bunnydemult3','bunnybase',(640,360),record=False,sync=animation1)
        self.addpart( animation3 )
        animation4=draw.obj_animation('ch4_bunnydemult4','bunnybase',(640,360),record=False,sync=animation1)
        self.addpart( animation4 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny2", [50] )
        animation1.addsound( "bunny4", [141],skip=1 )

        # animation1.addsound( "bunny5", [19, 138],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16g(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16f())
    def nextpage(self):
        if share.devmode or self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p16h())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16gdeath())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['shoot all the ',('monsters',share.colors.bunny),'.']
        self.world=world.obj_world_3dforest_rabbitshoot(self)
        self.addpart(self.world)
        self.world.addstartfightmessage()# add start fight message
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p16gdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16g())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4p16g())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16h())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p16h(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16g())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16i())
    def setup(self):
        self.text=[\
                'No no no noooo, said ',('{bunnyname}',share.colors.bunny),'.',\
                'This is humiliating. '\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'herobase','bunnybase','tree','bush','sun','cave'))
        self.addpart( draw.obj_image('herobase',(261,390),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(995,193),scale=0.33,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1166,318),scale=0.52,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(660,285),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(469,271),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(92,258),scale=0.39,rotate=0,fliph=False,flipv=False) )

        animation1=draw.obj_animation('ch4_bunnygetsbackupe','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [19, 138],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16i(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16h())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16j())
    def setup(self):
        share.datamanager.setbookmark('ch4_fightbigbunny')
        self.text=[\
                'But that is fine. Now witness my final form, Expand and Destroy!'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'moon','bush','sun','cave'))
        self.addpart( draw.obj_image('tree',(290,477),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(97,486),scale=0.46,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cave',(1148,504),scale=0.46,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(933,502),scale=0.41,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('moon',(1043,321),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_bunnygrwos','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny4", [70,270,360] )
        animation1.addsound( "bunny2", [100, 174] )
        # animation1.addsound( "bunny5", [19, 138],skip=1)
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16j(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16i())
    def nextpage(self):
        if share.devmode or self.world.win:
            share.scenemanager.switchscene(obj_scene_ch4p16k())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16jdeath())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['find a way to ',('escape',share.colors.red),'.']
        self.world=world.obj_world_3dforest_rabbitescapebig(self)
        self.addpart(self.world)
        self.world.addstartfightmessage()# add start fight message
        self.addpart( draw.obj_music('bunny') )



class obj_scene_ch4p16jdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16j())
    def nextpage(self):
        if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
            share.scenemanager.switchscene(obj_scene_ch4p16j())
        else:
            share.scenemanager.switchscene(obj_scene_ch4p16k())# skip
    def textboxset(self):
        self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died." ',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Now go back and try to act more "heroic". '\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(1030,500),fontsize='large') )
        y1=200
        textchoice=draw.obj_textchoice('choice_yesno',default='yes')
        textchoice.addchoice('Retry','yes',(500,y1))
        textchoice.addchoice('Abandon (skip)','no',(820,y1))
        self.addpart( textchoice )
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p16k(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16j())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16l())
    def setup(self):
        self.text=[\
                ('{heroname}',share.colors.hero),' valiantly retreated into the bushes once more. ',\
                'Look, said ',('{bug}',share.colors.bug),\
                ', this time its the saxophone! What could it possibly do.'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'saxophone','tree','bush'))
        self.addpart( draw.obj_image('saxophone',(624,441),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(841,376),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(361,418),scale=0.55,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('bush',(143,511),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(517,235),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(311,243),scale=0.45,rotate=0,fliph=True,flipv=False) )
        animation1=draw.obj_animation('ch4_heroinbushes','herobase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_buginbushes','bug',(640,360),record=False,sync=animation1)
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16l(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16k())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16m())
    def triggernextpage(self,controls):
        return self.world.done
    def textboxset(self):
        self.textboxopt={'do':False}
    def postpostsetup(self):# foreground do not show mouse pointer
        pass
    def setup(self):
        self.text=['Get the ',('saxophone',share.colors.item),'.']
        self.world=world.obj_world_3dforest_findsax(self)# fishing mini-game
        self.addpart(self.world)
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16m(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16l())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16n())
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' came back with the saxophone. ',\
                'And what exactly are you gonna do with that, said ',('{bunnyname}',share.colors.bunny),\
                '. I guess you can play a tune while dying."'\
                   ]
        # self.addpart(draw.obj_imageplacer(self,'herobase','bunnybase','tree','bush','sun','cave','saxophone'))
        self.addpart( draw.obj_image('cave',(1142,468),scale=0.57,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('herobase',(168,502),scale=0.45,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(388,263),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(389,448),scale=0.34,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(512,499),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('saxophone',(259,509),scale=0.28,rotate=4,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_bigbunnydubious','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny2", [241, 359],skip=1 )
        animation1.addsound( "bunny5", [92],skip=1)
        # animation1.addsound( "revealscary", [1],skip=1 )
        #
        self.addpart( draw.obj_music('bunny') )

class obj_scene_ch4p16n(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16m())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16o())
    def triggernextpage(self,controls):
        return self.world.done
    def soundnextpage(self):
        pass# no sound
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        share.datamanager.setbookmark('ch4_playsax')
        tempo='['+share.datamanager.controlname('arrows')+']'
        self.text=[\
                   'Play the melody with the ',('[arrows]',share.colors.instructions),'. '\
                   ]
        self.world=world.obj_world_serenade(self,bigrabbit=True)# serenade mini-game
        self.addpart(self.world)
        #
        self.addpart( draw.obj_music('bunny') )


class obj_scene_ch4p16o(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16n())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def setup(self):
        share.datamanager.setbookmark('ch4_getclue')
        self.text=[\
                'Aaaargh, this melody is so dull and random, said ',('{bunnyname}',share.colors.bunny),'. ',\
                'Make it stop, I beg you! I will even give you my ',('clue',share.colors.password),'! ']
        # self.addpart(draw.obj_imageplacer(self,'saxophone','herobase','bunnybase','tree','bush','sun','cave'))
        self.addpart( draw.obj_image('herobase',(261,390),scale=0.59,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('bush',(519,402),scale=0.41,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_image('bush',(1172,530),scale=0.41,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('sun',(1094,183),scale=0.38,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1166,318),scale=0.52,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('tree',(660,285),scale=0.53,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(469,271),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('tree',(92,258),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('saxophone',(369,391),scale=0.41,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(1017,173),scale=0.35,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_bunnygetsbackupe','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
        animation1.addsound( "bunny5", [19, 138],skip=1)
        # animation1.addsound( "unlock", [140],skip=1)
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p16o())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def triggernextpage(self,controls):
        return self.world.done# quick skip
    def textboxset(self):
        self.textboxopt={'do':False}
    def setup(self):
        self.text=[\
                   'Alright, you now what to do. Put your hands up in the air like you just dont care. '\
                   ]
        self.world=world.obj_world_getitem(self,item='bunnyhead',imgscale=0.7,imgxy=(0,-40))
        self.addpart(self.world)
        # background
        self.addpart( draw.obj_image('tree',(110,351),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1154,357),scale=0.51,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(1117,173),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(282,337),scale=0.32,rotate=0,fliph=False,flipv=False) )
        #
        animation1=draw.obj_animation('ch4_bunnycriesback','bunnybase',(640,360),record=False)
        self.addpart( animation1 )
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )

class obj_scene_ch4p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p19())
    def setup(self):
        self.text=[\
                 'You have received a ',('clue',share.colors.password),' from ',('{bunnyname}',share.colors.bunny),\
                 '! Here it goes... ']
        # background
        self.addpart( draw.obj_image('tree',(110,351),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cave',(1154,357),scale=0.51,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('moon',(1117,173),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tree',(282,337),scale=0.32,rotate=0,fliph=False,flipv=False) )
        # raise arms
        self.addpart(draw.obj_image('heroarmsfaceup',(620,513),scale=0.69,rotate=0,fliph=False,flipv=False))
        self.addpart(draw.obj_image('bunnyhead',(618,230-40),scale=0.4*0.7,rotate=0,fliph=False,flipv=False))
        self.addpart(draw.obj_image('cluesparkles',(618,230),scale=0.7,path='data/premade'))
        animation1=draw.obj_animation('bughovertoright1','bug',(640,360))
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch4_bunnycriesback','bunnybase',(640,360),record=False)
        self.addpart( animation2 )
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch4p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        self.text=[\
                 'The first part of the password that unlocks the ',\
                 ('evil tower',share.colors.location2),' is "',('abra',share.colors.password),'". ',\
                 'Now you only need to find two more parts. ']
        self.addpart( draw.obj_image('tower',(754,418),scale=0.74,rotate=0,fliph=False,flipv=False) )
        self.addpart(draw.obj_image('cluesparkles',(754,418),scale=1,path='data/premade'))

        animation1=draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(374,346),path='data/premade')
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','bunnyhead',(137,564-150),scale=0.3) )
        self.addpart( draw.obj_animation('ch3_bugtalks3intmark','interrogationmark',(1099,444),path='data/premade') )
        self.addpart( draw.obj_textbox('abra',(137,564+50),color=share.colors.password) )
        self.addpart( draw.obj_textbox('abra...',(754,418+200),color=share.colors.password) )
        # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
        # animation1.addsound( "bug1", [15, 120, 140])
        self.addpart( draw.obj_music('piano') )



class obj_scene_ch4end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch4unlocknext())
    def setup(self):
        self.text=[\
                    'Well that wasnt too hard after all, said the book of things. ',\
                   'Keep going and lets see what happens tomorrow. ',\
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


class obj_scene_ch4unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4end())
    def setup(self):
        share.datamanager.setbookmark('ch4_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter V',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=5)# chapter 5 becomes available
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )
#





####################################################################################
####################################################################################



# class obj_scene_ch4p1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_chapter4())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p3())
#     def setup(self):
#         self.text=[\
#                   '"',
#                    ('{partnername}',share.colors.partner),' was held captive in ',\
#                     ('{villainname}',share.colors.villain),'\'s ',\
#                      ('evil tower',share.colors.location2),', and ',\
#                      ('{heroname}',share.colors.hero),' needed to visit three ',\
#                      ('evil grandmasters',share.colors.grandmaster),' to reveal the tower\'s ',\
#                      ('password',share.colors.password2),'." ',\
#                    ]
#         self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
#         self.addpart( draw.obj_image('tower',(1156,312),scale=0.54,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(981,265),scale=0.35,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('mountain',(866,243),scale=0.23,rotate=0,fliph=True,flipv=False) )
#         animation1=draw.obj_animation('ch4_villaincapture1','villainbase',(640,360),record=False)
#         animation1.addimage('villainholdspartner')
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch4_villaincapture2','partnerbase',(640,360),record=False,sync=animation1)
#         animation2.addimage('empty',path='data/premade')
#         self.addpart( animation2 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'villain1','villain2','villain3','villain4','partner_scared') )
#         animation1.addsound( "villain1", [20] )
#         animation1.addsound( "villain2", [300] )
#         animation1.addsound( "villain3", [155] )
#         animation1.addsound( "partner_scared", [228] )
#         #
#         self.addpart( draw.obj_music('piano') )

# remove to shorten
# class obj_scene_ch4p2(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p1())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p3())
#     def setup(self):
#         self.text=[\
#                   '"',('{heroname}',share.colors.hero),\
#                    ' has befriended a terrifying ',('{bug}',share.colors.bug),\
#                     ', and they need to visit three ',\
#                     ('evil grandmasters',share.colors.grandmaster),\
#                     ' that know parts of the tower\'s password."',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('piano') )

# class obj_scene_ch4p2a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p2())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p3())
#     def setup(self):
#         share.datamanager.setbookmark('ch4_drawalarm')
#         self.text=[\
#                    'First, lets make sure ',('{heroname}',share.colors.hero),\
#                    ' wakes up on time today, said the book of things. ',\
#                    'Draw a ',('night stand',share.colors.item),\
#                    ' and an ',('alarm clock',share.colors.item),'. ',\
#                    ]
#         self.addpart( draw.obj_drawing('nightstanddraw',(340,450-50),legend='night stand',shadow=(250,250)) )
#         self.addpart( draw.obj_drawing('alarmclockextdraw',(940,450-50),legend='alarm clock (draw the exterior)',shadow=(250,250)) )
#         self.addpart( draw.obj_image('alarmclockfill',(940,450-50),path='data/premade',scale=1.25) )
#         self.addpart( draw.obj_image('alarmclockcenter8am',(940,450-50),path='data/premade',scale=1.25) )
#         #
#         self.addpart( draw.obj_music('piano') )


# class obj_scene_ch4p5(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p4())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p6())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                     '        ',\
#                     '"',('{hero_he}',share.colors.hero),\
#                      ' went to the lake and shot a fish ',\
#                       'with a gun.',\
#                        '"\n ',\
#                    ]
#         self.world=world.obj_world_fishing_withgun(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('ch4') )


# class obj_scene_ch4p8(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p7())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p9())
#     def setup(self):
#         self.text=[\
#                   '"The ',('{bug}',share.colors.bug),\
#                   ' crawled out of ',('{heroname}',share.colors.hero),\
#                   '\'s pocket and said: the first ',\
#                    ('evil grandmaster',share.colors.grandmaster),\
#                     ' lives in the east not far from here. Lets get going." ',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch4') )

# class obj_scene_ch4p12a(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p12())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p13())
#     def setup(self):
#         self.text=[\
#                 'Now draw ',('{bunnyname}',share.colors.bunny),'\'s body. ',\
#                 'Remember to make it very cute! ',\
#                    ]
#         yref=400
#         self.addpart( draw.obj_drawing('bunnybody',(640,yref+65),legend='bunny body (facing right)',shadow=(200,105+50),brush=share.brushes.pen6) )
#         self.addpart( draw.obj_image('bunnyhead',(640,yref-150),scale=0.5) )
#         #
#         self.addpart( draw.obj_music('ch4') )

# class obj_scene_ch4p14(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p13())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p15())
#     def setup(self):
#         self.text=[\
#                 '"Ha! You think I am cute, said ',('{bunnyname}',share.colors.bunny),'. ',\
#                 'Look at these trees, poof, I chopped them all ',\
#                 'with my ',('LITTLE PAWS',share.colors.bunny),'!" ',\
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
#         self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
#         # self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
#         # self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
#         # self.addpart( draw.obj_image('bunnybase',(867,525),scale=0.62,rotate=0,fliph=True,flipv=False) )
#         # self.addpart( draw.obj_image('tree',(618,439),scale=1.28,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_bunnyeats1','bunnybase',(640,360),record=False)
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch4_bunnyeats2','tree',(640,360),record=False,sync=animation1)
#         animation2.addimage('empty',path='data/premade')
#         animation2.addimage('poof',path='data/premade')
#         self.addpart( animation2 )
#         animation3=draw.obj_animation('ch4_bunnyeats3','tree',(640,360),record=False,sync=animation1)
#         animation3.addimage('empty',path='data/premade')
#         animation3.addimage('poof',path='data/premade')
#         self.addpart( animation3 )
#         animation4=draw.obj_animation('ch4_bunnyeats4','tree',(640,360),record=False,sync=animation1)
#         animation4.addimage('empty',path='data/premade')
#         animation4.addimage('poof',path='data/premade')
#         self.addpart( animation4 )
#         animation5=draw.obj_animation('ch4_bunnyeats5','tree',(640,360),record=False,sync=animation1)
#         animation5.addimage('empty',path='data/premade')
#         animation5.addimage('poof',path='data/premade')
#         self.addpart( animation5 )
#         #
#         self.sound=draw.obj_sound('revealscary')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5','bunny_scream') )
#         animation1.addsound( "bunny2", [0] )
#         animation1.addsound( "bunny5", [160] )
#         animation1.addsound( "bunny_hit", [159, 203, 243, 264] )
#         #
#         self.addpart( draw.obj_music('tension') )

# #################################################################
# # Lying game (skipped now)
# # *LYING
# #
#
# class obj_scene_lyingpart1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p17())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingp1q1(world=self.world))
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying(self)# or remake it
#         # Page Text
#         self.text=[\
#                     'Here are three statements ',\
#                     ('true statements',share.colors.darkgreen),' you need to remember. ',\
#                     'You can even take some notes at the bottom of the screen. '
#                    ]
#         self.addpart( draw.obj_textbox( '1. '+self.world.getstatement(0),(400,220),xleft=True,color=share.colors.darkgreen  ) )
#         self.addpart( draw.obj_textbox( '2. '+self.world.getstatement(1),(400,290),xleft=True,color=share.colors.darkgreen  ) )
#         self.addpart( draw.obj_textbox( '3. '+self.world.getstatement(2),(400,360),xleft=True,color=share.colors.darkgreen  ) )
#         # Page drawing
#         drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
#         if (kwargs is not None) and ('world' in kwargs):
#             pass
#         else:
#             drawing.clear()# erase drawing
#         self.addpart( drawing )
#         self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )
#         #
#         self.sound=draw.obj_sound('bunny2')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# class obj_scene_lyingp1q1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
#     def nextpage(self):
#         if self.world.isanswercorrect():
#             self.nextpage_lyinggame()
#         else:
#             self.nextpage_lyingfail()
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingp1q2(world=self.world))
#     def nextpage_lyingfail(self):
#         share.scenemanager.switchscene(obj_scene_lyingfailpart1(world=self.world))
#     def textchoice_lyinggame(self):
#         textchoice=draw.obj_textchoice('choice_yesno',default='yes')
#         textchoice.addchoice('True','yes',(640-100,250))
#         textchoice.addchoice('False','no',(640+100,250))
#         self.addpart( textchoice )
#     def textboxset(self):
#         self.textboxopt={'xy':(640,350),'text':'[confirm]','align':'center'}
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying(self)# or remake it
#         self.world.makequestion()
#         # Page text
#         self.text=self.text_lyinggame()
#         self.addpart( draw.obj_textbox( '" '+self.world.getquestion()+'"',(640,150)) )
#         self.textchoice_lyinggame()
#         # Drawing
#         drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
#         self.addpart( drawing )
#         # animation
#         animation1=draw.obj_animation('ch3_bunnheadwobble','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         self.addpart( draw.obj_animation('ch3_bunnheadwobble2','herohead',(640,360),record=False, sync=animation1) )
#         #
#         self.sound=draw.obj_sound('bunny3')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#         #
#     def text_lyinggame(self):
#         return ['Now tell me if this is true or false (1/3):']
#
#
# class obj_scene_lyingp1q2(obj_scene_lyingp1q1):# child of lying 1
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingp1q3(world=self.world))
#     def text_lyinggame(self):
#         return ['Now tell me if this is true or false (2/3):']
#
#
# class obj_scene_lyingp1q3(obj_scene_lyingp1q1):# child of lying 1
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1win())# forget lying game database
#     def text_lyinggame(self):
#         return ['Now tell me if this is true or false (3/3):']
#
#
# class obj_scene_lyingfailpart1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
#     def nextpage(self):
#         if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
#             share.scenemanager.switchscene(obj_scene_lyingpart1(world=self.world))
#         else:
#             # share.scenemanager.switchscene(obj_scene_lyingpart1win())# forget lying game database
#             share.scenemanager.switchscene(obj_scene_lyingend())# finish game
#     def textboxset(self):
#         self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying(self)# or remake it
#         self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),', ',\
#                     'you gave me the wrong answer. ',\
#                     'Now go back and win this first round, I know you can do it! ',\
#                                 ]
#         animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
#         self.addpart( animation1 )
#         #
#         y1=200
#         textchoice=draw.obj_textchoice('choice_yesno',default='yes')
#         textchoice.addchoice('Retry','yes',(540,y1))
#         textchoice.addchoice('Abandon (skip)','no',(740,y1))
#         self.addpart( textchoice )
#         #
#         self.sound=draw.obj_sound('bunny5')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# class obj_scene_lyingpart1win(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart2())
#     def setup(self):
#         share.datamanager.setbookmark('ch4_winlying1')
#         self.text=[\
#                     'Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
#                     'you won the ',\
#                     ('first round',share.colors.grandmaster2),'! ',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation1)
#         animation3.addimage('empty',path='data/premade')
#         self.addpart( animation3 )
#         #
#         self.sound=draw.obj_sound('unlock')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
#         animation1.addsound( "bunny4", [128] )
#         animation1.addsound( "bunny3", [43] )
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# ##########################
# class obj_scene_lyingpart2(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1win())# forget lying game database
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingp2q1(world=self.world))
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying2(self)# or remake it
#         # Page Text
#         self.text=['For the second round, remember these three ',('true statements',share.colors.darkgreen),'. ',\
#                     'But from now on I want you to lie to me',\
#                     ' and only give me only ',('wrong answers',share.colors.red),'.',\
#                    ]
#         # Same text but showing the opposite statements (the boolean reverse remains true)
#         self.addpart( draw.obj_textbox( '1. '+self.world.getstatement(0,lying=False),(400,220),xleft=True,color=share.colors.darkgreen) )
#         self.addpart( draw.obj_textbox( '2. '+self.world.getstatement(1,lying=False),(400,290),xleft=True,color=share.colors.darkgreen) )
#         self.addpart( draw.obj_textbox( '3. '+self.world.getstatement(2,lying=False),(400,360),xleft=True,color=share.colors.darkgreen) )
#         # Drawing
#         drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
#         if (kwargs is not None) and ('world' in kwargs):
#             pass
#         else:
#             drawing.clear()# erase drawing
#         self.addpart(drawing)
#         self.addpart( draw.obj_image('bunnyhead',(1150,300),scale=0.35,rotate=0,fliph=True,flipv=False) )
#         #
#         self.sound=draw.obj_sound('bunny2')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# class obj_scene_lyingp2q1(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
#     def nextpage(self):
#         if self.world.isanswercorrect(lying=True):# hero must lie
#             self.nextpage_lyinggame()
#         else:
#             self.nextpage_lyingfail()
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingp2q2(world=self.world))
#     def nextpage_lyingfail(self):
#         share.scenemanager.switchscene(obj_scene_lyingfailpart2(world=self.world))
#
#     def textchoice_lyinggame(self):
#         textchoice=draw.obj_textchoice('choice_yesno',default='yes')
#         textchoice.addchoice('"True"','yes',(640-100,250))
#         textchoice.addchoice('"False"','no',(640+100,250))
#         self.addpart( textchoice )
#     def textboxset(self):
#         self.textboxopt={'xy':(640,350),'text':'[confirm]','align':'center'}
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying2(self)# or remake it
#         self.world.makequestion()
#         # Page text
#         self.text=self.text_lyinggame()
#         self.addpart( draw.obj_textbox( '" '+self.world.getquestion()+'"',(640,150)) )
#         self.textchoice_lyinggame()
#         # Drawing
#         drawing=draw.obj_drawing('lyingnote',(640,530),shadow=(590,120),legend='Take some notes',brush=share.brushes.smallpen)
#         self.addpart( drawing )
#         # animation
#         animation1=draw.obj_animation('ch3_bunnheadwobble','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         self.addpart( draw.obj_animation('ch3_bunnheadwobble2','herohead',(640,360),record=False, sync=animation1) )
#         #
#         self.sound=draw.obj_sound('bunny3')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#     def text_lyinggame(self):
#         return ['Now "lyingly" tell me if this is true or false (1/3):']
#
# class obj_scene_lyingp2q2(obj_scene_lyingp2q1):# child of lying 2
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingp2q3(world=self.world))
#     def text_lyinggame(self):
#         return ['Now "lyingly" tell me if this is true or false (2/3):']
#
# class obj_scene_lyingp2q3(obj_scene_lyingp2q1):# child of lying 2
#     def nextpage_lyinggame(self):
#         share.scenemanager.switchscene(obj_scene_lyingend())# forget lying game database
#     def text_lyinggame(self):
#         return ['Now "lyingly" tell me if this is true or false (3/3):']
#
#
# class obj_scene_lyingfailpart2(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
#     def nextpage(self):
#         if share.devmode or share.datamanager.getword('choice_yesno')=='yes':
#             share.scenemanager.switchscene(obj_scene_lyingpart2(world=self.world))
#         else:
#             # share.scenemanager.switchscene(obj_scene_lyingpart2win())# forget lying game database
#             share.scenemanager.switchscene(obj_scene_lyingend())# finish game
#     def textboxset(self):
#         self.textboxopt={'xy':(640,280),'text':'[confirm]','align':'center'}
#     def setup(self,**kwargs):
#         # inherit world
#         if (kwargs is not None) and ('world' in kwargs):
#             self.world=kwargs["world"]# inherit lying database
#         else:
#             self.world=world.obj_world_lying2(self)# or remake it
#         self.text=['Sorry, said ',('{bunnyname}',share.colors.bunny),', that was actually correct! ',\
#                     'For this second round, remember to always give me the ',\
#                     ('wrong answer',share.colors.red),'. ',\
#                     'Now go back and win this. ',\
#                                 ]
#         animation1=draw.obj_animation('ch4_bunnytalking1','bunnybase',(640,360),record=False)
#         self.addpart( animation1 )
#         #
#         y1=200
#         textchoice=draw.obj_textchoice('choice_yesno',default='yes')
#         textchoice.addchoice('Retry','yes',(540,y1))
#         textchoice.addchoice('Abandon (skip)','no',(740,y1))
#         self.addpart( textchoice )
#         #
#         self.sound=draw.obj_sound('bunny5')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('ch4') )
#
# class obj_scene_lyingend(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart2())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p18())
#     def setup(self):
#         share.datamanager.setbookmark('ch4_winlying3')
#         self.text=[\
#                     '"Well done, said ',('{bunnyname}',share.colors.bunny),', ',\
#                     'you won my ',('lying game',share.colors.grandmaster2),'! ',\
#                     ' You are truly a great liar!"',\
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
#         self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         animation3=draw.obj_animation('ch4_herowalkbunny2love','love',(640,360),record=False,sync=animation1)
#         animation3.addimage('empty',path='data/premade')
#         self.addpart( animation3 )
#         animation4=draw.obj_animation('ch4_herowalkbunny2love2','love',(640,360),record=False,sync=animation1)
#         animation4.addimage('empty',path='data/premade')
#         self.addpart( animation4 )
#         animation5=draw.obj_animation('ch4_herowalkbunny2love3','love',(640,360),record=False,sync=animation1)
#         animation5.addimage('empty',path='data/premade')
#         self.addpart( animation5 )
#         #
#         self.sound=draw.obj_sound('unlock')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.sound=draw.obj_sound('serenade_cheer')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
#         animation1.addsound( "bunny5", [128] )
#         animation1.addsound( "bunny4", [43] )
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# # End of lying minigame
# #################################################################


#
# class obj_scene_ch4p16o(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p16n())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p16p())
#     def setup(self):
#         self.text=[\
#                 'what, what, said ',('{bunnyname}',share.colors.bunny),\
#                 '. This is so cute! I cannot be mad at you anymore, I am too delighted. '\
#                    ]
#         # self.addpart(draw.obj_imageplacer(self,'herobase','bunnybase','tree','bush','sun','cave','saxophone'))
#         self.addpart( draw.obj_image('cave',(1142,468),scale=0.57,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('herobase',(168,502),scale=0.45,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('sun',(388,263),scale=0.41,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tree',(389,448),scale=0.34,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(512,499),scale=0.43,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('saxophone',(259,509),scale=0.28,rotate=4,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_bigbunnyhappy','bunnybase',(640,360),record=False)
#         self.addpart( animation1 )
#         animation2=draw.obj_animation('ch4_bigbunnyhappy_note','musicnote',(640,360),record=False,sync=animation1)
#         self.addpart( animation2 )
#         animation3=draw.obj_animation('ch4_bigbunnyhappy_note','musicnote',(640+500,360-40),record=False,sync=animation1)
#         self.addpart( animation3 )
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
#         animation1.addsound( "bunny1", [327],skip=1 )
#         animation1.addsound( "bunny4", [213, 262, 354] )
#         animation1.addsound( "unlock", [140])
#         #
#         self.sound=draw.obj_sound('revealscary')
#         self.addpart(self.sound)
#         self.sound.play()
#         #
#         self.addpart( draw.obj_music('tension') )
#
# class obj_scene_ch4p16p(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p16o())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p17())
#     def setup(self):
#         self.text=[\
#                 'Lets take back a more suitable form, said ',('{bunnyname}',share.colors.bunny),\
#                 '.'\
#                    ]
#         animation1=draw.obj_animation('ch4_bigbunnyshrinks','bunnybase',(640,360),record=False)
#         self.addpart( animation1 )
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )#
#         animation1.addsound( "bunny2", [310] )
#         animation1.addsound( "bunny4", [64, 193] )
#         self.addpart( draw.obj_music('ch4') )
#
# class obj_scene_ch4p17(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p16p())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingpart1())
#     def setup(self):
#         share.datamanager.setbookmark('ch4_lyinggame')
#         self.text=[\
#                 '"So you want to know ',\
#                 ('my part of the tower\'s password',share.colors.password),'. ',\
#                 'I wont give it so easily, ',\
#                 'unless... you win my ',('lying game',share.colors.grandmaster2),\
#                 '! Now lets get started." ',\
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
#         self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
#         animation1.addsound( "bunny2", [128] )
#         animation1.addsound( "bunny3", [43],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
#
#
# class obj_scene_ch4p18(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_lyingend())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p19())
#     def setup(self):
#         self.text=[\
#                     '"The first part of the tower\'s password is: ',\
#                     ('"fight"',share.colors.password),'. ',\
#                     'That\'s my motto: fight in any situation."',\
#
#                    ]
#         # self.addpart( draw.obj_imageplacer(self,'herobase','cave','tree','bunnybody') )
#         self.addpart( draw.obj_image('herobase',(249,491),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('cave',(1149,374),scale=0.62,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('bunnybody',(867,605),scale=0.59,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(946,307),scale=0.39,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(761,293),scale=0.33,rotate=0,fliph=False,flipv=False) )
#         self.addpart( draw.obj_image('tree',(1148,596),scale=0.51,rotate=0,fliph=True,flipv=False) )
#         self.addpart( draw.obj_image('tree',(599,273),scale=0.32,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch4_herowalkbunny2','bunnyhead',(640,360),record=False)
#         self.addpart( animation1 )
#         animation3=draw.obj_animation('ch4_herowalkbunny3inter','interrogationmark',(640,360),record=False,sync=animation1,path='data/premade')
#         animation3.addimage('empty',path='data/premade')
#         self.addpart( animation3 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bunny1','bunny2','bunny3','bunny4','bunny5') )
#         animation1.addsound( "bunny2", [128] )
#         animation1.addsound( "bunny4", [43],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
# class obj_scene_ch4p19(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p18())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p20())
#     def setup(self):
#         self.text=[\
#                 '"The ',('{bug}',share.colors.bug),\
#                 ' crawled out of ',('{heroname}',share.colors.hero),\
#                 '\'s pocket and whispered: ',\
#                 'Well done, soon we will be able to figure out the entire password! ',\
#                 'Now lets scram." ',\
#                    ]
#         self.addpart( draw.obj_image('herobase',(286,635),scale=1.4,rotate=0,fliph=False,flipv=False) )
#         animation1=draw.obj_animation('ch3_bugtalks1','bug',(840,360),record=False)
#         self.addpart( animation1 )
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'bug1','bug2') )
#         animation1.addsound( "bug1", [15, 100] )
#         animation1.addsound( "bug2", [116],skip=1 )
#         #
#         self.addpart( draw.obj_music('ch4') )
#
#
#
#
# class obj_scene_ch4p20(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p19())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p22())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         share.datamanager.setbookmark('ch4_gohome')
#         self.text=[\
#                 'go back home',\
#                    ]
#         self.world=world.obj_world_travel(self,start='forest',goal='home',chapter=4)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music(None) )


### removed (avoid repetitions)
# class obj_scene_ch4p21(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p20())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p22())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    '"Back at home, ',\
#                    ('{heroname}',share.colors.hero), ' remembered how ',\
#                    ('{hero_he}',share.colors.hero2),' used to charm ',\
#                    ('{partnername}',share.colors.partner),' with a serenade. ',\
#                    ]
#         self.world=world.obj_world_serenade(self,partner=False,heroangry=True)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )

#
# class obj_scene_ch4p22(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p20())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p23())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                    # '"This made ',('{hero_him}',share.colors.hero2),\
#                    # ' so sad that ',\
#                    # ('{hero_he}',share.colors.hero),\
#                    # ' went straight to bed." ',\
#                    '"Back at home, ',\
#                    ('{heroname}',share.colors.hero),\
#                    ' went straight to bed. ',\
#                    ('{hero_he}',share.colors.hero2),' was still sad and lonely." ',\
#                    ]
#         self.world=world.obj_world_gotobed(self,bug=True,addmoon=False,addsun=True)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
#
#
# class obj_scene_ch4p23(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4p22())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch4end())
#     def triggernextpage(self,controls):
#         return self.world.done
#     def textboxset(self):
#         self.textboxopt={'do':False}
#     def setup(self):
#         self.text=[\
#                 '"The night fell, and tomorrow would be another day."',\
#                    ]
#         self.world=world.obj_world_sunset(self)
#         self.addpart(self.world)
#         #
#         self.addpart( draw.obj_music('piano') )
