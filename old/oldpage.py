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
    def __init__(self):
        # elements
        self.to_update=[]
        self.to_finish=[]
        # setup
        self.presetup() 
        self.setup()
        self.postsetup()
    # def __del__(self):
        # print('deleted: '+str(self))# pages are consistently deleted when no longer in use by scenemanager
    def presetup(self):# background
        self.addpart(draw.obj_pagebackground())
    def setup(self):# custom elements
        pass
    def postsetup(self):# foreground
        self.addpart(draw.obj_pagedisplay_fps())        
    def addpart(self,element):
        term=['drawing','textinput','textchoice','textbox','image','animation','dispgroup',\
              'pagebackground','pagefps','pagenumber','pagenote','pagetext',\
              'world']
        if element.type in term:
            self.to_update.append(element)            
        if element.type in ['drawing','textinput','textchoice']:
            self.to_finish.append(element)        
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i: i.remove(element)
    def update(self,controls):
        self.prepage(controls)
        self.page(controls) 
        self.postpage(controls) 
    def prepage(self,controls):# background
        for i in self.to_update: i.update(controls)
    def page(self,controls):# custom updates
        pass
    def postpage(self,controls):# foreground
        pass
    def preendpage(self):# before exiting page
        for i in self.to_finish: i.finish()     



# chapter page template: a page in a chapter of the book
class obj_chapterpage(obj_page):  
    def __init__(self):
        self.text=[]# Main body of text
        self.textkeys={}
        super().__init__()
    def postsetup(self):
        super().postsetup()
        self.addpart(draw.obj_pagedisplay_number())
        self.addpart(draw.obj_pagedisplay_note('[Tab: Back]  [Enter: Continue]'))
        term=draw.obj_pagedisplay_text()
        term.make(self.text,**self.textkeys)# rebuild main text
        self.addpart(term)
    def prepage(self,controls):# background
        super().prepage(controls)
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
    def callprevpage(self,controls):
        if controls.tab and controls.tabc:
            self.preendpage()# template
            self.endpage()# customized
            share.ipage -= 1
            self.prevpage()# switch to prev page
    def callexitpage(self,controls):
        if controls.esc and controls.esc: # go back to main menu
            self.preendpage()# template
            self.endpage()# customized
            share.ipage = 1
            self.exitpage()
    def callnextpage(self,controls):
        if controls.enter and controls.enterc: 
            self.preendpage()# template
            self.endpage()# customized
            share.ipage += 1
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
