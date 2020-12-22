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
import pyg
import page
#
import tests
import ch0
import ch1
import ch2


##########################################################
##########################################################
# Game Main Menu
# *TITLESCREEN

class obj_scene_titlescreen:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager        
        self.setup()
        #
    def setup(self):# setup (refresh content)
        # current chapter
        self.ichapter=share.savefile.chapter# read current selected chapter (-1=Erase,0=Prologue,1=Hero,etc...)
        # page number reset
        share.ipage=1
        # Reload window icon 
        share.windowicon.reset()
        # setup menu decorations (from book)
        if utils.pathexists('book/book.png'): 
            self.imgbook=pyg.loadsurface('book/book.png')
            self.imgbook=pyg.scalesurface(self.imgbook,(210,180))
            self.imgbook.set_colorkey(share.colors.colorkey)
        else:
            self.imgbook=[]
        if utils.pathexists('book/pen.png'): 
            self.imgpen=pyg.loadsurface('book/pen.png')
            self.imgpen=pyg.scalesurface(self.imgpen,(32,72))
            self.imgpen.set_colorkey(share.colors.colorkey)
        else:
            self.imgpen=[]        
        if utils.pathexists('book/eraser.png'): 
            self.imgeraser=pyg.loadsurface('book/eraser.png')
            self.imgeraser=pyg.scalesurface(self.imgeraser,(54,54))
            self.imgeraser.set_colorkey(share.colors.colorkey)
        else:
            self.imgeraser=[]
        # Prerender text
        self.textimg_startbook=share.fonts.font30.render('Start Book [Press Enter]',True,(0,0,0))
        self.textimg_instructions=share.fonts.font30.render('[Up/Down: Select]  [Enter: Read]',True,(0,0,0))
        self.textimg_erasebook=share.fonts.font30.render('Erase Book',True,(0,0,0))
        self.textimg_prologue=share.fonts.font30.render('Prologue',True,(0,0,0))
        self.textimg_chapt1=share.fonts.font30.render('Chapter I: The Hero',True,(0,0,0))
        self.textimg_chapt2=share.fonts.font30.render('Chapter II: A House',True,(0,0,0))
        self.textimg_cursor=share.fonts.font30.render('---',True,(0,0,0))
        self.textimg_devtests=share.fonts.font30.render('Appendix: Developer Tests (Press Space)',True,(0,0,0))
    def selectchapter(self,controls):
        if share.savefile.chapter<1:# new book
            if controls.enter  and controls.enterc: self.creator.scene=ch0.obj_scene_prologue(self.creator)
        else:
            # Change Chapter
            if (controls.s and controls.sc) or (controls.down and controls.downc): self.ichapter=min(self.ichapter+1,share.savefile.chapter)
            if (controls.w and controls.wc) or (controls.up and controls.upc): self.ichapter=max(self.ichapter-1,-1)
            # Go to Chapter
            if controls.enter  and controls.enterc: 
                if self.ichapter==-1: 
                    self.creator.scene=obj_scene_erasebook(self.creator)
                elif self.ichapter==0: 
                    self.creator.scene=ch0.obj_scene_prologue(self.creator)
                elif self.ichapter==1:
                    self.creator.scene=ch1.obj_scene_chapter1(self.creator)
                elif self.ichapter==2:
                    self.creator.scene=ch2.obj_scene_chapter2(self.creator)        
    def display(self):
        # Main elements
        share.screen.fill((255,255,255))
        share.screen.blit(share.fonts.font100.render('The Book of Things',True,(0,0,0)),(400,30))
        share.screen.blit(share.fonts.font30.render('By Sul',True,(0,0,0)),(1180,650))
        share.screen.blit(share.fonts.font30.render('Toggle Dev Mode: (Press Ctrl)',True,(0,0,0)),(10,680))
        # Menu text
        if share.savefile.chapter<1: share.screen.blit(self.textimg_startbook,(550,350))# empty book
        if share.savefile.chapter>0: 
            share.screen.blit(self.textimg_instructions,(550,350)) 
            share.screen.blit(self.textimg_erasebook,(550,380))
            share.screen.blit(self.textimg_prologue,(550,410))
            share.screen.blit(self.textimg_chapt1,(550,440))  
            share.screen.blit(self.textimg_cursor,(510,410+self.ichapter*30))            
            if share.savefile.chapter>1: share.screen.blit(self.textimg_chapt2,(550,470))          
        # Decorations
        if self.imgbook: share.screen.blit(self.imgbook,(530,150))   
        if self.imgeraser: share.screen.blit(self.imgeraser,(1180,600))
        if self.imgpen: share.screen.blit(self.imgpen,(470,360+self.ichapter*30))
        #        
    def devtools(self,controls):
        pyg.rectdisplay(share.screen,(0,0,220), (130,700,250,40)  )
        share.screen.blit(self.textimg_devtests,(970,680))
        if controls.space and controls.spacec: self.creator.scene=tests.obj_scene_tests(self.creator)   
    def update(self,controls):
        self.display()
        self.selectchapter(controls)      
        if share.devmode: self.devtools(controls)
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


class obj_scene_erasebookconfirmed(page.obj_page):
    def setup(self):      
        self.text=['Temporarily Unable to Erase the Book.',\
                   '\n Fix this in menu.py for final version [Tab: Back]']


# In Final version replace with the correct one
class obj_scene_erasebookconfirmed_BACKUP(page.obj_page):
    def setup(self):      
        self.text=['The book vanished.',\
                   '[Tab: Back]']
        share.savefile.eraseall()# erase all drawings and savefile
        share.words.eraseall()# erase all words written


####################################################################################################################
####################################################################################################################
        