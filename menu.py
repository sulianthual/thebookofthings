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
            # quickscene=ch0.obj_scene_ch0p12()
            # quickscene=ch1.obj_scene_ch1p12()
            # quickscene=ch1.obj_scene_ch1play3()
            # quickscene=ch2.obj_scene_ch2p6a()
            # quickscene=ch2.obj_scene_ch2play4()
            # quickscene=ch3.obj_scene_ch3p19()
            # quickscene=ch3.obj_scene_ch3p22easteregg()
            # quickscene=ch4.obj_scene_ch4p11()
            # quickscene=ch5.obj_scene_ch5p37()
            # quickscene=ch5.obj_scene_ch5p39()
            # quickscene=ch6.obj_scene_ch6p2()
            # quickscene=ch6.obj_scene_ch6p39()
            # quickscene=ch7.obj_scene_ch7p19()
            # quickscene=ch7.obj_scene_ch7ending()
            # quickscene=ch8.obj_scene_ch8west()
            # quickscene=ch8.obj_scene_ch8roam()
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
            quickscene=ch8.obj_scene_ch8roam()# ch8 travel
            # quickscene=ch8.obj_scene_ch8roam(start='island')
            #
            #
            share.scenemanager.switchscene(quickscene)# (must not initstart if has looped sounds)
        else:
            # test scenes (must initstart because are inventoried)
            # quickscene=tests.obj_scene_testdevnotes()
            # quickscene=tests.obj_scene_testdevnotesfiles()
            # quickscene=tests.obj_scene_testpagebacknext()
            # quickscene=tests.obj_scene_textbox()
            #
            quickscene=tests.obj_scene_testdrafting()
            #
            #
            share.scenemanager.switchscene(quickscene,initstart=True)# (must initstart because are inventoried)



##########################################################
##########################################################
# bookmark: go to last completed scene according to progress
# database of bookmark names and corresponding scenes here

class obj_gotobookmark():
    def __init__(self):
        self.dict={}# dictionary list of bookmarks and associated text
        self.chaptertext=''# associated text depending on chapter
    def __call__(self,chapter=None,launch=True,bookmark=None):
        # bookmark (if none specified we just use a default scene)
        bookmarkname=bookmark
        # if launch=False, we are not accessing scene, just making the dict and chaptertext data
        # bookmarked scene to launch (if none found doesnt launch)
        bookmarkscene=None
        # dictionary of scene comments (to make inventories for browsing without launching)
        self.dict={}
        #####
        if chapter==0:
        #
        # ch0
            self.chaptertext='Prologue: The Book of Things'
            self.dict['ch0_start']='start prologue'
            self.dict['ch0_drawpen']='draw the pen'
            self.dict['ch0_draweraser']='draw the eraser'
            self.dict['ch0_drawbook']='draw the book'
            self.dict['ch0_meetbook']='enter profile name'
            self.dict['ch0_drawpointer']='draw the pointer'
            # self.dict['ch0_endunlock']='Prologue End'
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
            elif bookmarkname == 'ch0_drawpointer':
                bookmarkscene=ch0.obj_scene_ch0p12()
            elif bookmarkname == 'ch0_endunlock':
                bookmarkscene=ch0.obj_scene_ch0unlocknext()
            else:
                bookmarkscene=ch0.obj_scene_prologue()

        elif chapter==1:
            #
            # ch1
            self.chaptertext='Chapter I: The Hero'
            self.dict['ch1_start']='start chapter'
            self.dict['ch1_writehero']='draw and name the hero'
            # self.dict['ch1_drawhero']='draw the hero'
            self.dict['ch1_drawbed']='draw the bed'
            self.dict['ch1_drawfish']='draw the fish and hook'
            # self.dict['ch1_gotfish']='caugth a fish'
            self.dict['ch1_drawsun']='draw the sun and moon'
            self.dict['ch1_startplay']='replay the story'
            # self.dict['ch1_endunlock']='Chapter End'
            if bookmarkname == 'ch1_start':
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
            else:
                bookmarkscene=ch1.obj_scene_chapter1()
        elif chapter==2:
            #
            # ch2
            self.chaptertext='Chapter II: Home Sweet Home'
            self.dict['ch2_start']='start chapter'
            self.dict['ch2_drawlove']='draw the love heart'
            self.dict['ch2_writepartner']='draw and name the partner'
            self.dict['ch2_drawmail']='draw the mailbox and mail letter'
            self.dict['ch2_drawmusic']='draw the saxophone and music notes'
            self.dict['ch2_drawhouse']='draw the house and pond'
            self.dict['ch2_drawbush']='draw the bush and flower'
            self.dict['ch2_startplay']='replay the story'
            # self.dict['ch2_endunlock']='Chapter End'
            if bookmarkname == 'ch2_start':
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
            else:
                bookmarkscene=ch2.obj_scene_chapter2()
        elif chapter==3:
            #
            # ch3
            self.chaptertext='Chapter III: Where are you'
            self.dict['ch3_start']='start chapter'
            self.dict['ch3_writevillain']='draw and name the villain'
            # self.dict['ch3_startstory']='start the day'
            # self.dict['ch3_checkmail']='read the mail'
            self.dict['ch3_drawmountain']='draw the castle and mountain'
            self.dict['ch3_drawgun']='draw the gun and bullet'
            self.dict['ch3_startdodge']='fight the villain'
            self.dict['ch3_windodge']='enter the password'
            self.dict['ch3_gohome']='back at home'
            self.dict['ch3_startbug']='name and draw the bug'
            # self.dict['ch3_endbug']='go to sleep'
            # self.dict['ch3_endunlock']='Chapter End'
            if bookmarkname == 'ch3_start':
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
                bookmarkscene=ch3.obj_scene_ch3p19()
            elif bookmarkname == 'ch3_windodge' :
                bookmarkscene=ch3.obj_scene_ch3p20()
            elif bookmarkname == 'ch3_gohome' :
                bookmarkscene=ch3.obj_scene_ch3p25a()
            elif bookmarkname == 'ch3_startbug' :
                bookmarkscene=ch3.obj_scene_ch3p32()
            elif bookmarkname == 'ch3_endbug' :
                bookmarkscene=ch3.obj_scene_ch3p39a()
            elif bookmarkname == 'ch3_endunlock':
                bookmarkscene=ch3.obj_scene_ch3unlocknext()
            else:
                bookmarkscene=ch3.obj_scene_chapter3()
        elif chapter==4:
            #
            # ch4
            self.chaptertext='Chapter IV Something East'
            self.dict['ch4_start']='start chapter'
            self.dict['ch4_drawalarm']='draw the night stand and alarm clock'
            # self.dict['ch4_startstory']='start the day'
            # self.dict['ch4_checkmail']='read the mail'
            self.dict['ch4_drawcave']='draw the cave and tree'
            self.dict['ch4_writebunny']='draw and name the bunny'
            self.dict['ch4_startlying']='play the lying game'
            # self.dict['ch4_winlying1']='lying game round 2'
            # self.dict['ch4_winlying2']='lying game round 3'
            # self.dict['ch4_winlying3']='back at home'
            self.dict['ch4_gohome']='back at home'
            # self.dict['ch4_endunlock']='Chapter End'
            if bookmarkname == 'ch4_start':
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
            else:
                bookmarkscene=ch4.obj_scene_chapter4()
        elif chapter==5:
            #
            # ch5
            self.chaptertext='Chapter V: Higher and Higher'
            self.dict['ch5_start']='start chapter'
            # self.dict['ch5_startstory']='start the day'
            # self.dict['ch5_checkmail']='read the mail'
            self.dict['ch5_drawcloud']='draw the cloud and lightning bolt'
            # self.dict['ch5_climb']='climb the peak'
            self.dict['ch5_writeelder']='draw and name the elder'
            self.dict['ch5_drawrock']='draw rock paper scissors'
            # self.dict['ch5_rps1']='learn rock paper scissors'
            # self.dict['ch5_lostrps1']='loose'
            # self.dict['ch5_lostrps2']='loose again'
            # self.dict['ch5_strongwilled']='what a strong willed character'
            # self.dict['ch5_eldercheatsecret']='how to cheat'
            self.dict['ch5_rps3']='play rock paper scissors'
            # self.dict['ch5_winrps3']='win rock paper scissors'
            self.dict['ch5_gohome']='back at home'
            # self.dict['ch5_endunlock']='Chapter End'
            if bookmarkname == 'ch5_start':
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
                bookmarkscene=ch5.obj_scene_ch5p36()
            elif bookmarkname == 'ch5_winrps3' :
                bookmarkscene=ch5.obj_scene_ch5p37()
            elif bookmarkname == 'ch5_gohome' :
                bookmarkscene=ch5.obj_scene_ch5p38()
            elif bookmarkname == 'ch5_endunlock':
                bookmarkscene=ch5.obj_scene_ch5unlocknext()
            else:
                bookmarkscene=ch5.obj_scene_chapter5()
        elif chapter==6:
            #
            # ch6
            self.chaptertext='Chapter VI: Treasure Hunt'
            self.dict['ch6_start']='start chapter'
            # self.dict['ch6_startstory']='start the day'
            # self.dict['ch6_checkmail']='read the mail'
            self.dict['ch6_drawwave']='draw the palm tree and wave'
            self.dict['ch6_writesailor']='draw and name the sailor'
            # self.dict['ch6_getlogs']='get some wood'
            self.dict['ch6_drawship']='draw the ship and skeletons'
            # self.dict['ch6_drawskull']='draw the skeletons'
            # self.dict['ch6_startskullisland']='arrive at skull island'
            self.dict['ch6_startsneak']='play the sneaking game'
            # self.dict['ch6_sneak1']='sneak game round 1'
            # self.dict['ch6_sneak2']='sneak game round 2'
            # self.dict['ch6_sneak3']='sneak game round 3'
            # self.dict['ch6_sneak4']='sneak game round 4'
            self.dict['ch6_drawcow']='draw treasure'
            self.dict['ch6_startride']='ride treasure'
            # self.dict['ch6_winride']='made it to the ship'
            # self.dict['ch6_byesailor']='bye bye sailor'
            self.dict['ch6_gohome']='back at home'
            # self.dict['ch6_endunlock']='Chapter End'
            if bookmarkname == 'ch6_start':
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
                bookmarkscene=ch6.obj_scene_ch6p39()
            elif bookmarkname == 'ch6_winride':
                bookmarkscene=ch6.obj_scene_ch6p40()
            elif bookmarkname == 'ch6_byesailor':
                bookmarkscene=ch6.obj_scene_ch6p42()
            elif bookmarkname == 'ch6_gohome':
                bookmarkscene=ch6.obj_scene_ch6p46()
            elif bookmarkname == 'ch6_endunlock':
                bookmarkscene=ch6.obj_scene_ch6unlocknext()
            else:
                bookmarkscene=ch6.obj_scene_chapter6()
        elif chapter==7:
            #
            # ch7
            self.chaptertext='Chapter VII: Showtime'
            self.dict['ch7_start']='start chapter'
            # self.dict['ch7_startstory']='start the day'
            # self.dict['ch7_checkmail']='read the mail'
            # self.dict['ch7_gotocastle']='go the the castle'
            self.dict['ch7_putpassword1']='enter the password'
            # self.dict['ch7_putpassword2']='enter the correct password'
            self.dict['ch7_startdodge']='fight the villain (guns)'
            self.dict['ch7_startstomp']='fight the villain (kicks)'
            # self.dict['ch7_winstomp']='victory'
            self.dict['ch7_gohome']='back at home'
            # self.dict['ch7_villainagain']='the villain is back'
            self.dict['ch7_startmech']='super-mech-fight'
            # self.dict['ch7_winmech']='victory again'
            self.dict['ch7_drawcake']='draw the cake'
            # self.dict['ch7_endunlock']='Chapter End'
            if bookmarkname == 'ch7_start':
                bookmarkscene=ch7.obj_scene_chapter7()
            elif bookmarkname == 'ch7_startstory':
                bookmarkscene=ch7.obj_scene_ch7p2()
            elif bookmarkname == 'ch7_checkmail':
                bookmarkscene=ch7.obj_scene_ch7p5()
            elif bookmarkname == 'ch7_gotocastle':
                bookmarkscene=ch7.obj_scene_ch7p10()
            elif bookmarkname == 'ch7_putpassword1':
                bookmarkscene=ch7.obj_scene_ch7p11()
            elif bookmarkname == 'ch7_putpassword2':
                bookmarkscene=ch7.obj_scene_ch7p19()
            elif bookmarkname == 'ch7_startdodge':
                bookmarkscene=ch7.obj_scene_ch7p22()
            elif bookmarkname == 'ch7_startstomp':
                bookmarkscene=ch7.obj_scene_ch7p25()
            elif bookmarkname == 'ch7_winstomp':
                bookmarkscene=ch7.obj_scene_ch7p26()
            elif bookmarkname == 'ch7_gohome':
                bookmarkscene=ch7.obj_scene_ch7p30()
            elif bookmarkname == 'ch7_villainagain':
                bookmarkscene=ch7.obj_scene_ch7p40()
            elif bookmarkname == 'ch7_startmech':
                bookmarkscene=ch7.obj_scene_ch7p49()
            elif bookmarkname == 'ch7_winmech':
                bookmarkscene=ch7.obj_scene_ch7p50()
            elif bookmarkname == 'ch7_drawcake':
                bookmarkscene=ch7.obj_scene_ch7p53()
            elif bookmarkname == 'ch7_endunlock':
                bookmarkscene=ch7.obj_scene_ch7unlocknext()
            else:
                bookmarkscene=ch7.obj_scene_chapter7()
        elif chapter==8:
            #
            # ch8
            self.chaptertext='Epilogue'
            self.dict['ch8_start']='start epilogue'
            if bookmarkname == 'ch8_start':
                bookmarkscene=ch8.obj_scene_chapter8()
            else:
                bookmarkscene=ch8.obj_scene_chapter8()
        #
        # go to bookmarked scene
        if bookmarkscene and launch:
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
    def makedecorations(self):
        #
        # choose a random decoration
        decooptions=[]
        if self.maxchapter>0:
            decooptions.append('book')
        if self.maxchapter>1:
            decooptions.append('hero')
            decooptions.append('hero2')
            decooptions.append('fish')
        if self.maxchapter>2:
            decooptions.append('partner')
            decooptions.append('house')
        if self.maxchapter>3:
            decooptions.append('villain')
            decooptions.append('villain2')
            decooptions.append('castle')
            decooptions.append('bug')
        if self.maxchapter>4:
            decooptions.append('bunny')
            decooptions.append('bunny2')
            decooptions.append('bedroom')
        if self.maxchapter>5:
            decooptions.append('elder')
            decooptions.append('elder2')
        if self.maxchapter>6:
            decooptions.append('sailor')
            decooptions.append('sailor2')
            decooptions.append('cow')
            decooptions.append('ship')
            decooptions.append('skeletons')
        if self.maxchapter>7:
            decooptions.append('mechs')
            decooptions.append('cake')
        #
        if decooptions:
            decochoice=tool.randchoice(decooptions)
        else:
            decochoice=None
        # decochoice='house'
        #
        if decochoice=='book':
            self.addpart( draw.obj_image('book',(253,496),scale=0.7,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('eraser',(971,519),scale=0.54,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('pen',(1131,460),scale=0.69,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='hero':
            self.addpart( draw.obj_image('herobasefish',(387,497),scale=0.82,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('sun',(1076,195),scale=0.48,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='hero2':
            self.addpart( draw.obj_image('herobase',(372,382),scale=0.63,rotate=140,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bed',(1058,237),scale=0.62,rotate=-44,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('fish',(802,449),scale=0.41,rotate=-230,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('moon',(147,587),scale=0.62,rotate=-328,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('sun',(808,224),scale=0.42,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='fish':
            self.addpart( draw.obj_image('fish',(980,437),scale=0.89,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('hook',(201,106),scale=0.73,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='partner':
            self.addpart( draw.obj_image('partnerbase',(1088,451),scale=0.68,rotate=-22,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('herobase',(887,459),scale=0.68,rotate=-30,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('love',(986,190),scale=0.41,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='house':
            self.addpart( draw.obj_image('house',(640,453),scale=0.51,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mailbox',(827,360),scale=0.25,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('pond',(272,260),scale=0.49,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bush',(122,338),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bush',(472,223),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bush',(155,96),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('flower',(981,588),scale=0.3,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('flower',(1090,567),scale=0.3,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('flower',(926,515),scale=0.3,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('flower',(1056,477),scale=0.3,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('flower',(1165,492),scale=0.3,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='villain':
            self.addpart( draw.obj_image('villainbase',(1036,447),scale=0.56,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('gun',(897,445),scale=0.23,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bullet',(740,431),scale=0.23,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('castle',(1083,146),scale=0.38,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1208,109),scale=0.32,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1189,272),scale=0.39,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(972,209),scale=0.33,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('herobase',(214,472),scale=0.59,rotate=2,fliph=False,flipv=False) )
        elif decochoice=='villain2':
            self.addpart( draw.obj_image('love',(447,240),scale=0.48,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('villainbase',(253,660),scale=1.62,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('flower',(1017,489),scale=1.01,rotate=22,fliph=False,flipv=False) )
        elif decochoice=='castle':
            self.addpart( draw.obj_image('castle',(955,414),scale=1.33,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('mountain',(610,473),scale=0.49,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(432,498),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1190,623),scale=0.45,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1224,465),scale=0.26,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('sun',(1065,88),scale=0.34,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('herobase',(105,564),scale=0.33,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bug',(232,659),scale=0.25,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='bug':
            self.addpart( draw.obj_image('saxophone',(188,511),scale=1,rotate=26,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('musicnote',(491,477),scale=0.63,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('musicnote',(747,362),scale=0.36,rotate=0,fliph=False,flipv=True) )
            self.addpart( draw.obj_image('musicnote',(346,232),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bug',(1009,302),scale=0.76,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='bunny':
            self.addpart( draw.obj_image('bunnybase',(278,434),scale=0.56,rotate=4,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cave',(188,183),scale=0.41,rotate=4,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('tree',(80,340),scale=0.53,rotate=4,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('tree',(306,224),scale=0.32,rotate=4,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('tree',(59,154),scale=0.3,rotate=4,fliph=False,flipv=False) )
        elif decochoice=='bedroom':
            self.addpart( draw.obj_image('nightstand',(129,580),scale=0.63,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('alarmclock8am',(132,378),scale=0.44,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bed',(553,558),scale=0.75,rotate=0,fliph=False,flipv=False) )
            # self.addpart( draw.obj_image('bug',(1075,604),scale=0.54,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('moon',(272,89),scale=0.54,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='bunny2':
            self.addpart( draw.obj_image('bunnyhead',(973,588),scale=0.77,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='elder':
            self.addpart( draw.obj_image('elderbase',(196,475),scale=0.62,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1084,260),scale=0.62,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cloud',(927,201),scale=0.35,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('lightningbolt',(1121,58),scale=0.35,rotate=-186,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('lightningbolt',(1194,112),scale=0.24,rotate=-218,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('lightningbolt',(995,90),scale=0.24,rotate=-210,fliph=True,flipv=False) )
        elif decochoice=='elder2':
            self.addpart( draw.obj_image('elderbase',(722,717),scale=1.46,rotate=-118,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('lightningbolt',(185,445),scale=0.74,rotate=-88,fliph=False,flipv=False) )
        elif decochoice=='sailor':
            self.addpart( draw.obj_image('herobase',(351,666),scale=0.77,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('sailorbase',(111,631),scale=0.77,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('skeletonbase',(962,326),scale=0.39,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('skeletonbase_sailorhat',(1120,341),scale=0.4,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('palmtree',(431,309),scale=0.7,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bush',(625,499),scale=0.59,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bush',(814,599),scale=0.47,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('sailboat',(139,237),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(214,330),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(74,354),scale=0.36,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('moon',(294,79),scale=0.43,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='sailor2':
            self.addpart( draw.obj_image('cow',(350,513),scale=0.81,rotate=12,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('herobase',(250,316),scale=0.48,rotate=-4,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('sailorbase',(88,273),scale=0.48,rotate=24,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bush',(750,446),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('bush',(1093,626),scale=0.43,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('rock',(971,296),scale=0.35,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('palmtree',(1150,97),scale=0.52,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='cow':
            self.addpart( draw.obj_image('cow',(301,526),scale=0.93,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('palmtree',(1098,303),scale=0.68,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('palmtree',(892,272),scale=0.5,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bush',(763,478),scale=0.5,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('bush',(635,610),scale=0.4,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('moon',(1104,69),scale=0.44,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='ship':
            self.addpart( draw.obj_image('sailboat',(337,455),scale=0.73,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(65,596),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(503,650),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(616,569),scale=0.49,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(886,624),scale=0.53,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('wave',(1077,575),scale=0.41,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cloud',(944,334),scale=0.5,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cloud',(82,246),scale=0.39,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('cloud',(1177,461),scale=0.36,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('sun',(1098,130),scale=0.4,rotate=0,fliph=False,flipv=False) )
        elif decochoice=='skeletons':
            self.addpart( draw.obj_image('skeletonbase',(244,509),scale=0.57,rotate=22,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('skeletonbase_sailorhat',(496,499),scale=0.57,rotate=22,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('skeletonbase',(782,491),scale=0.57,rotate=22,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('skeletonbase_partnerhair',(1075,489),scale=0.57,rotate=22,fliph=False,flipv=False) )
        elif decochoice=='mechs':
            self.addpart( draw.obj_image('heromechpunch',(341,417),scale=0.76,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('villainmechbase',(955,415),scale=0.76,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('mountain',(1212,602),scale=0.32,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('moon',(130,85),scale=0.39,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cloud',(1202,281),scale=0.3,rotate=0,fliph=True,flipv=False) )
            self.addpart( draw.obj_image('cloud',(838,209),scale=0.3,rotate=0,fliph=False,flipv=False) )
            self.addpart( draw.obj_image('cloud',(1034,164),scale=0.3,rotate=0,fliph=True,flipv=False) )
        elif decochoice=='cake':
            self.addpart( draw.obj_image('cake',(640,525),scale=0.66,rotate=0,fliph=False,flipv=False) )



        else:
            pass# dont draw anything


    def setup(self):
        #
        # current progress
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        # decorations (dependent on progress)
        self.makedecorations()
        share.display.reseticon()# window icon
        #
        # Main
        self.textboxtitle=draw.obj_textbox('The Book of Things',(640,80),fontsize='big',hover=self.hasbook,hovercolor=(0,0,0))
        self.addpart(self.textboxtitle)
        #
        # menu
        xref=640
        yref=200#+100
        dyref=55
        xleftref=False
        fontref='small'
        if not self.hasbook:
            self.sprite_continue=draw.obj_textbox('start new book',(xref,yref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_settings=draw.obj_textbox('settings',(xref,yref+dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_exit=draw.obj_textbox('exit',(xref,yref+2*dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.addpart(self.sprite_continue)
            self.addpart(self.sprite_settings)
            self.addpart(self.sprite_exit)
        else:
            # self.sprite_continue=draw.obj_textbox(playtext,(xref,yref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_chapters=draw.obj_textbox('read',(xref,yref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_settings=draw.obj_textbox('settings',(xref,yref+dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_exit=draw.obj_textbox('exit',(xref,yref+2*dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.addpart(self.sprite_chapters)
            self.addpart(self.sprite_settings)
            self.addpart(self.sprite_exit)
        #
        # audio
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        #
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
            self.addpart( draw.obj_music('tension') )
        # devtools
        if share.devaccess:
            tempo='developper mode is on (edit settings.txt to change) '
            tempo += '[f:quickscene] '
            tempo += '[space/enter:appendix] '
            self.addpart(draw.obj_textbox(tempo,(30,680),fontsize='smaller',xleft=True,color=share.colors.instructions))
            # self.sprite_quick=draw.obj_textbox('quickscene [left]',(xref,yref+3*dyref),fontsize=fontref,color=share.colors.instructions,hover=True)
            # self.addpart(self.sprite_quick)
            # self.sprite_appendix=draw.obj_textbox('appendix [right]',(xref,yref+4*dyref),fontsize=fontref,color=share.colors.instructions,hover=True)
            # self.addpart(self.sprite_appendix)


        # devtools: quick scene
        self.gotoquickscene=obj_quickscene()

    def page(self,controls):
        #
        # Hovering
        if not self.hasbook:
            if self.sprite_continue.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch0.obj_scene_prologue())# directly to start of prologue
            elif self.sprite_settings.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(obj_scene_settings())
            elif self.sprite_exit.isclicked(controls):
                share.quitgame()
        else:
            if self.sprite_chapters.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(obj_scene_chaptersscreen())# chapters
            elif self.sprite_settings.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(obj_scene_settings())
            elif self.sprite_exit.isclicked(controls):
                share.quitgame()


            #

        #
        if controls.gq and controls.gqc:
            share.quitgame()
        #
        #############################################3
        # devtools
        if share.devaccess:
            if controls.ga and controls.gac:
                self.sound_menugo.play()
                share.scenemanager.switchscene(tests.obj_scene_testmenu())

            if controls.f and controls.fc:
                self.sound_menugo.play()
                self.gotoquickscene()

            if self.textboxtitle.isclicked(controls):# reload
                share.scenemanager.switchscene(share.titlescreen,initstart=True)
            # self.sprite_appendix.show=share.devmode
            # self.sprite_quick.show=share.devmode




        #############################################3



####################################################################################################################
####################################################################################################################

# Chapters screen
class obj_scene_chaptersscreen(obj_scene_realtitlescreen):
    def setup(self):
        #
        # Main
        self.textboxtitle=draw.obj_textbox('The Book of Things',(640,80),fontsize='big')
        self.addpart(self.textboxtitle)
        # current progress
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        # menu
        xref=480
        yref=200
        dyref=55
        fontref='small'
        self.sprite_back=draw.obj_textbox('[back]',(xref-70,yref),fontsize=fontref,hover=True)
        self.addpart(self.sprite_back)
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
        # access scenes
        self.gotobookmarkscene=obj_gotobookmark()
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
        if True:
            if self.sprite_prologue.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch0.obj_scene_prologue())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=0))
        if self.maxchapter>0:
            if self.sprite_ch1.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch1.obj_scene_chapter1())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=1))
        if self.maxchapter>1:
            if self.sprite_ch2.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch2.obj_scene_chapter2())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=2))
        if self.maxchapter>2:
            if self.sprite_ch3.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch3.obj_scene_chapter3())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=3))
        if self.maxchapter>3:
            if self.sprite_ch4.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch4.obj_scene_chapter4())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=4))
        if self.maxchapter>4:
            if self.sprite_ch5.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch5.obj_scene_chapter5())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=5))
        if self.maxchapter>5:
            if self.sprite_ch6.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch6.obj_scene_chapter6())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=6))
        if self.maxchapter>6:
            if self.sprite_ch7.isclicked(controls):
                self.sound_menugo.play()
                # share.scenemanager.switchscene(ch7.obj_scene_chapter7())
                share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=7))
        if self.maxchapter>7:
            if self.sprite_ch8.isclicked(controls):
                self.sound_menugo.play()
                share.scenemanager.switchscene(ch8.obj_scene_chapter8())# go directly, there is only one bookmark
                # share.scenemanager.switchscene(obj_scene_chapterpartsscreen(chapter=8))


####################################################################################################################
####################################################################################################################
# Show subset of parts of a chapter for access
class obj_scene_chapterpartsscreen(obj_scene_realtitlescreen):
    def setup(self,**kwargs):
        self.tochapter=0# chapter list to show
        # options
        if (kwargs is not None) and ('chapter' in kwargs):
            self.tochapter=kwargs["chapter"]
        #
        # Main
        self.textboxtitle=draw.obj_textbox('The Book of Things',(640,80),fontsize='big')
        self.addpart(self.textboxtitle)
        # current progress
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not

        #
        # get list of subscenes
        self.gotobookmarkscene=obj_gotobookmark()
        self.gotobookmarkscene(self.tochapter,launch=False)# run a bookmarch check on chapter
        self.bookmarkdict=self.gotobookmarkscene.dict# ... and get back the dictionary
        self.bookmarktoptext=self.gotobookmarkscene.chaptertext#...on a header text for corresponding chapter
        #
        self.boomarkdictunlocked={}# now compute subset of bookmarks that are already unlocked
        for c,i in enumerate(self.bookmarkdict.keys()):
            if i in share.datamanager.allbookmarks:
                self.boomarkdictunlocked[i]=self.bookmarkdict[i]
        self.hassinglebookmark=len(self.boomarkdictunlocked.keys())<2# if only one bookmark (or none)
        #
        # menu
        xref=480
        yref=200
        dyref=55
        fontref='small'
        self.sprite_back=draw.obj_textbox('[back]',(xref-70,yref),fontsize=fontref,hover=True)
        self.addpart(self.sprite_back)
        self.addpart( draw.obj_textbox(self.bookmarktoptext,(xref,yref),fontsize=fontref,hover=False,xleft=True) )
        self.textboxclickdict={}
        for c,i in enumerate(self.boomarkdictunlocked.keys()):
            tempo=draw.obj_textbox('... '+self.boomarkdictunlocked[i],(xref,yref+(c+1)*dyref),fontsize=fontref,hover=True,xleft=True)
            self.textboxclickdict[i]=tempo
            self.addpart(tempo)

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
            share.scenemanager.switchscene(obj_scene_chaptersscreen())# back to chapters
        #
        if self.hassinglebookmark:# single bookmark, just go directly to it
            self.gotobookmarkscene(chapter=self.tochapter,bookmark=self.textboxclickdict.keys())
        else:# multiple bookmark, give list
            for i in self.textboxclickdict.keys():
                if self.textboxclickdict[i].isclicked(controls):
                    self.sound_menugo.play()
                    self.gotobookmarkscene(chapter=self.tochapter,bookmark=i)

####################################################################################################################
####################################################################################################################
# Settings Menu
class obj_scene_settings(obj_scene_realtitlescreen):
    def makedecorations(self):
        self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
        self.addpart(draw.obj_textbox('V1.0',(1210,670),fontsize='smaller'))
    def setup(self,**kwargs):
        self.tosoundon=False# start page when turning back sound on
        # options
        if (kwargs is not None) and ('tosoundon' in kwargs):
            self.tosoundon=kwargs["tosoundon"]
        # Default settings
        share.datamanager.loadsettings()# load current settings
        #
        # current progress
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        # decorations (dependent on progress)
        self.makedecorations()
        #
        # menu

        xref=480
        yref=200
        dyref=55
        fontref='small'
        #
        self.sprite_back=draw.obj_textbox('[back]',(xref-70,yref),fontsize=fontref,hover=True)
        self.addpart(self.sprite_back)
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

        self.sprite_controls=draw.obj_textbox('Controls',(xref,yref+4*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart( self.sprite_controls )
        self.sprite_credits=draw.obj_textbox('Credits',(xref,yref+5*dyref),fontsize=fontref,xleft=True,hover=True)
        self.addpart( self.sprite_credits )
        self.sprite_erasebook=draw.obj_textbox('Erase Book',(xref,yref+6*dyref),fontsize=fontref,xleft=True,hover=True)
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
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def setup(self):
        #
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        #

        self.text=['These are the game controls. [tab: back] ']
        #
        # Game controls instructions
        self.addpart( draw.obj_image('instructions_controls_domousebrowse',(640,420),path='premade') )
        self.addpart( draw.obj_textbox('[left mouse]',(927,311),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[right mouse]',(1136,252),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[space]',(564,533),color=share.colors.black) )

        self.addpart( draw.obj_textbox('[wasd]',(430,260),color=share.colors.black) )
        self.addpart( draw.obj_textbox(   'or',(508,267),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[arrows]',(555,320),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[esc]',(153,249),color=share.colors.black) )
        #
        self.addpart( draw.obj_textbox('draw',(930,370),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('select',(930,437),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('erase',(1174,305),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('play',(501,438),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('exit',(136,325),color=share.colors.instructions,fontsize='larger') )

        #
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
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
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def presetup(self):
        super().presetup()
        # self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def setup(self):
        #
        self.maxchapter=share.datamanager.chapter# highest unlocked chapter
        self.hasbook=self.maxchapter>0# there is a started book or not
        #
        credits=share.gamecredits.gettext()# game credits from database
        if not self.domousebrowse:
            credits += '['+share.datamanager.controlname('back')+': back]'
        self.text=[credits]
        #
        self.addpart( draw.obj_music('tension') )
        #
        if self.hasbook:
            self.addpart( draw.obj_music('piano') )
        else:
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
        return controls.gl and controls.gu and controls.gr and controls.gd
    def textboxnextpage(self):
        pass# no textbox for nextpage
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        tempo= 'Press ['+share.datamanager.controlname('left')
        tempo+= '+'+share.datamanager.controlname('up')
        tempo+= '+'+share.datamanager.controlname('right')
        tempo+= '+'+share.datamanager.controlname('down')
        tempo+= '] to erase the book. '
        tempo+= 'You will loose all your drawings and progress. '
        if not self.domousebrowse:
            tempo += '[',share.datamanager.controlname('back'),': back]'
        self.text=[tempo]
        #
        self.addpart( draw.obj_music('tension') )
        #

class obj_scene_erasebookconfirmed(page.obj_chapterpage):
    def nextpage(self):
        pass
    def triggernextpage(self,controls):
        return False
    def textboxnextpage(self):
        pass
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_settings())
    def setup(self):
        tempo = 'The book has vanished... '
        if not self.domousebrowse:
            tempo += '[',share.datamanager.controlname('back'),': back]'

        self.text=[tempo]
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
