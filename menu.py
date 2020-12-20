#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# book_menu.py: main menu of book of things
#
##########################################################
##########################################################

import sys
import os
import pygame
#
import share
import draw
import utils
#
import tests
import chapter0
import chapter1
import chapter2


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
        # menu decorations (from drawings)
        if os.path.exists('drawings/book.png'): 
            self.imgbook=pygame.image.load('drawings/book.png')
            self.imgbook=pygame.transform.scale(self.imgbook,(210,180))
            self.imgbook.set_colorkey((255,255,255))
        else:
            self.imgbook=[]
        if os.path.exists('drawings/pen.png'): 
            self.imgpen=pygame.image.load('drawings/pen.png')
            self.imgpen=pygame.transform.scale(self.imgpen,(32,72))
            self.imgpen.set_colorkey((255,255,255))
        else:
            self.imgpen=[]        
        if os.path.exists('drawings/eraser.png'): 
            self.imgeraser=pygame.image.load('drawings/eraser.png')
            self.imgeraser=pygame.transform.scale(self.imgeraser,(54,54))
            self.imgeraser.set_colorkey((255,255,255))
        else:
            self.imgeraser=[]  
        # Reload game window icon=book image (if created/modified during prologue)
        share.windowicon.reset()
        #
    def update(self,controls):
        # Screen
        share.screen.fill((255,255,255))
        share.screen.blit(share.fonts.font100.render('The Book of Things',True,(0,0,0)),(400,30))
        share.screen.blit(share.fonts.font30.render('By Sul',True,(0,0,0)),(1180,650))
        if self.imgbook: share.screen.blit(self.imgbook,(530,150))   
        if self.imgeraser: share.screen.blit(self.imgeraser,(1180,600)) 
        # Menu
        if share.savefile.chapter<1:
            self.startbook(controls)
        else:
            self.selectchapter(controls)
        # Access Developer Tests
        share.screen.blit(share.fonts.font30.render('Toggle Dev Mode: (Press Ctrl)',True,(0,0,0)),(10,680))
        if share.devmode: 
            pygame.draw.rect(share.screen, (0,0,220), (5, 680, 250,40), 3)
            share.screen.blit(share.fonts.font30.render('Appendix: Developer Tests (Press Space)',True,(0,0,0)),(970,680))
            if controls.space and controls.spacec:
                self.creator.scene=tests.obj_scene_tests(self.creator)
    def startbook(self,controls):# first time playing (share.savefile.chapter=0)
        share.screen.blit(share.fonts.font30.render('Start Book [Press Enter]',True,(0,0,0)),(550,350))
        if controls.enter  and controls.enterc: self.creator.scene=chapter0.obj_scene_prologue(self.creator)
    def selectchapter(self,controls):
        share.screen.blit(share.fonts.font30.render('[Up/Down: Select]  [Enter: Read]',True,(0,0,0)),(550,350)) 
        share.screen.blit(share.fonts.font30.render('Erase Book',True,(0,0,0)),(550,380))
        share.screen.blit(share.fonts.font30.render('Prologue',True,(0,0,0)),(550,410))
        if share.savefile.chapter>0: share.screen.blit(share.fonts.font30.render('Chapter I: The Hero',True,(0,0,0)),(550,440))  
        if share.savefile.chapter>1: share.screen.blit(share.fonts.font30.render('Chapter II: A House',True,(0,0,0)),(550,470))                
        # Select Chapter
        share.screen.blit(share.fonts.font30.render('---',True,(0,0,0)),(510,410+self.ichapter*30))
        if self.imgpen: share.screen.blit(self.imgpen,(470,360+self.ichapter*30))
        if (controls.s and controls.sc) or (controls.down and controls.downc): self.ichapter=min(self.ichapter+1,share.savefile.chapter)
        if (controls.w and controls.wc) or (controls.up and controls.upc): self.ichapter=max(self.ichapter-1,-1)
        # Go to Chapter
        if controls.enter  and controls.enterc: 
            if self.ichapter==-1: 
                self.creator.scene=obj_scene_erasebook(self.creator)
            elif self.ichapter==0: 
                self.creator.scene=chapter0.obj_scene_prologue(self.creator)
            elif self.ichapter==1:
                self.creator.scene=chapter1.obj_scene_chapter1(self.creator)
            elif self.ichapter==2:
                self.creator.scene=chapter2.obj_scene_chapter2(self.creator)
        # Quit Game with Esc
        if controls.esc and controls.escc: share.quitgame()
            
            

            

####################################################################################################################
####################################################################################################################
# Erase Book
# *ERASE
class obj_scene_erasebook(utils.obj_page):
    def setup(self):
        self.text=['It was decided to erase the book to start a new one. One had to be very sure.',\
                   'All drawings, all names would be erased, and everything would have to be created again.',\
                   '[Tab: Cancel]  [Enter: ',('Erase the Book',share.colors.red),']']
        self.addpart( draw.obj_animation('bookerase','book',(640,360)) )      
    def nextpage(self):
        self.creator.scene=obj_scene_erasebookconfirm(self.creator)


class obj_scene_erasebookconfirm(utils.obj_page):
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


class obj_scene_erasebookconfirmed(utils.obj_page):
    def setup(self):      
        self.text=['Temporarily Unable to Erase the Book.',\
                   '\n Fix this in menu.py for final version [Tab: Back]']


# In Final version replace with the correct one
class obj_scene_erasebookconfirmed_BACKUP(utils.obj_page):
    def setup(self):      
        self.text=['The book vanished.',\
                   '[Tab: Back]']
        share.savefile.eraseall()# erase all drawings and savefile
        share.words.eraseall()# erase all words written


####################################################################################################################
####################################################################################################################
        