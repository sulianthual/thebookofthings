#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# core.py: game core (most essential elements)
#
# Any direct call to the pygame module (currently version 1.9.4) must be here.
#
# Why?
# - We can improve the game engine more easily (e.g. switch to dirty sprites)
# - If we wanted to change the game engine from pygame we could do it more easily here.
#
##########################################################
##########################################################

import pygame
# print(pygame.__file__)# file location
#
import share
import tool

####################################################################################################################
# Game Core

# initialize game engine
def initialize():
    #
    # New: audio
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.init()
    #
    #
    pygame.init()# init all modules (we could select them if they are not all used)
    # pygame.time.wait(200)# wait 200 ms (to let some modules like pygame.font initialize entirely)



# Quit Game Procedure
class obj_quit:
     def __init__(self):
         pass
     def __call__(self):
        pygame.display.quit()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        tool.sysexit()


# Game Clock (delays game update to given fps)
class obj_clock:
    def __init__(self):
        self.clock=pygame.time.Clock()
        self.targetfps=share.fps
    def getfps(self):
        return self.clock.get_fps()
    def update(self):
        share.dt=self.clock.tick(self.targetfps)


# Scene Manager: update current scene and switches between scenes
class obj_scenemanager:
    def __init__(self):
        self.scene=None# a scene object (called page in the book of things)
    def switchscene(self,newscene,initstart=False):
        self.scene=newscene
        if initstart:# reload page content
            self.scene.initstart()
    def update(self,controls):
        self.scene.update(controls)# Update current scene
        if controls.quit: share.quitgame()
        # devtools:
        if share.devaccess:
            if controls.gdev and controls.gdevc: share.devmode = not share.devmode# toggle dev mode
            if share.devmode and controls.gm2 and controls.gm2c:# print coordinates
                print( '('+str(controls.gmx)+','+str(controls.gmy)+')')
            if controls.gq and controls.gqc:
                # share.quitgame()# quit directly
                share.scenemanager.switchscene(share.titlescreen)# go back to menu

####################################################################################################################
####################################################################################################################
# Audio players

# Music Player
# Musics are not unique to pages, they are managed globally
class obj_musicplayer:
    def __init__(self):
        self.setup()
    def setup(self):
        self.name=None# current music being played (None=silence)
        #
        if share.datamanager.domusic:# launch options
            self.mastervolume=share.datamanager.musicvol*0.2# master volume for music (changed in settings, 0-1)
        else:
            self.mastervolume=0
        self.musicfilevolume=1# volume specific to current music file being played
    def change(self,name):# change music (new music=change, None=silence, same as before=continue)
        if name is None:
            self.name=None
            self.stop()
        else:
            if name != self.name:
                self.load(name)
                self.play()
    def load(self,name):
        self.name=name
        path='data/musics/'+share.musics.getmusicfilename(name)
        if not tool.ospathexists(path):
            self.name='error'
            path='data/musics/'+share.musics.getmusicfilename(self.name)
        pygame.mixer.music.load(path)
        self.musicfilevolume=share.musics.getmusicvolume(self.name)
        self.resetvolume()
        # self.set_volume(self.mastervolume*self.musicfilevolume)
    def play(self):
        pygame.mixer.music.play(-1)# loop
    def pause(self):
        pygame.mixer.music.pause()
    def fadeout(self,amount=1000):
        pygame.mixer.music.fadeout(amount)#
    def rewind(self):
        pygame.mixer.music.rewind()
    def stop(self):
        pygame.mixer.music.stop()
    def set_volume(self,volume):
        pygame.mixer.music.set_volume(volume)
    def setmastervolume(self,volume):
        self.mastervolume=volume
        self.resetvolume()
        # self.set_volume(self.volumerefmult*self.mastervolume*self.musicfilevolume)
    def resetvolume(self):# reset volume to expected level
        volumerefmult= 2 # IMPORTANT: arbitrary grand volume multiplicator (for all musics)
        self.set_volume(volumerefmult*self.mastervolume*self.musicfilevolume)




# Sound Player
# sounds are unique to pages, they are managed locally (like image sprites)
class obj_soundplayer:
    def __init__(self):
        self.setup()
    def setup(self):
        if share.datamanager.dosound:# launch options
            self.mastervolume=share.datamanager.soundvol*0.2# master volume for sounds (changed in settings, ref=1)
        else:
            self.mastervolume=0
        # self.nchannels=16# max number of channels allowed
        # pygame.mixer.set_num_channels(self.nchannels)# set number of channels
    def getmastervolume(self):# return mastervolume
        return self.mastervolume
    def setmastervolume(self,volume):
        self.mastervolume=volume
    def stop(self):# stop all sounds
        pygame.mixer.stop()


# pygame sound sprite
# acts much like an image sprite:
# - is (loaded/forgotten by pages)
# - created/called by a draw.obj_sound
class obj_soundsprite:
    def __init__(self,name,mastervolume):
        self.name=name
        self.mastervolume=mastervolume# mastervolume from soundplayer
        self.setup()
    def setup(self):
        path='data/sounds/'+share.sounds.getsoundfilename(self.name)
        if not tool.ospathexists(path):
            self.name='error'
            path='data/sounds/'+share.sounds.getsoundfilename(self.name)
        self.sound=pygame.mixer.Sound(path)# pygame sound (loaded to a channel)
        self.soundfilevolume=share.sounds.getsoundvolume(self.name)
        self.reset_volume()
    def play(self,loop=False):
        if loop:
            self.sound.play(-1)
        else:
            self.sound.play()
    def stop(self):
        self.sound.stop()
    def set_volume(self,volume):# set sound volume in sprite
        self.sound.set_volume(volume)
    def reset_volume(self):# reset volume to expected level
        volumerefmult= 2 # IMPORTANT: arbitrary grand volume multiplicator (for all sounds)
        self.set_volume(volumerefmult*self.mastervolume*self.soundfilevolume)



####################################################################################################################
####################################################################################################################


# Display Manager
class obj_display:
    def __init__(self):
        self.infos=pygame.display.Info()# get computer display info (only at init)
        # initial setup (can be repeated on settings changes)
        if share.datamanager.donative:# launch in windowed
            self.setup()
        else:
            self.setup(native=False)# launch in fullscreen
    def setup(self,native=True):
        self.native=native# native (windowed in 1280,720) or fullscreen (adapted resolution)
        # initialize display and buffer screen
        if self.native:
            # native (windowed 1280x720)
            self.displayresolution=(1280,720)
            share.screen.screen=pygame.display.set_mode(self.displayresolution)
            share.screen.set_alpha(None) # Remove alpha=transparency (for increased performances)
        else:
            # fullscreen (image goes screen->displayscreen)
            self.displayresolution=(self.infos.current_w, self.infos.current_h)
            share.screen.screen=pygame.Surface((1280,720))
            share.screen.set_alpha(None)
            self.displayscreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)# fullscreen
            # self.displayscreen = pygame.display.set_mode((0,0), pygame.NOFRAME)# borderless
            # self.displayscreen = pygame.display.set_mode((0,0))# windowed
            self.displayscreen.set_alpha(None)
        # Mouse
        self.mousescaling=(1280/self.displayresolution[0],720/ self.displayresolution[1])# scaling
        share.controls.mousescaling=self.mousescaling# tell controls about new mouse scaling
        pygame.mouse.set_visible(False)# show mouse
        # Other
        pygame.display.set_caption("The Book of Things")# window banner
        self.reseticon()# window icon
    def reset(self,native=True):# reset display with new values
        pygame.display.quit()
        self.setup(native)
    #
    def reseticon(self):
        self.makeicon()
        self.seticon()
    def makeicon(self):# make window icon from a player drawing
        if tool.ospathexists('book/book.png'):
            img=pygame.image.load('book/book.png').convert()
            img=pygame.transform.scale(img,(42,36))
            pygame.image.save(img,'book/bookicon.png')
    def seticon(self):
        if tool.ospathexists('book/bookicon.png'):
            img=pygame.image.load('book/bookicon.png').convert()
        else:
            img=pygame.image.load('data/booknoicon.png').convert()
        img.set_colorkey(share.colorkey)
        pygame.display.set_icon(img)
    #
    def update(self):
        if self.native:# display is directly the screen
            pygame.display.update()# always refresh entire display
            # pygame.display.update(share.screen.areas)# only refresh parts of the display
        else:# adapted, intermediary screen
            pygame.transform.scale(share.screen.screen,self.displayresolution,self.displayscreen)# scaling
            # pygame.transform.smoothscale(share.screen.screen,self.displayresolution,self.displayscreen)# smoothscale (too slow)
            pygame.display.update()# refresh entire display
            # pygame.display.update(share.screen.areas)# only refresh parts of the display





####################################################################################################################
####################################################################################################################
####################################################################################################################


# Game buffer screen (sprites draw on it)
# draws sprites and determines which display areas (rects) are updated (WIP)
class obj_screen:
    def __init__(self):
        self.screen=None
        self.areas=[]# list of areas for display refresh (rectangles (x,y,width,heigth))
    def set_alpha(self,value):
        self.screen.set_alpha(value)
    ### draw calls
    def fillsurf(self,value):
        self.screen.fill(value)
    def drawsurf(self,surface,xy):#xy=top left
        self.screen.blit(surface, (int(xy[0]),int(xy[1])) )
    def drawline(self,color,xy1,xy2,thickness=3):
        pygame.draw.line(self.screen,color,xy1,xy2,thickness)
    def drawcircle(self,color,xy,radius,thickness=3,fill=False):
        if fill:
            pygame.draw.circle(self.screen, color, xy, int(radius), 0)
        else:
            pygame.draw.circle(self.screen, color, xy, int(radius), thickness)
    def drawrect(self,color,rect,thickness=3,fill=False):
        x,y,width,height=rect
        if fill:
            pygame.draw.rect(self.screen, color, (int(x-width/2), int(y-height/2), int(width), int(height)), 0)
        else:
            pygame.draw.rect(self.screen, color, (int(x-width/2), int(y-height/2), int(width), int(height)), thickness)
    def drawcross(self,color,xy,radius,thickness=3,diagonal=False):
        if not diagonal:
            pygame.draw.line(self.screen,color,(xy[0]-radius,xy[1]),(xy[0]+radius,xy[1]),thickness)
            pygame.draw.line(self.screen,color,(xy[0],xy[1]-radius),(xy[0],xy[1]+radius),thickness)
        else:
            pygame.draw.line(self.screen,color,(xy[0]-radius,xy[1]-radius),(xy[0]+radius,xy[1]+radius),thickness)
            pygame.draw.line(self.screen,color,(xy[0]+radius,xy[1]-radius),(xy[0]-radius,xy[1]+radius),thickness)


####################################################################################################################
# Sprites

# Sprite Template:
# sprites are the basis for any on-screen display
# sprites dont have an on-screen position xy (position is determined elsewhere)
# sprites are NOT pygame sprites (although they may contain a pygame.surface)
class obj_sprite:
    def __init__(self):
        self.type='sprite'
        self.spritetype=None#image,text,etc...

# background (entire screen)
class obj_sprite_background(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='background'
        self.surf=None
    def make(self,color):
        self.color=color
        self.surf=pygame.Surface(share.screen.screen.get_size())
        self.surf.fill(self.color)
    def display(self):
        share.screen.fillsurf(self.color)

# image sprite
class obj_sprite_image(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='image'
        self.surf=None# associated pygame surface
        self.rx=None# half-width
        self.ry=None# half-heigth
        self.colorkey=share.colorkey# transparent color
        self.rxref=None# reference half-width (if scaling from reference)
        self.ryref=None# reference half-height
    def make(self):# create empty
        pass
    def makeempty(self,rx,ry):
        self.surf=pygame.Surface((2*rx,2*ry))
        self.addtransparency()
        self.fill(self.colorkey)
        self.recordscale()# record reference scale
    def load(self,path,convert=True,failsafe=True,replacewhite=True):
        if tool.ospathexists(path):
            if convert:
                self.surf=pygame.image.load(path).convert()
            else:
                self.surf=pygame.image.load(path)
            self.addtransparency()
            if replacewhite:
                self.replacewhite()# white to gray
            self.recordscale()# record reference scale
            return True# load succeeded
        elif failsafe:
            self.surf=pygame.image.load('data/error.png').convert()
            self.addtransparency()
            self.recordscale()# record reference scale
            return True
        else:
            return False# load failed
    def replacewhite(self):# replace white in images with background game color (gray)
        self.replacecolor((245,245,245),share.datamanager.getbackcolor())
    def replacecolor(self,color,newcolor,treshold=(10,10,10)):
        pygame.transform.threshold(self.surf,self.surf,color,treshold,newcolor,inverse_set=True)
    def save(self,name):
        pygame.image.save(self.surf,name)
    def addtransparency(self):
        self.surf.set_colorkey(self.colorkey)
    def getrx(self):
        return self.surf.get_rect().size[0]/2
    def getry(self):
        return self.surf.get_rect().size[1]/2
    def getrxry(self):
        term=self.surf.get_rect().size
        return (term[0]/2,term[1]/2)
    def clear(self):
        self.surf.fill(self.colorkey)
    def blitfrom(self,sprite_source,xoffset,yoffset):
        self.surf.blit(sprite_source.surf,( int(xoffset),int(yoffset)) )
    def fill(self,color):
        self.surf.fill(color)
    def fliph(self):
        self.surf=pygame.transform.flip(self.surf,True,False)
    def flipv(self):
        self.surf=pygame.transform.flip(self.surf,False,True)
    def flip(self,fliph,flipv):
        if fliph or flipv:
            self.surf=pygame.transform.flip(self.surf,fliph,flipv)
    def scale(self,scaling,target=False):# scaling factor or target size
        if not target:
            if scaling !=1:
                termx=self.getrx()*2*scaling
                termy=self.getry()*2*scaling
                self.surf=pygame.transform.scale(self.surf, (int(termx),int(termy)) )
        else:
                self.surf=pygame.transform.scale(self.surf, (int(scaling[0]),int(scaling[1])) )
    def recordscale(self):# record current scale (to scale with respect to it)
        self.rxref=self.getrx()
        self.ryref=self.getry()
    def scaleto(self,scaling):# scale with respect to reference scale
        termx=self.rxref*2*scaling
        termy=self.ryref*2*scaling
        self.surf=pygame.transform.scale(self.surf, (int(termx),int(termy)) )
    def rotate(self,angle):# returns position offset from rotation
        if angle !=0:
            xold,yold=self.surf.get_rect().center
            self.surf=pygame.transform.rotate(self.surf,int(angle))
            xnew,ynew=self.surf.get_rect().center
            return xold-xnew,yold-ynew
        else:
            return 0,0
    def rotate90(self,angle):#rotate by closest increment
        angle= int(round(angle%360/90,0)*90)# (in 0,90,180,270)
        if angle !=0:
            self.surf=pygame.transform.rotate(self.surf,int(angle))
    def display(self,x,y):# xy=(x,y) center of display
        xd,yd=x-self.getrx(),y-self.getry()# recompute
        share.screen.drawsurf(self.surf,(int(xd),int(yd)))# top left needed (CHANGE IT?)


# text=like an image but with prerender
class obj_sprite_text(obj_sprite_image):
    def __init__(self):
        super().__init__()
        self.spritetype='text'
    def make(self,text,font,color,bold=True,fillcolor=None):
        if fillcolor==None:# separate because leads to different qualities
            self.surf=font.render(text,bold,color)
        else:
            self.surf=font.render(text,bold,color,fillcolor=fillcolor)
        self.rx,self.ry=self.getrxry()


# line sprite
class obj_sprite_line(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='line'
    def make(self):
        pass
    def display(self,color,xy1,xy2):
        share.screen.drawline(color,xy1,xy2)


# line sequence sprite (from list of points)
class obj_sprite_linesequence(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='lineseq'
    def make(self):
        pass
    def display(self,color,xylist):#xylist=[xy1,xy2,...]
        if xylist and len(xylist)>1:
            for i,j in zip( range(0,len(xylist)-2) , range(1,len(xylist)-1) ):
                xy1,xy2=xylist[i],xylist[j]
                share.screen.drawline(color,xy1,xy2)


# cross sprite
class obj_sprite_cross(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='cross'
    def make(self):
        pass
    def display(self,color,xy,radius,thickness=3,diagonal=False):
        share.screen.drawcross(color,xy,radius,thickness=thickness,diagonal=diagonal)

# circle sprite
class obj_sprite_circle(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='circle'
    def make(self):
        pass
    def display(self,color,xy,radius):
        share.screen.drawcircle(color,xy,radius)

# rectangle sprite
class obj_sprite_rect(obj_sprite):
    def __init__(self):
        super().__init__()
        self.spritetype='rect'
    def make(self):
        pass
    def display(self,color,rect):
        share.screen.drawrect(color,rect)


# brush used for drawing (not rendered directly on screen)
class obj_sprite_brush(obj_sprite_image):
    def __init__(self):
        super().__init__()
        self.spritetype='brush'
    def makebrush(self,pen):
        self.load(pen[0])
        self.scale(pen[1],target=True)


# font sprite (not rendered directly on screen)
class obj_sprite_font:
    def __init__(self,name,size):
        self.font=pygame.font.Font(name,size)# pygame font
        # self.font.set_bold(True)# Test
        # self.font.set_italic(True)# Test
        # self.font.set_underline(True)# Test
    def render(self,text,bold,color,fillcolor=None):
        if fillcolor is not None:
            return self.font.render(text,bold,color,fillcolor)
        else:
            return self.font.render(text,bold,color)

    def size(self,text):
        return self.font.size(text)



####################################################################################################################

# Controls
# *CONTROLS
# Manages Input controls
class obj_controls:
    def __init__(self):
        self.azerty=share.datamanager.doazerty# azerty mode (modified by datb/datamanager)
        self.events=pygame.event.get()
        # pygame.event.set_grab(True)# grab the mouse (cannot escape window)
        self.setup_quit()
        self.setup_mouse()
        self.setup_keys()
        self.setup_gkeys()
    def getevents(self):
        self.events=pygame.event.get()
    def setup_quit(self):
        self.quit=False
    def getquit(self):
        for event in self.events:
            if event.type==pygame.QUIT:
                self.quit=True
    def setup_mouse(self):
        # mouse
        self.mousescaling=(1,1)#(= (1,1) unless screen is scaled)
        self.mousex=0
        self.mousey=0
        self.mouse1=False# pressed or not
        self.mouse2=False
        # self.mouse3=False
        # self.mouse4=False
        # self.mouse5=False
        # booleans to detect if change on frame
        self.mouse1c=False# changed or not
        self.mouse2c=False
        # self.mouse3c=False
        # self.mouse4c=False
        # self.mouse5c=False
        #
    def setmouse(self,x,y):
        pygame.mouse.set_pos([x,y])
    def getmouse(self):
        self.mouse1c=False# left click
        self.mouse2c=False# right click
        # self.mouse3c=False# middle click
        # self.mouse4c=False#middle up
        # self.mouse5c=False# middle down
        (self.mousex,self.mousey)=pygame.mouse.get_pos()
        self.mousex=int(self.mousex*self.mousescaling[0])# scale input if screen is stretched
        self.mousey=int(self.mousey*self.mousescaling[1])# must remain an integer!!)
        for event in self.events:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.mouse1, self.mouse1c = True, True
                elif event.button==3:
                    self.mouse2, self.mouse2c = True, True
                # elif event.button==2:
                #     self.mouse3, self.mouse3c = True, True
                # elif event.button==4:
                #     self.mouse4, self.mouse4c = True, True
                # elif event.button==5:
                #     self.mouse5, self.mouse5c = True, True
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    self.mouse1, self.mouse1c = False, True
                elif event.button==3:
                    self.mouse2, self.mouse2c = False, True
                # elif event.button==2:
                #     self.mouse3, self.mouse3c = False, True
                # elif event.button==4:
                #     self.mouse4, self.mouse4c = False, True
                # elif event.button==5:
                #     self.mouse5, self.mouse5c = False, True
    def setup_keys(self):
        # keys
        self.esc=False
        self.enter=False
        self.backspace=False
        self.tab=False
        self.space=False
        self.lctrl=False
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
        self.t=False
        self.f=False
        self.g=False
        self.z=False
        #
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.lctrlc=False
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
        self.tc=False
        self.fc=False
        self.gc=False
        self.zc=False
    def getkeys(self):
        self.escc=False
        self.enterc=False
        self.backspacec=False
        self.tabc=False
        self.spacec=False
        self.lctrlc=False
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
        self.tc=False
        self.fc=False
        self.gc=False
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
                elif event.key==pygame.K_LCTRL:
                    self.lctrl, self.lctrlc = True, True
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
                elif event.key==pygame.K_a:
                    self.a, self.ac = True, True
                elif event.key==pygame.K_w:
                    self.w, self.wc = True, True
                elif event.key==pygame.K_q:
                    self.q, self.qc = True, True
                elif event.key==pygame.K_e:
                    self.e, self.ec = True, True
                elif event.key==pygame.K_r:
                    self.r, self.rc = True, True
                elif event.key==pygame.K_t:
                    self.t, self.tc = True, True
                elif event.key==pygame.K_f:
                    self.f, self.fc = True, True
                elif event.key==pygame.K_g:
                    self.g, self.gc = True, True
                elif event.key==pygame.K_z:
                    self.z, self.zc = True, True
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
                elif event.key==pygame.K_LCTRL:
                    self.lctrl, self.lctrlc = False, True
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
                elif event.key==pygame.K_a:
                    self.a, self.ac = False, True
                elif event.key==pygame.K_w:
                    self.w, self.wc = False, True
                elif event.key==pygame.K_q:
                    self.q, self.qc = False, True
                elif event.key==pygame.K_e:
                    self.e, self.ec = False, True
                elif event.key==pygame.K_r:
                    self.r, self.rc = False, True
                elif event.key==pygame.K_t:
                    self.t, self.tc = False, True
                elif event.key==pygame.K_f:
                    self.f, self.fc = False, True
                elif event.key==pygame.K_g:
                    self.g, self.gc = False, True
                elif event.key==pygame.K_z:
                    self.z, self.zc = False, True
    def setup_gkeys(self):
        # generalized keys
        # (see corresponding names in datb.obj_datamanager)
        self.gu=False# up
        self.gd=False# down
        self.gl=False# left
        self.gr=False# right
        self.ga=False# action
        self.gb=False# back
        self.gq=False# quit
        self.gdev=False# dev key
        self.gm1=False# mouse 1
        self.gm2=False# mouse 2
        self.gmx=0# mouse x
        self.gmy=0# mouse y
        #
        self.guc=False
        self.gdc=False
        self.glc=False
        self.grc=False
        self.gac=False
        self.gbc=False
        self.gqc=False
        self.gdevc=False
        self.gm1c=False
        self.gm2c=False
    def getgkeys(self):
        # generalized keys
        if self.azerty:
            self.gu=self.z or self.up
            self.gd=self.s or self.down
            self.gl=self.q or self.left
            self.gr=self.d or self.right
            self.guc=self.zc or self.upc
            self.gdc=self.sc or self.downc
            self.glc=self.qc or self.leftc
            self.grc=self.dc or self.rightc
        else:
            self.gu=self.w or self.up
            self.gd=self.s or self.down
            self.gl=self.a or self.left
            self.gr=self.d or self.right
            self.guc=self.wc or self.upc
            self.gdc=self.sc or self.downc
            self.glc=self.ac or self.leftc
            self.grc=self.dc or self.rightc
        #
        self.ga=self.space# or self.enter
        self.gb=self.tab
        self.gq=self.esc
        self.gdev=self.lctrl
        self.gac=self.spacec# or self.enterc
        self.gbc=self.tabc
        self.gqc=self.escc
        self.gdevc=self.lctrlc
        #
        self.gm1=self.mouse1
        self.gm2=self.mouse2
        self.gmx=self.mousex
        self.gmy=self.mousey
        self.gm1c=self.mouse1c
        self.gm2c=self.mouse2c

    def nogkeys(self): # inhibit generalized inputs
        # (useful when editing text)
        self.gu=False
        self.gd=False
        self.gl=False
        self.gr=False
        self.ga=False
        self.gb=False
        # self.gq=False# dont inhibit
        # self.gdev=False# dont inhibit
        # self.gm1=False# dont inhibit
        # self.gm2=False# dont inhibit
        #
        self.guc=False
        self.gdc=False
        self.glc=False
        self.grc=False
        self.gac=False
        self.gbc=False
        # self.gqc=False
        # self.gdevc=False
        # self.gm1c=False# dont inhibit

        # self.gm2c=False# dont inhibit
    def edittext(self,text):# edit existing text with keyboard inputs
    # Beware of interaction with other inputs (e.g. space!)
        self.nogkeys()# inhibit generalized inputs
        for event in self.events:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:# Pressed once
                    # text = ''#remove all
                    text = text[:-1]# remove last character
                elif event.key == pygame.K_RETURN:# Enter (nothing happens)
                    pass
                elif event.key==pygame.K_ESCAPE:# Esc (nothing happens)
                    pass
                elif event.key==pygame.K_TAB:# Tab (nothing happens)
                    pass
                else:
                    text += event.unicode# record text
        return text
    def iskeydown(self):# tell if a key is being pressed (any key)
        istrue=False
        for event in self.events:
            if event.type==pygame.KEYDOWN:
                istrue=True
        return istrue

    def update(self):
        self.getevents()# Important: only get events once per frame!
        self.getmouse()
        self.getkeys()
        self.getgkeys()
        self.getquit()


####################################################################################################################
