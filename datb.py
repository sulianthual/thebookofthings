#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# datb.py: databases and file utilities
#
##########################################################
##########################################################

import core
import tool
import draw

##########################################################
##########################################################

# musics database
# (musics have an indirect name in the code)
class obj_musics:
    def __init__(self):
        self.dict={}
        self.setup()
        #
    def getmusicfilename(self,name):
        if name in self.dict.keys():
          return self.dict[name][0]
        else:
          return self.dict['error'][0]
    def getmusicvolume(self,name):
        if name in self.dict.keys():
          return self.dict[name][1]
        else:
          return self.dict['error'][1]
    def setup(self):
        # dictionary= tuples of filename, volume level
        # Use only ogg files! => Not compiled by pygame/pyinstaller on windows
        # so use only wav files!
        #
        tempo=0.15# reference (0.2 or less)
        # general
        self.dict['error']=( 'general/error.wav' , 1 )# when a music cant be found
        self.dict['tension']=( 'general/whitenoise_ambient.wav' , 0.8 )# tense silence
        self.dict['test']=self.dict['tension']
        # upbeat musics
        # ch0
        self.dict['piano']=( 'ch0/POL-you-and-me-short.wav' , 0.2 )# main theme (soft piano)
        # ch1
        self.dict['hero']=( 'ch1/POL-blob-tales-short.wav' , tempo )# draw the hero (energetic fun)
        # ch2
        self.dict['partner']=( 'ch2/POL-pet-park-short.wav' , tempo )# partner music (cute)
        # ch3
        self.dict['villain']=( 'ch3/POL-spooky-toyland-short.wav' , tempo )# villain music (evil)
        self.dict['gunfight']=( 'ch3/POL-knock-out-short.wav' , tempo )
        self.dict['tower']=( 'ch3/POL-nuts-and-bolts-short.wav' , tempo )# tower music (technologic)
        self.dict['bug']=( 'ch3/POL-bomb-carrier-short.wav' , tempo )# bug (tense)
        # ch4
        self.dict['ch4']=( 'ch4/POL-azure-waters-short.wav' , tempo )# start day (energetic cute)
        self.dict['bunny']=( 'ch4/POL-lone-wolf-short.wav' , tempo )
        self.dict['forest']=( 'ch4/POL-illusion-castle-short.wav' , tempo )
        # ch5
        self.dict['ch5']=( 'ch5/POL-king-of-coins-short.wav' , tempo )# start the day (energetic)
        self.dict['elder']=( 'ch5/POL-find-the-exit-short.wav' , tempo )# elder music (for rps game)
        self.dict['winds']=( 'ch5/wind woosh loop.wav' , 1 )# winds on top of highest peak
        # ch6
        self.dict['ch6']=self.dict['ch5']
        self.dict['sailor']=( 'ch6/POL-jungle-hideout-short.wav' , tempo )# sailor music (jungle jazz)
        self.dict['stealth']=( 'ch6/POL-stealth-mode-short.wav' , tempo )# stealth game (epiiiic)
        self.dict['racing']=( 'ch6/POL-tlalok-temple-short.wav' , tempo )# racing game (energetic)
        # ch7
        self.dict['ch7']=( 'ch7/POL-galactic-trek-short.wav' , tempo )# start the last day (very energetic)
        self.dict['fistfight']=( 'ch7/POL-time-attack-short.wav' , tempo )
        self.dict['mechs']=( 'ch7/POL-underground-army-short.wav' , tempo )# mech transformations (technologic energetic)
        self.dict['mechfight']=self.dict['fistfight']
        self.dict['victory']=( 'ch7/POL-gold-gryphons-short.wav' , tempo )# final victory (epic positive)
        # ch8
        # (reuses all musics)



# sounds database
# (sounds have an indirect name in the code)
class obj_sounds:
    def __init__(self):
        self.dict={}
        self.setup()
    def setup(self):
        # dictionary= tuples of filename, volume level
        # Only ogg (preferred) or wav files!
        #
        # general use
        self.dict['error']=( 'general/error.wav' , 1 )# sound is missing
        self.dict['menugo']=( 'general/drop_001.wav' , 0.5 )# browse menu and pages (forward)
        self.dict['menuback']=( 'general/drop_004.wav' , 0.5 )# browse menu and pages (back)
        self.dict['unlock']=( 'general/Cure.wav' , 1 )# unlock new chapter
        self.dict['erasebook']=( 'general/link (3).wav' , 1 )# erase the book
        self.dict['revealscary']=( 'general/reveal_reversed-suspenseful-harp-3shorter.wav' , 1 )# erase the book
        #
        # draw functions (draw, enter text, etc)
        self.dict['drawstart']=( 'draw/pen1.wav' , 0.2 )# when draws (looped)
        self.dict['drawerase']=( 'draw/bookFlip2a.wav' , 1 )# erase
        self.dict['pen']=( 'draw/pen2.wav' , 1 )# pen character
        self.dict['eraser']=( 'draw/bookFlip2a.wav' , 1 )# eraser character
        self.dict['textchoicego']=( 'draw/bookFlip3a.wav' , 0.5 )# change a textchoice
        self.dict['textinputkeyboard']=( 'draw/click_002.wav' , 1 )# keyboard sound when entering text
        self.dict['textinputedit']=( 'draw/bookFlip3a.wav' , 1 )# when entering edit mode
        self.dict['textinputdone']=( 'draw/maximize_006.wav' , 0.5 )# when exiting edit mode
        #
        ### SPECIFIC TO CHAPTERS/CHARACTERS
        # tests
        self.dict['test1']=( 'tests/phaseJump1.wav' , 1 )
        self.dict['test2']=( 'tests/footstep_grass_001.wav' , 1 )
        self.dict['test3']=( 'tests/troll_01.wav' , 1 )
        self.dict['test4']=( 'tests/desert-ambience.wav' , 1 )# looped
        self.dict['test3a']=( 'tests/male_standard_1.wav' , 0.1 )
        self.dict['test3b']=( 'tests/male_standard_2.wav' , 0.1 )
        self.dict['test3c']=( 'tests/male_standard_3.wav' , 0.1 )
        self.dict['test3d']=( 'tests/male_standard_4.wav' , 0.1 )
        # ch0
        self.dict['bookscene']=( 'book/link (3).wav' , 0.5 )# a scene with the book of things
        self.dict['book2']=( 'book/part (3).wav' , 0.7 )
        self.dict['book1']=( 'book/wall (4).wav' , 1 )
        self.dict['book3']=( 'book/wall (2).wav' , 1 )
        # ch1
        self.dict['hero1']=( 'hero/grunt_male-grunt-disapprove.wav' , 1 )
        self.dict['hero2']=( 'hero/haha01.wav' , 1 )
        self.dict['hero3']=( 'hero/sniff.wav' , 1 )
        self.dict['hero4']=( 'hero/grunt__oh-1.wav' , 1 )
        self.dict['hero5']=( 'hero/haha_laugh1.wav' , 1 )
        self.dict['hero6']=( 'hero/cough_02.wav' , 1 )
        self.dict['hero_what']=( 'hero/whatconfused-what_male.wav' , 1 )# ch7
        # ch2
        self.dict['partner1']=( 'partner/haha-girlp1.wav' , 1 )
        self.dict['partner2']=( 'partner/haha-girlp2.wav' , 1 )
        self.dict['partner3']=( 'partner/giggle_small-giggle.wav' , 1 )
        self.dict['partner_scared']=( 'partner/grunt_female__oh-gah.wav' , 1 )# oh no for any purpose
        # ch3
        self.dict['villain1']=( 'villain/grunt_01.wav' , 1 )
        self.dict['villain2']=( 'villain/haha_evil-laughshort.wav' , 0.5 )
        self.dict['villain3']=( 'villain/grunt_03.wav' , 1 )
        self.dict['villain4']=( 'villain/monster_07.wav' , 1 )
        self.dict['villain_bangdoor']=( 'villain/wood_hit_09.wav' , 1 )# ch7
        self.dict['tower_elec']=( 'tower/paralyzer-discharge-03.wav' , 1 )
        self.dict['tower_hurt']=( 'tower/die_02.wav' , 1 )
        self.dict['tower1']=( 'tower/robot_1.wav' , 0.5 )
        self.dict['tower2']=( 'tower/robot_2.wav' , 0.5 )
        self.dict['tower3']=( 'tower/robot_3.wav' , 0.5 )
        self.dict['tower4']=( 'tower/robot_4.wav' , 0.5 )
        self.dict['tower5']=( 'tower/r2d2.wav' , 1 )
        self.dict['tower6']=( 'tower/robot_classic-computing-sound_short.wav' , 1 )
        # self.dict['bug1']=( 'bug/move.wav' , 1 )
        self.dict['bug1']=( 'bug/misc_menu.wav' , 1 )
        self.dict['bug2']=( 'bug/negative_2.wav' , 1 )
        self.dict['bugitem1']=( 'bug/clean_trumpet.wav' , 1 )
        self.dict['bugitem2']=( 'bug/tadaam.wav' , 0.7 )
        # ch4
        self.dict['bunny1']=( 'bunny/cute_07.wav' , 1 )
        # self.dict['bunny2']=( 'bunny/giggle__dumb-heh.wav' , 1 )# hinhin
        self.dict['bunny2']=( 'bunny/evil_laugh_02.wav' , 1 )# hinhin
        self.dict['bunny3']=( 'bunny/cute_08.wav' , 1 )# oh
        self.dict['bunny4']=( 'bunny/grunt_femalegrunt1.wav' , 1 )# grrr
        self.dict['bunny5']=( 'bunny/Pixie.wav' , 1 )# niaaaah
        self.dict['bunny_hit']=( 'bunny/Punch4.wav' , 1 )
        self.dict['bunny_cave']=( 'bunny/monster-growl_with-reverb.wav' , 1 )
        # ch5
        self.dict['elder1']=( 'elder/grunt_malegrunt1.wav' , 1 )
        self.dict['elder2']=( 'elder/hahaha_elder.wav' , 1 )
        self.dict['elder3']=( 'elder/grunt_malegrunt3.wav' , 1 )
        self.dict['elder4']=( 'elder/haha_evil-man-laughing.wav' , 1 )
        self.dict['elder5']=( 'elder/weird_07.wav' , 1 )
        self.dict['elder6']=( 'elder/grunt_malegrunt2.wav' , 1 )
        # ch6
        self.dict['sailor1']=( 'sailor/humanYell3.wav' , 1 )
        self.dict['sailor2']=( 'sailor/uhuh.wav' , 1 )
        self.dict['sailor3']=( 'sailor/humanYell4.wav' , 1 )
        self.dict['sailor4']=( 'sailor/drunk-hic.wav' , 1 )
        self.dict['sailor5']=( 'sailor/pirate_arrshort2.wav' , 0.5 )
        self.dict['sailor_radio']=( 'sailor/radiocut2.wav' ,1 )

        self.dict['skeleton1']=( 'skeleton/wood_squeak_01.wav' , 0.5 )
        self.dict['skeleton3']=( 'skeleton/wood_squeak_02.wav' , 0.5 )
        self.dict['skeleton2']=( 'skeleton/ghost_SpiritShout.wav' , 0.4 )
        self.dict['skeleton4']=( 'skeleton/ghostshort1.wav' , 0.4 )
        self.dict['skeleton5']=( 'skeleton/ghost_scream1.wav' , 1 )
        self.dict['cow']=( 'cow/cow-mooing-in-south-of-france-limousin-short.wav' , 1 )
        # ch7
        #
        ### SPECIFIC TO MINIGAMES
        # sunrise
        self.dict['sunrise_start']=( 'world/sunrise/1up3.wav' , 1 )
        self.dict['sunrise_end']=( 'world/sunrise/rooster2.wav' , 0.7 )
        # sunset
        self.dict['sunset_start']=( 'world/sunset/Lose4.wav' , 1 )
        self.dict['sunset_end']=( 'world/sunset/howling_shorter.wav' , 2 )
        # wakeup
        self.dict['wakeup_snore1']=( 'world/wakeup/snore.wav' , 1 )
        self.dict['wakeup_snore2']=( 'world/wakeup/snore1.wav' , 1 )
        self.dict['wakeup_wake1']=( 'world/wakeup/scream-6.wav' , 2 )
        self.dict['wakeup_wake2']=( 'world/wakeup/yawn_male-yawnshorter.wav' , 1 )
        self.dict['wakeup_alarm']=( 'world/wakeup/alarm_03.wav' , 0.4 )
        # gotobed
        self.dict['gotobed_start']=( 'world/gotobed/scream-6.wav' , 2 )
        self.dict['gotobed_end']=( 'world/gotobed/snore1.wav' , 1 )
        # fishing
        self.dict['fishing_reel']=( 'world/fish/Fidget_Spinner2.wav' , 1 )
        self.dict['fishing_catch']=( 'world/fish/1up3.wav' , 1 )
        self.dict['fishing_shoot']=( 'world/fish/gun-5.wav' , 0.5 )
        self.dict['fishing_hit']=( 'world/fish/die_02.wav' , 1 )
        self.dict['fishing_throw']=( 'world/fish/swish-9.wav' , 0.5 )
        self.dict['fishing_boomerang']=( 'world/fish/swosh-06.wav' , 2 )#
        self.dict['fishing_lightshoot']=( 'world/fish/lightshoot.wav' , 2 )#
        self.dict['fishing_lighthit']=( 'world/fish/lighthit.wav' , 1 )#
        # eating
        self.dict['eat']=( 'world/eat/eatgulp2.wav' , 1 )
        self.dict['eatend']=( 'world/eat/eat_burp.wav' , 1 )
        self.dict['eatendpowerup']=( 'world/eat/1up3.wav' , 1 )
        # mail
        self.dict['mailjump']=( 'world/mail/woosh-3.wav' , 1 )
        self.dict['mailopen']=( 'world/mail/paper_01.wav' , 1 )
        # serenade
        self.dict['noted']=( 'world/serenade/note_1.wav' , 1 )
        self.dict['notel']=( 'world/serenade/note_3.wav' , 1 )
        self.dict['noter']=( 'world/serenade/note_5.wav' , 1 )
        self.dict['noteu']=( 'world/serenade/note_8.wav' , 1 )
        self.dict['serenade_ambience']=( 'world/serenade/record_player_loop.wav' , 1 )# loop
        self.dict['serenade_cheer']=( 'world/serenade/cheer1.wav' , 0.2 )
        self.dict['serenade_cheeralone']=( 'world/serenade/clapalone1.wav' , 1 )
        # kiss
        self.dict['kiss_start']=( 'world/kiss/scream-6.wav' , 1 )
        self.dict['kiss_kiss']=( 'world/kiss/kiss_cartoon-kiss-cjohnstone.wav' , 1 )
        self.dict['kiss_cheer']=( 'world/kiss/haha-girlp2.wav' , 1 )
        self.dict['kiss_cheer2']=( 'world/kiss/haha01.wav' , 1 )
        self.dict['kiss_ohgah']=( 'world/kiss/grunt_female__oh-gah.wav' , 1 )
        # travel
        self.dict['travel_forest']=( 'world/travel/forest-birds-loop-02.wav' , 1 )
        self.dict['travel_ocean']=( 'world/travel/ocean-waves.wav' , 1 )
        self.dict['travel_winds']=( 'world/travel/wind woosh loop.wav' , 1 )
        self.dict['travel_chop']=( 'world/travel/chop-into-wood-little-debris.wav' , 1 )
        self.dict['travel_choplast']=( 'world/travel/Cure.wav' , 1 )
        self.dict['travel_pickflower']=( 'world/travel/click18.wav' , 1 )
        self.dict['travel_enter']=( 'world/travel/1up3.wav' , 1 )
        # dodgebullets
        self.dict['dodgebullets_start']=( 'world/dodgebullets/fight_lowreverb.wav' , 1 )
        self.dict['dodgebullets_shoot']=( 'world/dodgebullets/gun-5.wav' , 0.5 )
        self.dict['dodgebullets_hit']=( 'world/dodgebullets/die_02.wav' , 1 )
        self.dict['dodgebullets_die']=( 'world/dodgebullets/die_04.wav' , 1 )
        self.dict['dodgebullets_win']=( 'world/dodgebullets/cheer1.wav' , 0.5 )
        self.dict['dodgebullets_jump']=( 'world/dodgebullets/sfx_movement_jump13.wav' , 0.3 )
        self.dict['dodgebullets_crouch']=( 'world/dodgebullets/swish-9.wav' , 0.5 )
        # climb
        self.dict['climb_jump']=( 'world/climb/sfx_movement_jump13.wav' , 0.3 )
        self.dict['climb_fall']=( 'world/climb/fall4.wav' , 1 )
        # rps=rock paper scissors (8 sounds=max?)
        self.dict['rps_select']=( 'world/rps/select.wav' , 1 )
        self.dict['rps_start']=( 'world/rps/fight_lowreverb.wav' , 1 )
        self.dict['rps_count']=( 'world/rps/FX01.wav' , 1 )
        self.dict['rps_hit']=( 'world/rps/die_02.wav' , 1 )
        self.dict['rps_strike']=( 'world/rps/1up3.wav' , 1 )
        self.dict['rps_tie']=( 'world/rps/alert.wav' , 1 )
        self.dict['rps_die']=( 'world/rps/die_04.wav' , 1 )
        self.dict['rps_win']=( 'world/rps/cheer1.wav' , 0.2 )
        # stealth
        self.dict['stealth_jumpinbush']=( 'world/stealth/scream-6.wav' , 0.5 )# cutscene only
        self.dict['stealth_bush1']=( 'world/stealth/rustle13.wav' , 0.5 )
        self.dict['stealth_bush2']=( 'world/stealth/rustle14.wav' , 0.5 )
        self.dict['stealth_bush3']=( 'world/stealth/rustle20.wav' , 0.5 )
        self.dict['stealth_next']=( 'world/stealth/Cure.wav' , 0.5 )
        self.dict['stealth_win']=( 'world/stealth/cheer1.wav' , 0.5 )
        # self.dict['stealth_alarm']=( 'skeleton/ghost_scream1.wav' , 1 )
        self.dict['stealth_alarm']=( 'world/stealth/alarmwtf-02.wav' , 1 )
        # ride cow
        self.dict['ridecow_hit']=( 'world/ridecow/Punch4.wav' , 1 )
        self.dict['ridecow_hitgasp']=( 'world/ridecow/die_02.wav' , 1 )
        # self.dict['ridecow_die']=( 'world/ridecow/die_04.wav' , 1 )
        self.dict['ridecow_die']=( 'world/ridecow/cow-mooing-in-south-of-france-limousin-short.wav' , 1 )
        self.dict['ridecow_win']=( 'world/ridecow/cheer1.wav' , 0.5 )
        self.dict['ridecow_start']=( 'world/ridecow/fight_lowreverb.wav' , 1 )
        # stomp
        self.dict['stomp_jump']=( 'world/stomp/sfx_movement_jump13.wav' , 0.3 )
        self.dict['stomp_hit']=( 'world/stomp/die_02.wav', 1 )
        self.dict['stomp_die']=( 'world/stomp/die_04.wav', 1 )
        self.dict['stomp_strike']=( 'world/stomp/Death1.wav', 0.5 )
        self.dict['stomp_win']=( 'world/stomp/cheer1.wav', 0.5 )
        self.dict['stomp_kick']=( 'world/stomp/swish-9.wav', 1 )
        self.dict['stomp_contact']=( 'world/stomp/Punch4.wav', 1 )
        self.dict['stomp_start']=( 'world/stomp/fight_lowreverb.wav' , 1 )
        # mech
        self.dict['mech_transform1']=( 'world/mech/transformers-sound.wav', 1 )
        self.dict['mech_transform2']=( 'world/mech/transformers-sound_pitch2.wav', 1 )
        self.dict['mech_stomp']=( 'world/mech/stomp_mixedlow.wav', 1 )
        self.dict['mech_start']=( 'world/mech/fight_lowreverb.wav' , 1 )
        self.dict['mech_hit']=( 'world/mech/die_02.wav' , 1 )
        self.dict['mech_strike']=( 'world/mech/Death1.wav', 0.5 )
        self.dict['mech_die']=( 'world/mech/die_04.wav' , 1 )
        self.dict['mech_win']=( 'world/mech/cheer1.wav' , 0.5 )
        self.dict['mech_contact']=( 'world/mech/Punch4.wav', 1 )
        self.dict['mech_counter']=( 'world/mech/Whip.wav', 1 )
        self.dict['mech_correct']=( 'world/mech/confirmation_002.wav', 1 )
        self.dict['mech_wrong']=( 'world/mech/fail.wav', 1 )
        # 3d forest
        self.dict['3dforest_gunreload']=( 'world/3dforest/gunreload.wav' , 0.5 )
        self.dict['3dforest_pickupsax']=( 'world/3dforest/swish-9.wav' , 1 )
        self.dict['3dforest_shoot']=( 'world/3dforest/gun-5.wav' , 0.5 )
        self.dict['3dforest_hit']=( 'world/3dforest/die_02.wav' , 1 )
        self.dict['3dforest_die']=( 'world/3dforest/die_04.wav' , 1 )
        self.dict['3dforest_bunnyhaha']=( 'world/3dforest/giggle__dumb-heh.wav' , 1 )
        # self.dict['3dforest_bunnyhaha']=( 'world/3dforest/evil_laugh_02.wav' , 1 )
        self.dict['3dforest_bunnyscream']=( 'world/3dforest/Pixie.wav' , 1 )
        self.dict['3dforest_bunnydie']=( 'world/3dforest/squish.wav', 0.5 )
        self.dict['3dforest_win']=( 'world/3dforest/cheer1.wav', 0.5 )
        self.dict['3dforest_bunnystrike']=( 'world/3dforest/Punch4.wav', 1 )
        # master rps
        self.dict['master_fail']=( 'world/rpsmaster/fall4.wav' , 1 )
        self.dict['master_fold']=( 'world/rpsmaster/paper_01.wav' , 1 )
        self.dict['master_win']=( 'world/rpsmaster/cheer1.wav' , 0.2 )
        self.dict['master_count']=( 'world/rpsmaster/FX01.wav' , 1 )
        self.dict['master_kick']=( 'world/rpsmaster/swish-9.wav', 1 )

        #
    def getsoundfilename(self,name):
        if name in self.dict.keys():
          return self.dict[name][0]
        else:
          return self.dict['error'][0]
    def getsoundvolume(self,name):
        if name in self.dict.keys():
          return self.dict[name][1]
        else:
          return self.dict['error'][1]


####################################################################################################################
# Credits (text that appears in settings and end-game)

class obj_gamecredits:
    def __init__(self):
        self.setup()
    def setup(self):
        credits ='"The book of things", a video game by Sulian Thual (2021). '
        credits+='Made with Python and Pygame. '
        credits+='All musics from PlayOnLoop.com (Licensed under Creative Commons by Attribution 4.0). '
        credits+='Sounds from opengameart.com and freesound.com (License CC0). '
        credits+='Thank you for playing. '
        self.text=credits
    def gettext(self):
        return self.text


####################################################################################################################
# Databases

# colors database (RGB)
class obj_colors:
    def __init__(self):
        # NB: colorkey is defined in share (as global variable)
        # base colors
        self.purple=(128,0,128)# THIS IS THE TRANSPARENCEY COLOR (colorkey in share.py), DONT USE IT
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.red=(220,0,0)# bit darker
        self.blue=(0,0,220)
        self.lightblue=(100,100,220)
        self.green=(0,220,0)
        self.darkgreen=(0,100,0)
        self.gray=(150,150,150)
        self.darkgray=(100,100,100)
        self.brown=(165,42,42)
        self.maroon=(128,0,0)
        self.darkerpurple=(138,0,138)
        self.pink=(231,84,128)
        self.darkorange=(240,94,35)
        # Colors devmode
        self.devtextbox=(233,222,100)# yellow
        self.devimage=(250,150,0)# orange
        self.devanimation=(0,220,0)# green
        self.devdispgroup=(128,0,128)# purple
        self.devactor=(0,0,220)# blue (hitbox)
        # Colors game elements
        self.background=self.white# game background
        self.text=self.black# regular text
        self.instructions=self.darkerpurple# any instruction text/element
        self.drawing=(220,0,0)# drawing
        self.input=self.red# text input (in text)
        self.textinput=(200,0,0)# text input (box and highlight)
        self.textchoice=(180,0,0)# text input box
        # Colors for story
        self.player=self.red# player text color
        self.hero=self.red# hero text color
        self.hero2=self.text# hero in secondary context (he/him..)
        self.partner=self.pink
        self.partner2=self.text
        #
        self.villain=self.brown
        self.villain2=self.text
        self.bug=self.maroon
        self.bug2=self.text
        self.password=self.red# password color
        self.password2=self.text
        #
        self.grandmaster=self.red
        self.grandmaster2=self.text
        self.bunny=self.darkgreen#self.darkorange
        self.bunny2=self.text
        self.elder=self.darkgray
        self.elder2=self.text
        self.sailor=self.lightblue
        self.sailor2=self.text
        #
        self.skeleton=self.maroon
        self.skeleton2=self.text
        self.cow=self.blue
        self.cow2=self.text
        #
        self.item=self.instructions# items (when prompted to draw)
        self.item2=self.text# items in secondary context
        self.location=self.darkgreen# locations
        self.location2=self.text



# fonts database
class obj_fonts:
    def __init__(self):
         self.font15=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 15)# tiny (for FPS)
         self.font30=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 30)# small indicators,textbox
         self.font40=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 40)# small indicators,textbox
         self.font50=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 50)# medium (for story text)
         self.font60=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 60)# large
         self.font80=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 80)# larger
         self.font100=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 100)# big (for titlescreen)
         self.font120=core.obj_sprite_font('data/AmaticSC-Bold.ttf', 120)# huge
    def font(self,fontname):# call by key(string)
         if fontname=='tiny' or fontname==15:
             return self.font15
         elif fontname=='smaller' or fontname==30:
             return self.font30
         elif fontname=='small' or fontname==40:
             return self.font40
         elif fontname=='medium' or fontname==50:
             return self.font50
         elif fontname=='large' or fontname==60:
             return self.font60
         elif fontname=='larger' or fontname==80:
             return self.font80
         elif fontname=='big' or fontname==100:
             return self.font100
         elif fontname=='huge' or fontname==120:
             return self.font120
         else:
             return self.font50# medium font


# brushes  database (used for drawing)
class obj_brushes:
    def __init__(self):
        self.megapen=('data/pen.png',(32,32))
        self.bigpen=('data/pen.png',(16,16))
        self.pen12=('data/pen.png',(12,12))
        self.pen10=('data/pen.png',(10,10))
        self.pen=('data/pen.png',(8,8))
        self.pen6=('data/pen.png',(6,6))
        self.pen5=('data/pen.png',(5,5))
        self.smallpen=('data/pen.png',(4,4))
        self.tinypen=('data/pen.png',(2,2))
        self.shadowpen=('data/shadowpen.png',(64,64))
        self.emptypen=('data/emptypen.png',(8,8))


####################################################################################################################


# Data Manager: manages all data files
# flieprogress: last unlocked chapter
# filewords: dictionary of textinputs,textchoices written in the book of things (by the player)
class obj_datamanager:
    def __init__(self):
        self.fileprogress='book/progress.txt'# current game progress for unlocks
        self.loadprogress()
        self.filewords='book/words.txt'# current written words for things
        self.loadwords()
        self.filesettings='book/settings.txt'
        self.loadsettings()
        self.temp=obj_datatemp()# object for temporal data storage (by anyone anytime)
    def getdevaccess(self):# tell if user has developper access (from reading settings.txt)
        return self.devaccess
    def erasebook(self):
        files = tool.oslistdir('book')
        if '.gitkeep' in files: files.remove('.gitkeep')# do not erase git file
        for i in files: tool.osremove('book/'+i)# erase everything
        self.loadprogress()# reset progress
        self.saveprogress()
        self.loadwords()# reset words
        self.savewords()
        self.savesettings()# conserve current settings
    #
    def getprogress(self):
        return self.chapter# last chapter unlocked
    def saveprogress(self):
        with open(self.fileprogress,'w+') as f1:
            f1.write('maxchapter:'+'\n')# highest unlocked chapter
            f1.write(str(self.chapter)+'\n')#
            f1.write('allbookmarks:'+'\n')# all unlocked bookmarks
            for i in self.allbookmarks:
                f1.write(str(i)+'\n')#
    def loadprogress(self):
        if tool.ospathexists(self.fileprogress):
            self.allbookmarks=[]
            f1=open(self.fileprogress,'r+')
            line=f1.readline()# highest unlocked chapter
            line=f1.readline()
            self.chapter=int(line)
            line=f1.readline()# all bookmarks text
            line=f1.readline()
            while line:
                self.allbookmarks.append(line[:-1])
                line=f1.readline()# all bookmarks text
            f1.close()
        else:
            # default progress
            self.chapter=0
            self.bookmarkname='ch0_start'
            self.allbookmarks=['ch0_start']
            self.saveprogress()
    def updateprogress(self,chapter=None):# update highest unlocked chapter (for menu display)
        if chapter:
            self.chapter=max(self.chapter,chapter)
        self.saveprogress()

    def setbookmark(self,bookmarkname):# update name of bookmark (current page to return to)
        if bookmarkname not in self.allbookmarks:# add to list of unlocked bookmarks
            self.allbookmarks.append(bookmarkname)
            self.saveprogress()
    #
    def savesettings(self):
        with open(self.filesettings,'w') as f1:
                f1.write('doazerty:'+'\n')#key
                f1.write(str(self.doazerty)+'\n')#value
                f1.write('dowindowed:'+'\n')#key
                f1.write(str(self.donative)+'\n')#value
                f1.write('doshowfps:'+'\n')#key
                f1.write(str(self.doshowfps)+'\n')#value
                f1.write('domusic:'+'\n')#key
                f1.write(str(self.domusic)+'\n')#value
                f1.write('musicvol:'+'\n')#key
                f1.write(str(self.musicvol)+'\n')#value
                f1.write('dosound:'+'\n')#key
                f1.write(str(self.dosound)+'\n')#value
                f1.write('soundvol:'+'\n')#key
                f1.write(str(self.soundvol)+'\n')#value
                f1.write('brightness:'+'\n')#key
                f1.write(str(self.brightness)+'\n')#value
                f1.write('devaccess:'+'\n')#key
                f1.write(str(self.devaccess)+'\n')#value
    def loadsettings(self):
        if tool.ospathexists(self.filesettings):
            with open(self.filesettings,'r+') as f1:
                line=f1.readline()# difficulty
                line=f1.readline()
                self.doazerty=line=='True'+'\n'
                line=f1.readline()# donative (dowindowed)
                line=f1.readline()
                self.donative=line=='True'+'\n'
                line=f1.readline()# doshowfps
                line=f1.readline()
                self.doshowfps=line=='True'+'\n'
                line=f1.readline()# domusic
                line=f1.readline()
                self.domusic=line=='True'+'\n'
                line=f1.readline()# musicvol
                line=f1.readline()
                self.musicvol=int(line)
                self.musicvol=max(0,self.musicvol)# safety checks
                self.musicvol=min(5,self.musicvol)
                line=f1.readline()# dosound
                line=f1.readline()
                self.dosound=line=='True'+'\n'
                line=f1.readline()# soundvol
                line=f1.readline()
                self.soundvol=int(line)
                self.soundvol=max(0,self.soundvol)# safety checks
                self.soundvol=min(5,self.soundvol)
                line=f1.readline()# backgroundcolor
                line=f1.readline()
                self.brightness=int(line)
                self.brightness=max(0,self.brightness)# safety checks
                self.brightness=min(5,self.brightness)
                line=f1.readline()# dev access
                line=f1.readline()#
                self.devaccess=line=='True'+'\n'
        else:
            # default settings
            self.doazerty=False# qwerty keyboard
            self.donative=False# 1280x720(native windowed) or adapted (fullscreen) resolution
            self.doshowfps=False# show fps on/off
            self.domusic=True# music on/off
            self.musicvol=3# 0-5 music volume
            self.dosound=True# sound on/off
            self.soundvol=3# 0-5 sound volume
            self.brightness=4# background color (0-5 for gray to white, default=white)
            self.devaccess=False# User has no dev access by default
            # write down default settings
            self.savesettings()
    def getbackcolor(self):# return background color (0-255) from brightness level (0-5)
        minbri=235# min brightness (keep >= 235 cf pen/eraser/book shadows are at 225)
        tempo=int( self.brightness/5*(255-minbri) )+minbri
        return (tempo,tempo,tempo)
    #
    # words written by user
    def getwords(self):
        return self.dictwords# dictionary of words=(key,value)
    def getwordkeys(self):
        return self.dictwords.keys()
    def getword(self,wordkey):
        return self.dictwords[wordkey]
    def setword(self,wordkey,wordvalue):
        self.writeword(wordkey,wordvalue)
    def writeword(self,wordkey,wordvalue):
        self.dictwords[wordkey]=wordvalue
    def savewords(self):# save keywords to file
        with open(self.filewords,'w') as f1:
            for i in self.dictwords.items():# iterate over tuples =(key,value)
                f1.write(str(i[0])+'\n')#key
                f1.write(str(i[1])+'\n')#value
    def loadwords(self):# load keywords from file
        if tool.ospathexists(self.filewords):
            self.dictwords={}
            with open(self.filewords,'r') as f1:
                matrix=f1.read().splitlines()
                for i in range(int(len(matrix)/2)):# read alternated key,value on lines
                    self.dictwords[matrix[i*2]]=matrix[i*2+1]
        else:
            # default words (empty)
            self.dictwords={}
            # save if empty
            self.savewords()
    #
    # control names
    def controlname(self,name):
        # control names
        self.dictcontrolnames={}
        self.dictcontrolnames['up']='up'
        self.dictcontrolnames['down']='down'
        self.dictcontrolnames['left']='left'
        self.dictcontrolnames['right']='right'
        self.dictcontrolnames['action']='space'
        self.dictcontrolnames['back']='tab'
        self.dictcontrolnames['quit']='esc'
        self.dictcontrolnames['dev']='lctrl'
        self.dictcontrolnames['mouse1']='left mouse'
        self.dictcontrolnames['mouse2']='right mouse'
        self.dictcontrolnames['arrows']='arrows'
        self.dictcontrolnames['mouse']='mouse'
        self.dictcontrolnames['keyboard']='keyboard'
        #
        return self.dictcontrolnames[name]
    #
    # check if a drawing by has already been done by the player
    def drawingmade(self,name):
        return tool.ospathexists('book/'+name+'.png')


# Temp object for datamanager: store any temporal data here
# (under share.datamanager.temp.something=True)
class obj_datatemp:
    def __init__(self):
        self.setup()
    def setup(self):
        pass

####################################################################################################################
# *SNAPSHOTS DATABASE
#
# Snapshot manager
# A snapshot is an image combining several parts (images)
# Issue is: it needs to be remade EVERY TIME one of its part is modified
# the snapshot manager redoes all related images for a given drawing (it is automatically called on drawing finish)
class obj_snapshotmanager:
    def __init__(self):
        pass
    def remake(self,name):
        # Note: order matters! (some image needed for remaking others)
        #
        # pen
        if name=='pendraw':
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('pendraw',(640,360),scale=0.666))
            dispgroup1.snapshot((640,360,100,200),'pen')
        # eraser
        if name=='eraserdraw':
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('eraserdraw',(640,360),scale=0.666))
            dispgroup1.snapshot((640,360,135,135),'eraser')
        # book
        if name=='bookdraw':
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bookdraw',(640,360),scale=0.666))
            dispgroup1.snapshot((640,360,210,180),'book')

        # hero
        if name=='happyfacedraw':
            # heroface redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('happyfacedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'happyface')
            # combine sitckhead+happyface=herohead
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('happyface',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'herohead')
            # combine herohead+stickbody = herobase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360,200,300),'herobase')
            # combine herohead+stickbodyarmsup = heroarmsup
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbodyarmsup',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360,200,300),'heroarmsup')
            # combine herohead(rotated)+stickbodyarmsup = heroarmfacesup
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbodyarmsup',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5,rotate=90) )
            dispgroup1.snapshot((640,360,200,300),'heroarmsfaceup')
            # make herobaseangry (obsolete, used to be with angry head)
            # dispgroup1=draw.obj_dispgroup((640,360))
            # dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            # dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            # dispgroup1.snapshot((640,360,200,300),'herobaseangry')
            # herohead+stickbody+zapaura=herozapped
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup2.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup2.addpart('part3',draw.obj_image('zapaura',(640,360),path='data/premade') )
            dispgroup2.snapshot((640,360,200,300),'herozapped')
            # herohead+stickcrouch =herocrouch
            image1=draw.obj_image('stickcrouch',(940,360),path='data/premade')
            image2=draw.obj_image('herohead',(800,360),scale=0.5,rotate=90)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((940,360,300,200),'herocrouch')# 0 to 660 in height
            # heromech armature
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5) )
            dispgroup1.addpart( 'part2', draw.obj_image('heromecharmature_noface',(640,360),path='data/premade') )
            dispgroup1.snapshot((640,360,300,220),'heromecharmature')

        # partner
        if name in ['happyfacedraw','partnerhairdraw']:
            # partnerface redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('partnerhairdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'partnerhair')
            # combine stickbody+stickhead+partnerhair=partnerbasenoface
            image1=draw.obj_image('stickbody',(640,460),path='data/premade')
            image2=draw.obj_image('partnerhair',(640,200))
            image3=draw.obj_image('stickhead',(640,200),path='data/premade')# hero instead of stick head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.addpart('part3',image3)
            dispgroup1.snapshot((640,330,200,330),'partnerbasenoface')# 0 to 660 in height
            # combine stickbody+herohead+partnerhair=partnerbase
            image1=draw.obj_image('stickbody',(640,460),path='data/premade')
            image2=draw.obj_image('partnerhair',(640,200))
            image3=draw.obj_image('herohead',(640,200),scale=0.5)# hero instead of stick head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.addpart('part3',image3)
            dispgroup1.snapshot((640,330,200,330),'partnerbase')# 0 to 660 in height
            #combine stickhead+partnerhair=parnerhead
            image1=draw.obj_image('partnerhair',(640,200))
            image2=draw.obj_image('herohead',(640,200),scale=0.5)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,200,200,200),'partnerhead')

        # villain
        if name in ['scardraw','angryfacedraw']:
            # angryface redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('angryfacedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'angryface')
            # scar redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('scardraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'scar')
            # save angry head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='data/premade'))
            dispgroup1.addpart('part2',draw.obj_image('angryface',(640,360)))
            dispgroup1.snapshot((640,360,200,200),'angryhead')
            # save villain head drawing
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('angryhead',(640,360)) )
            dispgroup1.addpart('part2',draw.obj_image('scar',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'villainhead')
            # save villain full body (slightly different than hero, because originally we could include partnerhair)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup2.addpart('part2',draw.obj_image('villainhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,330,200,330),'villainbase')
            # villainhead+stickshootcrouch =villainshootcrouch (beware larger if girl)
            image1=draw.obj_image('stickshootcrouch',(640,360+100),path='data/premade')
            image2=draw.obj_image('villainhead',(640,360),scale=0.5,fliph=True)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360+100-50,300,250),'villainshootcrouch')# 0 to 660 in height
            # villain rest
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('stickbodyrest',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('villainhead',(640+80,200+50),scale=0.5,rotate=-10) )
            dispgroup1.snapshot((640,330,200,330),'villainbaserest')
            # villainmech armature
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part3', draw.obj_image('villainmecharmature_noface',(640,360),path='data/premade') )
            dispgroup1.snapshot((640,360,300,220),'villainmecharmature')
        if name in ['scardraw','angryfacedraw','partnerhairdraw']:
            # villainbase+partnerbase=villainholdspartner
            image1=draw.obj_image('villainbase',(640,360))
            image2=draw.obj_image('partnerbase',(640-70,360+80),rotate=90)
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,400,330),'villainholdspartner')

        #bug
        if name=='bugdraw':
            # bug redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bugdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'bug')

        # grandmasters
        # if name =='bunnyfacedraw':
        #     # save bunny head
        #     dispgroup1=draw.obj_dispgroup((640,360))
        #     dispgroup1.addpart('part1',draw.obj_image('bunnystickhead',(640,360+150),scale=0.75,path='data/premade'))
        #     dispgroup1.addpart('part2',draw.obj_image('bunnyfacedraw',(640,360)))
        #     dispgroup1.snapshot((640,360,400,300),'bunnyhead')
        # if name in ['bunnyfacedraw','bunnybodydraw']:
        #     # bunny body redux
        #     dispgroup1=draw.obj_dispgroup((640,360))
        #     dispgroup1.addpart('part1',draw.obj_image('bunnybodydraw',(640,360),scale=0.666))
        #     dispgroup1.snapshot((640,360,200,155),'bunnybody')
        #     # bunny head+body
        #     dispgroup1=draw.obj_dispgroup((640,360))
        #     dispgroup1.addpart('part1',draw.obj_image('bunnybody',(640,360+65)))
        #     dispgroup1.addpart('part2',draw.obj_image('bunnyhead',(640,360-150),scale=0.5))
        #     dispgroup1.snapshot((640,295,200,235+50),'bunnybase')
        if name =='bunnyfacedraw':
            # save bunny head
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bunnystickheadnew',(640,360),path='data/premade'))
            dispgroup1.addpart('part2',draw.obj_image('bunnyfacedraw',(640,360+100)))
            dispgroup1.snapshot((640,360,400,300),'bunnyhead')
        if name in ['bunnyfacedraw','bunnybodydraw']:
            # bunny body redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bunnybodydraw',(640,360),scale=0.666))
            dispgroup1.snapshot((640,360,200,155),'bunnybody')
            # bunny head+body
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bunnybody',(640,360+65)))
            dispgroup1.addpart('part2',draw.obj_image('bunnyhead',(640,360-150),scale=0.5))
            dispgroup1.snapshot((640,295,200,235+50),'bunnybase')
        if name =='elderheaddraw':
            # elderhead redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part0',draw.obj_image('stickhead',(640,360),scale=2,path='data/premade') )
            dispgroup1.addpart('part1',draw.obj_image('elderheaddraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'elderhead')
            # # save elder full body (slight offset made)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,330,200,330),'elderbase')
            # save elder full body (This is the CORRECT way, is used for some animations)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,360,200,300),'elderbase2')
        if name =='sailorfacedraw':
            # sailorface redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('sailorfacedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'sailorface')
            # combine sitckhead+sailorface=sailorbaldhead
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('sailorface',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'sailorbaldhead')
        if name in ['sailorfacedraw','sailorhat']:
            # save sailor head
            dispgroup1=draw.obj_dispgroup((640,450))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('sailorbaldhead',(640,450),scale=1))
            dispgroup1.addpart('part2',draw.obj_image('sailorhat',(640,450-200)))
            dispgroup1.snapshot((640,325+50,400,275),'sailorhead')# 250, 275
            # combine herohead+stickbody = herobase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('sailorbaldhead',(640,200),scale=0.5))
            dispgroup1.addpart('part3',draw.obj_image('sailorhat',(640,200-100),scale=0.5))
            dispgroup1.snapshot((640,360-15,200,300+15),'sailorbase')
        #
        # skeletons
        if name =='skeletonheaddraw':
            #skeletonhead redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('skeletonheaddraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'skeletonhead')
            # combine skeletonhead+stickbody = skeletonbase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('skullheadnocontours',(640,200),path='data/premade') )
            dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase')
        if name in ['skeletonheaddraw','partnerhairdraw']:
            # skeleton with hair
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('partnerhair',(640,200)) )
            dispgroup1.addpart('part3',draw.obj_image('skullheadnocontours',(640,200),path='data/premade') )
            dispgroup1.addpart('part4',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_partnerhair')
        if name in ['skeletonheaddraw','sailorhat']:
            # skeleton with sailor hat
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='data/premade') )
            dispgroup1.addpart('part2',draw.obj_image('skullheadnocontours',(640,200),path='data/premade') )
            dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_sailorhat')

        #
        # chapter items
        if name=='fishdraw':
            # fish draw
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('fishback',(640,360),scale=1,path='data/premade'))
            dispgroup1.addpart('part2',draw.obj_image('fishdraw',(640,360),fliph=True,scale=1))
            dispgroup1.snapshot((640,360,300,200),'fish')
        if name in ['happyfacedraw','fishdraw']:
            # combine hero+fish into: hero holding fish
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('herobase',(640,452), scale=0.7))
            dispgroup1.addpart('part2',draw.obj_image('fish',(776,486), scale=0.4,rotate=-90))
            dispgroup1.snapshot((700,452,200,260),'herobasefish')
        # love heart draw
        if name=='lovedraw':
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('lovedraw',(640,360),scale=4/3))
            dispgroup1.snapshot((640,360,300,200),'love')

        if name=='housedraw':
            # house redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('housedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'house')
        if name=='ponddraw':
            # pond redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('ponddraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'pond')
        if name=='towerdraw':
            # tower redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('towerdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'tower')
        if name=='bushdraw':
            # bush redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('bushdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'bush')
        if name=='flowerdraw':
            # flower redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('flowerdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'flower')
        if name in ['scardraw','angryfacedraw','gun']:
            # villainbase+gun =villainbasegun (for cutscenes)
            image1=draw.obj_image('villainbase',(640,330))
            image2=draw.obj_image('gun',(640+180,330),scale=0.4)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640+50,330,200+50,330),'villainbasegun')# 0 to 660 in height
        if name=='mountaindraw':
            # mountain redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('mountaindraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'mountain')
        if name=='nightstanddraw':
            # nightstand redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('nightstanddraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'nightstand')
        if name =='alarmclockextdraw':
            # alarmclockext redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('alarmclockextdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'alarmclockext')
            # combine alarmclockext+alarmclockfill=alarmclock (no hour shown)
            image1=draw.obj_image('alarmclockext',(640,360))
            image2=draw.obj_image('alarmclockfill',(640,360),path='data/premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock')
            # combine alarmclock+alarmclockcenter8am=alarmclock8am (morning)
            image1=draw.obj_image('alarmclock',(640,360))
            image2=draw.obj_image('alarmclockcenter8am',(640,360),path='data/premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock8am')
            # combine alarmclock+alarmclockcenter8am=alarmclock8am (night)
            image1=draw.obj_image('alarmclock',(640,360))
            image2=draw.obj_image('alarmclockcenter12am',(640,360),path='data/premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock12am')
        if name=='cavedraw':
            # cave redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('cavedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'cave')
        if name=='treedraw':
            # tree redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('treedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'tree')
        if name=='clouddraw':
            # cloud redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('clouddraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'cloud')
        if name=='lightningboltdraw':
            # lightningbolt redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('lightningboltdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'lightningbolt')
        if name=='palmtreedraw':
            # palmtree redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('palmtreedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'palmtree')
        if name=='cowdraw':
            # cow redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('cowdraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,300,200),'cow')
        if name in ['happyfacedraw','cowdraw']:
            # combine herobase+cow=heroridecow
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('herobase',(640,360-100),scale=0.5) )
            dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
            dispgroup1.snapshot((640,360+25,300,300-25),'heroridecow')


        # mechs
        if name in ['towerdraw','mountaindraw','gun','lightningboltdraw','cavedraw']:
            # villainmech complete no face
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('villainmecharmature_noface',(640,360),path='data/premade') )
            dispgroup1.addpart( 'part2', draw.obj_image('tower',(640,180),scale=0.35) )
            dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
            dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
            dispgroup1.snapshot((640,360,410,330),'villainmechbase_noface')
        if name in ['scardraw','angryfacedraw','towerdraw','mountaindraw','gun','lightningboltdraw','cavedraw']:
            # villainmech complete
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part3', draw.obj_image('villainmechbase_noface',(640,360)) )
            dispgroup1.snapshot((640,360,410,330),'villainmechbase')
        if name in ['housedraw','bushdraw','fishdraw','scissors','sailboat']:
            # heromech complete no face
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature_noface',(640,360),path='data/premade') )
            dispgroup1.addpart( 'part2', draw.obj_image('house',(640,180),scale=0.35) )
            dispgroup1.addpart( 'part3', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part4', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('fish',(640-300,470),scale=0.3,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part6', draw.obj_image('scissors',(640+300,470),scale=0.35,rotate=-45,flipv=True) )
            dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
            dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
            dispgroup1.snapshot((640,360,410,330),'heromechbase_noface')
        if name in ['happyfacedraw','housedraw','bushdraw','fish','scissors','sailboat']:
            # heromech complete
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature',(640,360)) )
            dispgroup1.addpart( 'part2', draw.obj_image('heromechbase_noface',(640,360)) )
            dispgroup1.snapshot((640,360,410,330),'heromechbase')
        #
        if name=='cakedraw':
            # cake redux
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('cakedraw',(640,360),scale=0.8))
            dispgroup1.snapshot((640,360,200,200),'cake')



####################################################################################################################
