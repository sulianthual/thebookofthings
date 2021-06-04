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
import ch8



##########################################################
##########################################################

# Reference to titlescreen
class obj_scene_titlescreen(page.obj_page):
    def update(self,controls):
        # reloads main menu every time
        share.scenemanager.switchscene(obj_scene_realtitlescreen())


# Main Menu
class obj_scene_realtitlescreen(page.obj_page):
    def presetup(self):
        super().presetup()
        # menu
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('V1.0',(1210,670),fontsize='smaller')
        self.sprite_pointer=draw.obj_textbox('---',(500-100,410),fontsize='smaller')
        tempo= '['+share.datamanager.controlname('quit')+': exit] '
        tempo+= '['+share.datamanager.controlname('up')+'/'+share.datamanager.controlname('down')+': select] '
        tempo+= '['+share.datamanager.controlname('action')+': choose] '
        self.sprite_info=draw.obj_textbox(tempo,(640,350),fontsize='smaller')
        # self.sprite_info=draw.obj_textbox('[Esc: Exit] [Up/Down: Select] [Enter: Choose]',(640,350),fontsize='smaller')
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
        self.sprite_ch8=draw.obj_textbox('Epilogue',(540,650),fontsize='smaller',xleft=True)
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
        self.addpart(self.sprite_ch8)
        # decorations
        self.sprite_pen=draw.obj_image('pen',(460-100,360), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        # devtools
        if share.devaccess:
            tempo1= '['+share.datamanager.controlname('dev')+': toggle dev mode] '
            tempo2= '['+share.datamanager.controlname('right')+': appendix of tests] '
            tempo3= '['+share.datamanager.controlname('left')+': quick access scene] '
            textmat=['Developper Access is on:','(edit settings.txt to change)',tempo1,tempo2,tempo3]
            x1,y1,dy1=30,500,30
            for i in textmat:
                self.addpart(draw.obj_textbox(i,(x1,y1),fontsize='smaller',xleft=True,color=share.colors.instructions))
                y1 += dy1

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
        self.sprite_ch8.show=self.maxchapter>7
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
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        #
        # music
        if self.maxchapter>0:
            self.addpart( draw.obj_music('piano') )
        else:
            self.addpart( draw.obj_music('tension') )

    def page(self,controls):
        if controls.gd and controls.gdc:
            self.sound_menugo.play()
            # self.ichapter=min(self.ichapter+1,self.maxchapter)
            self.ichapter +=1
            if self.ichapter>self.maxchapter: self.ichapter=-1
            self.sprite_pointer.movetoy(410+self.ichapter*30)
            self.sprite_pen.movetoy(360+self.ichapter*30)
        if controls.gu and controls.guc:
            self.sound_menugo.play()
            # self.ichapter=max(self.ichapter-1,-1)
            self.ichapter -=1
            if self.ichapter<-1: self.ichapter=self.maxchapter
            self.sprite_pointer.movetoy(410+self.ichapter*30)
            self.sprite_pen.movetoy(360+self.ichapter*30)
        if controls.ga  and controls.gac:
            self.sound_menugo.play()
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
            elif self.ichapter==8:
                share.scenemanager.switchscene(ch8.obj_scene_chapter8())
        if controls.gq and controls.gqc:
            share.quitgame()
        #############################################3
        if share.devaccess:
            if controls.gr and controls.grc:
                share.scenemanager.switchscene(tests.obj_scene_testmenu())
            if controls.gl and controls.glc:
                #
                # change current WIP scene here
                quickscene=ch3.obj_scene_ch3p37()
                #
                share.scenemanager.switchscene(quickscene)# must not inistart if not testpage (for looped sounds)
                # share.scenemanager.switchscene(quickscene,initstart=True)# must initstart if a testpage
        #############################################3


####################################################################################################################
####################################################################################################################
# Settings Menu
class obj_scene_settings(page.obj_page):
    def setup(self,**kwargs):
        self.tosoundon=False# start page when turning back sound on
        # options
        if (kwargs is not None) and ('tosoundon' in kwargs):
            self.tosoundon=kwargs["tosoundon"]
        # Default settings
        share.datamanager.loadsettings()# load current settings
        # Text
        self.addpart( draw.obj_textbox('Settings',(640,80),fontsize='large') )
        tempo= '['+share.datamanager.controlname('back')+'/'+share.datamanager.controlname('quit')+': back] '
        tempo+= '['+share.datamanager.controlname('up')+'/'+share.datamanager.controlname('down')+': select] '
        tempo+= '['+share.datamanager.controlname('action')+': change] '
        self.addpart( draw.obj_textbox(tempo,(640,350),fontsize='smaller') )
        #
        self.maxjpos=5# max pointer position
        self.jpos=0# pointer position
        if self.tosoundon:# turning back sound
            self.jpos=3
        self.sprite_pointer=draw.obj_textbox('---',(400,380+self.jpos*30),fontsize='smaller')
        self.addpart(self.sprite_pointer)
        #
        self.keyboardqwerty=draw.obj_textbox('Keyboard: Qwerty (arrows = WASD)',(640,380),fontsize='smaller')
        self.keyboardazerty=draw.obj_textbox('Keyboard: Azerty (arrows = ZQSD)',(640,380),fontsize='smaller')
        self.addpart( self.keyboardqwerty )
        self.addpart( self.keyboardazerty )
        self.keyboardqwerty.show=not share.datamanager.doazerty
        self.keyboardazerty.show=share.datamanager.doazerty
        #
        self.screennative=draw.obj_textbox('Display: Windowed (1280x720)',(640,410),fontsize='smaller')
        self.screenadapted=draw.obj_textbox('Display: Fullscreen',(640,410),fontsize='smaller')
        self.addpart( self.screennative )
        self.addpart( self.screenadapted )
        self.screennative.show=share.datamanager.donative
        self.screenadapted.show=not share.datamanager.donative
        #
        self.musicoff=draw.obj_textbox('Music: Off',(640,440),fontsize='smaller')
        self.musicon=draw.obj_textbox('Music: On',(640,440),fontsize='smaller')
        self.addpart( self.musicoff )
        self.addpart( self.musicon )
        self.musicoff.show=not share.datamanager.domusic
        self.musicon.show=share.datamanager.domusic
        #
        self.soundoff=draw.obj_textbox('Sound: Off',(640,470),fontsize='smaller')
        self.soundon=draw.obj_textbox('Sound: On',(640,470),fontsize='smaller')
        self.addpart( self.soundoff )
        self.addpart( self.soundon )
        self.soundoff.show=not share.datamanager.dosound
        self.soundon.show=share.datamanager.dosound
        #
        self.addpart( draw.obj_textbox('Erase Book',(640,500),fontsize='smaller') )
        self.addpart( draw.obj_textbox('Credits',(640,530),fontsize='smaller') )

        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
        if self.tosoundon:
            self.sound_menuback.play()
        #
        self.addpart( draw.obj_music('tension') )
        #
    def page(self,controls):
        if controls.gd and controls.gdc:
            self.sound_menugo.play()
            # self.jpos=min(self.jpos+1,self.maxjpos)
            self.jpos +=1
            if self.jpos>self.maxjpos: self.jpos=0
            self.sprite_pointer.movetoy(380+self.jpos*30)
        if controls.gu and controls.guc:
            self.sound_menugo.play()
            # self.jpos=max(self.jpos-1,0)
            self.jpos -=1
            if self.jpos<0: self.jpos=self.maxjpos
            self.sprite_pointer.movetoy(380+self.jpos*30)
        # change difficulty
        if self.jpos==0 and (controls.ga and controls.gac):
            self.sound_menuback.play()
            share.datamanager.doazerty=not share.datamanager.doazerty
            share.controls.azerty=share.datamanager.doazerty# change controls as well
            self.keyboardqwerty.show=not share.datamanager.doazerty
            self.keyboardazerty.show=share.datamanager.doazerty
            share.datamanager.savesettings()# save settings
        # change display
        if self.jpos==1 and (controls.ga and controls.gac):
            self.sound_menuback.play()
            share.datamanager.donative= not share.datamanager.donative
            self.screennative.show=share.datamanager.donative
            self.screenadapted.show=not share.datamanager.donative
            if share.datamanager.donative:
                share.display.reset(native=True)
            else:
                share.display.reset(native=False)
            share.datamanager.savesettings()# save settings
        # toggle music
        if self.jpos==2 and (controls.ga and controls.gac):
            share.datamanager.domusic=not share.datamanager.domusic
            if share.datamanager.domusic:
                share.musicplayer.setmastervolume(1)
            else:
                share.musicplayer.setmastervolume(0)
            self.musicoff.show=not share.datamanager.domusic
            self.musicon.show=share.datamanager.domusic
            share.datamanager.savesettings()# save settings
        # toggle sound
        if self.jpos==3 and (controls.ga and controls.gac):
            share.datamanager.dosound=not share.datamanager.dosound
            if share.datamanager.dosound:
                share.soundplayer.setmastervolume(1)
            else:
                share.soundplayer.setmastervolume(0)
            self.soundoff.show=not share.datamanager.dosound
            self.soundon.show=share.datamanager.dosound
            share.datamanager.savesettings()# save settings
            share.scenemanager.switchscene(obj_scene_settings(tosoundon=True))# reload scene
        # erase book
        if self.jpos==4 and (controls.ga and controls.gac):
            self.sound_menugo.play()
            share.scenemanager.switchscene(obj_scene_erasebook())
        # read game credits
        if self.jpos==5 and (controls.ga and controls.gac):
            self.sound_menugo.play()
            share.scenemanager.switchscene(obj_scene_creditscreen())
        # back to titlescreen
        if (controls.gb and controls.gbc) or (controls.gq and controls.gqc):
            self.sound_menuback.play()
            share.scenemanager.switchscene(share.titlescreen,initstart=True)


####################################################################################################################
####################################################################################################################
# Credits
# *CREDITS

class obj_scene_creditscreen(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def triggernextpage(self,controls):
        return False
    def setup(self):
        self.text=['Credits: ',\
                    '\n\nThe book of things: a game by Sulian Thual (circa 2020-2021). ',\
                    'Made with Pygame. ',\
                    'All musics from PlayOnLoop.com (Licensed under Creative Commons by Attribution 4.0). ',\
                    'Sounds from opengameart.com and freesound.com (License CC0). ',\
                   '[',share.datamanager.controlname('back'),': back]']
        #
        self.addpart( draw.obj_music('tension') )


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
        return controls.gl and controls.gu and controls.gr and controls.ga
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempo= 'Press ['+share.datamanager.controlname('left')
        tempo+= '+'+share.datamanager.controlname('up')
        tempo+= '+'+share.datamanager.controlname('right')
        tempo+= '+'+share.datamanager.controlname('action')
        tempo+= '] to erase the book.'
        self.text=[tempo,\
                    'You will loose all your drawings and progress. ',\
                    '[',share.datamanager.controlname('back'),': back]',\
                    ]
        #
        self.addpart( draw.obj_music('tension') )
        #

class obj_scene_erasebookconfirmed(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def setup(self):
        self.text=['The book has vanished. ',\
                   '[',share.datamanager.controlname('back'),': back]']
        share.datamanager.erasebook()
        #
        self.sound=draw.obj_sound('erasebook')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('tension') )

        #

####################################################################################################################
####################################################################################################################
