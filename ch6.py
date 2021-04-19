#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter6.py: ...
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

# Chapter VI: ...
# *CHAPTER VI

# name house
class obj_scene_chapter6(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_sunrise())
    def setup(self):
        self.text=['-----   Chapter V: The Full Story   -----   ',\
                   ]

        y1=200
        self.addpart( draw.obj_textbox('unlock partner:',(180,y1)) )
        textchoice=draw.obj_textchoice('unlock_partner')
        textchoice.addchoice('yes','True',(440,y1))
        textchoice.addchoice('no','False',(740,y1))
        self.addpart( textchoice )




class obj_scene_sunrise(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch4play())
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
        share.scenemanager.switchscene(obj_scene_fishing())
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


class obj_scene_fishing(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_wakeup())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"',('{heroname}',share.colors.hero),\
                     ' went to the river and caught a fish."',\
                   ]
        self.world=world.obj_world_fishing(self)
        self.addpart(self.world)


class obj_scene_mailbox(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_fishing())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromvillain())
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


class obj_scene_letterfromvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_mailboxagain())
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



class obj_scene_mailboxagain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailbox())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromelder())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.s and controls.sc)
    def setup(self):
        self.text=[\
                  '"',\
                    ('{heroname}',share.colors.hero),' checked ',\
                    ('{hero_his}',share.colors.hero),' mailbox again.',\
                    ('{hero_he}',share.colors.hero),' had received ',\
                    'another ',' letter". ',\
                   ]
        self.addpart(draw.obj_textbox('Press [S] to Continue',(640,660),color=share.colors.instructions))
        self.addpart( draw.obj_image('herobase',(204,470),scale=0.65,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1059,526),scale=0.65,rotate=0,fliph=False,flipv=False) )
        animation1=draw.obj_animation('ch2_mail1','mailletter',(640,360),record=False)
        animation1.addimage('empty',path='premade')
        self.addpart(animation1)
        self.addpart( draw.obj_animation('ch2_mail2','sun',(640,360),record=False,sync=animation1) )



class obj_scene_letterfromelder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_mailboxagain())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travelhomepeak())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or (controls.w and controls.wc)
    def setup(self):
        self.addpart( draw.obj_textbox('"The second letter said:"',(163+30,83)) )
        xmargin=100
        ymargin=230
        self.textkeys={'pos':(xmargin,ymargin),'xmin':xmargin,'xmax':770}# same as ={}
        self.text=[\
                    'Dear ',\
                    ('[Current resident at the House with Trees]',share.colors.hero),', ',\
                      '\nDo you need to rescue someone. ',\
                      'Fight a ',('villain',share.colors.villain),'. ',\
                     'Come find help at the  ',\
                    ('highest peak',share.colors.location),'. ',\
                    '\n\nsigned: unknown. ',\
                   ]
        self.addpart( draw.obj_image('mailframe',(640,400),path='premade') )
        self.addpart( draw.obj_image('interrogationmark',(1065,305),path='premade',scale=1.5) )
        self.addpart(draw.obj_textbox('Press [W] to Continue',(640,670),color=share.colors.instructions))


class obj_scene_travelhomepeak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_letterfromelder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_climbpeak())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '" And so ',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('highest peak',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='home',goal='peak',chapter=5)
        self.addpart(self.world)


class obj_scene_climbpeak(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travelhomepeak())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_meetelder())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"',('{hero_he}',share.colors.hero),\
                ' climbed the ',('highest peak',share.colors.location),'".',\
                   ]
        self.world=world.obj_world_climbpeak(self)
        self.addpart(self.world)



class obj_scene_meetelder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_climbpeak())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_elderoffer())
    def setup(self):
        self.text=[\
               '"At the top of the ',('highest peak',share.colors.location),', above the clouds, ',\
               ('{heroname}',share.colors.hero),' met the ',('elder',share.colors.elder),' called ',\
               ('{eldername}',share.colors.elder),'. ',\

                   ]
        self.addpart( draw.obj_image('elderbase',(964,325),scale=0.48,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mountain',(72,655),scale=0.34,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(209,681),scale=0.22,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(530,603),scale=0.55,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(266,557),scale=0.43,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(84,527),scale=0.24,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1184,487),scale=0.42,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1219,584),scale=0.32,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('cloud',(339,663),scale=0.22,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('floor4',(1280-500,720-140),path='premade') )
        animation1=draw.obj_animation('ch5_meetelder','herobase',(640,360),record=False)
        self.addpart( animation1 )
        self.addpart( draw.obj_animation('ch5_meetelder2','sun',(640,360),record=True,sync=animation1) )
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','cloud','sun','mountain') ) )


class obj_scene_elderoffer(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_meetelder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())

    def setup(self):
        self.text=[\
               '"I may grant you the gift of ',('agility',share.colors.item),\
               ', said ',('{eldername}',share.colors.elder),'. ',\
               'All you have to do is win a game of ',('rock-paper-scissors',share.colors.item),\
               '". ',\
                  ]
        self.addpart( draw.obj_image('sun',(188,298),scale=0.37,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(71,576),scale=0.28,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('mountain',(221,630),scale=0.39,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1053,226),scale=0.5,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(1192,383),scale=0.32,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('cloud',(313,444),scale=0.32,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_imageplacer(self,'cloud','sun','mountain') )
        animation1=draw.obj_animation('ch5eldertalks1','elderbase',(640,360),record=False)
        self.addpart( animation1 )



class obj_scene_rpselder(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_elderoffer())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_elderwon())
        else:
            share.scenemanager.switchscene(obj_scene_rpselderfail())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
               '"And so they played".',\
                  ]
        self.world=world.obj_world_rockpaperscissors(self)
        self.addpart(self.world)
class obj_scene_rpselderfail(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' lost."',\
                'Well, that doesnt sound right, said the book of things. ',\
               ('Peek',share.colors.hero),' at what your opponent is thinking and ',\
               ('counter',share.colors.hero),' at the ',\
               ('last moment',share.colors.hero),'. ',\
                'Now try again. ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )


class obj_scene_elderwon(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_rpselder())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travelpeaklair())
    def setup(self):
        self.text=[\
                '"You won! said ',('{eldername}',share.colors.elder),'. ',\
               'As a reward, I shall grant you the gift of ',('agility',share.colors.item),'.', \
               'With this, you will even be able to dodge bullets".',\
                  ]
        # self.addpart(draw.obj_imageplacer(self,'sun','cloud','mountain','elderbase'))
        animation1=draw.obj_animation('ch5eldertalks5','elderbase',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch5eldertalks5a','lightningbolt',(640,360),record=False,sync=animation1)
        animation2.addimage('empty',path='premade')
        self.addpart( animation2 )
        animation3=draw.obj_animation('ch5eldertalks5b','lightningbolt',(640,360),record=False,sync=animation1)
        animation3.addimage('empty',path='premade')
        self.addpart( animation3 )



class obj_scene_travelpeaklair(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_elderwon())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_meetvillain())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '" And so ',\
                    ('{heroname}',share.colors.hero),' travelled to the ',\
                  ('evil lair',share.colors.location),'". ',\
                   ]
        self.world=world.obj_world_travel(self,start='peak',goal='tower',chapter=5)
        self.addpart(self.world)




class obj_scene_meetvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travelpeaklair())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
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



class obj_scene_dodgebullets(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_meetvillain())
    def nextpage(self):
        if self.world.win:
            share.scenemanager.switchscene(obj_scene_defeatvillain())
        else:
            share.scenemanager.switchscene(obj_scene_dodgebulletsdeath())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"They fought with guns". ',\
                   ]
        self.world=world.obj_world_dodgegunshots(self)
        self.addpart(self.world)
class obj_scene_dodgebulletsdeath(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def setup(self):
        self.text=[\
                  '"... and then the ',('hero',share.colors.hero),' died."',\
                'Well, that doesnt sound right, said the book of things. ',\
              'Dont do that all the time it gets annoying you know. ',\
                'Now go back and try to act more "heroic". ',\
                   ]
        self.addpart(draw.obj_image('herobase',(640,540),scale=0.5,rotate=120))
        self.addpart(draw.obj_textbox('You are Dead',(640,360),scale=1.5) )



class obj_scene_defeatvillain(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dodgebullets())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_travellairhome())
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




class obj_scene_travellairhome(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_defeatvillain())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_dinner())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                  '"',('{heroname}',share.colors.hero),' and ',\
                  ('{partnername}',share.colors.partner),' went back home". ',\
                   ]
        self.world=world.obj_world_travel(self,start='tower',goal='home',chapter=3,partner=True)
        self.addpart(self.world)




class obj_scene_dinner(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_travellairhome())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_serenade())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                    '"They  ate ',\
                    ('fish',share.colors.item),' for dinner".',\
                   ]
        self.world=world.obj_world_eatfish(self,partner=True)
        self.addpart(self.world)


class obj_scene_serenade(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_dinner())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_kiss())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"',('{heroname}',share.colors.hero),' charmed ',\
                   ('{partnername}',share.colors.partner),' with a serenade..." ',\
                   ]
        self.world=world.obj_world_serenade(self)
        self.addpart(self.world)


class obj_scene_kiss(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_serenade())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall())
    def triggernextpage(self,controls):
        return (controls.enter and controls.enterc) or self.world.done# quick skip
    def setup(self):
        self.text=[\
                   '"...and then they kissed".   ',\
                   ]
        self.world=world.obj_world_kiss(self)
        self.addpart(self.world)


class obj_scene_nightfall(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_kiss())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_gotobed())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                '"It was already night".',\
                   ]
        self.world=world.obj_world_sunset(self)
        self.addpart(self.world)


class obj_scene_gotobed(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_nightfall())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   '"',\
                   ('{heroname}',share.colors.hero),' and ',('{partnername}',share.colors.partner),\
                   ' went back to bed". ',\
                   ]
        self.world=world.obj_world_gotobed(self,partner=True)
        self.addpart(self.world)
