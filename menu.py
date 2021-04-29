#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# menu.py: main menu
#
##########################################################
##########################################################


#
import share
import tool
import draw
import page
import world
#
import tests
import ch0
import ch1
import ch2
import ch3
import ch4
import ch5
import ch6
import ch7
import cha# remove this in final version



##########################################################
##########################################################

# Reference to titlescreen
class obj_scene_titlescreen:
    def __init__(self):
        pass
    def update(self,controls):
        # reloads main menu every time
        share.scenemanager.switchscene(obj_scene_realtitlescreen())


# Main Menu
class obj_scene_realtitlescreen(page.obj_page):
    def __init__(self):
        super().__init__()
    def presetup(self):
        super().presetup()
        # menu
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('By Sul',(1210,670),fontsize='smaller')
        self.sprite_pointer=draw.obj_textbox('---',(500-100,410),fontsize='smaller')
        self.sprite_info=draw.obj_textbox('[Up/Down: Select]  [Enter: Choose]',(640,350),fontsize='smaller')
        self.sprite_settings=draw.obj_textbox('Settings',(540,380),fontsize='smaller',xleft=True)
        self.sprite_start=draw.obj_textbox('Start New Book',(540,410),fontsize='smaller',xleft=True)
        self.sprite_prologue=draw.obj_textbox('Prologue: The Book of Things',(540,410),fontsize='smaller',xleft=True)
        self.sprite_ch1=draw.obj_textbox('Chapter I: The Hero',(540,440),fontsize='smaller',xleft=True)
        self.sprite_ch2=draw.obj_textbox('Chapter II: Home Sweet Home',(540,470),fontsize='smaller',xleft=True)
        self.sprite_ch3=draw.obj_textbox('Chapter III: Where are you',(540,500),fontsize='smaller',xleft=True)
        self.sprite_ch4=draw.obj_textbox('Chapter IV Something East',(540,530),fontsize='smaller',xleft=True)
        self.sprite_ch5=draw.obj_textbox('Chapter V: Higher and Higher',(540,560),fontsize='smaller',xleft=True)
        self.sprite_ch6=draw.obj_textbox('Chapter VI: Treasure Hunt',(540,590),fontsize='smaller',xleft=True)
        self.sprite_ch7=draw.obj_textbox('Chapter VII: Showtime',(540,620),fontsize='smaller',xleft=True)
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pointer)
        self.addpart(self.sprite_info)
        self.addpart(self.sprite_settings)
        self.addpart(self.sprite_start)
        self.addpart(self.sprite_prologue)
        self.addpart(self.sprite_ch1)
        self.addpart(self.sprite_ch2)
        self.addpart(self.sprite_ch3)
        self.addpart(self.sprite_ch4)
        self.addpart(self.sprite_ch5)
        self.addpart(self.sprite_ch6)
        self.addpart(self.sprite_ch7)
        # decorations
        self.sprite_pen=draw.obj_image('pen',(460-100,360), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        # devtools
        if share.devaccess:
            self.addpart(draw.obj_textbox('[Ctrl: Toggle Dev Mode]',(130,700),fontsize='smaller'))
            self.addpart(draw.obj_textbox('[F: Quick Access for Developer]',(640,700),fontsize='smaller'))
            self.addpart(draw.obj_textbox('[Space: Appendix Developer Tests]',(1120,700),fontsize='smaller'))

    def setup(self):
        super().setup()
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.ichapter=self.maxchapter# pointer position
        share.ipage=1# current page number in chapter
        # update menu (chapter dependent)
        self.sprite_author.show=self.maxchapter>0
        self.sprite_pointer.show=True
        self.sprite_info.show=True
        self.sprite_settings.show=True
        self.sprite_start.show=self.maxchapter==0
        self.sprite_prologue.show=self.maxchapter>0
        self.sprite_ch1.show=self.maxchapter>0
        self.sprite_ch2.show=self.maxchapter>1
        self.sprite_ch3.show=self.maxchapter>2
        self.sprite_ch4.show=self.maxchapter>3
        self.sprite_ch5.show=self.maxchapter>4
        self.sprite_ch6.show=self.maxchapter>5
        self.sprite_ch7.show=self.maxchapter>6
        # update decorations (chapter dependent)
        share.display.reseticon()# window icon
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_book.show=self.ichapter>0
        self.sprite_pen.show=self.ichapter>0
        self.sprite_eraser.show=self.ichapter>0
        # pointer
        self.sprite_pointer.movetoy(410+self.ichapter*30)
        self.sprite_pen.movetoy(360+self.ichapter*30)

    def page(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            self.ichapter=min(self.ichapter+1,self.maxchapter)
            self.sprite_pointer.movetoy(410+self.ichapter*30)
            self.sprite_pen.movetoy(360+self.ichapter*30)
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            self.ichapter=max(self.ichapter-1,-1)
            self.sprite_pointer.movetoy(410+self.ichapter*30)
            self.sprite_pen.movetoy(360+self.ichapter*30)
        if controls.enter  and controls.enterc:
            if self.ichapter==-1:
                share.scenemanager.switchscene(obj_scene_settings())
            elif self.ichapter==0:
                share.scenemanager.switchscene(ch0.obj_scene_prologue())
            elif self.ichapter==1:
                share.scenemanager.switchscene(ch1.obj_scene_chapter1())
            elif self.ichapter==2:
                share.scenemanager.switchscene(ch2.obj_scene_chapter2())
            elif self.ichapter==3:
                share.scenemanager.switchscene(ch3.obj_scene_chapter3())
            elif self.ichapter==4:
                share.scenemanager.switchscene(ch4.obj_scene_chapter4())
            elif self.ichapter==5:
                share.scenemanager.switchscene(ch5.obj_scene_chapter5())
            elif self.ichapter==6:
                share.scenemanager.switchscene(ch6.obj_scene_chapter6())
            elif self.ichapter==7:
                share.scenemanager.switchscene(ch7.obj_scene_chapter7())
        if controls.esc and controls.escc:
            share.quitgame()
        #############################################3
        if share.devaccess:
            if controls.space and controls.spacec:
                share.scenemanager.switchscene(tests.obj_scene_testmenu())
            if controls.f and controls.fc:
                #
                # change current WIP scene here
                quickscene=ch7.obj_scene_ch7p47()
                #
                share.scenemanager.switchscene(quickscene)
        #############################################3


####################################################################################################################
####################################################################################################################
# Settings Menu
class obj_scene_settings(page.obj_page):
    def __init__(self):
        super().__init__()
    def presetup(self):
        super().presetup()
        # Default settings
        share.datamanager.loadsettings()# load current settings
        #
        self.addpart( draw.obj_textbox('Settings',(640,80),fontsize='large') )
        self.addpart( draw.obj_textbox('[Tab: Back] [Up/Down: Select] [Enter: Change]',(640,
        350),fontsize='smaller') )
        self.maxjpos=4# max pointer position
        self.jpos=0# pointer position
        self.sprite_pointer=draw.obj_textbox('---',(400,380+self.jpos*30),fontsize='smaller')
        self.addpart(self.sprite_pointer)
        #
        self.difficultyeasy=draw.obj_textbox('Difficulty: Easy (Coming Soon)',(640,380),fontsize='smaller')
        self.difficultymedium=draw.obj_textbox('Difficulty: Medium',(640,380),fontsize='smaller')
        self.difficultyhard=draw.obj_textbox('Difficulty: Hard (Coming Sfoon)',(640,380),fontsize='smaller')
        self.screennative=draw.obj_textbox('Display: Windowed (1280x720)',(640,410),fontsize='smaller')
        self.screenadapted=draw.obj_textbox('Display: Fullscreen',(640,410),fontsize='smaller')
        self.musicoff=draw.obj_textbox('Music: Off',(640,440),fontsize='smaller')
        self.musicon=draw.obj_textbox('Music: On (Coming Soon)',(640,440),fontsize='smaller')
        self.soundoff=draw.obj_textbox('Sound: Off',(640,470),fontsize='smaller')
        self.soundon=draw.obj_textbox('Sound: On (Coming Soon)',(640,470),fontsize='smaller')
        self.addpart( draw.obj_textbox('Erase Book',(640,500),fontsize='smaller') )
        self.addpart( self.difficultyeasy )
        self.addpart( self.difficultymedium )
        self.addpart( self.difficultyhard )
        self.difficultyeasy.show=share.datamanager.leveldifficulty == 0
        self.difficultymedium.show=share.datamanager.leveldifficulty == 1
        self.difficultyhard.show=share.datamanager.leveldifficulty == 2
        self.addpart( self.screennative )
        self.addpart( self.screenadapted )
        self.screennative.show=share.datamanager.donative
        self.screenadapted.show=not share.datamanager.donative
        self.addpart( self.musicoff )
        self.addpart( self.musicon )
        self.musicoff.show=not share.datamanager.domusic
        self.musicon.show=share.datamanager.domusic
        self.addpart( self.soundoff )
        self.addpart( self.soundon )
        self.soundoff.show=not share.datamanager.dosound
        self.soundon.show=share.datamanager.dosound
    def page(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            self.jpos=min(self.jpos+1,self.maxjpos)
            self.sprite_pointer.movetoy(380+self.jpos*30)
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            self.jpos=max(self.jpos-1,0)
            self.sprite_pointer.movetoy(380+self.jpos*30)
        # change difficulty
        if self.jpos==0 and (controls.enter and controls.enterc):
            if share.datamanager.leveldifficulty == 0:
                share.datamanager.leveldifficulty=1
            elif share.datamanager.leveldifficulty == 1:
                share.datamanager.leveldifficulty=2
            else:
                share.datamanager.leveldifficulty=0
            self.difficultyeasy.show=share.datamanager.leveldifficulty == 0
            self.difficultymedium.show=share.datamanager.leveldifficulty == 1
            self.difficultyhard.show=share.datamanager.leveldifficulty == 2
            share.datamanager.savesettings()# save settings
        # change display
        if self.jpos==1 and (controls.enter and controls.enterc):
            share.datamanager.donative= not share.datamanager.donative
            self.screennative.show=share.datamanager.donative
            self.screenadapted.show=not share.datamanager.donative
            if share.datamanager.donative:
                share.display.reset(native=True)
            else:
                share.display.reset(native=False)
            share.datamanager.savesettings()# save settings
        # change music
        if self.jpos==2 and (controls.enter and controls.enterc):
            share.datamanager.domusic=not share.datamanager.domusic
            self.musicoff.show=not share.datamanager.domusic
            self.musicon.show=share.datamanager.domusic
            share.datamanager.savesettings()# save settings
        # change sound
        if self.jpos==3 and (controls.enter and controls.enterc):
            share.datamanager.dosound=not share.datamanager.dosound
            self.soundoff.show=not share.datamanager.dosound
            self.soundon.show=share.datamanager.dosound
            share.datamanager.savesettings()# save settings
        # erase book
        if self.jpos==4 and (controls.enter and controls.enterc):
            share.scenemanager.switchscene(obj_scene_erasebook())
        # back to titlescreen
        if (controls.tab and controls.tabc):
            share.scenemanager.switchscene(share.titlescreen,init=True)


####################################################################################################################
####################################################################################################################
# Erase Book
# *ERASE

class obj_scene_erasebook(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_erasebookconfirmed())
    def triggernextpage(self,controls):
        return controls.enter and controls.space and controls.lctrl
    def setup(self):
        self.text=['Press [Enter+Space+Ctrl] to erase the book. ',\
                    'You will loose all your drawings and progress. ',\
                    '[Tab: Back]',\
                    ]


class obj_scene_erasebookconfirmed(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def setup(self):
        self.text=['The book has vanished.',\
                   '[Tab: Back]']
        share.datamanager.erasebook()


####################################################################################################################
####################################################################################################################
