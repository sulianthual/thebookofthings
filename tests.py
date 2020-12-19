#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Created Sept 2020
# runs with pygame 1.9.4
#
# chaptertests.py: developer tests
#
##########################################################
##########################################################

import sys
import os
import pygame
import inspect
#
import share
import draw
import utils
import actor
import menu

##########################################################
##########################################################

# Chapter Developer Tests
# *TESTS
# 
# Test Menu
class obj_scene_tests:
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.list=[]# list of modules
        self.loadtests()
        self.nrow=17# number of rows one column
    def loadtests(self):# load all tests 
        #####
        # ADD ALL TESTS FROM THIS MODULE HERE
        #


        # text tests
        self.list.append(obj_scene_testsmessage(self.creator))
        self.list.append(obj_scene_interactivetext(self.creator))
        self.list.append(obj_scene_inputtext(self.creator))           
        self.list.append(obj_scene_textbox(self.creator))       

        # drawings tests
        self.list.append(obj_scene_testdrawing(self.creator))
        self.list.append(obj_scene_testdrawingimage(self.creator))
        self.list.append(obj_scene_testdrawinganimation(self.creator))
        self.list.append(obj_scene_testseveraldrawings(self.creator))
        self.list.append(obj_scene_testdrawingbase(self.creator))
        # image test
        self.list.append(obj_scene_testimage(self.creator))        
        
        # animations tests        
        self.list.append(obj_scene_testanimation(self.creator))
        self.list.append(obj_scene_testanimation2(self.creator))
        self.list.append(obj_scene_testmoveanimation(self.creator))        
        self.list.append(obj_scene_testanimationimage(self.creator))
        self.list.append(obj_scene_testanimationanimation(self.creator))
        self.list.append(obj_scene_testanimationseveralimages(self.creator))
        # group animations tests
        self.list.append(obj_scene_testdispgroup(self.creator))
        self.list.append(obj_scene_testdispgroupmove(self.creator))
        # world and actors tests
        self.list.append(obj_scene_testherodraw(self.creator))
        self.list.append(obj_scene_testworldactor(self.creator))
        # text tests
        #
        # quickdraft (show last)
        self.list.append(obj_scene_testdraftanimation(self.creator))
        #####
        self.listlen=len(self.list)
    def selecttest(self,controls):
        if (controls.s and controls.sc) or (controls.down and controls.downc): 
            # share.itest=min(share.itest+1,self.listlen-1)
            share.itest += 1
            if share.itest == self.listlen: share.itest=0
        if (controls.w and controls.wc) or (controls.up and controls.upc): 
            # share.itest=max(share.itest-1,0)
            share.itest -= 1
            if share.itest == -1: share.itest=self.listlen-1
        if controls.tab  and controls.tabc: self.creator.scene=menu.obj_scene_titlescreen(self.creator) 
        if (controls.enter and controls.enterc): 
            self.creator.scene=self.list[share.itest]
            self.creator.scene.setup()# refresh scene
            self.creator.scene.postsetup()# refresh scene
                 
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.screen.blit(share.fonts.font50.render('-- Appendix -- Developer Tests: [Enter] to Read, [Tab] to Exit.',True,(0,0,0)),(50,30))
        
        if share.itest<self.nrow-1:
            share.screen.blit(share.fonts.font30.render('---',True,(0,0,0)),(60,130+share.itest*30))
        else:
            share.screen.blit(share.fonts.font30.render('---',True,(0,0,0)),(460,130+(share.itest-self.nrow+1)*30))
        #
        for i,test in enumerate(self.list[:self.nrow-1]):
            share.screen.blit(share.fonts.font30.render(test.name,True,(0,0,0)),(100,130+i*30))
        for i,test in enumerate(self.list[self.nrow-1:]):
            share.screen.blit(share.fonts.font30.render(test.name,True,(0,0,0)),(500,130+i*30))
        self.selecttest(controls)
        # Quit Game with Esc
        if controls.esc and controls.escc: self.creator.scene=share.titlescreen
        
##########################################################
##########################################################

# Template for obj_scene test
class obj_scene_testpage():
    def __init__(self,creator):
        self.creator=creator# created by scenemanager
        self.name='Unamed'# needs name to display on test menu
        self.text=[]# empty text
        self.setup()
        self.postsetup()
    def postsetup(self):
        share.textdisplay(self.text,rebuild=True)# rebuild text prerender 
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)          
        self.page(controls)
        if (controls.tab  and controls.tabc) or (controls.esc and controls.escc): 
            self.endpage()
            self.creator.scene=obj_scene_tests(self.creator)
    def setup(self):# fill here for each test
        pass
    def page(self,controls):# fill here for each test
        pass
    def endpage(self):# fill here for each test
        pass
        
##########################################################
##########################################################

# Scene: quickdraft animations (do it quickly here)
class obj_scene_testdraftanimation(obj_scene_testpage):
    def setup(self):
        self.name='QuickDraft Animation'       
        self.text=['Draft One Animation here [Tab: Back]']
        #
        if False:# hero legs stand (chapter 1)
            self.animation=draw.obj_animation('herolegs_stand','herolegs_stand',(640,360))
        elif False:# hero legs walk (chapter 1)
            self.animation=draw.obj_animation('herolegs_walk','herolegs_stand',(640,360))
            self.animation.addimage('herolegs_walk')
        elif False:# hero head (chapter 1)
            self.animation=draw.obj_animation('herohead_lookaround','herohead',(640,360))
        elif False:# hero  strike (chapter 1)
            self.animation=draw.obj_animation('herostrike_basic','herostrike',(640,360))
        elif True:# test
            self.animation=draw.obj_animation('testtest','herohead',(640,360))
    def page(self,controls):
        self.animation.update(controls)# this means animation can be edited


##########################################################
##########################################################
# Text Tests

class obj_scene_testsmessage(obj_scene_testpage):
    def setup(self):
        self.name='Message from the Developer'       
        self.text=['-----   Appendix: Developer Tests   -----   ',\
                   '\nThis is an appendix for tests by the Game Developer.',\
                       'If you are not the Game Developer get out of here!',\
                   '[Tab: Back]']


class obj_scene_interactivetext(obj_scene_testpage):
    def setup(self):
        self.name='Text Basics'     
        self.text=[
            'Text Basics: the text returns to line with a symbol (antislash-n) \n or returns to line automatically using closest whitespace. '\
            '\n\nCode inputs with list of [text,..,(text,color),...] writing, with default or optional color. For example:',\
            ' The ', ('Hero',share.colors.red), ' was ', ('happy',share.colors.blue),'.',\
                ]


class obj_scene_inputtext(obj_scene_testpage):
    def setup(self):
        self.name='Text input and keyword'      
        self.text=[
            'Input text on this page. Hover over the text box to input with keyboard. [Backspace] erases all.',\
            'This saves keywords in the game dictionary (words.txt) to be reused like:',\
            'Test1 name is',('{test1}',share.colors.gray),', '\
            'and Test2 name is',('{test2}',share.colors.gray),'. '\
            'Only use existing keywords in text.',\
            '[Tab:Return]',\
                ]
        self.textinput1=draw.obj_textinput('test1',20,(500,300))# input keyword, max characters, position
        self.textinput1.makelegend('The name of the test1')
        #
        self.textinput2=draw.obj_textinput('test2',20,(500,500))# input text, max characters, position
        self.textinput2.makelegend('The name of the test2')
    def page(self,controls):
        self.textinput1.update(controls)
        self.textinput2.update(controls)
    def endpage(self):
        share.words.save()# resave (entire) dictionary of words in file


class obj_scene_textbox(obj_scene_testpage):
    def setup(self):
        self.name='Text Box Basics'    
        self.text=[
            'Text Box Basics. Acts like an image. ',\
            'Can reset[space], move [Arrows], flip [q,e], scale[w,s], rotate90 [a,d]. ',\
            'Can rotate[f] but use sparingly (enlargens-memory issues) [Tab:Return]',\
                ]
        #
        self.textbox=draw.obj_textbox('textbox',(340,360),color=share.colors.blue)
        self.textbox2=draw.obj_textbox('textbox',(840,460),color=share.colors.red)
        self.dx=5# move rate with controls
        self.dy=5# move rate
    def page(self,controls):
        self.textbox.display()
        self.textbox2.play(controls)
        if controls.right: self.textbox2.movex(self.dx)
        if controls.left: self.textbox2.movex(-self.dx)
        if controls.up: self.textbox2.movey(-self.dy)
        if controls.down: self.textbox2.movey(self.dy)
        if controls.e and controls.ec: self.textbox2.fliph()# tests
        if controls.q and controls.qc: self.textbox2.flipv()# tests        
        if controls.a and controls.ac: self.textbox2.rotate90(90)
        if controls.d and controls.dc: self.textbox2.rotate90(-90)
        if controls.w and controls.wc: self.textbox2.scale(2)
        if controls.s and controls.sc: self.textbox2.scale(0.5)
        if controls.space and controls.spacec: self.textbox2.setup()
        if controls.f and controls.fc: self.textbox2.rotate(45)

            
#########################################################################3
# Tests Drawings

# Scene: test draw something
class obj_scene_testdrawing(obj_scene_testpage):
    def setup(self):
        self.name='Drawing Basics'      
        self.text=['Drawing Basics. Draw with [Left Mouse], Erase with [Right Mouse]',\
                   ' [Tab: Back]']
        self.drawing=draw.obj_drawing('testimage',(640,360))# new drawing
    def page(self,controls):
        self.drawing.display()
        self.drawing.update(controls)
    def endpage(self):
        self.drawing.finish()# save drawing



# Scene: test drawing alongside image
class obj_scene_testdrawingimage(obj_scene_testpage):
    def setup(self):
        self.name='Drawing alongside Image'      
        self.text=['Drawing alongside an image. straightforward.',\
                   ' [Tab: Back]']
        self.image=draw.obj_image('testimage',(440,360))# image
        self.drawing=draw.obj_drawing('testimage2',(840,360))# new drawing
    def page(self,controls):
        self.image.display()
        self.drawing.display()
        self.drawing.update(controls)
    def endpage(self):
        self.drawing.finish()# save drawing


# Scene: test drawing alongside animation
class obj_scene_testdrawinganimation(obj_scene_testpage):
    def setup(self):
        self.name='Drawing alongside animation'      
        self.text=['Animation alongside a drawing. The animation cannot be edited,',\
                   ' use -play- instead of -update- in code. [Tab: Back]']
        self.drawing=draw.obj_drawing('testimage3',(440,420))# new drawing 
        self.animation=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation
    def page(self,controls):
        self.animation.play(controls)# this means animation CANNOT be edited
        self.drawing.display()
        self.drawing.update(controls)
    def endpage(self):
        self.drawing.finish()# save drawing

            
# Scene: test several drawings at the same time
class obj_scene_testseveraldrawings(obj_scene_testpage):
    def setup(self):
        self.name='Drawing alongside drawing'        
        self.text=['several drawings on the same page.  [Tab: Back]',\
                    'Erasing with [Right Mouse] works only when the mouse is in the corresponding rectangle.']
        self.drawing1=draw.obj_drawing('testimagea',(340,420))# new drawing
        self.drawing2=draw.obj_drawing('testimageb',(940,420))# new drawing
        self.drawing1.eraseonareahover=True# only erase if mouse hovers this drawing area (is default value!)
        self.drawing2.eraseonareahover=True# only erase if mouse hovers this drawing area (is default value!)
    def page(self,controls):
        self.drawing1.display()
        self.drawing1.update(controls)
        self.drawing2.display()
        self.drawing2.update(controls)
    def endpage(self):
        self.drawing1.finish()# save drawing
        self.drawing2.finish()# save drawing


# Scene: test several drawings at the same time
class obj_scene_testdrawingbase(obj_scene_testpage):
    def setup(self):
        self.name='Drawing Base'      
        self.text=['Drawing 1 is the base for drawing 2 [Tab: Back]. ',\
                    'Drawing 2 must same dimensions, and no shadows (unlike here)']
        self.drawing1=draw.obj_drawing('testimagea',(340,420))# new drawing
        self.drawing2=draw.obj_drawing('testimageb',(940,420),base=self.drawing1)# new drawing
    def page(self,controls):
        self.drawing1.display()
        self.drawing1.update(controls)
        self.drawing2.display()
        self.drawing2.update(controls)
    def endpage(self):
        self.drawing1.finish()# save drawing
        self.drawing2.finish()# save drawing


#########################################################################
# Tests Images

# Scene: test show image
class obj_scene_testimage(obj_scene_testpage):
    def setup(self):
        self.name='Image Basics'      
        self.text=['Image Basics.',\
            'Can reset[space], move [Arrows], flip [q,e], scale[w,s], rotate90 [a,d]. ',\
            'Can rotate[f] but use sparingly (enlargens-memory issues) [Tab:Return]',\
            ]
        self.image1=draw.obj_image('testimage',(440,420))# image
        self.image2=draw.obj_image('testimage',(840,420))# image
        self.dx=5# move rate with controls
        self.dy=5# move rate
    def page(self,controls):
        self.image1.display()
        self.image2.play(controls)
        if controls.right: self.image2.movex(self.dx)
        if controls.left: self.image2.movex(-self.dx)
        if controls.up: self.image2.movey(-self.dy)
        if controls.down: self.image2.movey(self.dy)
        if controls.e and controls.ec: self.image2.fliph()# tests
        if controls.q and controls.qc: self.image2.flipv()# tests        
        if controls.a and controls.ac: self.image2.rotate90(90)
        if controls.d and controls.dc: self.image2.rotate90(-90)
        if controls.w and controls.wc: self.image2.scale(2)
        if controls.s and controls.sc: self.image2.scale(0.5)
        if controls.space and controls.spacec: self.image2.setup()
        if controls.f and controls.fc: self.image2.rotate(45)
            
#########################################################################
# Tests Animations
            
# Scene: test create/show animation
class obj_scene_testanimation(obj_scene_testpage):
    def setup(self):
        self.name='Animation Record'    
        self.text=['It was a test to create and play an animation. Toggle Edit Mode with [Space].',\
                    '\n-- While in Edit Mode:',\
                    '\n[BackSpace]: Erase all frames',\
                    '\n[Hold LMouse]: Append new frames',\
                    '\n[A-D]: Rotate around center',\
                    '\n[W-S]: Scale',\
                    '\n[Q-E]: Flip Horizontal/Vertical',\
                    '\n[F]: Change Image (if several)',\
                    '\n[R]: Save Animation to File (!)',\
                    '\nRed Line tracks image center for all frames.',\
                    '\nBlue cross shows animation reference position.',\
                   '\n-- Out of Edit Mode: Animation loop-plays.  [Tab: Back]']
        self.animation=draw.obj_animation('testanimation','testimage',(640,360))# start animation
    def page(self,controls):
        self.animation.update(controls)# this means animation can be edited


# Scene: test create/show animation
class obj_scene_testanimation2(obj_scene_testpage):
    def setup(self):
        self.name='Animation Permanent Changes 1/2'       
        self.text=['On top of recording, animation accepts permanent changes: move,flip, scale, rotate90. ',\
                   'rotate() is not implement (cf enlargen-memory issues) ',\
                   'Always record WITHOUT any permanent change. ',\
                   '[Tab: Back]']
        self.animation=draw.obj_animation('testanimationbis','testimage',(640,360))# start animation
    def page(self,controls):
        self.animation.update(controls)# this means animation cannot be edited
 
# Scene: test move animation
class obj_scene_testmoveanimation(obj_scene_testpage):
    def setup(self):
        self.name='Animation Permanent Changes 2/2'      
        self.text=['Apply permanent changes [Arrows] Move, [w,s] scale, [a,d] rotate90, [q,e] flip. ',\
                   'The permanent changes modify the recorded animation movements too consistently',\
                   '[Tab: Back]']
        self.animation=draw.obj_animation('testanimationbis','testimage',(640,360))# start animation                        
        self.dx=5# move rate with controls
        self.dy=5# move rate
    def page(self,controls):
        self.animation.play(controls)# this means animation cannot be edited
        if controls.right: self.animation.movex(self.dx)
        if controls.left: self.animation.movex(-self.dx)
        if controls.up: self.animation.movey(-self.dy)
        if controls.down: self.animation.movey(self.dy)
        if controls.e and controls.ec: self.animation.fliph()# tests
        if controls.q and controls.qc: self.animation.flipv()# tests        
        if controls.a and controls.ac: self.animation.rotate90(90)
        if controls.d and controls.dc: self.animation.rotate90(-90)
        if controls.w and controls.wc: self.animation.scale(2)
        if controls.s and controls.sc: self.animation.scale(0.5)
        if controls.space and controls.spacec: self.animation.setup()

        

# Scene: test animation alongside image
class obj_scene_testanimationimage(obj_scene_testpage):
    def setup(self):
        self.name='Animation alongside Image'       
        self.text=['It was a test for an animation alongside an image. [Space] to Toggle Edit Mode.',\
                   ' [Tab: Back]']
        self.image=draw.obj_image('testimage',(440,360))# image
        self.animation=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation
    def page(self,controls):
        self.image.display()
        self.animation.update(controls)# this means animation can be edited


# Scene: test animation alongside animation
class obj_scene_testanimationanimation(obj_scene_testpage):
    def setup(self):
        self.name='Animation alongside Animation'      
        self.text=['It was a test for an animation alongside an animation. Only one animation can be edited.',\
                   'Use -ntmax- in code to give it same duration as other, and record it that duration.',\
                    'Refresh page [Tab then Space] to loop both animations with correct sync.',\
                      'Use -tstart- in code to change animation time offset manually [Tab: Back]']
        self.animation2=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation 
        self.animation3=draw.obj_animation('testanimation3','testimage3',(640,360))# start animation  
        self.animation3.ntmax=self.animation2.nt# animation3 has same max duration as animation2 duration
    def page(self,controls):
        self.animation2.play(controls)# this means animation CANNOT be edited
        self.animation3.update(controls)# this means animation CAN be edited


# Scene: test animation with several images
class obj_scene_testanimationseveralimages(obj_scene_testpage):
    def setup(self):
        self.name='Animation with several image frames'       
        self.text=['It was a test for an animation using several images. Use [F] in Edit Mode to switch image.',\
                   'All additional images must be added manually to the animation in code.',\
                       '[Tab: Back]']
        self.animation=draw.obj_animation('testanimation4','testimage',(640,360))# start animation 
        self.animation.addimage('testimage2')# add image to list
        self.animation.addimage('testimage3')# add image to list
        self.animation.movex(50)# move all images by dx
        self.animation.movey(100)
        # self.animation.fliph()# flip all images horizontally
        # self.animation.flipv()# vertically
        # self.animation.scale(0.75)# scale all images
        # self.animation.rotate(45)# rotate all images (messy if scaling during animation?)
    def page(self,controls):
        self.animation.update(controls)# this means animation CAN be edited

            
#########################################################################
# Tests Group Animations

# Scene: test animation group
class obj_scene_testdispgroup(obj_scene_testpage):
    def setup(self):
        self.name='Display Group'     
        self.text=['It was a test for a group of displays. Displays could be images, animations or textboxes. ',\
                   'All the animations were played together.',\
                   'There was also an image in the group, treated similarly. [Tab: Back]']
        #
        self.dispgroup=draw.obj_dispgroup((640,360))# create animation group (give ref position xini)
        self.animation2=draw.obj_animation('testanimation2','testimage2',(440,360))# animation xini is respect to group ref now
        self.animation3=draw.obj_animation('testanimation3','testimage3',(840,360))# animation xini is respect to group ref now      
        self.image1=draw.obj_image('testimage',(640,360))
        self.dispgroup.addpart("testanim2",self.animation2)# add animation to group
        self.dispgroup.addpart("testanim3",self.animation3)# add animation to group
        self.dispgroup.addpart("testimg1",self.image1)# add image to group
    def page(self,controls):
        self.dispgroup.play(controls)# play all animations
        

# Scene: test animation group move
class obj_scene_testdispgroupmove(obj_scene_testpage):
    def setup(self):
        self.name='Display Group Transform'        
        self.text=['Display group transformed while conserving structure. These are permanent changes. [arrow keys] to move.',\
                   ' [q] and [e] to flip. [w] and [s] to 2x scale (dont repeat, degrades images).',\
                   '[a] and [d] for rotate90 (rotation not 90 not implemented: too complex).',\
                   ' reset with [space].',\
                   ' [Tab: Back]']
        self.rreset()
    def rreset(self):
        self.dispgroup=draw.obj_dispgroup((640,360))# create animation group (give ref position xini)
        self.animation2=draw.obj_animation('testanimation2','testimage2',(540,360))# (place animation with respect to group)
        self.animation3=draw.obj_animation('testanimation3','testimage3',(740,360))# (place animation with respect to group)
        self.image1=draw.obj_image('testimage',(640,360))
        self.image2=draw.obj_image('testimage2',(540,360))
        self.image3=draw.obj_image('testimage3',(740,360))
        self.textbox3=draw.obj_textbox('Trying',(740,360),color=share.colors.blue)
        #
        self.dispgroup.addpart("testimg1",self.image1)# add image to group
        # self.dispgroup.addpart("testimg2",self.image2)# add image to group
        # self.dispgroup.addpart("testimg3",self.image3)# add image to group
        self.dispgroup.addpart("testanim2",self.animation2)# add animation to group
        # self.dispgroup.addpart("testanim3",self.animation3)# add animation to group
        self.dispgroup.addpart("textbox3",self.textbox3)# add textnpx to group
        #
        self.dx=5# move rate with controls
        self.dy=5# move rate
    def page(self,controls):
        self.dispgroup.play(controls)# play all animations
        if controls.right: self.dispgroup.movex(self.dx)
        if controls.left: self.dispgroup.movex(-self.dx)
        if controls.up: self.dispgroup.movey(-self.dy)
        if controls.down: self.dispgroup.movey(self.dy)
        if controls.w and controls.wc: self.dispgroup.scale(2)
        if controls.s and controls.sc: self.dispgroup.scale(0.5)
        if controls.a and controls.ac: self.dispgroup.rotate90(90)
        if controls.d and controls.dc: self.dispgroup.rotate90(-90)
        if controls.e and controls.ec: self.dispgroup.fliph()# tests
        if controls.q and controls.qc: self.dispgroup.flipv()# tests
        if controls.space  and controls.space: self.rreset()

            
#########################################################################
# Actors Tests

# Scene: test drawing the hero
class obj_scene_testherodraw(obj_scene_testpage):
    def setup(self):
        self.name='Actors Show Hero'        
        self.text=['It was a test to show the hero. Only head and legs is easier and more functional.',\
                   'Legs=360x200, Head=200x200, Strike=360x200, Overlap=40',\
                       '[Tab: Back] [Space: Refresh]']
        self.image1=draw.obj_image('herohead',(840,420))
        self.image2=draw.obj_image('herostrike',(1080,520))
        self.image3=draw.obj_image('herolegs_stand',(840,580))
    def page(self,controls):
        for i in [self.image3,self.image2,self.image1]:
            i.display()            
          

class obj_scene_testworldactor(obj_scene_testpage):
    def setup(self):
        self.name='Actors World with simple actor'       
        self.text=['Test world with simple actor. Walk with [WASD] [Tab: Back].',\
                   'Activate Dev mode with [Ctrl] to see actors hit boxes.']
        # Build world
        self.world=actor.obj_world_v1(self)
        # Hero in world
        self.hero=actor.obj_actor_hero(self.world,(640,360))
        self.s=0.5# scaling factor
        self.image1=draw.obj_image('herolegs_stand',(640,440)) 
        self.image1.scale(self.s)
        self.hero.addpart("legs_stand",self.image1)# add shown element (image, animation or dispgroup)
    def page(self,controls):
        self.world.update(controls)







####################################################################################################################



