#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter5.py: ...
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

# Chapter V: ...
# *CHAPTER V

# name house
class obj_scene_chapter5(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def setup(self):
        self.text=['-----   Chapter V: Over the Rainbow    -----   ',\
                   '\n It was the next day for the book of things, the pen and the eraser. ',\
                  'The book of things said: "Lets see how our story is going so far". ',\
                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch5p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_chapter5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' found out that ',\
                    ('{partnername}',share.colors.partner),' and ',\
                    ('{villainname}',share.colors.villain),\
                    ' were lovers, so he burned the place down and left them to die". ',\
                   'That is quite ',('evil',share.colors.villain),\
                   ', said the book of things. ',\
                   ]
        self.addpart( draw.obj_image('tower',(1100,310), scale=0.7) )
        self.addpart( draw.obj_image('mountain',(1151,596),scale=0.61,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(877,605),scale=0.54,rotate=90,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(660,490),scale=0.51,rotate=90,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch4_evillairburns1','herobaseangry',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch4_evillairburns2','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns3','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_evillairburns4','flame',(640,360),record=False,sync=animation1) )


class obj_scene_ch5p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_sunrise())
    def setup(self):
        self.text=[\
                  'Choices have consequences you see, and they lead to different outcomes in this story. ',\
                 'This is what happened yesterday when we changed the ',('hero',share.colors.hero),' and ',\
                 ('partner',share.colors.partner),'\'s relationship status to "its complicated". ',\
                 'Today we shall try to change the ',\
                 ('evil ending',share.colors.villain),' from yesterday by making a few better choices.',\
                   ]
        y1=400
        self.addpart( draw.obj_textbox('The hero and the partner were:',(250,y1)) )
        self.addpart( draw.obj_textbox('1. in love',(630,y1)) )
        self.addpart( draw.obj_textbox('2. its complicated',(1060,y1)) )
        self.choice1=draw.obj_rectangle((630,y1),100,50,color=share.colors.textchoice)
        self.choice2=draw.obj_rectangle((1060,y1),150,50,color=share.colors.textchoice)
        self.addpart( self.choice1 )
        self.addpart( self.choice2 )
        self.choice1.show=False
        self.choice2.show=True

##########################################################
##########################################################
# From here we use unordered pages for the story with multiple choices


class obj_scene_sunrise(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
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


class obj_scene_wakeup(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_sunrise())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_choosebreakfast())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),' and ',\
                ('{partnername}',share.colors.partner),' woke up. ',\
                'They were angry because their relationship was complicated". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_sun','sun',(640,360),scale=0.5))
        self.world=world.obj_world_wakeup(self,partner='inlove',angryfaces=True)
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # combine stickhead+angryface+stickbody = herobaseangry
        image1=draw.obj_image('stickbody',(640,460),path='premade')
        image2=draw.obj_image('stickhead',(640,200),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,300),'herobaseangry')
        # combine stickbase+angryface+partnerhair=partnerbaseangry
        image1=draw.obj_image('partnerhair',(640,200))
        image2=draw.obj_image('stickbase',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,200),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,330,200,330),'partnerbaseangry')
        # combine stickhead+angryface+partnerhair=partnerheadangry
        image1=draw.obj_image('partnerhair',(640,360))
        image2=draw.obj_image('stickhead',(640,360),path='premade')
        image3=draw.obj_image('angryface',(640,360),scale=0.5)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.addpart('part3',image3)
        dispgroup1.snapshot((640,360,200,200),'partnerheadangry')



class obj_scene_choosebreakfast(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
    def nextpage(self):
        if share.datamanager.getword('hero_breakfast')=='drink':
            share.scenemanager.switchscene(obj_scene_breakfast_drinking())
        else:
            share.scenemanager.switchscene(obj_scene_breakfast_notdrinking())
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'decided what to have for breakfast". ',\
                   ]
        y1=200
        self.addpart( draw.obj_textbox('The hero decided to have:',(340,y1)) )
        textchoice=draw.obj_textchoice('hero_breakfast')
        textchoice.addchoice('1. A drink','drink',(640,y1))
        textchoice.addchoice('2. A cup of coffee','coffeecup',(940,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('bed',(440,500), scale=0.75) )
        self.addpart( draw.obj_image('herobaseangry',(1067,488),scale=0.67,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(814,472),scale=0.67,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('sun',(141,325),scale=0.36,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'herobaseangry','partnerbaseangry','bed','sun') )


class obj_scene_breakfast_drinking(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_choosebreakfast())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'got drunk at breakfast and made ',\
                ('{partnername}',share.colors.partner),' more angry".',\
                   ]
        self.world=world.obj_world_breakfastdrinking(self)
        self.addpart(self.world)

class obj_scene_breakfast_notdrinking(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_choosebreakfast())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def setup(self):
        self.text=[\
                '"',('{heroname}',share.colors.hero),\
                'got coffee for breakfast. ',\
                ('{partnername}',share.colors.partner),' was a little ',\
                ('happier',share.colors.partner),'".',\
                   ]
        self.addpart( draw.obj_image('floor3',(640,720-100),path='premade') )
        self.addpart( draw.obj_image('coffeecup',(830,560),scale=0.5,fliph=False) )
        self.addpart( draw.obj_image('coffeecup',(495,560),scale=0.5,fliph=True) )
        self.addpart( draw.obj_image('herobaseangry',(150,540),scale=1.15,fliph=False) )
        self.addpart( draw.obj_image('stickbody',(1160-50,640+15),scale=1.15,fliph=True,path='premade') )
        animation1=draw.obj_animation('ch5_breakfastpartner1','partnerheadangry',(640,360),record=True)
        animation1.addimage('partnerhead')
        self.addpart( animation1 )


class obj_scene_fishing(page.obj_chapterpage):
    def prevpage(self):
        if share.datamanager.getword('hero_breakfast')=='drink':
            share.scenemanager.switchscene(obj_scene_breakfast_drinking())
        else:
            share.scenemanager.switchscene(obj_scene_breakfast_notdrinking())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travel_hometolair())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish".',
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)




class obj_scene_travel_hometolair(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_arriveatlair())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"When',\
                    ('{heroname}',share.colors.hero),' came back home, ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                'So ',('{hero_he}',share.colors.hero),' travelled to ',
                ('{villainname}',share.colors.villain),'\'s evil lair to rescue',\
                ('{partner_him}',share.colors.partner),'". ',\
                   ]
        self.world=world.obj_world_traveltolair(self)
        self.addpart(self.world)



class obj_scene_arriveatlair(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travel_hometolair())
    def nextpage(self):
        if share.datamanager.getword('hero_fightortalk')=='talk':
            share.scenemanager.switchscene(obj_scene_atlair_talk())# skip fight
        else:
            share.scenemanager.switchscene(obj_scene_dodgebullets())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' found ',\
                    ('{partnername}',share.colors.partner),' in bed with ',\
                    ('{villainname}',share.colors.villain),'.',\
                   ]
        y1=200
        self.addpart( draw.obj_textbox('The hero decided to:',(240,y1)) )
        textchoice=draw.obj_textchoice('hero_fightortalk')
        textchoice.addchoice('1. fight them','fight',(640,y1))
        textchoice.addchoice('2. talk to the partner','talk',(940,y1))
        self.addpart( textchoice )
        share.datamanager.writeword('hero_fightswhom','villainpartner')# will fight both by default

        self.addpart( draw.obj_image('bed',(340,500), scale=0.75) )
        self.addpart( draw.obj_image('herobaseangry',(1100,458),scale=0.67,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(737,457),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(333,435),scale=0.65,rotate=0,fliph=False,flipv=False) )



class obj_scene_atlair_talk(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_arriveatlair())
    def nextpage(self):
        if share.datamanager.getword('hero_atlairtalk')=='peace':
            share.scenemanager.switchscene(obj_scene_atlair_talkpeace())# skip fight
        else:
            share.scenemanager.switchscene(obj_scene_dodgebullets())
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),' talked to ',\
                    ('{partnername}',share.colors.villain),', but ',\
                    ('{hero_he}',share.colors.hero),' was too drunk to say anything meaningful". ',\
                       ]
        y1=200
        if share.datamanager.getword('hero_breakfast')=='drink':
            self.addpart( draw.obj_textbox('The hero said:',(200,y1)) )
            self.addpart( draw.obj_textbox('1. I hate you so much, lets fight.',(600,y1)) )
            self.addpart( draw.obj_rectangle((600,y1),230,35,color=share.colors.textchoice) )
            share.datamanager.writeword('hero_atlairtalk','fight')# will fight
        else:
            self.addpart( draw.obj_textbox('The hero said:',(200,y1)) )
            textchoice=draw.obj_textchoice('hero_atlairtalk')
            textchoice.addchoice('1. I hate you so much, lets fight.','fight',(600,y1))
            textchoice.addchoice('2. Im sorry for everything, let make peace. ','peace',(680,y1+80))
            self.addpart( textchoice )
        self.addpart( draw.obj_image('herohead',(340,535),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerheadangry',(947,556),scale=1.17,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'angryhead','partnerheadangry') )
    def presetup(self):
        super().presetup()
        # herohead+scar+stickbody=villainbasehappy
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
        dispgroup2.addpart('part3',draw.obj_image('scar',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'villainbasehappy')


class obj_scene_atlair_talkpeace(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_atlair_talk())
    def nextpage(self):
        if share.datamanager.getword('hero_wheretofromlair')=='peak':
            share.scenemanager.switchscene(obj_scene_default())
        else:
            share.scenemanager.switchscene(obj_scene_travel_lairtohome_alone())
    def setup(self):
        self.text=[\
                    '"',('{partnername}',share.colors.villain),' said to ',\
                    ('{heroname}',share.colors.hero),': thank you for understanding. ',\
                    ' And so they made peace. ',\
                    ('{partner_he}',share.colors.villain),' asked: what will you do now". ',\
                       ]
        y1=240
        self.addpart( draw.obj_textbox('The hero replied, I will:',(200,y1)) )
        textchoice=draw.obj_textchoice('hero_wheretofromlair')
        textchoice.addchoice('1. Go home','home',(600,y1))
        textchoice.addchoice('2. Seek wisdom on the highest peak','peak',(740,y1+80))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('herohead',(340,535),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerhead',(947,556),scale=1.17,rotate=0,fliph=True,flipv=False) )



class obj_scene_dodgebullets(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_arriveatlair())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_stompfight())
        else:
            share.scenemanager.switchscene(obj_scene_dodgebulletsdeath())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"And so they fought with guns". ',\
                   ]
        if share.datamanager.getword('hero_fightswhom')=='villainpartner':
            self.world=world.obj_world_dodgegunshots(self,heroangry=True,partnerenemy=True)
        else:
            self.world=world.obj_world_dodgegunshots(self,heroangry=True)# villain only
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # heroheadangry+stickcrouch =herocrouchangry
        image1=draw.obj_image('stickcrouch',(940,360),path='premade')
        image2=draw.obj_image('angryhead',(800,360),scale=0.5,rotate=90)
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',image1)
        dispgroup1.addpart('part2',image2)
        dispgroup1.snapshot((940,360,300,200),'herocrouchangry')# 0 to 660 in height
class obj_scene_dodgebulletsdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Just go back to the last event and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobaseangry',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_stompfight(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_lairfire())
        else:
            share.scenemanager.switchscene(obj_scene_stompfightdeath())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"... and then they fought with fists." ',\
                   ]
        if share.datamanager.getword('hero_fightswhom')=='villainpartner':
            self.world=world.obj_world_stompfight(self,heroangry=True,partnerenemy=True)
        else:
            self.world=world.obj_world_stompfight(self,heroangry=True)# villain only
        self.addpart(self.world)
    def presetup(self):
        super().presetup()
        # combine partnerheadangry+stickkick =partnerkickangry
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickkick',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('partnerheadangry',(640,200)) )
        dispgroup2.snapshot((640,330,300,330),'partnerkickangry')
class obj_scene_stompfightdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_stompfight())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_stompfight())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
                'Just go back to the last event and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobaseangry',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_lairfire(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_stompfight())
    def nextpage(self):
        if share.datamanager.getword('hero_savefromfire')=='villainpartner':
            share.scenemanager.switchscene(obj_scene_lairfire_saveboth())
        else:
            share.scenemanager.switchscene(obj_scene_lairfire_savenone())
    def setup(self):
        if share.datamanager.getword('hero_fightswhom')=='villainpartner':
            self.text=[\
                      '"',('{heroname}',share.colors.hero),' won the fight, then ',\
                      'the evil lair took fire. ',('{villainname}',share.colors.villain),\
                      ' and ',('{partnername}',share.colors.villain),\
                      ' were laying unconscious". ',
                       ]
        else:# villain only
            self.text=[\
                      '"',('{heroname}',share.colors.hero),' won the fight, then ',\
                      'the evil lair took fire. ',('{villainname}',share.colors.villain),\
                      ' was laying unconscious". ',
                       ]
        y1=200
        self.addpart( draw.obj_textbox('The hero decided to:',(200,y1)) )
        textchoice=draw.obj_textchoice('hero_savefromfire')
        if share.datamanager.getword('hero_fightswhom')=='villainpartner':
            textchoice.addchoice('1. Save them','villainpartner',(640,y1))
            textchoice.addchoice('2. Leave them','notvillainpartner',(1040,y1))
        else:
            textchoice.addchoice('1. Save the villain','villain',(640,y1))
            textchoice.addchoice('2. Leave the villain','notvillain',(1040,y1))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('herobaseangry',(300,523),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1155,443),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1188,626),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(969,439),scale=0.34,rotate=10,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flame',(536,655),scale=0.28,rotate=10,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(87,499),scale=0.37,rotate=10,fliph=False,flipv=False) )
        if share.datamanager.getword('hero_fightswhom')=='villainpartner':
            self.addpart( draw.obj_image('villainbase',(893,620),scale=0.45,rotate=94,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('partnerbaseangry',(616,514),scale=0.34,rotate=94,fliph=True,flipv=False) )
        else:
            self.addpart( draw.obj_image('villainbase',(893,620),scale=0.45,rotate=94,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'flame','herobaseangry','villainbase','partnerbaseangry','tower','mountain') )


class obj_scene_lairfire_saveboth(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lairfire())
    def nextpage(self):
        if share.datamanager.getword('hero_wheretofromlair')=='peak':
            share.scenemanager.switchscene(obj_scene_default())
        else:
            share.scenemanager.switchscene(obj_scene_travel_lairtohome_alone())
    def setup(self):
        self.text=[\
                    '"',('{partnername}',share.colors.villain),' and ',\
                    ('{villainname}',share.colors.villain),\
                    ' thanked ',('{heroname}',share.colors.hero),' for saving them. '\
                    'They asked: what will you do now". ',\
                       ]
        y1=200
        self.addpart( draw.obj_textbox('The hero replied, I will:',(200,y1)) )
        textchoice=draw.obj_textchoice('hero_wheretofromlair')
        textchoice.addchoice('1. Go home','home',(600,y1))
        textchoice.addchoice('2. Seek wisdom on the highest peak','peak',(740,y1+80))
        self.addpart( textchoice )
        self.addpart( draw.obj_image('herobase',(300,523),scale=0.59,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('tower',(1155,443),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(1188,626),scale=0.35,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbase',(737,511),scale=0.61,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('villainbasehappy',(956,490),scale=0.61,rotate=0,fliph=True,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'flame','herobase','villainbasehappy','partnerbase','tower','mountain') )
    def presetup(self):
        super().presetup()
        # herohead+scar+stickbody=villainbasehappy
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup2.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
        dispgroup2.addpart('part3',draw.obj_image('scar',(640,200),scale=0.5) )
        dispgroup2.snapshot((640,330,200,330),'villainbasehappy')


class obj_scene_lairfire_savenone(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_lairfire())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_endingevil())
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),\
                  ' left ',('{partnername}',share.colors.villain),\
                  ' and ',('{villainname}',share.colors.villain),' to die. ',\
                  'He realized he had been hurt during the fight and ',\
                  'a large ',('scar',share.colors.villain),' was splitting his face. ',\
                  'He had become the ',('villain',share.colors.villain),'. ',\
                  'He erupted into a maniacal laughter".',\
                   ]
        animation1=draw.obj_animation('ch4_heroisevil','angryhead',(640,360),record=False)
        animation1.addimage( 'angryheadscar' )
        animation1.addimage( 'heroheadscar' )
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch4_heroisevil2','flame',(640,360),record=False,sync=animation1) )
        self.addpart( draw.obj_animation('ch4_heroisevil3','flame',(640,360),record=False,sync=animation1) )
    def presetup(self):
        super().presetup()
        # angryhead+scar=angryheadscar (not necessarily=villain if has hair)
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('angryhead',(640,360)) )
        dispgroup2.addpart('part2',draw.obj_image('scar',(640,360)) )
        dispgroup2.snapshot((640,360,200,200),'angryheadscar')
        # herohead+scar=heroheadscar
        dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup2.addpart('part1',draw.obj_image('herohead',(640,360)) )
        dispgroup2.addpart('part2',draw.obj_image('scar',(640,360)) )
        dispgroup2.snapshot((640,360,200,200),'heroheadscar')


class obj_scene_travel_lairtohome_alone(page.obj_chapterpage):
    def prevpage(self):
        pass# bottleneck so no going back!
        # share.scenemanager.switchscene(obj_scene_lairfire_saveboth())
        # share.scenemanager.switchscene(obj_scene_atlair_talkpeace())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_eatfish_alone())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' went back home". ',\
                   ]
        self.world=world.obj_world_traveltolair(self,tohome=True,partner=False)
        self.addpart(self.world)


class obj_scene_eatfish_alone(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travel_lairtohome_alone())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall_alone())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{hero_he}',share.colors.hero),' ate ',\
                    ('fish',share.colors.item),'for dinner".',\
                   ]
        self.world=world.obj_world_eatfish(self)
        self.addpart(self.world)


class obj_scene_nightfall_alone(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_eatfish_alone())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_tosleep_alone())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_tosleep_alone(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall_alone())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_endingbasic())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),\
                   ' went back to bed". ',\
                   ]
        self.addpart(draw.obj_animation('ch1_sun','moon',(640,360),scale=0.5))
        self.world=world.obj_world_gotobed(self)
        self.addpart(self.world)

####################################################################################################################
# Mountain peak quest


class obj_scene_travel_hometolair(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_arriveatlair())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"When',\
                    ('{heroname}',share.colors.hero),' came back home, ',\
                  ('{partnername}',share.colors.partner),' wasnt there. ',\
                'So ',('{hero_he}',share.colors.hero),' travelled to ',
                ('{villainname}',share.colors.villain),'\'s evil lair to rescue',\
                ('{partner_him}',share.colors.partner),'". ',\
                   ]
        self.world=world.obj_world_traveltolair(self)
        self.addpart(self.world)


####################################################################################################################
####################################################################################################################
# Endings


class obj_scene_endingbasic(page.obj_chapterpage):
    def prevpage(self):
        pass# cant go back!
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5uncorrectending())
    def setup(self):
        self.text=[\
                   '" And ',('{hero_he}',share.colors.hero),' lived happily ever after, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very basic story)',(640,280)) )

        self.addpart( draw.obj_image('bed',(400,530), scale=0.25) )
        self.addpart( draw.obj_image('herobase',(580,490), scale=0.25) )
        self.addpart( draw.obj_image('sun',(893,411), scale=0.25) )
        self.addpart( draw.obj_image('moon',(410,365), scale=0.25) )
        self.addpart( draw.obj_image('fish',(843,540), scale=0.15,rotate=90) )


class obj_scene_endingevil(page.obj_chapterpage):
    def prevpage(self):
        pass# cant go back!
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch5uncorrectending())
    def setup(self):
        self.text=[\
                   '"And ',('{hero_he}',share.colors.hero),' lived evily ever after, the End". ',\
                   ]
        self.addpart( draw.obj_image('endframe',(640,410),path='premade') )
        self.addpart( draw.obj_textbox('The End',(640,200),fontsize='huge') )
        self.addpart( draw.obj_textbox('(of a very evil story)',(640,280)) )
        self.addpart( draw.obj_image('house',(320,430), scale=0.25) )
        self.addpart( draw.obj_image('tree',(340,560), scale=0.25) )
        self.addpart( draw.obj_image('tower',(950,430), scale=0.25) )
        self.addpart( draw.obj_image('mountain',(910,540), scale=0.25) )
        self.addpart( draw.obj_image('herobaseangry',(538,439),scale=0.3,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('partnerbaseangry',(732,570),scale=0.3,rotate=92,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('villainbase',(808,462),scale=0.27,rotate=92,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flame',(467,582),scale=0.21,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(417,331),scale=0.21,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('flame',(850,347),scale=0.21,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flame',(972,347),scale=0.16,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'flame','herobaseangry','partnerbaseangry','villainbase') )



class obj_scene_ch5uncorrectending(page.obj_chapterpage):
    def prevpage(self):
        pass# cant go back!
    def nextpage(self):
        if share.datamanager.getword('choice_restartstory')=='yes':
            share.scenemanager.switchscene(obj_scene_sunrise())
        else:
            super().nextpage()
    def setup(self):
        self.text=['This is interesting but not exactly the ending we were looking for, said the book of things. ',
                   'Do you wan to restart the story. ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )
        y1=200
        self.addpart( draw.obj_textbox('Restart the story:',(200,y1)) )
        textchoice=draw.obj_textchoice('choice_restartstory')
        textchoice.addchoice('1. Yes','yes',(640,y1))
        textchoice.addchoice('2. No','no',(1040,y1))
        self.addpart( textchoice )

# Default page
class obj_scene_default(page.obj_chapterpage):
    def prevpage(self):
        pass
    def nextpage(self):
        pass
    def setup(self):
        self.text=[\
                'default page',\
                   ]

####################################################################################################################
####################################################################################################################

#
