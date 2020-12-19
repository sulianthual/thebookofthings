#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# drw.py: all tools for drawings, images, animations on screen
#
##########################################################
##########################################################

import os
import pygame
import share
import utils


####################################################################################################################
# Bank of parameters for drawing(colors, brushes etc)

# Colors (dictionary of RGB)
# *COLOR
class obj_colors:
    def __init__(self):
        self.black=(0,0,0)
        self.red=(220,0,0)# bit darker
        self.blue=(0,0,220)
        self.green=(0,220,0)
        self.gray=(150,150,150)
        self.brown=(165,42,42)
        #
        # Specific colors for devtools
        self.devactor=(0,0,220)# blue (hitbox)
        self.devtextbox=(225,225,25)# yellowish
        self.devimage=(250,150,0)# orange
        self.devanimation=(250,50,50)# red
        self.devdispgroup=(128,0,128)# purple
        
        # Specific colors for some game elements
        self.book=self.blue# anything book of thing
        self.input=self.red# input text color
        self.hero=self.red# hero text color
        self.weapon=self.brown# hero weapon text color
        self.itemloved=self.green
        self.itemhated=self.blue
        self.house=self.red# hero house
        
# Font
# *FONT
class obj_fonts:
     def __init__(self):
         self.font15=pygame.font.Font('data/AmaticSC-Bold.ttf', 15)# text font (for FPS) 
         self.font30=pygame.font.Font('data/AmaticSC-Bold.ttf', 30)# text font for indicators,textbox
         self.font60=pygame.font.Font('data/AmaticSC-Bold.ttf', 60)# text font for textbox
         self.font120=pygame.font.Font('data/AmaticSC-Bold.ttf', 120)# text font for textbox
         self.font50=pygame.font.Font('data/AmaticSC-Bold.ttf', 50)# text font for story text
         self.font100=pygame.font.Font('data/AmaticSC-Bold.ttf', 100)# text font for titlescreen 
         

# Brushes used for drawing
class obj_brushes:
    def __init__(self):
        self.pen=pygame.image.load('data/pen.png')
        self.pen=pygame.transform.scale(self.pen,(8,8))
        self.smallpen=pygame.image.load('data/pen.png')
        self.smallpen=pygame.transform.scale(self.smallpen,(4,4))
        self.tinypen=pygame.image.load('data/pen.png')
        self.tinypen=pygame.transform.scale(self.smallpen,(2,2))    
        
        
####################################################################################################################

# A drawing (image to edit interactively by the player)
# *DRAWING
class obj_drawing:
    def __init__(self,name,xy,base=None):# start new drawing (load or new)
        self.name=name# drawing name
        self.xy=xy# drawing position on screen (x,y), CENTER OF THE DRAWING
        self.base=base# drawing base (drawn over, part of final drawing), must be other drawing object (same dimensions)
        # Load brush
        self.brush=share.brushes.pen# currently used brush (can be changed externally)
        # Load drawing function with mouse
        self.mousedrawing=obj_mousedrawing()
        self.eraseonareahover=True# erase only if mouse hovers drawing area (useful if multiple drawings on screen)
        # Load shadow (must exist)
        self.imgbase=pygame.image.load('shadows/'+self.name+'.png')# drawing shadow image
        self.size=self.imgbase.get_rect().size
        self.xytl=(self.xy[0]-int(self.size[0]/2), self.xy[1]-int(self.size[1]/2))# position of top left corner
        self.rect=(self.xytl[0],self.xytl[0]+self.size[0],self.xytl[1],self.xytl[1]+self.size[1])# drawing rectangle area
        # Load drawing (or create empty one)
        if os.path.exists('drawings/'+self.name+'.png'):
            self.drawing=pygame.image.load('drawings/'+self.name+'.png')# load drawing image
        else:
            self.drawing=pygame.Surface(self.size)# make empty drawing image
            self.reset()
        self.drawing.set_colorkey((255,255,255))# set white as colorkey (that color will not be displayed) 
        # legend (displayed under drawing, optional)
        self.legend=[]
        self.legend_surface=[]
        self.legend_xtl=0
        self.legend_ytl=0
    def reset(self):
        self.drawing.fill((255,255,255))# erase drawing
        self.drawing.blit(self.imgbase,(0,0))# add shadow
    def display(self):
        pygame.draw.rect(share.screen, (255,255,255), (self.xytl[0], self.xytl[1], self.size[0],self.size[1]), 0)# white background
        if self.base:
            share.screen.blit(self.base.drawing,self.xytl)# display other drawing base at 
        # share.screen.blit(self.imgbase,self.xytl)# display shadow
        share.screen.blit(self.drawing,self.xytl)
        pygame.draw.rect(share.screen, (220,0,0), (self.xytl[0], self.xytl[1], self.size[0],self.size[1]), 3)# red borders (optional)
        self.displaylegend()
    def makelegend(self,legend):# make legend (and prerender)
        self.legend=legend
        self.legend_surface=share.fonts.font50.render(legend, True, (0, 0, 0))
        text_width, text_height=self.legend_surface.get_size()
        self.legend_xtl=int( self.xytl[0] + self.size[0]/2 - text_width/2 )
        self.legend_ytl=self.xytl[1]+self.size[1]
    def displaylegend(self):# display prerendered legend
        if self.legend:
            share.screen.blit(self.legend_surface, (self.legend_xtl,self.legend_ytl))
    def draw(self,controls):
        if controls.mouse1:# draw
            self.drawing=self.mousedrawing(controls,self.drawing,self.brush,self.xytl)# use drawing function                      
        if controls.mouse2:# erase
            if self.eraseonareahover:# erase only if mouse overs drawing rectangle area
                if utils.isinrect(controls.mousex,controls.mousey,self.rect): self.reset()
            else:# erase anyway
                self.reset()
    def update(self,controls):
        self.draw(controls)
        self.display()
    def finish(self):
        term=self.drawing.copy()# final
        term.fill((255,255,255))# erase drawing
        if self.base: term.blit(self.base.drawing,(0,0))# add base
        term.blit(self.drawing,(0,0))# add drawing
        pygame.image.save(term, 'drawings/'+self.name+'.png')# save drawing

# Function for drawing with mouse on a drawing (using Left Mouse)
# (Records Mouse Position to Draw Lines between Mouse Positions each frame)
class obj_mousedrawing:
    def __init__(self):
        self.mousexr=0# last recorded mouse position
        self.mouseyr=0
        self.surface=[]# surface copy for drawing
    def __call__(self,controls,surface,brush,xy):# call function (see example in object obj_drawing)
        # controls: user controls
        # surface: drawing to draw on
        # brush: brush to use
        # xy: position of drawing (TOP-LEFT CORNER)
        if controls.mouse1:
            brushdx=int(brush.get_rect().size[0]/2)# brush size
            brushdy=int(brush.get_rect().size[1]/2)
            if controls.mouse1c: # mouse just pressed
                surface.blit(brush,(controls.mousex-brushdx-xy[0],controls.mousey-brushdy-xy[1]))# draw on screen
                self.mousexr=controls.mousex# record mouse position
                self.mouseyr=controls.mousey
            else:# mouse held 
                surface.blit(brush,(controls.mousex-brushdx-xy[0],controls.mousey-brushdy-xy[1]))# draw on screen 
                # draw line between current and last mouse position
                dx=controls.mousex-self.mousexr
                dy=controls.mousey-self.mouseyr
                dist=max(abs(dx),abs(dy))
                for i in range(dist):
                    x = int( self.mousexr + float(i)/dist*dx)
                    y = int( self.mouseyr + float(i)/dist*dy)
                    surface.blit(brush,(x-brushdx-xy[0],y-brushdy-xy[1]))# draw on screen 
                # record mouse position
                self.mousexr=controls.mousex
                self.mouseyr=controls.mousey                    
        return(surface)


####################################################################################################################

# A text input area
# acts like a drawing (not moveable or scalable)
class obj_textinput:
    def __init__(self,key,nchar,xy,color=(0,0,0)):
        # key in dictionary of written words
        self.key=key
        self.textfromdict()# get text value from dictionary
        #
        self.xy=xy# center position
        self.nchar=nchar# max number of characters
        #
        self.font=share.fonts.font50# text font
        self.color=color# text color
        self.xmargin=20# margin left/right
        self.ymargin=10#margin top/bottom
        self.makeframe()# make frame for text
        #
        # legend (displayed under drawing, optional)
        self.legend=[]
        self.legend_surface=[]
        self.legend_xtl=0
        self.legend_ytl=0  
    def textfromdict(self):# 
        if self.key in share.words.dict:# key exists
            self.text=share.words.dict[self.key]
        else:# create key with empty text
            share.words.dict[self.key]=''
            self.text=''        
    def makeframe(self):# make frame for text
        # estimate max text size
        char_surface=self.font.render('W',True,self.color)# largest character
        self.size=char_surface.get_size()
        self.size= self.size[0]*self.nchar, self.size[1]# size of text (without margins)
        # top left corner
        self.xytl=self.xy[0]-int(self.size[0]/2)-self.xmargin, self.xy[1]-int(self.size[1]/2)-self.ymargin
        # rectangle
        self.rect=(self.xytl[0],self.xytl[0]+self.size[0]+2*self.xmargin,self.xytl[1],self.xytl[1]+self.size[1]+2*self.ymargin)# drawing rectangle area        
    def display(self):
         # text (centered inside frame)
        word_surface=self.font.render(self.text,True,self.color)
        text_width,text_height=word_surface.get_size()
        termx=self.xytl[0]+int(self.size[0]/2)+self.xmargin-int(text_width/2)
        termy=self.xytl[1]+self.ymargin
        share.screen.blit(word_surface,(termx,termy) )# display text
        # frame borders (red)
        pygame.draw.rect(share.screen, (220,0,0), \
                         (self.xytl[0], self.xytl[1], self.size[0]+self.xmargin*2,self.size[1]+self.ymargin*2), 3)     
        # frame legend
        self.displaylegend()

    def makelegend(self,legend):# make legend (and prerender)
        self.legend=legend
        self.legend_surface=share.fonts.font30.render(legend, True, (220, 0, 0))
        text_width, text_height=self.legend_surface.get_size()
        self.legend_xtl=int( self.xytl[0] + self.size[0]/2 +self.xmargin - text_width/2 )
        self.legend_ytl=int( self.xytl[1] + self.size[1] + text_height/2 )

    # def displaylegend(self):
    #     if self.legend:# could have a def makelegend, such that doesnt recompute/render every update
    #         # text_surface=share.fonts.font30.render(self.legend, True, (220, 0, 0))
    #         # text_width,text_height=text_surface.get_size()
    #         termx=self.xytl[0]+int(self.size[0]/2)+self.xmargin-int(text_width/2)
    #         termy=self.xytl[1]+self.size[1]+int(text_height/2)
    #         share.screen.blit(text_surface, (termx,termy))
            
    def displaylegend(self):# display prerendered legend
        if self.legend:
            share.screen.blit(self.legend_surface, (self.legend_xtl,self.legend_ytl))
    def changetext(self,controls):        
        if utils.isinrect(controls.mousex,controls.mousey,self.rect):# edit only if mouse in frame
            self.text=controls.edittext(self.text)# edit text
            if len(self.text)>self.nchar: self.text=self.text[:self.nchar-1]# control max size
            share.words.dict[self.key]=self.text# update text value in dictionary         
    def update(self,controls):
        self.display()
        self.changetext(controls)    
        
        
####################################################################################################################
#  
# A text box
# acts like an image (can be moved/scaled, part of a animgroup)
class obj_textbox:
    def __init__(self,text,xy,fontsize='medium',color=(0,0,0)):
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.text=text
        self.color=color# color of text (default=black)
        self.fontsize=fontsize# font size of text (default=medium)
        self.bold=True#bold or not
        self.flippedh=False# is image flipped horizontally (inverted) or not (original)
        self.flippedv=False# is image flipped vertically (inverted) or not (original)
        self.show=True# show the image or not (can be toggled on/off)
        self.setup()
    def setup(self):
        self.x=self.xini# center of textbox
        self.y=self.yini
        self.xc=0# position correction (from rotation)
        self.yc=0# 
        self.s= 1# scaling factor
        self.r= 0# rotation angle (degree)
        if self.fontsize=='tiny':
            self.img=share.fonts.font15.render(self.text, self.bold, self.color)
        elif self.fontsize=='small':
            self.img=share.fonts.font30.render(self.text, self.bold, self.color)
        elif self.fontsize=='large':
            self.img=share.fonts.font60.render(self.text, self.bold, self.color)
        elif self.fontsize=='huge':
            self.img=share.fonts.font120.render(self.text, self.bold, self.color)
        else:
            self.img=share.fonts.font50.render(self.text, self.bold, self.color)
        self.imgsize=self.img.get_size()
    def movetox(self,x): # move to x
        self.x=x
    def movetoy(self,y): # move to y
        self.y=y
    def movex(self,dx): # displace by dx
        self.x += dx
    def movey(self,dy): #displace by dy
        self.y += dy
    def fliph(self): # flip image horizontally
        self.flippedh= not self.flippedh
        self.img=pygame.transform.flip(self.img,True,False)
    def ifliph(self): # flip image horizontally to inverted
        if not self.flippedh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.flippedh=True
    def ofliph(self): # flip image horizontally to original
        if self.flippedh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.flippedh=False
    def flipv(self): # flip image vertically
        self.flippedv= not self.flippedv
        self.img=pygame.transform.flip(self.img,False,True)
    def iflipv(self): # flip image vertically to inverted
        if not self.flippedv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.flippedv=True
    def oflipv(self): # flip image vertically to original
        if self.flippedv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.flippedv=False
    def rotate(self,r): # rotate image by given angle r (and correct position)
        self.r += r
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]
    def scale(self,s): # scale image by given factor s (and correct position)
        self.s *= s
        self.img=pygame.transform.scale(self.img,(int(self.imgsize[0]*s),int(self.imgsize[1]*s)))
        self.imgsize=self.img.get_rect().size
    def display(self):
        if self.show:
            xtl=self.x-self.imgsize[0]/2 +self.xc# top left corner position
            ytl=self.y-self.imgsize[1]/2 +self.yc
            share.screen.blit(self.img,(int(xtl),int(ytl)))
    def devtools(self):
        share.crossdisplay((self.x,self.y),10,share.colors.devtextbox,3)
    def update(self,controls):
        self.play(self,controls)
    def play(self,controls):# same as display, but renamed for consitency with play() for animations, dispgroups
        self.display()
        if share.devmode: self.devtools()# dev tools
        
        
####################################################################################################################

# A simple image (from the drawings folder) to display at a given location
class obj_image:
    def __init__(self,name,xy):
        if os.path.exists('drawings/'+name+'.png'):
            self.img_ini=pygame.image.load('drawings/'+name+'.png')# load drawing image
        else:
            self.img_ini=pygame.image.load('data/error.png')# load error image
        self.xini=xy[0]# xy is the CENTER of the image on screen
        self.yini=xy[1]
        self.setup()
    def setup(self):#
        self.img=self.img_ini
        self.x=self.xini# image correction
        self.y=self.yini
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.xc=0# position correction (due to rotation)
        self.yc=0
        self.imgsize=self.img.get_rect().size
        self.img.set_colorkey((255,255,255))# set white as colorkey (that color will not be displayed)  
        self.flippedh=False# is image flipped horizontally (inverted) or not (original)
        self.flippedv=False# is image flipped vertically (inverted) or not (original)
        self.show=True# show the image or not (can be toggled on/off)
        # legend (displayed under, optional)
        self.legend=[]  
    def replaceimage(self,newimgname):# replace existing image with new one
        # Should have same dimensions as original (e.g. for correct rotations)
        # load
        if os.path.exists('drawings/'+newimgname+'.png'):
            img=pygame.image.load('drawings/'+newimgname+'.png')# load drawing image
        else:
            img=pygame.image.load('data/error.png')# load error image
        img.set_colorkey((255,255,255)) 
        # reapply reference transformations (fliph,flipv,scale, rotate...)
        if self.flippedh: img=pygame.transform.flip(img,True,False)
        if self.flippedv: img=pygame.transform.flip(img,False,True)
        if self.s != 1: 
            imgsize=img.get_rect().size
            img=pygame.transform.scale(img,(int(imgsize[0]*self.s),int(imgsize[1]*self.s)))
        if self.r != 0: img=pygame.transform.rotate(img,self.r)
        # assign
        self.img=img
    def movetox(self,x): # move to x
        self.x=x
    def movetoy(self,y): # move to y
        self.y=y
    def movex(self,dx): # displace by dx
        self.x += dx
    def movey(self,dy): #displace by dy
        self.y += dy
    def fliph(self): # flip image horizontally
        self.flippedh= not self.flippedh
        self.img=pygame.transform.flip(self.img,True,False)
    def ifliph(self): # flip image horizontally to inverted
        if not self.flippedh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.flippedh=True
    def ofliph(self): # flip image horizontally to original
        if self.flippedh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.flippedh=False
    def flipv(self): # flip image vertically
        self.flippedv= not self.flippedv
        self.img=pygame.transform.flip(self.img,False,True)
    def iflipv(self): # flip image vertically to inverted
        if not self.flippedv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.flippedv=True
    def oflipv(self): # flip image vertically to original
        if self.flippedv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.flippedv=False
    def scale(self,s): # scale image by given factor s (and correct position)
        self.s *= s
        self.img=pygame.transform.scale(self.img,(int(self.imgsize[0]*s),int(self.imgsize[1]*s)))
        self.imgsize=self.img.get_rect().size
    def rotate(self,r): # rotate image by given angle r (and correct position)
        self.r += r# Note: rotation increases image size, can be considerable if repeated often
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]
        # Note: Each rotate increases image size, eventually freezes memory. Do sparingly
    def display(self):
        if self.show:
            xtl=self.x-self.imgsize[0]/2 +self.xc
            ytl=self.y-self.imgsize[1]/2 +self.yc
            share.screen.blit(self.img,(int(xtl),int(ytl)))
            self.displaylegend()
    def displaylegend(self):
        if self.legend:
            text_surface=share.fonts.font50.render(self.legend, True, (0, 0, 0))
            text_width,text_height=text_surface.get_size()
            termx=self.x-int(text_width/2)
            termy=self.y+int(self.imgsize[1]/2)-int(text_height/2)
            share.screen.blit(text_surface, (termx,termy))            
    def devtools(self):
        share.crossdisplay((self.x,self.y),10,share.colors.devimage,3)
        # self.rx=self.imgsize[0]/2
        # self.ry=self.imgsize[0]/2
        # pygame.draw.rect(share.screen,share.colors.devimage, (self.x-self.rx, self.y-self.ry, 2*self.rx,2*self.ry), 3)            
    def update(self,controls):
        self.play(controls)
    def play(self,controls):# update,play,display kept for consistency and calls
        self.display()
        if share.devmode: self.devtools()


####################################################################################################################

# Animate an image on screen
# Consists of base image(s) (can be transformed permanently) + animation transformations(t) (applied each frame)
#* ANIMATION  
class obj_animation:      
    def __init__(self,name,imgname,xy):# start new animation (load or new)
        self.name=name# animation name
        self.imgname=imgname# reference image (more can be added)
        self.xini=xy[0]# reference position of animation ( (0,0)=default or center of screen)
        self.yini=xy[1]
        self.setup()
    def setup(self):
        # General Parameters
        self.x=self.xini# animation center (changed externally)
        self.y=self.yini# animation position (changed externally)
        self.xc=0# position correction (due to permanent rotation)
        self.yc=0# 
        self.flippedh=False# are the images flipped horizontally or not
        self.flippedv=False# are the images flipped horizontally or not
        self.r=0# current rotation angle of images
        self.s=1# current scaling factor of images (default =1)
        # Images Parameters
        if os.path.exists('drawings/'+self.imgname+'.png'):# load  image
            self.img_ini=pygame.image.load('drawings/'+self.imgname+'.png')
        else:
            self.img_ini=pygame.image.load('data/error.png')
        self.resetimages()# (re)initiate all images
        # Animation Sequence Parameters
        self.show=True# show the animation or not (can be toggled on/off)
        self.recording=False# Edit Mode On/Off (can be toggled)
        self.ntmax=False# max duration (number of frames) (ntmax=False means unlimited)
        self.tstart=0# start time offset when playing animation (0=default)
        self.aniname='animations/'+self.name+'.txt'# animation name
        self.resetanimation()# reset parameters to default values
        if os.path.exists(self.aniname): self.load()# load animation (if exists)
    ######
    # Part I: IMAGES
    def resetimages(self): # reset all image(s) (erase all permanent changes)
        self.img=self.img_ini
        self.img.set_colorkey((255,255,255))# set white to transparent
        self.imglist=[]# reset list of all available images
        self.imglist.append(self.img)
    def addimage(self,newimgname):# add an image to list of available ones for animation
        if os.path.exists('drawings/'+newimgname+'.png'):
            img=pygame.image.load('drawings/'+newimgname+'.png')# load drawing image
        else:
            img=pygame.image.load('data/error.png')# load error image
        img.set_colorkey((255,255,255))
        self.imglist.append(img)
    def replaceimage(self,newimgname,index):# replace existing image (at index=0,1...) with new one
        # Should have same dimensions as original (e.g. for correct rotations)
        if index >-1 and index<len(self.imglist):
            # load
            if os.path.exists('drawings/'+newimgname+'.png'):
                img=pygame.image.load('drawings/'+newimgname+'.png')# load drawing image
            else:
                img=pygame.image.load('data/error.png')# load error image
            img.set_colorkey((255,255,255)) 
            #
            # reapply reference transformations (fliph,flipv,scale, rotate...)
            if self.flippedh: img=pygame.transform.flip(img,True,False)
            if self.flippedv: img=pygame.transform.flip(img,False,True)
            if self.s != 1: 
                imgsize=img.get_rect().size
                img=pygame.transform.scale(img,(int(imgsize[0]*self.s),int(imgsize[1]*self.s)))
            if self.r != 0: img=pygame.transform.rotate(img,self.r)
            # assign
            self.imglist[index]=img
    ######
    # PART II: ANIMATION (transformations reapplied each frame to images)
    def resetanimation(self):# reset animation (=image transformations(t) )entirely
        # Animation transformations
        self.animation=[]# animation vector
        self.nt=False# animation length (False if none)
        self.anim_t=self.tstart# animation time increment        
        self.anim_x=0# x position anomalies around reference (integer) 
        self.anim_y=0# y position anomalies around reference (integer) 
        self.anim_fh=False# horizontal flip (boolean)
        self.anim_fv=False# vertical flip (boolean)
        self.anim_r=0# rotation angle (int, in degrees)
        self.anim_s=0# scaling factor (int): scaling = anim_bs**anim_s
        self.anim_bs=1.01# base for animation scaling
        self.anim_c=0# index of image used (0=default, >0=next images) 
    def firstframe(self):# reset animation to first frame
        self.anim_t=0
    def record(self,controls):# record animation with dev controls
        # Display Informations for Edit Mode
        share.screen.blit(share.fonts.font15.render('- EDIT MODE -', True, (255, 0, 0)), (1180,135)) 
        share.screen.blit(share.fonts.font15.render('Space: Toggle Mode', True, (255, 0, 0)), (1180,155)) 
        share.screen.blit(share.fonts.font15.render('Backspace: Reset', True, (255, 0, 0)), (1180,175))        
        share.screen.blit(share.fonts.font15.render('LMouse: Record', True, (255, 0, 0)), (1180,195)) 
        share.screen.blit(share.fonts.font15.render('a-d: rotate', True, (255, 0, 0)), (1180,215)) 
        share.screen.blit(share.fonts.font15.render('w-s: scale', True, (255, 0, 0)), (1180,235)) 
        share.screen.blit(share.fonts.font15.render('q-e: flip', True, (255, 0, 0)), (1180,255)) 
        share.screen.blit(share.fonts.font15.render('r: Save', True, (255, 0, 0)), (1180,275))
        share.screen.blit(share.fonts.font15.render('f: change image', True, (255, 0, 0)), (1180,295))
        # Position
        self.anim_x=controls.mousex-self.xini# anomalies around reference
        self.anim_y=controls.mousey-self.yini
        # Transformations
        if controls.q and controls.qc: self.anim_fh = not self.anim_fh# toggle horizontal flip
        if controls.e and controls.ec: self.anim_fv = not self.anim_fv# toggle vertical flip
        if controls.a: self.anim_r += 1
        if controls.d: self.anim_r -= 1
        if controls.w: self.anim_s += 1# (scaling is in anim_bs**anim_s)
        if controls.s: self.anim_s -= 1 
        if controls.f and controls.fc: self.anim_c += 1 # change image
        if self.anim_c > len(self.imglist)-1: self.anim_c =0# reset to first image
        # Record Frame  
        if controls.mouse1:
            if self.ntmax:# imposed max duration
                if len(self.animation)<self.ntmax:
                    self.animation.append([self.anim_t,self.anim_x,self.anim_y,self.anim_fh,self.anim_fv,self.anim_r,self.anim_s,self.anim_c])
                    self.anim_t += 1
            else:# no imposed max duration
                self.animation.append([self.anim_t,self.anim_x,self.anim_y,self.anim_fh,self.anim_fv,self.anim_r,self.anim_s,self.anim_c])
                self.anim_t += 1                
        if controls.backspace and controls.backspacec: self.resetanimation()# Reset animation        
        if controls.r and controls.rc: self.save()# Save to file
        # Display
        self.display()        
        # Show trajectories of image center for all frames (red)
        if self.animation and len(self.animation)>1: 
            for i in range(1,len(self.animation)): 
                term1=self.animation[i-1][1]+self.xini
                term2=self.animation[i-1][2]+self.yini
                term3=self.animation[i][1]+self.xini
                term4=self.animation[i][2]+self.yini
                pygame.draw.line(share.screen,(255,0,0),(term1,term2),(term3,term4),3)
        # Show reference animation position with cross (xini, yini)
        share.crossdisplay((self.xini,self.yini),10,(0,0,255),3)        
    def save(self):# save animation to file      
        f1=open(self.aniname, 'w+')
        f1.write('t,x,y,fh,fv,r,s,frame:'+'\n')# first line
        for i in range(0,len(self.animation)):
            line=str(self.animation[i][0])# anim_t
            line +=','+str(self.animation[i][1])# anim_x 
            line +=','+str(self.animation[i][2])# anim_y
            if self.animation[i][3]: # anim_fh (boolean to 0-1)
                line +=','+'1'
            else:
                line +=','+'0'
            if self.animation[i][4]: # anim_fv (boolean to 0-1)
                line +=','+'1'
            else:
                line +=','+'0' 
            line +=','+str(self.animation[i][5])# anim_r
            line +=','+str(self.animation[i][6])# anim_s
            line +=','+str(self.animation[i][7])# anim_c
            line +='\n'
            f1.write(line)
        f1.close()
    def load(self):# load animation from file
        self.animation=[]
        f1=open(self.aniname,'r+')
        line=f1.readline()# first line (skip)
        while line:
            line=f1.readline()
            if line:
                line = line.rstrip("\n")# remove trailing \n
                line=line.split(",")# split with delimiter ' '
                vect=[]
                vect.append(int(line[0]))# anim_t
                vect.append(int(line[1]))# anim_x
                vect.append(int(line[2]))# anim_y
                if int(line[3]) == 1:# anim_fh 
                    vect.append(True)
                else:
                    vect.append(False)
                if int(line[4]) == 1:# anim_fv 
                    vect.append(True)
                else:
                    vect.append(False)
                vect.append(int(line[5]))# anim_r
                vect.append(float(line[6]))# anim_s
                vect.append(int(line[7]))# anim_c 
                self.animation.append(vect)
        f1.close()   
        if self.animation:# compute animation length
            self.nt=len(self.animation)
        else:
            self.nt=False
    ### PART III: Global transformations
    # These transformations are permanent (unlike anim_x,r,s reapplied each frame)
    def movetox(self,x): # move to x
        self.x=x
    def movetoy(self,y): # move to y
        self.y=y
    def movex(self,x): # displace all images by dx (permanent)
        self.x += x
    def movey(self,y): #displace all images by dy (permanent)
        self.y += y  
    def fliph(self):# flip all animation images horizontally
        self.flippedh= not self.flippedh
        for i,value in enumerate(self.imglist):
            self.imglist[i]=pygame.transform.flip(value,True,False)        
    def flipv(self):# flip all animation images vertically
        self.flippedv= not self.flippedv
        for i,value in enumerate(self.imglist):
            self.imglist[i]=pygame.transform.flip(value,False,True)           
    def ifliph(self): # flip all animation images  horizontally (if not already flipped)
        if not self.flippedh:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,True,False)
            self.flippedh=True
    def ofliph(self): # unflip all animation images horizontally (if already flipped)
        if self.flippedh:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,True,False)
            self.flippedh=False    
    def iflipv(self): # flip all animation images  vertically (if not already flipped)
        if not self.flippedv:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,False,True)
            self.flippedv=True
    def oflipv(self): # unflip all animation images vertically (if already flipped)
        if self.flippedv:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,False,True)
            self.flippedv=False 
    def scale(self,s): # scale by factor s (and correct position)(also scales anim_x*self.s)
        self.s *= s
        for i,value in enumerate(self.imglist):
            imgsize=value.get_rect().size
            self.imglist[i]=pygame.transform.scale(value,(int(imgsize[0]*s),int(imgsize[1]*s)))
    def rotate(self,r): # rotate by given angle r (and correct position)
        self.r += r
        center1=self.imglist[0].get_rect().center
        for i,value in enumerate(self.imglist):            
            self.imglist[i]=pygame.transform.rotate(value,r)
        center2= self.imglist[0].get_rect().center 
        self.xc +=center1[0]-center2[0]# correction computed from first image
        self.yc +=center1[1]-center2[1]# (correction wrong if other images have different sizes)
        # Note: Each rotate increases image size, eventually freezes memory. Do sparingly
    ######
    # Part VI: General
    def playanim(self):# play animation (loop)
        self.anim_t +=1
        if self.anim_t > len(self.animation)-1: self.anim_t=0
        if self.animation:# read animation state at time
            term,self.anim_x,self.anim_y,self.anim_fh,self.anim_fv,\
                self.anim_r,self.anim_s,self.anim_c=self.animation[self.anim_t]
            self.display()
    def display(self):# display one animation frame (either when playing or recording)
        if self.show:
            self.imgt=self.imglist[self.anim_c]# base image
            self.imgsize=self.imgt.get_rect().size
            # Apply Transformations (reapplied each frame to base image)
            if self.anim_fh: self.imgt=pygame.transform.flip(self.imgt,True,False)
            if self.anim_fv: self.imgt=pygame.transform.flip(self.imgt,False,True)
            if self.anim_s != 0: # (scale before rotation)
                termscaling=self.anim_bs**self.anim_s
                self.imgt=pygame.transform.scale(self.imgt,(int(self.imgsize[0]*termscaling),int(self.imgsize[1]*termscaling)))
            else:
                termscaling=1
            if self.anim_r != 0: 
                term1=self.imgt.get_rect().center
                self.imgt=pygame.transform.rotate(self.imgt,self.anim_r)
                term2= self.imgt.get_rect().center 
                self.anim_r_dc=(term1[0]-term2[0],term1[1]-term2[1])# correction of position due to rotation
            else:
                self.anim_r_dc=(0,0)
            # position= x(move from external) +x_anim(animation) + corrections (scaling, rotations...)
            term1=self.x + self.anim_x*self.s -self.imgsize[0]/2*termscaling-self.anim_r_dc[0] +self.xc
            term2=self.y + self.anim_y*self.s -self.imgsize[1]/2*termscaling-self.anim_r_dc[1] +self.yc
            # Display
            share.screen.blit(self.imgt,(int(term1),int(term2)))
    def devtools(self):
        share.crossdisplay((self.x,self.y),10,share.colors.devanimation,3)
    def update(self,controls):# useful only for recording mode
        if share.devmode and controls.space and controls.spacec: self.recording= not self.recording     
        if self.recording: 
            self.record(controls)
        else:
            self.play(controls)
    def play(self,controls):# useful in game
        self.playanim()
        if share.devmode: self.devtools()
            

####################################################################################################################

# Group of Display Elements (Animations, Images or textboxes)
# Can apply transformations (move,flip,scale,rotate) while conserving properties (distance between elements)
# Every Element must have the followed fonctionalities (called/modified by the dispgroup):
#  self.xini, self.yini: reference position (used to compute conserved distances)
#  self.x, self.y: position
#  self.play(): display function
#  self.fliph(): flip image function (also must have ofliph, ifliph, same for flipv)
#  self.scale(): scale 
#  self.rotate(): rotate
class obj_dispgroup:
    def __init__(self,xy):
        self.xini=xy[0]# position center of group
        self.yini=xy[1]
        self.reset()
    def reset(self): # reset all (and erase lists)
        self.dict={}# dictionary of elements
        self.dictx={}# relative positions of elements (relative to self.x when element is added)
        self.dicty={}
        self.x=self.xini# x position of group (useful to track overall position, starts a xini, yini)
        self.y=self.yini
        self.flippedh=False# are the images flipped horizontally (inverted) or not (original)
        self.flippedv=False# are the images flipped vertically (inverted) or not (original)
        self.s=1# group scale
        self.r=0# group rotation
    def addpart(self,name,element):# add element to dispgroup (element=textbox,image or animation)
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )# record relative difference
    def removepart(self,name):# remove element
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
    def movetox(self,x):# 
        self.x=x
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movetoy(self,y):# 
        self.y=y
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def movex(self,dx): # move all elements by dx
        self.x += dx
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,dy): # move all elements by dy
        self.y += dy
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def symh(self,name): # shift element horizontally (relative to dispgroup)
        self.dictx[name] *= -1
        self.dict[name].movetox(self.x + self.dictx[name])
    def symv(self,name): # shift element vertically (relative to dispgroup)
        self.dicty[name] *= -1
        self.dict[name].movetoy(self.y + self.dicty[name])
    def fliph(self): # flip group horizontally
        self.flippedh=not self.flippedh
        for i in self.dict.keys(): 
            self.dict[i].fliph()
            self.symh(i)  
    def ifliph(self):# flip group horizontally to inverted orientation
        if not self.flippedh:
            self.flippedh=True
            for i in self.dict.keys(): 
                self.dict[i].ifliph()
                self.symh(i)                  
    def ofliph(self):# flip group horizontally to original orientation
        if self.flippedh:
            self.flippedh=False
            for i in self.dict.keys(): 
                self.dict[i].ofliph()
                self.symh(i)    
    def flipv(self): # flip group vertically
        self.flippedv=not self.flippedv
        for i in self.dict.keys(): 
            self.dict[i].flipv()
            self.symv(i) 
    def iflipv(self):# flip group vertically to inverted orientation
        if not self.flippedv:
            self.flippedv=True
            for i in self.dict.keys(): 
                self.dict[i].iflipv()
                self.symv(i)   
    def oflipv(self):# flip group vertically to original orientation
        if self.flippedv:
            self.flippedv=False
            for i in self.dict.keys(): 
                self.dict[i].oflipv()
                self.symv(i)
    def scale(self,s):# scale group (permanent)
        self.s *= s# update dispgroup scale
        for i in self.dict.keys():
            self.dict[i].scale(s)# scale element
            self.dictx[i] *= s# update element position in dispgroup
            self.dicty[i] *= s
            self.dict[i].movetox(self.x+self.dictx[i])# update element position
            self.dict[i].movetoy(self.y+self.dicty[i])
    def rotate(self,r):# rotate group (permanent)
        self.r += r# update dispgroup rotation
        for i in self.dict.keys():
            self.dict[i].rotate(r)
    def devtools(self):
        share.crossdisplay((self.x,self.y),10,share.colors.devdispgroup,6,diagonal=True)            
    def play(self,controls): # play all animations and display all images (in order of append)
        for i in self.dict.values(): i.play(controls)
        # for i in self.dict.keys(): # Force elements position relative to dispgroup each frame (unecessary)
        #     self.dict[i].movetox(self.x+self.dictx[i])
        #     self.dict[i].movetoy(self.y+self.dicty[i])
        if share.devmode: self.devtools()

####################################################################################################################

