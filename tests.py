#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# tests.py: developer tests
#
##########################################################
##########################################################

import pygame
#
import share
import draw
import utils
import page
import actor
import world
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
        # message
        self.list.append(obj_scene_testmessage(self.creator))       
        self.list.append(obj_scene_testdevnotes(self.creator))
        self.list.append(obj_scene_testdevmodeinfo(self.creator))
        # page tests
        self.list.append(obj_scene_testpagefunctions(self.creator))
        # text tests
        self.list.append(obj_scene_interactivetext(self.creator))
        self.list.append(obj_scene_textinput(self.creator))     
        self.list.append(obj_scene_textchoice(self.creator))              
        self.list.append(obj_scene_textbox(self.creator))       
        # drawings tests
        self.list.append(obj_scene_testdrawing(self.creator))
        self.list.append(obj_scene_testdrawingbase(self.creator))
        # image test
        self.list.append(obj_scene_testimage(self.creator))        
        # animations tests        
        self.list.append(obj_scene_testanimation(self.creator))    
        self.list.append(obj_scene_testanimationanimation(self.creator))
        self.list.append(obj_scene_testanimationplayback(self.creator)) 
        # group animations tests
        self.list.append(obj_scene_testdispgroup(self.creator))
        # world and actors tests
        self.list.append(obj_scene_testworld(self.creator))
        self.list.append(obj_scene_testworldgrandactor(self.creator))
        self.list.append(obj_scene_testrigidbody(self.creator))
        
        # quickdraft 
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
            self.creator.scene.__init__(self.creator)# reset scene
                 
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


# Template for test page = page with slightly modified functionalities
class obj_testpage(page.obj_page):
    def __init__(self,creator):
        self.name='Unamed'# needs name to display on test menu
        super().__init__(creator)
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}
    def postsetup(self):
        super().postsetup()
        share.pagenotedisplay('[Tab: Back]',xy=(1180,5),rebuild=True)
    def callprevpage(self,controls):# no browsing
        pass
    def callnextpage(self,controls):# no browsing
        pass
    def callexitpage(self,controls):# back to test menu
        if (controls.tab  and controls.tabc) or (controls.esc and controls.escc):
            self.preendpage() 
            self.endpage()
            self.creator.scene=obj_scene_tests(self.creator)
    def prevpage(self):# no browsing
        pass
    def nextpage(self):# no browsing
        pass

        
#########################################################################
#########################################################################
# All Tests Here


class obj_scene_testmessage(obj_testpage):
    def setup(self):
        self.name='Message from the Developer'       
        self.text=['Message from the Developer: ',\
                   '\n\nThis is an appendix for tests by the Game Developer. ',\
                   'If you are not the Game Developer get out of here!',\
                   ]
        self.textkeys={}# defaut text formatting


class obj_scene_testdevnotes(obj_testpage):
    def setup(self):
        self.name='Developper Notes'      
        self.text=[
            'Developper Notes:',\
            ('\n\nFile Structure: ',share.colors.red),\
            'main=execute program. ',\
            'share=store global variables. ',\
            'utils=basic functions (link external libraries there like math,os...). ',\
            'pyg=same as utils but for all pygame fonctions. ',\
            'page=elements that build a page in the book. ',\
            'draw=draws that can be displayed on a page. ',\
            '(drawing, textinput, textchoice, textbox, image, animation, dispgroup). ',\
            'world=worlds that can be displayed on a page (and their rules). ',\
            'actor=actors that can be added to worlds. ',\
            'menu=main menus pages. ',\
            'ch0,ch1,ch2...=book chapters pages. ',\
            'tests=developper tests menu and pages. ',\
                   ]

        

class obj_scene_testdevmodeinfo(obj_testpage):
    def setup(self):
        self.name='Developper Mode'       
        self.text=['Developper Mode (devmode): ',\
                   'Toggle devmode with [CTRL]. ',\
                   'While in devmode additional information is displayed on screen, like centers and edges. ',\
                   'They are color coded like this: ',\
                   ('textbox',share.colors.devtextbox),', ',\
                   ('image',share.colors.devimage),', ',\
                   ('animation',share.colors.devanimation),', ',\
                   ('dispgroup',share.colors.devdispgroup),', ',\
                   ('grand actor (hitbox)',share.colors.devactor),'. However ',\
                   ('drawing',share.colors.drawing),', ',\
                   ('textinput',share.colors.textinput),', ',\
                   ('textchoice',share.colors.textchoice),\
                   ' are not affected. ',\
                   'You can also print mouse position in terminal with [Middle Mouse]. ',\
                   ]
        self.addpart( draw.obj_textinput('test1',20,(260,300),legend='textinput') )
        self.addpart( draw.obj_drawing('testimage1',(260,500),legend='drawing') )
        self.addpart( draw.obj_textbox('textbox',(1140,400)) )
        self.addpart( draw.obj_image('testimage1',(1140,600)) )
        self.addpart( draw.obj_animation('testanimation1','testimage1',(940,360)) )
        ww=world.obj_world(self)
        self.addpart(ww)
        test=actor.obj_grandactor(ww,(640,360))
        test.addpart("image", draw.obj_image('testimage2',(640,360)) )



# Scene: page basics
class obj_scene_testpagefunctions(obj_testpage):
    def setup(self):
        self.name='Page Basics'        
        self.text=['Pages Basics: Pages have default functionalities (see obj_page). ',\
                   'addpart(element) adds element to list of managed elements. ',\
                   'Managed elements can be: ',\
                   'drawing, textinput, textchoice,textbox, image, animation, dispgroup, world. ',\
                   'Managed elements are updated in order they were added. ',\
                   'They are finished on endpage if necessary (drawings,textinput). ',\
                   ' Elements can alternatively be managed manually. ',\
                   ]
        # managed elements can be: drawing,textinput,textbox,image,animation,dispgroup,world
        # element must have matching self.type to be managed by obj_page
        self.addpart(draw.obj_textbox('Managed elements here',(340,260),color=share.colors.red))
        self.addpart(draw.obj_drawing('testimage1',(340,520)))
        self.textbox=draw.obj_textbox('Non Managed elements here',(940,260),color=share.colors.blue)
        self.drawing=draw.obj_drawing('testimage2',(940,520))# new drawing
    def page(self,controls):
        self.textbox.update(controls)# non-managed elements must be updated here
        self.drawing.update(controls)
    def endpage(self):
        self.drawing.finish()# non-managed elements must be finished here (textinput and drawings...)
        
        
class obj_scene_interactivetext(obj_testpage):
    def setup(self):
        self.name='Text Basics'     
        self.text=['Text Basics: self.text on page is displayed with automatic return to line (or with antislash-n). ',\
                   'It can have colors like : '\
                    ' The ', ('Hero',share.colors.red), ' was ', ('happy',share.colors.blue),'. ',\
                    '\n\nself.textkeys can be used for tuning text properties (like on this page). ',\
                    ' For example, the regular chapter pages and the test pages have different fontsizes. ',\
                   ]
        # self.textkeys={}# default for pages
        self.textkeys={'pos':(50,50),'xmin':50,'xmax':1230,'linespacing':55,'fontsize':'medium'}# same as ={}
        # self.textkeys={'fontsize':'small','linespacing': 45}# modification for test pages (obj_testpage)
            

class obj_scene_textinput(obj_testpage):
    def setup(self):
        self.name='Text input'      
        self.text=[
            'textinput: Hover over the text box to input with keyboard. [Backspace] erases all.',\
            'This saves keywords in the game dictionary (words.txt) to be reused like:',\
            'Test1 name is',('{test1}',share.colors.gray),', '\
            'and Test2 name is',('{test2}',share.colors.gray),' '\
            '(refresh page to see those changes). ',\
            'Only use keywords that already exist, or formatting will return error. ',\
            'Special characters can be included in inputs (no issues found). ',\
                   ]
        self.addpart( draw.obj_textinput('test1',20,(640,300),legend='name of test1') )
        self.addpart( draw.obj_textinput('test2',20,(640,500),legend='name of test2') )


class obj_scene_textchoice(obj_testpage):
    def setup(self):
        self.name='Text Choice'      
        self.text=[
            'textchoice: Hover with [Mouse] and click with [Left Mouse] to select among choices. ',\
            'The current choice is the circled one. ',\
            'This saves keywords (in words.txt) similar to textinput. ',\
            'Refresh this page to see changes: \nThe test was a:',('{test_he}',share.colors.red),'. ',\
            '\nA textchoice can have additional keys: ',\
            'a choice for the base key determines the choices of the additional keys using analogies. ',\
            'The test gender was: ',('{test_his}',share.colors.red),' choice. ',\
            ]
        self.addpart( draw.obj_textbox("The test gender was:",(200,360)) )
        textchoice=draw.obj_textchoice('test_he')
        textchoice.addchoice('1. A guy','he',(440,360))
        textchoice.addchoice('2. A girl','she',(740,360))
        textchoice.addchoice('3. A thing','it',(1040,360))
        textchoice.addkey('test_his',{'he':'his','she':'her','it':'its'})# additional key and analogies
        self.addpart( textchoice )
    def page(self,controls):
        pass
        # print(share.words.dict['test_he'])# can access key value directly
        

class obj_scene_textbox(obj_testpage):
    def setup(self):
        self.name='Textbox Basics'    
        self.text=[
            'Textbox Basics: Placed anywhere, can customize font and color. ',\
            'Acts like an image: Can reset[space], move [Arrows], flip [q,e], scale[w,s], rotate90 [a,d]. ',\
            'Can rotate[f] but use sparingly (enlargens-memory issues). ',\
                   ]
        self.addpart(draw.obj_textbox('textbox',(340,360),color=share.colors.blue))#customize font and color
        self.addpart(draw.obj_textbox('smaller',(340,460),color=share.colors.blue, fontsize='tiny'))
        self.addpart(draw.obj_textbox('large',(340,560),color=share.colors.blue, fontsize='big'))
        self.textbox=draw.obj_textbox('textbox:move me',(840,460),color=share.colors.red)
        self.dx,self.dy=5,5
    def page(self,controls):
        self.textbox.update(controls)
        if controls.right: self.textbox.movex(self.dx)
        if controls.left: self.textbox.movex(-self.dx)
        if controls.up: self.textbox.movey(-self.dy)
        if controls.down: self.textbox.movey(self.dy)
        if controls.e and controls.ec: self.textbox.fliph()# tests
        if controls.q and controls.qc: self.textbox.flipv()# tests        
        if controls.a and controls.ac: self.textbox.rotate90(90)
        if controls.d and controls.dc: self.textbox.rotate90(-90)
        if controls.w and controls.wc: self.textbox.scale(2)
        if controls.s and controls.sc: self.textbox.scale(0.5)
        if controls.space and controls.spacec: self.textbox.setup()
        if controls.f and controls.fc: self.textbox.rotate(45)
        
        
# Scene: test draw something
class obj_scene_testdrawing(obj_testpage):
    def setup(self):
        self.name='Drawing Basics'      
        self.text=['Drawing Basics: Draw with [Left Mouse], Erase with [Right Mouse] ',\
                   '(only when the mouse is in drawing area). ',\
                   'It has optionally a legend and no borders. ',\
                   'A drawing needs a background of same name in folder ./shadows. ',\
                   'It is saved in folder ./drawings. ',\
                   'If replacing the shadow erase the drawing as well (or new drawing may glitch). ',\
                   ]
        self.addpart( draw.obj_drawing('testimage1',(640,360),legend='draw me',borders=(True,False,True,True)) )


# Scene: test several drawings at the same time
class obj_scene_testdrawingbase(obj_testpage):
    def setup(self):
        self.name='Drawing Base'      
        self.text=['Drawing Base: A drawing can be the base for other drawing ',\
                   '(of same dimensions). The other drawing should better have no shadows.',\
                   'Small glitches happen when coming back to existing drawings with base: in that case just erase and restart. ',\
                   ]
        drawing=draw.obj_drawing('testimage1',(340,420),legend='base')
        self.addpart(drawing )
        self.addpart( draw.obj_drawing('testimage2',(940,420),base=drawing,legend='drawing with base'))


# Scene: test show image
class obj_scene_testimage(obj_testpage):
    def setup(self):
        self.name='Image Basics'      
        self.text=['Image Basics: ',\
            'Test transformations here like move [Arrows], flip [q,e], scale [w,s], rotate90 [a,d], reset [space]. ',\
            'Can rotate [f] but use sparingly: it enlargens image each time leading to memory issues. ',\
                   ]
        self.addpart( draw.obj_image('testimage1',(440,420), scale=0.5) )# (can also scale at creation)
        self.image=draw.obj_image('testimage2',(840,420))
        self.dx=5# move rate with controls
        self.dy=5# move rate
    def page(self,controls):
        self.image.update(controls)
        if controls.right: self.image.movex(self.dx)
        if controls.left: self.image.movex(-self.dx)
        if controls.up: self.image.movey(-self.dy)
        if controls.down: self.image.movey(self.dy)
        if controls.e and controls.ec: self.image.fliph()# tests
        if controls.q and controls.qc: self.image.flipv()# tests        
        if controls.a and controls.ac: self.image.rotate90(90)
        if controls.d and controls.dc: self.image.rotate90(-90)
        if controls.w and controls.wc: self.image.scale(2)
        if controls.s and controls.sc: self.image.scale(0.5)
        if controls.space and controls.spacec: self.image.setup()
        if controls.f and controls.fc: self.image.rotate(45)
            
#########################################################################
# Tests Animations
            
# Scene: test create/show animation
class obj_scene_testanimation(obj_testpage):
    def setup(self):
        self.name='Animation Basics'    
        self.text=['Animation Basics: Animation has two modes, Record and Playback. Toggle Mode with [Space]. ',\
                   '\n(You must be in Dev Mode to do so, which is Toggled by [CTRL]). ',\
                    '\n-- While in Record Mode:',\
                    '\nRed Line tracks image center for all frames.',\
                    '\nBlue cross shows animation reference position.',\
                    '\n[BackSpace]: Erase all frames',\
                    '\n[Hold LMouse]: Append new frames',\
                    '\n[A-D]: Rotate around center',\
                    '\n[W-S]: Scale',\
                    '\n[Q-E]: Flip Horizontal/Vertical',\
                    '\n[F]: Change Image (if several exist)',\
                    '\n[R]: Save Animation to File (!)',\
                   '\n-- While in Playback Mode: Animation loop-plays.',\
                   ]
        animation=draw.obj_animation('testanimation1','testimage1',(640,360),record=True) 
        animation.addimage('testimage2')
        animation.addimage('testimage3')
        self.addpart(animation)


# Scene: test animation alongside animation
class obj_scene_testanimationanimation(obj_testpage):
    def setup(self):
        self.name='Animation alongside'      
        self.text=['Animation alongside: An animation can be alongside anything. ',\
                   'But if animation is alongside drawing it should not be editable. ',\
                   'If two animations are alongside only one should be editable. ',\
                   'To ensure both animations have same duration: ',\
                   'set max duration (ntmax=nt) and record for max duration ',\
                   '(then return to this page to see both animations in sync). ',\
                   'Can also set tstart=animation start offset in code',\
                   ]
        animation1=draw.obj_animation('testanimation1','testimage1',(340,360))# cannot edit
        animation2=draw.obj_animation('testanimation2','testimage2',(940,360),record=True)# can edit
        animation2.ntmax=animation1.nt# set same length
        self.addpart(animation1)
        self.addpart(animation2)


# Scene: test create/show animation
class obj_scene_testanimationplayback(obj_testpage):
    def setup(self):
        self.name='Animation Playback'       
        self.text=['Animation Playback: ',\
                   'During playback, animation accepts permanent changes: move,flip, scale, rotate90. ',\
                   'rotate() is not implemented (cf enlargen-memory issues). ',\
                   'Always record animation WITHOUT any permanent changes. ',\
                   'Test permanent changes here: [Arrows] Move, [w,s] scale, [a,d] rotate90, [q,e] flip. ',\
                   'The permanent changes modify animation movements too (with almost no errors)',\
                   ]
        self.animation=draw.obj_animation('testanimation1','testimage1',(640,360))                    
        self.dx,self.dy=5,5
    def page(self,controls):
        self.animation.update(controls)# manual update
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
            

# Scene: test animation group move
class obj_scene_testdispgroup(obj_testpage):
    def setup(self):
        self.name='Display group'        
        self.text=['Display Group (or dispgroup): A group of elements that can be transformed while conserving its structure. ',\
                   'accepted elements are: textbox, image, animation. ',\
                   'Test here applying permanent changes to the dispgroup: [arrow keys] to move. ',\
                   '[q] and [e] to flip. [w] and [s] to 2x scale (dont repeat, it degrades images). ',\
                   '[a] and [d] for rotate90. Reset this page with [space]. ',\
                   'rotate() is not implemented for dispgroup. ',\
                   ]
        self.dispgroup=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup.addpart( "key_element1", draw.obj_image('testimage1',(440,360)) )# add image
        self.dispgroup.addpart( "key_element2", draw.obj_textbox('Move this',(640,360)) )# add textbox
        self.dispgroup.addpart( "key_element3", draw.obj_animation('testanimation2','testimage2',(840,360)) )# add animation
        # Note: each element of dispgroup must have an unique key
        self.dx,self.dy=5,5
    def page(self,controls):
        self.dispgroup.update(controls)
        if controls.right: self.dispgroup.movex(self.dx)
        if controls.left: self.dispgroup.movex(-self.dx)
        if controls.up: self.dispgroup.movey(-self.dy)
        if controls.down: self.dispgroup.movey(self.dy)
        if controls.w and controls.wc: self.dispgroup.scale(2)
        if controls.s and controls.sc: self.dispgroup.scale(0.5)
        if controls.a and controls.ac: self.dispgroup.rotate90(90)
        if controls.d and controls.dc: self.dispgroup.rotate90(-90)
        if controls.e and controls.ec: self.dispgroup.fliph()
        if controls.q and controls.qc: self.dispgroup.flipv()
        if controls.space  and controls.space: self.setup()
          

class obj_scene_testworld(obj_testpage):
    def setup(self):
        self.name='World Basics'       
        self.text=['World Basics: ',\
                   'A World has actors in it as well as rules that manage interaction between actors. ',\
                   'The world checks all rules, and the rules may check and modify actors (but the actors dont check on rules). ',\
                   'Here the world has an actor=hero, an actor=boundaries, and a rule=collision between the two ',\
                   '(that pushes back the hero). ',\
                   '\nThere are several types of actors: simple actors (obj_actor), grand actors (obj_grandactor), ',\
                   'rigidbody actors (obj_rbodyactor),etc. One can make new actors as childs from the templates ',\
                   'but be careful with the init, setup, birth sequence (e.g. edit preferentially the setup). ',\
                   ]
        self.world=world.obj_world(self)# world template
        self.world.addrule('rule_world_bdry', world.obj_rule_bdry_bounces_rigidbody(self.world))# add rule: collision hero and bdry
        self.bdry=actor.obj_actor_bdry(self.world)# actors adds themselves to world upon creation
        self.hero=actor.obj_actor_hero_v0(self.world,(640,360))
        self.hero.addpart("a textbox",draw.obj_textbox('Move with [arrows] or [WASD]',(640,680),fontsize='large'))
        self.hero.scale(0.5)
    def page(self,controls):
        self.world.update(controls)


class obj_scene_testworldgrandactor(obj_testpage):
    def setup(self):
        self.name='World Grand Actor'       
        self.text=['World Grand Actor: ',\
                   'A simple actor (obj_actor) does basic functions. ',\
                   'A grand actor (obj_grandactor) is more elaborate: ',\
                   'it has a hitbox (r,rx,ry), ',\
                   'it can have elements (textbox, image, animation or dispgroup), ',\
                   'and it can be transformed.',\
                   'Try permanent transformations here: move [arrows], scale [w,s], rotate90 [a,d], flip [q,e]. ',\
                   'Toggle Dev mode with [Ctrl] to see grand actors hit boxes.',\
                   ]
        self.world=world.obj_world_ch1(self)
        self.hero=actor.obj_actor_hero_v0(self.world,(640,360))# a grand actor
        self.hero.addpart("element1",draw.obj_textbox('textbox attached to actor',(640,640),fontsize='large'))
        self.hero.scale(0.5)
    def page(self,controls):
        self.world.update(controls)
        if controls.w and controls.wc: self.hero.scale(2)
        if controls.s and controls.sc: self.hero.scale(0.5)
        if controls.a and controls.ac: self.hero.rotate90(90)
        if controls.d and controls.dc: self.hero.rotate90(-90)
        if controls.q and controls.qc: self.hero.fliph()
        if controls.e and controls.ec: self.hero.flipv()

class obj_scene_testrigidbody(obj_testpage):
    def setup(self):
        self.name='Actors with Rigid Bodies'       
        self.text=['Actors with Rigid Bodies: ',\
                   'A grand actor can have a rigidbody dynamics that induce additional movement. ',\
                   'External forces start rigidbody dynamics, and internal friction slows the actor ',\
                   'back to stalling.  ',\
                   'If stalling the actor can still be moved like a non rigidbody. '\
                   'Test move with [arrows] (non-rigidbody), force with [WASD] (rigidbody), ',\
                   'stall with [q,e]. ',\
                   ]
        self.world=world.obj_world(self)# world template
        self.world.addrule('truc',world.obj_rule_bdry_bounces_rigidbody(self.world) )
        bdry=actor.obj_actor_bdry(self.world)
        self.rigidbody=actor.obj_rbodyactor(self.world,(640,360))# actor rigidbody template
        self.rigidbody.addpart( 'img',draw.obj_image('testimage1',(640,360)) )        
    def page(self,controls):
        self.world.update(controls)
        # non rigid-body
        if controls.right: self.rigidbody.movex(5) 
        if controls.left: self.rigidbody.movex(-5)  
        if controls.up: self.rigidbody.movey(-5) 
        if controls.down: self.rigidbody.movey(5)     
        # rigid-body
        if controls.w and controls.wc: self.rigidbody.forcey(-5)
        if controls.s and controls.sc: self.rigidbody.forcey(5)
        if controls.a and controls.ac: self.rigidbody.forcex(-5)
        if controls.d and controls.dc: self.rigidbody.forcex(5)
        if controls.q and controls.qc: self.rigidbody.stall()
        if controls.e and controls.ec: self.rigidbody.stall()

####################################################################################################################


# quickdraft animations (do it quickly here)
class obj_scene_testdraftanimation(obj_testpage):
    def setup(self):
        self.name='QuickDraft Animation'       
        self.text=['QuickDraft Animation: [Space] Toggle Record Mode.']
        #
        if False:# hero legs stand (chapter 1)
            self.animation=draw.obj_animation('herolegs_stand','herolegs_stand',(640,360),record=True)
        elif False:# hero legs walk (chapter 1)
            self.animation=draw.obj_animation('herolegs_walk','herolegs_stand',(640,360),record=True)
            self.animation.addimage('herolegs_walk')
        else:# hero head (chapter 1)
            self.animation=draw.obj_animation('herohead_lookaround','herohead',(640,360))

    def page(self,controls):
        self.animation.update(controls)# this means animation can be edited


####################################################################################################################



