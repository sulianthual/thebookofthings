#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# draw.py: game draws = any display object on a page in the book
#         (drawing,textinput,textchoice,textbox,image,animation,dispgroup)
#         (pagebackground,pagefps,pagenumber,pagenote,pagetext)
#         (only one not included here is the hitbox from actors)
##########################################################
##########################################################

import share
import tool
import core

####################################################################################################################
# page background

class obj_pagebackground:
    def __init__(self):
        self.type='pagebackground'
        self.sprite=core.obj_sprite_background()
        self.color=(255,255,255)
        self.make()
    def make(self):
        self.sprite.make(self.color)
    def display(self):
        self.sprite.display()
    def update(self,controls):
        self.display()


####################################################################################################################
# UI elements

# display fps
class obj_pagedisplay_fps:
    def __init__(self):
        self.type='pagefps'
        self.sprite=core.obj_sprite_text()
        self.make()
    def make(self):
        text='FPS='+str(int(share.clock.getfps()))
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))
    def display(self):
        # self.sprite.display(50,20)
        self.sprite.display(1230,20)
    def update(self,controls):
        self.make()# rebuild sprite every update
        self.display()


# display page number (obsolete)
class obj_pagedisplay_number:
    def __init__(self):
        self.type='pagenumber'
        self.sprite=core.obj_sprite_text()
        self.make()
    def make(self):
        text='Page '+str(share.ipage)
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))
    def display(self):
        # self.sprite.display(1190,680)# bottom right
        self.sprite.display(640,30)# top middle
    def update(self,controls):
        self.display()

# display recurrent page note
class obj_pagedisplay_note:
    def __init__(self,text):
        self.type='pagenote'
        self.sprite=core.obj_sprite_text()
        self.make(text)
    def make(self,text):
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0))
    def display(self):
        self.sprite.display(1140,30)
    def update(self,controls):
        self.display()

####################################################################################################################


# Main body of text on a story page
class obj_pagedisplay_text:
    def __init__(self):
        self.type='pagetext'
        self.words_prerender=[]# list of words (sprites and positions)
    def make(self,textmatrix,pos=(50,50),xmin=50,xmax=1230, linespacing=55,fontsize='medium'):
        self.words_prerender=[]
        formattextkwargs=share.datamanager.getwords()
        if textmatrix:
            self.ipos=pos# text cursor position
            for i in textmatrix:
                if type(i) is str:
                    text, color = i, (0,0,0)# input: text
                else:
                    text, color = i# input: (text,color)
                text=tool.formattext(text,**formattextkwargs)
                self.ipos=self.rebuildtext(text,self.ipos,share.fonts.font(fontsize),xmin,xmax,linespacing,color=color)
    def rebuildtext(self,text,pos,font,xmin,xmax,linespacing,color=(0,0,0)):
        wordmatrix=[row.split(' ') for row in text.splitlines()]# 2D array of words
        space_width=font.size(' ')[0]# width of a space
        space_widthnone=font.size('')[0]# width of no separation
        x,y=pos# text position (top left corner)
        if x<xmin: x==xmin
        for count,line in enumerate(wordmatrix):
            for word in line:
                word_surface=core.obj_sprite_text()# New sprite_text object for each word
                word_surface.make(word,font,color)
                word_width, word_height = 2*word_surface.getrx(),2*word_surface.getry()
                if x + word_width >= xmax:# return to line auto
                    x = xmin
                    y += linespacing
                self.words_prerender.append( (word_surface,(x+word_width/2,y+word_height/2)) )# record prerendered text
                x += word_width + space_width
            # return to line from user
            if count<len(wordmatrix)-1:
                x = xmin
                y += linespacing
            # last item of line, replace space with no-separation
            x = x - space_width + space_widthnone
        return x,y# return position for next call
    def display(self):
        for i in self.words_prerender:
            word_surface, xy=i
            word_surface.display(xy[0],xy[1])
    def update(self,controls):
        self.display()

####################################################################################################################
# Basic Shapes

# a basic rectangle on screen
class obj_rectangle:
    def __init__(self,xy,rx,ry,color=(0,0,0)):
        self.type='rectangle'
        self.x,self.y=xy
        self.rx=rx
        self.ry=ry
        self.color=color
        self.setup()
    def setup(self):
        self.spriterect=core.obj_sprite_rect()
        self.show=True# show rectangle or not
    def movetoxy(self,x,y):
        self.movetox(x)
        self.movetoy(y)
    def movetox(self,x):
        self.x=x
    def movetoy(self,y):
        self.y=y
    def movex(self,dx):
        self.x += dx
    def movey(self,dy):
        self.y += dy
    def scale(self,s): # scale image by given factor s (permanent)
        self.rx *= s
        self.ry *= s
    def rotate90(self): # rotate rectangle 90 degrees (permanent)
        self.rx,self.ry= self.ry, self.rx
    def display(self):
        if self.show: self.spriterect.display(self.color,(self.x,self.y,2*self.rx,2*self.ry))
    def play(self,controls):
        self.display()
    def update(self,controls):
        self.play(controls)





####################################################################################################################

# A drawing (image to edit interactively by the player)
# *DRAWING
class obj_drawing:
    def __init__(self,name,xy,base=None,legend=None,shadow=None,brush=None,scale=1):# start new drawing (load or new)
        self.type='drawing'
        self.name=name# drawing name
        self.x,self.y = xy
        self.base=base# basis (other drawing object)
        self.legend=legend
        self.shadow=shadow# =None (use file) or =(rx,ry) (use empty canvas)
        self.scale=scale# scale drawing area on screen
        self.brushtype=brush
        self.setup()
    def setup(self):
        # drawing tools
        self.mousedraw=obj_mousedraw()# mouse drawing tool
        self.brush=core.obj_sprite_brush()
        if not self.brushtype:# default brush type
            self.brush.makebrush(share.brushes.pen)
        else:# specify brush type
            self.brush.makebrush(self.brushtype)
        self.shadowbrush=core.obj_sprite_brush()
        self.shadowbrush.makebrush(share.brushes.shadowpen)
        # shadow (start of the drawing)
        self.sprite_shadow=core.obj_sprite_image()
        if self.shadow:
            self.sprite_shadow.makeempty(self.shadow[0],self.shadow[1])
            self.rx,self.ry=self.shadow
        else:
            self.sprite_shadow.load('shadows/'+self.name+'.png',convert=False)
            self.rx,self.ry=self.sprite_shadow.getrxry()
        # base
        if self.base:
            self.sprite_base=core.obj_sprite_image()
            self.sprite_base.makeempty(self.rx,self.ry)
            self.sprite_base.blitfrom(self.base.sprite,0,0)
        # drawing
        self.sprite=core.obj_sprite_image()
        term=self.sprite.load('book/'+self.name+'.png',failsafe=False)
        if not term: self.clear()# drawing did not load
        # frame
        self.sprite_frame=core.obj_sprite_rect()
        self.makeframe()
        # legend
        self.sprite_legend=core.obj_sprite_text()
        if self.legend: self.makelegend(self.legend)
        # devtools
        self.devcross=core.obj_sprite_cross()
    def clear(self):
        self.sprite.makeempty(self.rx,self.ry)
        self.sprite.clear()
        self.sprite.blitfrom(self.sprite_shadow,0,0)
    def draw(self,controls):
        if controls.mouse1:
            self.mousedraw(controls,controls.mouse1,controls.mouse1c,self.sprite,self.brush,self.x,self.y)
        # if controls.mouse3:# draw shadow for dev
        #     self.mousedraw(controls,controls.mouse3,controls.mouse3c,self.sprite,self.shadowbrush,self.x,self.y)
        if controls.backspace and controls.backspacec and tool.isinrect(controls.mousex,controls.mousey,self.rect):
            self.clear()
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
        self.sprite_legend.make(self.legend,share.fonts.font('medium'),share.colors.instructions,bold=True)
        termx,termy=self.sprite_legend.getrxry()
        self.xl,self.yl =self.x, self.y+self.ry+termy
    def display(self):
        if self.base: self.sprite_base.display(self.x,self.y)
        self.sprite.display(self.x,self.y)
        self.sprite_frame.display(share.colors.drawing,(self.x,self.y,2*self.rx,2*self.ry))
        if self.legend: self.sprite_legend.display(self.xl,self.yl)
    def devtools(self):
        self.devcross.display(share.colors.drawing,(self.x,self.y),10,diagonal=True,thickness=6)
    def update(self,controls):
        self.draw(controls)
        self.basedraw()
        self.display()
        if share.devmode: self.devtools()
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
    def __call__(self,controls,controlhold,controlclick,sprite,sprite_brush,x,y):
        if controlhold:# button held or just pressed
            xoff=int(x-sprite.getrx()+sprite_brush.getrx())
            yoff=int(y-sprite.getry()+sprite_brush.getry())
            sprite.blitfrom(sprite_brush,controls.mousex-xoff,controls.mousey-yoff)
            if controlclick:# button just pressed
                self.mousexr=controls.mousex# record mouse position
                self.mouseyr=controls.mousey
            else:# button held
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
        # devtools
        self.devcross=core.obj_sprite_cross()
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
    def devtools(self):
        self.devcross.display(share.colors.textinput,(self.x,self.y),10,diagonal=True,thickness=6)
    def update(self,controls):
        self.changetext(controls)
        self.display()
        if share.devmode: self.devtools()
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
    def __init__(self,key,default=None):
        self.type='textchoice'
        self.key=key# key from choice that will be saved (in words.txt)
        if default:# impose default choice
            self.setdefault(default)
        self.setup()
    def setup(self):
        self.choices=[]
        self.ichoice=0# selected choice
        self.morekeys=[]# additional keys from choice
        self.xmargin=20
        self.ymargin=10
        self.keytodict(self.key)
    def setdefault(self,default):
        share.datamanager.writeword(self.key,default)

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
    def __init__(self,text,xy,fontsize='medium',color=(0,0,0),scale=1,rotate=0):
        self.type='textbox'# object type
        self.text=text
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.fontsize=fontsize
        self.color=color
        self.setup()
        if scale != 1: self.scale(scale)
        if rotate != 0: self.rotate(rotate)
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
    def movetoxy(self,x,y):
        self.movetox(x)
        self.movetoy(y)
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
    def bfliph(self,boolflip):# boolean flip
        if boolflip:
            self.ofliph()
        else:
            self.ifliph()
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
    def bflipv(self,boolflip):# boolean flip
        if boolflip:
            self.oflipv()
        else:
            self.iflipv()
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
    def snapshot(self,filename,path='book'):# save image of textbox
        snap=core.obj_sprite_image()
        snap.makeempty(self.sprite.getrx(),self.sprite.getry())
        snap.blitfrom(self.sprite,0,0)
        snap.save(path+'/'+filename+'.png')
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
    def __init__(self,name,xy,scale=1,rotate=0,fliph=False,flipv=False,fliphv=False,show=True,path='book'):
        self.type='image'# object type
        self.name=name
        self.xini=xy[0]# xy is the CENTER of the image on screen
        self.yini=xy[1]
        self.show=show# show or not (can be toggled)
        self.path=path# folder where image is found
        self.setup()
        if scale != 1: self.scale(scale)
        if rotate !=0: self.rotate(rotate)
        if fliph: self.fliph()
        if flipv: self.flipv()
        if fliphv:
            self.fliph()
            self.flipv()
    def setup(self):#
        self.x=self.xini# position
        self.y=self.yini
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        # sprite
        self.sprite=core.obj_sprite_image()# sprite
        self.load(self.name)
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
    def load(self,name):
        self.sprite.load(self.path+'/'+name+'.png')
    def save(self,name):
        if not self.path:
            self.sprite.save(self.path+'/'+name+'.png')
    def replaceimage(self,name):
        self.name=name
        self.sprite.load(self.path+'/'+name+'.png')
        # reapply historial of transformations
        self.sprite.flip(self.fh,self.fv)
        self.sprite.scale(self.s)
        self.sprite.rotate(self.r)
    def movetoxy(self,x,y):
        self.movetox(x)
        self.movetoy(y)
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
    def bfliph(self,boolflip):# boolean flip
        if boolflip:
            self.ofliph()
        else:
            self.ifliph()
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
    def bflipv(self,boolflip):# boolean flip
        if boolflip:
            self.oflipv()
        else:
            self.iflipv()
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


# An image filler with a single color
class obj_imagefill(obj_image):
    def __init__(self,data,xy,scale=1):
        color,termx,termy=data
        super().__init__('imagefill',xy,scale=scale)
        self.sprite.makeempty(termx,termy)
        self.sprite.fill(color)
    def load(self,name):# cant load
        pass
    def save(self,name):# cant save
        pass
    def replaceimage(self,name):# cant replace
        pass


####################################################################################################################

# Quickly Place Images on Screen
# This edits an output text file which code can be copied to a page
# input types:
# - 'pen','eraser'...(only read images from folder /book)
class obj_imageplacer:
    def __init__(self,creator,*args,actor=None):
        self.type='imageplacer'# object type
        self.creator=creator# created by page
        self.imglist=[]# list of available images
        if args is not None:# args is the list of image names
            for i in args:
                self.imglist.append(i)
        self.actor=actor# format for an actor instead
        self.setup()
    def setup(self):
        self.nimglist=len(self.imglist)
        self.iimg=0# index
        # pointer image
        self.pointer=obj_image('error',(640,360))
        self.creator.addpart(self.pointer)# add to page
        self.pointer.replaceimage(self.imglist[self.iimg])
        # transformations (reapplied from base each time)
        self.s=1
        self.r=0
        self.fh=False
        self.fv=False
        # placed images on screen (in a dispgroup)
        self.dispgroup=obj_dispgroup((640,360))# dispgroup of placed images
        self.creator.addpart(self.dispgroup)
        self.iplaced=0# index for placed images
        # output code
        self.filecode='book/aaa.txt'
        self.outputmatrix=[]# output matrix of text
        # active mode
        self.activemode=True
    def retransformpointer(self):
        self.pointer.setup()# reset pointer entirely
        if self.s != 1: self.pointer.scale(self.s)
        if self.r != 0: self.pointer.rotate(self.r)
        if self.fh == True: self.pointer.fliph()
        if self.fv == True: self.pointer.flipv()
    def placefrompointer(self,controls):# place image on screen
        self.dispgroup.addpart('img_'+str(self.iplaced),\
        obj_image(self.imglist[self.iimg],(controls.mousex,controls.mousey),\
        scale=self.s,rotate=self.r,fliph=self.fh,flipv=self.fv) )
        self.iplaced += 1
        if self.actor is None:# format for adding content to page
            self.outputmatrix.append(\
            '        '\
            +'self.addpart( '\
            +'draw.obj_image(\''+str(self.imglist[self.iimg])+'\','\
            +'('+str(controls.mousex)+','+str(controls.mousey)\
            +'),scale='+str(round(self.s,2))+',rotate='+str(self.r)\
            +',fliph='+str(self.fh)+',flipv='+str(self.fv)\
            +') )'\
            )
        else:# format for adding content to actor
            self.outputmatrix.append(\
            '        '\
            +'self.'+str(self.actor)+'.addpart( '\
            +'"img'+str(self.iplaced)+'", '\
            +'draw.obj_image(\''+str(self.imglist[self.iimg])+'\','\
            +'('+str(controls.mousex)+','+str(controls.mousey)\
            +'),scale='+str(round(self.s,2))+',rotate='+str(self.r)\
            +',fliph='+str(self.fh)+',flipv='+str(self.fv)\
            +') )'\
            )
    def removefrompointer(self,controls):# remove last image from screen
        self.dispgroup.removepart('img_'+str(self.iplaced-1))
        self.outputmatrix[:-1]
        self.iplaced = max(self.iplaced-1,0)
    def finish(self):# save output code
        with open(self.filecode,'w+') as f1:
            f1.write(' '+'\n')
            for i in self.outputmatrix:
                f1.write(i+'\n')#
            f1.write(' '+'\n')
    def update(self,controls):
        self.retransform=False
        if controls.g and controls.gc:
            self.activemode=not self.activemode
        if self.activemode:
            if controls.e and controls.ec:
                self.fh=not self.fh
                self.retransform=True
            if controls.q and controls.qc:
                self.fv=not self.fv
                self.retransform=True
            if controls.a or controls.left:
                self.r += 2
                self.retransform=True
            if controls.d or controls.right:
                self.r -= 2
                self.retransform=True
            if controls.w or controls.up:
                self.s *= 1.05
                self.retransform=True
            if controls.s or controls.down:
                self.s *= 0.95
                self.retransform=True
            if controls.f and controls.fc:# change image
                self.iimg += 1
                if self.iimg>self.nimglist-1: self.iimg=0
                self.pointer.replaceimage(self.imglist[self.iimg])# replace with image from folder /book
                self.retransform=True
            if controls.backspace and controls.backspacec:# reset
                self.iimg=0# index
                self.s=1
                self.r=0
                self.fh=False
                self.fv=False
                self.retransform=True
        self.pointer.update(controls)
        if self.retransform:
            self.retransformpointer()
        self.pointer.movetoxy(controls.mousex,controls.mousey)
        if self.activemode:
            if controls.mouse1 and controls.mouse1c:
                self.placefrompointer(controls)
            if controls.mouse2 and controls.mouse2c:
                self.removefrompointer(controls)
            if controls.space and controls.spacec:
                self.finish()# save content

####################################################################################################################

# Animate an image on screen
# Animation=base sprite  + temporal sequence of transformations (cyclic)
class obj_animation:
    def __init__(self,name,imgname,xy,record=False,scale=1,imgscale=1,sync=None,path='book'):
        self.type='animation'
        self.name=name# animation name
        self.imgname=imgname# reference image (more can be added). Or can be text if textbox=True
        self.xini=xy[0]
        self.yini=xy[1]
        self.record=record# ability to record sequence
        self.sync=sync# synced animation(or None)
        if self.sync:# sync sequence length to other animation object
            self.maxlength=sync.sequence.length
        else:
            self.maxlength=None
        self.path=path# folder where images are found
        self.imgscale=imgscale# scale of ref image
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
        self.addimage(self.imgname,scale=self.imgscale,path=self.path)
        self.rx,self.ry=self.spritelist[0].getrxry()
        # sprite
        self.sprite=core.obj_sprite_image()# the one that is played
        self.sprite.makeempty(self.rx,self.ry)
        # sequence
        self.sequence=obj_animationsequence(self,self.name,(self.xini,self.yini),self.record,maxlength=self.maxlength)
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
        self.devcrossref=core.obj_sprite_cross()
        self.devlineseq=core.obj_sprite_linesequence()
        self.devxy=(self.x,self.y)
        self.devarea=(self.x,self.y, 2*self.rx, 2*self.ry )
    def addimage(self,imgname,scale=1,path='book'):
        sprite=core.obj_sprite_image()
        sprite.load(path+'/'+imgname+'.png')
        if scale != 1: sprite.scale(scale)
        self.spritelist.append(sprite)
    def replaceimage(self,imgname,index):
        if index >=0 and index<len(self.spritelist):
            self.spritelist[index].load(self.path+'/'+imgname+'.png')
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
    def bfliph(self,boolflip):# boolean flip
        if boolflip:
            self.ofliph()
        else:
            self.ifliph()
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
    def bflipv(self,boolflip):# boolean flip
        if boolflip:
            self.oflipv()
        else:
            self.iflipv()
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
    def rewind(self,frame=None):
        self.sequence.rewindsequence(ta=frame)# rewind to frame ta
    def display(self):
        if self.show:
            # read sequence
            ta,xa,ya,fha,fva,ra,sa,ia=self.sequence.frame
            bscal=self.sequence.bscal
            # sprite image
            self.isprite = ia
            if ia>len(self.spritelist)-1: ia=0
            if ia<0: ia=len(self.spritelist)-1
            termx,termy=self.spritelist[ia].getrxry()
            self.sprite.makeempty(termx,termy)
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
            angle=self.r
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
# Only recorded at 60 fps, and can only be read at 60,30 or 20 fps
class obj_animationsequence:
    def __init__(self,creator,name,xy,record,maxlength=None):
        self.type='animationsequence'
        self.creator=creator# created by obj_animation
        self.name=name# sequence name (same as animation)
        self.xini=xy[0]# reference position (needed to track mouse)
        self.yini=xy[1]
        self.record=record# ability to record sequence (bool)
        self.maxlength=maxlength# sequence max number of frames (None=unlimited)
        self.setup()
    def setup(self):
        self.recording=False# record or playback mode
        self.bscal=1.01# base for scaling = bscal**sa
        # sequence data
        self.data=[]
        self.length=0
        self.clearsequence()
        self.loadsequence(maxlength=self.maxlength)
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
        self.dddra=1# increment
        self.dddsa=1# increment
    def update(self,controls):
        if self.record:# ability to record
            if share.devmode and controls.space and controls.spacec: self.recording= not self.recording
        if self.recording:
            self.recordsequence(controls)# record mode
        else:
            self.playbacksequence()# playback mode
    def rewindsequence(self,ta=None):
        if ta==None:
            self.ta=0
        else:
            self.ta=ta
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
        self.xa,self.ya=(controls.mousex-self.xini),(controls.mousey-self.yini)
        if controls.q and controls.qc: self.fha = not self.fha
        if controls.e and controls.ec: self.fva = not self.fva
        if controls.a: self.ra += self.dddra
        if controls.d: self.ra -= self.dddra
        if controls.w: self.sa += self.dddsa# (scaling is in bscal**sa)
        if controls.s: self.sa -= self.dddsa
        # change rotation/scaling increment
        if controls.f and controls.fc: self.ia += 1 # change sprite
        if controls.g and controls.gc: self.ia -= 1
        if self.ia > len(self.creator.spritelist)-1: self.ia =0
        if self.ia<0: self.ia=len(self.creator.spritelist)-1
        self.frame=[self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia]
        if controls.mouse1:
            if not self.maxlength or len(self.data)<self.maxlength:
                self.data.append(self.frame)
                self.ta += 1
        if controls.mouse2 and not controls.mouse1:# rewind synced animation (if any)
        # to record anim2 synced to anim1, 1) hold mouse2 (freezes anim1 to anim2 current frame)
        # 2) hold mouse1 (record anim2 while playing anim1 in sync)
        # 3) optionally unhold mouse2
            if self.creator.sync:# animation is
                self.creator.sync.rewind(frame=self.ta)# adjust to this sequence framesynced
                # self.creator.sync.rewind()# rewind to start
        if controls.up and controls.upc: self.dddsa += 1
        if controls.down and controls.downc: self.dddsa = max(self.dddsa-1,1)
        if controls.right and controls.rightc: self.dddra += 1
        if controls.left and controls.leftc: self.dddra = max(self.dddra-1,1)
    def savesequence(self):
        if not share.fps==60:
            print('WARNING: Animation sequence not recorded, can only record at 60 fps')
        else:
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
    def loadsequence(self,maxlength=None):
        if share.fps==60:
            lineinc=1# read every frame (sequences are recorded at 60 fps)
        elif share.fps==30:
            lineinc=2# read 1 out of 2 frames
        elif share.fps==20:
            lineinc=3# read 1 out of 3 frames
        else:
            lineinc=None
        if not lineinc:
            print('WARNING: Animation sequence not loaded, only supports 20, 30 or 60 fps')
        else:
            self.data=[]
            term=0
            linenumber=0
            if tool.ospathexists('animations/'+self.name+'.txt'):
                with open('animations/'+self.name+'.txt','r+') as f1:
                    line=f1.readline()# first line skip
                    while line:
                        line=f1.readline()
                        if line and linenumber%lineinc==0:
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
                            term += 1
                            if maxlength and term>maxlength-1:
                                break
                        linenumber +=1
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
    def addpart(self,name,element,index=None):
        self.dict[name]=element
        self.dictx[name]= int( element.xini - self.xini )# record relative difference
        self.dicty[name]= int( element.yini - self.yini )
    def removepart(self,name):
        for i in [self.dict, self.dictx, self.dicty]: i.pop(name,None)
    # transform a part within the dispgroup
    def movexwithin(self,name,dx):# move an existing part within the dispgroup
        self.dictx[name] += dx
        self.movetox(self.x)#
    def moveywithin(self,name,dy):# move an existing part within the dispgroup
        self.dicty[name] += dy
        self.movetoy(self.y)#
    # transform the entire dispgroup
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
    def bfliph(self,boolflip):# boolean flip
        if boolflip:
            self.ofliph()
        else:
            self.ifliph()
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
    def bflipv(self,boolflip):# boolean flip
        if boolflip:
            self.oflipv()
        else:
            self.iflipv()
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
    def snapshot(self,rect,filename,path='book',edges=False):# print a snapshot of dispgroup (images only)
        if not edges:
            xsnap,ysnap,rxsnap,rysnap=rect# snapshot area x,y center on screen, radx and rady
        else:
            xmin,xmax,ymin,ymax=rect# give edges of snapshot area (xmin,xmax,ymin,ymax)
            rxsnap=int((xmax-xmin)/2)
            rysnap=int((ymax-ymin)/2)
            xsnap=xmin+rxsnap
            ysnap=ymin+rysnap
        snap=core.obj_sprite_image()# make new sprite image object
        snap.makeempty(rxsnap,rysnap)# empty with desired dimensions
        for i in self.dict.keys():# iterate dispgroup elements
            if self.dict[i].type=='image':
                # offset from comparing snapshot/image topleft corner positions on screen
                xoff=(self.dict[i].x-self.dict[i].sprite.getrx()) - (xsnap - rxsnap)
                yoff=(self.dict[i].y-self.dict[i].sprite.getry()) - (ysnap - rysnap)
                snap.blitfrom(self.dict[i].sprite,xoff,yoff)# blit image to snapshot
        snap.save(path+'/'+filename+'.png')# save snapshot (folder book by default)

    def devtools(self):
        self.devcross.display(share.colors.devdispgroup,(self.x,self.y),10,diagonal=True,thickness=6)
    def play(self,controls):
        for i in self.dict.values(): i.play(controls)
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)


####################################################################################################################
