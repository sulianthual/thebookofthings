#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# draw.py: game draws = main display objects that can be added to a page in the book
#         (drawing,textinput,textchoice,textbox,image,animation,dispgroup)
#
##########################################################
##########################################################

import pygame
#
import share
import utils
        
####################################################################################################################

# A drawing (image to edit interactively by the player)
# *DRAWING
class obj_drawing:
    def __init__(self,name,xy,base=None,legend=None,borders=(True,True,True,True)):# start new drawing (load or new)
        self.type='drawing'# object type
        self.name=name# drawing name
        self.xy=xy# drawing position on screen (x,y), CENTER OF THE DRAWING
        self.base=base# drawing base (drawn over, part of final drawing), must be other drawing object (same dimensions)
        self.borders=borders# draw each border or not (west,east,north,south)
        # Load brush
        self.brush=share.brushes.pen# currently used brush (can be changed externally)
        # Load drawing function with mouse
        self.mousedrawing=obj_mousedrawing()
        self.eraseonareahover=True# erase only if mouse hovers drawing area (useful if multiple drawings on screen)
        # Load shadow (must exist)
        if utils.pathexists('shadows/'+self.name+'.png'):
            self.imgbase=pygame.image.load('shadows/'+self.name+'.png')#do not convert!
        else:
            self.imgbase=pygame.image.load('data/error.png')#do not convert!
        self.imgbase.set_colorkey(share.colors.colorkey)
        self.size=self.imgbase.get_rect().size
        self.xytl=(self.xy[0]-int(self.size[0]/2), self.xy[1]-int(self.size[1]/2))# position of top left corner
        self.rect=(self.xytl[0],self.xytl[0]+self.size[0],self.xytl[1],self.xytl[1]+self.size[1])# drawing rectangle area
        # Load drawing (or create empty one)
        if utils.pathexists('book/'+self.name+'.png'):
            self.drawing=pygame.image.load('book/'+self.name+'.png').convert()
        else:
            self.drawing=pygame.Surface(self.size)
            self.reset()
        self.drawing.set_colorkey(share.colors.colorkey)# set white as colorkey (that color will not be displayed) 
        # legend (displayed under drawing, optional)
        self.legend=legend
        self.legend_surface=[]
        self.legend_xtl=0
        self.legend_ytl=0
        if self.legend: self.makelegend(self.legend)
    def reset(self):
        self.drawing.fill(share.colors.colorkey)# erase drawing
        self.drawing.blit(self.imgbase,(0,0))# add shadow
    def display(self):
        pygame.draw.rect(share.screen, share.colors.colorkey, (self.xytl[0], self.xytl[1], self.size[0],self.size[1]), 0)# white background
        if self.base:
            share.screen.blit(self.base.drawing,self.xytl)# display other drawing base at 
        # share.screen.blit(self.imgbase,self.xytl)# display shadow
        share.screen.blit(self.drawing,self.xytl)# display drawing
        # pygame.draw.rect(share.screen, (220,0,0), (self.xytl[0], self.xytl[1], self.size[0],self.size[1]), 3)# borders (optional)
        self.displayborders()
        self.displaylegend()
    def displayborders(self):
        if self.borders[0]:
            pygame.draw.line(share.screen,share.colors.drawing,\
                             (self.xytl[0],self.xytl[1]),(self.xytl[0],self.xytl[1]+self.size[1]),3)# left
        if self.borders[1]:
            pygame.draw.line(share.screen,share.colors.drawing,\
                             (self.xytl[0]+self.size[0],self.xytl[1]),(self.xytl[0]+self.size[0],self.xytl[1]+self.size[1]),3)# right
        if self.borders[2]:
            pygame.draw.line(share.screen,share.colors.drawing,\
                             (self.xytl[0],self.xytl[1]),(self.xytl[0]+self.size[0],self.xytl[1]),3)# top
        if self.borders[3]:
            pygame.draw.line(share.screen,share.colors.drawing,\
                             (self.xytl[0],self.xytl[1]+self.size[1]),(self.xytl[0]+self.size[0],self.xytl[1]+self.size[1]),3)# bottom
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
        pygame.image.save(term, 'book/'+self.name+'.png')# save drawing

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
    def __init__(self,key,nchar,xy,color=(0,0,0),legend=None):
        self.type='textinput'# object type
        self.key=key
        self.nchar=nchar# max number of characters
        self.xy=xy# center position
        self.color=color# text color
        self.legend=legend
        self.setup()
    def setup(self):
        self.texttodict()
        self.font=share.fonts.font50# text font
        self.xmargin=20# margin left/right
        self.ymargin=10#margin top/bottom
        self.makeframe()# make frame for text
        self.legend_surface=[]
        self.legend_xtl=0
        self.legend_ytl=0 
        if self.legend: self.makelegend(self.legend)
    def texttodict(self):# get text value to/from dictionary
        if self.key in share.words.dict:
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
        word_surface=self.font.render(self.text,True,self.color)# could prerender only on changetext
        text_width,text_height=word_surface.get_size()
        termx=self.xytl[0]+int(self.size[0]/2)+self.xmargin-int(text_width/2)
        termy=self.xytl[1]+self.ymargin
        share.screen.blit(word_surface,(termx,termy) )# display text
        pygame.draw.rect(share.screen, share.colors.textinput, \
                         (self.xytl[0], self.xytl[1], self.size[0]+self.xmargin*2,self.size[1]+self.ymargin*2), 3)     
        self.displaylegend()
    def makelegend(self,legend):# make legend (and prerender)
        self.legend=legend
        self.legend_surface=share.fonts.font30.render(legend, True, (0,0,0))
        text_width, text_height=self.legend_surface.get_size()
        self.legend_xtl=int( self.xytl[0] + self.size[0]/2 +self.xmargin - text_width/2 )
        self.legend_ytl=int( self.xytl[1] + self.size[1] + text_height/2 )
    def displaylegend(self):# display prerendered legend
        if self.legend:
            share.screen.blit(self.legend_surface, (self.legend_xtl,self.legend_ytl))
    def changetext(self,controls):        
        if utils.isinrect(controls.mousex,controls.mousey,self.rect):# edit only if mouse in frame
            self.text=controls.edittext(self.text)# edit text
            # Note: apparently no need to filter special characters ( \, ', ", {, }, etc )
            if len(self.text)>self.nchar: self.text=self.text[:self.nchar-1]# control max size
    def update(self,controls):
        self.display()
        self.changetext(controls)
    def finish(self):
        share.words.dict[self.key]=self.text# update text value in dictionary
        share.words.save()# resave (entire) dictionary of words in file

####################################################################################################################
#
# A text choice: similar to textinput (saves keyword) but must select between choices      
# $ textchoice=draw.obj_textchoice('herogender')
# $ textchoice.addchoice('1. A guy','he',(340,360))
# $ textchoice.addchoice('2. A girl','she',(640,360))
# $ textchoice.addkey('hero_his',{'he':'his','she':'her'})
class obj_textchoice:
    def __init__(self,key):
        self.type='textchoice'# object type
        self.key=key# key from choice that will be saved (in words.txt)
        self.setup()
    def setup(self):
        self.choices=[]# choices data
        self.ichoice=0# selected choice
        self.morekeys=[]# additional keys from choice
        self.xmargin=20# margin left/right
        self.ymargin=10# margin top/bottom
        self.keytodict(self.key)
    def keytodict(self,key):# write key in dictionary if not there
        if not key in share.words.dict: share.words.dict[key]=''   
    def addchoice(self,text,value,xy,fontsize='medium',bold=True,color=(0,0,0)):
        img=share.fonts.font(fontsize).render(text, bold, color)
        size=img.get_size()
        area=( int(xy[0]-size[0]/2-self.xmargin), int(xy[0]+size[0]/2+self.xmargin),\
              int(xy[1]-size[1]/2-self.ymargin),int(xy[1]+size[1]/2+self.ymargin) )
        self.choices.append( (value,img,xy,size,area) )
        self.checkchoice()
    def checkchoice(self):# check current choice from possible value matches
        for c,i in enumerate(self.choices): 
            value,img,xy,size,area=i
            if (self.key in share.words.dict) and share.words.dict[self.key]==value: 
                self.ichoice=c
                break
    def changechoice(self,controls):
        if controls.mouse1 and controls.mouse1c: 
            for c,i in enumerate(self.choices):
                value,img,xy,size,area=i
                if utils.isinrect(controls.mousex,controls.mousey,area): 
                    self.ichoice=c
                    break# break for loop
    def choicetodict(self):# write key choice in words dict
        if self.choices:
            value,img,xy,size,area=self.choices[self.ichoice]
            share.words.dict[self.key]=value            
    def addkey(self,key,analogies):# add a key affected by choice (with dict of analogies of values)
        self.keytodict(key)
        self.morekeys.append( (key,analogies) )
    def morekeystodict(self):# write addictional key choices in words dict
        for i in self.morekeys:
            key,analogies=i# 'hero_his',{'he':'his','she':'her'}
            for j in analogies.keys():
                if j==share.words.dict[self.key]:
                    share.words.dict[key]=analogies[j]
                    break
    def display(self):
        for c,i in enumerate(self.choices): 
            value,img,xy,size,area=i
            termx=xy[0]-size[0]/2
            termy=xy[1]-size[1]/2
            share.screen.blit(img,(int(termx),int(termy)))  
            if c==self.ichoice:
                rect=(termx-self.xmargin, termy-self.ymargin, size[0]+2*self.xmargin,size[1]+2*self.ymargin)
                pygame.draw.rect(share.screen,share.colors.textchoice,rect, 3)          
    def play(self,controls):
        self.display()
        self.changechoice(controls)
    def update(self,controls):
        self.play(controls)
    def finish(self):
        self.choicetodict()
        self.morekeystodict()
        share.words.save()# save dictionary of words on file

        
####################################################################################################################
#  
# A text box
# acts like an image (can be moved/scaled, part of a animgroup)
class obj_textbox:
    def __init__(self,text,xy,fontsize='medium',color=(0,0,0),scale=1):
        self.type='textbox'# object type
        self.text=text
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.fontsize=fontsize# font size of text (default=medium)
        self.color=color# color of text (default=black)
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):
        self.x=self.xini# center of textbox
        self.y=self.yini
        self.xc=0# position correction (from rotation)
        self.yc=0# 
        self.s= 1# scaling factor
        self.r= 0# rotation angle (degree)         
        self.bold=True#bold or not
        self.fh=False# is image flipped horizontally (inverted) or not (original)
        self.fv=False# is image flipped vertically (inverted) or not (original)
        self.show=True# show the image or not (can be toggled on/off)
        self.replacetext(self.text)
    def replacetext(self,text):   
        self.img=share.fonts.font(self.fontsize).render(text, self.bold, self.color)
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
        self.fh= not self.fh
        self.img=pygame.transform.flip(self.img,True,False)
    def ifliph(self): # flip image horizontally to inverted
        if not self.fh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.fh=True
    def ofliph(self): # flip image horizontally to original
        if self.fh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.fh=False
    def flipv(self): # flip image vertically
        self.fv= not self.fv
        self.img=pygame.transform.flip(self.img,False,True)
    def iflipv(self): # flip image vertically to inverted
        if not self.fv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.fv=True
    def oflipv(self): # flip image vertically to original
        if self.fv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.fv=False
    def scale(self,s): # scale image by given factor s (permanent)
        self.s *= s
        self.img=pygame.transform.scale(self.img,(int(self.imgsize[0]*s),int(self.imgsize[1]*s)))
        self.imgsize=self.img.get_rect().size
    def rotate(self,r): # rotate image by given angle r (permanent)
        self.r += r# DO NOT OVERDO: ENLARGENS IMAGE WITH MEMORY ISSUES
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]
    def rotate90(self,r):# rotate image in 90 increments nonly
        self.r += int(round(r%360/90,0)*90)# find closest increment (in 0,90,180,270)
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]        
    def display(self):
        if self.show:
            xtl=self.x-self.imgsize[0]/2 +self.xc# top left corner position
            ytl=self.y-self.imgsize[1]/2 +self.yc
            share.screen.blit(self.img,(int(xtl),int(ytl)))
    def devtools(self):
        utils.crossdisplay((self.x,self.y),10,share.colors.devtextbox,3)
        termx,termy=self.img.get_rect().size
        pygame.draw.rect(share.screen,share.colors.devtextbox, (int(self.x-termx/2), int(self.y-termy/2), termx,termy), 3)  
    def play(self,controls):# same as display, but renamed for consitency with play() for animations, dispgroups
        self.display()
        if share.devmode: self.devtools()# dev tools
    def update(self,controls):
        self.play(controls)        
        
####################################################################################################################

# A simple image (from the book folder) to display at a given location
class obj_image:
    def __init__(self,name,xy,scale=1):
        self.type='image'# object type
        self.name=name
        self.xini=xy[0]# xy is the CENTER of the image on screen
        self.yini=xy[1]
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):#
        self.img=self.readimage(self.name)
        self.imgsize=self.img.get_rect().size
        self.x=self.xini# image correction
        self.y=self.yini
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.xc=0# position correction (due to rotation)
        self.yc=0
        self.fh=False# is image flipped horizontally (inverted) or not (original)
        self.fv=False# is image flipped vertically (inverted) or not (original)
        self.show=True# show the image or not (can be toggled on/off)
    def readimage(self,name):
        if utils.pathexists('book/'+name+'.png'):
            img=pygame.image.load('book/'+name+'.png').convert()# load drawing image
        else:
            img=pygame.image.load('data/error.png').convert()# load error image        
        img.set_colorkey(share.colors.colorkey)# set white as colorkey (that color will not be displayed) 
        return img
    def replaceimage(self,newimgname):# replace existing image with new one
        self.name=newimgname
        img=self.readimage(self.name)
        # reapply reference transformations (fliph,flipv,scale, rotate...)
        if self.fh: img=pygame.transform.flip(img,True,False)
        if self.fv: img=pygame.transform.flip(img,False,True)
        if self.s != 1: 
            imgsize=img.get_rect().size
            img=pygame.transform.scale(img,(int(imgsize[0]*self.s),int(imgsize[1]*self.s)))
        if self.r != 0: img=pygame.transform.rotate(img,self.r)
        # assign
        self.img=img
        self.imgsize=self.img.get_rect().size
    def movetox(self,x): # move to x
        self.x=x
    def movetoy(self,y): # move to y
        self.y=y
    def movex(self,dx): # displace by dx
        self.x += dx
    def movey(self,dy): #displace by dy
        self.y += dy
    def fliph(self): # flip image horizontally
        self.fh= not self.fh
        self.img=pygame.transform.flip(self.img,True,False)
    def ifliph(self): # flip image horizontally to inverted
        if not self.fh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.fh=True
    def ofliph(self): # flip image horizontally to original
        if self.fh:
            self.img=pygame.transform.flip(self.img,True,False)
            self.fh=False
    def flipv(self): # flip image vertically
        self.fv= not self.fv
        self.img=pygame.transform.flip(self.img,False,True)
    def iflipv(self): # flip image vertically to inverted
        if not self.fv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.fv=True
    def oflipv(self): # flip image vertically to original
        if self.fv:
            self.img=pygame.transform.flip(self.img,False,True)
            self.fv=False
    def scale(self,s): # scale image by given factor s (permanent)
        self.s *= s
        self.img=pygame.transform.scale(self.img,(int(self.imgsize[0]*s),int(self.imgsize[1]*s)))
        self.imgsize=self.img.get_rect().size
    def rotate(self,r): # rotate image by given angle r (permanent)
        self.r += r# DO NOT OVERDO: ENLARGENS IMAGE WITH MEMORY ISSUES
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]
    def rotate90(self,r):# rotate image in 90 increments nonly
        self.r += int(round(r%360/90,0)*90)# find closest increment (in 0,90,180,270)
        center1=self.img.get_rect().center
        self.img=pygame.transform.rotate(self.img,r)
        center2= self.img.get_rect().center 
        self.xc +=center1[0]-center2[0]
        self.yc +=center1[1]-center2[1]       
    def display(self):
        if self.show:
            xtl=self.x-self.imgsize[0]/2 +self.xc
            ytl=self.y-self.imgsize[1]/2 +self.yc
            share.screen.blit(self.img,(int(xtl),int(ytl)))
    def devtools(self):
        utils.crossdisplay((self.x,self.y),10,share.colors.devimage,3)
        termx,termy=self.img.get_rect().size
        pygame.draw.rect(share.screen,share.colors.devimage, (int(self.x-termx/2), int(self.y-termy/2), termx,termy), 3)            
    def play(self,controls):# update,play,display kept for consistency and calls
        self.display()
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)  

####################################################################################################################

# Animate an image on screen
# Consists of base image(s) (can be transformed permanently) + animation transformations(t) (reapplied each frame)
#* ANIMATION  
class obj_animation:      
    def __init__(self,name,imgname,xy,record=False,scale=1):
        self.type='animation'# object type
        self.name=name# animation name
        self.imgname=imgname# reference image (more can be added)
        self.xini=xy[0]# reference position of animation ( (0,0)=default or center of screen)
        self.yini=xy[1]
        self.record=record# ability to record this animation
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):
        # Parameters (and permanent changes)
        self.show=True# show the animation or not (can be toggled on/off)
        self.x=self.xini# animation center (changed externally)
        self.y=self.yini# animation position (changed externally)
        self.fh=False# animation flipped horizontally or not
        self.fv=False# animation flipped vertically or not
        self.r=0# rotation angle (default =0)
        self.s=1# scaling factor (default =1)
        self.xc=0# position correction (from permanent rotation r)
        self.yc=0# 
        self.xt=0# animation image screen position each frame (top left corner)
        self.yt=0
        # Images
        self.setupimages()# setup images
        # Animation 
        self.setupanimation()
    ######
    # Part I: IMAGES (basis of animation)
    def setupimages(self): # setup images
        self.img_ini=self.readimage(self.imgname)
        self.imglist=[]# list of all available images
        self.imglist.append(self.img_ini)
    def readimage(self,imgname):# read image on file
        if utils.pathexists('book/'+imgname+'.png'):# load  image
            img=pygame.image.load('book/'+imgname+'.png').convert()
        else:
            img=pygame.image.load('data/error.png').convert()
        img.set_colorkey(share.colors.colorkey)# set white to transparent
        return img
    def addimage(self,imgname):# add an image to list of available ones for animation
        img=self.readimage(imgname)      
        self.imglist.append(img)
    def replaceimage(self,newimgname,index):# replace image with new one (must be same dimensions!)
        if index >-1 and index<len(self.imglist):
            img=self.readimage(newimgname)
            # reapply permanent transformations (fliph,flipv,scale, rotate...)
            if self.fh: img=pygame.transform.flip(img,True,False)
            if self.fv: img=pygame.transform.flip(img,False,True)
            if self.s != 1: 
                sizex,sizey=img.get_rect().size
                img=pygame.transform.scale(img,(int(sizex*self.s),int(sizey*self.s)))
            if self.r != 0: img=pygame.transform.rotate(img,self.r)
            self.imglist[index]=img
    ######
    # PART II: ANIMATION (transformations reapplied each frame to images)
    def setupanimation(self):
        self.recording=False# Edit Mode On/Off (can be toggled)
        self.ntmax=False# max duration (number of frames) (ntmax=False means unlimited)
        self.tstart=0# start time offset when playing animation (0=default)
        self.aniname='animations/'+self.name+'.txt'# animation name
        self.eraseanimation()# erase animation
        if utils.pathexists(self.aniname): self.load()# load animation (if exists)
    def eraseanimation(self):# reset animation (=image transformations(t) )entirely
        # Animation transformations
        self.animation=[]# animation vector
        self.nt=False# animation length (False if none)
        self.ta=self.tstart# animation time increment        
        self.xa=0# animation position around reference
        self.ya=0
        self.fha=False# horizontal flip (boolean)
        self.fva=False# vertical flip (boolean)
        self.ra=0# rotation angle (int, in degrees)
        self.sa=0# scaling factor (int): scaling = bsa**sa
        self.bsa=1.01# base for animation scaling
        self.ia=0# index of image used (0=default, >0=next images) 
    def firstframe(self):# reset animation to first frame
        self.ta=0
    def recorder_infos(self):
        # Display Informations for Record Mode (not prerendered but doesnt matter)
        share.screen.blit(share.fonts.font15.render('- RECORD MODE -', True, (255, 0, 0)), (1180,135)) 
        share.screen.blit(share.fonts.font15.render('Space: Toggle Mode', True, (255, 0, 0)), (1180,155)) 
        share.screen.blit(share.fonts.font15.render('Backspace: Reset', True, (255, 0, 0)), (1180,175))        
        share.screen.blit(share.fonts.font15.render('LMouse: Record', True, (255, 0, 0)), (1180,195)) 
        share.screen.blit(share.fonts.font15.render('a-d: rotate', True, (255, 0, 0)), (1180,215)) 
        share.screen.blit(share.fonts.font15.render('w-s: scale', True, (255, 0, 0)), (1180,235)) 
        share.screen.blit(share.fonts.font15.render('q-e: flip', True, (255, 0, 0)), (1180,255)) 
        share.screen.blit(share.fonts.font15.render('r: Save', True, (255, 0, 0)), (1180,275))
        share.screen.blit(share.fonts.font15.render('f: change image', True, (255, 0, 0)), (1180,295))
    def recorder(self,controls):# record animation with dev controls
        self.recorder_infos()
        # Position
        self.xa=controls.mousex-self.xini# anomalies around reference
        self.ya=controls.mousey-self.yini
        # Transformations
        if controls.q and controls.qc: self.fha = not self.fha# toggle horizontal flip
        if controls.e and controls.ec: self.fva = not self.fva# toggle vertical flip
        if controls.a: self.ra += 1
        if controls.d: self.ra -= 1
        if controls.w: self.sa += 1# (scaling is in bsa**sa)
        if controls.s: self.sa -= 1 
        if controls.f and controls.fc: self.ia += 1 # change image
        if self.ia > len(self.imglist)-1: self.ia =0# reset to first image
        # Record Frame  
        if controls.mouse1:
            if self.ntmax:# imposed max duration
                if len(self.animation)<self.ntmax:
                    self.animation.append([self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia])
                    self.ta += 1
            else:# no imposed max duration
                self.animation.append([self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia])
                self.ta += 1                
        if controls.backspace and controls.backspacec: self.eraseanimation()# Erase animation        
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
        utils.crossdisplay((self.xini,self.yini),10,(0,0,255),3) 
    def save(self):# save animation to file      
        f1=open(self.aniname, 'w+')
        f1.write('t,x,y,fh,fv,r,s,frame:'+'\n')# first line
        for i in range(0,len(self.animation)):
            line=str(self.animation[i][0])# ta
            line +=','+str(self.animation[i][1])# xa 
            line +=','+str(self.animation[i][2])# ya
            if self.animation[i][3]: # fha (boolean to 0-1)
                line +=','+'1'
            else:
                line +=','+'0'
            if self.animation[i][4]: # fva (boolean to 0-1)
                line +=','+'1'
            else:
                line +=','+'0' 
            line +=','+str(self.animation[i][5])# ra
            line +=','+str(self.animation[i][6])# sa
            line +=','+str(self.animation[i][7])# ia
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
                vect.append(int(line[0]))# ta
                vect.append(int(line[1]))# xa
                vect.append(int(line[2]))# ya
                if int(line[3]) == 1:# fha 
                    vect.append(True)
                else:
                    vect.append(False)
                if int(line[4]) == 1:# fva 
                    vect.append(True)
                else:
                    vect.append(False)
                vect.append(int(line[5]))# ra
                vect.append(float(line[6]))# sa
                vect.append(int(line[7]))# ia 
                self.animation.append(vect)
        f1.close()   
        if self.animation:# compute animation length
            self.nt=len(self.animation)
        else:
            self.nt=False
    ### PART III: Permanent changes
    def movetox(self,x): # move to x
        self.x=x
    def movetoy(self,y): # move to y
        self.y=y
    def movex(self,x): # displace all images by dx (permanent)
        self.x += x
    def movey(self,y): #displace all images by dy (permanent)
        self.y += y  
    def fliph(self):# flip all animation images horizontally
        self.fh= not self.fh
        for i,value in enumerate(self.imglist):
            self.imglist[i]=pygame.transform.flip(value,True,False)        
    def flipv(self):# flip all animation images vertically
        self.fv= not self.fv
        for i,value in enumerate(self.imglist):
            self.imglist[i]=pygame.transform.flip(value,False,True)           
    def ifliph(self): # flip all animation images  horizontally (if not already flipped)
        if not self.fh:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,True,False)
            self.fh=True
    def ofliph(self): # unflip all animation images horizontally (if already flipped)
        if self.fh:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,True,False)
            self.fh=False    
    def iflipv(self): # flip all animation images  vertically (if not already flipped)
        if not self.fv:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,False,True)
            self.fv=True
    def oflipv(self): # unflip all animation images vertically (if already flipped)
        if self.fv:
            for i,value in enumerate(self.imglist):
                self.imglist[i]=pygame.transform.flip(value,False,True)
            self.fv=False 
    def scale(self,s): # permanent scaling by factor s 
        self.s *= s
        for i,value in enumerate(self.imglist):
            sizex,sizey=value.get_rect().size
            self.imglist[i]=pygame.transform.scale(value,(int(sizex*s),int(sizey*s)))
    def rotate90(self,r):# rotate image in 90 increments nonly 
        self.r += int(round(r%360/90,0)*90)# find closest increment (in 0,90,180,270)
        cx1,cy1=self.imglist[0].get_rect().center
        for i,value in enumerate(self.imglist):            
            self.imglist[i]=pygame.transform.rotate(value,r)
        cx2,cy2= self.imglist[0].get_rect().center 
        self.xc +=cx1-cx2# correction computed from first image
        self.yc +=cy1-cy2# (correction wrong if other images have different sizes)    
    #def rotate(self,r) not implemented (enlargens-memory issues and complex corrections to self.xa, self.ya)
    ######
    # Part VI: General
    def playback(self):# play back animation (loop)
        self.ta +=1
        if self.ta > len(self.animation)-1: self.ta=0
        if self.animation:# read animation state at time
            term,self.xa,self.ya,self.fha,self.fva,\
                self.ra,self.sa,self.ia=self.animation[self.ta]
            self.display()
    def display(self):# display one animation frame (either when playing or recording)
        if self.show:
            if self.ia<len(self.imglist):
                self.imgt=self.imglist[self.ia]# base image
            else:
                self.imgt=self.imglist[0]# error image frame out of range, take first image frame
            sizex,sizey=self.imgt.get_rect().size
            # Apply Transformations (reapplied each frame to base image)
            if self.fha: self.imgt=pygame.transform.flip(self.imgt,True,False)
            if self.fva: self.imgt=pygame.transform.flip(self.imgt,False,True)
            if self.sa != 0: # (scale before rotation)
                ssa=self.bsa**self.sa# frame scaling
                self.imgt=pygame.transform.scale(self.imgt,(int(sizex*ssa),int(sizey*ssa)))
            else:
                ssa=1
            if self.ra != 0: 
                self.ra *= 1 - 2*int(self.fh)# rotation direction inverts with fh,fv!
                self.ra *= 1 - 2*int(self.fv)# 
                cx1,cy1=self.imgt.get_rect().center
                self.imgt=pygame.transform.rotate(self.imgt,self.ra)
                cx2,cy2= self.imgt.get_rect().center 
                rcdx=cx1-cx2# correction from frame rotation
                rcdy=cy1-cy2
            else:
                rcdx=0
                rcdy=0
            # animation position xa,ya: apply corrections from frame scaling and rotation (sa,ra)
            # and also apply corrections from permanent changes (movex,fh,fv,s,r)
            # ALMOST PERFECT BUT STILL SMALL ERRORS (FROM rotate90 r)
            termx =  self.xa# position of animation (relative to animation center) 
            termy =  self.ya  
            termx *= self.s# correction permanent scaling(s)
            termy *= self.s
            termx *= 1 - 2*int(self.fh)# *=1 if fh=False, *=-1 if fh=True
            termy *= 1 - 2*int(self.fv)# 
            r=int(round(self.r%360/90,0)*90)# (r=0,90,180 or 270)
            if r==90:# correction from rotate90 (r=0,90,180 or 270)
                termx,termy=termy,-termx
                termx += -sizey*ssa/2# correction image center to top left
                termy += -sizex*ssa/2
            elif r==180:
                termx,termy=-termx,-termy
                termx += -sizex*ssa/2
                termy += -sizey*ssa/2
            elif r==270:
                termx,termy=-termy,termx
                termx += -sizey*ssa/2
                termy += -sizex*ssa/2
            else:            
                termx += -sizex*ssa/2
                termy += -sizey*ssa/2
            termx += rcdx# correction frame rotation(ra)
            termy += rcdy
            termx += self.xc# correction permanent rotation90(r)
            termy += self.yc
            termx += self.x# movex, movetox
            termy += self.y# movey, movetoy
            self.xt=termx
            self.yt=termy
            share.screen.blit(self.imgt,(int(termx),int(termy)))
    def devtools(self):        
        termx,termy=self.imgt.get_rect().size
        pygame.draw.rect(share.screen,share.colors.devanimation, (int(self.xt), int(self.yt), termx,termy), 3)          
        if not self.recording: utils.crossdisplay((self.x,self.y),10,share.colors.devanimation,3)
    def play(self,controls):
        if self.record:# ability to record 
            if share.devmode and controls.space and controls.spacec: self.recording= not self.recording# switch mode  
        if self.recording: 
            self.recorder(controls)# record mode
        else:
            self.playback()# playback mode
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)        
            

####################################################################################################################

# Group of Display Elements (Animations, Images or textboxes)
# Can apply transformations (move,flip,scale,rotate) while conserving properties (distance between elements)
# Every Element must have the followed fonctionalities (called/modified by the dispgroup):
#  self.xini, self.yini: reference position (used to compute conserved distances)
#  self.x, self.y: position
#  self.play(): display function
#  self.fliph(): flip image function (also must have ofliph, ifliph, same for flipv)
#  self.scale(): scale 
#  self.rotate90(): rotation in increments of 90 degrees
#  (rotation of elements not implemented due to issues with image size changes)
class obj_dispgroup:
    def __init__(self,xy,scale=1):
        self.type='dispgroup'# object type
        self.xini=xy[0]# position center of group
        self.yini=xy[1]
        self.reset()
        if scale != 1: self.scale(scale)
    def reset(self): # reset all (and erase lists)
        self.dict={}# dictionary of elements
        self.dictx={}# relative positions of elements (relative to self.x when element is added)
        self.dicty={}
        self.x=self.xini# x position of group (useful to track overall position, starts a xini, yini)
        self.y=self.yini
        self.fh=False# flipped horizontally (inverted) or not (original)
        self.fv=False# flipped vertically (inverted) or not (original)
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
        self.fh=not self.fh
        for i in self.dict.keys(): 
            self.dict[i].fliph()
            self.symh(i)  
    def ifliph(self):# flip group horizontally to inverted orientation
        if not self.fh:
            self.fh=True
            for i in self.dict.keys(): 
                self.dict[i].ifliph()
                self.symh(i)                  
    def ofliph(self):# flip group horizontally to original orientation
        if self.fh:
            self.fh=False
            for i in self.dict.keys(): 
                self.dict[i].ofliph()
                self.symh(i)    
    def flipv(self): # flip group vertically
        self.fv=not self.fv
        for i in self.dict.keys(): 
            self.dict[i].flipv()
            self.symv(i) 
    def iflipv(self):# flip group vertically to inverted orientation
        if not self.fv:
            self.fv=True
            for i in self.dict.keys(): 
                self.dict[i].iflipv()
                self.symv(i)   
    def oflipv(self):# flip group vertically to original orientation
        if self.fv:
            self.fv=False
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
    def rotate90(self,r):# rotate group in 90 increments (permanent)
        r=int(round(r%360/90,0)*90)# r in 0,90,180,270
        self.r += r
        for i in self.dict.keys():
            self.dict[i].rotate90(r)
            termx,termy=self.dictx[i],self.dicty[i]
            if r==90:
                self.dictx[i],self.dicty[i]=termy,-termx
            elif r==180: 
                self.dictx[i],self.dicty[i]=-termx,-termy
            if r==270:
                self.dictx[i],self.dicty[i]=-termy,termx                
            self.dict[i].movetox(self.x+self.dictx[i])# update element position
            self.dict[i].movetoy(self.y+self.dicty[i])
    def devtools(self):
        utils.crossdisplay((self.x,self.y),10,share.colors.devdispgroup,6,diagonal=True)            
    def play(self,controls): # play all animations and display all images (in order of append)
        for i in self.dict.values(): i.play(controls)
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)  
####################################################################################################################

