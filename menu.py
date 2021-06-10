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
import page
import draw
import world
import tool
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
# quickscene: access a scene directly from titlescreen (for developper only)

class obj_quickscene():
     def __call__(self):
        #
        # if True :
        if False :
            # regular scenes
            #
            quickscene=obj_scene_settings()

            # quickscene=ch0.obj_scene_prologue()
            # quickscene=ch0.obj_scene_ch0p10()
            # quickscene=ch1.obj_scene_ch1p14()
            # quickscene=ch1.obj_scene_ch1play3()
            # quickscene=ch2.obj_scene_ch2p4()
            # quickscene=ch2.obj_scene_ch2play4()
            # quickscene=ch3.obj_scene_ch3p12()
            # quickscene=ch3.obj_scene_ch3p31()
            # quickscene=ch3.obj_scene_ch3p22easteregg()
            # quickscene=ch4.obj_scene_ch4p21()
            # quickscene=ch5.obj_scene_ch5p16()
            # quickscene=ch5.obj_scene_ch5p39()
            # quickscene=ch6.obj_scene_ch6p42()
            # quickscene=ch6.obj_scene_ch6p27()
            # quickscene=ch7.obj_scene_ch7p25()
            # quickscene=ch7.obj_scene_ch7p49()
            # quickscene=ch7.obj_scene_ch7ending()
            # quickscene=ch8.obj_scene_ch8west()
            # quickscene=ch8.obj_scene_ch8roam(start='island')
            #
            # minigames
            # quickscene=ch2.obj_scene_ch2p8()# ch2 serenade
            # quickscene=ch3.obj_scene_ch3p19()# ch3 dodge
            # quickscene=ch4.obj_scene_lyingstart()# ch4 lying
            # quickscene=ch5.obj_scene_ch5p36()# ch5 rps
            # quickscene=ch6.obj_scene_ch6p21()# ch6 travel (get logs)
            # quickscene=ch6.obj_scene_ch6p30()# ch6 sneak
            # quickscene=ch6.obj_scene_ch6p38a()# ch6 ride cow
            # quickscene=ch7.obj_scene_ch7p22()# ch7 dodge
            # quickscene=ch7.obj_scene_ch7p25()# ch7 stomp
            # quickscene=ch7.obj_scene_ch7p49()# ch7 mechs
            # quickscene=ch8.obj_scene_ch8roam()# ch8 travel
            # quickscene=ch8.obj_scene_ch8roam(start='island')
            #
            #
            share.scenemanager.switchscene(quickscene)# (must not initstart if has looped sounds)
        else:
            # test scenes (must initstart because are inventoried)
            # quickscene=tests.obj_scene_testdevnotes()
            # quickscene=tests.obj_scene_testdevnotesfiles()
            quickscene=tests.obj_scene_textbox()
            #
            # quickscene=tests.obj_scene_testdrafting()
            #
            #
            share.scenemanager.switchscene(quickscene,initstart=True)# (must initstart because are inventoried)



##########################################################
##########################################################
# bookmark: go to last completed scene according to progress
# database of bookmark names and corresponding scenes here

class obj_gotobookmark():
     def __call__(self):
        bookmarkname=share.datamanager.getbookmark()
        #
        # ch0
        if bookmarkname == 'ch0_start':# also default in datb.py if book is empty
            bookmarkscene=ch0.obj_scene_prologue()
        elif bookmarkname == 'ch0_drawpen':
            bookmarkscene=ch0.obj_scene_ch0p2()
        elif bookmarkname == 'ch0_draweraser':
            bookmarkscene=ch0.obj_scene_ch0p4()
        elif bookmarkname == 'ch0_drawbook':
            bookmarkscene=ch0.obj_scene_ch0p7()
        elif bookmarkname == 'ch0_meetbook':
            bookmarkscene=ch0.obj_scene_ch0p10()
        elif bookmarkname == 'ch0_endunlock':
            bookmarkscene=ch0.obj_scene_ch0unlocknext()
        #
        # ch1
        elif bookmarkname == 'ch1_start':
            bookmarkscene=ch1.obj_scene_chapter1()
        elif bookmarkname == 'ch1_writehero':
            bookmarkscene=ch1.obj_scene_ch1p1()
        elif bookmarkname == 'ch1_drawhero':
            bookmarkscene=ch1.obj_scene_ch1p3()
        elif bookmarkname == 'ch1_drawbed':
            bookmarkscene=ch1.obj_scene_ch1p5()
        elif bookmarkname == 'ch1_drawfish':
            bookmarkscene=ch1.obj_scene_ch1p9()
        elif bookmarkname == 'ch1_gotfish':
            bookmarkscene=ch1.obj_scene_ch1p11()
        elif bookmarkname == 'ch1_drawsun':
            bookmarkscene=ch1.obj_scene_ch1p14()
        elif bookmarkname == 'ch1_startplay':
            bookmarkscene=ch1.obj_scene_ch1play()
        elif bookmarkname == 'ch1_endunlock':
            bookmarkscene=ch1.obj_scene_ch1unlocknext()
        #
        # ch2
        elif bookmarkname == 'ch2_start':
            bookmarkscene=ch2.obj_scene_chapter2()
        elif bookmarkname == 'ch2_drawlove':
            bookmarkscene=ch2.obj_scene_ch2p2()
        elif bookmarkname == 'ch2_writepartner':
            bookmarkscene=ch2.obj_scene_ch2p3()
        elif bookmarkname == 'ch2_drawmail':
            bookmarkscene=ch2.obj_scene_ch2p6a()
        elif bookmarkname == 'ch2_drawmusic':
            bookmarkscene=ch2.obj_scene_ch2p7()
        elif bookmarkname == 'ch2_drawhouse':
            bookmarkscene=ch2.obj_scene_ch2p11()
        elif bookmarkname == 'ch2_drawbush':
            bookmarkscene=ch2.obj_scene_ch2p13()
        elif bookmarkname == 'ch2_startplay':
            bookmarkscene=ch2.obj_scene_ch2play()
        elif bookmarkname == 'ch2_endunlock':
            bookmarkscene=ch2.obj_scene_ch2unlocknext()
        #
        # ch3
        elif bookmarkname == 'ch3_start':
            bookmarkscene=ch3.obj_scene_chapter3()
        elif bookmarkname == 'ch3_writevillain':
            bookmarkscene=ch3.obj_scene_ch3p2()
        elif bookmarkname == 'ch3_startstory':
            bookmarkscene=ch3.obj_scene_ch3p5()
        elif bookmarkname == 'ch3_checkmail' :
            bookmarkscene=ch3.obj_scene_ch3p9()
        elif bookmarkname == 'ch3_drawmountain' :
            bookmarkscene=ch3.obj_scene_ch3p12()
        elif bookmarkname == 'ch3_drawgun' :
            bookmarkscene=ch3.obj_scene_ch3p15()
        elif bookmarkname == 'ch3_startdodge' :
            bookmarkscene=ch3.obj_scene_ch3p16()
        elif bookmarkname == 'ch3_windodge' :
            bookmarkscene=ch3.obj_scene_ch3p20()
        elif bookmarkname == 'ch3_gohome' :
            bookmarkscene=ch3.obj_scene_ch3p25a()
        elif bookmarkname == 'ch3_startbug' :
            bookmarkscene=ch3.obj_scene_ch3p31()
        elif bookmarkname == 'ch3_endbug' :
            bookmarkscene=ch3.obj_scene_ch3p39a()
        elif bookmarkname == 'ch3_endunlock':
            bookmarkscene=ch3.obj_scene_ch3unlocknext()
        #
        # ch4
        elif bookmarkname == 'ch4_start':
            bookmarkscene=ch4.obj_scene_chapter4()
        elif bookmarkname == 'ch4_drawalarm' :
            bookmarkscene=ch4.obj_scene_ch4p2a()
        elif bookmarkname == 'ch4_startstory' :
            bookmarkscene=ch4.obj_scene_ch4p3()
        elif bookmarkname == 'ch4_checkmail' :
            bookmarkscene=ch4.obj_scene_ch4p6()
        elif bookmarkname == 'ch4_drawcave' :
            bookmarkscene=ch4.obj_scene_ch4p9()
        elif bookmarkname == 'ch4_writebunny' :
            bookmarkscene=ch4.obj_scene_ch4p11()
        elif bookmarkname == 'ch4_startlying' :
            bookmarkscene=ch4.obj_scene_lyingstart()
        elif bookmarkname == 'ch4_winlying1' :
            bookmarkscene=ch4.obj_scene_lyingpart1win()
        elif bookmarkname == 'ch4_winlying2' :
            bookmarkscene=ch4.obj_scene_lyingpart2win()
        elif bookmarkname == 'ch4_winlying3' :
            bookmarkscene=ch4.obj_scene_lyingend()
        elif bookmarkname == 'ch4_gohome' :
            bookmarkscene=ch4.obj_scene_ch4p20()
        elif bookmarkname == 'ch4_endunlock':
            bookmarkscene=ch4.obj_scene_ch4unlocknext()
        #
        # ch5
        elif bookmarkname == 'ch5_start':
            bookmarkscene=ch5.obj_scene_chapter5()
        elif bookmarkname == 'ch5_startstory':
            bookmarkscene=ch5.obj_scene_ch5p3()
        elif bookmarkname == 'ch5_checkmail':
            bookmarkscene=ch5.obj_scene_ch5p6()
        elif bookmarkname == 'ch5_drawcloud':
            bookmarkscene=ch5.obj_scene_ch5p9()
        elif bookmarkname == 'ch5_climb':
            bookmarkscene=ch5.obj_scene_ch5p11()
        elif bookmarkname == 'ch5_writeelder' :
            bookmarkscene=ch5.obj_scene_ch5p14()
        elif bookmarkname == 'ch5_drawrock' :
            bookmarkscene=ch5.obj_scene_ch5p21()
        elif bookmarkname == 'ch5_rps1' :
            bookmarkscene=ch5.obj_scene_ch5p22()
        elif bookmarkname == 'ch5_lostrps1' :
            bookmarkscene=ch5.obj_scene_ch5p25()
        elif bookmarkname == 'ch5_lostrps2' :
            bookmarkscene=ch5.obj_scene_ch5p27()
        elif bookmarkname == 'ch5_strongwilled' :
            bookmarkscene=ch5.obj_scene_ch5p28()
        elif bookmarkname == 'ch5_eldercheatsecret' :
            bookmarkscene=ch5.obj_scene_ch5p32()
        elif bookmarkname == 'ch5_rps3' :
            bookmarkscene=ch5.obj_scene_ch5p35a()
        elif bookmarkname == 'ch5_winrps3' :
            bookmarkscene=ch5.obj_scene_ch5p37()
        elif bookmarkname == 'ch5_gohome' :
            bookmarkscene=ch5.obj_scene_ch5p38()
        elif bookmarkname == 'ch5_endunlock':
            bookmarkscene=ch5.obj_scene_ch5unlocknext()
        #
        # ch6
        elif bookmarkname == 'ch6_start':
            bookmarkscene=ch6.obj_scene_chapter6()
        elif bookmarkname == 'ch6_startstory':
            bookmarkscene=ch6.obj_scene_ch6p3()
        elif bookmarkname == 'ch6_checkmail':
            bookmarkscene=ch6.obj_scene_ch6p6()
        elif bookmarkname == 'ch6_drawwave':
            bookmarkscene=ch6.obj_scene_ch6p11()
        elif bookmarkname == 'ch6_writesailor':
            bookmarkscene=ch6.obj_scene_ch6p13()
        elif bookmarkname == 'ch6_getlogs':
            bookmarkscene=ch6.obj_scene_ch6p20()
        elif bookmarkname == 'ch6_drawship':
            bookmarkscene=ch6.obj_scene_ch6p22()
        elif bookmarkname == 'ch6_drawskull':
            bookmarkscene=ch6.obj_scene_ch6p24()
        elif bookmarkname == 'ch6_startskullisland':
            bookmarkscene=ch6.obj_scene_ch6p27()
        elif bookmarkname == 'ch6_startsneak':
            bookmarkscene=ch6.obj_scene_ch6p29()
        elif bookmarkname == 'ch6_sneak1':
            bookmarkscene=ch6.obj_scene_ch6p30a()
        elif bookmarkname == 'ch6_sneak2':
            bookmarkscene=ch6.obj_scene_ch6p31()
        elif bookmarkname == 'ch6_sneak3':
            bookmarkscene=ch6.obj_scene_ch6p32()
        elif bookmarkname == 'ch6_sneak4':
            bookmarkscene=ch6.obj_scene_ch6p33()
        elif bookmarkname == 'ch6_drawcow':
            bookmarkscene=ch6.obj_scene_ch6p34()
        elif bookmarkname == 'ch6_startride':
            bookmarkscene=ch6.obj_scene_ch6p38()
        elif bookmarkname == 'ch6_winride':
            bookmarkscene=ch6.obj_scene_ch6p40()
        elif bookmarkname == 'ch6_byesailor':
            bookmarkscene=ch6.obj_scene_ch6p42()
        elif bookmarkname == 'ch6_gohome':
            bookmarkscene=ch6.obj_scene_ch6p46()
        elif bookmarkname == 'ch6_endunlock':
            bookmarkscene=ch6.obj_scene_ch6unlocknext()
        #
        # ch7
        elif bookmarkname == 'ch7_start':
            bookmarkscene=ch7.obj_scene_chapter7()
        elif bookmarkname == 'ch7_startstory':
            bookmarkscene=ch7.obj_scene_ch7p2()
        elif bookmarkname == 'ch7_checkmail':
            bookmarkscene=ch7.obj_scene_ch7p5()
        elif bookmarkname == 'ch7_gotocastle':
            bookmarkscene=ch7.obj_scene_ch7p10()
        elif bookmarkname == 'ch7_putpassword1':
            bookmarkscene=ch7.obj_scene_ch7p13()
        elif bookmarkname == 'ch7_putpassword2':
            bookmarkscene=ch7.obj_scene_ch7p19()
        elif bookmarkname == 'ch7_startdodge':
            bookmarkscene=ch7.obj_scene_ch7p21a()
        elif bookmarkname == 'ch7_windodge':
            bookmarkscene=ch7.obj_scene_ch7p23()
        elif bookmarkname == 'ch7_winstomp':
            bookmarkscene=ch7.obj_scene_ch7p26()
        elif bookmarkname == 'ch7_gohome':
            bookmarkscene=ch7.obj_scene_ch7p30()
        elif bookmarkname == 'ch7_villainagain':
            bookmarkscene=ch7.obj_scene_ch7p40()
        elif bookmarkname == 'ch7_startmech':
            bookmarkscene=ch7.obj_scene_ch7p48()
        elif bookmarkname == 'ch7_winmech':
            bookmarkscene=ch7.obj_scene_ch7p50()
        elif bookmarkname == 'ch7_drawcake':
            bookmarkscene=ch7.obj_scene_ch7p53()
        elif bookmarkname == 'ch7_endunlock':
            bookmarkscene=ch7.obj_scene_ch7unlocknext()
        #
        # ch8
        elif bookmarkname == 'ch8_start':
            bookmarkscene=ch8.obj_scene_chapter8()

        # no bookmark found
        else:
            bookmarkscene=None

        #
        # go to bookmarked scene
        if bookmarkscene:
            share.scenemanager.switchscene(bookmarkscene)

##########################################################
##########################################################




##########################################################
##########################################################

# Reference to titlescreen
class obj_scene_titlescreen(page.obj_page):
    def update(self,controls):
        # reloads main menu every time
        share.scenemanager.switchscene(obj_scene_realtitlescreen())


# Main Menu
class obj_scene_realtitlescreen(page.obj_page):
    def setup(self):
        share.display.reseticon()# window icon
        #
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        #
        # decorations
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('V1.0',(1210,670),fontsize='smaller')
        self.sprite_pen=draw.obj_image('pen',(70,620), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1280-70,620), scale=0.25)
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_author.show=self.hasbook
        self.sprite_book.show=self.hasbook
        self.sprite_pen.show=self.hasbook
        self.sprite_eraser.show=self.hasbook
        # menu
        xref=640
        yref=380
        dyref=80
        fontref='larger'
        if not self.hasbook:
            self.sprite_continue=draw.obj_textbox('start new book',(xref,yref),fontsize=fontref,xleft=False,hover=True)
            self.sprite_settings=draw.obj_textbox('settings',(xref,yref+dyref),fontsize=fontref,xleft=False,hover=True)
            self.sprite_exit=draw.obj_textbox('exit',(xref,yref+2*dyref),fontsize=fontref,xleft=False,hover=True)
        else:
            self.sprite_continue=draw.obj_textbox('continue book',(xref,yref),fontsize=fontref,xleft=False,hover=True)
            self.sprite_chapters=draw.obj_textbox('chapters',(xref,yref+dyref),fontsize=fontref,xleft=False,hover=True)
            self.sprite_settings=draw.obj_textbox('settings',(xref,yref+2*dyref),fontsize=fontref,xleft=False,hover=True)
            self.sprite_exit=draw.obj_textbox('exit',(xref,yref+3*dyref),fontsize=fontref,xleft=False,hover=True)
        self.addpart(self.sprite_continue)
        self.addpart(self.sprite_chapters)
        self.addpart(self.sprite_settings)
        self.addpart(self.sprite_exit)
        self.sprite_continue.show=True
        self.sprite_chapters.show=self.hasbook
        self.sprite_settings.show=True
        self.sprite_exit.show=True
        #
        # audio
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
            self.addpart( draw.obj_music('tension') )
        # devtools
        if share.devaccess:
            tempo1= '['+share.datamanager.controlname('dev')+': toggle dev mode] '
            tempo2= '['+share.datamanager.controlname('right')+': appendix of tests] '
            tempo3= '['+share.datamanager.controlname('left')+': quick access scene] '
            textmat=['Developper Access is on:','(edit settings.txt to change)',tempo1,tempo2,tempo3]
            x1,y1,dy1=30,300,30
            for i in textmat:
                self.addpart(draw.obj_textbox(i,(x1,y1),fontsize='smaller',xleft=True,color=share.colors.instructions))
                y1 += dy1
        # devtools: quick scene
        self.gotoquickscene=obj_quickscene()
        self.gotobookmarkscene=obj_gotobookmark()

    def page(self,controls):
        #
        # Hovering
        if not self.hasbook:
            if self.sprite_continue.isclicked(controls):
                share.scenemanager.switchscene(ch0.obj_scene_prologue())
            elif self.sprite_settings.isclicked(controls):
                share.scenemanager.switchscene(obj_scene_settings())
            elif self.sprite_exit.isclicked(controls):
                share.quitgame()
        else:
            if self.sprite_continue.isclicked(controls):
                self.gotobookmarkscene()
            elif self.sprite_chapters.isclicked(controls):
                share.scenemanager.switchscene(obj_scene_chaptersscreen())# chapters
            elif self.sprite_settings.isclicked(controls):
                share.scenemanager.switchscene(obj_scene_settings())
            elif self.sprite_exit.isclicked(controls):
                share.quitgame()
        #
        if controls.gq and controls.gqc:
            share.quitgame()
        #############################################3
        if share.devaccess:
            if controls.gr and controls.grc:
                share.scenemanager.switchscene(tests.obj_scene_testmenu())
            if controls.gl and controls.glc:
                self.gotoquickscene()
        #############################################3



####################################################################################################################
####################################################################################################################

# Chapters screen
class obj_scene_chaptersscreen(page.obj_page):
    def setup(self):
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        # decorations
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('V1.0',(1210,670),fontsize='smaller')
        self.sprite_pen=draw.obj_image('pen',(70,620), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_author.show=self.hasbook
        self.sprite_book.show=self.hasbook
        self.sprite_pen.show=self.hasbook
        self.sprite_eraser.show=self.hasbook
        # menu
        self.sprite_back=draw.obj_textbox('back',(420,370),fontsize='larger',hover=True)
        self.addpart(self.sprite_back)
        xref=540
        yref=360
        dyref=40
        fontref='smaller'
        self.sprite_prologue=draw.obj_textbox('Prologue: The Book of Things',(xref,yref),fontsize=fontref,xleft=True, hover=True)
        self.addpart(self.sprite_prologue)
        if self.maxchapter>0:
            self.sprite_ch1=draw.obj_textbox('Chapter I: The Hero',(xref,yref+dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch1)
        if self.maxchapter>1:
            self.sprite_ch2=draw.obj_textbox('Chapter II: Home Sweet Home',(xref,yref+2*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch2)
        if self.maxchapter>2:
            self.sprite_ch3=draw.obj_textbox('Chapter III: Where are you',(xref,yref+3*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch3)
        if self.maxchapter>3:
            self.sprite_ch4=draw.obj_textbox('Chapter IV Something East',(xref,yref+4*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch4)
        if self.maxchapter>4:
            self.sprite_ch5=draw.obj_textbox('Chapter V: Higher and Higher',(xref,yref+5*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch5)
        if self.maxchapter>5:
            self.sprite_ch6=draw.obj_textbox('Chapter VI: Treasure Hunt',(xref,yref+6*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch6)
        if self.maxchapter>6:
            self.sprite_ch7=draw.obj_textbox('Chapter VII: Showtime',(xref,yref+7*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch7)
        if self.maxchapter>7:
            self.sprite_ch8=draw.obj_textbox('Epilogue',(xref,yref+8*dyref),fontsize=fontref,xleft=True, hover=True)
            self.addpart(self.sprite_ch8)
        #
        # audio
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
        #
        # music
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
            self.addpart( draw.obj_music('tension') )

    def page(self,controls):
        # hovers
        if self.sprite_back.isclicked(controls):
            self.sound_menuback.play()
            share.scenemanager.switchscene(share.titlescreen,initstart=True)# go back to menu
        if self.sprite_prologue.isclicked(controls):
            self.sound_menugo.play()
            share.scenemanager.switchscene(ch0.obj_scene_prologue())
        if self.maxchapter>0:
            if self.sprite_ch1.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch1.obj_scene_chapter1())
        if self.maxchapter>1:
            if self.sprite_ch2.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch2.obj_scene_chapter2())
        if self.maxchapter>2:
            if self.sprite_ch3.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch3.obj_scene_chapter3())
        if self.maxchapter>3:
            if self.sprite_ch4.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch4.obj_scene_chapter4())
        if self.maxchapter>4:
            if self.sprite_ch5.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch5.obj_scene_chapter5())
        if self.maxchapter>5:
            if self.sprite_ch6.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch6.obj_scene_chapter6())
        if self.maxchapter>6:
            if self.sprite_ch7.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch7.obj_scene_chapter7())
        if self.maxchapter>7:
            if self.sprite_ch8.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch8.obj_scene_chapter8())


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
        #
        ######################
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        # decorations
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.sprite_author=draw.obj_textbox('V1.0',(1210,670),fontsize='smaller')
        self.sprite_pen=draw.obj_image('pen',(70,620), scale=0.25)
        self.sprite_book=draw.obj_image('book',(640,230), scale=0.5)
        self.sprite_eraser=draw.obj_image('eraser',(1210,620), scale=0.25)
        self.addpart(self.sprite_author)
        self.addpart(self.sprite_pen)
        self.addpart(self.sprite_book)
        self.addpart(self.sprite_eraser)
        self.sprite_pen.replaceimage('pen')
        self.sprite_book.replaceimage('book')
        self.sprite_eraser.replaceimage('eraser')
        self.sprite_author.show=self.hasbook
        self.sprite_book.show=self.hasbook
        self.sprite_pen.show=self.hasbook
        self.sprite_eraser.show=self.hasbook

        #
        # menu
        self.sprite_back=draw.obj_textbox('back',(420,370),fontsize='larger',hover=True)
        self.addpart(self.sprite_back)
        xref=540
        yref=360
        dyref=40
        fontref='smaller'
        #
        self.sprite_keyboard=draw.obj_textbox('xxx',(xref,yref+0*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart(self.sprite_keyboard)
        if share.datamanager.doazerty:
            self.sprite_keyboard.replacetext('Keyboard: Azerty (arrows = ZQSD)')
        else:
            self.sprite_keyboard.replacetext('Keyboard: Qwerty (arrows = WASD)')
        #
        self.sprite_display=draw.obj_textbox('xxx',(xref,yref+1*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart(self.sprite_display)
        if share.datamanager.donative:
            self.sprite_display.replacetext('Display: Windowed (1280x720)')
        else:
            self.sprite_display.replacetext('Display: Fullscreen')
        #
        self.sprite_music=draw.obj_textbox('xxx',(xref,yref+2*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart(self.sprite_music)
        if share.datamanager.domusic:
            self.sprite_music.replacetext('Music: On')
        else:
            self.sprite_music.replacetext('Music: Off')
        #
        self.sprite_sound=draw.obj_textbox('xxx',(xref,yref+3*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart(self.sprite_sound)
        if share.datamanager.dosound:
            self.sprite_sound.replacetext('Sound: On')
        else:
            self.sprite_sound.replacetext('Sound: Off')

        self.sprite_controls=draw.obj_textbox('Controls',(xref,yref+4*dyref),fontsize=fontref,xleft=True)
        self.addpart( self.sprite_controls )
        self.sprite_credits=draw.obj_textbox('Credits',(xref,yref+5*dyref),fontsize=fontref,xleft=True)
        self.addpart( self.sprite_credits )
        self.sprite_erasebook=draw.obj_textbox('Erase Book',(xref,yref+6*dyref),fontsize=fontref,xleft=True)
        self.addpart( self.sprite_erasebook )

        #
        # audio
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
        if self.tosoundon:
            self.sound_menuback.play()
        # music
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
            self.addpart( draw.obj_music('tension') )

    def page(self,controls):
        # hovers
        if self.sprite_back.isclicked(controls):
            self.sound_menuback.play()
            share.scenemanager.switchscene(share.titlescreen,initstart=True)# go back to menu
        elif self.sprite_keyboard.isclicked(controls):
            self.sound_menuback.play()
            share.datamanager.doazerty=not share.datamanager.doazerty
            share.controls.azerty=share.datamanager.doazerty# change controls as well
            share.datamanager.savesettings()# save settings
            if share.datamanager.doazerty:
                self.sprite_keyboard.replacetext('Keyboard: Azerty (arrows = ZQSD)')
            else:
                self.sprite_keyboard.replacetext('Keyboard: Qwerty (arrows = WASD)')

        # change display
        elif self.sprite_display.isclicked(controls):
            self.sound_menuback.play()
            share.datamanager.donative= not share.datamanager.donative
            if share.datamanager.donative:
                share.display.reset(native=True)
            else:
                share.display.reset(native=False)
            share.datamanager.savesettings()# save settings
            if share.datamanager.donative:
                self.sprite_display.replacetext('Display: Windowed (1280x720)')
            else:
                self.sprite_display.replacetext('Display: Fullscreen')

        # toggle music
        elif self.sprite_music.isclicked(controls):
            self.sound_menuback.play()
            share.datamanager.domusic=not share.datamanager.domusic
            if share.datamanager.domusic:
                share.musicplayer.setmastervolume(1)
            else:
                share.musicplayer.setmastervolume(0)
            share.datamanager.savesettings()# save settings
            if share.datamanager.domusic:
                self.sprite_music.replacetext('Music: On')
            else:
                self.sprite_music.replacetext('Music: Off')

        # toggle sound
        elif self.sprite_sound.isclicked(controls):
            # self.sound_menuback.play()
            share.datamanager.dosound=not share.datamanager.dosound
            if share.datamanager.dosound:
                share.soundplayer.setmastervolume(1)
            else:
                share.soundplayer.setmastervolume(0)
            share.datamanager.savesettings()# save settings
            if share.datamanager.dosound:
                self.sprite_sound.replacetext('Sound: On')
            else:
                self.sprite_sound.replacetext('Sound: Off')
            share.scenemanager.switchscene(obj_scene_settings(tosoundon=True))# reload scene with sound

        # instructions for controls
        elif self.sprite_controls.isclicked(controls):
            self.sound_menugo.play()
            share.scenemanager.switchscene(obj_scene_instructions_controls_screen())
        # read game credits
        elif self.sprite_credits.isclicked(controls):
            self.sound_menugo.play()
            share.scenemanager.switchscene(obj_scene_creditscreen())
        # erase book
        elif self.sprite_erasebook.isclicked(controls):
            self.sound_menugo.play()
            share.scenemanager.switchscene(obj_scene_erasebook())


####################################################################################################################
####################################################################################################################
# Instructions for the Controls
# *CONTROLS

class obj_scene_instructions_controls_screen(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def triggernextpage(self,controls):
        return False
    def setup(self):
        self.text=['Controls: ']
        #
        # Game controls instructions
        self.addpart( draw.obj_image('instructions_controls',(640,420),path='premade') )
        self.addpart( draw.obj_textbox('[left mouse]',(927,311),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[right mouse]',(1136,252),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[space]',(564,533),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[enter]',(732,525),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[wasd]',(430,260),color=share.colors.black) )
        self.addpart( draw.obj_textbox(   'or',(508,267),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[arrows]',(555,320),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[esc]',(153,249),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[tab]',(81,534),color=share.colors.black) )
        #
        self.addpart( draw.obj_textbox('draw',(930,370),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('select',(930,437),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('erase',(1174,305),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('play',(579,260),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('next',(778,580),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('previous',(216,544),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('exit',(136,325),color=share.colors.instructions,fontsize='larger') )
        #
        self.addpart( draw.obj_music('tension') )

####################################################################################################################
####################################################################################################################
# Credits
# *CREDITS

class obj_scene_creditscreen(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def triggernextpage(self,controls):
        return False
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def setup(self):
        credits=share.gamecredits.gettext()# game credits from database
        self.text=[credits,\
                   '['+share.datamanager.controlname('back')+': back]']
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


####################################################################################################################
####################################################################################################################







#
