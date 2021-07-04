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
        self.initstart(**kwargs)
    def initstart(self,**kwargs):# start
        # elements
        self.to_start=[]# elements to start when they are added
        self.to_update=[]# elements to manage at page update
        self.to_finish=[]# elements to manage at page finish
        # unique page elements (one per page therefore are overwritten)
        self.pagemusic=draw.obj_music(None)# menu music by default
        # setup
        self.presetup()
        self.setup(**kwargs)# potential kwargs passed to setup
        self.postsetup()
        self.postpostsetup()
    def presetup(self):# background
        self.addpart(draw.obj_pagebackground())
        # share.soundplayer.stop()# stop all sounds for safety (omitted for soundnextpage,etc)
    def setup(self,**kwargs):# custom elements
        pass
    def postsetup(self):# foreground
        if share.datamanager.doshowfps:
            self.addpart(draw.obj_pagedisplay_fps())
    def postpostsetup(self):# foreground (DO NOT APPEND)
        self.addpart(draw.obj_pagemousepointer())
    #
    def pagename(self):# page has a name for scene inventories (optional)
        return None
    def addpart(self,element):
        term=['timer']
        if element.type in term:
            self.to_start.append(element)
            element.start()# element is started as it is added
        #
        term=['drawing','textinput','textchoice','textbox','image','animation','dispgroup',\
              'imageplacer','soundplacer',\
              'sound',\
              'rectangle',\
              'timer',\
              'pagebackground','pagefps','pagetext','pagemousepointer',\
              'world']
        if element.type in term:
            self.to_update.append(element)
        #
        term=['drawing','textinput','textchoice',\
                'imageplacer',\
                'dispgroup','animation','sound']# dispgroups hold animations hold sounds, so all must finish
        if element.type in term:
            self.to_finish.append(element)
        #
        if element.type=='music':# override page music (unique element)
            self.pagemusic=element
    def removepart(self,element):
        for i in [self.to_update,self.to_finish]:
            if element in i:
                i.remove(element)
    # def __del__(self):# not needed: pages are consistently deleted when no longer in use
        # print('deleted: '+str(self))
    #
    def update(self,controls):
        self.prepage(controls)
        self.page(controls)
        self.postpage(controls)
    def prepage(self,controls):# background
        for i in self.to_update:
            i.update(controls)
        if self.pagemusic:
            self.pagemusic.update(controls)
    def page(self,controls):# custom updates
        pass
    def postpage(self,controls):# foreground
        pass
    def preendpage(self):# before exiting page
        for i in self.to_finish:
            i.finish()# finish drawings/textinput/textchoice (saves them), sounds (stop them)




# chapter page template: a page in a chapter of the book
class obj_chapterpage(obj_page):
    def initstart(self,**kwargs):
        self.text=[]# Main body of text
        self.textkeys={}
        super().initstart(**kwargs)
    def presetup(self):
        super().presetup()
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
        #
    def postsetup(self):
        super().postsetup()
        self.pagetext=draw.obj_pagedisplay_text()
        self.pagetext.make(self.text,**self.textkeys)# rebuild main text
        self.addpart(self.pagetext)
        #
        # Mouse Browsing (optional)
        self.textboxplace()# place textboxes
        self.textboxopt={}# default
        self.textboxset()# set options
        self.dotextboxprevpage=False
        self.textboxprevpage()
        self.dotextboxnextpage=False
        self.textboxnextpage()
    # textboxes for mouse browsing
    def textboxplace(self):
        pagetext_x,pagetext_y=self.pagetext.getposition()
        if pagetext_x<1080:
            self.textboxnextpage_xy=( pagetext_x+10,pagetext_y+33 )
        else:
            self.textboxnextpage_xy=( 50,pagetext_y+90 )
    def textboxprevpage(self):# no back option anymore (obsolete)
        self.dotextboxprevpage=False
    def textboxset(self):# change textboxopt by user here
        pass# user options for the nextpage
        # self.textboxopt={'show',False}# remnoves the textbox
        # self.textboxopt={'xy',(640,510)}# set position
        # self.textboxopt={'text','[continue]'}# set text
        # self.textboxopt={'align','center'}# set align ('left','right' or 'center')
    def textboxnextpage(self):
        self.dotextboxnextpage=True# keep
        self.textboxref={'do':True, 'xy':self.textboxnextpage_xy,'text':'[next]','align':'left'}# default
        for i in self.textboxopt.keys():# replace with optional keys if any
            self.textboxref[i]=self.textboxopt[i]
        # make
        self.dotextboxnextpage=self.textboxref['do']
        if self.dotextboxnextpage:
            if self.textboxref['align']=='right':
                self.textbox_next=draw.obj_textbox(self.textboxref['text'],\
                self.textboxref['xy'],color=(138,0,138),hover=True,hovercolor=(220,0,220),fontsize='medium',xright=True)
            elif self.textboxref['align']=='center':
                self.textbox_next=draw.obj_textbox(self.textboxref['text'],\
                self.textboxref['xy'],color=(138,0,138),hover=True,hovercolor=(220,0,220),fontsize='medium')
            else:
                self.textbox_next=draw.obj_textbox(self.textboxref['text'],\
                self.textboxref['xy'],color=(138,0,138),hover=True,hovercolor=(220,0,220),fontsize='medium',xleft=True)
            self.addpart(self.textbox_next)
    #############
    def prepage(self,controls):# background
        super().prepage(controls)
        self.callprevpage(controls)
        self.callnextpage(controls)
        self.callexitpage(controls)
    # first level (may customize for pages, e.g. if minigame)
    def triggerprevpage(self,controls):
        return False
        # return self.textbox_prev.isclicked(controls)
    def triggernextpage(self,controls):
        return self.textbox_next.isclicked(controls)
    def triggerexitpage(self,controls):
        return controls.gq and controls.gqc
    # second level (required in rare cases)
    def triggerprevpage2(self,controls):
        return True and self.triggerprevpage(controls)
    def triggernextpage2(self,controls):
        return True and self.triggernextpage(controls)
    def triggerexitpage2(self,controls):
        return True and self.triggerexitpage(controls)
    # third level (dev)
    def triggerprevpage3(self,controls):
        return self.triggerprevpage2(controls) or (share.devmode and controls.gb and controls.gbc)
    def triggernextpage3(self,controls):
        return self.triggernextpage2(controls) or (share.devmode and controls.ga and controls.gac)
    def triggerexitpage3(self,controls):
        return self.triggerexitpage2(controls)
    #############################
    def callprevpage(self,controls):
        if self.triggerprevpage3(controls):
            self.preendpage()# template
            self.endpage()# customized
            self.soundprevpage()
            self.prevpage()# switch to prev page
    def callexitpage(self,controls):
        if self.triggerexitpage3(controls): # go back to main menu
            self.preendpage()# template
            self.endpage()# customized
            self.soundexitpage()
            self.exitpage()
    def callnextpage(self,controls):
        if self.triggernextpage3(controls):
            self.preendpage()# template
            self.endpage()# customized
            self.soundnextpage()
            self.nextpage()# switch to next page
    def soundprevpage(self):
        self.sound_menuback.play()
    def soundexitpage(self):
        self.sound_menuback.play()
    def soundnextpage(self):
        self.sound_menugo.play()
    def endpage(self):# when exit page
        pass
    def prevpage(self):# actions to prev page (replace here)**
        share.scenemanager.switchscene(share.titlescreen,initstart=True)
    def exitpage(self):
        share.scenemanager.switchscene(share.titlescreen,initstart=True)
    def nextpage(self):# actions to next page (replace here)**
        share.scenemanager.switchscene(share.titlescreen,initstart=True)


####################################################################################################################
