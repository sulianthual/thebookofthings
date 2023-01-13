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
#
#         New: now also manages audio, music and sounds placed on a page
#
##########################################################
##########################################################

import share
import tool
import core

####################################################################################################################
# page baground
# *BACKGROUND
class obj_pagebackground:
    def __init__(self):
        self.type='pagebackground'
        self.sprite=core.obj_sprite_background()# background sprite
        self.color=(255,255,255)# default white
        self.make()
    def make(self):
        self.color=share.datamanager.getbackcolor()
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
        self.sprite.make(text,share.fonts.font('smaller'),(0,0,0),fillcolor=share.datamanager.getbackcolor())
    def display(self):
        # self.sprite.display(50,20)
        self.sprite.display(1240,20)
        # self.sprite.display(640,20)
    def update(self,controls):
        self.make()# rebuild sprite every update
        self.display()


# mouse pointer image
class obj_pagemousepointer:
    def __init__(self):
        self.type='pagemousepointer'
        self.sprite=core.obj_sprite_image()
        self.make()
    def make(self):
        if tool.ospathexists('book/mousepointer.png'):
            self.sprite.load('book/mousepointer.png')
        else:
            self.sprite.load('data/mousepointerbase.png')

    def display(self,controls):
        self.sprite.display(controls.gmx,controls.gmy)
    def update(self,controls):
        self.make()# rebuild sprite every update
        self.display(controls)

####################################################################################################################


# Main body of text on a story page
# *TEXT
class obj_pagedisplay_text:
    def __init__(self):
        self.type='pagetext'
        self.words_prerender=[]# list of words (sprites and positions)
        self.ipos=(0,0)
    def make(self,textmatrix,pos=(50,20),xmin=50,xmax=1230, linespacing=55,fontsize='medium',fillcolor=(255,255,255)):
        self.words_prerender=[]
        self.rects_prerender=[]
        formattextkwargs=share.datamanager.getwords()
        if textmatrix:
            self.ipos=pos# text cursor position
            for i in textmatrix:
                if type(i) is str:
                    text, color = i, (0,0,0)# input: text
                else:
                    text, color = i# input: (text,color)
                text=tool.formattext(text,**formattextkwargs)
                self.ipos=self.rebuildtext(text,self.ipos,share.fonts.font(fontsize),xmin,xmax,linespacing,color=color,fillcolor=fillcolor)
    def rebuildtext(self,text,pos,font,xmin,xmax,linespacing,color=(0,0,0),fillcolor=(255,255,255)):
        wordmatrix=[row.split(' ') for row in text.splitlines()]# 2D array of words
        space_width=font.size(' ')[0]# width of a space
        space_widthnone=font.size('')[0]# width of no separation
        x,y=pos# text position (top left corner)
        if x<xmin: x==xmin
        for count,line in enumerate(wordmatrix):
            for word in line:
                word_surface=core.obj_sprite_text()# New sprite_text object for each word
                # word_surface.make(word,font,color,fillcolor)# not rendering properly as pygame sprite, omit
                word_surface.make(word,font,color)
                word_width, word_height = 2*word_surface.getrx(),2*word_surface.getry()
                if x + word_width >= xmax:# return to line auto
                    x = xmin
                    y += linespacing
                # background rectangle from fillcolor (cleaner than fillcolor in pygame sprite)
                if False:# experimental, add a surface rect for EACH WORD (crashes sometimes)
                    word_fillrect=core.obj_sprite_image()
                    tempo=word_width+20
                    if x+tempo>=xmax:
                        tempo=word_width+xmax-x
                    elif x-tempo<=xmin:
                        tempo=word_width+x-xmin
                    word_fillrect.makeempty(tempo/2,word_height/2)
                    word_fillrect.fill( fillcolor )
                    self.rects_prerender.append( (word_fillrect,(x+word_width/2,y+word_height/2)) )
                # word
                self.words_prerender.append( (word_surface,(x+word_width/2,y+word_height/2)) )# record prerendered text

                x += word_width + space_width
            # return to line from user
            if count<len(wordmatrix)-1:
                x = xmin
                y += linespacing
            # last item of line, replace space with no-separation
            x = x - space_width + space_widthnone
        return x,y# return position for next call
    def getposition(self):# return last known text position
        return self.ipos
    def display(self):
        for i in self.rects_prerender:
            word_fillrect, xy=i
            word_fillrect.display(xy[0],xy[1])
        for i in self.words_prerender:
            word_surface, xy=i
            word_surface.display(xy[0],xy[1])
    def update(self,controls):
        self.display()

####################################################################################################################
# Basic Shapes

# a basic rectangle on screen
# *RECTANGLE
class obj_rectangle:
    def __init__(self,xy,rx,ry,color=(0,0,0)):
        self.type='rectangle'
        self.xini=xy[0]# xy is the CENTER of the rectangle on screen
        self.yini=xy[1]
        self.rx=rx
        self.ry=ry
        self.color=color
        self.setup()
    def setup(self):
        self.x=self.xini# position
        self.y=self.yini
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


# writes headers for pages in the file aaa.txt
# (useful to write long chapters)
# *HEADERMAKER
class obj_headermaker:
    def __init__(self,header,pagemin,pagemax):
        self.type='headermaker'# object type
        self.header=header
        self.pagemin=max(pagemin,1)# must be >0
        self.pagemax=max(pagemax,self.pagemin)# must be >0
        self.setup()
    def setup(self):
        self.filecode='book/aaa.txt'
        self.makeheadercode()
    def makeheadercode(self):
        with open(self.filecode,'w+') as f1:
            for i in range(self.pagemin,self.pagemax):
                f1.write(' '+'\n')
                f1.write('class obj_scene_'+self.header+'p'+str(i)+'(page.obj_chapterpage):'+'\n')
                f1.write('    def prevpage(self):'+'\n')
                f1.write('        share.scenemanager.switchscene(obj_scene_'+self.header+'p'+str(i-1)+'())'+'\n')
                if i<self.pagemax-1:
                    f1.write('    def nextpage(self):'+'\n')
                    f1.write('        share.scenemanager.switchscene(obj_scene_'+self.header+'p'+str(i+1)+'())'+'\n')
                else:
                    f1.write('    # def nextpage(self):'+'\n')
                    f1.write('    #     share.scenemanager.switchscene(obj_scene_'+self.header+'p'+str(i+1)+'())'+'\n')

                f1.write(' '+'\n')





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
        self.mousexr=0
        self.mouseyr=0
        # self.mousedraw=obj_mousedraw()# mouse drawing tool
        # brush
        self.brush=core.obj_sprite_brush()
        if not self.brushtype:# default brush type
            self.brush.makebrush(share.brushes.pen)
        else:# specify brush type
            self.brush.makebrush(self.brushtype)
        # brush tip (useful for visibility e.g. if drawing black on black)
        self.sprite_brushtip=core.obj_sprite_image()
        self.sprite_brushtip.load('data/mousepointerdraw.png')
        # shadow (start of the drawing)
        self.sprite_shadow=core.obj_sprite_image()
        if self.shadow:
            self.sprite_shadow.makeempty(self.shadow[0],self.shadow[1])
            self.rx,self.ry=self.shadow
        else:
            self.sprite_shadow.load('data/shadows/'+self.name+'.png',convert=False)
            self.rx,self.ry=self.sprite_shadow.getrxry()
        # base
        if self.base:
            self.sprite_base=core.obj_sprite_image()
            self.sprite_base.makeempty(self.rx,self.ry)
            self.sprite_base.blitfrom(self.base.sprite,0,0)
        # drawing first layer
        self.sprite=core.obj_sprite_image()
        term=self.sprite.load('book/'+self.name+'.png',failsafe=False)
        if not term: self.clear()# drawing did not load
        # drawing layers
        self.layers=[]# list of layers (each one is a sprite)
        self.layers.append(self.sprite)
        # frame
        self.sprite_frame=core.obj_sprite_rect()
        self.makeframe()
        # legend
        self.sprite_legend=core.obj_sprite_text()
        if self.legend: self.makelegend(self.legend)
        # devtools
        self.devcross=core.obj_sprite_cross()
        # audio
        self.sounddrawstart=obj_sound('drawstart')
        self.sounddrawerase=obj_sound('drawerase')
        # firstframe issues
        self.updatedfirstframe=False# first frame was updated (needed for drawing click upon page transitions)
        self.isdrawing=False# is drawing now
        #
    def clear(self):# clear self.sprite=first layer
        self.sprite.makeempty(self.rx,self.ry)
        self.sprite.clear()
        self.sprite.blitfrom(self.sprite_shadow,0,0)
    def draw(self,controls):
        self.mousedraw(controls)# new internal function
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
        # self.sprite.display(self.x,self.y)
        for i in self.layers:
            i.display(self.x,self.y)
        self.sprite_frame.display(share.colors.drawing,(self.x,self.y,2*self.rx,2*self.ry))
        if self.legend: self.sprite_legend.display(self.xl,self.yl)
    def displaybrush(self,controls):
        # display the brush where the mouse is (optional, kind of ugly)
        if tool.isinrect(controls.gmx,controls.gmy,self.rect):
            self.sprite_brushtip.display(controls.gmx,controls.gmy)
    def devtools(self):
        self.devcross.display(share.colors.drawing,(self.x,self.y),10,diagonal=True,thickness=6)
    def update(self,controls):
        self.draw(controls)
        self.basedraw()
        self.display()
        self.displaybrush(controls)
        if share.devmode: self.devtools()
        if not self.updatedfirstframe:
            self.updatedfirstframe=True
    def finish(self):
        # merge layers to sprite
        for i in self.layers:
            self.sprite.blitfrom(i,0,0)# back
        # manage if base
        if self.base:
            # replace background color in base
            self.sprite_base.blitfrom(self.sprite,0,0)# to base
            self.sprite.clear()
            self.sprite.blitfrom(self.sprite_base,0,0)# back
        self.sprite.save('book/'+self.name+'.png')
        # call the snapshot manager to redraw any related image
        share.snapshotmanager.remake(self.name)
        #
        self.sounddrawstart.finish()
        self.sounddrawerase.finish()
    def mousedraw(self,controls):
        if not self.isdrawing:
            if controls.gm1 and controls.gm1c and self.updatedfirstframe:
                self.isdrawing=True
        else:
            if not controls.gm1:
                self.isdrawing=False

        # if self.updatedfirstframe and controls.gm1 and tool.isinrect(controls.gmx,controls.gmy,self.rect):
        if self.isdrawing and tool.isinrect(controls.gmx,controls.gmy,self.rect):
            sprite=self.layers[-1]# last sprite from layers
            xoff=int(self.x-sprite.getrx()+self.brush.getrx())
            yoff=int(self.y-sprite.getry()+self.brush.getry())
            if controls.gm1c:
                # play sound
                # self.sounddrawstart.play()
                self.sounddrawstart.play(loop=True)
                # add new layer
                newsprite=core.obj_sprite_image()
                newsprite.makeempty(sprite.getrx(),sprite.getry())
                newsprite.clear()
                self.layers.append(newsprite)
                # draw
                newsprite.blitfrom(self.brush,controls.gmx-xoff,controls.gmy-yoff)
            else:
                # draw line between current and last mouse position (each pixel)
                dx=controls.gmx-self.mousexr
                dy=controls.gmy-self.mouseyr
                dist=max(abs(dx),abs(dy))
                for i in range(dist):
                    xi = int( self.mousexr + float(i)/dist*dx)
                    yi = int( self.mouseyr + float(i)/dist*dy)
                    sprite.blitfrom(self.brush,xi-xoff,yi-yoff)
                # draw
                sprite.blitfrom(self.brush,controls.gmx-xoff,controls.gmy-yoff)
        else:
            self.sounddrawstart.stop()
            if controls.gm2 and controls.gm2c and tool.isinrect(controls.gmx,controls.gmy,self.rect):
                # play sound
                self.sounddrawerase.play()
                # remove last layer (except if first layer)
                if len(self.layers)>1:
                    del self.layers[-1]
                else:
                    self.clear()# erase self.sprite=first layer
        # always record current mouse position as old
        self.mousexr=controls.gmx
        self.mouseyr=controls.gmy


####################################################################################################################

# A text input
# *TEXTINPUT
class obj_textinput:
    def __init__(self,key,nchar,xy,color=(0,0,0),legend=None,default=None,empty='...'):
        self.type='textinput'
        self.key=key# key from textinput that will be saved
        self.nchar=nchar# max number of characters
        self.x,self.y = xy# position
        self.color=share.colors.text# text color
        self.colorbox=share.colors.textinput# output box
        self.colorshow=self.color# text color to show
        self.legend=legend
        self.empty=empty# default empty text (if nothing written)
        if default:# impose default choice (overrides empty)
            self.setdefault(default)
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
        # audio
        self.soundkeyboard=obj_sound('textinputkeyboard')
        self.soundedit=obj_sound('textinputedit')
        self.soundnoedit=obj_sound('textinputdone')
        # editmode
        self.editmode=False# in edit mode or not
        #
    def setdefault(self,default):
        share.datamanager.writeword(self.key,default)
    def texttodict(self):# text to/from dictionary
        if self.key in share.datamanager.getwordkeys():
            self.text=share.datamanager.getword(self.key)
        else:# create key with empty text
            share.datamanager.writeword(self.key,'')
            # self.text=''
            self.text=self.empty
    def changetext(self,controls):
        # edit mode
        if self.editmode:
            self.text=controls.edittext(self.text)# edit text
            if controls.iskeydown() and not controls.enterc:
                self.soundkeyboard.play()
            # Note: apparently no need to filter special characters ( \, ', ", {, }, etc )
            if len(self.text)>self.nchar: self.text=self.text[:self.nchar-1]# control max size
        # toggle edit mode (put AFTER edit mode functions)
        if not self.editmode:
            if tool.isinrect(controls.gmx,controls.gmy,self.rect):
                if (controls.gm1 and controls.gm1c) or (controls.enter and controls.enterc):# flip to edit mode
                    self.editmode = True
                    self.colorshow=self.colorbox# same as box
                    self.soundedit.play()
                    if self.text==self.empty:
                        self.text=''
        else:
            if (controls.gm1 and controls.gm1c) or (controls.enter and controls.enterc):# flip to non-edit mode
                self.editmode=False
                self.soundnoedit.play()
                self.colorshow=self.color
                if self.text=='':# like setempty
                    self.text=self.empty
            elif not tool.isinrect(controls.gmx,controls.gmy,self.rect):# to non-edit mode but no sound
                self.editmode=False
                self.colorshow=self.color
                if self.text=='':# like setempty
                    self.text=self.empty
    def makeframe(self):
        self.sprite.make('W',self.font,self.colorshow)# biggest character
        self.rx=self.sprite.getrx()*self.nchar# biggest text size
        self.ry=self.sprite.getry()
        self.sprite_frame.make()
        self.rect=(self.x-self.rx-self.xm,self.x+self.rx+self.xm,self.y-self.ry-self.ym,self.y+self.ry+self.ym)
    def makelegend(self,legend):# make legend (and prerender)
        self.legend=legend
        formattextkwargs=share.datamanager.getwords()
        self.legend=tool.formattext(self.legend,**formattextkwargs)# replace with book of things keywords
        self.sprite_legend.make(self.legend,share.fonts.font('smaller'),share.colors.instructions,bold=True)
        termx,termy=self.sprite_legend.getrxry()
        self.xl,self.yl =self.x, self.y+self.ry+termy
    def display(self):
        self.sprite.make(self.text,self.font,self.colorshow,bold=True)# rebuild sprite every display
        self.sprite.display(self.x,self.y)
        self.sprite_frame.display(self.colorbox,(self.x,self.y,2*self.rx,2*self.ry))
        if self.legend: self.sprite_legend.display(self.xl,self.yl)
    def devtools(self):
        self.devcross.display(self.colorbox,(self.x,self.y),10,diagonal=True,thickness=6)
    def update(self,controls):
        self.changetext(controls)
        self.display()
        if share.devmode: self.devtools()
    def finish(self):
        if self.text=='':# no empty words
            self.text=self.empty
        share.datamanager.writeword(self.key,self.text)# write down text to dictionary
        share.datamanager.savewords()



####################################################################################################################
#
# text choice: similar to textinput (saves keyword) but must select between choices
# *TEXTCHOICE
# $ textchoice=draw.obj_textchoice('herogender')
# $ textchoice.addchoice('1. A guy','he',(340,360))
# $ textchoice.addchoice('2. A girl','she',(640,360))
# $ textchoice.addkey('hero_his',{'he':'his','she':'her'})
class obj_textchoice:
    def __init__(self,key,default=None,suggested=''):
        self.type='textchoice'
        self.key=key# key from choice that will be saved (in words.txt)
        if default:# impose a default choice each time
            self.setdefault(default)
        self.suggested=suggested# suggest a choice if none already exist
        self.setup()
    def setup(self):
        self.choices=[]
        self.ichoice=0# selected choice
        self.morekeys=[]# additional keys from choice
        self.xmargin=20
        self.ymargin=10
        self.keytodict(self.key)
        # audio
        self.soundgo=obj_sound('textchoicego')
        #
    def setdefault(self,default):
        share.datamanager.writeword(self.key,default)
    def keytodict(self,key):# write key in dictionary if not there
        if not key in share.datamanager.getwordkeys():
            share.datamanager.writeword(key,self.suggested)# write the suggested outcome
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
        if controls.gm1 and controls.gm1c:
            for c,i in enumerate(self.choices):
                value,sprite,spriterect,xy,size,area=i
                if tool.isinrect(controls.gmx,controls.gmy,area):
                    self.soundgo.play()
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
# *TEXTBOX
# acts like an image (can be moved/scaled, part of a animgroup)
class obj_textbox:
    def __init__(self,text,xy,fontsize='medium',color=(0,0,0),scale=1,rotate=0,\
    xleft=False,xright=False,ytop=False,fillcolor=None,hover=False,hovercolor=(220,0,220),blinking=None):
        self.type='textbox'# object type
        self.text=text
        self.xini=xy[0]# initial position
        self.yini=xy[1]
        self.fontsize=fontsize
        self.color=color
        self.xleft=xleft# x (from xy) defines left of frame instead of center
        self.xright=xright# x (from xy) defines right of frame instead of center
        self.ytop=ytop# y (from xy) defines top of frame instead of center
        self.fillcolor=fillcolor# color for textbox background
        self.trackinghover=hover# track if hovered or not (and change color accordingly)
        self.nohovercolor=color# color when not hovered
        self.hovercolor=hovercolor# color when hovered (if tracked, default = dark purple)
        self.blinking=blinking# blinking time (in frames), If None, then no textbox blinking
        self.setup()
        if scale != 1: self.scale(scale)
        if rotate != 0: self.rotate(rotate)
    def setup(self):
        self.x=self.xini# position
        self.y=self.yini
        self.xoffset=0# offset from xleft,xright
        self.yoffset=0# offset from ytop
        self.fh=False# is flipped horizontally
        self.fv=False# is flipped vertically
        self.s=1# scaling factor
        self.r=0# rotation angle (deg)
        self.show=True# show or not (can be toggled)
        # sprite
        self.sprite=core.obj_sprite_text()# sprite
        self.replacetext(self.text)
        self.rx=self.sprite.getrx()# dimensions
        self.ry=self.sprite.getry()
        # hover
        self.hovered=False# is it being hovered
        # blinking
        if self.blinking is not None:
            self.blinkingtimer=tool.obj_timer(self.blinking)
            self.blinkingtimer.start()
            self.blinkingshow=True# staet on/off during blinking
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
    def makeoffsets(self):
        if self.xleft:
            self.xoffset=self.rx
        elif self.xright:
            self.xoffset=-self.rx
        if self.ytop:
            self.yoffset=self.ry
    def replacetext(self,text):
        self.text=text
        formattextkwargs=share.datamanager.getwords()
        self.text=tool.formattext(self.text,**formattextkwargs)# replace with book of things keywords
        self.sprite.make(self.text,share.fonts.font(self.fontsize),self.color,fillcolor=self.fillcolor)
        self.newscaleadapt()
    def newscaleadapt(self):# recompute anything affected by change of scale
        self.rx=self.sprite.getrx()
        self.ry=self.sprite.getry()
        self.makeoffsets()
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
        self.newscaleadapt()
    def rotate(self,r): # rotate image (permanent)
        self.r += r# (do not overdo, enlargens image with memory issues)
        self.sprite.rotate(r)
        self.newscaleadapt()
    def rotate90(self,r):# rotate image in 90 increments nonly
        self.r += int(round(r%360/90,0)*90)# (in 0,90,180,270)
        self.sprite.rotate90(r)
        self.newscaleadapt()
    def snapshot(self,filename,path='book'):# save image of textbox
        snap=core.obj_sprite_image()
        snap.makeempty(self.sprite.getrx(),self.sprite.getry())
        snap.blitfrom(self.sprite,0,0)
        snap.save(path+'/'+filename+'.png')
    def display(self):
        if self.show:
            if self.blinking:
                if self.blinkingshow:
                    self.sprite.display(self.x+self.xoffset,self.y+self.yoffset)
            else:
                self.sprite.display(self.x+self.xoffset,self.y+self.yoffset)

    def devtools(self):
        self.devcross.display(share.colors.devtextbox,(self.x+self.xoffset,self.y+self.yoffset),10)
        termx,termy=self.sprite.getrxry()
        self.devrect.display(share.colors.devtextbox,(self.x+self.xoffset,self.y+self.yoffset,termx*2,termy*2))
    def play(self,controls):# same as display, but renamed for consitency with play() for animations, dispgroups
        self.display()
        if share.devmode: self.devtools()# dev tools
    def ishovered(self,controls):# check is textbox is being hovered by mouse
        rect=(self.x+self.xoffset-self.rx, self.x+self.xoffset+self.rx, self.y+self.yoffset-self.ry, self.y+self.yoffset+self.ry)
        return tool.isinrect(controls.gmx,controls.gmy,rect )
    def isclicked(self,controls):# check is textbox is being clicked
        return controls.gm1 and controls.gm1c and self.ishovered(controls)
    def isholdclicked(self,controls):# check is textbox is being hold clicked
        return controls.gm1 and self.ishovered(controls)
    def trackhover(self,controls):
        if self.trackinghover:
            if self.ishovered(controls):
                if not self.hovered:# flip to hovered
                    self.hovered=True
                    self.color=self.hovercolor
                    self.replacetext(self.text)
            else:
                if self.hovered:# flip to non hovered
                    self.hovered=False
                    self.color=self.nohovercolor
                    self.replacetext(self.text)
    def updateblinking(self):
        if self.blinking:
            self.blinkingtimer.update()
            if self.blinkingtimer.ring or self.blinkingtimer.off:
                self.blinkingshow=not self.blinkingshow
                self.blinkingtimer.start()

    def update(self,controls):
        self.play(controls)
        self.updateblinking()
        self.trackhover(controls)


####################################################################################################################

# A simple image (from the book folder) to display at a given location
#*IMAGE
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
    def replaceimage(self,name,path=None):
        self.name=name
        if path is not None:
            self.path=path
        self.sprite.load(self.path+'/'+name+'.png')
        self.retransform()
    def reload(self,name):# reload image and apply all existing transformations
        self.sprite.load(self.path+'/'+name+'.png')
        self.retransform()
    def retransform(self):# reapply historial of transformations
        if not self.fh or not self.fv:
            self.sprite.flip(self.fh,self.fv)
        if self.s!=1:
            self.sprite.scale(self.s)
        if self.r!=0:
            self.sprite.rotate(self.r)
    def replacecolor(self,color,newcolor,treshold=(5,5,5)):
        self.sprite.replacecolor(color,newcolor,treshold=treshold)
    def xytoxyini(self):# reinitialize initial coordinates to current ones
        self.xini=self.x# (useful if adding existing images to a dispgroup)
        self.yini=self.y
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
    def scaleto(self,s):# NOT FULLPROOF TESTED
        self.s=s
        self.sprite.scaleto(s)
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
# *IMAGEPLACER
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
        obj_image(self.imglist[self.iimg],(controls.gmx,controls.gmy),\
        scale=self.s,rotate=self.r,fliph=self.fh,flipv=self.fv) )
        self.iplaced += 1
        if self.actor is None:# format for adding content to page
            self.outputmatrix.append(\
            '        '\
            +'self.addpart( '\
            +'draw.obj_image(\''+str(self.imglist[self.iimg])+'\','\
            +'('+str(controls.gmx)+','+str(controls.gmy)\
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
            +'('+str(controls.gmx)+','+str(controls.gmy)\
            +'),scale='+str(round(self.s,2))+',rotate='+str(self.r)\
            +',fliph='+str(self.fh)+',flipv='+str(self.fv)\
            +') )'\
            )
    def removefrompointer(self,controls):# remove last image from screen
        self.dispgroup.removepart('img_'+str(self.iplaced-1))
        self.outputmatrix=self.outputmatrix[:-1]
        self.iplaced = max(self.iplaced-1,0)
    def removeall(self,controls):
        for i in range(self.iplaced):
            self.removefrompointer(controls)
    def finish(self):# save output code (file and print on screen)
        with open(self.filecode,'w+') as f1:
            f1.write(' '+'\n')
            print('###')
            print(' '+'#')
            for i in self.outputmatrix:
                f1.write(i+'\n')#
                print(i)
            f1.write(' '+'\n')
            print(' '+'#')
    def update(self,controls):
        if share.devaccess:
            self.retransform=False
            if controls.t and controls.tc:
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
                if controls.g and controls.gc:# reset
                    self.iimg=0# index
                    self.pointer.replaceimage(self.imglist[self.iimg])
                    self.s=1
                    self.r=0
                    self.fh=False
                    self.fv=False
                    self.retransform=True
                    self.removeall(controls)
            self.pointer.update(controls)
            if self.retransform:
                self.retransformpointer()
            self.pointer.movetoxy(controls.gmx,controls.gmy)
            if self.activemode:
                if controls.gm1 and controls.gm1c:
                    self.placefrompointer(controls)
                if controls.gm2 and controls.gm2c:
                    self.removefrompointer(controls)
                if controls.r and controls.rc:
                    self.finish()# save content

####################################################################################################################

# Animate an image on screen
# *ANIMATION
# Animation=base sprite  + temporal sequence of transformations (cyclic)
class obj_animation:
    def __init__(self,name,imgname,xy,record=False,scale=1,imgscale=1,imgfliph=False,imgflipv=False, sync=None,path='book'):
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
        self.imgfliph=imgfliph# fliph of ref image
        self.imgflipv=imgflipv# flipv of ref image
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
        self.paused=False# if paused, always show the same frame
        # sprite list
        self.spritelist=[]
        self.addimage(self.imgname,scale=self.imgscale,fliph=self.imgfliph,flipv=self.imgflipv,path=self.path)
        self.rx,self.ry=self.spritelist[0].getrxry()
        # sprite
        self.sprite=core.obj_sprite_image()# the one that is played
        self.sprite.makeempty(self.rx,self.ry)
        # sequence
        self.sequence=obj_animationsequence(self,self.name,(self.xini,self.yini),self.record,maxlength=self.maxlength)
        # sounds
        self.sounddict={}# sounds by names
        self.sounddict_frames={}# corresponding frames where played
        self.sounddict_islist={}# frames are a list or integer
        self.soundonloop=True# sound on this animation loop (alternates between True and False)
        self.nsilentloops=0# how many silent loops for a non silent one (1 or 2 is good)
        self.isilentloops=0# counter for silent loops
        # devtools
        self.devcross=core.obj_sprite_cross()
        self.devrect=core.obj_sprite_rect()
        self.devcrossref=core.obj_sprite_cross()
        self.devlineseq=core.obj_sprite_linesequence()
        self.devxy=(self.x,self.y)# used in minigames to track image center (fishing), not just for dev
        self.devarea=(self.x,self.y, 2*self.rx, 2*self.ry )
    def addimage(self,imgname,scale=1,fliph=False,flipv=False,path='book'):
        sprite=core.obj_sprite_image()
        sprite.load(path+'/'+imgname+'.png')
        if scale != 1: sprite.scale(scale)
        if fliph: sprite.fliph()
        if flipv: sprite.flipv()
        self.spritelist.append(sprite)
    def replaceimage(self,imgname,index):
        if index >=0 and index<len(self.spritelist):
            self.spritelist[index].load(self.path+'/'+imgname+'.png')
            self.spritelist[index].flip(self.fh,self.fv)
            self.spritelist[index].scale(self.s)
            self.spritelist[index].rotate(self.r)
    def addsound(self,soundname,framelist,skip=None):# add a sound (give name and framelist=[0,10] frames at which is played)
        self.sounddict[soundname]=obj_sound(soundname)
        self.sounddict_frames[soundname]=framelist
        self.sounddict_islist[soundname]=isinstance(framelist, list)# is list, else assumed integer
        if skip:
            self.nsilentloops=skip# how manu times loop is silent (affects all all other sounds too)
    def removesound(self,soundname):
        self.sounddict.pop(soundname, None)
        self.sounddict_frames.pop(soundname, None)
        self.sounddict_islist.pop(soundname, None)
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
        self.soundonloop=True# reset sound on loops
        self.isilentloops=0
        self.unpause()
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
            self.devxy=(xd,yd)# this is actually used in some minigames
            self.devarea=(xd,yd, 2*self.sprite.getrx(), 2*self.sprite.getry() )
            # play sounds
            if self.nsilentloops>0:
                if ta==0:# new loop
                    if self.soundonloop:# played last loop
                        self.soundonloop=False
                        self.isilentloops=0# reset counter
                    else:
                        self.isilentloops +=1# increment counter
                        if self.isilentloops >= self.nsilentloops:
                            self.soundonloop=True
            else:# no silent loops at all
                self.soundonloop=True
            if self.soundonloop:
                for i in self.sounddict_frames.keys():
                    if self.sounddict_islist[i]:# list of frames
                        if ta in self.sounddict_frames[i]:
                            self.sounddict[i].play()
                    else:# single frame
                        if ta ==self.sounddict_frames[i]:
                            self.sounddict[i].play()
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
    def pause(self):
        self.paused=True
    def unpause(self):
        self.paused=False
    def play(self,controls):
        if not self.paused:
            self.sequence.update(controls)# if paused, do not advance sequence
        self.display()
        if share.devmode: self.devtools()
    def update(self,controls):
        self.play(controls)
    def finish(self):# upon page exit
        for i in self.sounddict.keys():
            self.sounddict[i].finish()# stop all sounds associated to animation

# Animation sequence (vector of time-transformations)
# *SEQUENCE
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
        self.length=0# animation sequence length
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
            if share.devmode and controls.t and controls.tc: self.recording= not self.recording
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
        if controls.g and controls.gc: self.clearsequence()
        if controls.r and controls.rc: self.savesequence()
        self.xa,self.ya=(controls.gmx-self.xini),(controls.gmy-self.yini)
        if controls.q and controls.qc: self.fha = not self.fha
        if controls.e and controls.ec: self.fva = not self.fva
        if controls.a: self.ra += self.dddra
        if controls.d: self.ra -= self.dddra
        if controls.w: self.sa += self.dddsa# (scaling is in bscal**sa)
        if controls.s: self.sa -= self.dddsa
        # change rotation/scaling increment
        if controls.f and controls.fc: self.ia += 1 # change sprite
        if self.ia > len(self.creator.spritelist)-1: self.ia =0
        if self.ia<0: self.ia=len(self.creator.spritelist)-1
        self.frame=[self.ta,self.xa,self.ya,self.fha,self.fva,self.ra,self.sa,self.ia]
        if controls.gm1:
            if not self.maxlength or len(self.data)<self.maxlength:
                self.data.append(self.frame)
                self.ta += 1
        if controls.gm2 and not controls.gm1:# rewind synced animation (if any)
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
            with open('data/animations/'+self.name+'.txt', 'w+') as f1:
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
            if tool.ospathexists('data/animations/'+self.name+'.txt'):
                with open('data/animations/'+self.name+'.txt','r+') as f1:
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
# *DISPGROUP
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

    def finish(self):# upon page exit
        for i in self.dict.keys():
            if self.dict[i].type=='animation':
                self.dict[i].finish()# stop all animations



####################################################################################################################
# Audio


# A music placed in a game page
# *MUSIC
# Notes:
# - if a page has no new music, the old one keeps playing.
# - music is changed on first update (instead of at init and setup, because page could be preloaded)
#
class obj_music:
    def __init__(self,name,fadeout=False):# start new drawing (load or new)
        self.type='music'
        self.name=name# music name
        self.fadeout=fadeout# fadeout previous music or not
        self.setup()
    def setup(self):
        self.changed=False
    def update(self,controls):
        if not self.changed:
            share.musicplayer.change(self.name)
            self.changed=True



# A sound placed in a game page
# *SOUND
class obj_sound:
    def __init__(self,name):
        self.type='sound'
        self.name=name# sound name
        self.setup()
    def setup(self):
        mastervol=share.soundplayer.getmastervolume()
        self.soundsprite=core.obj_soundsprite(self.name,mastervol)# associated sound sprite
        self.playing=False
    def play(self,loop=False):
        self.soundsprite.play(loop)
        self.playing=True
    def stop(self):
        if self.playing:
            self.soundsprite.stop()
            self.playing=False
            # print('stop='+self.name)
    def reset_volume(self):# reset sound sprite volume (to mastervolume*soundfilevolume )
        self.soundsprite.reset_volume()
    def update(self,controls):
        pass
    def finish(self):
        self.stop()# stop upon quiting page
        # print('stopped='+self.name)

# Place sounds alongside an animation with developper tools (arrows etc...)
# writes code output in file book/aaa.txt
# *SOUNDPLACER
class obj_soundplacer:
    def __init__(self,animation,*args):
        self.type='soundplacer'
        self.animation=animation# associated animation (must be on page)
        self.maxsounds=7# max number of sounds (for arrows+q,e,f)
        self.soundnames=[]
        if args is not None:# args is the list of soundnames
            for c,i in enumerate(args):
                if c<=self.maxsounds-1:
                    self.soundnames.append(i)
        self.setup()
    def setup(self):
        self.soundlist=[]
        self.soundexists=[False] * self.maxsounds# if sound exists
        self.soundrecords=[ [] for _ in range(self.maxsounds) ]# list of frames where sound placed
        for c,i in enumerate(self.soundnames):
            self.soundlist.append(obj_sound(i))
            self.soundexists[c]=True
        # output code
        self.filecode='book/aaa.txt'
        # toggle record sounds
        self.recordingsounds=True# default on
        #
    def triggersounds(self,controls,index):
        # play sounds with controls (wasd)
        if index==0:
            return controls.a and controls.ac
        elif index==1:
            return controls.w and controls.wc
        elif index==2:
            return controls.d and controls.dc
        elif index==3:
            return controls.s and controls.sc
        elif index==4:
            return controls.q and controls.qc
        elif index==5:
            return controls.e and controls.ec
        elif index==6:
            return controls.f and controls.fc
        else:
            return False
    def quickreplay(self):# quick replay as animation replays
        ta=self.getanimationframe()
        for i in range(self.maxsounds):
            if self.soundexists[i]:
                if ta in self.soundrecords[i]:
                    self.soundlist[i].play()
    def update(self,controls):
        if share.devaccess:
            # toggle record mode
            if controls.t and controls.tc:
                self.recordingsounds= not self.recordingsounds
            # rewind animation (rmouse)
            if controls.gm2:
                self.animation.rewind(frame=1)# to frame=1 because can put first heard sound there
            # play sounds with controls (arrows)
            for i in range(self.maxsounds):
                if self.soundexists[i] and self.triggersounds(controls,i):
                    if self.recordingsounds:
                        self.soundrecords[i].append(self.getanimationframe())
                    else:
                        self.soundlist[i].play()
            # quick replay (outside of rewind animation)
            if not controls.gm2:
                self.quickreplay()
            # clear sequences
            if controls.g and controls.gc:
                self.soundrecords=[ [] for _ in range(self.maxsounds) ]# list of frames where sound placed
            # output code
            if controls.r and controls.rc:
                self.outputcode()
    def outputcode(self):# output in aaa.txt and also on screen
        with open(self.filecode,'w+') as f1:
            f1.write(' '+'\n')
            print('###')
            print('animation lenght='+str(self.animation.sequence.length))
            print('        '+'#')
            for i in range(self.maxsounds):
                if self.soundexists[i] and len(self.soundrecords[i])>0:
                    f1.write('        '+'animation1.addsound( "'+self.soundnames[i]+'", '+str(self.soundrecords[i])+' )'+'\n')
                    print('        '+'animation1.addsound( "'+self.soundnames[i]+'", '+str(self.soundrecords[i])+' )')
            f1.write(' '+'\n')
            print('        '+'#')
        # also print on screen (faster)
    def getanimationframe(self):
        return self.animation.sequence.ta




####################################################################################################################





















#
