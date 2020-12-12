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
        # quickdraft
        self.list.append(obj_scene_testdraftanimation(self.creator))

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
        if (controls.enter and controls.enterc): self.creator.scene=self.list[share.itest]
        if controls.tab  and controls.tabc: self.creator.scene=menu.obj_scene_titlescreen(self.creator)          
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
        if controls.esc and controls.escc: share.quitgame()
        
##########################################################
##########################################################

# Scene: quickdraft animations (do it quickly here)
class obj_scene_testdraftanimation:
    def __init__(self,creator):
        self.name='QuickDraft'
        self.creator=creator# created by scenemanager         
        self.text=['Draft One Animation here [Tab: Back]']
        #
        if False:# hero legs stand (chapter 1)
            self.animation=draw.obj_animation('herolegs_stand','herolegs_stand',(640,360))
        elif True:# hero legs walk (chapter 1)
            self.animation=draw.obj_animation('herolegs_walk','herolegs_stand',(640,360))
            self.animation.addimage('herolegs_walk')
        elif False:# hero head (chapter 1)
            self.animation=draw.obj_animation('herohead_basic','herohead',(640,360))
        elif False:# hero  strike (chapter 1)
            self.animation=draw.obj_animation('herostrike_basic','herostrike',(640,360))
            
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.update(controls)# this means animation can be edited
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)

##########################################################
##########################################################
# Text Tests

class obj_scene_testsmessage:
    def __init__(self,creator):
        self.name='Text Basics'
        self.creator=creator# created by scenemanager         
        self.text=['-----   Appendix: Developer Tests   -----   ',\
                   '\nIt was just an Appendix for tests by the Game Developer.',\
                       'If you are not the Game Developer get out of here!',\
                   '[Tab: Back]']
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)


class obj_scene_interactivetext:
    def __init__(self,creator):
        self.name='Text Dynamics and color'
        self.creator=creator# created by scenemanager         
        self.text=[
            'Interactive Text: the text returns to line with a symbol (antislash-n) \n or returns to line automatically using closest whitespace. '\
            '\n\nCode inputs with list of [text,..,(text,color),...] writing, with default or optional color. For example:',\
            ' The ', ('Hero',share.colors.red), ' was ', ('happy',share.colors.blue),'.',\
                ]
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        if controls.tab  and controls.tabc:
            self.creator.scene=obj_scene_tests(self.creator)


class obj_scene_inputtext:
    def __init__(self,creator):
        self.name='Text input and keyword'
        self.creator=creator# created by scenemanager         
        self.text=[
            'Input text on this page. Hover over the text box to input with keyboard. [Backspace] erases all.',\
            'This saves keywords in the game dictionary (words.txt) to be reused like:',\
            'Test1 name is',('{test1}',share.colors.gray),', '\
            'and Test2 name is',('{test2}',share.colors.gray),'. '\
            'Only use existing keywords in text.',\
            '[Tab:Return]',\
                ]
        self.textinput1=draw.obj_textinput('test1',20,(500,300))# input keyword, max characters, position
        self.textinput1.legend='The name of the test1'
        #
        self.textinput2=draw.obj_textinput('test2',20,(500,500))# input text, max characters, position
        self.textinput2.legend='The name of the test2'
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.textinput1.update(controls)
        self.textinput2.update(controls)
        #
        if controls.tab  and controls.tabc:
            share.words.save()# resave (entire) dictionary of words in file
            self.creator.scene=obj_scene_tests(self.creator)


class obj_scene_textbox:
    def __init__(self,creator):
        self.name='Text Box'
        self.creator=creator# created by scenemanager         
        self.text=[
            'Display text in a text box. Acts like an image, can be part of dispgroup, actor,moved, scaled, flipped.',\
            'Use WASD or arrow keys to move, flip with [q] and [e], reset with [space] [Tab:Return]',\
                ]
        #
        self.textbox=draw.obj_textbox('textbox',(340,360),color=share.colors.blue)
        #
        self.dispgroup=draw.obj_dispgroup((840,360))
        self.image1=draw.obj_image('testimage',(840,360))
        self.dispgroup.addpart("image", self.image1)
        self.textbox2=draw.obj_textbox('textbox in  dispgroup',(840,460),color=share.colors.blue)
        self.dispgroup.addpart("textbox", self.textbox2)
        self.dx=5# move rate with controls
        self.dy=5# move rate 

    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.textbox.display()
        self.dispgroup.play(controls)
        if controls.d or controls.right: self.dispgroup.movex(self.dx)
        if controls.a or controls.left: self.dispgroup.movex(-self.dx)
        if controls.w or controls.up: self.dispgroup.movey(-self.dy)
        if controls.s or controls.down: self.dispgroup.movey(self.dy)
        if controls.e and controls.ec: self.dispgroup.fliph()# tests
        if controls.q and controls.qc: self.dispgroup.flipv()# tests
        if controls.space  and controls.space: self.reset()
        #
        if controls.tab  and controls.tabc:
            share.words.save()# resave (entire) dictionary of words in file
            self.creator.scene=obj_scene_tests(self.creator)
            
#########################################################################3
# Tests Drawings

# Scene: test draw something
class obj_scene_testdrawing:
    def __init__(self,creator):
        self.name='Drawing Basics'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for a drawing [draw].Draw with [Left Mouse], Erase with [Right Mouse]',\
                   ' [Tab: Back]']
        self.drawing=draw.obj_drawing('testimage',(640,360))# new drawing
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)      
        #
        self.drawing.display()
        self.drawing.update(controls)
        if controls.tab  and controls.tabc:
            self.drawing.finish()# save drawing
            self.creator.scene=obj_scene_tests(self.creator)


# Scene: test drawing alongside image
class obj_scene_testdrawingimage:
    def __init__(self,creator):
        self.name='Drawing alongside Image'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for a drawing alongside an image. It was straightforward.',\
                   ' [Tab: Back]']
        self.image=draw.obj_image('testimage',(440,360))# image
        self.drawing=draw.obj_drawing('testimage2',(840,360))# new drawing                        
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.image.display()
        self.drawing.display()
        self.drawing.update(controls)
        if controls.tab  and controls.tabc:
            self.drawing.finish()# save drawing
            self.creator.scene=obj_scene_tests(self.creator)

# Scene: test drawing alongside animation
class obj_scene_testdrawinganimation:
    def __init__(self,creator):
        self.name='Drawing alongside animation'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for an animation alongside a drawing. The animation cannot be edited,',\
                   'so one must use -play- instead of -update- in code. [Tab: Back]']
        self.drawing=draw.obj_drawing('testimage3',(440,420))# new drawing 
        self.animation=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation                           
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.play(controls)# this means animation CANNOT be edited
        self.drawing.display()
        self.drawing.update(controls)
        if controls.tab  and controls.tabc:
            self.drawing.finish()# save drawing
            self.creator.scene=obj_scene_tests(self.creator)
            
# Scene: test several drawings at the same time
class obj_scene_testseveraldrawings:
    def __init__(self,creator):
        self.name='Drawing alongside drawing'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for several drawings on the same page.  [Tab: Back]',\
                    'Erasing with [Right Mouse] works only when the mouse is in the corresponding rectangle.']
        self.drawing1=draw.obj_drawing('testimagea',(340,420))# new drawing
        self.drawing2=draw.obj_drawing('testimageb',(940,420))# new drawing
        self.drawing1.eraseonareahover=True# only erase if mouse hovers this drawing area (is default value!)
        self.drawing2.eraseonareahover=True# only erase if mouse hovers this drawing area (is default value!)
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)      
        #
        self.drawing1.display()
        self.drawing1.update(controls)
        self.drawing2.display()
        self.drawing2.update(controls)
        if controls.tab  and controls.tabc:
            self.drawing1.finish()# save drawing
            self.drawing2.finish()# save drawing
            self.creator.scene=obj_scene_tests(self.creator)

# Scene: test several drawings at the same time
class obj_scene_testdrawingbase:
    def __init__(self,creator):
        self.name='Drawing Base from other drawing'
        self.creator=creator# created by scenemanager         
        self.text=['Test Drawing Base. Drawing 1 is the base drawing 2 [Tab: Back]. ',\
                    'Should have same dimensions, and avoid shadows on drawing 2']
        self.drawing1=draw.obj_drawing('testimagea',(340,420))# new drawing
        self.drawing2=draw.obj_drawing('testimageb',(940,420),base=self.drawing1)# new drawing
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)      
        #
        self.drawing1.display()
        self.drawing1.update(controls)
        self.drawing2.display()
        self.drawing2.update(controls)
        if controls.tab  and controls.tabc:
            self.drawing1.finish()# save drawing
            self.drawing2.finish()# save drawing
            self.creator.scene=obj_scene_tests(self.creator)

#########################################################################
# Tests Images

# Scene: test show image
class obj_scene_testimage:
    def __init__(self,creator):
        self.name='Image Basics'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test to show an image and a transformed one.',\
                   'For transformations rotation should always be applied last [Tab: Back]']
        self.image1=draw.obj_image('testimage',(440,420))# image
        self.image2=draw.obj_image('testimage',(840,420))# image
        # self.image2.rotate(45)# Do not apply transformations after a rotation! It would mess the image size and center
        self.image2.reset()# optional, reset to original
        # self.image2.movex(100)
        # self.image2.movey(50)
        self.image2.fliph()
        # self.image2.flipv()   
        self.image2.scale(0.75)
        self.image2.rotate(45)# Apply last
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.image1.display()
        self.image2.display()
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
            
#########################################################################
# Tests Animations
            
# Scene: test create/show animation
class obj_scene_testanimation:
    def __init__(self,creator):
        self.name='Animation Basics'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test to create and play an animation. Toggle Edit Mode with [Space]..',\
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
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.update(controls)# this means animation can be edited
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)

# Scene: test create/show animation
class obj_scene_testanimation2:
    def __init__(self,creator):
        self.name='Animation Test Again'
        self.creator=creator# created by scenemanager         
        self.text=['It was the same test for an animation with more space. [Tab: Back]',\
                   '\nanim position=xini(ref)+x(changed externally)+xanim(recorded)+corrections']
        self.animation=draw.obj_animation('testanimationbis','testimage',(640,360))# start animation                        
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.update(controls)# this means animation can be edited
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
 
# Scene: test move animation
class obj_scene_testmoveanimation:
    def __init__(self,creator):
        self.name='Animation test move'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test to move animation with WASD or arrow keys [Tab: Back]. ',\
                   'This changes x,y in code (avoid doing it on a page that records)']
        self.animation=draw.obj_animation('testanimationbis','testimage',(640,360))# start animation                        
        self.dx=5# move rate with controls
        self.dy=5# move rate 
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.play(controls)# this means animation cannot be edited
        if controls.d or controls.right: self.animation.movex(self.dx)
        if controls.a or controls.left: self.animation.movex(-self.dx)
        if controls.w or controls.up: self.animation.movey(-self.dy)
        if controls.s or controls.down: self.animation.movey(self.dy)
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
        

# Scene: test animation alongside image
class obj_scene_testanimationimage:
    def __init__(self,creator):
        self.name='Animation alongside Image'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for an animation alongside an image. [Space] to Toggle Edit Mode.',\
                   ' [Tab: Back]']
        self.image=draw.obj_image('testimage',(440,360))# image
        self.animation=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation                
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.image.display()
        self.animation.update(controls)# this means animation can be edited
        if controls.tab  and controls.tabc:
            self.creator.scene=obj_scene_tests(self.creator)


# Scene: test animation alongside animation
class obj_scene_testanimationanimation:
    def __init__(self,creator):
        self.name='Animation alongside Animation'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for an animation alongside an animation. Only one animation can be edited.',\
                   'Use -ntmax- in code to give it same duration as other, and record it that duration.',\
                    'Refresh page [Tab then Space] to loop both animations with correct sync.',\
                      'Use -tstart- in code to change animation time offset manually [Tab: Back]']
        self.animation2=draw.obj_animation('testanimation2','testimage2',(640,360))# start animation 
        self.animation3=draw.obj_animation('testanimation3','testimage3',(640,360))# start animation  
        self.animation3.ntmax=self.animation2.nt# animation3 has same max duration as animation2   duration                       
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation2.play(controls)# this means animation CANNOT be edited
        self.animation3.update(controls)# this means animation CAN be edited
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)


# Scene: test animation with several images
class obj_scene_testanimationseveralimages:
    def __init__(self,creator):
        self.name='Animation with several image frames'
        self.creator=creator# created by scenemanager         
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
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.animation.update(controls)# this means animation CAN be edited
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
            
#########################################################################
# Tests Group Animations

# Scene: test animation group
class obj_scene_testdispgroup:
    def __init__(self,creator):
        self.name='Display Group'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test for a group of displays. Displays could be images, animations or textboxes. ',\
                   'All the animations were played together.',\
                   'There was also an image in the group, treated similarly. [Tab: Back]']

        self.dispgroup=draw.obj_dispgroup((640,360))# create animation group (give ref position xini)
        self.animation2=draw.obj_animation('testanimation2','testimage2',(440,360))# animation xini is respect to group ref now
        self.animation3=draw.obj_animation('testanimation3','testimage3',(840,360))# animation xini is respect to group ref now      
        self.image1=draw.obj_image('testimage',(640,360))
        self.dispgroup.addpart("testanim2",self.animation2)# add animation to group
        self.dispgroup.addpart("testanim3",self.animation3)# add animation to group
        self.dispgroup.addpart("testimg1",self.image1)# add image to group
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        self.dispgroup.play(controls)# play all animations
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
        

# Scene: test animation group move
class obj_scene_testdispgroupmove:
    def __init__(self,creator):
        self.name='Display Group Move'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test to move the group of displays. Use WASD or arrow keys to move.',\
                   ' Flip with [q] and [e]. reset with [space]. Group cannot be scaled or rotated (not implemented)',\
                      'Reset with [Space]. [Tab: Back]']
        self.reset()
    def reset(self):
        self.dispgroup=draw.obj_dispgroup((640,360))# create animation group (give ref position xini)
        self.animation2=draw.obj_animation('testanimation2','testimage2',(540,360))# (place animation with respect to group)
        self.animation3=draw.obj_animation('testanimation3','testimage3',(740,360))# (place animation with respect to group)
        self.image1=draw.obj_image('testimage',(640,360))
        self.dispgroup.addpart("testanim2",self.animation2)# add animation to group
        self.dispgroup.addpart("testanim3",self.animation3)# add animation to group
        self.dispgroup.addpart("testimg1",self.image1)# add image to group
        self.dx=5# move rate with controls
        self.dy=5# move rate 
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        self.dispgroup.play(controls)# play all animations
        if controls.d or controls.right: self.dispgroup.movex(self.dx)
        if controls.a or controls.left: self.dispgroup.movex(-self.dx)
        if controls.w or controls.up: self.dispgroup.movey(-self.dy)
        if controls.s or controls.down: self.dispgroup.movey(self.dy)
        if controls.e and controls.ec: self.dispgroup.fliph()# tests
        if controls.q and controls.qc: self.dispgroup.flipv()# tests
        if controls.space  and controls.space: self.reset()
        #
        if controls.tab  and controls.tabc: self.creator.scene=obj_scene_tests(self.creator)
            
#########################################################################
# Actors Tests

# Scene: test drawing the hero
class obj_scene_testherodraw:
    def __init__(self,creator):
        self.name='Actors Draw Hero'
        self.creator=creator# created by scenemanager         
        self.text=['It was a test to draw the hero. Only head and legs is easier and more functional.',\
                   'Legs=360x200, Head=200x200, Strike=360x200, Overlap=40',\
                       '[Tab: Back] [Space: Refresh]']
        self.drawing1=draw.obj_drawing('herohead',(190,300))# new drawing  
        self.drawing2=draw.obj_drawing('herostrike',(570,300))# new drawing
        self.drawing3=draw.obj_drawing('herolegs_stand',(190,510))# new drawing 
        #
        self.image1=draw.obj_image('herohead',(840,420))
        self.image2=draw.obj_image('herostrike',(1080,520))
        self.image3=draw.obj_image('herolegs_stand',(840,580))        
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)      
        #
        for i in [self.drawing1,self.drawing2,self.drawing3]:
            i.display()
            i.update(controls)
        for i in [self.image3,self.image2,self.image1]:
            i.display()            
        if controls.tab  and controls.tabc:
            for i in [self.drawing1,self.drawing2,self.drawing3]: i.finish()
            self.creator.scene=obj_scene_tests(self.creator)
        if controls.space  and controls.space:
            for i in [self.drawing1,self.drawing2,self.drawing3]: i.finish()
            self.creator.scene=obj_scene_testherodraw(self.creator)            

class obj_scene_testworldactor:
    def __init__(self,creator):
        self.name='Actors World with simple actor'
        self.creator=creator# created by scenemanager         
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
        #
    def update(self,controls):
        share.screen.fill((255,255,255))
        share.textdisplay(self.text)
        #
        self.world.update(controls)
        if controls.tab  and controls.tabc:
            self.creator.scene=obj_scene_tests(self.creator)






####################################################################################################################



