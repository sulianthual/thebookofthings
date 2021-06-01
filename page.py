#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# pages.py: game objects that make up a page in the book
#
##########################################################
##########################################################

import core# for sprites
#
import share
import draw
import tool

##########################################################
##########################################################


# Template for any game scene (called a page in the book of things)
class obj_page:
    def __init__(self,**kwargs):
        # elements
        self.to_update=[]# elements to manage at page update
        self.to_finish=[]# elements to manage at page finish
        # unique page elements (one per page therefore are overwritten)
        self.pagemusic=draw.obj_music('menu')# menu music by default
        # self.pagemusic=draw.obj_music(None)# menu music by default
        # setup
        self.presetup()
        self.setup(**kwargs)# potential kwargs passed to setup
        self.postsetup()
    # def __del__(self):
        # print('deleted: '+str(self))# pages are consistently deleted when no longer in use by scenemanager
    def presetup(self):# background
        self.addpart(draw.obj_pagebackground())
    def setup(self,**kwargs):# custom elements
        pass
    def postsetup(self):# foreground
        self.addpart(draw.obj_pagedisplay_fps())
    def addpart(self,element):
        term=['drawing','textinput','textchoice','textbox','image','animation','dispgroup',\
              'imageplacer','soundplacer',\
              'sound',\
              'rectangle',\
              'pagebackground','pagefps','pagetext',\
              'world']
        if element.type in term:
            self.to_update.append(element)
        if element.type in ['drawing','textinput','textchoice','imageplacer','sound']:
            self.to_finish.append(element)
        if element.type=='music':# override page music (unique element)
            self.pagemusic=element
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i: i.remove(element)
    def update(self,controls):
        self.prepage(controls)
        self.page(controls)
        self.postpage(controls)
    def prepage(self,controls):# background
        for i in self.to_update: i.update(controls)
        if self.pagemusic:
            self.pagemusic.update(controls)
    def page(self,controls):# custom updates
        pass
    def postpage(self,controls):# foreground
        pass
    def preendpage(self):# before exiting page
        for i in self.to_finish: i.finish()




# chapter page template: a page in a chapter of the book
class obj_chapterpage(obj_page):
    def __init__(self,**kwargs):
        self.text=[]# Main body of text
        self.textkeys={}
        super().__init__(**kwargs)
    def presetup(self):
        super().presetup()
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
    def postsetup(self):
        super().postsetup()
        term=draw.obj_pagedisplay_text()
        term.make(self.text,**self.textkeys)# rebuild main text
        self.addpart(term)
    def prepage(self,controls):# background
        super().prepage(controls)
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
    def triggerprevpage(self,controls):
        return controls.gb and controls.gbc
    def triggerexitpage(self,controls):
        return controls.gq and controls.gqc
    def triggernextpage(self,controls):
        return controls.ga and controls.gac
    def soundprevpage(self):
        self.sound_menuback.play()
    def soundexitpage(self):
        self.sound_menuback.play()
    def soundnextpage(self):
        self.sound_menugo.play()
    def callprevpage(self,controls):
        if self.triggerprevpage(controls):
            self.preendpage()# template
            self.endpage()# customized
            self.soundprevpage()
            self.prevpage()# switch to prev page
    def callexitpage(self,controls):
        if self.triggerexitpage(controls): # go back to main menu
            self.preendpage()# template
            self.endpage()# customized
            self.soundexitpage()
            self.exitpage()
    def callnextpage(self,controls):
        if self.triggernextpage(controls):
            self.preendpage()# template
            self.endpage()# customized
            self.soundnextpage()
            self.nextpage()# switch to next page
    def endpage(self):# when exit page
        pass
    def prevpage(self):# actions to prev page (replace here)**
        share.scenemanager.switchscene(share.titlescreen,init=True)
    def exitpage(self):
        share.scenemanager.switchscene(share.titlescreen,init=True)
    def nextpage(self):# actions to next page (replace here)**
        share.scenemanager.switchscene(share.titlescreen,init=True)


####################################################################################################################
