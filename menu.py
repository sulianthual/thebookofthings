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
import draw
import utils
import page
#
import tests
import ch0
import ch1
import ch2


##########################################################
##########################################################

# Main Menu
class obj_scene_titlescreen(page.obj_pagetemplate):
    def __init__(self,creator):
        super().__init__(creator)
    def presetup(self):
        super().presetup()
        # menu
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('By Sul',(1210,670),fontsize='smaller')
        self.sprite_pointer=draw.obj_textbox('---',(500,410),fontsize='smaller')
        self.sprite_start=draw.obj_textbox('Start Book [Press Enter]',(640,350),fontsize='smaller')
        self.sprite_info=draw.obj_textbox('[Up/Down: Select]  [Enter: Read]',(640,350),fontsize='smaller')
        self.sprite_erase=draw.obj_textbox('Erase Book',(640,380),fontsize='smaller')
        self.sprite_prologue=draw.obj_textbox('Prologue',(640,410),fontsize='smaller')
        self.sprite_ch1=draw.obj_textbox('Chapter I: The Hero',(640,440),fontsize='smaller')
        self.sprite_ch2=draw.obj_textbox('Chapter II: A House',(640,470),fontsize='smaller')  
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pointer)
        self.addpart(self.sprite_start)
        self.addpart(self.sprite_info)
        self.addpart(self.sprite_erase)
        self.addpart(self.sprite_prologue)
        self.addpart(self.sprite_ch1)
        self.addpart(self.sprite_ch2)
        # decorations
        self.sprite_pen=draw.obj_image('pen',(460,360), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        # devtools
        self.addpart(draw.obj_textbox('Toggle Dev Mode: (Press Ctrl)',(130,700),fontsize='smaller'))
        self.addpart(draw.obj_textbox('Appendix: Developer Tests (Press Space)',(1120,700),fontsize='smaller'))

    def setup(self):
        super().setup()
        self.ichapter=share.savefile.chapter# current chapter
        share.ipage=1# current page number
        
        # update menu (chapter dependent)
        self.sprite_author.show=self.ichapter>0
        self.sprite_pointer.show=self.ichapter>0
        self.sprite_start.show=self.ichapter==0
        self.sprite_info.show=self.ichapter>0
        self.sprite_erase.show=self.ichapter>0
        self.sprite_prologue.show=self.ichapter>0
        self.sprite_ch1.show=self.ichapter>0
        self.sprite_ch2.show=self.ichapter>1
        # update decorations (chapter dependent)
        share.windowicon.reset()# window icon  
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_book.show=self.ichapter>0
        self.sprite_pen.show=self.ichapter>0
        self.sprite_eraser.show=self.ichapter>0
        #
    def selectchapter(self,controls):
        self.sprite_pointer.movetoy(410+self.ichapter*30)
        self.sprite_pen.movetoy(360+self.ichapter*30)
        if share.savefile.chapter<1:# new book
            if controls.enter  and controls.enterc: self.creator.scene=ch0.obj_scene_prologue(self.creator)
        else:
            if (controls.s and controls.sc) or (controls.down and controls.downc): self.ichapter=min(self.ichapter+1,share.savefile.chapter)
            if (controls.w and controls.wc) or (controls.up and controls.upc): self.ichapter=max(self.ichapter-1,-1)
            if controls.enter  and controls.enterc: 
                if self.ichapter==-1: 
                    self.creator.scene=obj_scene_erasebook(self.creator)
                elif self.ichapter==0: 
                    self.creator.scene=ch0.obj_scene_prologue(self.creator)
                elif self.ichapter==1:
                    self.creator.scene=ch1.obj_scene_chapter1(self.creator)
                elif self.ichapter==2:
                    self.creator.scene=ch2.obj_scene_chapter2(self.creator)          
    def page(self,controls):
        self.selectchapter(controls)      
        if share.devmode and controls.space and controls.spacec: self.creator.scene=tests.obj_scene_tests(self.creator)  
        if controls.esc and controls.escc: share.quitgame()
            

####################################################################################################################
####################################################################################################################
# Erase Book
# *ERASE
class obj_scene_erasebook(page.obj_page):
    def setup(self):
        self.text=['It was decided to erase the book to start a new one. One had to be very sure.',\
                   'All drawings, all names would be erased, and everything would have to be created again.',\
                   '[Tab: Cancel]  [Enter: ',('Erase the Book',share.colors.red),']']
        self.addpart( draw.obj_animation('bookerase','book',(640,360)) )      
    def nextpage(self):
        self.creator.scene=obj_scene_erasebookconfirm(self.creator)


class obj_scene_erasebookconfirm(page.obj_page):
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
        self.creator.scene=obj_scene_erasebookconfirmed(self.creator)


# In Final version replace with the correct one
class obj_scene_erasebookconfirmed(page.obj_page):
    def setup(self):      
        self.text=['The book vanished.',\
                   '[Tab: Back]']
        share.savefile.eraseall()# erase all drawings and savefile
        share.words.eraseall()# erase all words written


####################################################################################################################
####################################################################################################################
        