#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Billiard Knight
# Game by sul
# Created April-May-June 2020
# runs with pygame 1.9.4
#
##########################################################
##########################################################
# Import libraries and other files

import pygame# (should only be select functions?)
from pygame import mixer#sound

# Basic maths
from math import cos as cos
from math import sin as sin
from math import atan2 as atan2
from math import pi as pi
from math import sqrt as sqrt
from math import floor as floor
from math import ceil as ceil
# import random

import os.path# for knowing which level files are present
import sys# to properly quit game

# import bk_globalvars
# from bk_globalvars import *
# from bk_display import obj_display
##########################################################ccccc
# Summary of code structure:

# imports
#
# scene
# titlescreen (creator=scene)
# overworld (creator=scene)
# level editor (creator=scene)
# level (creator=scene)
#
# background (creator=level)
# player (creator=level)
# mouse pointer (creator=level)
# enemies (creator=level)
#
# holes (creator=level)
# obstacles (sphere,rectangle,triangle) (creator=level)
# forces (creator=level)
#
# physics engine (creator=level)
# other functions
# controls
#
# game initialization (define all functions/objects beforehand)
# game loop

##########################################################
##########################################################
##########################################################


# Display Manager
#*DISPLAY
# Manages display
class obj_display:
    def __init__(self):
        #
        # Get computer screen infos (only once when game starts with display on)
        self.infos=pygame.display.Info()# info object from pygame

        # Default Configuration
        self.native=False# default configuration screenwxscreenh (overwrites all other parameters, is not selected in game)
        # Resolution
        # self.displayresolution=(0,0)# adapted
        # self.displayresolution=(800,600)# the game was originally first with that resolution
        self.displayresolution=(1280,720)# the game native resolution. It is standard 720p resolution
        # self.displayresolution=(1920,1080)# standard resolution 1080p. It is 1.5x the 720p resolution
        # self.displayresolution=(2560,1440)# other standard resolution, 2x the 720p. Best performance/look if combined with 2xs scaling.
        self.adapted=False# becomes true if (0,0) proposed
        # Scaling method (pick only one)
        self.scalingmethod='s'# choose between s(=default),ss,s2x (scaling can still be omitted if possible).
        self.noscaling=False# no scaling needed (dont create new surface)
        self.smoothscaling=False# smooth scaling method (instead of regular scaling)
        self.scaling2x=False# 2x scale method, nice round edges! (only if display screen is 2xnative=1600x1200)
        self.scaling2xforced=False# Exploratory, scale first to a display/2 surface then 2xscale to display
        # Keys
        self.optionset='windowed'# choose between windowed(=default),borders, fullscreen

        self.noframe=False# no frame/controls on window
        # self.fullscreen=False# fullscreen mode (=False always, too dangerous if cant exit!)
        # self.resizable=False# toggle omitted (=False always)
        # self.hwsurface=False# toggle omitted (should better be =True if fullscreen)
        # self.doublebuf=False# toggle omitted (should better be =True if fullscreen)
        #
        # Setup
        self.setup()# initial setup (can be repeated on settings changes)
        #
    def reset(self):# reset display with new values
        # self.mousepos=pygame.mouse.get_pos()# get current mouse position
        pygame.display.quit()
        self.setup()
        controls.set_mousescaling(display.mousescaling)# retell controls about new mouse scaling!
        # pygame.mouse.set_pos(self.mousepos)# reset mouse position to previous before changes
    def setup(self):
        #
        # Create Game Screen
        global screen
        screen = pygame.Surface((screenw,screenh))# native screen for game to draw on
        #
        # Get current computer screen infos
        # self.availableresolutions=pygame.display.list_modes()# list of all possible resolutions
        #
        # Manage Keys Dependencies
        if self.native: self.displayresolution,self.adapted,self.optionset,self.scalingmethod=\
            (screenw,screenh),False,False,'windowed','s'# default mode
        self.adapted= (self.displayresolution==(0,0))
        if not self.adapted:
            if self.displayresolution[0]<screenw: self.displayresolution=(screenw,self.displayresolution[1])# scale if smaller than source
            if self.displayresolution[1]<screenh: self.displayresolution=(self.displayresolution[0],screenh)
        if self.displayresolution[0]>self.infos.current_w: self.displayresolution=(0,0)# switch to adapted if too big
        if self.displayresolution[1]>self.infos.current_h: self.displayresolution=(0,0)
        if self.scalingmethod == 's': self.noscaling,self.smoothscaling,self.scaling2x,self.scaling2xforced = False,False,False,False
        if self.scalingmethod == 'ss': self.noscaling,self.smoothscaling,self.scaling2x,self.scaling2xforced = False,True,False,False
        if self.scalingmethod == 's2x':
            if self.displayresolution==(screenw*2,screenh*2):
                self.noscaling,self.smoothscaling,self.scaling2x,self.scaling2xforced = False,False,True,False
            else:
                self.noscaling,self.smoothscaling,self.scaling2x,self.scaling2xforced = False,False,False,True
        if self.scaling2x and self.displayresolution != (2*screenw,2*screenh): self.scaling2x=False# (revert to s=scaling)
        if self.displayresolution==(screenw,screenh): # if target resolution match source, omit all scaling methods
            self.noscaling,self.smoothscaling,self.scaling2x,self.scaling2xforced = True,False,False,False
        #
        # Create Display Screen
        if self.native:
            screen = pygame.display.set_mode(self.displayresolution)
            self.displayscreen=False# no need for extra screen
        else:
            if self.optionset == 'windowed':
                if self.noscaling:
                    screen = pygame.display.set_mode(self.displayresolution)
                    self.displayscreen=False# no need for extra screen
                else:
                    self.displayscreen = pygame.display.set_mode(self.displayresolution)
            elif self.optionset == 'borders':# make display screen at computer resolution and with no frames
                self.displayscreen = pygame.display.set_mode((self.infos.current_w,self.infos.current_h), pygame.NOFRAME)
            elif self.optionset == 'fullscreen':# make display screen at computer resolution and with no frames
                self.displayscreen = pygame.display.set_mode((self.infos.current_w,self.infos.current_h), pygame.FULLSCREEN)
                # self.displayscreen = pygame.display.set_mode((self.infos.current_w,self.infos.current_h), pygame.FULLSCREEN, pygame.HWSURFACE, pygame.DOUBLEBUF)
            else:
                self.displayscreen = pygame.display.set_mode(self.displayresolution)

        # Adjustments for Display Screen
        if self.adapted: # from 0x0 to computer resolution# dont strech but conserve ratios
            # self.displayresolution=(self.infos.current_w, self.infos.current_h)# this would be a simple stretch
            if self.infos.current_w/self.infos.current_h > screenw/screenh: # target screen is wide compared to source, match heigth only
                self.displayresolution=( int(self.infos.current_h*screenw/screenh), self.infos.current_h )
            else:
                self.displayresolution=( self.infos.current_w, int(self.infos.current_w*screenh/screenw) )
        if self.scaling2xforced:
            self.screen2xforced_dr=(int(self.displayresolution[0]/2),int(self.displayresolution[1]/2))
            self.screen2xforced = pygame.Surface(self.screen2xforced_dr)# create another intermediary screen
        # Game Window Decorations
        pygame.display.set_caption("Billiard Knight")# text on window banner
        pygame.display.set_icon(pygame.image.load('data/bk_imgwindowicon.png').convert_alpha())# icon on window banner
        # Mouse
        self.mousescaling=(screenw/ self.displayresolution[0],screenh/ self.displayresolution[1])# scaling
        pygame.mouse.set_visible(False)# Hide Mouse
        # Remove alpha (for increased performances ?)
        if self.native or self.noscaling:
            screen.set_alpha(None)
        else:
            self.displayscreen.set_alpha(None)
        #
        # If Borders are needed: create intermediary screen with target resolution
        if self.optionset=='borders' or self.optionset=='fullscreen' or (self.optionset=='windowed' and self.adapted):
            self.intermscreen=pygame.Surface(self.displayresolution)
            self.intermscreen_offsetx=int(self.infos.current_w/2-self.displayresolution[0]/2)
            self.intermscreen_offsety=int(self.infos.current_h/2-self.displayresolution[1]/2)
            # Need to rescale mouse again in that case omitting borders
            self.mousescaling=(screenw/ self.infos.current_w,screenh/ self.infos.current_h)# scaling
            self.intermscreen.set_alpha(None)
    def update(self):
        # Apply draw methods depending on conditions
        #
        # Native: override all other options
        if self.native:
            pass# screen is already the display screen, disregard all other options
        # # Simple Windows that fit into the screen: draw directly
        elif (self.optionset=='windowed'):
            if not self.adapted:# Windowed-non Adapted: directly scale and draw
                if self.noscaling:
                    pass# nothing necessary, screen is already the display
                else:
                    if self.smoothscaling:
                        pygame.transform.smoothscale(screen,self.displayresolution,self.displayscreen)
                    elif self.scaling2x:
                        pygame.transform.scale2x(screen,self.displayscreen)# must be exactly 2x
                    elif self.scaling2xforced:#note: interm scaling should be scale not smoothscale (much more efficient)
                        pygame.transform.scale(screen,self.screen2xforced_dr,self.screen2xforced)
                        pygame.transform.scale2x(self.screen2xforced,self.displayscreen)
                    else:
                        pygame.transform.scale(screen,self.displayresolution,self.displayscreen)
            else:# Windowed-Adapted: use intermediary surface
                if self.noscaling:
                    pass# this should not be the case under window-adapted option (unless computer screen is at screenw,screenh?)
                else:
                    if self.smoothscaling:
                        pygame.transform.smoothscale(screen,self.displayresolution,self.intermscreen)
                    elif self.scaling2x:
                        pygame.transform.scale2x(screen,self.intermscreen)# must be exactly 2x
                    elif self.scaling2xforced:
                        pygame.transform.scale(screen,self.screen2xforced_dr,self.screen2xforced)
                        pygame.transform.scale2x(self.screen2xforced,self.intermscreen)
                    else:
                        pygame.transform.scale(screen,self.displayresolution,self.intermscreen)
                    # blit intermediary screen to display
                    self.displayscreen.blit(self.intermscreen,(self.intermscreen_offsetx,self.intermscreen_offsety))
        # Windows with borders: always use intermediary surface (unless no scaling)
        elif self.optionset=='borders' :
            if self.smoothscaling:
                pygame.transform.smoothscale(screen,self.displayresolution,self.intermscreen)
            elif self.scaling2x:
                pygame.transform.scale2x(screen,self.intermscreen)# must be exactly 2x
            elif self.scaling2xforced:
                pygame.transform.scale(screen,self.screen2xforced_dr,self.screen2xforced)
                pygame.transform.scale2x(self.screen2xforced,self.intermscreen)
            else:
                pygame.transform.scale(screen,self.displayresolution,self.intermscreen)
            # blit intermediary screen to display
            self.displayscreen.blit(self.intermscreen,(self.intermscreen_offsetx,self.intermscreen_offsety))
        # Fullscreen= same as window with borders: always use intermediary surface (unless no scaling)
        elif self.optionset=='fullscreen' :
            if self.smoothscaling:
                pygame.transform.smoothscale(screen,self.displayresolution,self.intermscreen)
            elif self.scaling2x:
                pygame.transform.scale2x(screen,self.intermscreen)# must be exactly 2x
            elif self.scaling2xforced:
                pygame.transform.scale(screen,self.screen2xforced_dr,self.screen2xforced)
                pygame.transform.scale2x(self.screen2xforced,self.intermscreen)
            else:
                pygame.transform.scale(screen,self.displayresolution,self.intermscreen)
            # blit intermediary screen to display
            self.displayscreen.blit(self.intermscreen,(self.intermscreen_offsetx,self.intermscreen_offsety))
        # Update display
        pygame.display.update()

##########################################################
##########################################################

# sound module
# *SOUND
# manages all sounds and plays them when asked
class obj_sound:
    def __init__(self):
        self.sounddatabase=[]# sound database (name, filename, reference volume)
        # menu
        self.sounddatabase.append(obj_onesound( 'pause', 'smw_pause.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'nextpart', 'smw_pipe.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'menugo' , 'smw_map_move_to_spot.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'menuback' , 'smw_yoshi_runs_away.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'erasesave' , 'smw_lemmy_wendy_falls_out_of_pipe.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'cant' , 'smw_lemmy_wendy_incorrect.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'overworldmove' , 'smw_map_move_to_spot.wav' , 1 ))
        # player shots
        self.sounddatabase.append(obj_onesound( 'shootself' , 'smw_fireball.wav' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'shootself2' , 'smw_stomp_no_damage.wav' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'shootself3' , 'smw_yoshi_runs_away.wav' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'shootselfwater' , 'smw_swimming.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'slowdown' , 'smw_shell_ricochet.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'scrollup' , 'switch_004.ogg' , 0.2 ))
        self.sounddatabase.append(obj_onesound( 'scrolldown' , 'switch_005.ogg' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'slowtime' , 'sfx_wpn_missilelaunch.wav' , 0.1 ))
        self.sounddatabase.append(obj_onesound( 'jump' , 'smw_jump.wav' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'lava' , 'smw_lava_bubble.wav' , 0.5 ))

        # level
        self.sounddatabase.append(obj_onesound( 'finishready' , 'smw_power-up.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'hitlever' , 'smw_coin_voladj.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'enemyfalls' , 'smw_stomp.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'shrink' , 'smw_reserve_item_release.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'hitspill' , 'smw_dragon_coin.wav' , 1 ))
        self.sounddatabase.append(obj_onesound( 'clifffall' , 'smw_lemmy_wendy_falls_out_of_pipe.wav' , 1 ))
        # collisions
        self.sounddatabase.append(obj_onesound( 'mcircles' , 'impactSoft_medium_002.ogg' , 0.5 ))
        self.sounddatabase.append(obj_onesound( 'hitbdry' , 'impactSoft_medium_000.ogg' , 0.8 ))
        self.sounddatabase.append(obj_onesound( 'hit' , 'impactSoft_medium_001.ogg' , 1 ))
        self.sounddatabase.append(obj_onesound( 'hit_sp' , 'footstep_grass_003.ogg' , 1 ))
        self.sounddatabase.append(obj_onesound( 'hit_pk' , 'impactSoft_heavy_001.ogg' , 0.2 ))
        #
        # Channels
        self.nchannels=16# max number of channels allowed
        pygame.mixer.set_num_channels(self.nchannels)# set number of channels
        # self.ichannel=0# id (integer of the channel)# uncessary, pygame will automatically find/switch channels
    def load(self,onesound):# load sound for first time (parameter is the obj_onesound, must exist
        onesound.sound=mixer.Sound('sounds/'+onesound.filename)
        onesound.sound.set_volume(onesound.volume)# set at reference volume
        onesound.loaded=True
    def play(self,soundname):
        if dosound:
            for i in self.sounddatabase:
                if i.soundname == soundname:
                    if not i.loaded: self.load(i)
                    i.sound.play()# play the sound
                    # i.channel.play(i.sound)# play on imposed channel
    def play_mult_volume(self,soundname,volumemult):# play with a volume factor (reset volume afterwards)
        if dosound:
            for i in self.sounddatabase:
                if i.soundname == soundname:
                    if not i.loaded: self.load(i)
                    volume=i.sound.get_volume()# record current volume
                    i.sound.set_volume(volume*volumemult)
                    i.sound.play()# play the sound
                    i.sound.set_volume(volume)# reset volume to current
    def set_volume(self,soundname,volume):# change sound volume
        for i in self.sounddatabase:
                if i.soundname == soundname:
                    if not i.loaded: self.load(i)
                    i.sound.set_volume(volume)

# one sound data to be used by the sound module
class obj_onesound:
    def __init__(self,soundname,filename,volume):
        self.soundname=soundname
        self.filename=filename
        self.volume=volume
        self.loaded=False# if the sound is loaded in pygame mixer or not
        self.sound=False# here save the loaded sound
        self.channel=False# here save the channel the sound is playing on (obsolete)

##########################################################
##########################################################

# music manager
# loads and plays all musics
# Note: a music is always loaded, but is playing or not. Volume can be modified
#* MUSIC
class obj_music:
    def __init__(self):
        self.musicdatabase=[]# music database (name, filename, reference volume)

        self.musicdatabase.append(obj_onemusic( 'titlescreen' , '62 Staff Roll.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'overworld' , '12 Overworld.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'overworldtolevel' , '48 Fade Out!.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'win' , '47 Course Clear.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'loose' , '51 Player Down.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'none' , '62 Staff Roll.mp3' , 0 )) # no music
        #
        self.musicdatabase.append(obj_onemusic( 'chill1' , '04 Wandering the Plains.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'chill2' , '03 Yoshis Island.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'chill3' , '09 Star Road.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'chill4' , '02 Title.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'fast1' , '62 Staff Roll.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'fast2' , '64 Cast List.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'fast3' , '16 Athletic.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'fast4' , '40 Bonus Game.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'atm1' , '24 Swimming.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'atm2' , '06 Forest of Illusion.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'atm3' , '30 Fortress.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'atm4' , '28 Haunted House.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'atm5' , '20 Underground.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'dark1' , '05 Vanilla Dome.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'dark2' , '08 Valley of Bowser.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'dark3' , '43 Boss Battle.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'dark4' , '53 The Evil King Bowser.mp3' , 1 ))
        self.musicdatabase.append(obj_onemusic( 'mario' , '11 Super Mario Bros. Remix.mp3' , 1 ))
        self.music=self.musicdatabase[0]# take first element
        self.start()# start music

    def start(self):
        mixer.music.load('musics/'+self.music.filename)
        if domusic:
            self.set_volume(1)
            self.play()
    def restart(self):# load and play
        self.set_volume(1)
        self.play()
    def play(self):# play
        self.set_volume(1)
        mixer.music.play(-1)
    def stop(self):# stop playing
        self.set_volume(0)
        mixer.music.stop()
    def change(self,nextmusic):
        if nextmusic != self.music.musicname:
            for i in self.musicdatabase:
                if i.musicname == nextmusic:
                    self.music=i
                    if self.music.musicname == 'none':
                        self.stop()
                    else:
                        mixer.music.load('musics/'+self.music.filename)
                        if domusic:
                            self.play()
    def playonce(self,nextmusic): #actually is change and play once
            for i in self.musicdatabase:
                if i.musicname == nextmusic:
                    self.music=i
                    if domusic:
                        mixer.music.load('musics/'+self.music.filename)
                        mixer.music.play(1)
    def set_volume(self,volume):
        mixer.music.set_volume(volume)
    def set_volume_mult(self,volumemult):# set volume using multiplier
        volume=pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(volume*volumemult)

# one sound data to be used by the sound module
class obj_onemusic:
    def __init__(self,musicname,filename,volume):
        self.musicname=musicname
        self.filename=filename
        self.volume=volume
        self.loaded=False# if the sound is loaded in pygame mixer or not
        self.sound=False# here save the loaded sound


##########################################################
##########################################################

# Scene Manager
# *SCENE (this is a marker for browsing the code)
# Creates/Deletes and switches between levels
# Keeps titlescreen and overworld in memory but regenerates other levels
class obj_scenemanager:
    def __init__(self):
        # Rq: loading org
        self.titlescreen=obj_titlescreen(self)# titlescreen scene
        self.levelmanager=obj_levelmanager(self)# level manager (manages database, no scene)
        self.settingsscreen=obj_settingsscreen(self)# settings scene. load after levelmanager
        self.overworld=obj_overworld(self)# overworld scene. load after levelmanager
        self.levelscrollbar=obj_levelscrollbar(self)# level scrollbar. load after levelmanager
        self.leveleditor=obj_leveleditor(self)# level editor scene. load after levelmanager
        self.userleveleditor=obj_userleveleditor(self)# level editor scene. load after levelmanager
        #
        self.level=self.titlescreen# current level being played/unlocked
        self.levelname='titlescreen'# name of current level (for pause menu)
        #
        self.quitgame=obj_quit(self)# allows to quit the game
        self.pause=obj_pause(self)# runs in parallel to level
        self.dopause=False# activate pause menu
        #
        # initiate cutscenes (preloaded, modified by levels sometimes)
        self.cutscenelist=[]
        self.cutscenelist.append(obj_cutscene1(self))
        self.cutscenelist.append(obj_cutscene2(self))
        #
        self.debugfont=pygame.font.Font('data/editundo.ttf', 15)# text fonts
        #
        self.music=False# obsolete but may be called
    def changemusic(self,musicname):# obsolete but may be called by level files
        pass
    def changescene(self,nextscene,cutscene_name):
        if not cutscene_name or not any(i.name==cutscene_name for i in self.cutscenelist):# no cutscene
            self.progresstoscene(nextscene)
        else:# cutscene
            for i in self.cutscenelist:
                if i.name==cutscene_name:
                    i.nextscene=nextscene
                    i.timer=i.duration
                    self.level=i
                    break
    def progresstoscene(self,nextscene):
        self.levelname=nextscene# record level name (for various purpose e.g. pause menu)
        changexcam(0)# reset camera systematically (possibly after cutscene)
        changeycam(0)
        if nextscene=='quit':
            self.quitgame()# closes the game
        elif nextscene=='titlescreen':
            music.change('titlescreen')
            self.level= self.titlescreen
        if nextscene=='overworld':
            music.change('overworld')
            self.level=self.overworld
        if nextscene=='leveleditor':
            self.levelmanager.loadlevel_editmode()
        if nextscene=='levelscrollbar':
            music.change('overworld')
            self.level=self.levelscrollbar
        if nextscene=='settings':
            music.change('titlescreen')
            self.level=self.settingsscreen
            self.level.resetsavedone=False# can reset settings again
        if nextscene=='level':
            self.levelmanager.loadlevel()
        if nextscene=='userlevel':
            self.levelmanager.loaduserlevel()
        if nextscene=='userleveleditor':
            self.levelmanager.loaduserlevel_editmode()
    def update(self,controls):
        # Toggle Pause
        if controls.esc and controls.escc:
            if not self.dopause:
                self.pause.start()
            else:
                self.pause.end()
        # Scene (or Pause in Parallel)
        if self.dopause:
            self.pause.update(controls)
        else:
            self.level.update(controls)# Everything here !
        # Quit game
        if controls.quit: self.quitgame()
        # Always show FPS
        screen.blit(self.debugfont.render('FPS='+str(int(clock.get_fps())), True, (0, 0, 0)), (screenw-50,5))
        # Dev mode infos
        if dodebug:
            pygame.draw.rect(screen, (255,255,255), (0, 0, 60,13), 0)
            screen.blit(self.debugfont.render("Dev Mode", True, (0, 0, 0)), (0,0))
##########################################################
# OBJ Quit
#*QUIT
class obj_quit:
     def __init__(self,creator):
         self.creator=creator# created by scenemanager
     def __call__(self):
         # global ingame
         pygame.display.quit()
         pygame.mixer.music.stop()
         pygame.mixer.quit()
         pygame.quit()
         sys.exit()# very important to properly quit game without crashing


##########################################################
# OBJ Pause

# Pause game
#*PAUSE
class obj_pause:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.pointer=obj_pointersword(self)
        self.hoveringresume=False
        self.hoveringrestart=False
        self.hoveringexit=False
        self.rect_resume=(250*scsx,550*scsx,200*scsy,250*scsy)
        self.rect_restart=(250*scsx,550*scsx,275*scsy,325*scsy)
        self.rect_exit=(250*scsx,550*scsx,350*scsy,400*scsy)
        self.bigfont = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        #
        #
    def start(self):
        self.creator.dopause=True
        #
        # Determine which pause screen: none, menus (with settings), levels (with restart)
        if any(self.creator.levelname == i for i in ['titlescreen','settings','overworld','levelscrollbar',]):
            self.end()# end pause directly
        else:
            music.set_volume_mult(0.1)
            sound.play('pause')
            self.pausescreen=screen.copy()

    def end(self):
        self.creator.dopause=False
        music.set_volume_mult(10)
    def draw (self):
        screen.blit(self.pausescreen,(0,0))# copy of current screen
        #
        for i,j,k in zip([self.rect_resume,self.rect_restart,self.rect_exit],\
                       [self.hoveringresume,self.hoveringrestart,self.hoveringexit],\
                        ['Resume','Restart','Exit']):# Fullscreen options omitted for now
            pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(i), 0)
            pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(i), 3)
            func_drawtextinrect(k,self.bigfont,self.getcolor(j),i)
    def getcolor(self,inputboolean):# return color to draw depending on True/False input
        if inputboolean:
            return (222,198,0)
        else:
            return (0,0,0)
        return()
    def progress(self,controls):
        # just close menu
        if self.hoveringresume and controls.mouse1 and controls.mouse1c: # close menu
            self.end()
        # exit
        if self.hoveringexit and controls.mouse1 and controls.mouse1c:
            if self.creator.levelname == 'leveleditor':
                self.creator.changescene('overworld',False)
            elif self.creator.levelname == 'level':
                self.creator.changescene('overworld',False)
            elif self.creator.levelname == 'userlevel':
                self.creator.changescene('levelscrollbar',False)
            elif self.creator.levelname == 'userleveleditor':
                self.creator.changescene('levelscrollbar',False)
            else:
                self.creator.changescene('titlescreen',False)# this shouldnt happen
            self.end()
        # restart or settings
        if self.hoveringrestart and controls.mouse1 and controls.mouse1c:
            if self.creator.levelname == 'level':
                self.creator.changescene('level',False)
            elif self.creator.levelname == 'userlevel':
                self.creator.changescene('userlevel',False)
            self.end()

    def hovers(self,controls):
        self.hoveringresume=isinrect(controls.mousex,controls.mousey,self.rect_resume)
        self.hoveringrestart=isinrect(controls.mousex,controls.mousey,self.rect_restart)
        self.hoveringexit=isinrect(controls.mousex,controls.mousey,self.rect_exit)
    def update(self,controls):
        # if scene.level!=scene.titlescreen and scene.level!=scene.settingsscreen:
        self.hovers(controls)
        self.progress(controls)
        self.draw()
        self.pointer.update(controls)

##########################################################

# Object custscene for transition between scenes (empty canvas)
#*CUTSCENE
class obj_cutscene:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.name='cutscene'
        self.nextscene='overworld'#next scene that after cutscene
        self.duration=100# duration of cutscene
        self.timer=self.duration
    def update(self,controls):
        self.play()
        if self.timer>0:
            self.timer -= 1
        else:
            self.timer=self.duration
            self.creator.progresstoscene(self.nextscene)
    def play(self):# here play whatever for the duration!
        pass
# Custom cutscene 1: transition overworld to level
# uses preloaded data from overworld to make transition
class obj_cutscene1(obj_cutscene):
    def __init__(self,creator):
        super().__init__(creator)
        self.name='cutscene1'
        self.duration=100
    def play(self):
        if once('cutscene1play', self.timer==self.duration): music.change('overworldtolevel')
        pygame.draw.circle(screen, (0, 0, 0),
        (self.creator.overworld.xplayer,self.creator.overworld.yplayer), min(1000,int(1200*(1-self.timer/self.duration))), 0)
        screen.blit(self.creator.overworld.imgplayer,\
        (self.creator.overworld.xplayer-25,self.creator.overworld.yplayer-30))# must be same as on overworld

# Custom cutscene 2: transition between level parts
# uses preloaded data from overworld to make transition
class obj_cutscene2(obj_cutscene):
    def __init__(self,creator):
        super().__init__(creator)
        self.name='cutscene2'
        self.duration=70
        # Copies player head info for drawing
        # everything modified by current level before it ends and starts this cutscene
        self.imgh=False
        self.xh=400
        self.yh=300
        self.uh=0
        self.uh=0
        self.kspringh=0
        self.cdf=0
        self.rad=0
        self.holex=0
        self.holey=0
        self.imgholein=pygame.image.load('data/bk_imgholefinishgoin.png').convert_alpha()
    def play(self):
        # start of cutscene
        bsize=self.timer/self.duration
        if once('cutscene1play', self.timer==self.duration):
            sound.play('nextpart')
            self.kspringh=self.kspringh# more wiggle
            self.cdh=self.cdh/2
        # rest of loop
        screen.fill((0,0,0))
        func_drawimage(self.imgholein, (self.holex-25,screenh-self.holey-25),25,25)
        if self.timer>self.duration*0.25:
            self.uh = self.uh- self.kspringh*(self.xh-self.holex)*dt - self.cdh*self.uh*dt
            self.vh = self.vh- self.kspringh*(self.yh-self.holey)*dt - self.cdh*self.vh*dt
            self.xh += self.uh*dt
            self.yh += self.vh*dt
            func_drawimage(self.imgh, (self.xh-self.rad,screenh-self.yh-self.rad),self.rad,self.rad)# head
        # end of cutscene
        if self.timer==0:
            self.imgh=False# forget image



##########################################################


# Game TitleScreen
# *TITLESCREEN
class obj_titlescreen:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.img=pygame.image.load('data/bk_imgtitlescreen.png').convert_alpha()
        self.pointer=obj_pointersword(self)
        self.hoveringstart=False
        self.hoveringsettings=False
        self.hoveringquit=False
        self.font = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        #
        self.rect_start=(300*scsx,500*scsx,400*scsy,440*scsy)
        self.rect_settings=(300*scsx,500*scsx,450*scsy,490*scsy)
        self.rect_quit=(300*scsx,500*scsx,500*scsy,540*scsy)
    def draw(self):
        screen.blit(self.img, (0, 0))
        for i,j,k in zip([self.rect_start,self.rect_settings,self.rect_quit],\
               [self.hoveringstart,self.hoveringsettings,self.hoveringquit],\
                ['Start','Settings','Quit']):# Fullscreen options omitted for now
                idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
                func_drawtextinrect(k,self.font,(255,255,255),idec)
                func_drawtextinrect(k,self.font,self.getcolor(j),i)
    def getcolor(self,inputboolean):# return color to draw depending on True/False input
        if inputboolean:
            return (222,198,0)
        else:
            return (0,0,0)
        return()
    def gotooverworld(self,controls):
        if self.hoveringstart and (controls.mouse1 and controls.mouse1c):
            sound.play('menugo')
            self.creator.changescene('overworld',False)
    def gotosettings(self,controls):
        if self.hoveringsettings and (controls.mouse1 and controls.mouse1c):
            sound.play('menugo')
            self.creator.changescene('settings',False)
    def gotoquitgame(self,controls):
        if self.hoveringquit and (controls.mouse1 and controls.mouse1c):
            self.creator.changescene('quit',False)# quit game
    def hovers(self,controls):
        self.hoveringstart=isinrect(controls.mousex,controls.mousey,self.rect_start)
        self.hoveringsettings=isinrect(controls.mousex,controls.mousey,self.rect_settings)
        self.hoveringquit=isinrect(controls.mousex,controls.mousey,self.rect_quit)
    def debugcommands(self,controls):
        if controls.q and controls.qc: self.creator.changescene('quit',False)# quit game
    def update(self,controls):
        self.hovers(controls)
        self.gotooverworld(controls)
        self.gotosettings(controls)
        self.gotoquitgame(controls)
        self.draw()
        self.pointer.update(controls)
        if dodebug: self.debugcommands(controls)
        # if controls.esc and controls.escc: self.creator.changescene('quit',False)# quit game (safety for changes to fullscreen)



##################################################################################

# Settings (not a scene, manages read/write settings)
#*SETTINGS
class obj_settings:
    def __init__(self):
        self.settingsfile='settings/settingsfile.txt'# where settings are stored
        self.loadsettings()# load current settings
    def savesettings(self):
        if os.path.exists(self.settingsfile):
            f1=open(self.settingsfile, 'w+')
            f1.write('domusic#'+str(domusic)+'#\n')
            f1.write('dosound#'+str(dosound)+'#\n')
            f1.write('resolutionx#'+str(display.displayresolution[0])+'#\n')
            f1.write('resolutiony#'+str(display.displayresolution[1])+'#\n')
            f1.write('scalingmethod#'+str(display.scalingmethod)+'#\n')
            f1.write('displaymode#'+str(display.optionset)+'#\n')
            f1.write('doazerty#'+str(controls.doazerty)+'#\n')
            f1.close()
    def loadsettings(self):
        if os.path.exists(self.settingsfile):
            f1=open(self.settingsfile, 'r+')
            line=f1.readline()
            [_,term,_]=line.split("#")# read domusic
            changedomusic(term=='True')
            line=f1.readline()
            [_,term,_]=line.split("#")# read dosound
            changedosound(term=='True')
            line=f1.readline()
            [_,termx,_]=line.split("#")# read resolutionx
            line=f1.readline()
            [_,termy,_]=line.split("#")# read resolutiony
            display.displayresolution=(int(termx),int(termy))
            line=f1.readline()
            [_,term,_]=line.split("#")# read scaling method
            display.scalingmethod=term
            line=f1.readline()
            [_,term,_]=line.split("#")# read display mode
            display.optionset=term
            line=f1.readline()
            [_,term,_]=line.split("#")# read azerty on/off
            if term=='False': # beware we convert a string to boolean
                controls.doazerty=False
            else:
                controls.doazerty=True
            f1.close()
            #
            display.reset()# reset display to current values

# Game Settings Screen (allows to change settings)
# *SETTINGSSCREEN
class obj_settingsscreen:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.font = pygame.font.Font('data/editundo.ttf', 30)# text fonts
        self.bigfont = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        self.pointer=obj_pointersword(self)
        # Booleans for hovers
        self.hoveringreturn=False
        self.hoveringresetsave=False
        self.resetsavedone=False
        self.hoveringmusic=False
        self.hoveringsound=False
        self.h800x600=False
        self.h1200x900=False
        self.h1600x1200=False
        self.hadapted=False
        self.hscales=False
        # self.hscaless=False
        self.hscales2x=False
        self.hmodewd=False
        self.hmodefs=False
        self.hmodenf=False
        # Rectangle for each option
        self.rect_title=(250*scsx,550*scsx,25*scsy,75*scsy)
        self.rect_return=(350*scsx,450*scsx,500*scsy,575*scsy)
        self.rect_resetsave=(250*scsx,550*scsx,100*scsy,150*scsy)
        self.rect_music=(50*scsx,350*scsx,175*scsy,225*scsy)
        self.rect_sound=(450*scsx,750*scsx,175*scsy,225*scsy)
        self.rect_800x600=(20*scsx,180*scsx,250*scsy,300*scsy)
        self.rect_1200x900=(220*scsx,380*scsx,250*scsy,300*scsy)
        self.rect_1600x1200=(420*scsx,580*scsx,250*scsy,300*scsy)
        self.rect_adapted=(620*scsx,780*scsx,250*scsy,300*scsy)
        self.rect_scaleinfo=(20*scsx,180*scsx,325*scsy,375*scsy)
        self.rect_scales=(220*scsx,380*scsx,325*scsy,375*scsy)
        # self.rect_scaless=(420*scsx,580*scsx,325*scsy,375*scsy)
        self.rect_scales2x=(620*scsx,780*scsx,325*scsy,375*scsy)
        self.rect_modeinfo=(20*scsx,180*scsx,400*scsy,450*scsy)
        self.rect_modewd=(220*scsx,380*scsx,400*scsy,450*scsy)
        self.rect_modefs=(620*scsx,780*scsx,400*scsy,450*scsy)# omitted for now
        self.rect_modenf=(420*scsx,580*scsx,400*scsy,450*scsy)
    def gototitlescreen(self,controls):
        if (self.hoveringreturn and controls.mouse1 and controls.mouse1c) or (controls.esc and controls.escc):
            sound.play('menuback')
            settings.savesettings()# save settings on exit from settings screen !!!
            self.creator.changescene('titlescreen',False)
    def draw(self):
        # screen.blit(self.img, (0, 0))
        screen.fill((159,26,26))
        i=self.rect_title
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('Settings',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('Settings',self.bigfont,self.getcolor(False),self.rect_title)
        #
        i=self.rect_return
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('Back',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('Back',self.bigfont,self.getcolor(self.hoveringreturn),self.rect_return)
        #
        pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(self.rect_resetsave), 0)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_resetsave), 3)
        func_drawtextinrect('Reset Save',self.font,self.getcolor(self.hoveringresetsave),self.rect_resetsave)
        #
        pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(self.rect_music), 0)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_music), 3)
        if domusic:
            func_drawtextinrect('Music On',self.font,self.getcolor(self.hoveringmusic),self.rect_music)
        else:
            func_drawtextinrect('Music Off',self.font,self.getcolor(self.hoveringmusic),self.rect_music)
        #
        pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(self.rect_sound), 0)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_sound), 3)
        if dosound:
            func_drawtextinrect('Sound On',self.font,self.getcolor(self.hoveringsound),self.rect_sound)
        else:
            func_drawtextinrect('Sound Off',self.font,self.getcolor(self.hoveringsound),self.rect_sound)
        #
        for i,j,k in zip([self.rect_800x600,self.rect_1200x900,self.rect_1600x1200,self.rect_adapted],\
                       [self.h800x600,self.h1200x900,self.h1600x1200,self.hadapted],\
                        [str(screenw)+'x'+str(screenh)+'*','1920x1080','2560x1440','adapted']):
            pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(i), 0)
            pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(i), 3)
            func_drawtextinrect(k,self.font,self.getcolor(j),i)
        #
        func_drawtextinrect('Scaling',self.font,self.getcolor(False),self.rect_scaleinfo)
        for i,j,k in zip([self.rect_scales,self.rect_scales2x],\
                       [self.hscales,self.hscales2x],\
                        ['Regular','  2Xs']):# we removed smooth scaling=too expensive
            pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(i), 0)
            pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(i), 3)
            func_drawtextinrect(k,self.font,self.getcolor(j),i)
        #
        func_drawtextinrect('Mode',self.font,self.getcolor(False),self.rect_modeinfo)
        for i,j,k in zip([self.rect_modewd,self.rect_modenf,self.rect_modefs],\
                       [self.hmodewd,self.hmodenf,self.hmodefs],\
                        ['Windowed','Borders','Fullscreen']):# Fullscreen options omitted for now
            pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(i), 0)
            pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(i), 3)
            func_drawtextinrect(k,self.font,self.getcolor(j),i)
            #
    def getcolor(self,inputboolean):# return color to draw depending on True/False input
        if inputboolean:
            return (222,198,0)
        else:
            return (0,0,0)
        return()
    def changeresolution(self,controls):
        # note: we should impose
        if self.h800x600 and (controls.mouse1 and controls.mouse1c):
            display.displayresolution=(screenw,screenh)# not 800x600 but the native resolution
            display.reset()
        if self.h1200x900 and (controls.mouse1 and controls.mouse1c):
            display.displayresolution=(1920,1080)
            display.reset()
        if self.h1600x1200 and (controls.mouse1 and controls.mouse1c):
            display.displayresolution=(2560,1440)
            display.reset()
        if self.hadapted and (controls.mouse1 and controls.mouse1c):
            display.displayresolution=(0,0)# adapted
            display.reset()
    def changescalingmethod(self,controls):
        # note: we should impose scaling method depending on resolution:
            # 1280x720: no scaling
            # 2560x1440: always 2xs (even if adapted and dimensions match)
            # other resolutions: regular scaling s
            # (this is because 2xs looks best but only in 2560x1440, s is ok, and ss is horrible/slow)
        if self.hscales and (controls.mouse1 and controls.mouse1c):
            display.scalingmethod='s'
            display.reset()
        # if self.hscaless and (controls.mouse1 and controls.mouse1c):# removed because too expensive
        #     display.scalingmethod='ss'
        #     display.reset()
        if self.hscales2x and (controls.mouse1 and controls.mouse1c):
            display.scalingmethod='s2x'
            display.reset()
    def changedisplaymode(self,controls):
        if self.hmodewd and (controls.mouse1 and controls.mouse1c):
            display.optionset='windowed'
            display.reset()
        if self.hmodenf and (controls.mouse1 and controls.mouse1c):
            display.optionset='borders'
            display.reset()
        if self.hmodefs and (controls.mouse1 and controls.mouse1c):
            display.optionset='fullscreen'
            display.reset()
    def changemusicsound(self,controls):
        if self.hoveringmusic and controls.mouse1 and controls.mouse1c:
            if domusic:
                sound.play('menuback')
                changedomusic(False)
                music.stop()
            else:
                changedomusic(True)
                music.restart()
                sound.play('menugo')
        if self.hoveringsound and controls.mouse1 and controls.mouse1c:
            if dosound:
                sound.play('menuback')
                changedosound(False)
            else:
                changedosound(True)
                sound.play('menugo')
    def resetsavefile(self,controls):
        if self.hoveringresetsave and controls.mouse1 and controls.mouse1c:
            sound.play('erasesave')
            if not self.resetsavedone:
                self.creator.levelmanager.resetprogress()
                self.resetsavedone=True
    def hovers(self,controls):
        self.hoveringreturn=isinrect(controls.mousex,controls.mousey,self.rect_return)
        self.hoveringresetsave=isinrect(controls.mousex,controls.mousey,self.rect_resetsave)
        self.hoveringmusic=isinrect(controls.mousex,controls.mousey,self.rect_music)
        self.hoveringsound=isinrect(controls.mousex,controls.mousey,self.rect_sound)
        self.h800x600=isinrect(controls.mousex,controls.mousey,self.rect_800x600)
        self.h1200x900=isinrect(controls.mousex,controls.mousey,self.rect_1200x900)
        self.h1600x1200=isinrect(controls.mousex,controls.mousey,self.rect_1600x1200)
        self.hadapted=isinrect(controls.mousex,controls.mousey,self.rect_adapted)
        self.hscales=isinrect(controls.mousex,controls.mousey,self.rect_scales)
        # self.hscaless=isinrect(controls.mousex,controls.mousey,self.rect_scaless)
        self.hscales2x=isinrect(controls.mousex,controls.mousey,self.rect_scales2x)
        self.hmodewd=isinrect(controls.mousex,controls.mousey,self.rect_modewd)
        self.hmodefs=isinrect(controls.mousex,controls.mousey,self.rect_modefs)
        self.hmodenf=isinrect(controls.mousex,controls.mousey,self.rect_modenf)
    def debugcommands(self,controls):
        if controls.q and controls.qc: self.creator.changescene('titlescreen',False)
    def update(self,controls):
        self.hovers(controls)
        self.gototitlescreen(controls)
        self.resetsavefile(controls)
        self.draw()
        self.pointer.update(controls)
        self.changemusicsound(controls)
        self.changeresolution(controls)
        self.changescalingmethod(controls)
        self.changedisplaymode(controls)
        if dodebug: self.debugcommands(controls)

# Game Overworld
# *OVERWORLD
class obj_overworld:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.ilevel=0# index of current level hovered
        #
        self.img=pygame.image.load('data/bk_imgoverworld.png').convert_alpha()
        self.imgallleveldots=pygame.image.load('data/bk_imgoverworld_allleveldots.png').convert_alpha()
        self.imgplayer=pygame.image.load('data/bk_imgoverworld_player.png').convert_alpha()
        self.imgwon=pygame.image.load('data/bk_imgoverworld_levelwon.png').convert_alpha()
        self.imglevelinfo=pygame.image.load('data/bk_imgoverworld_levelinfo.png').convert_alpha()
        self.imgleveldot=pygame.image.load('data/bk_imgoverworld_leveldot.png').convert_alpha()
        self.medfont = pygame.font.Font('data/editundo.ttf', 20)# text fonts
        self.bigfont = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        self.hoverrad=20# radius to detect mouse is hovering on
        self.pointer=obj_pointersword(self)
        #
        self.hoveringmenu=False
        self.hoveringuserlevels=False
        self.hoveringlevel=False
        self.moveplayer=True
        self.placeplayer()#place player on map (after init)
        #
        self.rect_userlevels=(300*scsx,500*scsx,10*scsy,30*scsy)
        self.rect_return=(350*scsx,450*scsx,500*scsy,575*scsy)
        self.rect_levelinfo=(900,1200,100,300)
        self.rect_leveltitle=(900,1200,100,150)
        self.rect_levelplayershots=(900,1200,150,200)
        self.rect_levelplayertime=(900,1200,200,250)
        #
    def changelevel(self,controls):
        self.hoveringlevel=False
        for ic,i in enumerate(self.creator.levelmanager.levels):
            if (controls.mousex-i.xdot)**2+(controls.mousey-i.ydot)**2<self.hoverrad**2:
                if i.open or i.unlocked or dodebug:#
                    if once('overworlddot',self.ilevel): sound.play('overworldmove')
                    self.ilevel=ic# change current level on overworld
                    self.creator.levelmanager.ilevel=ic# also change current level in level manager
                    self.moveplayer=True
                    self.hoveringlevel=True
    def gotolevel(self,controls):# load level from file
        if not self.hoveringmenu and not self.hoveringuserlevels and self.hoveringlevel:
            if not dodebug and controls.mouse1 and controls.mouse1c: self.creator.changescene('level','cutscene1')#cutscene!
            if dodebug and controls.mouse1 and controls.mouse1c: self.creator.changescene('level',False)
    def gotouserlevels(self,controls):
        if (controls.mouse1 and controls.mouse1c and self.hoveringuserlevels):
            sound.play('menuback')
            self.creator.changescene('levelscrollbar',False)
    def gototitlescreen(self,controls):
        if (self.hoveringreturn and controls.mouse1 and controls.mouse1c) or (controls.esc and controls.escc):
            sound.play('menuback')
            settings.savesettings()# save settings on exit from settings screen !!!
            self.creator.changescene('titlescreen',False)
    def draw(self):
        screen.blit(self.img, (0, 0))# background overworld image
        if dodebug: screen.blit(self.imgallleveldots, (0, 0))# dev only, show all level dots
        # draw won levels
        for i in self.creator.levelmanager.levels:
            if i.unlocked: # level made playable by dev
                if i.won:
                    screen.blit(self.imgwon,(i.xdot-25,i.ydot-25))
                else:
                    screen.blit(self.imgleveldot,(i.xdot-15,i.ydot-15))
        # Menu transitions
        # if self.hoveringuserlevels:  screen.blit(self.imghoveringuserlevels, (0, 0))
        i=self.rect_userlevels
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('User Levels',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('User Levels',self.bigfont,self.getcolor(self.hoveringuserlevels),self.rect_userlevels)
        #
        i=self.rect_return
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('Back',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('Back',self.bigfont,self.getcolor(self.hoveringreturn),self.rect_return)
        #draw player
        screen.blit(self.imgplayer,(self.xplayer-25,self.yplayer-30))
        # draw progress on hovered levels
        if not self.hoveringuserlevels and self.hoveringlevel:
            screen.blit(self.imglevelinfo,(self.xplayer-25,self.yplayer-65))#progress on hovered level
            term=self.creator.levelmanager.levels[self.ilevel] # draw info on hovered level
            screen.blit(self.medfont.render(str(term.progress)+'/'+str(term.nlevelparts), True, (0, 0, 0)), (self.xplayer-15,self.yplayer-54))
            # Draw level infos (title, completion...)
            # pygame.draw.rect(screen, (222,198,0), rect_to_pygame_rect(self.rect_levelinfo), 0)
            # pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_levelinfo), 3)
            # func_drawtextinrect(term.levelname,self.medfont,(0,0,0),self.rect_leveltitle)
            # func_drawtextinrect('Total Shots Fired: '+str(term.playershots),self.medfont,(0,0,0),self.rect_levelplayershots)
            # func_drawtextinrect('Total Completion Time: '+\
            #                     str(floor(term.playertime/60000))+'m '+\
            #                         str(floor(term.playertime%60000/1000))+'s',\
            #                         self.medfont,(0,0,0),self.rect_levelplayertime)# time is in ms

    def getcolor(self,inputboolean):# return color to draw depending on True/False input
        if inputboolean:
            return (222,198,0)
        else:
            return (0,0,0)
        return()
    def placeplayer(self):
        if self.moveplayer:
            self.moveplayer=False
            if self.hoveringuserlevels:
                self.xplayer=270*scsx
                self.yplayer=25*scsy
            else:
                self.xplayer=self.creator.levelmanager.levels[self.ilevel].xdot
                self.yplayer=self.creator.levelmanager.levels[self.ilevel].ydot
    def hovers(self,controls):
        self.hoveringreturn=isinrect(controls.mousex,controls.mousey, self.rect_return)
        self.hoveringuserlevels=isinrect(controls.mousex,controls.mousey,self.rect_userlevels)
        if self.hoveringmenu or self.hoveringuserlevels: self.moveplayer=True
    def debugcommands(self,controls):
        if controls.q and controls.qc: self.creator.changescene('titlescreen',False)
    def update(self,controls):
        self.hovers(controls)
        self.placeplayer()
        self.changelevel(controls)
        self.gotolevel(controls)# do after changelevel
        self.gotouserlevels(controls)
        self.gototitlescreen(controls)
        self.draw()
        self.pointer.update(controls)
        if dodebug: self.debugcommands(controls)


# User Levels Scrollbar
# *SCROLLBAR
class obj_levelscrollbar:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.hoveringreturn=False
        self.hoveringplay=False
        self.hoveringedit=False
        self.hoveringnew=False
        self.hoveringdelete=False
        self.hoveringconfirmcancel=False
        self.hoveringconfirm=False
        self.hoveringcancel=False
        self.textmode=False# in text mode
        self.nametaken=False
        self.font = pygame.font.Font('data/editundo.ttf', 20)# text fonts
        self.medfont = pygame.font.Font('data/editundo.ttf', 30)# text fonts
        self.bigfont = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        self.pointer=obj_pointersword(self)
        # self.levelnames=os.listdir('./levels/customlevels')# read from folder
        self.levelnames=[]
        self.getleveldatabase()
        #
        self.rect_title=(250*scsx,550*scsx,25*scsy,75*scsy)
        self.rect_return=(350*scsx,450*scsx,500*scsy,575*scsy)
        self.rect_play=(100*scsx,200*scsx,100*scsy,150*scsy)
        self.rect_edit=(350*scsx,450*scsx,100*scsy,150*scsy)
        self.rect_new=(600*scsx,700*scsx,100*scsy,150*scsy)
        self.rect_delete=(100*scsx,200*scsx,450*scsy,500*scsy)
        self.rect_confirm=(500*scsx,600*scsx,450*scsy,500*scsy)
        self.rect_cancel=(650*scsx,750*scsx,450*scsy,500*scsy)
        self.rect_text=(100*scsx,700*scsx,150*scsy,450*scsy)
        self.rect_texttop=(100*scsx,700*scsx,150*scsy,170*scsy)
        self.rect_textmid=(100*scsx,700*scsx,190*scsy,210*scsy)
        #
    def draw(self):
        #
        screen.fill((159,26,26))
        i=self.rect_title
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('User Levels',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('User Levels',self.bigfont,self.getcolor(False),self.rect_title)
        #
        i=self.rect_return
        idec=(i[0]-3,i[1]-3,i[2]+2,i[3]+2)
        func_drawtextinrect('Back',self.bigfont,(255,255,255),idec)
        func_drawtextinrect('Back',self.bigfont,self.getcolor(self.hoveringreturn),self.rect_return)
        #
        for i,j,k in zip([self.rect_play,self.rect_edit,self.rect_new,self.rect_delete],\
                       [self.hoveringplay,self.hoveringedit,self.hoveringnew,self.hoveringdelete],\
                        ['Play','Edit','New','Delete']):
            # pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(i), 3)
            func_drawtextinrect(k,self.medfont,self.getcolor(j),i)
        #
        if self.hoveringconfirmcancel:
            func_drawtextinrect('Confirm',self.medfont,self.getcolor(self.hoveringconfirm),self.rect_confirm)
            func_drawtextinrect('Cancel',self.medfont,self.getcolor(self.hoveringcancel),self.rect_cancel)
        #
        pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(self.rect_text), 0)
        if self.textmode and controls.textmode:
            pygame.draw.rect(screen, (222,198,0), rect_to_pygame_rect(self.rect_texttop), 0)
            func_drawtextinrect('Enter New Level Name : '+controls.text,self.font,(0,0,0),self.rect_texttop)
        else:
            pygame.draw.rect(screen, (222,198,0), rect_to_pygame_rect(self.rect_textmid), 0)
            func_drawtextinrect('Scroll Levels with WASD or Arrows :',self.font,(0,0,0),self.rect_texttop)
        if self.levelnames:
            j=self.rect_textmid
            for ic,i in enumerate(self.levelnames):
                if ic<15:
                    jdec=(j[0],j[1],j[2]+ic*20,j[3]+ic*20)
                    func_drawtextinrect(i,self.font,(0,0,0),jdec)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_text), 3)
    def getcolor(self,inputboolean):# return color to draw depending on True/False input
        if inputboolean:
            return (222,198,0)
        else:
            return (0,0,0)
        return()
    def getleveldatabase(self):
        term=os.listdir('./levels/customlevels')
        for i in term:
            j=i.split("_#")
            self.levelnames.append(str(j[0]))

        if self.levelnames:
            self.levelnames=sorted(self.levelnames)# sort alphabetically
            self.creator.levelmanager.userlevelname=self.levelnames[0]# update levelmanager
    def scrolllevels(self,controls):
        if ((controls.s and controls.sc) or (controls.down and controls.downc)) and len(self.levelnames)>1:# shift list order
            self.levelnames=shiftlist_left(self.levelnames)
            self.creator.levelmanager.userlevelname=self.levelnames[0]# update levelmanager
        if ((controls.w and controls.wc) or (controls.up and controls.upc)) and len(self.levelnames)>1:# shift list order
            self.levelnames=shiftlist_right(self.levelnames)
            self.creator.levelmanager.userlevelname=self.levelnames[0]# update levelmanager
    def gotolevel(self,controls):# load level from file
        if self.hoveringplay:
            if controls.mouse1 and controls.mouse1c:
                self.creator.changescene('userlevel',False)# no cutscene
    def gotolevel_editmode(self,controls):# load level from file
        if self.hoveringedit:
            if controls.mouse1 and controls.mouse1c:
                self.creator.changescene('userleveleditor',False)# no cutscene
    def createnewlevel(self,controls):
        if self.hoveringnew and not self.textmode:
            if controls.mouse1 and controls.mouse1c:
                controls.starttextmode('')
                self.textmode=True
        if self.textmode and not controls.textmode:
            if not any(i==controls.text for i in self.levelnames):
                self.createnewlevelfile(controls.text)
                self.levelnames.append(controls.text)
                self.levelnames=shiftlist_right(self.levelnames)
                self.creator.levelmanager.userlevelname=self.levelnames[0]# update levelmanager
            else:
                self.nametaken=True
            self.textmode=False
    def checknametaken(self):
        if self.nametaken:
            pygame.draw.rect(screen, (179, 29, 29), (30*scsx, 199*scsy, 740*scsx, 20*scsy), 0)
            screen.blit(self.font.render('  Name taken ! ', True, (0, 0, 0)), (40*scsx,200*scsy))
            if timer('checknametaken',True,50):
                self.nametaken=False
                timer.reset('checknametaken')
    def createnewlevelfile(self,filename):
        f1=open('levels/customlevels/'+controls.text+'_#0.txt', 'w+')# write basic level
        f1.write('self.background=obj_background("background0",self)#background0#0#0#\n')
        f1.write('self.borders=obj_borders("borders0",self)#borders0#0#0#\n')
        f1.write('self.boundaries=obj_boundaries(25,775,25,575,25,(217, 123, 0),"bdry_0",self)#bdry_0#0#0#\n')
        f1.write('self.music="None"#nomusic#0#0#\n')
        f1.write('self.player=obj_player(202,301,self)#player#202#301#\n')
        f1.write('self.enemies.append(obj_enemy1(601,300,self))#enemy1#601#300#\n')
        f1.write('self.holesfinish.append(obj_holefinish(402,300,25,"data/bk_imgholefinish.png",self))#holefinish#402#300#\n')
        f1.write('self.holes.append(obj_hole(701,300,25,"data/bk_imghole.png",self))#hole#701#300#\n')
        f1.close()
    def deletefile(self,filename):
        if self.hoveringdelete and controls.mouse1 and controls.mouse1c: # confirm
            self.hoveringconfirmcancel=True
        if self.hoveringconfirmcancel and self.hoveringcancel and controls.mouse1 and controls.mouse1c:# cancel
            self.hoveringconfirmcancel=False
        if self.hoveringconfirmcancel and self.hoveringconfirm and controls.mouse1 and controls.mouse1c:# delete
            if len(self.levelnames)>0:
                if os.path.exists('levels/customlevels/'+self.levelnames[0]+'_#0.txt'):
                    os.remove('levels/customlevels/'+self.levelnames[0]+'_#0.txt')
                    del self.levelnames[0]
                    self.creator.levelmanager.userlevelname=self.levelnames[0]# update levelmanager
            self.hoveringconfirmcancel=False
    def gotooverworld(self,controls):
        if (controls.mouse1 and controls.mouse1c and self.hoveringreturn) or (controls.esc and controls.escc):
            sound.play('menuback')
            self.creator.changescene('overworld',False)
    def hovers(self,controls):
        self.hoveringreturn=isinrect(controls.mousex,controls.mousey, self.rect_return)
        self.hoveringplay=isinrect(controls.mousex,controls.mousey, self.rect_play)
        self.hoveringedit=isinrect(controls.mousex,controls.mousey, self.rect_edit)
        self.hoveringnew=isinrect(controls.mousex,controls.mousey, self.rect_new)
        self.hoveringdelete=isinrect(controls.mousex,controls.mousey, self.rect_delete)
        self.hoveringconfirm=isinrect(controls.mousex,controls.mousey, self.rect_confirm)
        self.hoveringcancel=isinrect(controls.mousex,controls.mousey, self.rect_cancel)
    def debugcommands(self,controls):
        if controls.q and controls.qc: self.creator.changescene('overworld',False)
    def update(self,controls):
        self.createnewlevel(controls)
        if not self.textmode and not self.nametaken: # text mode (for creating new level)
            self.hovers(controls)
            self.scrolllevels(controls)
            self.deletefile(controls)
            self.gotooverworld(controls)
            self.gotolevel(controls)
            self.gotolevel_editmode(controls)
        self.draw()
        self.checknametaken()
        self.pointer.update(controls)
        if dodebug: self.debugcommands(controls)

# Level Manager: manages progress, current part played, number of parts of each level, as well as save file
# (not a scene, doesnt display anything on screen)
# *MANAGER
class obj_levelmanager:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.levels=[]# array of levels
        self.initleveldata()# get initial data for all level (postion on overworld, prefix...)
        self.recompute_nlevelparts()# (re)compute  nlevelparts for each level (using OS)
        self.savefile='levels/savefile.txt'# save file for progress
        self.loadprogressfromfile()#
        self.recompute_wonopenlevels()
        self.ilevel=0# index of current level being used
        #
        self.userlevelname=[]# user level name (different system than original level database)
        #
    def recompute_nlevelparts(self):# determine how much extensions _#i of each file exist using the os
        for i in self.levels:
            j=0
            nparts=0
            fileexists=True
            while fileexists:
                nparts=nparts+1
                fileexists=os.path.exists('levels/'+i.levelprefix+'_#'+str(j)+'.txt')
                j=j+1
            i.nlevelparts=nparts-1#n-1 in loop
    def recompute_wonopenlevels(self):# recompute which levels are won or open
        # Determine which levels are won
        for i in self.levels:
            if i.progress >= i.nlevelparts:
                i.won=True
            else:
                i.won=False
        # Open access to levels (level is open if previous one was won)
        self.levels[0].open=True# first level always accessible
        for ic in range(1,len(self.levels)):
            if self.levels[ic-1].won == True:
                self.levels[ic].open=True
    def loadlevel(self):# these should not be called directly but by the scene manager using changescene
        term='levels/'+self.levels[self.ilevel].levelprefix+'_#'+str(self.levels[self.ilevel].levelpart)+'.txt'
        if self.levels[self.ilevel].levelpart==0:# if restarting from first level part
            self.levels[self.ilevel].playershots=0# reset player shots in level manager
            self.levels[self.ilevel].playertime=0# reset player time in level manager
        self.creator.level=obj_levelfromfile(term,self.creator)
    def loaduserlevel(self):
        if self.userlevelname:
            term='levels/customlevels/'+self.userlevelname+'_#0.txt'
            self.creator.level=obj_userlevelfromfile(term,self.creator)
    def loadlevel_editmode(self):
        self.creator.leveleditor.recompute_fileedit()
        self.creator.level=self.creator.leveleditor
        self.creator.leveleditor.readdatabase()# reload the level editor database.txt
        self.creator.leveleditor.loadcommands()
    def loaduserlevel_editmode(self):
        self.creator.userleveleditor.fileedit='customlevels/'+self.userlevelname+'_#0'
        self.creator.level=self.creator.userleveleditor
        self.creator.leveleditor.readdatabase()# reload the database
        self.creator.userleveleditor.loadcommands()
    def saveprogresstofile(self):
        f1=open(self.savefile, 'w+')
        for i in self.levels:
            f1.write(i.levelprefix+'#'+str(i.progress)+'\n')
        f1.close()
    def resetprogress(self):
        f1=open(self.savefile, 'w+')
        for i in self.levels:
            f1.write(i.levelprefix+'#0\n')
        f1.close()
        self.loadprogressfromfile()
        self.recompute_wonopenlevels()
    def loadprogressfromfile(self):
        f1=open(self.savefile, 'r+')
        line=f1.readline()
        while line:
            [termlevelprefix,termprogress]=line.split("#")
            for i in self.levels:
                if i.levelprefix==termlevelprefix and thiscanbeanint(termprogress):#matching names and integer
                    i.progress=int(termprogress)
            line=f1.readline()
        f1.close()
    def initleveldata(self):
        # Database of levels (position x,y on overworld, levelprefix )
        # Ordering gives unlock order
        self.levels.append(obj_leveldata(int(32),int(100),'level_tutorial','Tutorial',True,self))# First #Number 1
        self.levels.append(obj_leveldata(int(31),int(164),'level_woods1','Into the Woods',True,self))# woods 1
        self.levels.append(obj_leveldata(int(134),int(108),'level_woods2','TBD',True,self))# woods 2
        self.levels.append(obj_leveldata(int(241),int(140),'level_lake','Calm Lake',False,self))#lake
        self.levels.append(obj_leveldata(int(304),int(184),'level_cloud','Up in the Clouds',True,self))#cloud
        self.levels.append(obj_leveldata(int(437),int(201),'level_windmill','The Windmill',True,self))#windwill
        self.levels.append(obj_leveldata(int(509),int(183),'level_house','TBD',True,self))#house
        self.levels.append(obj_leveldata(int(564),int(150),'level_ocean1','TBD',False,self))#ocean
        self.levels.append(obj_leveldata(int(630),int(102),'level_iceberg1','Rolling on Ice',True,self))#iceberg 1
        self.levels.append(obj_leveldata(int(747),int(127),'level_iceberg2','TBD',False,self))#iceberg2      #Number 10
        self.levels.append(obj_leveldata(int(665),int(165),'level_iceberg3','TBD',False,self))#small iceberg
        self.levels.append(obj_leveldata(int(724),int(156),'level_ocean2','TBD',False,self))#ocean
        self.levels.append(obj_leveldata(int(770),int(191),'level_ocean3','TBD',False,self))#ocean
        self.levels.append(obj_leveldata(int(629),int(242),'level_lighthouse','The Lighthouse',True,self))#lighthouse
        self.levels.append(obj_leveldata(int(694),int(288),'level_shore1','TBD',False,self))#shore
        self.levels.append(obj_leveldata(int(721),int(334),'level_whale','Under the Sea',True,self))#whale
        self.levels.append(obj_leveldata(int(676),int(367),'level_shore2','TBD',False,self))#shore
        self.levels.append(obj_leveldata(int(627),int(401),'level_shore3','TBD',True,self))#shore
        self.levels.append(obj_leveldata(int(653),int(455),'level_smallisland','TBD',False,self))#small island
        self.levels.append(obj_leveldata(int(753),int(508),'level_bigisland1','Tiny Big Island',True,self))#volcano      #Number 20
        self.levels.append(obj_leveldata(int(690),int(535),'level_bigisland2','TBD',False,self))#big island
        self.levels.append(obj_leveldata(int(597),int(560),'level_pirateship','Pirate Ship',False,self))#pirate ship
        self.levels.append(obj_leveldata(int(468),int(537),'level_shore4','TBD',False,self))#beach
        self.levels.append(obj_leveldata(int(382),int(522),'level_deserttown','TBD',False,self))#desert town
        self.levels.append(obj_leveldata(int(333),int(552),'level_camel','TBD',False,self))#camel
        self.levels.append(obj_leveldata(int(275),int(485),'level_toswamp','TBD',False,self))#to swamp
        self.levels.append(obj_leveldata(int(267),int(441),'level_swamp1','TBD',False,self))#swamp 1
        self.levels.append(obj_leveldata(int(328),int(419),'level_swamp2','TBD',False,self))#swamp 2
        self.levels.append(obj_leveldata(int(417),int(386),'level_outswamp','TBD',False,self))#out of swamp    #Number 30
        self.levels.append(obj_leveldata(int(503),int(337),'level_smallcastle','TBD',False,self))#small castle
        self.levels.append(obj_leveldata(int(410),int(283),'level_woods3','TBD',False,self))# woods 3
        self.levels.append(obj_leveldata(int(335),int(295),'level_woods4','TBD',False,self))# woods 4
        self.levels.append(obj_leveldata(int(254),int(291),'level_tomountains','TBD',False,self))# to mountains
        self.levels.append(obj_leveldata(int(212),int(221),'level_mountain1','TBD',False,self))#mountain 1
        self.levels.append(obj_leveldata(int(129),int(191),'level_mountain2','TBD',False,self))#mountain 2
        self.levels.append(obj_leveldata(int(62),int(214),'level_mountain3','TBD',False,self))#mountain 3
        self.levels.append(obj_leveldata(int(92),int(249),'level_mountain4','TBD',False,self))#mountain 4
        self.levels.append(obj_leveldata(int(138),int(286),'level_mine','TBD',False,self))#mine             #Number 40
        self.levels.append(obj_leveldata(int(52),int(319),'level_woods5','TBD',False,self))# woods 5
        self.levels.append(obj_leveldata(int(108),int(407),'level_underredflag','TBD',False,self))#under red flag
        self.levels.append(obj_leveldata(int(186),int(399),'level_swamptree','TBD',False,self))#swamp tree
        self.levels.append(obj_leveldata(int(159),int(449),'level_toboss','TBD',False,self))#to boss
        self.levels.append(obj_leveldata(int(88),int(556),'level_boss','The BOOOSSS',False,self))# BOSS            #Number 45
        self.nlevels=len(self.levels)# number of levels on overworld

# Level informations stored here (number of parts, filename etc, position in overworld, etc...)
class obj_leveldata:
    def __init__(self,xdot,ydot,levelprefix,levelname,unlocked,creator):
        self.creator=creator# creator=obj_overworld
        self.xdot=xdot# position of dot on overworld
        self.ydot=ydot# position of dot on overworld
        self.levelprefix=levelprefix# prefix name
        self.levelname=levelname# level name
        self.nlevelparts=1# number of parts (is given by )
        self.levelpart=0# index of current level part if played
        self.progress=0# index of progress (current level part to be completed) on level
        self.won=False# level was finished or not
        self.open=False# level is accessible from previous ones
        self.unlocked=unlocked# Level unlocked for play (shows on overworld)
        self.playershots=0# total number of shots fired to complete (over all level parts)
        self.playertime=0# time for completion in ms (over all level parts)
        self.playershotsbest=0# best of all tries
        self.playertimebest=0# best of all tries
    def update(self):
        pass



##########################################################
#
# Level Editor
# *EDITOR
# Generates level files=sequence of python commands to be executed on level load
# these commands add level elements (player, enemies, obstacles,etc...)
class obj_leveleditor:
    def __init__(self,creator):
        self.creator=creator# creator=scene

        # Load all level editor assests from database file !!!!
        self.initleveldatafile='leveleditor/database.txt'
        self.readdatabase()# reload the database

        #
        # Compute databases lengths
        self.nparamdatabase=len(self.paramdatabase)
        self.iparamshown=0# current param shown
        self.nbackgrounddatabase=len(self.backgrounddatabase)
        self.ibackgroundshown=0# current background used
        self.nbordersdatabase=len(self.bordersdatabase)
        self.ibordersshown=0# current borders used
        self.nbdrydatabase=len(self.bdrydatabase)
        self.ibdryshown=0# current bdry used
        self.nmusicdatabase=len(self.musicdatabase)
        self.imusicshown=0# current music used
        self.actormarkers.append(len(self.actordatabase)-1)# last marker
        self.nactordatabase=len(self.actordatabase)
        #############################################3
        # Currently Edited File
        self.fileedit='defaultlevel_#0'# prefix of currently edited file
        # Categories for scrolling
        self.categorylist=['actors','parameters','background','borders','music','boundaries','text','parts','commands','instructions']
        self.icategorylist=0# current selected category
        self.ncategorylist=len(self.categorylist)
        # actors already placed
        self.actorlist=[]
        self.nactorlist=len(self.actorlist)
        # actor held by mouse
        self.iactorheld=0
        self.actorheld=self.actordatabase[self.iactorheld]# actor held by mouse
        # parameters
        self.hitsleft=999# number of shots left
        self.changingparam=False
        # load text file
        self.levelfiletext=[]# content of level text file line by line (when reading)
        self.onecommandredux=['shotsleft','0','0']# one command from file text (ALWAYS format ID,X,Y)
        self.actorread=[]# actor read from file before placing
        # displayed text during level
        self.leveltext=[]
        self.changingleveltext=False
        # Extra commands (any)
        self.extracommands=[]
        self.changingextracommands=False
        # Make/Erase Level Parts
        # grid is on or not
        self.gridon=True
        # follow mouse
        self.mousex0=0# record mouse position if starts grabbing
        self.mousey0=0
        self.xcam0=0# record xcam as well
        self.ycam0=0
        self.imagegrabscreen=pygame.image.load('data/bk_imgleveleditor_grabscreen.png').convert_alpha()
        # Misc
        self.font = pygame.font.Font('data/editundo.ttf', 20)#
        self.textfont = pygame.font.Font('data/editundo.ttf', 20)#
        self.commandfont = pygame.font.Font('data/roboto.ttf', 20)#
        self.imglocation=pygame.image.load('data/bk_imgleveleditor_location.png').convert_alpha()
        self.pointer=obj_pointerleveleditor(self)#mouse pointer
        self.screenadb=False# a huge screen to display the actor database
    def drawinstructions(self):
        term=['Instructions on how to use the Level Editor:',' ',\
          'Q : Exit           E: Play Level ( E to return )',\
          'X : Toggle Grid',' Hold Space + Mouse: Move Camera',\
          'A and D :  Scroll Categories',\
          'F and G :  Scroll Level Parts ',\
          'Hold C : Quick Pick Actor (Scroll with W-S or MouseWheel, Choose Actor with LMouse)',' ',\
          'if Category = Actor :  W and S : Scroll Actors One by One',\
          '                       MouseWheel : Quicker Scroll',\
          '                       LMouse : Place Actor',\
          '                       RMouse : Remove Actor',\
          '                       MMouse : Grab Actor',\
          'if Category = Background, Boundaries, Borders, Music :      A and D : Scroll',\
          'if Category = Parameters :    W/S Shift Lines Order     Enter/Backspace: Edit Last Line',\
          'if Category = Commands :      W/S Shift Lines Order     Enter/Backspace: Edit Last Line',\
          'if Category = Text :          Enter/Backspace: Edit Text    Space+Backspace: Erase All Text',\
          'if Category = Parts :         Create/Destroy Part/All Actors (Enter/Backspace/Space + H)',\
          'if Category = Instructions :  Displays these Instructions',' ',\
          '(Level Part is automatically saved on play, exit or scroll level part)']
        pygame.draw.rect(screen, (200, 200, 200), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 0)
        pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 3)
        for i in range(len(term)): screen.blit(self.font.render(term[i], True, (0, 0, 0)), (int(100*scsx),int((50+(i+1)*20)*scsy)))
    def recompute_fileedit(self):# recompute the current fileedit using level editor data
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        self.fileedit=term.levelprefix+'_#'+str(term.levelpart)
    def readdatabase(self):
        f1=open(self.initleveldatafile, 'r+')
        line=f1.readline()
        exec(str(line))
        while line:
            line=f1.readline()
            exec(str(line))
        f1.close()
        #
        # Find and print duplicates:
        seen = {}
        dupes = []
        for i in self.actordatabase:
            j=i.barcode
            if j not in seen:
                seen[j] = 1
            else:
                if seen[j] == 1:
                    dupes.append(j)
                seen[j] += 1
        if dupes: print('duplicates in actor database: '+str(dupes))
    def add_pdb(self,name,command,value,barcode):# add an (editable) parameter to database
        self.paramdatabase.append(obj_leveleditorparam(name,command,value,barcode,self))
    def add_bdb(self,imagename,barcode):# add a background to database
        self.backgrounddatabase.append(obj_leveleditorbackground(imagename,barcode,self))
    def add_bodb(self,borderref,barcode):# add a borders to database
        self.bordersdatabase.append(obj_leveleditorborders(borderref,barcode,self))
    def add_bdrydb(self,xmin,xmax,ymin,ymax,radius,color,barcode):# add a boundaries to database
        self.bdrydatabase.append(obj_leveleditorboundaries(xmin,xmax,ymin,ymax,radius,color,barcode,self))
    def add_mdb(self,musicname,barcode):# add a music to database
        self.musicdatabase.append(obj_leveleditormusic(musicname,barcode,self))
    def add_adb(self,image,radx,rady,command,barcode):# add an actor to database
        self.actordatabase.append(obj_leveleditoractor(image,radx,rady,command,barcode,self))
    def drawinfos(self):
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        pygame.draw.rect(screen, (0, 0, 0), (22*scsx, 5*scsy, 120*scsx, 15*scsy), 0)
        screen.blit(self.font.render('Part: ', True, (150, 150, 150)), (int(27*scsx),int(6*scsy)))
        screen.blit(self.font.render(str(term.levelpart+1)+' / '+str(term.nlevelparts), True, (255, 255, 255)), (int(77*scsx),int(6*scsy)))
        pygame.draw.rect(screen, (0, 0, 0), (197*scsx, 5*scsy, 210*scsx, 15*scsy), 0)
        screen.blit(self.font.render('Current Category: ', True, (150, 150, 150)), (int(202*scsx),int(6*scsy)))
        screen.blit(self.font.render(str(self.categorylist[self.icategorylist]), True, (255, 255, 255)), (int(327*scsx),int(6*scsy)))
        #
        for ic,i in enumerate(self.categorylist):
            pygame.draw.rect(screen, (0, 0, 0), ((2+ic*80)*scsx, 25*scsy, 75*scsx, 15*scsy), 0)
            if ic==self.icategorylist:
                screen.blit(self.font.render(i, True, (255, 255, 255)), (int((2+ic*80+1)*scsx),int(26*scsy)))
            else:
                screen.blit(self.font.render(i, True, (150, 150, 150)), (int((2+ic*80+1)*scsx),int(26*scsy)))
        #
        if  self.categorylist[self.icategorylist]=='actors':
            pygame.draw.rect(screen, (0, 0, 0), (497*scsx, 5*scsy, 210*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Actor Held: ', True, (150, 150, 150)), (502*scsx,6*scsy))
            if self.actorheld: screen.blit(self.font.render(str(self.actorheld.barcode), True, (255, 255, 255)), (592*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='background':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current background: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.backgrounddatabase:
                screen.blit(self.font.render(self.backgrounddatabase[self.ibackgroundshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='boundaries':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current boundaries: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.bdrydatabase:
                screen.blit(self.font.render(self.bdrydatabase[self.ibdryshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='borders':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current border: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.bordersdatabase:
                screen.blit(self.font.render(self.bordersdatabase[self.ibordersshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='music':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current Music: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.musicdatabase:
                screen.blit(self.font.render(self.musicdatabase[self.imusicshown].musicname, True, (255, 255, 255)), (552*scsx,6*scsy))
        #
        pygame.draw.rect(screen, (0, 0, 0), (22*scsx, 580*scsy, 250*scsx, 15*scsy), 0)
        screen.blit(self.font.render('File: ', True, (150, 150, 150)), (27*scsx,581*scsy))
        screen.blit(self.font.render(str(self.fileedit)+'.txt', True, (255, 255, 255)), (77*scsx,581*scsy))
        #
        # Show mouse in increments of the 800x600 screens
        pygame.draw.rect(screen, (0, 0, 0), (497*scsx, 580*scsy, 210*scsx, 15*scsy), 0)
        screen.blit(self.font.render('Mouse: ', True, (150, 150, 150)), (502*scsx,581*scsy))
        termx=round( (controls.mousex+xcam)/screenw, 1 )
        termy=round( (screenh-controls.mousey-ycam)/screenh, 1 )
        screen.blit(self.font.render('x = '+str(termx)+' , y = '+str(termy), True, (255, 255, 255)), (552*scsx,581*scsy))
    def changelevelpart(self,controls):# change level part (save commands, change part, load commands)
        # Note: doesnt use the scene manager changescene (faster)
        if controls.g and controls.gc:
            self.savecommands()
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
            # self.creator.levelmanager.levels[self.creator.levelmanager.ilevel].levelpart=min(term.levelpart+1,term.nlevelparts-1)
            term.levelpart=min(term.levelpart+1,term.nlevelparts-1)
            self.creator.changescene('leveleditor',False)# DO NOT USE CHANGE SCENE, DOES NOT LOAD PROPERLY!!!
        if controls.f and controls.fc:
            self.savecommands()
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]
            # self.creator.levelmanager.levels[self.creator.levelmanager.ilevel].levelpart=max(term.levelpart-1,0)
            term.levelpart=max(term.levelpart-1,0)
            self.creator.changescene('leveleditor',False)
    def changecategory(self,controls):
        if (controls.d and controls.dc) or (controls.right and controls.rightc):
            self.icategorylist=min(self.icategorylist+1,self.ncategorylist-1)
        if (controls.a and controls.ac) or (controls.left and controls.leftc):
            self.icategorylist=max(self.icategorylist-1,0)
        if (not controls.d and controls.dc) or (not controls.right and controls.rightc):# fast scroll when hold key
            timer.reset('changecategory_r')
        if (controls.d or controls.right) and timer('changecategory_r',True,20):
            if timer('changecategory_rs',True,4):
                timer.reset('changecategory_rs')
                self.icategorylist=min(self.icategorylist+1,self.ncategorylist-1)
        if (not controls.a and controls.ac) or (not controls.left and controls.leftc): # fast scroll when hold key
            timer.reset('changecategory_l')
        if (controls.a or controls.left) and timer('changecategory_l',True,20):
            if timer('changecategory_ls',True,4):
                timer.reset('changecategory_ls')
                self.icategorylist=max(self.icategorylist-1,0)
    def changebackgroundshown(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc): self.ibackgroundshown=min(self.ibackgroundshown+1,self.nbackgrounddatabase-1)
        if (controls.w and controls.wc) or (controls.up and controls.upc): self.ibackgroundshown=max(self.ibackgroundshown-1,0)
    def drawbackground(self):
        self.backgrounddatabase[self.ibackgroundshown].draw()
    def changebordersshown(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc): self.ibordersshown=min(self.ibordersshown+1,self.nbordersdatabase-1)
        if (controls.w and controls.wc) or (controls.up and controls.upc): self.ibordersshown=max(self.ibordersshown-1,0)
    def drawborders(self):
        self.bordersdatabase[self.ibordersshown].draw()
    def changebdryshown(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc): self.ibdryshown=min(self.ibdryshown+1,self.nbdrydatabase-1)
        if (controls.w and controls.wc) or (controls.up and controls.upc): self.ibdryshown=max(self.ibdryshown-1,0)
    def drawbdry(self):
        self.bdrydatabase[self.ibdryshown].color=self.bordersdatabase[self.ibordersshown].bordercolor#change to current color of borders
        self.bdrydatabase[self.ibdryshown].draw()
    def changemusicshown(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            self.imusicshown=min(self.imusicshown+1,self.nmusicdatabase-1)
            music.change(self.musicdatabase[self.imusicshown].musicname)
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            self.imusicshown=max(self.imusicshown-1,0)
            music.change(self.musicdatabase[self.imusicshown].musicname)
    def changeactorheld(self,controls):
        if controls.mouse5c: self.iactorheld=min(self.iactorheld+8,self.nactordatabase-1)
        if controls.mouse4c: self.iactorheld=max(self.iactorheld-8,0)
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            self.iactorheld=min(self.iactorheld+1,self.nactordatabase-1)
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            self.iactorheld=max(self.iactorheld-1,0)
        self.actorheld=self.actordatabase[self.iactorheld]# actor held by mouse
    def changeparameters(self,controls):
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            if not self.changingparam and len(self.paramdatabase)>1:# shift list order
                 self.paramdatabase=shiftlist_right(self.paramdatabase)
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            if not self.changingparam and len(self.paramdatabase)>1:# shift list order
                 self.paramdatabase=shiftlist_left(self.paramdatabase)
        if (not controls.w and controls.wc) or (not controls.up and controls.upc):# fast scroll when hold key
            timer.reset('changeparam_u')
        if (controls.w or controls.up) and timer('changeparam_u',True,20):
            if timer('changeparam_us',True,2):
                timer.reset('changeparam_us')
                if not self.changingparam and len(self.paramdatabase)>1:
                     self.paramdatabase=shiftlist_right(self.paramdatabase)
        if (not controls.s and controls.sc) or (not controls.down and controls.downc):# fast scroll when hold key
            timer.reset('changeparam_d')
        if (controls.s or controls.down) and timer('changeparam_d',True,20):
            if timer('changeparam_ds',True,2):
                timer.reset('changeparam_ds')
                if not self.changingparam and len(self.paramdatabase)>1:
                     self.paramdatabase=shiftlist_left(self.paramdatabase)
        if controls.backspace and controls.backspacec and not self.changingparam:# start editing
            if controls.space:# reset all parameters to default
                for i in self.paramdatabase: i.newvalue=i.value
            else:
                controls.starttextmode('')# START CONTROL TEXT MODE
                self.changingparam=True
        if self.changingparam:
            self.paramdatabase[0].newvalue=controls.text
            if not controls.textmode:# once has exited input of text
                self.changingparam=False
                if self.paramdatabase[0].newvalue=='':# if nothing , reset to default value
                    self.paramdatabase[0].newvalue=self.paramdatabase[0].value
                if self.paramdatabase[0].value=='False' and self.paramdatabase[0].newvalue !='True':# conserve booleans
                    self.paramdatabase[0].newvalue=self.paramdatabase[0].value
                if self.paramdatabase[0].value=='True' and self.paramdatabase[0].newvalue !='False':# conserve booleans
                    self.paramdatabase[0].newvalue=self.paramdatabase[0].value
                if thiscanbeafloat(self.paramdatabase[0].value) and not thiscanbeafloat(self.paramdatabase[0].newvalue):# conserve numbers
                    self.paramdatabase[0].newvalue=self.paramdatabase[0].value
    def drawparameters(self):
        if self.paramdatabase:
            # restrict drawing to length 23
            pygame.draw.rect(screen, (200, 200, 200), (30*scsx, 49*scsy, 740*scsx, 25*20*scsy), 0)
            pygame.draw.rect(screen, (255, 255, 255), (30*scsx, (49)*scsy, 740*scsx, 20*scsy ), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, 25*20*scsy), 3)
            noff=10# offset
            pygame.draw.rect(screen, (255, 255, 255), (30*scsx, (49+40+noff*20)*scsy, 740*scsx, 20*scsy ), 0)
            if controls.space and not self.changingparam: pygame.draw.rect(screen, (179, 29, 29), (30*scsx, (49)*scsy, 740*scsx, 20*scsy ), 0)
            for ic,i in enumerate(self.paramdatabase):
                if ic<22-noff:# beggining of list from middle to bottom of scren
                    if i.value ==i.newvalue:
                        screen.blit(self.commandfont.render(i.name+' '+i.newvalue, True, (0, 0, 0)), (40*scsx,(50+(ic+2+noff)*20)*scsy))
                    else:
                        screen.blit(self.commandfont.render(i.name+' '+i.newvalue, True, (179, 29, 29)), (40*scsx,(50+(ic+2+noff)*20)*scsy))
                if ic>len(self.paramdatabase)-1-noff:# end of list from top to middle of screen
                    ic2=ic-(len(self.paramdatabase)-1-noff)+1
                    if i.value ==i.newvalue:
                        screen.blit(self.commandfont.render(i.name+' '+i.newvalue, True, (0, 0, 0)), (40*scsx,(50+(ic2)*20)*scsy))
                    else:
                        screen.blit(self.commandfont.render(i.name+' '+i.newvalue, True, (179, 29, 29)), (40*scsx,(50+(ic2)*20)*scsy))
        else:
            pygame.draw.rect(screen, (200, 200, 200), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 3)
        screen.blit(self.commandfont.render(\
                                            'Scroll with A-D    Return: Start Edit    Enter: End Edit    Fill Blank: Reset    Space+Backspace: Reset All'\
                                                , True, (0, 0, 0)), (40*scsx,50*scsy))
    def changegridon(self):
        if not self.gridon:
            self.gridon=True
        else:
            self.gridon=False
    def drawgrid(self):
        if self.gridon:
            for i in range(1,int(screenw/40)+1):
                xdraw=(i*40)-xcam%40
                pygame.draw.line(screen,(0,0,0), (xdraw,0),(xdraw,screenh), 1)
            for i in range(1,int(screenw/160)+1):
                xdraw=(i*160)-xcam%160
                pygame.draw.line(screen,(0,0,0), (xdraw,0),(xdraw,screenh), 3)
            for i in range(1,int(screenw/640)+1):
                xdraw=(i*640)-xcam%640
                pygame.draw.line(screen,(0,0,0), (xdraw,0),(xdraw,screenh),5)
            for i in range(1,int(screenw/1280)+1):
                xdraw=(i*1280)-xcam%1280
                pygame.draw.line(screen,(0,0,0), (xdraw,0),(xdraw,screenh),9)
            for j in range(1,int(screenh/40)+1):
                ydraw=(j*40)-ycam%40
                pygame.draw.line(screen,(0,0,0), (0,ydraw),(screenw,ydraw), 1)
            for j in range(1,int(screenh/120)+1):
                ydraw=(j*120)-ycam%120
                pygame.draw.line(screen,(0,0,0), (0,ydraw),(screenw,ydraw), 3)
            for j in range(1,int(screenh/360)+1):
                ydraw=(j*360)-ycam%360
                pygame.draw.line(screen,(0,0,0), (0,ydraw),(screenw,ydraw), 5)
            for j in range(1,int(screenh/720)+1):
                ydraw=(j*720)-ycam%720
                pygame.draw.line(screen,(0,0,0), (0,ydraw),(screenw,ydraw), 9)
    def changexcamycam(self,controls):# follow mouse when it hovers near borders
        if controls.space and controls.spacec:
            [self.mousex0,self.mousey0,self.xcam0,self.ycam0]=[controls.mousex,controls.mousey,xcam,ycam]
        if controls.space:
            changexcam(self.xcam0-max(min(controls.mousex-self.mousex0,screenw-self.mousex0),0-self.mousex0))
            changeycam(self.ycam0-max(min(controls.mousey-self.mousey0,screenh-self.mousey0),0-self.mousey0))
            screen.blit(self.imagegrabscreen,(self.mousex0-25+self.xcam0-xcam,self.mousey0-25+self.ycam0-ycam))
    def changeleveltext(self,controls):
        if controls.enter and controls.enterc and not self.changingleveltext:# add new line -enter edit mode
            self.leveltext.append('')
            controls.starttextmode('')# start text mode from no string
            self.changingleveltext=True
        if controls.backspace and controls.backspacec and not self.changingleveltext and len(self.leveltext)>0:
            if controls.space:
                self.leveltext=[]# erase all text
            else:
                controls.starttextmode(self.leveltext[-1])# start text mode controls inputs editing last line
                self.changingleveltext=True# edit last line
        if self.changingleveltext:# edit last line
            self.leveltext[-1]=controls.text
            if not controls.textmode:
                self.changingleveltext=False
                if self.leveltext[-1]=='': del self.leveltext[-1]# Remove last line if empty
    def drawleveltext(self):
        if self.leveltext:
            pygame.draw.rect(screen, (200, 200,200), (30*scsx, 49*scsy, 740*scsx, (len(self.leveltext)+4)*20*scsy), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, (len(self.leveltext)+4)*20*scsy), 3)
        else:
            pygame.draw.rect(screen, (200, 200,200), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 3)
        if controls.space and not self.changingleveltext: pygame.draw.rect(screen, (179, 29, 29), (30*scsx, (49+20)*scsy, 740*scsx, 20*scsy ), 0)
        screen.blit(self.textfont.render(\
                                         'Enter: Edit New Line   Backspace: Edit Last Line (Enter Again to Finish Edit)   Space+Backspace: Erase All Text',\
                                             True, (0, 0, 0)), (40*scsx,70*scsy))
        if self.leveltext:
            if self.changingleveltext: pygame.draw.rect(screen, (255, 255, 255), (30*scsx, (49+(len(self.leveltext)+2)*20)*scsy, 740*scsx, 20*scsy ), 0)
            for i in range(len(self.leveltext)): screen.blit(self.textfont.render(self.leveltext[i], True, (0, 0, 0)), (40*scsx,(50+(i+3)*20)*scsy))
            if not self.changingleveltext: screen.blit(self.textfont.render('...', True, (255, 255, 255)), (40*scsx, (50+(len(self.leveltext)+3)*20)*scsy))


    def changeextracommands(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc):
            if not self.changingextracommands and len(self.extracommands)>1:# shift list order
                self.extracommands=shiftlist_right(self.extracommands)
        if (controls.w and controls.wc) or (controls.up and controls.upc):
            if not self.changingextracommands and len(self.extracommands)>1:# shift list order
                self.extracommands=shiftlist_left(self.extracommands)
        if controls.enter and controls.enterc and not self.changingextracommands:# add new line -enter edit mode
            self.extracommands.append('')
            controls.starttextmode('')# start text mode from no string
            self.changingextracommands=True
        if controls.backspace and controls.backspacec and not self.changingextracommands and len(self.extracommands)>0:# last line -enter edit mode
            controls.starttextmode(self.extracommands[-1])# start text mode controls inputs editing last line
            self.changingextracommands=True
        if self.changingextracommands:# edit last line
            self.extracommands[-1]=controls.text
            if not controls.textmode:
                self.changingextracommands=False
                if self.extracommands[-1]=='': del self.extracommands[-1]# Remove last line if empty
    def drawextracommands(self):
        if self.extracommands:
            pygame.draw.rect(screen, (172, 172, 172), (30*scsx, 49*scsy, 740*scsx, (len(self.extracommands)+2)*20*scsy), 0)
            if self.changingextracommands: pygame.draw.rect(screen, (255, 255, 255), (30*scsx, (49+(len(self.extracommands))*20)*scsy, 740*scsx, 20*scsy ), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, (len(self.extracommands)+2)*20*scsy), 3)
            for i in range(len(self.extracommands)): screen.blit(self.commandfont.render(self.extracommands[i], True, (0, 0, 0)), (40*scsx,(50+(i+1)*20)*scsy))
            if not self.changingextracommands: screen.blit(self.font.render('...', True, (255, 255, 255)), (40*scsx, (50+(len(self.extracommands)+1)*20)*scsy ))
        else:
            pygame.draw.rect(screen, (172, 172, 172), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 0)
            pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, 3*20*scsy), 3)
            screen.blit(self.commandfont.render('...', True, (255, 255, 255)), (40*scsx,70*scsy))
    def createdestroylevelparts(self,controls):# create new level part at the end
        # Prompt/confirmation screen
        term=['Hold H, Press Enter: Create New Level Part',\
              'Hold H, Press Backspace: Erase Current Level Part',\
                  'Hold H, Press Space: Reset level to Default']
        pygame.draw.rect(screen, (179, 29, 29), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 0)
        pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 3)
        if controls.h: pygame.draw.rect(screen, (255, 255, 255), (30*scsx, (49+20)*scsy, 740*scsx, 60*scsy), 0)
        for i in range(len(term)): screen.blit(self.font.render(term[i], True, (0, 0, 0)), (40*scsx,(50+(i+1)*20)*scsy))
        # Remove all actors, reset to first background/borders/musc. Erase all Parameters and extracommands
        if controls.space and controls.spacec and controls.h:
                self.removeall()
                self.ibackgroundshown=0
                self.ibordersshown=0
                self.ibdryshown=0
                self.imusicshown=0
                for i in self.paramdatabase: i.newvalue=i.value
        # Create new level part on longpress of Enter
        if controls.enter and controls.enterc and controls.h:
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
            if term.levelpart==term.nlevelparts-1:# on last part, append new at nparts+1
                self.savecommands()# save current commands to current level
                term.nlevelparts=term.nlevelparts+1# n -> n+1
                term.levelpart=term.nlevelparts-1# i->last part n-1
                self.recompute_fileedit()
                f1=open('levels/'+self.fileedit+'.txt', 'w+')# create new empty file at i
                f1.close()
                self.creator.levelmanager.recompute_nlevelparts()# recompute level parts from files
                self.savecommands()# save current commands to newly created level part
                self.creator.changescene('leveleditor',False)
                # self.loadcommands()# load commands for new file
                # changexcam(0)# reset camera
                # changeycam(0)
            else:# not last part: swap following level parts filenames and append new here
                self.savecommands()# save current commands to current level
                for i in reversed(range(term.levelpart+1,term.nlevelparts)):# swap next level file names
                    oldname='levels/'+term.levelprefix+'_#'+str(i)+'.txt'
                    newname='levels/'+term.levelprefix+'_#'+str(i+1)+'.txt'
                    os.rename(oldname,newname)
                term.nlevelparts=term.nlevelparts+1# n -> n+1
                term.levelpart=term.levelpart+1# i->i+1
                self.recompute_fileedit()
                f1=open('levels/'+self.fileedit+'.txt', 'w+')# create new empty file at i+1
                f1.close()
                self.creator.levelmanager.recompute_nlevelparts()# recompute level parts from files
                self.savecommands()# save current commands to newly created level part
                self.creator.changescene('leveleditor',False)
                # self.loadcommands()# load commands for new file
                # changexcam(0)# reset camera
                # changeycam(0)
        # Destroy new level part on confirm
        if controls.backspace and controls.backspacec and controls.h:
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
            if term.nlevelparts>1:#Only if more than 1 level part
                self.recompute_fileedit()
                os.remove('levels/'+self.fileedit+'.txt')# remove current
                if term.levelpart != term.nlevelparts-1:# if not last file
                    for i in range(term.levelpart+1,term.nlevelparts):# swap next level file names
                        oldname='levels/'+term.levelprefix+'_#'+str(i)+'.txt'
                        newname='levels/'+term.levelprefix+'_#'+str(i-1)+'.txt'
                        os.rename(oldname,newname)
                term.nlevelparts=term.nlevelparts-1#n->n-1
                if term.levelpart==term.nlevelparts: # if deteled last part, must change current part to i-1
                    term.levelpart=term.nlevelparts-1
                self.creator.levelmanager.recompute_nlevelparts()# recompute level parts from files
                self.recompute_fileedit()# load closest level
                self.creator.changescene('leveleditor',False)
                # self.loadcommands()
                # changexcam(0)# reset camera
                # changeycam(0)
    def add_actor(self,actor):
        self.actorlist.append(actor)
        self.nactorlist=len(self.actorlist)
    def remove_actor(self,actor):
        try:
            self.actorlist.remove(actor)
        except ValueError:
            pass
        self.nactorlist=len(self.actorlist)
    def drawactors(self):# draw actors  that have been placed
        if self.nactorlist>0:
            for i1 in self.actorlist: i1.draw()
    def drawlocations(self):# draw little cross on top of actors
        if self.nactorlist>0:
            for i1 in self.actorlist:
                func_drawimage(self.imglocation,(i1.x-5-xcam,screenh-i1.y-5-ycam),5,5)
    def drawactorheld(self,controls):# draw actor held by mouse
        self.actorheld.x=controls.mousex+xcam
        self.actorheld.y=screenh-controls.mousey-ycam
        self.actorheld.draw()
        #
    def drawactordatabase(self,controls):# draw actor database to quick pick
        if once('leveleditordrawdatabase',self):
            self.screenadb = pygame.Surface((3200,1800))# 2.5 times as big!
        for ic,i in enumerate(self.categorylist):# switch back to category actors
            if i=='actors': self.icategorylist=ic
        # Draw on a screenadb twice as large then scale it to existing screen
        self.screenadb.fill((230,230,230))
        # draw actorheld on it centered
        self.actorheld.x=400
        self.actorheld.y=300
        imin=self.iactorheld-19
        imax=min(max(0,self.iactorheld+48),self.nactordatabase)
        intervalx=400
        intervaly=400
        perline=8
        i=0
        j=0
        for a in range(imin,imax):
            if a>=0:
                adisp=self.actordatabase[a]
                xdiff=intervalx*i+200
                ydiff=intervaly*j+200
                if adisp.radx<=200 and adisp.rady<=200:# each actor has 400x400 square to draw itself
                    self.screenadb.blit(adisp.img,(xdiff-adisp.radx,ydiff-adisp.rady))# draw it fully
                elif adisp.rady<=200:# only x is too large
                    self.screenadb.blit(adisp.img,(xdiff-200,ydiff-adisp.rady), (0,0,400,2*adisp.rady))# limit part drawn
                elif adisp.radx<=200:# only y is too large
                    self.screenadb.blit(adisp.img,(xdiff-adisp.radx,ydiff-200), (0,0,2*adisp.radx,400))# limit part drawn
                else:
                    self.screenadb.blit(adisp.img,(xdiff-200,ydiff-200), (0,0,400,400))# limit part drawn
                if a==self.iactorheld:
                    pygame.draw.rect(self.screenadb, (0, 0, 0), (xdiff-200, ydiff-200, 400, 400), 8)
                if (controls.mousex-xdiff/4)**2+(controls.mousey-ydiff/4)**2<50**2:
                    pygame.draw.rect(self.screenadb, (255, 0, 0), (xdiff-200, ydiff-200, 400, 400), 8)
                    if controls.mouse1 and controls.mouse1c:
                        self.iactorheld=a
                        self.actorheld=self.actordatabase[self.iactorheld]
            i +=1
            if i==perline:
                i = 0
                j += 1
        pygame.transform.scale(self.screenadb, (screenw, screenh), screen)# scale and draw to screen
    def placeactor(self,controls):
        if controls.mouse1 and controls.mouse1c:
            self.add_actor(obj_leveleditoractor(self.actorheld.imgname,self.actorheld.radx,self.actorheld.rady,self.actorheld.command,self.actorheld.barcode,self))
            self.actorlist[-1].x=controls.mousex+xcam
            self.actorlist[-1].y=screenh-controls.mousey-ycam
    def destroyactor(self,controls):# removed to be able to change explore screen
        if controls.mouse2 and controls.mouse2c:
            if self.nactorlist>0:
                for i1 in self.actorlist:
                    if abs(i1.x-controls.mousex-xcam)<20 and abs(i1.y-screenh+controls.mousey+ycam)<10:
                        self.remove_actor(i1)
    def grabactor(self,controls):
       if controls.mouse3 and controls.mouse3c:
           if self.nactorlist>0:
               for i1 in self.actorlist:
                   if abs(i1.x-controls.mousex-xcam)<20 and abs(i1.y-screenh+controls.mousey+ycam)<10:
                       for j,value in enumerate(self.actordatabase):# search back for actor in database
                           if str(value.barcode)==i1.barcode:# if match
                               self.iactorheld=j
                               self.remove_actor(i1)
    def destroyplayerduplicates(self):# remove any player duplicates in the actors
        if self.nactorlist>0:
            playersfound=[]
            for i1 in self.actorlist:
                if i1.barcode=='player' or i1.barcode=='playersmall':# check if barcode is one of player
                    playersfound.append(i1)
            nplayersfound=len(playersfound)
            if nplayersfound>1:
                for count, i1 in enumerate(playersfound):
                    if count<nplayersfound-1: self.remove_actor(i1)
    def destroycameraduplicates(self):# remove any camera duplicates in the actors
        if self.nactorlist>0:
            playersfound=[]
            for i1 in self.actorlist:
                if i1.barcode=='camera':# check if barcode is one of player
                    playersfound.append(i1)
            nplayersfound=len(playersfound)
            if nplayersfound>1:
                for count, i1 in enumerate(playersfound):
                    if count<nplayersfound-1: self.remove_actor(i1)
    def removeall(self): # CRUCIAL TO REMOVE ALL OR WILL WRITE DUPLICATES IN FILES!
        self.actorlist=[]
        self.levelfiletext=[]
        self.leveltext=[]# reset level text
        self.extracommands=[]
        self.hitsleft=999
    def savecommands_checkfile(self):# keep, is modified for user level editor
        pass
    def savecommands(self):# print command that generate level objects into text file (with #ID#X#Y# comment systematically!!)
        self.savecommands_checkfile()# keep, is modified for user level editor
        f1=open('levels/'+self.fileedit+'.txt', 'w+')
        if self.paramdatabase:
            for i in self.paramdatabase:# write parameters
                f1.write(i.command+i.newvalue+'#'+i.barcode+'#'+i.newvalue+'#0#\n')
        # f1.write('self.hitsleft='+str(self.hitsleft)+'#shotsleft#'+str(self.hitsleft)+'#0#\n')# Write Shots Left
        f1.write('self.background=obj_background("'\
                 +str(self.backgrounddatabase[self.ibackgroundshown].imagename)+'",self)'+'#'\
                 +str(self.backgrounddatabase[self.ibackgroundshown].barcode)+'#0#0#\n')# write background
        f1.write('self.borders=obj_borders("'\
                 +str(self.bordersdatabase[self.ibordersshown].borderref)+'",self)'+'#'\
                 +str(self.bordersdatabase[self.ibordersshown].barcode)+'#0#0#\n')# write borders
        f1.write('self.boundaries=obj_boundaries('\
                 +str(self.bdrydatabase[self.ibdryshown].command)+',self)'+'#'\
                 +str(self.bdrydatabase[self.ibdryshown].barcode)+'#0#0#\n')# write bdry
        f1.write('self.music="'\
         +str(self.musicdatabase[self.imusicshown].musicname)+'"#'\
         +str(self.musicdatabase[self.imusicshown].barcode)+'#0#0#\n')# write music
        f1.write('music.change(self.music)#musicchange#0#0#\n')# change level music
        if self.nactorlist>0:# Write actors
            for i1 in self.actorlist:
                f1.write(i1.command.replace("INX",str(int(i1.x))).replace("INY",str(int(i1.y)))+'#'+str(i1.barcode)+'#'+str(int(i1.x))+'#'+str(int(i1.y))+'#\n')
        if self.leveltext:
            for i,value in enumerate(self.leveltext):
                f1.write('self.text.append("'+value+'")#text#0#0#\n')
        if self.extracommands:
            for i,value in enumerate(self.extracommands):
                f1.write(value+'#extracommands#0#0#\n')
        f1.close()
    def loadcommands_checkfile(self):# keep, is modified for user level editor
        pass
    def loadcommands(self):# reset placed actors and load from text file
        self.removeall()# very important!
        # read
        self.loadcommands_checkfile()# keep, is modified for user level editor
        f1=open('levels/'+self.fileedit+'.txt', 'r+')
        line=f1.readline()
        self.levelfiletext.append(line)
        while line:
            line=f1.readline()
            self.levelfiletext.append(line)
        f1.close()
        # interpret each line
        for line in self.levelfiletext:
            line=line.split("#")
            if len(line)>=4:
                self.onecommandredux=line[0:4]# reduced command
                self.placefromcommandredux()# place actor from commandredux
    def placefromcommandredux(self):
        # if command is a parameter # change existing value
        for i in self.paramdatabase:
            if str(i.barcode)==self.onecommandredux[1]:
                i.newvalue=self.onecommandredux[2]
        # if command is a background
        for i,value in enumerate(self.backgrounddatabase):
            if str(value.barcode)==self.onecommandredux[1]:
                self.ibackgroundshown=i
        # if command is a borders
        for i,value in enumerate(self.bordersdatabase):
            if str(value.barcode)==self.onecommandredux[1]:
                self.ibordersshown=i
        # if command is a bdry
        for i,value in enumerate(self.bdrydatabase):
            if str(value.barcode)==self.onecommandredux[1]:
                self.ibdryshown=i
        # if command is a music
        for i,value in enumerate(self.musicdatabase):
            if str(value.barcode)==self.onecommandredux[1]:
                self.imusicshown=i
                music.change(self.musicdatabase[self.imusicshown].musicname)
        # if command is an actor
        for i,value in enumerate(self.actordatabase):
            if str(value.barcode)==self.onecommandredux[1]:
                self.actorread=self.actordatabase[i]
                self.add_actor(obj_leveleditoractor(self.actorread.imgname,self.actorread.radx,self.actorread.rady,self.actorread.command,self.actorread.barcode,self))
                self.actorlist[-1].x=int(self.onecommandredux[2])
                self.actorlist[-1].y=int(self.onecommandredux[3])
        # if command is a text
        if self.onecommandredux[1]=='text':
            term=self.onecommandredux[0].split('"')# we assume text is within "" so we extract using this delimiter
            self.leveltext.append(term[1])
        # if command is an extra command
        if self.onecommandredux[1]=='extracommands':
            term=self.onecommandredux[0]# we assume text is within "" so we extract using this delimiter
            self.extracommands.append(term)
    def playlevel(self):# switch to play level (current part)
        self.savecommands()# save to current file
        self.creator.changescene('level',False)
        # self.creator.level=obj_levelfromfile('levels/'+self.fileedit+'.txt',self.creator)
    def exittooverworld(self):# exit to overworld ()
        self.savecommands()# save current commands
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        term.levelpart=0# reset to first part
        self.creator.changescene('overworld',False)
    def update_editorview(self,controls):
        # Update order matters for displaying objects on top of others
        self.drawbackground()
        self.changecategory(controls)
        self.changelevelpart(controls)
        self.drawactors()
        if self.categorylist[self.icategorylist]=='actors':# actor
            self.drawactorheld(controls)
            self.changeactorheld(controls)
            self.placeactor(controls)
            self.destroyactor(controls)
            self.grabactor(controls)
        if self.categorylist[self.icategorylist]=='background':# backgound
            self.changebackgroundshown(controls)
        if self.categorylist[self.icategorylist]=='borders':# borders
            self.changebordersshown(controls)
        if self.categorylist[self.icategorylist]=='boundaries':# boundaries
            self.changebdryshown(controls)
        if self.categorylist[self.icategorylist]=='music':# music
            self.changemusicshown(controls)
        self.drawgrid()
        self.drawborders()
        self.drawbdry()
        self.drawlocations()
        self.drawinfos()
        if self.categorylist[self.icategorylist]=='parameters':# parameters
            self.changeparameters(controls)
            self.drawparameters()
        if self.categorylist[self.icategorylist]=='commands':# change extra commands
            self.changeextracommands(controls)
            self.drawextracommands()
        if self.categorylist[self.icategorylist]=='text':# change level text
            self.changeleveltext(controls)
            self.drawleveltext()
        if self.categorylist[self.icategorylist]=='parts':# create new level part
            self.createdestroylevelparts(controls)
        if self.categorylist[self.icategorylist]=='instructions':# instructions
            self.drawinstructions()
        self.destroyplayerduplicates()
        self.destroycameraduplicates()
        self.changexcamycam(controls)# change area displayed
        if controls.x and controls.xc: self.changegridon()
        if controls.q and controls.qc: self.exittooverworld()
        if controls.e and controls.ec: self.playlevel()
        self.pointer.update(controls)
    def update(self,controls):
        if controls.c:
            self.changeactorheld(controls)
            self.drawactordatabase(controls)# display all database actors with scrolling
        else:
            self.update_editorview(controls)# regular editor


# An actor to be added/shown on the level editor screen
class obj_leveleditoractor:
    def __init__(self,imagename,radx,rady,command,barcode,creator):
        self.imgname=imagename# only one image per object
        self.radx=radx# radx is the half size along x axis
        self.rady=rady
        self.command=command# command to put in script
        self.barcode=barcode# a string to identify what the object is (e.g. player, enemy1)
        self.x=0
        self.y=0
        self.img=pygame.image.load(imagename).convert_alpha()
        self.creator=creator# creator=leveleditor
    def draw(self):
        func_drawimage(self.img,(self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# A music to be added/shown on the level editor screen
class obj_leveleditormusic:
    def __init__(self,musicname,barcode,creator):
        self.musicname=musicname
        self.barcode=barcode# a string to identify what the object is (e.g. player, enemy1)
        self.creator=creator# creator=leveleditor

# A parameter to be added/shown on the level editor screen
# ultimately create an extracommand of the form: command+value, e.g.: self.player.maxshoot=200
class obj_leveleditorparam:
    def __init__(self,name,command,value,barcode,creator):
        self.name=name# to be displayed in level editor (e.g. player maxshoot=)
        self.value=str(value)# reference value, e.g. 200. Converted to string
        self.newvalue=self.value# value to be editor
        self.command=command# prefix of the extracommand, e.g. self.player.maxshoot=
        self.barcode=barcode# a string to identify what the object is (e.g. player, enemy1)
        self.creator=creator# creator=leveleditor

# Version of level editor for users (many restrictions)
#*USEREDITOR
class obj_userleveleditor(obj_leveleditor):
    def __init__(self,creator):
        super().__init__(creator)# created by scenemanager
        # Restricted access to some categories only
        self.categorylist=['actors','background','borders','music','boundaries','text','parameters','instructions']
        self.ncategorylist=len(self.categorylist)
    def drawinstructions(self):
        term=['Instructions on how to use the Level Editor:',' ',\
          'Q : Exit           E: Play Level ( E to return )',\
          'X : Toggle Grid','Hold Space + Mouse: Move Camera',\
          'Left-Right :  Scroll Categories',\
          'Hold C : Quick Pick Actor (Scroll with Up-Down or MouseWheel, Choose with LMouse)',' ',\
          'if Category = Instructions :  Displays these Instructions',\
          'if Category = Actor :  Up and Down : Scroll Actors one by one',\
          '                       MouseWheel : Quicker Scroll',\
          '                       LMouse : Place Actor',\
          '                       RMouse : Remove Actor',\
          '                       MMouse : Grab Actor',\
          'if Category = Background, Borders,  Music, Boundaries:      Up and Down : Scroll',\
          'if Category = Text :          Enter/Backspace: Edit Text    Space+Backspace: Erase All Text',\
          'if Category = Parameters :    Up/Down Scroll Lines     Enter/Backspace: Edit Last Line',\
          ' ','(You can use WASD instead of Arrows. Level is automatically saved on exit)']
        pygame.draw.rect(screen, (200, 200, 200), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 0)
        pygame.draw.rect(screen, (0, 0, 0), (30*scsx, 49*scsy, 740*scsx, (len(term)+2)*20*scsy), 3)
        for i in range(len(term)): screen.blit(self.font.render(term[i], True, (0, 0, 0)), (int(100*scsx),int((50+(i+1)*20)*scsy)))
    def drawinfos(self):
        pygame.draw.rect(screen, (0, 0, 0), (22*scsx, 5*scsy, 140*scsx, 15*scsy), 0)
        screen.blit(self.font.render('  Press H for Help', True, (255, 255, 255)), (int(27*scsx),int(6*scsy)))
        pygame.draw.rect(screen, (0, 0, 0), (197*scsx, 5*scsy, 210*scsx, 15*scsy), 0)
        screen.blit(self.font.render('Current Category: ', True, (150, 150, 150)), (int(202*scsx),int(6*scsy)))
        screen.blit(self.font.render(str(self.categorylist[self.icategorylist]), True, (255, 255, 255)), (int(327*scsx),int(6*scsy)))
        #
        for ic,i in enumerate(self.categorylist):
            pygame.draw.rect(screen, (0, 0, 0), ((2+ic*100)*scsx, 25*scsy, 75*scsx, 15*scsy), 0)
            if ic==self.icategorylist:
                screen.blit(self.font.render(i, True, (255, 255, 255)), (int((2+ic*100+1)*scsx),int(26*scsy)))
            else:
                screen.blit(self.font.render(i, True, (150, 150, 150)), (int((2+ic*100+1)*scsx),int(26*scsy)))
        #
        if  self.categorylist[self.icategorylist]=='actors':
            pygame.draw.rect(screen, (0, 0, 0), (497*scsx, 5*scsy, 210*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Actor Held: ', True, (150, 150, 150)), (502*scsx,6*scsy))
            if self.actorheld: screen.blit(self.font.render(str(self.actorheld.barcode), True, (255, 255, 255)), (592*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='background':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current background: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.backgrounddatabase:
                screen.blit(self.font.render(self.backgrounddatabase[self.ibackgroundshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='boundaries':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current boundaries: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.bdrydatabase:
                screen.blit(self.font.render(self.bdrydatabase[self.ibdryshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='borders':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current border: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.bordersdatabase:
                screen.blit(self.font.render(self.bordersdatabase[self.ibordersshown].barcode, True, (255, 255, 255)), (595*scsx,6*scsy))
        #
        if  self.categorylist[self.icategorylist]=='music':
            pygame.draw.rect(screen, (0, 0, 0), (447*scsx, 5*scsy, 320*scsx, 15*scsy), 0)
            screen.blit(self.font.render('Current Music: ', True, (150, 150, 150)), (452*scsx,6*scsy))
            if self.musicdatabase:
                screen.blit(self.font.render(self.musicdatabase[self.imusicshown].musicname, True, (255, 255, 255)), (552*scsx,6*scsy))
        #
        pygame.draw.rect(screen, (0, 0, 0), (22*scsx, 580*scsy, 350*scsx, 15*scsy), 0)
        screen.blit(self.font.render('File: ', True, (150, 150, 150)), (27*scsx,581*scsy))
        screen.blit(self.font.render(str(self.fileedit)+'.txt', True, (255, 255, 255)), (77*scsx,581*scsy))
        #
        # Show mouse in increments of the 800x600 screens
        pygame.draw.rect(screen, (0, 0, 0), (497*scsx, 580*scsy, 210*scsx, 15*scsy), 0)
        screen.blit(self.font.render('Mouse: ', True, (150, 150, 150)), (502*scsx,581*scsy))
        termx=round( (controls.mousex+xcam)/screenw, 1 )
        termy=round( (screenh-controls.mousey-ycam)/screenh, 1 )
        screen.blit(self.font.render('x = '+str(termx)+' , y = '+str(termy), True, (255, 255, 255)), (552*scsx,581*scsy))
    def changecategory(self,controls):
        if (controls.d and controls.dc) or (controls.right and controls.rightc):
            self.icategorylist=min(self.icategorylist+1,self.ncategorylist-1)
        if (controls.a and controls.ac) or (controls.left and controls.leftc):
            self.icategorylist=max(self.icategorylist-1,0)
        if (not controls.d and controls.dc) or (not controls.right and controls.rightc):# fast scroll when hold key
            timer.reset('changecategory_r')
        if (controls.d or controls.right) and timer('changecategory_r',True,20):
            if timer('changecategory_rs',True,4):
                timer.reset('changecategory_rs')
                self.icategorylist=min(self.icategorylist+1,self.ncategorylist-1)
        if (not controls.a and controls.ac) or (not controls.left and controls.leftc): # fast scroll when hold key
            timer.reset('changecategory_l')
        if (controls.a or controls.left) and timer('changecategory_l',True,20):
            if timer('changecategory_ls',True,4):
                timer.reset('changecategory_ls')
                self.icategorylist=max(self.icategorylist-1,0)
        if controls.h and controls.hc:
            for ic,i in enumerate(self.categorylist):# switch back to category instructions
                if i=='instructions': self.icategorylist=ic
    def recompute_fileedit(self):
        self.fileedit='customlevels/'+self.creator.levelmanager.userlevelname+'_#0'
    def changelevelpart(self,controls):
        pass
    def createdestroylevelparts(self,controls):
        pass
    def changeextracommands(self,controls):
        pass
    def savecommands_checkfile(self):
        self.fileedit='customlevels/'+self.creator.levelmanager.userlevelname+'_#0'
    def loadcommands_checkfile(self):
        self.fileedit='customlevels/'+self.creator.levelmanager.userlevelname+'_#0'
    def playlevel(self):
        self.savecommands()# save current file
        self.creator.changescene('userlevel',False)
    def exittooverworld(self):
        self.savecommands()# save current file
        self.creator.changescene('levelscrollbar',False)
##########################################################
# Levels

# Game Level (empty canvas)
# Creates and manages all elements within (player,enemies,obstacles,physics engine)
# *LEVEL
class obj_level:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        # inherit global parameters from physics (can then be changed locally)
        #
        # Physics parameters
        self.cd0=0.01# reference viscosity (linear drag )
        self.m0=1# reference mass value (multiplies for each actor that is moving)
        self.m0player=1# additional reference mass multiplier for player only
        self.cor_mc=1# Coefficient of Restitution (COR) for collisions between all moving circles
        self.cort_mc=1# CORT (loss in tangent component) for collisions between all moving circles
        self.cor_bdry=0.7# COR for collision moving circles -boundaries
        self.cort_bdry=0.85# CORT for collision moving circles - boundaries
        self.cor=0.7# COR for collisions  moving circles with regular obstacles
        self.cort=0.85# CORT for tangent component:
        self.cor_sp=0.01# COR for collisions  moving circles with Spongy obstacles
        self.cort_sp=0.1# CORT for collisions  moving circles with Spongy obstacles
        self.cor_pk=1.5# COR for collisions  moving circles with pachinko (bumper) obstacles
        self.cort_pk=0.5# CORT for collisions  moving circles with pachinko (bumper) obstacles
        self.fgravi=3# amplitude of gravity force (for all gravity objects)
        self.fvisco=0.3# amplitude of viscosity force (for all sticky spills)
        self.fvisco_ice=0.001# amplitude of viscosity force (for all ice spills)
        self.fgyre=0.03# amplitude of gyre force (for all gyre objects)
        self.fgyrec=0.5# amplitude of gyre centrifugal force (for all gyre objects)
        self.fcorio=0.1# amplitude of coriolis force (for all coriolis objects)
        self.fspring=0.03# amplitude of spring force (for all spring objects)
        #

        # Camera
        self.cameramode=0# choose between: 0=fixed, 1=rect, 2=player, 3=dynamic
        self.cameradist=100# distance from edge where mouse starts pulling camera
        # Player shooting:
        self.playershots=0# number of shots fired by player (for this level part only)
        self.playertime=0# time for level completion (for this level part only)
        self.playertime0=pygame.time.get_ticks()
        # Shots parameters
        self.maxshoot=200# player shot intensity (all shots unless overwritten)
        self.shootspeedmult=0# speed multiplicator when shooting (all shots unless overwritten)
        self.cooldown=25# cooldown time after shooting (all shots unless overwritten)
        self.cshootmax=1# max value
        self.cshootmin=1/4# min value
        self.chargeshotspeed=1.1# multiplicator each frame when charging shot
        self.autochargeshotspeed=1.1# multiplicator each frame when charging shot
        self.hovertime=10# hover gun hover time
        self.hoverendspeedmult=0# hover gun speed multiplicator at end
        self.hovercd=0.01# hover gun drag when hovering
        self.usemousestop=False# stop player if hits mouse pointer dot
        self.mousestopmult=0# speed multiplicator if hits mouse pointer dot
        self.usechargeshot=True
        self.useautochargeshot=False
        self.useshotswimsound=False
        self.useshotjumpsound=False
        self.usehovershot=False
        self.usewarpshot=False
        self.useslowmoshot=False
        self.use4dirshot=False
        #
        # Player parameter: abilities
        self.usestopdown=False
        self.stopdownmult=0
        self.useslowdown= True # able to use slowdown ability (RMouse)
        self.slowdownrate= 0.8
        self.usemovewithkeys= True
        self.movewithkeysampl= 3
        self.movewithkeysendspeedmult= 0.5
        self.usedebugreplace= False # able to use place anywhere for debug (MMouse)
        self.useslowdowntime= False# slow time with right mouse
        self.slowdowntimerate= 0.1# drag multiplier for slowdown
        #
        # Camera
        self.camera=obj_camera(self)
        # Playing Area (create first)
        self.doplayarea=True# process only actors in play area (huge resource saver!)
        self.dplay=100# distance from screen edges for play area
        self.playarea=obj_playarea(self)# object outside are not updated
        # Physics Engine  (define first to append next elements)
        self.use_mcircle_collisions=True# compute collisions between moving circles (except player)
        self.physicsengine=obj_physicsengine(self)# manages physical interactions
        # Player guns
        self.gunmanager=obj_gunmanager(self)
        # Fixed Elements with no Physics no Interactions
        self.background=[]# background image
        self.decos=[]# decorations list
        self.borders=[]# banner with display
        # Fixed Elements with Interactions no Physics
        self.holes=[]# holes list
        self.holeslever=[]# levers list
        self.holesfinish=[]# finish lines list
        # Fixed Elements with Physics
        self.boundaries=[]
        self.obstacles=[]
        self.forces=[]# background forces list
        # Moving Elements with Physics and Interactions
        self.player=[]# player
        self.enemies=[]# enemy list
        self.ops=[]# arbitrary operations (can be anything)
        # Win/Loose conditions
        self.done=False# done playing
        self.win=False# won or lost
        self.noenemiesleft=False# if no enemies remaining
        self.allleversarehit=False# if all levers hit
        self.finishlineisready=False# finish line is ready
        self.imgwinflag=pygame.image.load('data/bk_imglevel_winflag.png').convert_alpha()
        self.hitsleft=10#
        self.timerforlastshot=0# timer for last shot
        # Mouse Pointer
        self.pointer=obj_pointeraim(self)# Mouse pointer
        # Level Text
        self.text=[]# level text
        self.texton=False# Display Text or not (toggle with Space)
        self.hugefont = pygame.font.Font('data/editundo.ttf',240)# text fonts
        self.bigfont = pygame.font.Font('data/editundo.ttf', 120)# text fonts
        self.medfont = pygame.font.Font('data/editundo.ttf', 60)# text fonts
        self.textfont = pygame.font.Font('data/editundo.ttf', 30)# text fonts
        self.smallfont = pygame.font.Font('data/editundo.ttf', 15)#
        # Sounds
        self.music='overworld'#default music (if not overwritten by file load)
        # Misc
        self.holefinishx=0# record x-y of finish hole (for cutscene)
        self.holefinishy=0
        #
        # NOTE: here, additional content will be loaded by leveltext file
        # (these are exec commands contained in level_#i.txt files, created e.g. by level editor)
        # after loading them, a setup is necessary (e.g. to setup operators that targets elements from the leveltext file)
        self.setupdone=False
        #
        # NOTE FOR SELF! THIS DESIGN FOR LEVELS IS MESSY! ##################
        # A better design would be as follows:
        # 1) Have a single list of actors self.actors=[]
        #   each actor in this list must have a self.name and a list self.tags=[]
        #   (this will help make lists for interactions between them)
        #
        # 2) Load all actors during the level __init__ as self.actors.append(obj_new)
        #  (actors can be added using commands from textfiles genereated by the level editor )
        # 3) on first execution of level run a setup
        #  (this helps each actor target other ones that have been added during 1) )
        # 4) on next executions of level do an update of each actors
        # (possibly using the names and tags to determine update order etc...)
        #
        self.rect_textmid=(100*scsx,700*scsx,50*scsy,100*scsy)
        self.rect_won=(100,1180,200,520)

    def setup(self):# setup done once at beginning of level (AFTER all level content has been loaded)
        # Camera Setup
        self.camera.setup()
        # Operators (need loaded actors to setup)
        if self.ops:
            for i in self.ops: i.setup()
        # Change boundary colors from self to the one of borders
        if self.boundaries and self.borders: self.boundaries.color = self.borders.bordercolor
        # Load shot
        self.gunmanager.setup()# assign currently used gun
        #
        self.setupdone=True
        #
        if not self.use_mcircle_collisions:# remove collisions moving circles (except with player)
            self.physicsengine.list_mcircle_mcircle_collide_mcircle=[]
    def tracktime(self):
        self.playertime=pygame.time.get_ticks()-self.playertime0
    def drawtext(self,controls):
        if controls.space and controls.spacec:# toggle text
            if self.texton:
                self.texton=False
            else:
                self.texton=True
        if self.texton:
            if self.text:
                j=self.rect_textmid
                for ic,i in enumerate(self.text):
                    if ic<19:
                        jdec=(j[0],j[1],j[2]+ic*30,j[3]+ic*30)
                        jdecw=(jdec[0]-2,jdec[1]-2,jdec[2]+1,jdec[3]+1)
                        func_drawtextinrect(i,self.textfont,(255,255,255),jdecw)
                        func_drawtextinrect(i,self.textfont,(0,0,0),jdec)
                        # pygame.draw.rect(screen, (255, 255, 255), rect_to_pygame_rect(self.rect_resetsave), 0)
    def checkwinloose(self):
        if not self.noenemiesleft:# check no enemies left
            if not self.enemies:
                if self.holes:
                    for i in self.holes:i.ison=True# turn to done all regular holes
                self.noenemiesleft=True
        if not self.allleversarehit:# check all levers are hit
            if not self.holeslever or all([self.holeslever[c].hit for c,i in enumerate(self.holeslever)]):
                self.allleversarehit=True
        if not self.finishlineisready:# check finish line is ready
            if self.noenemiesleft and self.allleversarehit:
                if self.holesfinish:
                    for i in self.holesfinish:
                        i.ready=True # turn to ready all finish holes
                        if once('finishready',self): sound.play('finishready')
                self.finishlineisready=True
        if self.finishlineisready:# Win if player reaches one finish line
            if self.player:
                if self.holesfinish:
                    for i in self.holesfinish:
                        if i.hit:
                            self.done=True
                            self.win=True
                            self.holefinishx=i.x# record x,y of finish hole when hit
                            self.holefinishy=i.y
        # We removed the option to loose!!!!
        if False:
            if self.hitsleft<1:# Loose if out of shots
                self.timerforlastshot += 1# start/increase timer
                # if has shot last shot, after small timer check if all moving objects are under min speed
                if self.timerforlastshot>50 and self.physicsengine.motion_checkallslow(0.1):
                    self.done=True# if so then lost
                    self.win=False
    def endlevelpart(self,controls):# keep, is modified for user levels
        if self.win:# Won this part
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
            if term.levelpart != term.nlevelparts-1:
                self.gotonextpart()
            else:
                self.wonlevel(controls)
        else:# Lost
            self.lostlevel(controls)
    def gotonextpart(self):# go to next part in game with cutscene
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        term.playershots=term.playershots+self.playershots# save number of player shots (add to ones from previous parts)
        term.playertime=term.playertime+self.playertime# save time
        term.levelpart = min(term.levelpart+1,term.nlevelparts-1)# change level part to+1
        if not term.won: term.progress = term.levelpart# mark next level part for starting again
        self.creator.levelmanager.saveprogresstofile()# save to file
        self.creator.levelmanager.recompute_wonopenlevels()# recompute which levels are won/open
        # cutscene 2 (preloaded) needs to know where player is, so tell it before forgetting level
        term=next((i for i in self.creator.cutscenelist if i.name == 'cutscene2'), None)
        termp=self.player
        [term.imgh,term.xh,term.yh,term.uh,term.vh,term.kspringh,term.cdh,term.rad,term.holex,term.holey]=\
        [termp.imghead,termp.xh,termp.yh,termp.uh,termp.vh,termp.kspringh,termp.cdh,termp.rad,self.holefinishx,self.holefinishy]
        self.creator.changescene('level','cutscene2')
    def wonlevel(self,controls):
        if self.background: self.background.update()
        if self.boundaries: self.boundaries.update()
        if self.borders: self.borders.update(self.hitsleft)
        if once('wonlevel',self): music.playonce('win')
        pygame.draw.rect(screen, (255, 210, 0), rect_to_pygame_rect(self.rect_won), 0)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_won), 3)
        func_drawtextatpoint('You Won',self.hugefont,(0,0,0),(640,340))
        screen.blit(self.imgwinflag,(640-50,180-50))
        if timer('wonlevel',self,50):
            func_drawtextatpoint('Click in Rejoice',self.medfont,(0,0,0),(640,460))
            if controls.mouse1 and controls.mouse1c:
                self.wonlevelprogress()
    def wonlevelprogress(self):# keep, is modified for user levels
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        term.playershots=term.playershots+self.playershots# save number of player shots (add to ones from previous parts)
        term.playertime=term.playertime+self.playertime# save time
        term.won=True
        term.progress=term.nlevelparts
        self.creator.levelmanager.saveprogresstofile()# save to file
        self.creator.levelmanager.recompute_wonopenlevels()# recompute which levels are won/open
        term.levelpart=0# reset to first part
        self.creator.changescene('overworld',False)
    def lostlevel(self,controls):
        if self.background: self.background.update()
        if self.boundaries: self.boundaries.update()
        if self.borders: self.borders.update(self.hitsleft)
        if once('lostlevel',self): music.playonce('loose')
        pygame.draw.rect(screen, (123,123,123), rect_to_pygame_rect(self.rect_won), 0)
        pygame.draw.rect(screen, (0, 0, 0), rect_to_pygame_rect(self.rect_won), 3)
        func_drawtextatpoint('You Lost',self.hugefont,(0,0,0),(640,340))
        if timer('lostlevel',self,50):
            func_drawtextatpoint('Click in Anger',self.medfont,(0,0,0),(640,460))
            if controls.mouse1 and controls.mouse1c:
                self.lostlevelprogress()
    def lostlevelprogress(self):# keep, is modified for user levels
        self.creator.changescene('level',False)# reload same level
    def gotooverworld(self):
        self.creator.levelmanager.saveprogresstofile()# save to file
        self.creator.levelmanager.recompute_wonopenlevels()# recompute which levels are won/open
        term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
        if term.won: term.levelpart=0# if already won always come back to first part
        self.creator.changescene('overworld',False)
    def editlevel(self):
        self.creator.changescene('leveleditor',False)
    def update_playing(self):
        # Apply Level operators
        self.tracktime()
        self.checkwinloose()
        #
        self.physicsengine.update()# Update physics
        if self.background: self.background.update()# background/decorations
        if self.decos: [i.update() for i in self.decos]
        if self.ops: [i.operate() for i in self.ops]# operators (may include drawing)
        if self.forces: [i.update() for i in self.forces]# forces (drawing)
        if self.obstacles: [i.update() for i in self.obstacles] # Obstacles
        if self.boundaries: self.boundaries.update()# (non-iterable)
        if self.holeslever: [i.update() for i in self.holeslever]
        if self.holes: [i.update() for i in self.holes]
        if self.holesfinish: [i.update() for i in self.holesfinish]
        if self.enemies: [i.update() for i in self.enemies]# Enemies<Player
        if self.player: self.player.update(controls) # (non-iterable)

        if self.borders: self.borders.update(self.hitsleft)# (non-iterable)
        self.camera.update(controls)
        self.drawtext(controls)
        self.pointer.update(controls)
        self.gunmanager.update(controls)# (non-iterable, draws on top of pointer)
        #
    def debugcommands(self,controls):# commands and abilities only for dev
        if self.player: self.player.usedebugreplace=True
        if controls.e and controls.ec: self.editlevel()# toggle edit mode
        if controls.q and controls.qc: self.gotooverworld()
        if controls.r and controls.rc: self.creator.changescene('level',False)# reload current level
        if controls.g and controls.gc:
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]# access current level data
            term.levelpart=min(term.levelpart+1,term.nlevelparts-1)
            self.creator.changescene('level',False)
        if controls.f and controls.fc:
            term=self.creator.levelmanager.levels[self.creator.levelmanager.ilevel]
            term.levelpart=max(term.levelpart-1,0)
            self.creator.changescene('level',False)
    def update(self,controls):
        if not self.setupdone: self.setup()# done once at beginning of level
        if not self.done:
            self.update_playing()# while playing the level
        else:
            self.endlevelpart(controls)# done playing
        if dodebug: self.debugcommands(controls)# debug mode switch level part with F and G



# Level generated from level canvas then by additions from text file
class obj_levelfromfile(obj_level):
    def __init__(self,filename,creator):
        super().__init__(creator)# created by scenemanager
        self.filename=filename
        f1=open(self.filename, 'r+')
        line=f1.readline()
        exec(str(line))
        while line:
            line=f1.readline()
            exec(str(line))
        f1.close()

# User Level: generated from file, cannot win/update as in normal mode
#*USERLEVEL
class obj_userlevelfromfile(obj_level):
    def __init__(self,filename,creator):
        super().__init__(creator)# created by scenemanager
        self.filename=filename
        f1=open(self.filename, 'r+')
        line=f1.readline()
        exec(str(line))
        while line:
            line=f1.readline()
            exec(str(line))
        f1.close()
    def endlevelpart(self,controls):
        if self.win:
            self.wonlevel(controls)
        else:
            self.lostlevel(controls)
    def gotonextpart(self):
        pass
    def wonlevelprogress(self):
        music.change('overworld')
        self.creator.changescene('levelscrollbar',False)
    def lostlevelprogress(self,controls):
        self.creator.changescene('levelscrollbar',False)
    def gotooverworld(self):
        self.creator.changescene('levelscrollbar',False)
    def editlevel(self):
        self.creator.changescene('userleveleditor',False)
        # self.creator.level.loadcommands()
    def debugcommands(self,controls):# same but cant change level part as there is only one
        pass
    def update(self,controls):
        if not self.setupdone: self.setup()# done once at beginning of level
        if not self.done:
            self.update_playing()# while playing the level
        else:
            self.endlevelpart(controls)# done playing
        if controls.q and controls.qc: self.gotooverworld()# user has access to shortcuts
        if controls.r and controls.rc: self.creator.changescene('userlevel',False)
        if controls.e and controls.ec: self.editlevel()
# Level generated without text file (fallback method)
class obj_levelfallback(obj_level):
    def __init__(self,creator):
        super().__init__(creator)# inherit initiatilization from level
        self.hitsleft=999# number of hits left
        self.text=['fallback level']
        self.background=obj_background('data/bk_imglevel_background1.png',self)
        self.holes.append(obj_hole(35,35,25,'data/bk_imghole.png',self))
        self.holes.append(obj_hole(765,35,25,'data/bk_imghole.png',self))
        self.holes.append(obj_hole(35,565,25,'data/bk_imghole.png',self))
        self.holes.append(obj_hole(765,565,25,'data/bk_imghole.png',self))
        self.holes.append(obj_hole(400,25,25,'data/bk_imghole.png',self))
        self.holes.append(obj_hole(400,575,25,'data/bk_imghole.png',self))
        self.enemies.append(obj_enemy1(700,500,self))
        self.player=obj_player(400,300,self)

##########################################################

# Level Camera
# *CAMERA
# Note: formula for going from physical position (xs,ys with y axis upward) to position on display screen (xp,yp) is:
    # xp=xs-xcam
    # yp=screenh-ys-ycam
    # where xcam,ycam are the offsets
class obj_camera:
    def __init__(self,creator):
        self.creator=creator# created by level
        # Reset Camera on creation
        changexcam(0)
        changeycam(0)
    # Most init (except initial position) is done in setup, called during level setup instead of init
    def setup(self):
        # Abilities of camera (overview)
        self.cameramode=self.creator.cameramode# choose between: fixed, dynamic, player, playeru, rect or rectu
        self.cameradist=self.creator.cameradist# use same edge distance for all (simpler)
        if self.cameramode>-1 and self.cameramode<6:
            self.cameramodename=['fixed','rect','player','dynamic'][self.cameramode]
        else:
            self.cameramodename='fixed'
        self.usefixedcamera=(self.cameramodename=='fixed')# fix camera definitively (omit all other procedures)
        self.usemouseatborders=any(self.cameramodename==i for i in ['player','rect'])# follow mouse if at borders
        # Player at center (not good for aiming!)
        self.usefocusonplayer=(self.cameramodename=='player')# focus on present player position
        self.usefocusonexpectedplayer=False# obsolete
        # Player in rectangle
        self.usefocusonplayerinrect=(self.cameramodename=='rect')
        self.usefocusonexpectedplayerinrect=False# obsolete
        # Strictest rules
        self.usekeepplayeronscreen=True# keep player on screen second top priority (always true)
        self.usehidebdry=True # hide what is behind the boundaries (top priority,always true)
        #
        # Mouse near screen edges (overrules focus)
        self.cam_matbspeed=0.1# max speed of camera movement
        self.cam_matbdistx=self.cameradist#399# inward distance from screen edges when starts moving (must be >0), for x direction
        self.cam_matbdisty=self.cameradist#299# same for y direction
        #
        # Focus on player (any distance)
        self.cam_fopspeed=0.003# focus speed
        # Focus on expected player position(any distance)
        self.cam_foexpspeed=0.003# focus speed
        self.cam_foexptime=10# typical time to compute expected position from speed (in frames)
        #
        # Focus on player in a rectangle
        self.cam_fopirspeed=0.1# max speed of camera movement (if player all the way to border)
        self.cam_fopirdistx=self.cameradist# inward distance from screen edges when force starts (best if same as self.cam_matbdist)
        self.cam_fopirdisty=self.cameradist
        # Focus on expected player in a rectangle
        self.cam_foexpirspeed=0.1# max speed of camera movement (if player all the way to border)
        self.cam_foexpirdistx=self.cameradist# inward distance from screen edges when force starts (can be<0 for outer edges)
        self.cam_foexpirdisty=self.cameradist
        self.cam_foexpirtime=10
        #
        # Dynamic Camera
        self.usedynamiccamera=(self.cameramodename=='dynamic')# dynamic Camera
        self.kmc_distx=self.cameradist# distance from screen edges where mouse spring activates
        self.kmc_disty=self.cameradist
        self.mc=50# camera mass
        self.cdc=10# kinematic drag (is divided by mass!) should be big
        self.alphac=0.5# (match player speed, must be 0< =<1)
        self.kpc=0.05#0.05# spring to player
        self.kmc=0.3# spring to camera (if is = to kpc keeps player on screen without other actions)
        self.xc=xcam+screenw/2
        self.yc=screenh/2-ycam
        self.uc=0# camera speed
        self.vc=0
        self.fxc=0# external forces
        self.fyc=0
        #
        # Keep player on screen (overrules all previous rules)
        self.cam_kposdistx=40# min dist allowed between player +radius and edges of displayed screen (best keep at 25)
        self.cam_kposdisty=40# same y component
        #
        # Keep view from behind boundaries (overrules allprevious rules)
        self.cam_bdydist=40# max distance shown behind boundaries (keep at boundary size =25 usually)
        #
    def focusonplayer(self,controls):# try to focus on player at middle of screen (slowly)
        if self.creator.player:
            term=self.creator.player
            changexcam(xcam+(term.x-xcam-screenw/2)*self.cam_fopspeed)
            changeycam(ycam+(screenh-term.y-ycam-screenh/2)*self.cam_fopspeed)# left
    def focusonexpectedplayer(self,controls):# try to focus on player expected position from speed (fast)
        if self.creator.player:
            term=self.creator.player
            changexcam(xcam+(term.x+term.u*self.cam_foexptime*dt-xcam-screenw/2)*self.cam_foexpspeed)
            changeycam(ycam+(screenh-term.y-term.v*self.cam_foexptime*dt-ycam-screenh/2)*self.cam_foexpspeed)
    def focusonplayerinrect(self,controls):# try to focus player within center rectangle (slowly and account for player radius)
        if self.creator.player:
            term=self.creator.player
            if term.x-term.rad-xcam<self.cam_fopirdistx:
                changexcam(xcam+(term.x-term.rad-xcam-self.cam_fopirdistx)*self.cam_fopirspeed)# left
            if term.x+term.rad-xcam>screenw-self.cam_fopirdistx:
                changexcam(xcam+(term.x+term.rad-xcam-screenw+self.cam_fopirdistx)*self.cam_fopirspeed)# right
            if screenh-term.y-term.rad-ycam<self.cam_fopirdisty:
                changeycam(ycam+(screenh-term.y-term.rad-ycam-self.cam_fopirdisty)*self.cam_fopirspeed)# top
            if screenh-term.y+term.rad-ycam>screenh-self.cam_fopirdisty:
                changeycam(ycam+(-term.y+term.rad-ycam+self.cam_fopirdisty)*self.cam_fopirspeed)# bottom
    def focusonexpectedplayerinrect(self,controls):# try to focus expected player within center rectangle
        if self.creator.player:
            term=self.creator.player
            if term.x+term.u*self.cam_foexpirtime*dt-term.rad-xcam<self.cam_foexpirdistx:
                changexcam(xcam+(term.x+term.u*self.cam_foexpirtime*dt-term.rad-xcam-self.cam_foexpirdistx)*self.cam_foexpirspeed)# left
            if term.x+term.u*self.cam_foexpirtime*dt+term.rad-xcam>screenw-self.cam_foexpirdistx:
                changexcam(xcam+(term.x+term.u*self.cam_foexpirtime*dt+term.rad-xcam-screenw+self.cam_foexpirdistx)*self.cam_foexpirspeed)# right
            if screenh-term.y-term.v*self.cam_foexpirtime*dt-term.rad-ycam<self.cam_foexpirdisty:
                changeycam(ycam+(screenh-term.y-term.v*self.cam_foexpirtime*dt-term.rad-ycam-self.cam_foexpirdisty)*self.cam_foexpirspeed)# top
            if screenh-term.y-term.v*self.cam_foexpirtime*dt+term.rad-ycam>screenh-self.cam_foexpirdisty:
                changeycam(ycam+(-term.y-term.v*self.cam_foexpirtime*dt+term.rad-ycam+self.cam_foexpirdisty)*self.cam_foexpirspeed)# bottom
    def mouseatborders(self,controls):# Move Camera when mouse is near borders
        if controls.mousex<self.cam_matbdistx:
            changexcam(xcam-(self.cam_matbdistx-controls.mousex)*self.cam_matbspeed)# left
        if controls.mousex>screenw-self.cam_matbdistx:
            changexcam(xcam+(controls.mousex-screenw+self.cam_matbdistx)*self.cam_matbspeed)# right
        if controls.mousey<self.cam_matbdisty:
            changeycam(ycam-(self.cam_matbdisty-controls.mousey)*self.cam_matbspeed)# top
        if controls.mousey>screenh-self.cam_matbdisty:
            changeycam(ycam+(controls.mousey-screenh+self.cam_matbdisty)*self.cam_matbspeed)# bottom
    def keepplayeronscreen(self,controls):
        if self.creator.player:
            term=self.creator.player
            if term.x-term.rad-xcam<self.cam_kposdistx: changexcam(term.x-term.rad-self.cam_kposdistx)# left edge
            if term.x+term.rad-xcam>screenw-self.cam_kposdistx: changexcam(term.x+term.rad-screenw+self.cam_kposdistx)# right
            if screenh-term.y-term.rad-ycam<self.cam_kposdisty: changeycam(screenh-term.y-term.rad-self.cam_kposdisty)# top
            if screenh-term.y+term.rad-ycam>screenh-self.cam_kposdisty: changeycam(-term.y+term.rad+self.cam_kposdisty)# bottom
    def hidebehindboundaries(self,controls):
        if self.creator.boundaries:
            term=self.creator.boundaries
            if term.xmin-self.cam_bdydist-xcam > 0: changexcam(term.xmin-self.cam_bdydist)# left bdry
            if term.xmax+self.cam_bdydist-xcam < screenw: changexcam(term.xmax+self.cam_bdydist - screenw)# right bdry
            if screenh-term.ymax-self.cam_bdydist-ycam > 0: changeycam(screenh-term.ymax-self.cam_bdydist)# top bdry
            if screenh-term.ymin+self.cam_bdydist-ycam < screenh: changeycam(-term.ymin+self.cam_bdydist)# bottom bdry
    def dynamiccamera(self,controls):# dynamic model for the camera
        # Camera position xc,yc in game reference frame
        self.xc=xcam+screenw/2
        self.yc=screenh/2-ycam
        # reset camera forces
        self.fxc=0
        self.fyc=0
        # spring to player
        if self.creator.player:
            self.fxc += - self.kpc*(self.xc-self.creator.player.x)*dt
            self.fyc += - self.kpc*(self.yc-self.creator.player.y)*dt
        # spring to mouse position (in game reference frame)
        # Amplitude depends on areas of screen the mouse is in (=0 in center rectangle, then increases in corners)
        self.kmcx=0# factor 0< <1 for mouse spring depending on x-y area of screen
        self.kmcy=0
        if controls.mousex<self.kmc_distx:
            self.kmcx=(self.kmc_distx-controls.mousex)/self.kmc_distx# left
        elif controls.mousex>screenw-self.kmc_distx:
            self.kmcx=(controls.mousex-screenw+self.kmc_distx)/self.kmc_distx# right
        if controls.mousey<self.kmc_disty:
            self.kmcy=(self.kmc_disty-controls.mousey)/self.kmc_disty# top
        elif controls.mousey>screenh-self.kmc_disty:
            self.kmcy=(controls.mousey-screenh+self.kmc_disty)/self.kmc_disty# bottom
        self.fxc += - self.kmc*self.kmcx*(self.xc- (controls.mousex+xcam) )*dt
        self.fyc += - self.kmc*self.kmcy*(self.yc- (screenh-controls.mousey-ycam) )*dt
        # drag
        self.fxc += - self.cdc*self.uc*dt
        self.fyc += - self.cdc*self.vc*dt
        # match player speed
        if self.creator.player:
            self.fxc += self.cdc*self.alphac*self.creator.player.u*dt
            self.fyc += self.cdc*self.alphac*self.creator.player.v*dt
        # Update camera
        self.uc = self.uc + self.fxc/self.mc*dt
        self.vc = self.vc + self.fyc/self.mc*dt
        self.xc += self.uc*dt
        self.yc += self.vc*dt
        # Assign camera (in screen reference frame)
        changexcam(self.xc-screenw/2)
        changeycam(screenh/2-self.yc)
    def cameradebug(self,controls):# simple tests for dev
        if self.creator.player and controls.m:
            changexcam(self.creator.player.x-400)
            changeycam(300-self.creator.player.y)
        if controls.n:
            changexcam(0)
            changeycam(0)
        if controls.left: changexcam(xcam-5)
        if controls.right: changexcam(xcam+5)
        if controls.down: changeycam(ycam+5)
        if controls.up: changeycam(ycam-5)
    def draw(self):
        if not self.usefixedcamera: # Draw on screen area where mouse controls player (for any mode except fixed)
            self.drawareacrossairs(self.cameradist,self.cameradist,(0,0,0))
    def drawareacrossairs(self,termx,termy,color):
            pygame.draw.line(screen,color, (termx,termy),(termx+10,termy), 2)# crosses for camera center, top left
            pygame.draw.line(screen,color, (termx,termy),(termx,termy+10), 2)
            pygame.draw.line(screen,color, (screenw-termx,termy),(screenw-termx-10,termy), 2)# top right
            pygame.draw.line(screen,color, (screenw-termx,termy),(screenw-termx,termy+10), 2)
            pygame.draw.line(screen,color, (termx,screenh-termy),(termx+10,screenh-termy), 2)# bottom left
            pygame.draw.line(screen,color, (termx,screenh-termy),(termx,screenh-termy-10), 2)
            pygame.draw.line(screen,color, (screenw-termx,screenh-termy),(screenw-termx-10,screenh-termy), 2)# bottom right
            pygame.draw.line(screen,color, (screenw-termx,screenh-termy),(screenw-termx,screenh-termy-10), 2)
    def update(self,controls):
        if self.usefixedcamera:
            changexcam(0)# reset camera
            changeycam(0)
        else:
            self.draw()
            # update order matters as some functions supersede others
            if self.usedynamiccamera: self.dynamiccamera(controls)
            if self.usefocusonplayer: self.focusonplayer(controls)
            if self.usefocusonexpectedplayer: self.focusonexpectedplayer(controls)
            if self.usefocusonplayerinrect: self.focusonplayerinrect(controls)
            if self.usefocusonexpectedplayerinrect: self.focusonexpectedplayerinrect(controls)
            if self.usemouseatborders: self.mouseatborders(controls)#
            if self.usekeepplayeronscreen: self.keepplayeronscreen(controls)# should happen at all cost
            if self.usehidebdry: self.hidebehindboundaries(controls)
            if dodebug: self.cameradebug(controls)# simple tests for camera


##########################################################

# Level Background
# *BACKGROUND
class obj_background:
    def __init__(self,imagename,creator):
        self.imagename=imagename
        # self.img=pygame.image.load(imagename).convert_alpha()# background image.convert_alpha()
        # we choose to fill screen with one color for increased performances
        self.color=( 53 , 157 , 60 )# default green
        if self.imagename=='background0': self.color=( 53 , 157 , 60 )
        if self.imagename=='background1': self.color=( 83 , 189 , 90 )
        if self.imagename=='background2': self.color=( 212 , 196 , 120 )
        if self.imagename=='background3': self.color=( 176 , 167 , 128 )
        if self.imagename=='background4': self.color=( 66 , 183 , 231 )
        if self.imagename=='background5': self.color=( 131 , 236 , 225 )
        if self.imagename=='background6': self.color=( 224 , 224 , 224 )
        if self.imagename=='background7': self.color=( 97 , 138 , 115 )
        if self.imagename=='background8': self.color=( 167 , 172 , 171 )
        if self.imagename=='background9': self.color=( 112 , 112 , 112 )
        if self.imagename=='background10': self.color=( 54 , 51 , 51 )
        if self.imagename=='background11': self.color=( 30 , 30 , 30 )
    def draw(self):
        screen.fill(self.color)
    def update(self):
        self.draw()

# Background but used by level editor (same except for additional argument barcode)
class obj_leveleditorbackground(obj_background):
    def __init__(self,imagename,barcode,creator):
        super().__init__(imagename,creator)
        self.barcode=barcode# additional info: barcode to identify object type in level editor

# Level Borders  (draws on top of everything)
# Draws the banner and also imposes the color of boundaries
# *BORDERS
class obj_borders:
    def __init__(self,borderref,creator):
        self.creator=creator# created by level
        self.borderref=borderref# doesnt matter, unless wants to change border style each level
        self.font = pygame.font.Font('data/editundo.ttf', 15)# text fonts
        #
        self.bordercolor=(217,123,0)# reference
        if self.borderref == 'borders0': self.bordercolor= (217,123,0)
        if self.borderref == 'borders1': self.bordercolor= (189,107,0)
        if self.borderref == 'borders2': self.bordercolor= (212,196,120)
        if self.borderref == 'borders3': self.bordercolor= (176,167,128)
        if self.borderref == 'borders4': self.bordercolor= (66,183,231)
        if self.borderref == 'borders5': self.bordercolor= (131,236,225)
        if self.borderref == 'borders6': self.bordercolor= (224,224,224)
        if self.borderref == 'borders7': self.bordercolor= (97,138,115)
        if self.borderref == 'borders8': self.bordercolor= (167,172,171)
        if self.borderref == 'borders9': self.bordercolor= (112,112,112)
        if self.borderref == 'borders10': self.bordercolor= (54,51,51)
        if self.borderref == 'borders11': self.bordercolor= (120,14,136)
        if self.borderref == 'borders12': self.bordercolor= (255,210,0)
    def draw(self,hitsleft):
        pygame.draw.rect(screen, (255,255,255), (15,5,135,19), 0)# top +corners
        pygame.draw.rect(screen, (0,0,0), (15,5,135,19), 2)# top +corners
        term=self.creator.creator.levelmanager.levels[self.creator.creator.levelmanager.ilevel]
        # screen.blit(self.font.render(\
        #  'P='+str(term.levelpart+1)+'/'+str(term.nlevelparts)+' Help: Space', True, (0, 0, 0)), (26,8) )
        screen.blit(self.font.render(\
         'Shots: '+str(self.creator.playershots)+\
         ' Time: '+str(round(self.creator.playertime/1000,1)), True, (0, 0, 0)), (18,8) )
    def update(self,hitsleft):
        self.draw(hitsleft)

# Borders but used by level editor
class obj_leveleditorborders(obj_borders):
    def __init__(self,borderref,barcode,creator):
        super().__init__(borderref,creator)
        self.barcode=barcode# additional info: barcode to identify object type in level editor
    def draw(self):
        pass
        # self.draw()# draw borders but not informations


##########################################################
# Player
# *PLAYER
class obj_player:
    def __init__(self,xspawn,yspawn,creator):
        self.creator = creator# created by level
        self.imgbody=pygame.image.load('data/bk_imgplayer_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgplayer_head.png').convert_alpha()
        self.imgmagicshot=pygame.image.load('data/bk_imgplayer_magicshot.png').convert_alpha()
        self.smallfont = pygame.font.Font('data/editundo.ttf', 15)# text fonts
        self.x=xspawn# position
        self.y=yspawn
        # Physics
        self.u=0# speed
        self.v=0
        self.fx=0# forces applied for motion by physics engine
        self.fy=0
        self.cd0=self.creator.cd0# reference linear (inherit from level)
        self.cd=self.cd0# drag applied for motion by physics engine
        self.m0=self.creator.m0*self.creator.m0player#
        self.m=self.m0*10# reference mass (scaled by level reference mass m0)
        self.rad=25# radius(pixel)
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.active=True# is within playing area and subject to updates/interactions (always True)
        # Head
        self.xh=self.x# head position
        self.yh=self.y
        self.uh=0# head speed
        self.vh=0
        self.kspringh=0.1
        self.cdh=0.5
        ################
        # Player Abilities (except shooting)
        # Stopdown
        self.usestopdown=self.creator.usestopdown# Able to use stopdown ability (RMouse)
        self.stopdownmult=self.creator.stopdownmult# stop down speed mult
        # Slowdown
        self.useslowdown= self.creator.useslowdown # able to use slowdown ability (RMouse)
        self.slowdownrate=self.creator.slowdownrate# drag multiplier for slowdown
        # Move with WASD or arrows
        self.usemovewithkeys= self.creator.usemovewithkeys # able to use move with keys ability (WASD or Arrows)
        self.movewithkeysampl=self.creator.movewithkeysampl# rate of move with keys
        self.movewithkeysendspeedmult=self.creator.movewithkeysendspeedmult# speed mult when ends
        # Replace Player
        self.usedebugreplace= self.creator.usedebugreplace # able to use place anywhere for debug (MMouse)
        # Slow Time
        self.useslowdowntime=self.creator.useslowdowntime# slow down time with RMouse
        self.slowdowntimerate=self.creator.slowdowntimerate
         ################
        # Physics Engine and Interactions Engine
        self.dobforce=True# subject or not to background forces. Can be toggled (e.g. during magicshot)
        self.add_physics()# add self to physics
        self.hit=False# hit by another moving circle
        self.hitec=0# record hit energy
        self.hitecmax=200

    def add_physics(self):# Add Self to Physics Engine
        self.physicsengine_targetlist=[]# what this object gets from physics engine
        # self.physicsengine_targetlist.append('playarea')# freezes outside of playing area (uncessary)
        self.physicsengine_targetlist.append('motion')# motion from forces
        self.physicsengine_targetlist.append('mc_fb_collide_mc')# collision moving circle with fixed boundaries as moving circle
        self.physicsengine_targetlist.append('mcp_mc_collide_mcp')# collision player / moving circle as player
        self.physicsengine_targetlist.append('mc_fc_collide_mc')# collision moving circle / fixed circle as moving circle
        self.physicsengine_targetlist.append('mc_fr_collide_mc')# collision moving circle / fixed rectangle as moving circle
        self.physicsengine_targetlist.append('mc_ft_collide_mc')# collision moving circle / fixed triangle as moving circle
        self.physicsengine_targetlist.append('mc_bf_collide_mc')# interaction moving circle / background force as moving circle
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)
    def stopdown(self,controls):
        if controls.mouse2 and controls.mouse2c:
            if (self.u**2+self.v**2)/2>2**2: sound.play('slowdown')
            self.u *= self.stopdownmult
            self.v *= self.stopdownmult
            # self.cd=self.cd0*30# NEVER impose the drag entirely, use multiplier for consistency with forces!!!


    def slowdown(self,controls):
        if controls.mouse2:
            self.cd=self.cd*30
            # self.cd=self.cd0*30# NEVER impose the drag entirely, use multiplier for consistency with forces!!!
            if controls.mouse2c and (self.u**2+self.v**2)/2>2**2: sound.play('slowdown')

    def slowdowntime(self,controls):
        if controls.mouse2:
            func_slowtime(True)
        else:
            func_slowtime(False)
    def movewithkeys(self,controls):
        if controls.a or controls.left: self.fx -= self.movewithkeysampl
        if controls.d or controls.right: self.fx += self.movewithkeysampl
        if controls.w or controls.up: self.fy += self.movewithkeysampl
        if controls.s or controls.down: self.fy -= self.movewithkeysampl
        # stop motion when keys are released
        if (not controls.a and controls.ac) or (not controls.left and controls.leftc): self.u *= self.movewithkeysendspeedmult
        if (not controls.d and controls.dc) or (not controls.right and controls.rightc): self.u *= self.movewithkeysendspeedmult
        if (not controls.w and controls.wc) or (not controls.up and controls.upc): self.v *= self.movewithkeysendspeedmult
        if (not controls.s and controls.sc) or (not controls.down and controls.downc): self.v *= self.movewithkeysendspeedmult
    def debugreplace(self,controls): # reset player position to mouse (for debugging)
        if controls.mouse3 and controls.mouse3c:
            self.x=controls.mousex+xcam
            self.y=screenh-controls.mousey-ycam
            self.u=0
            self.v=0
            self.fx=0
            self.fy=0
            self.xh=self.x
            self.yh=self.y
            self.uh=0
            self.vh=0
    def movehead(self):# simple own v (spring/dissip) for head movement (doesnt interact with physics engine)
        # global dt# doesnt work!!!!
        self.uh = self.uh- self.kspringh*(self.xh-self.x)*dt - self.cdh*self.uh*dt
        self.vh = self.vh- self.kspringh*(self.yh-self.y)*dt - self.cdh*self.vh*dt
        self.xh += self.uh*dt
        self.yh += self.vh*dt
    def holeslever_hit(self):
        if self.creator.holeslever:
            for i in self.creator.holeslever:
                if i.active:
                    if not i.hit and bcirclebcircle_hit(i.x,i.y,i.rad,self.x,self.y,self.rad):
                        i.hit=True# hole is hit
                        sound.play('hitlever')
    def holesfinish_hit(self):
        if self.creator.holesfinish:
            for i in self.creator.holesfinish:
                if i.active:
                    if i.ready and bcirclebcircle_hit(i.x,i.y,i.rad,self.x,self.y,self.rad):
                        i.hit=True# hole is hit
    def draw(self):
        func_drawimage(self.imgbody,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)# body  (always on screen hopefully)
        func_drawimage(self.imghead, (self.xh-self.rad-xcam,screenh-self.yh-self.rad-ycam),self.rad,self.rad)# head
    def mcircles_hit(self):
        if once(self,self.hit) and timer(self,True,20) and self.hit:
            sound.play_mult_volume('mcircles',self.hitec/self.hitecmax)# play with a volume multiplier
            timer.reset(self)
    def kill(self):
        self.creator.physicsengine.remove_collider(self,self.physicsengine_targetlist)
    def update(self,controls):
        if self.usestopdown: self.stopdown(controls)
        if self.useslowdown: self.slowdown(controls)
        if self.useslowdowntime: self.slowdowntime(controls)
        if self.usedebugreplace: self.debugreplace(controls)
        if self.usemovewithkeys: self.movewithkeys(controls)
        #
        self.draw()
        self.movehead()
        self.mcircles_hit()
        self.holesfinish_hit()# check if player hits finish lines
        self.holeslever_hit()# check if player hits levers
        ### Here the level will execute the Physical Engine applying motion to player from fx,fy,cd,etc


# Player smaller version (60% radius)
class obj_playersmall(obj_player):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgplayersmall_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgplayersmall_head.png').convert_alpha()
        self.m=3.6# mass in r**2
        self.rad=15

##########################################################
##########################################################
# Guns: allows player to shoot
#*GUNS

# Gun manager: controls which gun is used (if multiples)
class obj_gunmanager:
    def __init__(self,creator):
        self.creator=creator# created by level
    def setup(self):
        self.gun=obj_gun(self.creator)# charge gun (with parameters from level)
    def update(self,controls):
        self.gun.update(controls)



# Canvas for gun with general functions
class obj_gun:
    def __init__(self,creator):
        self.creator=creator# created by level
        # Gun parameters
        self.maxshoot=self.creator.maxshoot# max shot intensity
        self.shootspeedmult=self.creator.shootspeedmult# player speed mult when shoots
        self.cooldown=self.creator.cooldown# cooldown time after shot (nothing can be done during then)
        self.cshootmax=self.creator.cshootmax# max value
        self.cshootmin=self.creator.cshootmin# min value
        self.chargeshotspeed=self.creator.chargeshotspeed
        self.autochargeshotspeed=self.creator.autochargeshotspeed
        self.hovertime=self.creator.hovertime
        self.hoverendspeedmult=self.creator.hoverendspeedmult
        self.hovercd=self.creator.hovercd
        self.usemousestop=self.creator.usemousestop# player stops if hits mouse pointer
        self.mousestopmult=self.creator.mousestopmult
        #
        self.usechargeshot=self.creator.usechargeshot
        self.useautochargeshot=self.creator.useautochargeshot
        self.useshotswimsound=self.creator.useshotswimsound
        self.useshotjumpsound=self.creator.useshotjumpsound
        self.usehovershot=self.creator.usehovershot
        self.usewarpshot=self.creator.usewarpshot
        self.useslowmoshot=self.creator.useslowmoshot
        self.use4dirshot=self.creator.use4dirshot
        #
        # Gun states (internal)
        self.aiming=False# gun is aiming or not
        self.shooting=False#gun is shooting or not
        self.cooling=False# gun is cooling down
        # Gun variables
        self.theta=0# angle player/pointer
        self.cshoot=1# multiplicator of maxshoot (0<  <= 1)
        self.cshootrec=self.cshoot# recorded cshoot during shooting
        self.mousedistrec=0# recorded distance player/mouse during shooting
        self.coolingtimer=0# cooldown timer
        self.hovering=False
        self.hovertimer=0
        self.traveldist=0# travelled distance
        self.mousestopon=False# toogle mousestop on/off once per shot

        # Gun wheel (display on mouse pointer)
        self.imggunwheel=pygame.image.load('data/bk_imggunwheel_chargegun.png').convert_alpha()
        self.gunwheel=obj_gunwheelcharge(self)# gun wheel (draw on mouse pointer)

    def useraims(self,controls):
        if controls.mouse1 and controls.mouse1c:
            self.aiming=True
            if self.useslowmoshot: sound.play('slowtime')
        if controls.mouse2 and controls.mouse2c: self.aiming=False# cancel with RMouse
    def aiming_actions(self,controls):# possible actions during aiming
        if self.useslowmoshot: func_slowtime(True)
    def usershoots(self,controls):
        if self.aiming and not self.cooling and not controls.mouse1 and controls.mouse1c: self.shoot(controls)
    def shoot_angle(self,controls):
        self.theta=atan2(screenh-controls.mousey-self.creator.player.y-ycam,controls.mousex-self.creator.player.x+xcam)
        if self.use4dirshot: self.theta=round(self.theta*2/pi)*pi/2
    def shoot_speedmult(self):
        self.creator.player.u *=self.shootspeedmult# cancel former player motion when starts shooting
        self.creator.player.v *=self.shootspeedmult
    def shoot(self,controls):
        self.aiming=False
        self.shooting=True
        self.shoot_angle(controls)
        self.shoot_speedmult()
        # self.creator.fx += self.maxshoot*self.cshoot*cos(self.theta)/dt# is a pulse so in 1/dt
        # self.creator.fy += self.maxshoot*self.cshoot*sin(self.theta)/dt
        # self.creator.player.u += self.maxshoot*self.cshoot*cos(self.theta)/self.creator.player.m
        # self.creator.player.v += self.maxshoot*self.cshoot*sin(self.theta)/self.creator.player.m
        self.creator.player.u += self.maxshoot*self.cshoot*cos(self.theta)/10# non dependent on mass!
        self.creator.player.v += self.maxshoot*self.cshoot*sin(self.theta)/10
        self.creator.playershots += 1# count shots fired
    def shoot_actions(self,controls):# other actions during shooting frame
        self.cshootrec=self.cshoot# record cshoot
        self.shoot_sound()
        if self.usehovershot:
            self.hovering=True
            self.creator.player.dobforce=False# doesnt feel external forces
        if self.usewarpshot:
            self.creator.player.xh += controls.mousex+xcam-self.creator.player.x
            self.creator.player.yh += screenh-controls.mousey-ycam-self.creator.player.y
            self.creator.player.x=controls.mousex+xcam
            self.creator.player.y=screenh-controls.mousey-ycam
        if self.useslowmoshot: func_slowtime(False)
        if self.usemousestop:
            self.mousestopon=True
            self.traveldist=0
            self.mousedistrec=sqrt((controls.mousex-self.creator.player.x+xcam)**2+(screenh-controls.mousey-self.creator.player.y-ycam)**2)
        self.shooting=False# end shooting actions
        self.cooling=True
    def shoot_sound(self):
        if self.useshotswimsound:
            sound.play('shootselfwater')
        elif self.useshotjumpsound:
            sound.play('jump')
        elif self.useslowmoshot:
            pass# no sound if using slowmo
        else:
            sound.play('shootself')
            # sound.play('shootself2')
            # sound.play('shootself3')
            # sound.play('lava')
    def shootends(self): # end shooting arbitrarily(can be called by any procedure)
        self.shootends_actions()
    def shootends_actions(self):# actions if shooting was ended arbitrarily
        if self.usemousestop: self.mousestopends()
        if self.usehovershot: self.hoverends()
    def gun_actions(self,controls):# actions all the time
        self.shoot_cooldown()
        if self.usechargeshot: self.charge()
        if self.useautochargeshot: self.autocharge()
        if self.usehovershot: self.hover()
        if self.usemousestop: self.mousestop(controls)
    def charge(self):
        if self.aiming and not self.cooling:
            self.cshoot=min(self.cshootmax,self.cshoot*self.chargeshotspeed)
        else:
            self.cshoot=self.cshootmin
    def autocharge(self):
        if not self.cooling:
            self.cshoot=min(self.cshootmax,self.cshoot*self.autochargeshotspeed)
        else:
            self.cshoot=self.cshootmin
    def shoot_cooldown(self):
        if self.shooting:
            self.cooling=True
            self.coolingtimer=0
            self.shooting=False
        elif self.cooling:
            self.coolingtimer += dt
            if self.coolingtimer > self.cooldown:
                self.coolingtimer=0
                self.cooling=False
    def hover(self):
        if self.hovering:
            self.creator.player.dobforce=False
            self.hovertimer += dt
            if self.hovertimer > self.hovertime*self.cshootrec:# recorded shooting amplitude
                self.creator.player.u *= self.hoverendspeedmult
                self.creator.player.v *= self.hoverendspeedmult
                self.shootends()# end shooting
    def hoverends(self):
        self.hovering=False
        self.hovertimer=0
        self.creator.player.dobforce=True
    def mousestop(self,controls):
        if self.mousestopon:
            self.traveldist += sqrt(self.creator.player.u**2+self.creator.player.v**2) *dt
            if self.traveldist > self.mousedistrec:
                self.creator.player.u *= self.mousestopmult
                self.creator.player.v *= self.mousestopmult
                self.shootends()# end shooting
    def mousestopends(self):
        self.traveldist=0
        self.mousestopon=False
    def update(self,controls):
        if self.creator.player: # only updates if attached to player
            self.useraims(controls)
            if self.aiming: self.aiming_actions(controls)
            self.usershoots(controls)# user shoots
            if self.shooting: self.shoot_actions(controls)
            self.gun_actions(controls)# actions in general
            self.gunwheel.update(controls)#gun wheel pointer

################################

# Gun wheel (draws on top of mouse pointer)
#*GUN *WHEEL
# Empty canvas
class obj_gunwheel:
    def __init__(self,creator):
        self.creator=creator# created by gun
    def draw(self):
        if self.creator.imggunwheel: screen.blit(self.creator.imggunwheel,(controls.mousex-25,controls.mousey-25))
    def update(self,controls):
        self.draw()

class obj_gunwheelcharge (obj_gunwheel):
    def __init__(self,creator):
        super().__init__(creator)# inherit initiatilization from level
        self.imgpointercharge0=pygame.image.load('data/bk_imgpointer_charge0.png').convert_alpha()
        self.imgpointercharge1=pygame.image.load('data/bk_imgpointer_charge1.png').convert_alpha()
        self.imgpointercharge2=pygame.image.load('data/bk_imgpointer_charge2.png').convert_alpha()
        self.imgpointercharge3=pygame.image.load('data/bk_imgpointer_charge3.png').convert_alpha()
        self.imgpointercharge4=pygame.image.load('data/bk_imgpointer_charge4.png').convert_alpha()
        self.imgpointercharge5=pygame.image.load('data/bk_imgpointer_charge5.png').convert_alpha()
        self.imgpointercharge6=pygame.image.load('data/bk_imgpointer_charge6.png').convert_alpha()
        self.imgpointercharge7=pygame.image.load('data/bk_imgpointer_charge7.png').convert_alpha()
        self.imgpointercharge8=pygame.image.load('data/bk_imgpointer_charge8.png').convert_alpha()
        self.imgpointercharge9=pygame.image.load('data/bk_imgpointer_charge9.png').convert_alpha()
        self.imgpointercharge10=pygame.image.load('data/bk_imgpointer_charge10.png').convert_alpha()
        self.imgpointercharge11=pygame.image.load('data/bk_imgpointer_charge11.png').convert_alpha()
        self.imgpointercharge12=pygame.image.load('data/bk_imgpointer_charge12.png').convert_alpha()
        self.imgpointercharge13=pygame.image.load('data/bk_imgpointer_charge13.png').convert_alpha()
        self.imgpointercharge14=pygame.image.load('data/bk_imgpointer_charge14.png').convert_alpha()
        self.imgpointercharge15=pygame.image.load('data/bk_imgpointer_charge15.png').convert_alpha()
        self.imgpointercharge16=pygame.image.load('data/bk_imgpointer_charge16.png').convert_alpha()
        self.imgpointeratmaxcharge=pygame.image.load('data/bk_imgpointer_atmaxcharge.png').convert_alpha()
    def draw(self):
        if self.creator.imggunwheel: screen.blit(self.creator.imggunwheel,(controls.mousex-25,controls.mousey-25))
        #
        # NB: the wheel is scaled from cshootmin to cshootmax for 0<= <=1
        self.cshootscaled=(self.creator.cshoot-self.creator.cshootmin)/(self.creator.cshootmax-self.creator.cshootmin)
        if self.cshootscaled<2/16:
            screen.blit(self.imgpointercharge0,(controls.mousex-25,controls.mousey-25))
        # elif self.cshootscaled>=1/16 and self.cshootscaled<2/16:
        #     screen.blit(self.imgpointercharge1,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=2/16 and self.cshootscaled<3/16:
            screen.blit(self.imgpointercharge2,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=3/16 and self.cshootscaled<4/16:
            screen.blit(self.imgpointercharge3,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=4/16 and self.cshootscaled<5/16:
            screen.blit(self.imgpointercharge4,(controls.mousex-25,controls.mousey-25))
        if self.cshootscaled>=5/16 and self.cshootscaled<6/16:
            screen.blit(self.imgpointercharge5,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=6/16 and self.cshootscaled<7/16:
            screen.blit(self.imgpointercharge6,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=7/16 and self.cshootscaled<8/16:
            screen.blit(self.imgpointercharge7,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=8/16 and self.cshootscaled<9/16:
            screen.blit(self.imgpointercharge8,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=9/16 and self.cshootscaled<10/16:
            screen.blit(self.imgpointercharge9,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=10/16 and self.cshootscaled<11/16:
            screen.blit(self.imgpointercharge10,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=11/16 and self.cshootscaled<12/16:
            screen.blit(self.imgpointercharge11,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=12/16 and self.cshootscaled<13/16:
            screen.blit(self.imgpointercharge12,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=13/16 and self.cshootscaled<14/16:
            screen.blit(self.imgpointercharge13,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=14/16 and self.cshootscaled<15/16:
            screen.blit(self.imgpointercharge14,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=15/16 and self.cshootscaled<1:
            screen.blit(self.imgpointercharge15,(controls.mousex-25,controls.mousey-25))
        elif self.cshootscaled>=1:
            screen.blit(self.imgpointercharge16,(controls.mousex-25,controls.mousey-25))
            screen.blit(self.imgpointeratmaxcharge,(controls.mousex-25,controls.mousey-25))
        else:
            pass

##########################################################
##########################################################

# Mouse Pointer (for overworld)
# *POINTER
class obj_pointersword:
    def __init__(self,creator):
        self.creator=creator# created by level
        self.imgpointer=pygame.image.load('data/bk_imgoverworld_pointer.png').convert_alpha()
    def draw(self,controls):
        screen.blit(self.imgpointer,(controls.mousex-12,controls.mousey-12))
    def update(self,controls):
        self.draw(controls)

# Mouse Pointer Class (dot basis during levels)
class obj_pointeraim:
    def __init__(self,creator):
        self.creator=creator# created by level
        self.rad=25
        self.imgpointer=pygame.image.load('data/bk_imgpointer.png').convert_alpha()
    def draw(self,controls):
        screen.blit(self.imgpointer,(controls.mousex-25,controls.mousey-25))# pointer base
    def update(self,controls):
        self.draw(controls)

# Mouse Pointer (for level editor)
# *POINTER
class obj_pointerleveleditor:
    def __init__(self,creator):
        self.creator=creator# created by level
        self.imgpointer=pygame.image.load('data/bk_imgleveleditor_locationheld.png').convert_alpha()
        pygame.mouse.set_visible(False)
    def draw(self,controls):
        screen.blit(self.imgpointer,(controls.mousex-5,controls.mousey-5))
    def update(self,controls):
        self.draw(controls)

##########################################################
# Enemies

# Enemy (empty canvas)
# *ENEMY
class obj_enemy:
    def __init__(self,xspawn,yspawn,creator):
        self.creator = creator# created by level
        self.imgbody=pygame.image.load('data/bk_imgenemy1_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy1_head.png').convert_alpha()
        self.x=xspawn# position
        self.y=yspawn
        self.u=0# speed
        self.v=0
        self.fx=0# forces
        self.fy=0
        self.m0=self.creator.m0
        self.m=self.m0*10# reference mass
        self.rad=25# radius(pixel)
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.cd0=self.creator.cd0# reference linear drag
        self.cd=self.cd0# linear drag (can be changed but is reset after motion)
        self.active=True# is within playing area and subject to updates/interactions
        # Head
        self.xh=self.x# head position
        self.yh=self.y
        self.uh=0# head speed
        self.vh=0
        self.kspringh=0.1
        self.cdh=0.5
        #
        # Physics Engine and Interactions Engine
        self.dobforce=True# is subject to background forces. Can be toggled
        self.add_physics()
        self.hit=False# hit by another circle (make a sound)
        self.hit12=False# hit by a hole (group 1-2)
        self.hitec=0
        self.hitecmax=200
    #
    def add_physics(self):# Add Self to Physics Engine
        self.physicsengine_targetlist=[]# what this object gets from physics engine
        self.physicsengine_targetlist.append('playarea')# freezes outside of playing area
        self.physicsengine_targetlist.append('motion')# motion from forces
        self.physicsengine_targetlist.append('mc_fb_collide_mc')# collision moving circle with fixed boundaries as moving circle
        self.physicsengine_targetlist.append('mcp_mc_collide_mc')# collision player / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_mc_collide_mc')# collision moving circle / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_fc_collide_mc')# collision moving circle / fixed circle as moving circle
        self.physicsengine_targetlist.append('mc_fr_collide_mc')# collision moving circle / fixed rectangle as moving circle
        self.physicsengine_targetlist.append('mc_ft_collide_mc')# collision moving circle / fixed triangle as moving circle
        self.physicsengine_targetlist.append('mc_bf_collide_mc')# interaction moving circle / background force as moving circle
        self.physicsengine_targetlist.append('bc1_bc2_collide_bc1')# collision enemies with holes
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)
    def mcircles_hit(self):
        if once(self,self.hit) and timer(self,True,20) and self.hit:
            sound.play_mult_volume('mcircles',self.hitec/self.hitecmax)# play with a volume multiplier
            timer.reset(self)
    def draw(self):
        func_drawimage(self.imgbody,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)# body
        func_drawimage(self.imghead, (self.xh-self.rad-xcam,screenh-self.yh-self.rad-ycam),self.rad,self.rad)# head
    def movehead(self):# simple own v (spring/dissip) for head movement (doesnt interact with physics engine)
        self.uh = self.uh- self.kspringh*(self.xh-self.x)*dt - self.cdh*self.uh*dt
        self.vh = self.vh- self.kspringh*(self.yh-self.y)*dt - self.cdh*self.vh*dt
        self.xh += self.uh*dt
        self.yh += self.vh*dt
    def hitahole(self):
        if self.hit12: self.kill()# if hit a hole (collision group 1-2), then die
    def kill(self):
        self.creator.enemies.remove(self)
        self.creator.physicsengine.remove_collider(self,self.physicsengine_targetlist)
    def update(self):
        self.hitahole()
        self.movehead()
        self.draw()
        self.mcircles_hit()

# Regular enemy: same weight/radius as player
class obj_enemy1(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy1_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy1_head.png').convert_alpha()
        self.m=self.m0*10
        self.rad=25
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        # self.m=2

# Heavy enemy: big weight and radius
class obj_enemy2(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy2_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy2_head.png').convert_alpha()
        self.m=self.m0*80# (mass is in rad**3 for sphere)
        self.rad=50
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy

# Small enemy: very lightweight and small
class obj_enemy3(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy3_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy3_head.png').convert_alpha()
        self.m=self.m0*2.1
        self.rad=15
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy

# Redux version 60% radius ()
class obj_enemy1small(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy1small_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy1small_head.png').convert_alpha()
        self.m=self.m0*2.1
        self.rad=15
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
class obj_enemy2small(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy2small_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy2small_head.png').convert_alpha()
        self.m=self.m0*17.3
        self.rad=30
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
class obj_enemy3small(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy3small_body.png').convert_alpha()
        self.imghead=pygame.image.load('data/bk_imgenemy3small_head.png').convert_alpha()
        self.m=self.m0*0.47# (mass is in rad**2)
        self.rad=9
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy

# Version under water (less mass)
class obj_enemy1water(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imghead=pygame.image.load('data/bk_imgenemy1_headwater.png').convert_alpha()
        self.m=self.m0*1
        self.rad=25
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy

# Version flying (not affected by background forces )
class obj_enemy1fly(obj_enemy):
    def __init__(self,xspawn,yspawn,creator):
        super().__init__(xspawn,yspawn,creator)# inherit initiatilization from level
        self.imgbody=pygame.image.load('data/bk_imgenemy1fly_body.png').convert_alpha()
        self.m=self.m0*10
        self.rad=25
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
    def add_physics(self):# Add Self to Physics Engine
        self.physicsengine_targetlist=[]# what this object gets from physics engine
        self.physicsengine_targetlist.append('motion')# motion from forces
        self.physicsengine_targetlist.append('playarea')# freezes outside of playing area
        self.physicsengine_targetlist.append('mc_fb_collide_mc')# collision moving circle with fixed boundaries as moving circle
        self.physicsengine_targetlist.append('mcp_mc_collide_mc')# collision player / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_mc_collide_mc')# collision moving circle / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_fc_collide_mc')# collision moving circle / fixed circle as moving circle
        self.physicsengine_targetlist.append('mc_fr_collide_mc')# collision moving circle / fixed rectangle as moving circle
        self.physicsengine_targetlist.append('mc_ft_collide_mc')# collision moving circle / fixed triangle as moving circle
        self.physicsengine_targetlist.append('bc1_bc2_collide_bc1')# collision with holes
        # removed interaction with background forces
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)
    def draw(self):
        func_drawimage(self.imgbody,(self.x-50-xcam,screenh-self.y-self.rad-ycam),50,self.rad)# body
        func_drawimage(self.imghead, (self.xh-self.rad-xcam,screenh-self.yh-self.rad-ycam),self.rad,self.rad)# head
##########################################################
# Level Fixed Elements (with no Physical Collisions)

# Decoration (just draw in the background)
#*DECO
class obj_deco:
    def __init__(self,xspawn,yspawn,radx,rady,image,creator):
        self.img=pygame.image.load(image).convert_alpha()
        self.x=xspawn
        self.y=yspawn
        self.radx=radx# half width
        self.rady=rady
        self.creator = creator# creator= level
        # self.color=(255,50,40)
        # pygame_changesurfacecolor(self.img,self.color)
    def draw(self):
        func_drawimage(self.img,(self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)
    def update(self):
        self.draw()

# Custom decoration that takes the image imposed by the borders
class obj_decocameleon():
    def __init__(self,xspawn,yspawn,radx,rady,color,image,creator):
        self.img=pygame.image.load(image).convert_alpha()
        self.x=xspawn
        self.y=yspawn
        self.radx=radx# half width
        self.rady=rady
        self.creator = creator# creator= level
        self.color=color
        # darken uniformly from background
        if self.creator.background:# take borders color
            self.color=self.creator.background.color
        self.colorch=[self.color[0],self.color[1],self.color[2]]
        for i in [0,1,2]:
            self.colorch[i]=int(self.colorch[i]*0.8)
        self.color=self.colorch[0],self.colorch[1],self.colorch[2]
        pygame_changesurfacecolor(self.img,self.color)
    def draw(self):
        func_drawimage(self.img,(self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)
    def update(self):
        self.draw()


# Hole (Kills Enemies on contact)
# *HOLE
class obj_hole:
    def __init__(self,xspawn,yspawn,radius,image,creator):
        self.img=pygame.image.load(image).convert_alpha()
        self.imghithole=pygame.image.load('data/bk_imghithole.png').convert_alpha()
        self.x=xspawn
        self.y=yspawn
        self.rad=radius
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.hit12=False# hit by group 1-2 (enemies) (determined by physics engine)
        self.ison=False#always read to be hit
        self.killanim=False# play kill animation
        self.timer=0# timer for hit animation
        self.creator = creator# creator= level
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.creator.physicsengine.add_collider(self,['bc1_bc2_collide_bc2'])# Add Self to Physics Engine
        self.active=True
    def draw(self):
        if self.ison or self.killanim:
            func_drawimage(self.imghithole,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
        else:
            func_drawimage(self.img,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
    def timer_hit(self):# start a timer to reset hit
        if not self.ison and self.hit12:
            self.killanim=True
            sound.play('enemyfalls')
        if self.killanim:
            self.timer += 1
            if self.timer>20:
                self.killanim=False
                self.timer=0
    def update(self):
        self.timer_hit()
        self.draw()


class obj_holebig(obj_hole):
    def __init__(self,xspawn,yspawn,radius,image,creator):
        super().__init__(xspawn,yspawn,radius,image,creator)# created by level
        self.imghithole=pygame.image.load('data/bk_imghitholebig.png').convert_alpha()

class obj_holesmall(obj_hole):
    def __init__(self,xspawn,yspawn,radius,image,creator):
        super().__init__(xspawn,yspawn,radius,image,creator)# created by level
        self.imghithole=pygame.image.load('data/bk_imghitholesmall.png').convert_alpha()

# gory animation when hit once
class obj_holebloody(obj_hole):
    def __init__(self,xspawn,yspawn,radius,image,creator):
        super().__init__(xspawn,yspawn,radius,image,creator)# created by level
        self.imgblood=pygame.image.load('data/bk_imghole_blood.png').convert_alpha()
        self.bloodon=False
        self.radblood=50
    def drawblood(self):
        if self.hit12: self.bloodon=True# only activate once
        if self.bloodon:
            func_drawimage(self.imgblood,(self.x-self.radblood-xcam,screenh-self.y-self.radblood-ycam),self.rad,self.rad)
    def update(self):
        self.timer_hit()
        self.draw()
        self.drawblood()

class obj_holebigbloody(obj_holebloody):
    def __init__(self,xspawn,yspawn,radius,image,creator):
        super().__init__(xspawn,yspawn,radius,image,creator)# created by level
        self.imghithole=pygame.image.load('data/bk_imghitholebig.png').convert_alpha()
        self.imgblood=pygame.image.load('data/bk_imgholebig_blood.png').convert_alpha()
        self.radblood=100

class obj_holesmallbloody(obj_holebloody):
    def __init__(self,xspawn,yspawn,radius,image,creator):
        super().__init__(xspawn,yspawn,radius,image,creator)# created by level
        self.imghithole=pygame.image.load('data/bk_imghitholesmall.png').convert_alpha()
        self.imgblood=pygame.image.load('data/bk_imgholesmall_blood.png').convert_alpha()
        self.radblood=30

# Finish Hole (Ends level when reached by player)
# *FINISH
class obj_holefinish():
    def __init__(self,xspawn,yspawn,radius,image,creator):
        self.img=pygame.image.load(image).convert_alpha()
        self.imghithole=pygame.image.load('data/bk_imgholefinishhit.png').convert_alpha()
        self.imgready=pygame.image.load('data/bk_imgholefinishready.png').convert_alpha()
        self.x=xspawn
        self.y=yspawn
        self.rad=radius
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.hit=False# is hit
        self.ready=False# ready to be hit
        self.creator = creator# creator= level
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True
    def draw(self):
        if self.ready:
            if not self.hit:
                func_drawimage(self.imgready,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
            else:
                func_drawimage(self.imghithole,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
        else:
            func_drawimage(self.img,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
    def update(self):
        self.draw()

# Lever Hole (activated when reached once by player)
#*LEVER
class obj_holelever():
    def __init__(self,xspawn,yspawn,radius,image,creator):
        self.img=pygame.image.load(image).convert_alpha()
        self.imghit=pygame.image.load('data/bk_imgholeleverhit.png').convert_alpha()
        self.x=xspawn
        self.y=yspawn
        self.rad=radius# hole radius
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.hit=False
        self.creator = creator# creator= level
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True
    def draw(self):
        if self.hit:
            func_drawimage(self.imghit,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
        else:
            func_drawimage(self.img,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
    def update(self):
        self.draw()


##########################################################
# Level Obstacles (with physical collisions)
# *OBSTACLES
#
# Level Boundaries (for reflections)
# *BOUNDARIES
class obj_boundaries:
    def __init__(self,xmin,xmax,ymin,ymax,radius,color,barcode,creator):
        # margins lists margins on side west,east,south,north
        self.creator=creator#created by level
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
        self.rad=radius# external radius for display (same in x and y)
        self.radx=self.rad# radius in x
        self.rady=self.rad# radius in y
        self.color=color
        self.barcode=barcode# for use by level editor
        #
        self.closedx=True# if the boundary is closed in x (otherwise is periodic)
        self.closedy=True# (this can be changed externally)
        self.setup()# add self to physics engine
        self.hit=False
        self.hitec=0
        self.hitecmax=200
        self.linecolor=(0,0,0)
        self.command=str(self.xmin)+','+str(self.xmax)+','+str(self.ymin)+','+str(self.ymax)+\
            ','+str(self.rad)+','+str(self.color)+',"'+str(self.barcode)+'"'# a command for level editor write
    def setup(self):
        self.creator.physicsengine.add_collider(self,['mc_fb_collide_fb'])# Add Self to Physics Engine
        self.active=True
    def makeperiodicinx(self):# make the x boundaries periodic (call once externally)
        self.closedx=False
        self.xmin=self.xmin-self.radx
        self.xmax=self.xmax+self.radx
    def makeperiodiciny(self):# make the y boundaries periodic (call once externally)
        self.closedy=False
        self.ymin=self.ymin-self.rady
        self.ymax=self.ymax+self.rady
    def draw(self):
        # draw borders by parts (faster than one entire screen)
        # different coordinate systems:
        # pygame xp,yp, my system xs,ys, camera move xc,yc: formula xp=xs-xc, yp=h-ys-yc where h is screenh=600
        if self.closedx:
            func_drawrect( self.color, (self.xmin-self.radx-xcam, screenh-self.ymax-ycam, self.radx, self.ymax-self.ymin), 0)# left
            func_drawrect( self.color, (self.xmax-xcam-2, screenh-self.ymax-ycam, self.radx, self.ymax-self.ymin), 0)# right
        if self.closedy:
            # func_drawrect( self.color, (self.xmin-xcam-self.rad, screenh-self.ymin-ycam-2, self.xmax-self.xmin+2*self.rad-2, self.rad), 0)# bottom +corners
            # func_drawrect( self.color, (self.xmin-xcam-self.rad, screenh-self.ymax-self.rad-ycam, self.xmax-self.xmin+2*self.rad-2, self.rad), 0)# top +corners
            func_drawrect( self.color, (self.xmin-xcam, screenh-self.ymin-ycam-2, self.xmax-self.xmin-2, self.rady), 0)# bottom
            func_drawrect( self.color, (self.xmin-xcam, screenh-self.ymax-self.rady-ycam, self.xmax-self.xmin-2, self.rady), 0)# top
        if self.closedx or self.closedy:
            func_drawrect( self.color, (self.xmin-xcam-self.radx, screenh-self.ymin-ycam-2, self.radx, self.rady+2), 0)# bottom left corner
            func_drawrect( self.color, (self.xmin-xcam-self.radx, screenh-self.ymax-self.rady-ycam, self.radx, self.rady), 0)# top left corner
            func_drawrect( self.color, (self.xmax-xcam-2, screenh-self.ymin-ycam-2, self.radx+2, self.rady+2), 0)# bottom right corner
            func_drawrect( self.color, (self.xmax-xcam-2, screenh-self.ymax-self.rady-ycam, self.radx+2, self.rady), 0)# top right corner

        # outer lines
        if self.closedx:
            func_drawline( self.linecolor, (self.xmin-self.radx-xcam,screenh-self.ymax-self.rady-ycam),(self.xmin-self.radx-xcam,screenh-self.ymin+self.rady-ycam-2), 2)# left
            func_drawline( self.linecolor, (self.xmax+self.radx-xcam-2,screenh-self.ymax-self.rady-ycam),(self.xmax+self.radx-xcam-2,screenh-self.ymin+self.rady-ycam-2), 2)# right
        if self.closedy:
            func_drawline( self.linecolor, (self.xmin-xcam-self.radx, screenh-self.ymin+self.rady-ycam-2), (self.xmax-xcam+self.radx, screenh-self.ymin+self.rady-ycam-2), 2)# bottom
            func_drawline( self.linecolor, (self.xmin-xcam-self.radx, screenh-self.ymax-self.rady-ycam), (self.xmax-xcam+self.radx, screenh-self.ymax-self.rady-ycam), 2)# top
        # iner lines
        if self.closedx and self.closedy:
            func_drawline( self.linecolor, (self.xmin-xcam,screenh-self.ymax-ycam),(self.xmin-xcam,screenh-self.ymin-ycam-2), 2)# left
            func_drawline( self.linecolor, (self.xmax-xcam-2,screenh-self.ymax-ycam),(self.xmax-xcam-2,screenh-self.ymin-ycam-2), 2)# right
            func_drawline( self.linecolor, (self.xmin-xcam, screenh-self.ymin-ycam-2), (self.xmax-xcam-2, screenh-self.ymin-ycam-2), 2)# bottom
            func_drawline( self.linecolor, (self.xmin-xcam, screenh-self.ymax-ycam), (self.xmax-xcam-2, screenh-self.ymax-ycam), 2)# top
        elif self.closedx:# periodic in y only
            func_drawline( self.linecolor, (self.xmin-xcam,screenh-self.ymax-self.rady-ycam),(self.xmin-xcam,screenh-self.ymin+self.rady-ycam-2), 2)# left (extended)
            func_drawline( self.linecolor, (self.xmax-xcam-2,screenh-self.ymax-self.rady-ycam),(self.xmax-xcam-2,screenh-self.ymin+self.rady-ycam-2), 2)# right (extendex)
        elif self.closedy:
            func_drawline( self.linecolor, (self.xmin-self.radx-xcam, screenh-self.ymin-ycam-2), (self.xmax+self.radx-xcam-2, screenh-self.ymin-ycam-2), 2)# bottom  (extended)
            func_drawline( self.linecolor, (self.xmin-self.radx-xcam, screenh-self.ymax-ycam), (self.xmax+self.radx-xcam-2, screenh-self.ymax-ycam), 2)# top (extended)
    def mcircles_hit(self):
        if once(self,self.hit) and timer(self,True,20) and self.hit:
            sound.play_mult_volume('hitbdry',self.hitec/self.hitecmax)# has to unhit bdry to replay
            timer.reset(self)
    def update(self):
        self.draw()
        self.mcircles_hit()


# Version to be used in level editor (doesnt add self to physics engine)
class obj_leveleditorboundaries(obj_boundaries):
    def __init__(self,xmin,xmax,ymin,ymax,radius,color,barcode,creator):
        super().__init__(xmin,xmax,ymin,ymax,radius,color,barcode,creator)# created by level editor
    def setup(self):
        pass# dont add self to physics engine

# Round obsctacles
# *ROUND-OBSTACLES
class obj_roundobstacle:
    def __init__(self,xspawn,yspawn,radius,ccor,ccort,image,creator):
        self.creator = creator# level
        self.x=xspawn# position of center
        self.y=yspawn
        self.u=0# if moves as platform (non-dynamic)
        self.v=0
        self.rad=radius# radius of self
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.ccor=ccor# custom coefficient of restitution
        self.ccort=ccort# custom COR (tangent component): 50% of normal component loss/gain
        self.imgobstacle=pygame.image.load(image).convert_alpha()# image displayed.convert_alpha()
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.creator.physicsengine.add_collider(self,['mc_fc_collide_fc'])# Add Self to Physics Engine
        self.active=True
        self.hit=False
        self.hitec=0
        self.hitecmax=200
        self.type='regular'
        if self.ccor==self.creator.cor_sp and self.ccort==self.creator.cort_sp: self.type='sp'
        if self.ccor==self.creator.cor_pk and self.ccort==self.creator.cort_pk: self.type='pk'
    def mcircles_hit(self):
            if once(self,self.hit) and timer(self,True,20) and self.hit:
                if self.type=='sp': sound.play_mult_volume('hit_sp',self.hitec/self.hitecmax)
                elif self.type=='pk': sound.play_mult_volume('hit_pk',self.hitec/self.hitecmax)
                else: sound.play_mult_volume('hit',self.hitec/self.hitecmax)
                timer.reset(self)
    def draw(self):
        func_drawimage(self.imgobstacle,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
    def update(self):
        self.draw()
        self.mcircles_hit()

# Rectangular obsctacles
# *RECTANGULAR-OBSTACLES
class obj_rectangularobstacle:
    def __init__(self,xspawn,yspawn,xradius,yradius,ccor,ccort,image,creator):
        self.creator = creator# level
        self.x=xspawn
        self.y=yspawn
        self.u=0# if moves as platform (non-dynamic)
        self.v=0
        self.radx=xradius# width
        self.rady=yradius# height
        self.ccor=ccor# custom coefficient of restitution
        self.ccort=ccort# custom COR (tangent component): 50% of normal component loss/gain
        self.imgobstacle=pygame.image.load(image).convert_alpha()
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.creator.physicsengine.add_collider(self,['mc_fr_collide_fr'])# Add Self to Physics Engine
        self.active=True
        self.hit=False
        self.hitec=0
        self.hitecmax=200
        self.type='regular'
        if self.ccor==self.creator.cor_sp and self.ccort==self.creator.cort_sp: self.type='sp'
        if self.ccor==self.creator.cor_pk and self.ccort==self.creator.cort_pk: self.type='pk'
    def mcircles_hit(self):
            if once(self,self.hit) and timer(self,True,20) and self.hit:
                if self.type=='sp': sound.play_mult_volume('hit_sp',self.hitec/self.hitecmax)
                elif self.type=='pk': sound.play_mult_volume('hit_pk',self.hitec/self.hitecmax)
                else: sound.play_mult_volume('hit',self.hitec/self.hitecmax)
                timer.reset(self)
    def draw(self):
        pass
        func_drawimage(self.imgobstacle,(self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)
    def update(self):
        self.draw()
        self.mcircles_hit()


# Right Triangle obsctacles (simpler than full triangles)
# *TRIANGLE-OBSTACLES
class obj_righttriangleobstacle:
    def __init__(self,xspawn,yspawn,radx,rady,side,ccor,ccort,image,creator):
        self.creator = creator# level
        self.imgobstacle=pygame.image.load(image).convert_alpha()
        self.x=xspawn# position of triangle (center of image)
        self.y=yspawn
        self.u=0# if moves as platform (non-dynamic)
        self.v=0
        self.radx=radx# half width of triangle
        self.rady=rady# half height of triangle
        self.side=side# side=1,2,3,4 for largest edge facing NE, NW, SW, SE
        self.ccor=ccor# custom coefficient of restitution
        self.ccort=ccort# custom COR (tangent component): 50% of normal component loss/gain
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.creator.physicsengine.add_collider(self,['mc_ft_collide_ft'])# Add Self to Physics Engine
        self.active=True
        self.hit=False
        self.hitec=0
        self.hitecmax=200
        self.type='regular'
        if self.ccor==self.creator.cor_sp and self.ccort==self.creator.cort_sp: self.type='sp'
        if self.ccor==self.creator.cor_pk and self.ccort==self.creator.cort_pk: self.type='pk'
    def mcircles_hit(self):
            if once(self,self.hit) and timer(self,True,20) and self.hit:
                if self.type=='sp': sound.play_mult_volume('hit_sp',self.hitec/self.hitecmax)
                elif self.type=='pk': sound.play_mult_volume('hit_pk',self.hitec/self.hitecmax)
                else: sound.play_mult_volume('hit',self.hitec/self.hitecmax)
                timer.reset(self)
    def draw(self):
        func_drawimage(self.imgobstacle,(self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)
    def update(self):
        self.draw()
        self.mcircles_hit()


##########################################################
# Level Background Forces
# *FORCE

# Background Force (Empty Canvas)
# (applies force on all some objects through a function)
class obj_force:
    def __init__(self,params,creator):
        self.creator = creator
        self.params=params
        self.creator.physicsengine.add_collider(self,['mc_bf_collide_bf'])# Add Self to Physics Engine
        self.creator.physicsengine.add_collider(self,['playarea'])# freeze outside of play area
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        # no modifications of forces by default
        return(fx,fy,cd)
    def draw(self):
        pass
    def update(self):
        self.draw()

# Custom background force: reset all previous forces in box (invisible)
class obj_forceresetinbox(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]
        self.y=self.params[1]
        self.radx=self.params[2]
        self.rady=self.params[3]
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            fx=0
            fy=0
            # note we dont reset drag
        return(fx,fy,cd)

# Custom background force: rest all previous forces in circle (invisible)
class obj_forceresetincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]
        self.y=self.params[1]
        self.rad=self.params[2]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        if (x-self.x)**2 + (y-self.y)**2<(radius+self.rad)**2:
            fx=0
            fy=0
            # note we dont reset drag
        return(fx,fy,cd)

# Custom background force: viscosity change in box
#*VISCOSITY
class obj_forceviscosityinbox(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.cd=self.params[0]
        self.x=self.params[1]
        self.y=self.params[2]
        self.radx=self.params[3]
        self.rady=self.params[4]
        self.imgforce=params[5]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            cd=cd*self.cd
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# Custom background force: viscosity change in circle
class obj_forceviscosityincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.cd=self.params[0]
        self.x=self.params[1]
        self.y=self.params[2]
        self.rad=self.params[3]
        self.imgforce=params[4]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        if (x-self.x)**2 + (y-self.y)**2<(radius+self.rad)**2:
            cd=cd*self.cd
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)


# Custom background force: gravity in box
# *GRAVITY
class obj_forcegravityinbox(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.radx=self.params[2]
        self.rady=self.params[3]
        self.ampl=self.params[4]
        self.theta=self.params[5]*pi/180
        self.imgforce=params[6]
        self.c0=cos(self.theta)
        self.s0=sin(self.theta)
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            fx=fx+mass*self.ampl*self.c0
            fy=fy+mass*self.ampl*self.s0
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# Custom background force: gravity in circle
class obj_forcegravityincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.ampl=self.params[3]
        self.theta=self.params[4]*pi/180
        self.imgforce=params[5]
        self.c0=cos(self.theta)
        self.s0=sin(self.theta)
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2 + (y-self.y)**2<(radius+self.rad)**2:
            fx=fx+mass*self.ampl*self.c0
            fy=fy+mass*self.ampl*self.s0
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)

# Custom background force: gyre in circle
class obj_forcegyreincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.ampl=self.params[3]# rotation 90 deg
        self.ampla=self.params[4]#attraction/repulsion towards half-radius
        self.imgforce=params[5]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2 + (y-self.y)**2<(radius+self.rad)**2:
            theta=atan2(y-self.y,x-self.x)
            c0=cos(theta)
            s0=sin(theta)
            dist=(x-self.x)*c0+(y-self.y)*s0
            fx=fx+mass*self.ampl*s0+mass*self.ampla*c0*cos(dist/self.rad*pi)
            fy=fy-mass*self.ampl*c0+mass*self.ampla*s0*cos(dist/self.rad*pi)
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)

# Custom background force: gyre everywhere
class obj_forcegyreeverywhere(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.ampl=self.params[3]# rotation 90 deg
        self.ampla=self.params[4]#attraction/repulsion towards center
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        # self.img=self.params[5]# ignored
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        theta=atan2(y-self.y,x-self.x)
        fx=fx+mass*self.ampl*sin(theta)+mass*self.ampla*cos(theta)
        fy=fy-mass*self.ampl*cos(theta)+mass*self.ampla*sin(theta)
        return(fx,fy,cd)

# Custom background force: coriolis in circle
#*CORIOLIS
class obj_forcecoriolisincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.ampl=self.params[3]
        self.imgforce=params[4]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2 + (y-self.y)**2<(radius+self.rad)**2:
            fx=fx+self.ampl*mass*v# coriolis
            fy=fy-self.ampl*mass*u
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)

# Custom background force: coriolis in box
#*CORIOLIS
class obj_forcecoriolisinbox(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.radx=self.params[2]
        self.rady=self.params[3]
        self.ampl=self.params[4]
        self.imgforce=params[5]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            fx=fx+self.ampl*mass*v# coriolis
            fy=fy-self.ampl*mass*u
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# Custom background force: coriolis everywhere
#*CORIOLIS
class obj_forcecorioliseverywhere(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.ampl=self.params[3]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        # self.img=self.params[4]# ignored
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        fx=fx+self.ampl*mass*v# coriolis
        fy=fy-self.ampl*mass*u
        return(fx,fy,cd)

# Custom background force: gravity everywhere
class obj_forcegravityeverywhere(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# image center
        self.y=self.params[1]
        self.rad=self.params[2]# for image display only
        self.ampl=self.params[3]
        self.theta=self.params[4]*pi/180
        self.c0=cos(self.theta)
        self.s0=sin(self.theta)
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        # self.img=self.params[5]# ignored
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        fx=fx+mass*self.ampl*self.c0
        fy=fy+mass*self.ampl*self.s0
        return(fx,fy,cd)

# Custom background force: gravity in circle with 1/d**2 coefficient (planet), acts everywhere
#*PLANET
class obj_forceplanetgravity(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center
        self.y=self.params[1]
        self.rad=self.params[2]# image radius
        self.radmin=self.params[3]# min radius for computing force in 1/r**2
        self.ampl=self.params[4]
        # self.img=self.params[5]# ignored
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        dist2=(x-self.x)**2 + (y-self.y)**2
        theta=atan2(y-self.y,x-self.x)
        dist2=max(dist2,self.radmin**2)# to avoid zero
        fx=fx-self.ampl*cos(theta)/dist2# planet gravity
        fy=fy-self.ampl*sin(theta)/dist2
        return(fx,fy,cd)

# Custom background force: gravity in circle with 1/d coefficient (planet)
#*PLANET
class obj_forceplanetgravity_1od(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center
        self.y=self.params[1]
        self.rad=self.params[2]# image radius
        self.radmin=self.params[3]# min radius for computing force in 1/r**2
        self.ampl=self.params[4]
        # self.img=self.params[5]# ignored
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        dist=sqrt((x-self.x)**2 + (y-self.y)**2)
        theta=atan2(y-self.y,x-self.x)
        dist=max(dist,self.radmin)# to avoid zero
        fx=fx-self.ampl*cos(theta)/dist# planet gravity
        fy=fy-self.ampl*sin(theta)/dist
        return(fx,fy,cd)

# Custom background force: gravity in circle with cte coefficient (planet)
#*PLANET
class obj_forceplanetgravity_cte(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center
        self.y=self.params[1]
        self.rad=self.params[2]# image radius
        self.radmin=self.params[3]# min radius for computing force in 1/r**2
        self.ampl=self.params[4]
        # self.img=self.params[5]# ignored
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        theta=atan2(y-self.y,x-self.x)
        fx=fx-self.ampl*cos(theta)# planet gravity
        fy=fy-self.ampl*sin(theta)
        return(fx,fy,cd)

# Custom background force: spring in circle (attracts to center, or pushes)
#*SPRING
class obj_forcespringincircle(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.rad=self.params[2]
        self.kspring=self.params[3]
        self.imgforce=self.params[4]
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        dist2=(x-self.x)**2 + (y-self.y)**2
        if dist2<(radius+self.rad)**2:
            theta=atan2(y-self.y,x-self.x)
            c0=cos(theta)
            s0=sin(theta)
            dist=sqrt(dist2)
            fx=fx - self.kspring*dist*c0
            fy=fy - self.kspring*dist*s0
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)

# Custom background force: spring in box (attracts to center lines differently on x and y)
# in inverted makes a perfect trampoline!
class obj_forcespringinbox(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.radx=self.params[2]
        self.rady=self.params[3]
        self.kspringx=self.params[4]
        self.kspringy=self.params[5]
        self.imgforce=self.params[6]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            fx=fx - self.kspringx*(x-self.x)
            fy=fy - self.kspringy*(y-self.y)
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# Custom background force: spring in box doesnt account for mass: perfect trampoline!
class obj_forcespringinboxnomass(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# gyre center
        self.y=self.params[1]
        self.radx=self.params[2]
        self.rady=self.params[3]
        self.kspringx=self.params[4]
        self.kspringy=self.params[5]
        self.imgforce=self.params[6]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        if (x-self.x)**2<(radius+self.radx)**2 and (y-self.y)**2<(radius+self.rady)**2:
            fx=fx - self.kspringx*(x-self.x)*mass
            fy=fy - self.kspringy*(y-self.y)*mass
        return(fx,fy,cd)
    def draw(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)
##########################################################
# Environments = combinations of several forces
# *ENVIRONMENTS

# Custom background force: water environment (no image)
class obj_forceenvwater(obj_force):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# image center
        self.y=self.params[1]
        self.ampl=self.params[2]
        self.creator=creator
        self.creator.useshotswimsound=True
        self.creator.physicsengine.remove_collider(self,['playarea'])# acts everywhere even outside playarea
    def __call__(self,x,y,u,v,fx,fy,mass,radius,cd):# redefine function
        fx=fx
        fy=fy+mass*self.ampl
        return(fx,fy,cd)
    def draw(self):
        pass

##########################################################

# Operators (Empty Canvas)
# *OPERATORS
# (applies operation of any type on objects through a function)
# e.g. turn on interruptor, move object (no physics involved), etc..
class obj_ops:
    def __init__(self,params,creator):
        self.creator = creator
        self.params=params
        self.targets=[]# list of targets in level affected by the operator
    def setup(self):# setup (is executed during level setup, AFTER all level content is loaded because it targets it)
        pass
    def operate(self):# the operator!
        pass

# Operator Cliff box: Displaces object to given position if is in fall area (and stops it)
# Draws an image (where fall area is transparent) and compares pixel colors to the background.
# This means a uniform background (with background.color) must be loaded!
#*CLIFF
class obj_opscliffbox(obj_ops):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center of image
        self.y=self.params[1]
        self.radx=self.params[2]# image radius
        self.rady=self.params[3]# image radius
        self.xfall=self.params[4]# where to fall (relative to center of image)
        self.yfall=self.params[5]# yfall is with respect to screen orientation
        self.colorfall=self.params[6]# default color to determine fall areas
        self.img=pygame.image.load(self.params[7]).convert_alpha()# image containing the cliff.convert_alpha()
        self.targets=[]#
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True

    def setup(self):
        if self.creator.player: self.targets.append(self.creator.player)
        if self.creator.enemies:
            for i in self.creator.enemies: self.targets.append(i)
    def operate(self):# redefine function
        func_drawimage(self.img, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)# draw the fall image
        for i in self.targets:
            if (i.x-self.x)**2<self.radx**2 and (i.y-self.y)**2<self.rady**2:
                colorread=screen.get_at((int(i.x),screenh-int(i.y)))# get color at object positoin
                if colorread==self.colorfall:
                    sound.play('clifffall')
                    [i.x,i.y,i.u,i.v]=[self.xfall,screenh-self.yfall,0,0]
                    [i.fx,i.fy,i.xh,i.yh]=[0,0,self.xfall,screenh-self.yfall]

#  A player or eneemy repositioner if needed
# give replace coordinates to other objects
# finds cliffs/traps in existing level objects and changes their replace positions
#*POSITIONER
class obj_opspositioner(obj_ops):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center of image and where to replace stuff
        self.y=self.params[1]
        self.radx=self.params[2]# image radius
        self.rady=self.params[3]# image radius
        self.imgops=params[4]
        if self.imgops:
            self.imgops=pygame.image.load(self.imgops).convert_alpha()
    def setup(self):
        if self.creator.ops:
            for i in self.creator.ops:# scroll all level ops to see if they need to replace
                if str(i.__class__.__name__)=='obj_opscliffbox':
                    i.xfall=self.x
                    i.yfall=screenh-self.y
                    print('found')
    def operate(self):# redefine function
        self.draw()
    def draw(self):
        if self.imgops: func_drawimage(self.imgops, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

# Round moving circle (not an ops but not a fixed obstacle either....)
# adds self to round obstacles....
# *MOVING
class obj_movingcircle:
    def __init__(self,params,creator):
        self.creator = creator# level
        self.x=params[0]# position of center
        self.y=params[1]
        self.rad=params[2]# radius of self
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.m=self.creator.m0*params[3]
        self.cd0=self.creator.cd0*params[4]
        self.ccor=params[5]
        self.ccort=params[6]
        self.imgobstacle=pygame.image.load(params[7]).convert_alpha()# image displayed.convert_alpha()
        self.active=True# is within playing area and subject to updates/interactions
        self.u=0
        self.v=0
        self.fx=0
        self.fy=0
        self.cd=self.cd0
        self.xh=0# not used but needed for collision with boundaries
        self.yh=0
        self.hit=False
        self.hitec=0
        self.hitecmax=200
        self.physicsengine_targetlist=[]# what this object gets from physics engine
        self.physicsengine_targetlist.append('playarea')# freezes outside of playing area
        self.physicsengine_targetlist.append('motion')# motion from forces
        self.physicsengine_targetlist.append('mc_fb_collide_mc')# collision moving circle with fixed boundaries as moving circle
        self.physicsengine_targetlist.append('mcp_mc_collide_mc')# collision player / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_mc_collide_mc')# collision moving circle / moving circle as moving circle
        self.physicsengine_targetlist.append('mc_fc_collide_mc')# collision moving circle / fixed circle as moving circle
        self.physicsengine_targetlist.append('mc_fr_collide_mc')# collision moving circle / fixed rectangle as moving circle
        self.physicsengine_targetlist.append('mc_ft_collide_mc')# collision moving circle / fixed triangle as moving circle
        self.physicsengine_targetlist.append('mc_bf_collide_mc')# interaction moving circle / background force as moving circle
        self.dobforce=True# is subject to background forces. Can be toggled
        self.addtophysics()
    def addtophysics(self):
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)
    def mcircles_hit(self):
        if self.hit:
            sound.play_mult_volume('mcircles',self.hitec/self.hitecmax)# play with a volume multiplier
            self.hit=False
    def draw(self):
        func_drawimage(self.imgobstacle,(self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
    def update(self):
        self.draw()
        self.mcircles_hit()


# Moving circle 4dir: behaves as moving circle except only goes in 4 directions
class obj_movingcircle4dir(obj_movingcircle):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.creator = creator# level
    def addtophysics(self):
        self.physicsengine_targetlist.append('motion_4dir')# only move in 4 directions
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)

# Moving circle 2dirx: behaves as moving circle except only goes right or left
class obj_movingcircle2dirx(obj_movingcircle):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.creator = creator# level
    def addtophysics(self):
        self.physicsengine_targetlist.append('motion_2dirx')# only move in 4 directions
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)

# Moving circle 2dirx: behaves as moving circle except only goes up or down
class obj_movingcircle2diry(obj_movingcircle):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.creator = creator# level
    def addtophysics(self):
        self.physicsengine_targetlist.append('motion_2diry')# only move in 4 directions
        self.creator.physicsengine.add_collider(self,self.physicsengine_targetlist)



# Interactor platform: displaces target objects on a timer (invisible)
# *PLATFORM
class obj_opsplatform(obj_ops):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center of image
        self.y=self.params[1]
        self.radx=self.params[2]# image size (for display and playarea detection)
        self.rady=self.params[3]#
        self.duration=self.params[4]# duration of platform half- cycle
        self.dx=self.params[5]# increment per frame
        self.dy=self.params[6]#
        self.startsign=self.params[7]# initial time start sign
        self.targets=[]#
        self.timer=self.duration
        self.way=sign(self.startsign)
        self.hitside=False
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True
    def setup(self):
        if self.creator.obstacles:
            for i in self.creator.obstacles:
                if (i.x-self.x)**2<self.radx**2 and (i.y-self.y)**2<self.rady**2:
                    self.targets.append(i)
    def operate(self):# redefine function
        # global dt# problem: doesnt change, probably just takes first value
        self.timer -= dt
        if self.timer<0:
            self.timer=self.duration
            self.way=-self.way
        for i in self.targets:
            i.u=self.way*self.dx
            i.v=self.way*self.dy
            i.x=i.x + i.u*dt
            i.y=i.y + i.v*dt
            if i.x<=self.x-self.radx:
                i.x=self.x-self.radx
                i.u=0
                self.hitside=True
            if i.x>=self.x+self.radx:
                i.x=self.x+self.radx
                i.u=0
                self.hitside=True
            if i.y<=self.y-self.rady:
                i.y=self.y-self.rady
                i.v=0
                self.hitside=True
            if i.y>=self.y+self.rady:
                i.y=self.y+self.rady
                i.v=0
                self.hitside=True


# shrinker: replaces player and enemy by their smaller/bigger version (onl)
#*SHRINKER
# Note we still use the SAME OBJECTS just change their properties
class obj_opsshrinker(obj_ops):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# center of image
        self.y=self.params[1]
        self.rad=self.params[2]# image size (just for display)
        self.radx=self.rad# radiusx
        self.rady=self.rad# radiusy
        self.img=pygame.image.load(params[3]).convert_alpha()
        self.imghit=pygame.image.load(params[4]).convert_alpha()
        self.targetnames=[]# name obj of targets
        self.imgbodylist=[]# make a copy of all target images (to avoid deterioarating image quality with multiple rescale)
        self.imgheadlist=[]
        self.hit=False# if has been hit
        self.hitduration=50
        self.timer=self.hitduration
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True
    def setup(self):
        if self.creator.player:
            self.targets.append(self.creator.player)
        if self.creator.enemies:
            for i in self.creator.enemies: self.targets.append(i)
        for i in self.targets:
            self.targetnames.append(str(i.__class__.__name__))
            self.imgbodylist.append(pygame.transform.scale(i.imgbody.copy(),(self.rad*2,self.rad*2)))
            self.imgheadlist.append(pygame.transform.scale(i.imghead.copy(),(self.rad*2,self.rad*2)))
    def operate(self):# redefine function
        if self.active:
            self.draw()
            if self.hit: self.timer -= 1
            if self.timer<0: self.hit=False
            for ic,i in enumerate(self.targets):
                if i.active and (i.x-self.x)**2+(i.y-self.y)**2<(self.rad+i.rad)**2:
                    # if any(str(i.__class__.__name__)==j for j in self.targetnames):
                    if str(i.__class__.__name__)==self.targetnames[ic]:
                        if i.rad != self.rad:
                            self.hit=True
                            self.timer=self.hitduration
                            i.imgbody=self.imgbodylist[ic]
                            i.imghead=self.imgheadlist[ic]
                            sound.play('shrink')
                            [i.rad,i.m]=[self.rad,i.m/(i.rad**3)*(self.rad**3)]
                            # if str(i.__class__.__name__)=='obj_player':
                                # self.creator.gunmanager.gun.maxshoot=self.creator.gunmanager.gun.maxshoot*(i.rad**3)/(self.rad**3)

    def draw(self):
        if self.hit:
            func_drawimage(self.imghit, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)
        else:
            func_drawimage(self.img, (self.x-self.rad-xcam,screenh-self.y-self.rad-ycam),self.rad,self.rad)


# Ops: just draw a background image
# no need to add to play area
class obj_opsbackground(obj_ops):
    def __init__(self,params,creator):
        super().__init__(params,creator)
        self.x=self.params[0]# image center
        self.y=self.params[1]
        self.radx=self.params[2]# image center
        self.rady=self.params[3]
        self.imgforce=params[4]
        if self.imgforce:
            self.imgforce=pygame.image.load(self.imgforce).convert_alpha()
        self.creator.physicsengine.add_collider(self,['playarea'])# Add Self to Physics Engine
        self.active=True
    def operate(self):
        if self.imgforce: func_drawimage(self.imgforce, (self.x-self.radx-xcam,screenh-self.y-self.rady-ycam),self.radx,self.rady)

##########################################################
##########################################################
##########################################################
# Playing Area
#*AREA
# Rectangular area (slightly off edges) outside of which updates/interactions stop: HUGE resource saver
# this area moves with the camera (use xs=xg-xcam, ys=screenh-yg-ycam to go from game to screen coordinates)
class obj_playarea:
    def __init__(self,creator):
        self.creator=creator# created by a level
        self.dplay=self.creator.dplay# distance from screen edges for play area
    def __call__(self,x,y,radx,rady):# determine if an element is in play area
        if x+radx-xcam<-self.dplay or x-radx-xcam>screenw+self.dplay or screenh-y+rady-ycam<-self.dplay or screenh-y-rady-ycam>screenh+self.dplay:
            return False
        else:
            return True

##########################################################
##########################################################

# Physical Engine: manages physical interactions between objects in level
#*PHYSICS *ENGINE
# For example forces, motion and collisions
# use VERY COARSE approximations as even lowest geometry computation reduce FPS too much
class obj_physicsengine:
    def __init__(self,creator):
        self.creator=creator# created by a level
        #
        # Physics Engine Parameters
        # (some not listed are global because of multiple uses in level editor)
        #
        # Lists of collisions
        self.list_playarea=[]# list of objects that check if they are in playing area
        self.list_motion=[]# list of objects that are applied motion by the physics engine
        self.list_motion_4dir=[]# list of objects with motion restrained to only 4 directions
        self.list_motion_2dirx=[]# list of objects with motion restrained to only left right
        self.list_motion_2diry=[]# list of objects with motion restrained to only up down
        self.list_mcircle_fbdry_collide_mcircle=[]# list of mobile circles applied collision with fixed boundaries
        self.list_mcircle_fbdry_collide_fbdry=[]# list of fixed borders applied collision with fixed boundaries
        self.list_mcircle_mcircle_collide_mcircle=[]# list of mobile circles applied collision between mobile and mobile circles
        self.list_mcircleply_mcircle_collide_mcircleply=[]# variant player vs enemies
        self.list_mcircleply_mcircle_collide_mcircle=[]# variant player vs enemies
        self.list_mcircle_fcircle_collide_mcircle=[]# list of mobile circles applied collision between mobile and fixed circles
        self.list_mcircle_fcircle_collide_fcircle=[]# list of fixed circles applied collision between mobile and fixed circles
        self.list_mcircle_frect_collide_mcircle=[]# list of mobile circles applied collision between mobile and fixed rectangles
        self.list_mcircle_frect_collide_frect=[]# list of fixed rectangles applied collision between mobile and fixed rectangles
        self.list_mcircle_ftrian_collide_mcircle=[]# list of mobile circles applied collision between mobile and fixed triangles
        self.list_mcircle_ftrian_collide_ftrian=[]# list of fixed triangles applied collision between mobile and fixed triangles
        self.list_mcircle_bforce_collide_mcircle=[]# list of mobile circles applied interaction mobile circle/background force
        self.list_mcircle_bforce_collide_bforce=[]# list of background forces applied interaction mobile circle/background force
        self.list_bcircle1_bcircle2_collide_bcircle1=[]# list of boolean circles applied collision between group1 and group 2
        self.list_bcircle1_bcircle2_collide_bcircle2=[]# list of boolean circles applied collision between group1 and group 2

    def add_collider(self,collider,targetlist):
        # collider is the object , and targetlist=['mobile','circles'] names all lists it should be added to
        if any(i=='playarea' for i in targetlist):       self.list_playarea.append(collider)
        if any(i=='motion' for i in targetlist):         self.list_motion.append(collider)
        if any(i=='motion_4dir' for i in targetlist):    self.list_motion_4dir.append(collider)
        if any(i=='motion_2dirx' for i in targetlist):    self.list_motion_2dirx.append(collider)
        if any(i=='motion_2diry' for i in targetlist):    self.list_motion_2diry.append(collider)
        if any(i=='mc_fb_collide_mc' for i in targetlist): self.list_mcircle_fbdry_collide_mcircle.append(collider)
        if any(i=='mc_fb_collide_fb' for i in targetlist): self.list_mcircle_fbdry_collide_fbdry.append(collider)
        if any(i=='mc_mc_collide_mc' for i in targetlist): self.list_mcircle_mcircle_collide_mcircle.append(collider)
        if any(i=='mcp_mc_collide_mcp' for i in targetlist): self.list_mcircleply_mcircle_collide_mcircleply.append(collider)
        if any(i=='mcp_mc_collide_mc' for i in targetlist): self.list_mcircleply_mcircle_collide_mcircle.append(collider)
        if any(i=='mc_fc_collide_mc' for i in targetlist): self.list_mcircle_fcircle_collide_mcircle.append(collider)
        if any(i=='mc_fc_collide_fc' for i in targetlist): self.list_mcircle_fcircle_collide_fcircle.append(collider)
        if any(i=='mc_fr_collide_mc' for i in targetlist): self.list_mcircle_frect_collide_mcircle.append(collider)
        if any(i=='mc_fr_collide_fr' for i in targetlist): self.list_mcircle_frect_collide_frect.append(collider)
        if any(i=='mc_ft_collide_mc' for i in targetlist): self.list_mcircle_ftrian_collide_mcircle.append(collider)
        if any(i=='mc_ft_collide_ft' for i in targetlist): self.list_mcircle_ftrian_collide_ftrian.append(collider)
        if any(i=='mc_bf_collide_mc' for i in targetlist): self.list_mcircle_bforce_collide_mcircle.append(collider)
        if any(i=='mc_bf_collide_bf' for i in targetlist): self.list_mcircle_bforce_collide_bforce.append(collider)
        if any(i=='bc1_bc2_collide_bc1' for i in targetlist): self.list_bcircle1_bcircle2_collide_bcircle1.append(collider)
        if any(i=='bc1_bc2_collide_bc2' for i in targetlist): self.list_bcircle1_bcircle2_collide_bcircle2.append(collider)


    def remove_collider(self,collider,targetlist):
        if any(i=='playarea' for i in targetlist):
            if self.list_playarea.remove(collider): self.list_playarea.remove(collider)
        if any(i=='motion' for i in targetlist):
            if self.list_motion.remove(collider): self.list_motion.remove(collider)
        if any(i=='motion_4dir' for i in targetlist):
            if self.list_motion_4dir.remove(collider): self.list_motion_4dir.remove(collider)
        if any(i=='motion_2dirx' for i in targetlist):
            if self.list_motion_2dirx.remove(collider): self.list_motion_2dirx.remove(collider)
        if any(i=='motion_2diry' for i in targetlist):
            if self.list_motion_2diry.remove(collider): self.list_motion_2diry.remove(collider)
        if any(i=='mc_fb_collide_mc' for i in targetlist):
            if self.list_mcircle_fbdry_collide_mcircle: self.list_mcircle_fbdry_collide_mcircle.remove(collider)
        if any(i=='mc_fb_collide_fb' for i in targetlist):
            if self.list_mcircle_fbdry_collide_fbdry: self.list_mcircle_fbdry_collide_fbdry.remove(collider)
        if any(i=='mc_mc_collide_mc' for i in targetlist):
            if self.list_mcircle_mcircle_collide_mcircle: self.list_mcircle_mcircle_collide_mcircle.remove(collider)
        if any(i=='mcp_mc_collide_mcp' for i in targetlist):
            if self.list_mcircleply_mcircle_collide_mcircleply: self.list_mcircleply_mcircle_collide_mcircleply.remove(collider)
        if any(i=='mcp_mc_collide_mc' for i in targetlist):
            if self.list_mcircleply_mcircle_collide_mcircle: self.list_mcircleply_mcircle_collide_mcircle.remove(collider)
        if any(i=='mc_fc_collide_mc' for i in targetlist):
            if self.list_mcircle_fcircle_collide_mcircle: self.list_mcircle_fcircle_collide_mcircle.remove(collider)
        if any(i=='mc_fc_collide_fc' for i in targetlist):
            if self.list_mcircle_fcircle_collide_fcircle: self.list_mcircle_fcircle_collide_fcircle.remove(collider)
        if any(i=='mc_fr_collide_mc' for i in targetlist):
            if self.list_mcircle_frect_collide_mcircle: self.list_mcircle_frect_collide_mcircle.remove(collider)
        if any(i=='mc_fr_collide_fr' for i in targetlist):
            if self.list_mcircle_frect_collide_frect: self.list_mcircle_frect_collide_frect.remove(collider)
        if any(i=='mc_ft_collide_mc' for i in targetlist):
            if self.list_mcircle_ftrian_collide_mcircle: self.list_mcircle_ftrian_collide_mcircle.remove(collider)
        if any(i=='mc_ft_collide_ft' for i in targetlist):
            if self.list_mcircle_ftrian_collide_ftrian: self.list_mcircle_ftrian_collide_ftrian.remove(collider)
        if any(i=='mc_bf_collide_mc' for i in targetlist):
            if self.list_mcircle_bforce_collide_mcircle: self.list_mcircle_bforce_collide_mcircle.remove(collider)
        if any(i=='mc_bf_collide_bf' for i in targetlist):
            if self.list_mcircle_bforce_collide_bforce: self.list_mcircle_bforce_collide_bforce.remove(collider)
        if any(i=='bc1_bc2_collide_bc1' for i in targetlist):
            if self.list_bcircle1_bcircle2_collide_bcircle1: self.list_bcircle1_bcircle2_collide_bcircle1.remove(collider)
        if any(i=='bc1_bc2_collide_bc2' for i in targetlist):
            if self.list_bcircle1_bcircle2_collide_bcircle2: self.list_bcircle1_bcircle2_collide_bcircle2.remove(collider)

    def playarea_activate(self):
        if self.list_playarea:
            for i in self.list_playarea: i.active=self.creator.playarea(i.x,i.y,i.radx,i.rady)

    def motion_applyspeed(self,dtrun):# apply momentum equations on moving objects
        if self.list_motion:
            for i in self.list_motion:
                if i.active: [i.u,i.v]=motion_physicsspeed(i.u,i.v,i.fx,i.fy,i.m,i.cd,dtrun)

    def motion_applyposition(self,dtrun):# apply momentum equations on moving objects
        if self.list_motion:
            for i in self.list_motion:
                if i.active: [i.x,i.y]=motion_physicsposition(i.x,i.y,i.u,i.v,dtrun)

    def motion_4dir(self):# apply momentum equations on moving objects
        if self.list_motion_4dir:
            for i in self.list_motion_4dir:
                if i.active: [i.u,i.v]=motion_to4dir(i.u,i.v)

    def motion_2dirx(self):# apply momentum equations on moving objects
        if self.list_motion_2dirx:
            for i in self.list_motion_2dirx:
                if i.active: [i.u,i.v]=motion_to2dirx(i.u,i.v)

    def motion_2diry(self):# apply momentum equations on moving objects
        if self.list_motion_2diry:
            for i in self.list_motion_2diry:
                if i.active: [i.u,i.v]=motion_to2diry(i.u,i.v)

    def motion_resetforcesanddrag(self):# reset forces/drag for mobile objects
        if self.list_motion:
            for i in self.list_motion: [i.fx,i.fy,i.cd]=[0,0,i.cd0]# we reset even outside of play area!

    def motion_stopslow(self):# stop mobile objects if they are too slow
        if self.list_motion:
            for i in self.list_motion:
                if i.active and i.u**2+i.v**2<self.minspeed**2: [i.u,i.v]=[0,0]

    def motion_checkallslow(self,targetspeed):# if asked by external program, check if all mobile objects are under min speed
        if self.list_motion:
            allslow=True# assumed slow
            for i in self.list_motion: # we check even outside play area!
                if i.u**2+i.v**2>targetspeed**2:
                    allslow=False
                    break
        return allslow

    def collide_mcircle_fbdry(self):# collide mobile circles with fixed boundaries (changes xh,yh=head position as well, e.g. periodic bdry)
        if self.list_mcircle_fbdry_collide_mcircle and self.list_mcircle_fbdry_collide_fbdry:
            for i in self.list_mcircle_fbdry_collide_mcircle:
                if i.active:
                    for j in self.list_mcircle_fbdry_collide_fbdry:
                        [i.x,i.y,i.u,i.v,i.fx,i.fy,i.xh,i.yh,hit,hitec]=\
                            mcirclefbdry_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.rad,i.xh,i.yh,\
                                             j.xmin,j.xmax,j.ymin,j.ymax,j.closedx,j.closedy,self.creator.cor_bdry,self.creator.cort_bdry)
                        if hit:
                            j.hit=hit
                            j.hitec=hitec

    def collide_mcircleply_mcircle(self):# collide player with mobile circles
        if self.list_mcircleply_mcircle_collide_mcircleply and self.list_mcircleply_mcircle_collide_mcircle:
            for i in self.list_mcircleply_mcircle_collide_mcircleply:
                if i.active:
                    for j in self.list_mcircleply_mcircle_collide_mcircle:
                        if j.active:
                            [i.x,i.y,i.u,i.v,i.fx,i.fy,j.x,j.y,j.u,j.v,j.fx,j.fy,hit,hitec]=\
                                mcirclemcircle_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,\
                                                   j.x,j.y,j.u,j.v,j.fx,j.fy,j.m,j.rad,self.creator.cor_mc,self.creator.cort_mc,dtp)
                            if hit:
                                j.hit=hit
                                j.hitec=hitec

    def collide_mcircle_mcircle(self):# collide mobile circles with mobile circles
    # (BEWARE: Here an element from list i collides with NEXT elements from list j !)
        if len(self.list_mcircle_mcircle_collide_mcircle)>1:
            for ic,i in enumerate(self.list_mcircle_mcircle_collide_mcircle):
                if i.active:
                    for jc,j in list(enumerate(self.list_mcircle_mcircle_collide_mcircle))[ic+1:]:# enumerate starting from ic+1 element
                        if j.active:
                            [i.x,i.y,i.u,i.v,i.fx,i.fy,j.x,j.y,j.u,j.v,j.fx,j.fy,hit,hitec]=\
                                mcirclemcircle_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,\
                                                   j.x,j.y,j.u,j.v,j.fx,j.fy,j.m,j.rad,self.creator.cor_mc,self.creator.cort_mc,dtp)
                            if hit: # only one in the pair plays the sound
                                i.hit=hit
                                i.hitec=hitec

    def collide_mcircle_fcircle(self):# collide mobile circles with fixed circles
        if self.list_mcircle_fcircle_collide_mcircle and self.list_mcircle_fcircle_collide_fcircle:
            for i in self.list_mcircle_fcircle_collide_mcircle:
                if i.active:
                    for j in self.list_mcircle_fcircle_collide_fcircle:
                        if j.active:
                            [i.x,i.y,i.u,i.v,i.fx,i.fy,hit,hitec]=\
                                mcirclefcircle_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,\
                                                   j.x,j.y,j.u,j.v,j.rad,j.ccor,j.ccort,dtp)
                            if hit:
                                j.hit=hit
                                j.hitec=hitec

    def collide_mcircle_frect(self):# collide mobile circles with fixed rectangles
        if self.list_mcircle_frect_collide_mcircle and self.list_mcircle_frect_collide_frect:
            for i in self.list_mcircle_frect_collide_mcircle:
                if i.active:
                    for j in self.list_mcircle_frect_collide_frect:
                        if j.active:
                            [i.x,i.y,i.u,i.v,i.fx,i.fy,hit,hitec]=\
                                mcirclefrect_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,\
                                                  j.x,j.y,j.u,j.v,j.radx,j.rady,j.ccor,j.ccort,dtp)
                            if hit:
                                j.hit=hit
                                j.hitec=hitec

    def collide_mcircle_ftrian(self):# collide mobile circles with fixed rectangles
        if self.list_mcircle_ftrian_collide_mcircle and self.list_mcircle_ftrian_collide_ftrian:
            for i in self.list_mcircle_ftrian_collide_mcircle:
                if i.active:
                    for j in self.list_mcircle_ftrian_collide_ftrian:
                        if j.active:
                            [i.x,i.y,i.u,i.v,i.fx,i.fy,hit,hitec]=\
                                mcircleftrian_hit(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,\
                                                  j.x,j.y,j.u,j.v,j.radx,j.rady,j.side,j.ccor,j.ccort,dtp)
                            if hit:
                                j.hit=hit
                                j.hitec=hitec

    def collide_mcircle_bforce(self):# collide mobile circles with background forces
        # (BEWARE: the background forces are functions!)
        if self.list_mcircle_bforce_collide_mcircle and self.list_mcircle_bforce_collide_bforce:
            for i in self.list_mcircle_bforce_collide_mcircle:
                if i.active:
                    if i.dobforce:
                        for j in self.list_mcircle_bforce_collide_bforce:
                            [i.fx,i.fy,i.cd]=j(i.x,i.y,i.u,i.v,i.fx,i.fy,i.m,i.rad,i.cd)


    def collide_bcircle1_bcircle2(self):# collide circles group 1 and 2 (no physics, only boolean)
        if self.list_bcircle1_bcircle2_collide_bcircle1 and self.list_bcircle1_bcircle2_collide_bcircle1:
            for i in self.list_bcircle1_bcircle2_collide_bcircle1:
                if i.active: i.hit12=False# reset all
            for j in self.list_bcircle1_bcircle2_collide_bcircle2:
                if j.active: j.hit12=False# reset all
            for i in self.list_bcircle1_bcircle2_collide_bcircle1:
                if i.active:
                    for j in self.list_bcircle1_bcircle2_collide_bcircle2:
                        if j.active:
                            hit=bcirclebcircle_hit(i.x,i.y,i.rad,j.x,j.y,j.rad)
                            if hit and i.rad<=j.rad:
                                i.hit12=True
                                j.hit12=True

    def reset_hits(self):# reset all hits from previous update (used to make collision sounds except for boolean collisions)
        # (BEWARE: the background forces are functions!)
        if self.list_mcircle_fbdry_collide_mcircle:
            for i in self.list_mcircle_fbdry_collide_mcircle: i.hit=False
        if self.list_mcircle_fbdry_collide_fbdry:
            for i in self.list_mcircle_fbdry_collide_fbdry: i.hit=False
        if self.list_mcircle_mcircle_collide_mcircle:
            for i in self.list_mcircle_mcircle_collide_mcircle: i.hit=False
        if self.list_mcircle_fcircle_collide_mcircle:
            for i in self.list_mcircle_fcircle_collide_mcircle: i.hit=False
        if self.list_mcircle_fcircle_collide_fcircle:
            for i in self.list_mcircle_fcircle_collide_fcircle: i.hit=False
        if self.list_mcircle_frect_collide_mcircle:
            for i in self.list_mcircle_frect_collide_mcircle: i.hit=False
        if self.list_mcircle_frect_collide_frect:
            for i in self.list_mcircle_frect_collide_frect: i.hit=False
        if self.list_mcircle_ftrian_collide_mcircle:
            for i in self.list_mcircle_ftrian_collide_mcircle: i.hit=False
        if self.list_mcircle_ftrian_collide_ftrian:
            for i in self.list_mcircle_ftrian_collide_ftrian: i.hit=False

    def update(self):
        #
        # At beginning of update, creator=level may modify forces and speed/position (e.g. from player controls)
        # Solve over several physical timesteps dtp=dt/mts for one game timestep
        #
        self.reset_hits()# reset hits from collisions (used to play sounds)
        #
        # Forces and drag (fx,fy,cd) are updated each dt but motion (u,v,x,y) at refined dtp for collisions detection
        for i in range(mts):
            #
            if self.creator.doplayarea: self.playarea_activate()# process only objects in play area (possible glitches at limits but huge resource saver)
            self.motion_applyspeed(dtp)# move motion objects (momentum equations)
            self.motion_4dir()# restrict motion to 4 directions for some objects
            self.motion_2dirx()# restrict motion to left right for some objects
            self.motion_2diry()# restrict motion to up down for some objects
            self.motion_applyposition(dtp)# move motion objects (momentum equations)
            #
            self.collide_mcircleply_mcircle()# collisions player / moving circles
            self.collide_mcircle_mcircle()# collisions moving circles / moving circles
            #
            self.collide_mcircle_fcircle()# collisions moving circles / fixed circles
            self.collide_mcircle_frect()# collisions moving circles / fixed rectangles
            self.collide_mcircle_ftrian()# collisions moving circles / fixed right triangles
            self.collide_mcircle_fbdry()# collisions moving circles / fixed boundaries
            #
            self.collide_bcircle1_bcircle2()# collisions (no physics) circle group1 vs group 2 (used for enemies vs holes)
            #
        self.motion_resetforcesanddrag()# reset force and drag of moving objects
        #
        self.collide_mcircle_bforce()# add background forces on moving circles (put right before player forces due to reset boxes)
        #
        # Important: bforce are at the end because "reset force" may cancel forces from player controls



##########################################################
##########################################################
##########################################################

# motion: Update speed/position from forces
def motion_physics(x,y,u,v,fx,fy,mass,drag,dt):
    u=u+fx/mass*dt-u*drag*dt
    v=v+fy/mass*dt-v*drag*dt
    x=x+dt*u
    y=y+dt*v
    return(x,y,u,v)

# motion: speed part
def motion_physicsspeed(u,v,fx,fy,mass,drag,dt):
    u=u+fx/mass*dt-u*drag*dt
    v=v+fy/mass*dt-v*drag*dt
    return(u,v)

# motion: position part
def motion_physicsposition(x,y,u,v,dt):
    x=x+dt*u
    y=y+dt*v
    return(x,y)

# motion: compute speed un expected at next timestep from motion_physics
def motion_nextself(u,v,fx,fy,mass,drag,dt):
    un=u*dt-u*drag*dt+fx/mass*dt
    vn=v*dt-v*drag*dt+fy/mass*dt
    xn=x+un*dt
    yn=y+vn*dt
    return(xn,yn,un,vn)

# motion: compute position xn expected at next timestep from motion_physics
def motion_futurepos(x,y,u,v,fx,fy,mass,drag,dt):
    [un,vn]=motion_futurespeed(u,v,fx,fy,mass,drag,dt)
    xn=x+un*dt
    yn=y+vn*dt
    return(xn,yn)

# compute motion: position in nt timesteps (e.g. for ploting an arc)
# fx0,fy0 are initial forces while fx,fy are applied at all following timesteps
def motion_futureself(x,y,u,v,fx0,fy0,fx,fy,mass,drag,dt,nt):
    xr=[]# result
    yr=[]
    ur=[]
    vr=[]
    xr.append(x)
    yr.append(y)
    ur.append(u)
    vr.append(v)
    [x,y,u,v]=motion_physics(x,y,u,v,fx0,fy0,mass,drag,dt)
    xr.append(x)
    yr.append(y)
    ur.append(u)
    vr.append(v)
    if nt>1:
        for i in range(nt-1):
            [x,y,u,v]=motion_physics(x,y,u,v,fx,fy,mass,drag,dt)
            xr.append(x)
            yr.append(y)
            ur.append(u)
            vr.append(v)
        return(xr,yr,ur,vr)

# motion: restrict to one of 4 directions (the one with max speed)
def motion_to4dir(u,v):
    if u**2>=v**2:
        [u,v]=[u,0]
    else:
        [u,v]=[0,v]
    return(u,v)

# motion: restrict to left right only
def motion_to2dirx(u,v):
    return(u,0)

# motion: restrict to up down only
def motion_to2diry(u,v):
    return(0,v)

# collision moving circle with boundaries
# *BOUNDARIES
def mcirclefbdry_hit(x,y,u,v,fx,fy,radius,xh,yh,bxmin,bxmax,bymin,bymax,closedx,closedy,cor,cort):
    # record collision (for sound effects)
    hit=False# record if collision happends or not
    hitec=0# record  change in Ec=0.5*(u**2+v**2) from collision (e.g. hitec=u**2 for change u to -u)
    #
    if x<bxmin+radius:# left
        if closedx:# closed boundary
            x=bxmin+radius
            if u<=0:
                hit=True
                hitec=u**2
                u=-u*cor# loss from coefficient of restitution
                v= v*cort
        else:# periodic boundary
            x += (bxmax-bxmin)
            xh += (bxmax-bxmin)
    elif x>bxmax-radius: #right
        if closedx:
            x=bxmax-radius
            if u>=0:
                hit=True
                hitec=u**2
                u=-u*cor
                v= v*cort
        else:
            x -= (bxmax-bxmin)
            xh -= (bxmax-bxmin)
    if y<bymin+radius: # bottom
        if closedy:
            y=bymin+radius
            if v<=0:
                hit=True
                hitec=v**2
                u= u*cort
                v=-v*cor
        else:
            y += (bymax-bymin)
            yh += (bymax-bymin)
    elif y>bymax-radius: # top
        if closedy:
            y=bymax-radius
            if v>=0:
                hit=True
                hitec=v**2
                u= u*cort
                v=-v*cor
        else:
            y -= (bymax-bymin)
            yh -= (bymax-bymin)
    return(x,y,u,v,fx,fy,xh,yh,hit,hitec)

# determine if two boolean circles are colliding (no physics involved)
def bcirclebcircle_hit(x1,y1,radius1,x2,y2,radius2):
    if (x1-x2)**2 + (y1-y2)**2<(radius1+radius2)**2:
        return(True)
    else:
        return(False)


# Collision between moving circles 1 and 2 (non-elastic choc)
#*CIRCLE
def mcirclemcircle_hit(x1,y1,u1,v1,fx1,fy1,m1,radius1,x2,y2,u2,v2,fx2,fy2,m2,radius2,cor,cort,dt):
    # record collision (for sound effects)
    hit=False# record if collision happends or not
    hitec=0# record  change in Ec=0.5*(u**2+v**2) from collision (e.g. hitec=u**2 for change u to -u)
    if (x1-x2)**2 + (y1-y2)**2<=(radius1+radius2)**2:# overlapping circles
        theta=atan2(y2-y1,x2-x1)
        c0=cos(theta)
        s0=sin(theta)
        sm=m1+m2
        dm=m1-m2
        if (x1-x2)*(u1-u2)+(y1-y2)*(v1-v2)<=0:# getting closer
            w1=u1*c0+v1*s0
            z1=-u1*s0+v1*c0
            w2=u2*c0+v2*s0
            z2=-u2*s0+v2*c0
            w1m =  dm/sm*w1 + 2*m2/sm*w2
            w2m = -dm/sm*w2 + 2*m1/sm*w1
            u1=w1m*c0*cor - z1*s0*cort
            v1=w1m*s0*cor + z1*c0*cort
            u2=w2m*c0*cor - z2*s0*cort
            v2=w2m*s0*cor + z2*c0*cort
            hit=True
            hitec=(w1-w2)**2
        dd=(radius1+radius2)-sqrt( (x1-x2)**2 + (y1-y2)**2 )
        x1=x1-dd*m2/sm*c0#correct position (weight with masses)
        y1=y1-dd*m2/sm*s0
        x2=x2+dd*m1/sm*c0#correct position (weight with masses)
        y2=y2+dd*m1/sm*s0
    return(x1,y1,u1,v1,fx1,fy1,x2,y2,u2,v2,fx2,fy2,hit,hitec)

# Collision moving circle 1 and fixed circle 2
#Note: circle2 could move non-dynamically, in which case it is treated as m2>>m1
def mcirclefcircle_hit(x1,y1,u1,v1,fx1,fy1,m1,radius1,x2,y2,u2,v2,radius2,cor,cort,dt):
    hit=False# record if collision happends or not
    hitec=0# record  change in Ec=0.5*(u**2+v**2) from collision (e.g. hitec=u**2 for change u to -u)
    if (x1-x2)**2+(y1-y2)**2<=(radius1+radius2)**2:#overlapping circles
        theta=atan2(y2-y1,x2-x1)
        c0=cos(theta)
        s0=sin(theta)
        if (x1-x2)*u1+(y1-y2)*v1<0:# getting closer
            w1= u1*c0+v1*s0
            z1=-u1*s0+v1*c0
            w1m=-w1
            u1= w1m*c0*cor - z1*s0*cort# correct speed (w1 becomes -w1 and apply cor,cort)
            v1= w1m*s0*cor + z1*c0*cort
            hit=True
            hitec=w1**2
        x1=x2-(radius1+radius2)*c0 + u2*dt#correct position+apply movement of 2
        y1=y2-(radius1+radius2)*s0 + v2*dt
    return(x1,y1,u1,v1,fx1,fy1,hit,hitec)


# Collision moving circle 1 with fixed rectangle 2
def mcirclefrect_hit(x1,y1,u1,v1,fx1,fy1,m1,radius1,x2,y2,u2,v2,radiusx2,radiusy2,cor,cort,dt):
    hit=False# record if collision happends or not
    hitec=0# record  change in Ec=0.5*(u**2+v**2) from collision (e.g. hitec=u**2 for change u to -u)
    if x1<x2-radiusx2-radius1 or x1>x2+radiusx2+radius1 or y1<y2-radiusy2-radius1 or y1>y2+radiusy2+radius1:
        pass# nothing happens if outside of extended area
    else:
    # Only one condition applies depending on circle center position in extended rectangle area:
        if x1<=x2-radiusx2:
            if y1>=y2+radiusy2:
                if u1>0 and v1<0:
                    [hit,hitec]=[True,u1**2]
                    [u1,v1]=[ -u1*cor ,  -v1*cor ]# top left corner
                [x1,y1]=[ x2-radiusx2-radius1 , y2+radiusy2+radius1 ]
            elif y1<=y2-radiusy2:
                if u1>0 and v1>0:
                    [hit,hitec]=[True,(u1**2+v1**2)/2]
                    [u1,v1]=[ -u1*cor ,  -v1*cor ] # bottom left corner
                [x1,y1]=[ x2-radiusx2-radius1 , y2-radiusy2-radius1 ]
            else:
                if u1>0:
                    [hit,hitec]=[True,u1**2]
                    [u1,v1]=[ -u1*cor ,  v1*cort ]# left side middle
                [x1,y1]=[ x2-radiusx2-radius1, y1 ]
        elif x1>x2+radiusx2:
            if y1>=y2+radiusy2:
                if u1<0 and v1<0:
                    [hit,hitec]=[True,(u1**2+v1**2)/2]
                    [u1,v1]=[ -u1*cor ,  -v1*cor ]# top right corner
                [x1,y1]=[ x2+radiusx2+radius1, y2+radiusy2+radius1 ]
            elif y1<=y2-radiusy2:
                if u1<0 and v1>0:
                    [hit,hitec]=[True,(u1**2+v1**2)/2]
                    [u1,v1]=[ -u1*cor ,  -v1*cor ]# bottom right corner
                [x1,y1]=[ x2+radiusx2+radius1, y2-radiusy2-radius1 ]
            else:
                if u1<0:
                    [hit,hitec]=[True,u1**2]
                    [u1,v1]=[ -u1*cor ,  v1*cort ]# right side middle
                [x1,y1]=[ x2+radiusx2+radius1, y1 ]
        elif y1>=y2+radiusy2:
            if v1<0:
                [hit,hitec]=[True,v1**2]
                [u1,v1]=[  u1*cort, -v1*cor ]# top side middle
            [x1,y1]=[ x1, y2+radiusy2+radius1 ]
        elif y1<=y2-radiusy2:
            if v1>0:
                [hit,hitec]=[True,v1**2]
                [u1,v1]=[  u1*cort, -v1*cor ]# bottom side middle
            [x1,y1]=[ x1, y2-radiusy2-radius1 ]
        else:# is within center area. move to closest edge
            ds2=[ (x1-x2+radiusx2)**2+(y1-y2)**2, (x1-x2-radiusx2)**2+(y1-y2)**2, (x1-x2)**2+(y1-y2+radiusy2)**2, (x1-x2)**2+(y1-y2-radiusy2)**2 ]
            ce=ds2.index(min(ds2))# index for min distance to W,E,S,N middle points of edges
            if ce==0:# left edge
                if u1>0:
                    [hit,hitec]=[True,u1**2]
                    [u1,v1]=[ -u1*cor ,  v1*cort ]
                [x1,y1]=[ x2-radiusx2-radius1, y1 ]
            elif ce==1:#right edge
                if u1<0:
                    [hit,hitec]=[True,u1**2]
                    [u1,v1]=[ -u1*cor ,  v1*cort ]
                [x1,y1]=[ x2+radiusx2+radius1, y1 ]
            elif ce==2:# bottom edge
                if v1>0:
                    [hit,hitec]=[True,v1**2]
                    [u1,v1]=[  u1*cort, -v1*cor ]
                [x1,y1]=[ x1, y2-radiusy2-radius1 ]
            elif ce==3:#top edge
                if v1<0:
                    [hit,hitec]=[True,v1**2]
                    [u1,v1]=[  u1*cort, -v1*cor ]
                [x1,y1]=[ x1, y2+radiusy2+radius1 ]
        #
        x1=x1+u2*dt# in all these cases collision happens, so apply velocity of 2 to 1 (2 is non dynamical but can be moving)
        y1=y1+v2*dt
    return(x1,y1,u1,v1,fx1,fy1,hit,hitec)


# Collision Moving Circle 1 with Fixed Right Triangle 2
# x2,y2 is the middle middle of triangle largest edge, radiusx2, radiusy2 the length of other edges
def mcircleftrian_hit(x1,y1,u1,v1,fx1,fy1,m1,radius1,x2,y2,u2,v2,radiusx2,radiusy2,side2,cor,cort,dt):
    hit=False# record if collision happends or not
    hitec=0# record  change in Ec=0.5*(u**2+v**2) from collision (e.g. hitec=u**2 for change u to -u)
    if x1<x2-radiusx2-radius1 or x1>x2+radiusx2+radius1 or y1<y2-radiusy2-radius1 or y1>y2+radiusy2+radius1:
        pass# nothing happens if outside of rectangle area
    else:
        if side2==1:# right triangle facing NE
            if x1<=x2-radiusx2:# left side
                if y1>=y2+radiusy2:
                    if u1>0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                elif y1<=y2-radiusy2:
                    if u1>0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ] # bottom left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if u1>0:
                        [hit,hitec]=[True,u1**2]
                        [u1,v1]=[ -u1*cor ,  v1*cort ]# left side middle
                    [x1,y1]=[ x2-radiusx2-radius1, y1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            elif y1<=y2-radiusy2:# bottom side
                if x1>=x2+radiusx2:
                    if u1<0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# bottom right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if v1>0:
                        [hit,hitec]=[True,v1**2]
                        [u1,v1]=[  u1*cort, -v1*cor ]# bottom side middle
                    [x1,y1]=[ x1, y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            else: # NE side or inside
                theta=atan2(radiusx2,radiusy2)
                c0=cos(theta)
                s0=sin(theta)
                if y1 <= -radiusy2/radiusx2*(x1- x2-radius1*c0 ) + y2+radius1*s0 : # edge formula at +radius
                    xw1=(x1-x2-radius1*c0)*c0+(y1-y2-radius1*s0)*s0# correct position
                    x1=x1-xw1*c0
                    y1=y1-xw1*s0
                    w1=u1*c0+v1*s0 # correct speed
                    if w1<0:
                        [hit,hitec]=[True,w1**2]
                        z1=-u1*s0+v1*c0
                        w1=-w1*cor
                        z1= z1*cort
                        u1=w1*c0 - z1*s0
                        v1=w1*s0 + z1*c0
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
        #
        elif side2==2:# right triangle facing NW
            if x1>=x2+radiusx2:# right side
                if y1>y2+radiusy2:
                    if u1<0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                elif y1<=y2-radiusy2:
                    if u1<0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# bottom right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if u1<0:
                        [hit,hitec]=[True,u1**2]
                        [u1,v1]=[ -u1*cor ,  v1*cort ]# right side middle
                    [x1,y1]=[ x2+radiusx2+radius1, y1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            elif y1<=y2-radiusy2:# bottom side
                if x1<x2-radiusx2:
                    if u1>0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ] # bottom left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if v1>0:
                        [hit,hitec]=[True,v1**2]
                        [u1,v1]=[  u1*cort, -v1*cor ]# bottom side middle
                    [x1,y1]=[ x1, y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            else: # NW side or inside
                theta=pi-atan2(radiusx2,radiusy2)
                c0=cos(theta)
                s0=sin(theta)
                if y1 <= radiusy2/radiusx2*(x1- x2-radius1*c0 ) + y2+radius1*s0 : # edge formula at+radius
                    xw1=(x1-x2-radius1*c0)*c0+(y1-y2-radius1*s0)*s0# correct position
                    x1=x1-xw1*c0
                    y1=y1-xw1*s0
                    w1=u1*c0+v1*s0 # correct speed
                    if w1<0:
                        [hit,hitec]=[True,w1**2]
                        z1=-u1*s0+v1*c0
                        w1=-w1*cor
                        z1= z1*cort
                        u1=w1*c0 - z1*s0
                        v1=w1*s0 + z1*c0
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
        #
        elif side2==3:# right triangle facing SW
            if x1>=x2+radiusx2:# right side
                if y1<=y2-radiusy2:
                    if u1<0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# bottom right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                elif y1>=y2+radiusy2:
                    if u1<0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if u1<0:
                        [hit,hitec]=[True,u1**2]
                        [u1,v1]=[ -u1*cor ,  v1*cort ]# right side middle
                    [x1,y1]=[ x2+radiusx2+radius1, y1 ]
            elif y1>=y2+ radiusy2:# top side
                if x1<=x2-radiusx2:
                    if u1>0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if v1<0:
                        [hit,hitec]=[True,v1**2]
                        [u1,v1]=[  u1*cort, -v1*cor ]# top side middle
                    [x1,y1]=[ x1, y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            else: # SW side or inside
                theta=atan2(radiusx2,radiusy2)+pi
                c0=cos(theta)
                s0=sin(theta)
                if y1 >= -radiusy2/radiusx2*(x1- x2-radius1*c0 ) + y2+radius1*s0 : # edge formula at+radius
                    xw1=(x1-x2-radius1*c0)*c0+(y1-y2-radius1*s0)*s0# correct position
                    x1=x1-xw1*c0
                    y1=y1-xw1*s0
                    w1=u1*c0+v1*s0 # correct speed
                    if w1<0:
                        [hit,hitec]=[True,w1**2]
                        z1=-u1*s0+v1*c0
                        w1=-w1*cor
                        z1= z1*cort
                        u1=w1*c0 - z1*s0
                        v1=w1*s0 + z1*c0
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
        #
        elif side2==4:# right triangle facing SE
            if x1<=x2-radiusx2:# left side
                if y1<=y2-radiusy2:
                    if u1>0 and v1>0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ] # bottom left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2-radiusy2-radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                elif y1>=y2+radiusy2:
                    if u1>0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top left corner
                    [x1,y1]=[ x2-radiusx2-radius1 , y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if u1>0:
                        [hit,hitec]=[True,u1**2]
                        [u1,v1]=[ -u1*cor ,  v1*cort ]# left side middle
                    [x1,y1]=[ x2-radiusx2-radius1, y1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            elif y1>=y2+ radiusy2:# top side
                if x1>=x2+radiusx2:
                    if u1<0 and v1<0:
                        [hit,hitec]=[True,(u1**2+v1**2)/2]
                        [u1,v1]=[ -u1*cor ,  -v1*cor ]# top right corner
                    [x1,y1]=[ x2+radiusx2+radius1, y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
                else:
                    if v1<0:
                        [hit,hitec]=[True,v1**2]
                        [u1,v1]=[  u1*cort, -v1*cor ]# top side middle
                    [x1,y1]=[ x1, y2+radiusy2+radius1 ]
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
            else: # SE side or inside
                theta=-atan2(radiusx2,radiusy2)
                c0=cos(theta)
                s0=sin(theta)
                if y1 >= radiusy2/radiusx2*(x1- x2-radius1*c0 ) + y2+radius1*s0 : # edge formula at+radius
                    xw1=(x1-x2-radius1*c0)*c0+(y1-y2-radius1*s0)*s0# correct position
                    x1=x1-xw1*c0
                    y1=y1-xw1*s0
                    w1=u1*c0+v1*s0 # correct speed
                    if w1<0:
                        [hit,hitec]=[True,w1**2]
                        z1=-u1*s0+v1*c0
                        w1=-w1*cor
                        z1= z1*cort
                        u1=w1*c0 - z1*s0
                        v1=w1*s0 + z1*c0
                    [x1,y1]=[x1+u2*dt,y1+u2*dt]
    return(x1,y1,u1,v1,fx1,fy1,hit,hitec)



##########################################################
# Functions specific to game
# *FUNCTIONS

# change screenw, screenh globally
def changescreenw(screenwin):
    global screenw
    screenw=screenwin
    return True
def changescreenh(screenhin):
    global screenh
    screenh=screenhin
    return True
# Change xcam, ycam globally
def changexcam(xcamin):
    global xcam
    xcam=xcamin
    return True
def changeycam(ycamin):
    global ycam
    ycam=ycamin
    return True
#
# Change music and sound (use a function because are global variables)
def changedomusic(musicon):
    global domusic
    domusic=musicon
    return domusic
def changedosound(soundon):
    global dosound
    dosound=soundon
    return dosound

# function: aiming slows down time (separate because global changes)
# rate can be True (sets intensity at 0.1), False, or a float for intensity
def func_slowtime(rate):
    global dt
    global dtp
    if rate:
        if isinstance(rate,bool):
            dt=0.1*dt0
            dtp=0.1*dtp0
        else:
            dt=rate*dt0
            dtp=rate*dtp0
    else:
        dt=dt0
        dtp=dtp0
    return True

# function: determine if line is on screen and should be drawn or not
# Difficult for lines completely outside of screen or crossing it (e.g. bdries)
# A=(xa,ya), B=(xb,yb)
def func_drawline(color,A,B,width):
    # if not max(A[0],B[0])<0 and not min(A[0],B[0])>screenw:
    #     if not max(A[1],B[1])<0 and not min(A[1],B[1]>screenh):
    #         pygame.draw.line(screen,color,A,B,width)
    pygame.draw.line(screen,color,A,B,width)
    return True

# function: determine if rectangle is on screen and should be drawn or not
# Difficult for rects completely outside of screen or crossing it (e.g. bdries)
# rect=(x0,y0,w,h)
def func_drawrect(color,rect,width):
    pygame.draw.rect(screen,color,rect,width)
    return True

# func_drawimage(self.imglocation,(i1.x-5-xcam,screenh-i1.y-5-ycam),5,5)
# function: determine if image is on screen and should be drawn or not
# needs additional info than blit (radx,rady=half width and half heigth)
# DO NOT USE FOR TEXT (although uses same pygame function blit)
# A=(x0,y0)
def func_drawimage(image,A,radx,rady):
    xmin=A[0]
    xmax=A[0]+2*radx
    ymin=A[1]
    ymax=A[1]+2*rady
    if xmin>screenw or xmax<0 or ymin>screenh or ymax<0:# completely outside
        pass
    else:
        screen.blit(image,A)# partially inside (draw entirely)
        # Note: we could make special conditions for images partially on screen, but it isnt worth the effort
    return True

# draw text in a given rectangle (xmin, ymin,xmax,ymax)
def func_drawtextinrect(text,font,color,rect):
    text=font.render(text,True,color)
    text_rect = text.get_rect(center=(rect[0]+(rect[1]-rect[0])/2, rect[2]+(rect[3]-rect[2])/2))
    screen.blit(text, text_rect)
    return True

# draw text centered on a given point
def func_drawtextatpoint(text,font,color,point):
    text=font.render(text,True,color)
    text_rect = text.get_rect(center=point)
    screen.blit(text, text_rect)
    return True

# Change a pygame image to a single color (but preserving transparency)
def pygame_changesurfacecolor(surface, color):
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))



##########################################################

# Controls Class
# *CONTROLS
class obj_controls:
    def __init__(self):
        # special
        self.events=pygame.event.get()
        self.quit=False
        # mouse
        self.mousescaling=(1,1)#(= (1,1) unless screen is scaled)
        self.mousex=0
        self.mousey=0
        self.mouse1=False# pressed or not
        self.mouse2=False
        self.mouse3=False
        self.mouse4=False
        self.mouse5=False
        # keys
        self.doazerty=False# switch some keys to azerty mode (doesnt affect text mode)
        self.esc=False
        self.enter=False
        self.backspace=False
        self.tab=False
        self.space=False
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        self.a=False
        self.d=False
        self.w=False
        self.s=False
        self.q=False
        self.e=False
        self.r=False
        self.f=False
        self.g=False
        self.h=False
        self.x=False
        self.m=False
        self.n=False
        self.p=False
        self.c=False
        self.z=False
        # booleans to detect if change on frame
        self.mouse1c=False# changed or not
        self.mouse2c=False
        self.mouse3c=False
        self.mouse4c=False
        self.mouse5c=False
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.leftc=False
        self.rightc=False
        self.upc=False
        self.downc=False
        self.ac=False
        self.dc=False
        self.wc=False
        self.sc=False
        self.qc=False
        self.ec=False
        self.rc=False
        self.fc=False
        self.gc=False
        self.hc=False
        self.xc=False
        self.mc=False
        self.nc=False
        self.pc=False
        self.cc=False
        self.zc=False
        # Text: switch to input text (omit regular getkeys except Enter)
        self.textmode=False
        self.textmode_return=False
        self.textmode_fasterase=False
        self.text=''
    def getevents(self):
        self.events=pygame.event.get()
    def starttextmode(self,starttext):
        self.textmode=True
        self.textmode_return=False
        self.text=starttext# start editing from input text
    def gettext(self):
        for event in self.events:
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.textmode=False# EXIT TEXTMODE
                    self.textmode_return=False
                    self.textmode_fasterase=False
                    timer.reset('controls_textmode_erase')
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.textmode_return=True
                else:
                    self.text += event.unicode
            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    self.textmode_return=False
                    self.textmode_fasterase=False
                    timer.reset('controls_textmode_erase')
        if self.textmode_return and timer('controls_textmode_erase',True,30):
            self.textmode_fasterase=True
        if self.textmode_fasterase and timer('controls_textmode_starterase',True,1):
            timer.reset('controls_textmode_starterase')
            self.text=self.text[:-1]
    def getmouse(self):
        self.mouse1c=False# left click
        self.mouse2c=False# right click
        self.mouse3c=False# middle click
        self.mouse4c=False#middle up
        self.mouse5c=False# middle down
        (self.mousex,self.mousey)=pygame.mouse.get_pos()
        self.mousex=int(self.mousex)# very important if screen is stretched
        self.mousey=int(self.mousey)
        for event in self.events:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.mouse1, self.mouse1c = True, True
                elif event.button==3:
                    self.mouse2, self.mouse2c = True, True
                elif event.button==2:
                    self.mouse3, self.mouse3c = True, True
                elif event.button==4:
                    self.mouse4, self.mouse4c = True, True
                elif event.button==5:
                    self.mouse5, self.mouse5c = True, True
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    self.mouse1, self.mouse1c = False, True
                elif event.button==3:
                    self.mouse2, self.mouse2c = False, True
                elif event.button==2:
                    self.mouse3, self.mouse3c = False, True
                elif event.button==4:
                    self.mouse4, self.mouse4c = False, True
                elif event.button==5:
                    self.mouse5, self.mouse5c = False, True
    def getkeys(self):
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.leftc=False
        self.rightc=False
        self.upc=False
        self.downc=False
        self.dc=False
        self.sc=False
        self.ec=False
        self.rc=False
        self.fc=False
        self.gc=False
        self.hc=False
        self.xc=False
        self.mc=False
        self.nc=False
        self.pc=False
        self.cc=False
        # qwerty/azerty keys
        self.qc=False
        self.ac=False
        self.wc=False
        self.zc=False
        for event in self.events:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.esc, self.escc = True, True
                elif event.key==pygame.K_RETURN:
                    self.enter, self.enterc = True, True
                elif event.key==pygame.K_BACKSPACE:
                    self.backspace, self.backspacec = True, True
                elif event.key==pygame.K_TAB:
                    self.tab, self.tabc = True, True
                elif event.key==pygame.K_SPACE:
                    self.space, self.spacec = True, True
                elif event.key==pygame.K_LEFT:
                    self.left, self.leftc = True, True
                elif event.key==pygame.K_RIGHT:
                    self.right, self.rightc = True, True
                elif event.key==pygame.K_UP:
                    self.up, self.upc = True, True
                elif event.key==pygame.K_DOWN:
                    self.down, self.downc = True, True
                elif event.key==pygame.K_d:
                    self.d, self.dc = True, True
                elif event.key==pygame.K_s:
                    self.s, self.sc = True, True
                elif event.key==pygame.K_e:
                    self.e, self.ec = True, True
                elif event.key==pygame.K_r:
                    self.r, self.rc = True, True
                elif event.key==pygame.K_f:
                    self.f, self.fc = True, True
                elif event.key==pygame.K_g:
                    self.g, self.gc = True, True
                elif event.key==pygame.K_h:
                    self.h, self.hc = True, True
                elif event.key==pygame.K_x:
                    self.x, self.xc = True, True
                elif event.key==pygame.K_m:
                    self.m, self.mc = True, True
                elif event.key==pygame.K_n:
                    self.n, self.nc = True, True
                elif event.key==pygame.K_p:
                    self.p, self.pc = True, True
                elif event.key==pygame.K_c:
                    self.c, self.cc = True, True
                else:
                    if not self.doazerty:
                        if event.key==pygame.K_a:
                            self.a, self.ac = True, True
                        elif event.key==pygame.K_w:
                            self.w, self.wc = True, True
                        elif event.key==pygame.K_q:
                            self.q, self.qc = True, True
                        elif event.key==pygame.K_z:
                            self.z,self.zc = True, True
                    # else:
                    #     if event.key==pygame.K_a:
                    #         self.q, self.qc = True, True
                    #     elif event.key==pygame.K_w:
                    #         self.z, self.zc = True, True
                    #     elif event.key==pygame.K_q:
                    #         self.a, self.ac = True, True
                    #     elif event.key==pygame.K_z:
                    #         self.w,self.wc = True, True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    self.esc, self.escc = False, True
                elif event.key==pygame.K_RETURN:
                    self.enter, self.enterc = False, True
                elif event.key==pygame.K_BACKSPACE:
                    self.backspace, self.backspacec = False, True
                elif event.key==pygame.K_TAB:
                    self.tab, self.tabc = False, True
                elif event.key==pygame.K_SPACE:
                    self.space, self.spacec = False, True
                elif event.key==pygame.K_LEFT:
                    self.left, self.leftc = False, True
                elif event.key==pygame.K_RIGHT:
                    self.right, self.rightc = False, True
                elif event.key==pygame.K_UP:
                    self.up, self.upc = False, True
                elif event.key==pygame.K_DOWN:
                    self.down, self.downc = False, True
                elif event.key==pygame.K_d:
                    self.d, self.dc = False, True
                elif event.key==pygame.K_s:
                    self.s, self.sc = False, True
                elif event.key==pygame.K_e:
                    self.e, self.ec = False, True
                elif event.key==pygame.K_r:
                    self.r, self.rc = False, True
                elif event.key==pygame.K_f:
                    self.f, self.fc = False, True
                elif event.key==pygame.K_g:
                    self.g, self.gc = False, True
                elif event.key==pygame.K_h:
                    self.h, self.hc = False, True
                elif event.key==pygame.K_x:
                    self.x, self.xc = False, True
                elif event.key==pygame.K_m:
                    self.m, self.mc = False, True
                elif event.key==pygame.K_n:
                    self.n, self.nc = False, True
                elif event.key==pygame.K_p:
                    self.p, self.pc = False, True
                elif event.key==pygame.K_c:
                    self.c, self.cc = False, True
                else:
                    if not self.doazerty:
                        if event.key==pygame.K_a:
                            self.a, self.ac = False, True
                        elif event.key==pygame.K_w:
                            self.w, self.wc = False, True
                        elif event.key==pygame.K_q:
                            self.q, self.qc = False, True
                        elif event.key==pygame.K_z:
                            self.z,self.zc = False, True

    def getquit(self):
        for event in self.events:
            if event.type==pygame.QUIT:
                self.quit=True
    def set_mousescaling(self,mousescaling):# changes default mousescale
        self.mousescaling=mousescaling
    def mousescale(self):
        self.mousex=int(self.mousex*self.mousescaling[0])# must remain an integer!!)
        self.mousey=int(self.mousey*self.mousescaling[1])
    def update(self):
        self.getevents()# Important: only get events once per frame!
        self.getmouse()
        self.mousescale()
        if self.textmode:
            self.gettext()
        else:
            self.getkeys()# regular keys not affected by azerty/qwerty
        self.getquit()

####################################################################################################################
####################################################################################################################
####################################################################################################################

# Other functions and useful objects
# *FUNCTIONS

# Convert a rectangle=(xmin,xmax,ymin,ymax) to a pygame rectangle=(xmin,ymin,width,height)
def rect_to_pygame_rect(rect):
    (xmin,xmax,ymin,ymax)=rect# not a pygame rectangle
    return (xmin,ymin,xmax-xmin,ymax-ymin)

# Returns coordinates of a point in a rectangle
# the xoffset and yoffset are 0< <1 and place point in rectangle from upper left edge
def point_in_rect(rect,xoffset,yoffset):
    (xmin,xmax,ymin,ymax)=rect# not a pygame rectangle
    xpoint=xmin+xoffset*(xmax-xmin)
    ypoint=ymin+yoffset*(ymax-ymin)
    return (int(xpoint),int(ypoint))

# check if is in rectangle (not a pygame rectangle definition)
def isinrect(x,y,rect):
    (xmin,xmax,ymin,ymax)=rect# not a pygame rectangle
    if x>xmin and x<xmax and y>ymin and y<ymax:
        return True
    else:
        return False
# sign function
def sign(x):
    if x==0:
        return(0)
    elif x>0:
        return(1)
    elif x<0:
        return(-1)

# swap two elements i1,i2 in list x
def swap2inlist(x,i1,i2):
    x[i1],x[i2]=x[i2],x[i1]
    return(x)

# find closest value in list
def findclosestvalue(value,liste):
    return liste[min(range(len(liste)), key = lambda i: abs(liste[i]-value))]

# check if something (e.g. string...) can be converted to integer
def thiscanbeanint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# check if something (e.g. string...) can be converted to integer
def thiscanbeafloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# remove capital letters from a string
def remove_caps(s):
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        if not ch.isupper(): result.append(ch)
        i += 1
    return ''.join(result)

# return clean version of a string: no caps, and remove reserved characters: " ' #
def cleanstring(s):
    result=s
    result=result.replace("'", "")
    result=result.replace('"','')
    result=result.replace('#','')
    result=remove_caps(result)
    return result

# check if something exists or not (to check deletion)
def wasthisdeleted(s):
        try:
            s
        except NameError:
            print('was deleted - doesnt exists')
        else:
            print('wasnt deleted - exists')

# Toggle a boolean
def toggle(s):
    if s:
        return False
    else:
        return True

# shit all list elements to the right
def shiftlist_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst

def shiftlist_left(lst):
    try:
        return  lst[1:] + [lst[0]]
    except IndexError:
        return lst

# Object Once:
# test=once(caller,comparator):
# first call: return True (record caller and comparator)
# next calls same comparator:  return False
# next call new comparator: return True, update comparator
#
# caller can be anything, but best to use a unique string for caller (e.g. 'frompartofcodel123')
# comparator can be anything (including object, e.g. current level etc)
#

class obj_once:
    def __init__(self):
        self.callers=[]
    def __call__(self,caller,comparator):
        answer=True# assume first call
        if self.callers:
            for i in self.callers:
                if i.caller==caller:
                    if i.comparator==comparator:# next call same comparator
                        answer=False
                    else:
                        i.comparator=comparator# next call new comparator
                    break
        if answer: self.callers.append(obj_oncecaller(caller,comparator))# record if first call
        return answer
# A caller for the object once (will be recorded)
class obj_oncecaller:
    def __init__(self,caller,comparator):
        self.caller=caller
        self.comparator=comparator


# class obj_onceor


# Object Timer:
# test=timer(caller,comparator,amount)
# first call: return False (record caller,comparator and start timer)
# new calls timer not done, same comparator: return False
# new calls timer done, same comparator: return True
# new calls different comparator: counts as a new first call, resets timer, return False
# caller: use a unique caller name (e.g. 'frompartofcodel123')
# amount: an integer (decrease by 1 each loop)
#
# IMPORTANT: timer.reset(caller) removes caller so new call can be made afterwards!
# The timer object must be updated in loop using timer.update()
#
# Note: comparator should be removed as it is more important to use timer.reset(caller)
class obj_timer:
    def __init__(self):
        self.callers=[]
    def __call__(self,caller,comparator,amount):
        firstcall=True# assume first call
        done=False# assume timer not done
        if self.callers:
            for i in self.callers:
                if i.caller==caller:# new call
                    firstcall=False
                    if i.comparator==comparator:# new call same comparator
                        if i.timer <= 0:
                            done=True# next call timer finished
                            break
                    else:# next call different comparator: reset timer
                        i.comparator=comparator
                        i.timer=amount
                        break
        if firstcall:
            self.callers.append(obj_timercaller(caller,comparator,amount))# record if first call
        return done
    def update(self):
        if self.callers:
            for i in self.callers:
                if i.timer>0:  i.timer -= 1
    def reset(self,caller):
        if self.callers:
            for i in self.callers:
                if i.caller==caller:# matching call
                    self.callers.remove(i)
# A caller for the object timer (will be recorded)
class obj_timercaller:
    def __init__(self,caller,comparator,amount):
        self.caller=caller
        self.comparator=comparator
        self.timer=amount


####################################################################################################################
# Initialize Game
# *GAME *INITIALIZATION
# (define all functions and objects before this)

# Global variables
#
# Physics Reference values (applies unless overwritten locally)
fps= 60  # game frames per second
dt0=1# game timestep (reference value)
mts0=10# how many updates by physical engine for one game update (reference value)
dtp0=dt0/mts0# Physical Engine timestep (reference value)
[dt,mts,dtp]=[dt0,mts0,dtp0]# assign to values used in game (that can be modified)
#
# Native Screen Size (should always be 800x600 for game)
# screenw, screenh = 800, 600# the game was originally writen at that resolution
screenw, screenh = 1280, 720# 720p common for PC
# screenw, screenh = 1920, 1080# 1080p common (but too demanding ?)
scsx, scsy =screenw/800, screenh/600# scalers for some text/images written in original resolution

# python run bk_globalvars

# Camera
xcam=0# offset for camera
ycam=0

# Playing area
dplay=100

dopause= False # game is paused or not
dosound= False # do sounds
domusic= False # do music
dodebug= False # allow dev controls (toggle with Tab)

##########################################################

# Misc
once=obj_once()# Create the object once for calls
timer=obj_timer()# Create the object timer for calls
##########################################################
# Initialize game

# Initialize music/sound mixer (recommended before game)
# pygame.mixer.pre_init(50000, -16, 2, 2048) # best one?
# pygame.mixer.pre_init(44100, -16, 1, 2048) #
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.init()

# Initialize pygame
pygame.init()# Intialize the pygame
clock = pygame.time.Clock()# start clock (to control framerate)
#
#
print('starting')
# Game Variables
display=obj_display()# display screen (create first)
controls=obj_controls()# mouse/keyboard controls (create second)
# controls.set_mousescaling(display.mousescaling)# unecessary if settings resets display/controls
settings=obj_settings()# settings manager (create third: changes display, display changes controls)
sound=obj_sound()# sound module (load after settings)
music=obj_music()# music module (load after settings)
scenemanager=obj_scenemanager()# game scene manager (level,pause,quit...)



##########################################################
while True:

    # Updates
    clock.tick(fps)# delay loop for game to update at 60 fps
    timer.update()# update all timers
    display.update()
    controls.update()
    scenemanager.update(controls)# everything happens here!
    #
    # Debug Mode (for dev only)
    if controls.tab and controls.tabc: dodebug=toggle(dodebug)
   #
    # print('### new frame ###')
    # print((controls.mousex,controls.mousey))
    # if dodebug and controls.m: func_slowtime(True)
    # if not controls.m and controls.mc: func_slowtime(False)
    # print(controls.doazerty)




##########################################################
# Quit game when break out of loop
