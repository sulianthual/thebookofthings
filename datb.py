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

# Databases

# colors database (RGB)
class obj_colors:
    def __init__(self):
        # NB: colorkey is defined in share (as global variable)
        # base colors
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
        self.purple=(128,0,128)
        self.pink=(231,84,128)
        self.darkorange=(255,140,0)
        # Colors devmode
        self.devtextbox=(233,222,100)# yellow
        self.devimage=(250,150,0)# orange
        self.devanimation=(0,220,0)# green
        self.devdispgroup=(128,0,128)# purple
        self.devactor=(0,0,220)# blue (hitbox)
        # Colors game elements
        self.background=self.white# game background
        self.text=self.black# regular text
        self.instructions=self.purple# any instruction text/element
        self.drawing=(220,0,0)# drawing
        self.input=self.red# text input (in text)
        self.textinput=(200,0,0)# text input (box)
        self.textchoice=(180,0,0)# text input box
        # Colors for story
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
        self.bunny=self.darkorange
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
         elif fontname=='big' or fontname==100:
             return self.font100
         elif fontname=='huge' or fontname==120:
             return self.font120
         else:
             return self.font50# medium font


# brushes  database (used for drawing)
class obj_brushes:
    def __init__(self):
        self.bigpen=('data/pen.png',(16,16))
        self.pen12=('data/pen.png',(12,12))
        self.pen=('data/pen.png',(8,8))
        self.pen6=('data/pen.png',(6,6))
        self.smallpen=('data/pen.png',(4,4))
        self.tinypen=('data/pen.png',(2,2))
        self.shadowpen=('data/shadowpen.png',(64,64))


####################################################################################################################

# musics database
# (musics have an indirect name in the code)
class obj_musics:
    def __init__(self):
        self.dict={}
        self.setup()
    def setup(self):
        # dictionary= tuples of filename, volume level
        #
        self.dict['error']=( 'error.mp3' , 1 )
        self.dict['test']=( 'POL-mali-maafe-short.mp3' , 0.5 )
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


# sounds database
# (sounds have an indirect name in the code)
class obj_sounds:
    def __init__(self):
        self.dict={}
        self.setup()
    def setup(self):
        # dictionary= tuples of filename, volume level
        #
        self.dict['error']=( 'error.ogg' , 1 )
        self.dict['test1']=( 'phaseJump1.ogg' , 1 )
        self.dict['test2']=( 'footstep_grass_001.ogg' , 1 )
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
            f1.write('chapter'+'\n')# highest unlocked chapter
            f1.write(str(self.chapter)+'\n')#
    def loadprogress(self):
        if tool.ospathexists(self.fileprogress):
            with open(self.fileprogress,'r+') as f1:
                line=f1.readline()# highest unlocked chapter
                line=f1.readline()
                self.chapter=int(line)
        else:
            # default progress
            self.chapter=0
            self.saveprogress()

    def updateprogress(self,chapter=None):
        if chapter:
            self.chapter=max(self.chapter,chapter)
        self.saveprogress()
    #
    def savesettings(self):
        with open(self.filesettings,'w') as f1:
                f1.write('doazerty'+'\n')#key
                f1.write(str(self.doazerty)+'\n')#value
                f1.write('donative'+'\n')#key
                f1.write(str(self.donative)+'\n')#value
                f1.write('domusic'+'\n')#key
                f1.write(str(self.domusic)+'\n')#value
                f1.write('dosound'+'\n')#key
                f1.write(str(self.dosound)+'\n')#value
                f1.write('devaccess'+'\n')#key
                f1.write(str(self.devaccess)+'\n')#value
    def loadsettings(self):
        if tool.ospathexists(self.filesettings):
            with open(self.filesettings,'r+') as f1:
                line=f1.readline()# difficulty
                line=f1.readline()
                self.doazerty=line=='True'+'\n'
                line=f1.readline()# donative
                line=f1.readline()
                self.donative=line=='True'+'\n'
                line=f1.readline()# domusic
                line=f1.readline()
                self.domusic=line=='True'+'\n'
                line=f1.readline()# dosound
                line=f1.readline()
                self.dosound=line=='True'+'\n'
                line=f1.readline()# dosound
                line=f1.readline()
                self.devaccess=line=='True'+'\n'
        else:
            # default settings
            self.doazerty=False# qwerty keyboard
            self.donative=True# 1280x720(native) or adapted resolution
            self.domusic=False# music on/off
            self.dosound=False# sound on/off
            self.devaccess=False# User has no dev access by default
            # write down default settings
            self.savesettings()
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
        self.dictcontrolnames['action']='enter/space'
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
        # hero
        if name=='happyface':
            # combine sitckhead+happyface=herohead
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('happyface',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'herohead')
            # combine herohead+stickbody = herobase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360,200,300),'herobase')
            # make herobaseangry (obsolete, used to be with angry head)
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360,200,300),'herobaseangry')
            # herohead+stickbody+zapaura=herozapped
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup2.addpart('part2',draw.obj_image('herohead',(640,200),scale=0.5) )
            dispgroup2.addpart('part3',draw.obj_image('zapaura',(640,360),path='premade') )
            dispgroup2.snapshot((640,360,200,300),'herozapped')
            # herohead+stickcrouch =herocrouch
            image1=draw.obj_image('stickcrouch',(940,360),path='premade')
            image2=draw.obj_image('herohead',(800,360),scale=0.5,rotate=90)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((940,360,300,200),'herocrouch')# 0 to 660 in height
        #
        # partner
        if name in ['happyface','partnerhair']:
            # combine stickbody+stickhead+partnerhair=partnerbasenoface
            image1=draw.obj_image('stickbody',(640,460),path='premade')
            image2=draw.obj_image('partnerhair',(640,200))
            image3=draw.obj_image('stickhead',(640,200),path='premade')# hero instead of stick head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.addpart('part3',image3)
            dispgroup1.snapshot((640,330,200,330),'partnerbasenoface')# 0 to 660 in height
            # combine stickbody+herohead+partnerhair=partnerbase
            image1=draw.obj_image('stickbody',(640,460),path='premade')
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
        #
        # villain
        if name in ['scar','angryface']:
            # save angry head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade'))
            dispgroup1.addpart('part2',draw.obj_image('angryface',(640,360)))
            dispgroup1.snapshot((640,360,200,200),'angryhead')
            # save villain head drawing
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('angryhead',(640,360)) )
            dispgroup1.addpart('part2',draw.obj_image('scar',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'villainhead')
            # save villain full body (slightly different than hero, because originally we could include partnerhair)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup2.addpart('part2',draw.obj_image('villainhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,330,200,330),'villainbase')
            # villainhead+stickshootcrouch =villainshootcrouch (beware larger if girl)
            image1=draw.obj_image('stickshootcrouch',(640,360+100),path='premade')
            image2=draw.obj_image('villainhead',(640,360),scale=0.5,fliph=True)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360+100-50,300,250),'villainshootcrouch')# 0 to 660 in height
        if name in ['scar','angryface','partnerhair']:
            # villainbase+partnerbase=villainholdspartner
            image1=draw.obj_image('villainbase',(640,360))
            image2=draw.obj_image('partnerbase',(640-70,360+80),rotate=90)
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,400,330),'villainholdspartner')

        #
        # grandmasters
        if name =='bunnyface':
            # save bunny head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360+150),scale=1.5,path='premade'))
            dispgroup1.addpart('part2',draw.obj_image('bunnyface',(640,360)))
            dispgroup1.snapshot((640,360,200,300),'bunnyhead')
        if name in ['bunnyface','bunnybody']:
            # save angry head
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('bunnybody',(640,360+65)))
            dispgroup1.addpart('part2',draw.obj_image('bunnyhead',(640,360-150),scale=0.5))
            dispgroup1.snapshot((640,295,200,235),'bunnybase')
        if name =='elderhead':
            # # save elder full body (slight offset made)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,330,200,330),'elderbase')
            # save elder full body (This is the CORRECT way, is used for some animations)
            dispgroup2=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup2.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup2.addpart('part2',draw.obj_image('elderhead',(640,200),scale=0.5) )
            dispgroup2.snapshot((640,360,200,300),'elderbase2')
        if name =='sailorface':
            # combine sitckhead+sailorface=sailorbaldhead
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('sailorface',(640,360)) )
            dispgroup1.snapshot((640,360,200,200),'sailorbaldhead')
        if name in ['sailorface','sailorhat']:
            # save sailor head
            dispgroup1=draw.obj_dispgroup((640,450))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('sailorbaldhead',(640,450),scale=1))
            dispgroup1.addpart('part2',draw.obj_image('sailorhat',(640,450-200)))
            dispgroup1.snapshot((640,325+50,250,275),'sailorhead')
            # combine herohead+stickbody = herobase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('sailorbaldhead',(640,200),scale=0.5))
            dispgroup1.addpart('part3',draw.obj_image('sailorhat',(640,200-100),scale=0.5))
            dispgroup1.snapshot((640,360-15,200,300+15),'sailorbase')
        #
        # skeletons
        if name =='skeletonhead':
            # combine skeletonhead+stickbody = skeletonbase
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
            dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            # dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
            # dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
            # dispgroup1.addpart('part6',draw.obj_image('scar',(640,200),scale=0.5) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase')
        if name in ['skeletonhead','partnerhair']:
            # skeleton with hair
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
            dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_partnerhair')
        if name in ['skeletonhead','sailorhat']:
            # skeleton with sailor hat
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
            dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
            dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
            dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
            dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_sailorhat')
        #
        # others
        if name in ['happyface','fish']:
            # combine hero+fish into: hero holding fish
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',draw.obj_image('herobase',(640,452), scale=0.7))
            dispgroup1.addpart('part2',draw.obj_image('fish',(776,486), scale=0.4,rotate=-90))
            dispgroup1.snapshot((700,452,200,260),'herobasefish')
        if name in ['scar','angryface','gun']:
            # villainbase+gun =villainbasegun (for cutscenes)
            image1=draw.obj_image('villainbase',(640,330))
            image2=draw.obj_image('gun',(640+180,330),scale=0.4)
            dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640+50,330,200+50,330),'villainbasegun')# 0 to 660 in height
        if name =='alarmclockext':
            # combine alarmclockext+alarmclockfill=alarmclock (no hour shown)
            image1=draw.obj_image('alarmclockext',(640,360))
            image2=draw.obj_image('alarmclockfill',(640,360),path='premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock')
            # combine alarmclock+alarmclockcenter8am=alarmclock8am (morning)
            image1=draw.obj_image('alarmclock',(640,360))
            image2=draw.obj_image('alarmclockcenter8am',(640,360),path='premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock8am')
            # combine alarmclock+alarmclockcenter8am=alarmclock8am (night)
            image1=draw.obj_image('alarmclock',(640,360))
            image2=draw.obj_image('alarmclockcenter12am',(640,360),path='premade')
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',image1)
            dispgroup1.addpart('part2',image2)
            dispgroup1.snapshot((640,360,200,200),'alarmclock12am')
        if name in ['happyface','cow']:
            # combine herobase+cow=heroridecow
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart('part1',draw.obj_image('herobase',(640,360-100),scale=0.5) )
            dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
            dispgroup1.snapshot((640,360+25,300,300-25),'heroridecow')
        #
        # mechs
        if name in ['scar','angryface']:
            # villainmech armature
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('angryface',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part2', draw.obj_image('scar',(640,360),scale=0.5,fliph=True) )
            dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='premade' ) )
            dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='premade') )
            dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640-200,400),path='premade') )
            dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640+200,400),path='premade') )
            dispgroup1.snapshot((640,360,300,220),'villainmecharmature')
        if name in ['scar','angryface','castle','mountain','gun','lightningbolt','cave']:
            # villainmech complete
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('villainmecharmature',(640,360)) )
            dispgroup1.addpart( 'part2', draw.obj_image('castle',(640,180),scale=0.35) )
            dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
            dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
            dispgroup1.snapshot((640,360,410,330),'villainmechbase')
        if name in ['scar','angryface','castle','mountain','gun','lightningbolt','cave']:
            # villainmech complete no face
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1a', draw.obj_image('villainmechcase',(640,360),path='premade' ) )
            dispgroup1.addpart( 'part2a', draw.obj_image('villainmech_legs1',(640,520),path='premade') )
            dispgroup1.addpart( 'part3a', draw.obj_image('villainmech_larm1',(640-200,400),path='premade') )
            dispgroup1.addpart( 'part4a', draw.obj_image('villainmech_rarm1',(640+200,400),path='premade') )
            dispgroup1.addpart( 'part2', draw.obj_image('castle',(640,180),scale=0.35) )
            dispgroup1.addpart( 'part3', draw.obj_image('mountain',(640-170,240),scale=0.4,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part4', draw.obj_image('mountain',(640+170,240),scale=0.4,rotate=45,fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('gun',(640-300,470),scale=0.3,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part6', draw.obj_image('lightningbolt',(640+300,470),scale=0.35,rotate=-45,fliph=True) )
            dispgroup1.addpart( 'part7', draw.obj_image('cave',(640-70,620),scale=0.35,fliph=True) )
            dispgroup1.addpart( 'part8', draw.obj_image('cave',(640+70,620),scale=0.35,fliph=False) )
            dispgroup1.snapshot((640,360,410,330),'villainmechbase_noface')
        #
        if name=='happyface':
            # heromech armature
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('happyface',(640,360),scale=0.5) )
            dispgroup1.addpart( 'part3', draw.obj_image('villainmechcase',(640,360),path='premade',fliph=True ) )
            dispgroup1.addpart( 'part4', draw.obj_image('villainmech_legs1',(640,520),path='premade',fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('villainmech_larm1',(640+200,400),path='premade',fliph=True) )
            dispgroup1.addpart( 'part6', draw.obj_image('villainmech_rarm1',(640-200,400),path='premade',fliph=True) )
            dispgroup1.snapshot((640,360,300,220),'heromecharmature')
        if name in ['happyface','house','bush','fish','flower','sailboat']:
            # heromech complete
            dispgroup1=draw.obj_dispgroup((640,360))
            dispgroup1.addpart( 'part1', draw.obj_image('heromecharmature',(640,360)) )
            dispgroup1.addpart( 'part2', draw.obj_image('house',(640,180),scale=0.35) )
            dispgroup1.addpart( 'part3', draw.obj_image('bush',(640-170,240),scale=0.4,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part4', draw.obj_image('bush',(640+170,240),scale=0.4,rotate=45,fliph=True) )
            dispgroup1.addpart( 'part5', draw.obj_image('fish',(640-300,470),scale=0.3,rotate=45,fliph=False) )
            dispgroup1.addpart( 'part6', draw.obj_image('flower',(640+300,470),scale=0.35,rotate=-45,flipv=True) )
            dispgroup1.addpart( 'part7', draw.obj_image('sailboat',(640-70-10,620),scale=0.25,fliph=True) )
            dispgroup1.addpart( 'part8', draw.obj_image('sailboat',(640+70+10,620),scale=0.25,fliph=False) )
            dispgroup1.addpart( 'part9', draw.obj_image('villainmech_legs1',(640,520),path='premade',fliph=True) )
            dispgroup1.addpart( 'part10', draw.obj_image('villainmech_larm1',(640+200,400),path='premade',fliph=True) )
            dispgroup1.addpart( 'part11', draw.obj_image('villainmech_rarm1',(640-200,400),path='premade',fliph=True) )
            dispgroup1.snapshot((640,360,410,330),'heromechbase')




####################################################################################################################
