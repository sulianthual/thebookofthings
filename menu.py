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


##########################################################
##########################################################

# Main Menu
class obj_scene_titlescreen(page.obj_page):
    def __init__(self):
        super().__init__()
    def presetup(self):
        super().presetup()
        # menu
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('By Sul',(1210,670),fontsize='smaller')
        self.sprite_pointer=draw.obj_textbox('---',(500,410),fontsize='smaller')
        self.sprite_start=draw.obj_textbox('Start Book [Press Enter]',(640,350),fontsize='smaller')
        self.sprite_info=draw.obj_textbox('[Up/Down: Select]  [Enter: Read]',(640,350),fontsize='smaller')
        self.sprite_erase=draw.obj_textbox('Erase Book',(640,380),fontsize='smaller')
        self.sprite_prologue=draw.obj_textbox('Prologue: The Book of Things',(640,410),fontsize='smaller')
        self.sprite_ch1=draw.obj_textbox('Chapter 1: The Hero',(640,440),fontsize='smaller')
        self.sprite_ch2=draw.obj_textbox('Chapter 2: The Partner',(640,470),fontsize='smaller')
        self.sprite_ch3=draw.obj_textbox('Chapter 3: The Villain',(640,500),fontsize='smaller')
        self.sprite_ch4=draw.obj_textbox('Chapter 4: A Perfect Story',(640,530),fontsize='smaller')
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pointer)
        self.addpart(self.sprite_start)
        self.addpart(self.sprite_info)
        self.addpart(self.sprite_erase)
        self.addpart(self.sprite_prologue)
        self.addpart(self.sprite_ch1)
        self.addpart(self.sprite_ch2)
        self.addpart(self.sprite_ch3)
        self.addpart(self.sprite_ch4)
        # decorations
        self.sprite_pen=draw.obj_image('pen',(460,360), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        # devtools
        self.addpart(draw.obj_textbox('[Ctrl: Toggle Dev Mode]',(130,700),fontsize='smaller'))
        self.addpart(draw.obj_textbox('[Ctrl+Space: Access WIP]',(640,700),fontsize='smaller'))
        self.addpart(draw.obj_textbox('[Space: Appendix Developer Tests]',(1120,700),fontsize='smaller'))

    def setup(self):
        super().setup()
        self.maxchapter=share.datamanager.getprogress()# last chapter unlocked
        self.ichapter=self.maxchapter# pointer position
        share.ipage=1# current page number in chapter
        # update menu (chapter dependent)
        self.sprite_author.show=self.maxchapter>0
        self.sprite_pointer.show=self.maxchapter>0
        self.sprite_start.show=self.maxchapter==0
        self.sprite_info.show=self.maxchapter>0
        self.sprite_erase.show=self.maxchapter>0
        self.sprite_prologue.show=self.maxchapter>0
        self.sprite_ch1.show=self.maxchapter>0
        self.sprite_ch2.show=self.maxchapter>1
        self.sprite_ch3.show=self.maxchapter>2
        self.sprite_ch4.show=self.maxchapter>3
        # update decorations (chapter dependent)
        share.windowicon.reset()# window icon
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_book.show=self.ichapter>0
        self.sprite_pen.show=self.ichapter>0
        self.sprite_eraser.show=self.ichapter>0

    def page(self,controls):
        self.sprite_pointer.movetoy(410+self.ichapter*30)
        self.sprite_pen.movetoy(360+self.ichapter*30)
        if self.maxchapter<1:# new book
            if controls.enter  and controls.enterc:
                share.scenemanager.switchscene(ch0.obj_scene_prologue())
        else:
            if (controls.s and controls.sc) or (controls.down and controls.downc):
                self.ichapter=min(self.ichapter+1,self.maxchapter)
            if (controls.w and controls.wc) or (controls.up and controls.upc):
                self.ichapter=max(self.ichapter-1,-1)
            if controls.enter  and controls.enterc:
                if self.ichapter==-1:
                    share.scenemanager.switchscene(obj_scene_erasebook())
                elif self.ichapter==0:
                    share.scenemanager.switchscene(ch0.obj_scene_prologue())
                elif self.ichapter==1:
                    share.scenemanager.switchscene(ch1.obj_scene_chapter1())
                elif self.ichapter==2:
                    share.scenemanager.switchscene(ch2.obj_scene_chapter2())
                elif self.ichapter==3:
                    share.scenemanager.switchscene(ch3.obj_scene_chapter3())
                elif self.ichapter==4:
                    share.scenemanager.switchscene(ch3.obj_scene_chapter4())
        if controls.esc and controls.escc:
            share.quitgame()
        if controls.space and controls.spacec:
            share.scenemanager.switchscene(tests.obj_scene_testmenu())
        #
        #############################################3
        # Access WIP: Jump to scene directly (remove in final version)
        if controls.f and controls.fc:
            #
            # change current WIP scene here
            quickscene=ch3.obj_scene_ch3play()
            #
            share.scenemanager.switchscene(quickscene)
        #############################################3


####################################################################################################################
####################################################################################################################
# Erase Book
# *ERASE
class obj_scene_erasebook(page.obj_chapterpage):
    def setup(self):
        self.text=['It was decided to erase the book to start a new one. One had to be very sure.',\
                   'All drawings, all names would be erased, and everything would have to be created again.',\
                   '[Tab: Cancel]  [Enter: ',('Erase the Book',share.colors.red),']']
        self.addpart( draw.obj_animation('bookerase','book',(640,360)) )
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_erasebookconfirm())


class obj_scene_erasebookconfirm(page.obj_chapterpage):
    def setup(self):
        self.text=['A ',('LAST WARNING',share.colors.red),' was issued. It was time to make a big decision.',\
                   '\n[Tab: Cancel]  [Enter+Space+Ctrl: ',('ERASE THE BOOK',share.colors.red),']']
        self.addpart( draw.obj_image('book',(640,350)) )
    def callnextpage(self,controls):
        if controls.enter and controls.space and controls.lctrl:
            self.preendpage()# template
            self.endpage()# customized
            share.ipage += 1
            self.nextpage()# switch to next page
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_erasebookconfirmed())


# In Final version replace with the correct one
class obj_scene_erasebookconfirmed(page.obj_chapterpage):
    def setup(self):
        self.text=['The book vanished.',\
                   '[Tab: Back]']
        share.datamanager.erasebook()


####################################################################################################################
####################################################################################################################
