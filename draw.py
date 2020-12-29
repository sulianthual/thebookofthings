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

import share
import tool
import core


####################################################################################################################

# A drawing (image to edit interactively by the player)
# *DRAWING
class obj_drawing:
    def __init__(self,name,xy,base=None,legend=None):# start new drawing (load or new)
        self.type='drawing'
        self.name=name# drawing name
        self.x,self.y = xy
        self.base=base# basis (other drawing object)
        self.legend=legend
        self.setup()
    def setup(self):
        # drawing tools
        self.mousedraw=obj_mousedraw()# mouse drawing tool
        self.brush=core.obj_sprite_brush()
        self.brush.makebrush(share.brushes.pen)
        # shadow
        self.sprite_shadow=core.obj_sprite_image()
        self.sprite_shadow.load('shadows/'+self.name+'.png',convert=False)
        self.rx,self.ry=self.sprite_shadow.getrxry()
        # base
        if self.base: 
            self.sprite_base=core.obj_sprite_image()
            self.sprite_base.makeempty(self.rx,self.ry)
            self.sprite_base.blitfrom(self.base.sprite,0,0)        
        # drawing
        self.sprite=core.obj_sprite_image()
        self.sprite.load('book/'+self.name+'.png',failsafe=False)
        if not self.sprite.surf: self.resetdrawing()# drawing not found
        # frame
        self.sprite_frame=core.obj_sprite_rect()
        self.makeframe()
        # legend
        self.sprite_legend=core.obj_sprite_text()
        if self.legend: self.makelegend(self.legend)
    def resetdrawing(self):
        self.sprite.clear()
        self.sprite.blitfrom(self.sprite_shadow,0,0)  
    def draw(self,controls):
        if controls.mouse1: self.mousedraw(controls,self.sprite,self.brush,self.x,self.y)
        if controls.mouse2 and tool.isinrect(controls.mousex,controls.mousey,self.rect): self.resetdrawing()
    def basedraw(self):
        if self.base: 
            self.sprite_base.clear()
            self.sprite_base.blitfrom(self.base.sprite,0,0)
    def makeframe(self):
        self.sprite_frame.make()
        self.rect=(self.x-self.rx,self.x+self.rx,self.y-self.ry,self.y+self.ry)
    def makelegend(self,legend):
        self.legend=legend
        formattextkwargs=share.datamanager.getwords()
        self.legend=tool.formattext(self.legend,**formattextkwargs)# replace with book of things keywords
        self.sprite_legend.make(self.legend,share.fonts.font('medium'),(0,0,0),bold=True)
        termx,termy=self.sprite_legend.getrxry()
        self.xl,self.yl =self.x, self.y+self.ry+termy
    def display(self):
        if self.base: self.sprite_base.display(self.x,self.y)
        self.sprite.display(self.x,self.y)
        self.sprite_frame.display(share.colors.drawing,(self.x,self.y,2*self.rx,2*self.ry))
        if self.legend: self.sprite_legend.display(self.xl,self.yl)
    def update(self,controls):
        self.draw(controls)
        self.basedraw()
        self.display()
    def finish(self):
        if self.base: 
            self.sprite_base.blitfrom(self.sprite,0,0)# to base
            self.sprite.clear()
            self.sprite.blitfrom(self.sprite_base,0,0)# back        
        self.sprite.save('book/'+self.name+'.png')


# Tool for drawing with the mouse
class obj_mousedraw:
    def __init__(self):
        self.mousexr=0
        self.mouseyr=0
    def __call__(self,controls,sprite,sprite_brush,x,y):
        if controls.mouse1:
            xoff=int(x-sprite.getrx()+sprite_brush.getrx())
            yoff=int(y-sprite.getry()+sprite_brush.getry())
            sprite.blitfrom(sprite_brush,controls.mousex-xoff,controls.mousey-yoff)
            if controls.mouse1c:# mouse just pressed
                self.mousexr=controls.mousex# record mouse position
                self.mouseyr=controls.mousey
            else:# mouse held
                # draw line between current and last mouse position
                dx=controls.mousex-self.mousexr
                dy=controls.mousey-self.mouseyr
                dist=max(abs(dx),abs(dy))
                for i in range(dist):
                    xi = int( self.mousexr + float(i)/dist*dx)
                    yi = int( self.mouseyr + float(i)/dist*dy)
                    sprite.blitfrom(sprite_brush,xi-xoff,yi-yoff)
                self.mousexr=controls.mousex
                self.mouseyr=controls.mousey


####################################################################################################################

# A text input
class obj_textinput:
    def __init__(self,key,nchar,xy,color=(0,0,0),legend=None):
        self.type='textinput'
        self.key=key# key from textinput that will be saved
        self.nchar=nchar# max number of characters
        self.x,self.y = xy# position
        self.color=color
        self.legend=legend
        self.setup()
    def setup(self):
        self.texttodict()
        self.font=share.fonts.font('medium')# text font
        self.xm,self.ym=20,10# margins
        # sprite
        self.sprite=core.obj_sprite_text()
        # frame
        self.sprite_frame=core.obj_sprite_rect()
        self.makeframe()# make frame for text
        # legend
        self.sprite_legend=core.obj_sprite_text()
        if self.legend: self.makelegend(self.legend)
    def texttodict(self):# text to/from dictionary
        if self.key in share.datamanager.getwordkeys():
            self.text=share.datamanager.getword(self.key)
        else:# create key with empty text
            share.datamanager.writeword(self.key,'')
            self.text=''    
    def changetext(self,controls):
        if tool.isinrect(controls.mousex,controls.mousey,self.rect):
            self.text=controls.edittext(self.text)# edit text
            # Note: apparently no need to filter special characters ( \, ', ", {, }, etc )
            if len(self.text)>self.nchar: self.text=self.text[:self.nchar-1]# control max size
    def makeframe(self):
        self.sprite.make('W',self.font,self.color)# biggest character
        self.rx=self.sprite.getrx()*self.nchar# biggest text size
        self.ry=self.sprite.getry()
        self.sprite_frame.make()
        self.rect=(self.x-self.rx-self.xm,self.x+self.rx+self.xm,self.y-self.ry-self.ym,self.y+self.ry+self.ym)
    def makelegend(self,legend):# make legend (and prerender)
        self.legend=legend
        formattextkwargs=share.datamanager.getwords()
        self.legend=tool.formattext(self.legend,**formattextkwargs)# replace with book of things keywords
        self.sprite_legend.make(self.legend,share.fonts.font('smaller'),(0,0,0),bold=True)
        termx,termy=self.sprite_legend.getrxry()
        self.xl,self.yl =self.x, self.y+self.ry+termy
    def display(self):
        self.sprite.make(self.text,self.font,self.color,bold=True)# rebuild sprite every display
        self.sprite.display(self.x,self.y)
        self.sprite_frame.display(share.colors.textinput,(self.x,self.y,2*self.rx,2*self.ry))
        if self.legend: self.sprite_legend.display(self.xl,self.yl)
    def update(self,controls):
        self.display()
        self.changetext(controls)
    def finish(self):
        share.datamanager.writeword(self.key,self.text)
        share.datamanager.savewords()



####################################################################################################################
#
# text choice: similar to textinput (saves keyword) but must select between choices
# $ textchoice=draw.obj_textchoice('herogender')
# $ textchoice.addchoice('1. A guy','he',(340,360))
# $ textchoice.addchoice('2. A girl','she',(640,360))
# $ textchoice.addkey('hero_his',{'he':'his','she':'her'})
class obj_textchoice:
    def __init__(self,key):
        self.type='textchoice'
        self.key=key# key from choice that will be saved (in words.txt)
        self.setup()
    def setup(self):
        self.choices=[]
        self.ichoice=0# selected choice
        self.morekeys=[]# additional keys from choice
        self.xmargin=20
        self.ymargin=10
        self.keytodict(self.key)
    def keytodict(self,key):# write key in dictionary if not there
        if not key in share.datamanager.getwordkeys():
            share.datamanager.writeword(key,'')
    def addchoice(self,text,value,xy,fontsize='medium',bold=True,color=(0,0,0)):
        formattextkwargs=share.datamanager.getwords()
        text=tool.formattext(text,**formattextkwargs)# replace with book of things keywords
        sprite=core.obj_sprite_text()
        sprite.make(text,share.fonts.font(fontsize),color,bold=bold)
        size=sprite.getrx()*2,sprite.getry()*2
        area=( int(xy[0]-size[0]/2-self.xmargin), int(xy[0]+size[0]/2+self.xmargin),\
              int(xy[1]-size[1]/2-self.ymargin),int(xy[1]+size[1]/2+self.ymargin) )
        spriterect=core.obj_sprite_rect()
        self.choices.append( (value,sprite,spriterect,xy,size,area) )
        self.checkchoice()
    def checkchoice(self):# check current choice from possible value matches
        for c,i in enumerate(self.choices):
            value,sprite,spriterect,xy,size,area=i
            if (self.key in share.datamanager.getwordkeys()) and share.datamanager.getword(self.key)==value:
                self.ichoice=c
                break
    def changechoice(self,controls):
        if controls.mouse1 and controls.mouse1c:
            for c,i in enumerate(self.choices):
                value,sprite,spriterect,xy,size,area=i
                if tool.isinrect(controls.mousex,controls.mousey,area):
                    self.ichoice=c
                    break
    def choicetodict(self):# write key choice in words dict
        if self.choices:
            value,img,sprite,spriterect,size,area=self.choices[self.ichoice]
            share.datamanager.writeword(self.key,value)
    def addkey(self,key,analogies):# add a key affected by choice (using value analogies)
        self.keytodict(key)
        self.morekeys.append( (key,analogies) )
    def morekeystodict(self):# write addictional key choices in words dict
        for i in self.morekeys:
            key,analogies=i# 'hero_his',{'he':'his','she':'her'}
            for j in analogies.keys():
                if j==share.datamanager.getword(self.key):
                    share.datamanager.writeword(key,analogies[j])
                    break
    def display(self):
        for c,i in enumerate(self.choices):
            __,sprite,spriterect,xy,size,__=i
            sprite.display(xy[0],xy[1])
            if c==self.ichoice:
                rect=(xy[0],xy[1],size[0]+self.xmargin,size[1]+self.ymargin)
                spriterect.display(share.colors.textchoice,rect)
    def play(self,controls):
        self.display()
        self.changechoice(controls)
    def update(self,controls):
        self.play(controls)
    def finish(self):
        self.choicetodict()
        self.morekeystodict()
        share.datamanager.savewords()


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
        self.fontsize=fontsize
        self.color=color
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):
        self.x=self.xini# position
        self.y=self.yini
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.show=True# show or not (can be toggled)
        # sprite
        self.sprite=core.obj_sprite_text()# sprite
        self.replacetext(self.text)
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
    def replacetext(self,text):
        self.text=text
        formattextkwargs=share.datamanager.getwords()
        self.text=tool.formattext(self.text,**formattextkwargs)# replace with book of things keywords
        self.sprite.make(self.text,share.fonts.font(self.fontsize),self.color)
    def movetox(self,x):
        self.x=x
    def movetoy(self,y):
        self.y=y
    def movex(self,dx):
        self.x += dx
    def movey(self,dy):
        self.y += dy
    def fliph(self):# horizontal
        self.sprite.flip(True,False)
        self.fh= not self.fh
    def ifliph(self):# to inverted
        if not self.fh:
            self.sprite.flip(True,False)
            self.fh=True
    def ofliph(self):# to original
        if self.fh:
            self.sprite.flip(True,False)
            self.fh=False
    def flipv(self):# vertical
        self.fv= not self.fv
        self.sprite.flip(False,True)
    def iflipv(self):# to inverted
        if not self.fv:
            self.sprite.flip(False,True)
            self.fv=True
    def oflipv(self):# to original
        if self.fv:
            self.sprite.flip(False,True)
            self.fv=False
    def scale(self,s): # scale image by given factor s (permanent)
        self.s *= s
        self.sprite.scale(s)
    def rotate(self,r): # rotate image (permanent)
        self.r += r# (do not overdo, enlargens image with memory issues)
        self.sprite.rotate(r)
    def rotate90(self,r):# rotate image in 90 increments nonly
        self.r += int(round(r%360/90,0)*90)# (in 0,90,180,270)
        self.sprite.rotate90(r)
    def display(self):
        if self.show: self.sprite.display(self.x,self.y)
    def devtools(self):
        self.devcross.display(share.colors.devtextbox,(self.x,self.y),10)
        termx,termy=self.sprite.getrxry()
        self.devrect.display(share.colors.devtextbox,(self.x,self.y,termx*2,termy*2))
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
        self.x=self.xini# position
        self.y=self.yini
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.show=True# show or not (can be toggled)
        # sprite
        self.sprite=core.obj_sprite_image()# sprite
        self.sprite.load('book/'+self.name+'.png')
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
    def replaceimage(self,name):
        self.name=name
        self.sprite.load('book/'+name+'.png')
        # reapply historial of transformations
        self.sprite.flip(self.fh,self.fv)
        self.sprite.scale(self.s)
        self.sprite.rotate(self.r)
    def movetox(self,x):
        self.x=x
    def movetoy(self,y):
        self.y=y
    def movex(self,dx):
        self.x += dx
    def movey(self,dy):
        self.y += dy
    def fliph(self):# horizontal
        self.sprite.flip(True,False)
        self.fh= not self.fh
    def ifliph(self):# to inverted
        if not self.fh:
            self.sprite.flip(True,False)
            self.fh=True
    def ofliph(self):# to original
        if self.fh:
            self.sprite.flip(True,False)
            self.fh=False
    def flipv(self):# vertical
        self.fv= not self.fv
        self.sprite.flip(False,True)
    def iflipv(self):# to inverted
        if not self.fv:
            self.sprite.flip(False,True)
            self.fv=True
    def oflipv(self):# to original
        if self.fv:
            self.sprite.flip(False,True)
            self.fv=False
    def scale(self,s): # scale image by given factor s (permanent)
        self.s *= s
        self.sprite.scale(s)
    def rotate(self,r): # rotate image (permanent)
        self.r += r# (do not overdo, enlargens image with memory issues)
        self.sprite.rotate(r)
    def rotate90(self,r):# rotate image in 90 increments nonly
        self.r += int(round(r%360/90,0)*90)# (in 0,90,180,270)
        self.sprite.rotate90(r)
    def display(self):
        if self.show: self.sprite.display(self.x,self.y)
    def devtools(self):
        self.devcross.display(share.colors.devimage,(self.x,self.y),10)
        termx,termy=self.sprite.getrxry()
        self.devrect.display(share.colors.devimage,(self.x,self.y,termx*2,termy*2))
    def play(self,controls):# update,play,display kept for consistency and calls
        self.display()
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)


####################################################################################################################

# Animate an image on screen
# Animation=base sprite  + temporal sequence of transformations (cyclic)
class obj_animation:
    def __init__(self,name,imgname,xy,record=False,scale=1):
        self.type='animation'
        self.name=name# animation name
        self.imgname=imgname# reference image (more can be added)
        self.xini=xy[0]
        self.yini=xy[1]
        self.record=record# ability to record sequence
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):
        self.x=self.xini# animation center (changed externally)
        self.y=self.yini# animation position (changed externally)
        self.fh=False# animation flipped horizontally or not
        self.fv=False# animation flipped vertically or not
        self.r=0# rotation angle (default =0)
        self.s=1# scaling factor (default =1)
        self.show=True# show the animation or not (can be toggled on/off)
        # sprite list
        self.spritelist=[]
        self.addimage(self.imgname)
        self.rx,self.ry=self.spritelist[0].getrxry()
        # sprite
        self.sprite=core.obj_sprite_image()# the one that is played
        self.sprite.makeempty(self.rx,self.ry)
        # sequence
        self.sequence=obj_animationsequence(self,self.name,(self.xini,self.yini),self.record)
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
        self.devcrossref=core.obj_sprite_cross()
        self.devlineseq=core.obj_sprite_linesequence()
    def addimage(self,imgname):
        sprite=core.obj_sprite_image()
        sprite.load('book/'+imgname+'.png')
        self.spritelist.append(sprite)
    def replaceimage(self,imgname,index): 
        if index >=0 and index<len(self.spritelist):
            self.spritelist[index].load('book/'+imgname+'.png')
            self.spritelist[index].flip(self.fh,self.fv)
            self.spritelist[index].scale(self.s)
            self.spritelist[index].rotate(self.r)
    def movetox(self,x):
        self.x=x
    def movetoy(self,y):
        self.y=y
    def movex(self,dx):
        self.x += dx
    def movey(self,dy):
        self.y += dy
    def fliph(self):# horizontal
        self.fh= not self.fh
        for i in self.spritelist: i.flip(True,False)
    def ifliph(self):# to inverted
        if not self.fh:
            for i in self.spritelist: i.flip(True,False)
            self.fh=True
    def ofliph(self):# to original
        if self.fh:
            for i in self.spritelist: i.flip(True,False)
            self.fh=False
    def flipv(self):# vertical
        self.fv= not self.fv
        for i in self.spritelist: i.flip(False,True)
    def iflipv(self):# to inverted
        if not self.fv:
            for i in self.spritelist: i.flip(False,True)
            self.fv=True
    def oflipv(self):# to original
        if self.fv:
            for i in self.spritelist: i.flip(False,True)
            self.fv=False
    def scale(self,s):
        self.s *= s
        for i in self.spritelist: i.scale(s)
        self.rx,self.ry=self.spritelist[0].getrxry()
    def rotate90(self,r):
        r= int(round(r%360/90,0)*90)# (in 0,90,180,270)
        self.r += r
        for i in self.spritelist: i.rotate(r)
        self.rx,self.ry=self.spritelist[0].getrxry()
    def rotate(self,r):
        self.r += r
        for i in self.spritelist: i.rotate(r)
        self.rx,self.ry=self.spritelist[0].getrxry()
    def display(self):
        if self.show:
            # read sequence
            ta,xa,ya,fha,fva,ra,sa,ia=self.sequence.frame
            bscal=self.sequence.bscal
            # sprite image
            self.isprite = ia
            if ia>len(self.spritelist)-1: ia=0
            if ia<0: ia=len(self.spritelist)-1
            self.sprite.makeempty(self.rx,self.ry)
            self.sprite.blitfrom(self.spritelist[ia],0,0)
            # transformations
            self.sprite.flip(fha,fva)
            ssa=bscal**sa
            if sa != 0: self.sprite.scale(ssa)
            ra *= 1-2*int(self.fh)
            ra *= 1-2*int(self.fv)
            self.sprite.rotate(ra)
            # Display position
            xd,yd=xa*self.s,ya*self.s
            angle=self.r/180*tool.pi()
            coo,soo=tool.cos(angle),tool.sin(angle)
            xd,yd=coo*xd+soo*yd,coo*yd-soo*xd
            xd,yd=xd*(1-2*int(self.fh)),yd*(1-2*int(self.fv))
            xd,yd=xd+self.x,yd+self.y
            # display
            self.sprite.display(xd,yd)
            # devtools
            self.devxy=(xd,yd)
            self.devarea=(xd,yd, 2*self.sprite.getrx(), 2*self.sprite.getry() )
    def devtools(self):
        if self.sequence.recording:
            if self.sequence.data and len(self.sequence.data)>1:
                xylist=[]
                for i in range(len(self.sequence.data)):
                    termx=self.sequence.data[i][1]+self.xini
                    termy=self.sequence.data[i][2]+self.yini
                    xylist.append( (termx,termy) )
                self.devlineseq.display((255,0,0),xylist)
            self.devcrossref.display((0,0,255),(self.xini,self.yini),10)
        self.devcross.display(share.colors.devanimation,self.devxy,10)
        self.devrect.display(share.colors.devanimation,self.devarea)
    def play(self,controls):
        self.sequence.update(controls)
        self.display()
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)


# Animation sequence (vector of time-transformations)
class obj_animationsequence:
    def __init__(self,creator,name,xy,record):
        self.type='animationsequence'
        self.creator=creator# created by obj_animation
        self.name=name# sequence name (same as animation)
        self.xini=xy[0]# reference position (needed to track mouse)
        self.yini=xy[1]
        self.record=record# ability to record sequence (bool)
        self.setup()
    def setup(self):
        self.recording=False# record or playback mode
        self.maxlength=None# sequence max number of frames (None=unlimited)
        self.bscal=1.01# base for scaling = bscal**sa
        # sequence data
        self.data=[]
        self.length=0
        self.clearsequence()
        self.loadsequence()
    def clearsequence(self):
        self.data=[]# sequence data
        self.length=0
        self.setupframe()
    def setupframe(self):
        self.ta=0# time (0<ta<maxlength-1)
        self.xa=0# position offset
        self.ya=0
        self.fha=False# horizontal flip (boolean)
        self.fva=False# vertical
        self.ra=0# rotation angle (int, in degrees)
        self.sa=0# scaling exponent (int) for scaling = bscal**sa
        self.ia=0# index of image used (0=default, >0=next images)
        self.frame=self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia
    def update(self,controls):
        if self.record:# ability to record
            if share.devmode and controls.space and controls.spacec: self.recording= not self.recording
        if self.recording:
            self.recordsequence(controls)# record mode
        else:
            self.playbacksequence()# playback mode
    def rewindsequence(self):
        self.ta=0
    def playbacksequence(self):
        self.ta +=1
        if self.ta > len(self.data)-1: self.ta=0
        if self.data:
            self.frame=self.data[self.ta]
        else:
            self.setupframe()# backup default frame
    def recordsequence(self,controls):
        if controls.backspace and controls.backspacec: self.clearsequence()
        if controls.r and controls.rc: self.savesequence()
        self.xa,self.ya=controls.mousex-self.xini,controls.mousey-self.yini
        if controls.q and controls.qc: self.fha = not self.fha
        if controls.e and controls.ec: self.fva = not self.fva
        if controls.a: self.ra += 1
        if controls.d: self.ra -= 1
        if controls.w: self.sa += 1# (scaling is in bscal**sa)
        if controls.s: self.sa -= 1
        if controls.f and controls.fc: self.ia += 1 # change sprite
        if controls.g and controls.gc: self.ia -= 1
        if self.ia > len(self.creator.spritelist)-1: self.ia =0
        if self.ia<0: self.ia=len(self.creator.spritelist)-1
        self.frame=[self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia]
        if controls.mouse1:
            if not self.maxlength or len(self.data)<self.maxlength:
                self.data.append(self.frame)
                self.ta += 1
    def savesequence(self):
        with open('animations/'+self.name+'.txt', 'w+') as f1:
            f1.write('t,x,y,fh,fv,r,s,frame:'+'\n')# first line
            for i in range(0,len(self.data)):
                line=str(self.data[i][0])# ta
                line +=','+str(self.data[i][1])# xa
                line +=','+str(self.data[i][2])# ya
                if self.data[i][3]: # fha (boolean to 0-1)
                    line +=','+'1'
                else:
                    line +=','+'0'
                if self.data[i][4]: # fva (boolean to 0-1)
                    line +=','+'1'
                else:
                    line +=','+'0'
                line +=','+str(self.data[i][5])# ra
                line +=','+str(self.data[i][6])# sa
                line +=','+str(self.data[i][7])# ia
                line +='\n'
                f1.write(line)
    def loadsequence(self):
        self.data=[]
        if tool.ospathexists('animations/'+self.name+'.txt'):
            with open('animations/'+self.name+'.txt','r+') as f1:
                line=f1.readline()# first line skip
                while line:
                    line=f1.readline()
                    if line:
                        line = line.rstrip("\n")
                        line=line.split(",")
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
                        self.data.append(vect)
        self.length=len(self.data)


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
        self.setup()
        if scale != 1: self.scale(scale)
    def setup(self):
        self.x=self.xini# position
        self.y=self.yini
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        # elements
        self.dict={}
        self.dictx={}# relative position
        self.dicty={}
        # devtools
        self.devcross=core.obj_sprite_cross()
    def addpart(self,name,element):
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )
    def removepart(self,name):
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
    def movetox(self,x):
        self.x=x
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movetoy(self,y):
        self.y=y
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def movex(self,dx):
        self.x += dx
        for i in self.dict.keys(): self.dict[i].movetox(self.x+self.dictx[i])
    def movey(self,dy):
        self.y += dy
        for i in self.dict.keys(): self.dict[i].movetoy(self.y+self.dicty[i])
    def symh(self,name):# shift element symmetrically (horizontal)
        self.dictx[name] *= -1
        self.dict[name].movetox(self.x + self.dictx[name])
    def symv(self,name):# shift element symmetrically (vertical)
        self.dicty[name] *= -1
        self.dict[name].movetoy(self.y + self.dicty[name])
    def fliph(self):# horizontal
        self.fh=not self.fh
        for i in self.dict.keys():
            self.dict[i].fliph()
            self.symh(i)
    def ifliph(self):# to inverted
        if not self.fh:
            self.fh=True
            for i in self.dict.keys():
                self.dict[i].ifliph()
                self.symh(i)
    def ofliph(self):# to original
        if self.fh:
            self.fh=False
            for i in self.dict.keys():
                self.dict[i].ofliph()
                self.symh(i)
    def flipv(self):# vertical
        self.fv=not self.fv
        for i in self.dict.keys():
            self.dict[i].flipv()
            self.symv(i)
    def iflipv(self):# to inverted
        if not self.fv:
            self.fv=True
            for i in self.dict.keys():
                self.dict[i].iflipv()
                self.symv(i)
    def oflipv(self):# to original
        if self.fv:
            self.fv=False
            for i in self.dict.keys():
                self.dict[i].oflipv()
                self.symv(i)
    def scale(self,s):
        self.s *= s
        for i in self.dict.keys():
            self.dict[i].scale(s)
            self.dictx[i] *= s
            self.dicty[i] *= s
            self.dict[i].movetox(self.x+self.dictx[i])
            self.dict[i].movetoy(self.y+self.dicty[i])
    def rotate90(self,r):
        r=int(round(r%360/90,0)*90)# in 0,90,180,270
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
    def rotate(self,r):
        self.r += r
        for i in self.dict.keys():
            self.dict[i].rotate(r)
            xd,yd=self.dictx[i],self.dicty[i]
            angle=r/180*tool.pi()
            coo,soo=tool.cos(angle),tool.sin(angle)
            xd,yd=coo*xd+soo*yd,coo*yd-soo*xd
            self.dictx[i],self.dicty[i]=xd,yd
            self.dict[i].movetox(self.x+self.dictx[i])# update element position
            self.dict[i].movetoy(self.y+self.dicty[i])
    def devtools(self):
        self.devcross.display(share.colors.devdispgroup,(self.x,self.y),20,diagonal=True,thickness=6)
    def play(self,controls):
        for i in self.dict.values(): i.play(controls)
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)


####################################################################################################################
