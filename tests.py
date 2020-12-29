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

import core

import share
import tool
import draw
import page
import actor
import world
#
import menu

##########################################################
##########################################################

# Test Menu
class obj_scene_testmenu(page.obj_page):
    def __init__(self):
        super().__init__()
    def setup(self):
        self.nrow=17# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Appendix Developer Tests [Enter: Read] [Tab: Back]',(640,50),fontsize='medium'))
        for i,test in enumerate(self.list[:self.nrow-1]):
            self.addpart(draw.obj_textbox(test.name,(250,130+i*30),fontsize='smaller'))
        for i,test in enumerate(self.list[self.nrow-1:]):
            self.addpart(draw.obj_textbox(test.name,(640,130+i*30),fontsize='smaller'))            
        self.sprite_pointer=draw.obj_textbox('---',(640,360),fontsize='smaller')# moved around
        self.addpart(self.sprite_pointer)                
    def page(self,controls):
        if share.itest<self.nrow-1:
            self.sprite_pointer.movetox(60)
            self.sprite_pointer.movetoy(130+share.itest*30)
        else:
            self.sprite_pointer.movetox(460)
            self.sprite_pointer.movetoy(130+(share.itest-self.nrow+1)*30)
        if (controls.s and controls.sc) or (controls.down and controls.downc): 
            share.itest += 1
            if share.itest == self.listlen: share.itest=0
        if (controls.w and controls.wc) or (controls.up and controls.upc): 
            share.itest -= 1
            if share.itest == -1: share.itest=self.listlen-1
        if (controls.tab  and controls.tabc) or (controls.esc and controls.escc): 
            share.scenemanager.switchscene(share.titlescreen,init=True)
        if (controls.enter and controls.enterc):
            share.scenemanager.switchscene(self.list[share.itest],init=True)
    def loadtests(self):# load all tests 
        # developper
        self.list.append(obj_scene_testmessage())       
        self.list.append(obj_scene_testdevnotes())
        self.list.append(obj_scene_testdevmodeinfo())
        # page
        self.list.append(obj_scene_testpagefunctions())
        # text
        self.list.append(obj_scene_interactivetext())
        self.list.append(obj_scene_textinput())     
        self.list.append(obj_scene_textchoice())              
        self.list.append(obj_scene_textbox())       
        # drawing
        self.list.append(obj_scene_testdrawing())
        self.list.append(obj_scene_testdrawingbase())
        # image
        self.list.append(obj_scene_testimage())        
        # animation      
        self.list.append(obj_scene_testanimation())    
        self.list.append(obj_scene_testanimationanimation())
        self.list.append(obj_scene_testanimationplayback()) 
        #dispgroup
        self.list.append(obj_scene_testdispgroup())
        #world
        self.list.append(obj_scene_testworld())
        self.list.append(obj_scene_testworldgrandactor())
        self.list.append(obj_scene_testrigidbody())        
        #quickdraft
        self.list.append(obj_scene_testdraftanimation())          
        #
        self.listlen=len(self.list)


# Template for test page = chapter page with slightly modified functionalities
class obj_testpage(page.obj_chapterpage):
    def __init__(self):
        self.name='Unamed'# needs name to display on test menu
        super().__init__()
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}
    def setup(self):
        super().setup()
    def postsetup(self):
        super().postsetup()
        self.pagenote.make('[Tab: Back]  [Enter: Back]')
    def postpage(self,controls):# foreground
        self.pagedisplay_fps.update()
        self.pagenote.display()
        self.pagetext.display()
    def callprevpage(self,controls):# no browsing
        pass
    def callnextpage(self,controls):# no browsing
        pass
    def callexitpage(self,controls):
        if (controls.tab  and controls.tabc) or (controls.enter  and controls.enterc) or (controls.esc and controls.escc):
            self.preendpage() 
            self.endpage()
            share.scenemanager.switchscene(obj_scene_testmenu())
    def prevpage(self):# no browsing
        pass
    def nextpage(self):# no browsing
        pass     

        
#########################################################################
#########################################################################
# All Tests Here

# quickdraft animations (do it quickly here)
class obj_scene_testdraftanimation(obj_testpage):
    def setup(self):
        self.name='QuickDraft Animation'       
        self.text=['QuickDraft Animation: [Space] Toggle Record Mode.']
        #
        animation=draw.obj_animation('herohead_lookaround','herohead',(640,360))
        # animation=draw.obj_animation('herolegs_stand','herolegs_stand',(640,360),record=True)
        # animation=draw.obj_animation('herolegs_walk','herolegs_stand',(640,360),record=True)
        # animation.addimage('herolegs_walk')
        ###
        
        ###
        self.addpart(animation)
        

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
            'core=game engine (all pygame elements there)',\
            'tool=basic functions (link external libraries there like math,os...). ',\
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
        self.name='Devmode'       
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
        dg=draw.obj_dispgroup((640,600))
        self.addpart(dg)
        dg.addpart("key_element1",draw.obj_textbox('dispgroup',(640,650)) )
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
            'Test1 name 1 is',('{test1}',share.colors.gray),', '\
            'and Test2 name is',('{test2}',share.colors.gray),' '\
            '(refresh page to see those changes). ',\
            'Special characters can be included in inputs (no issues were found). ',\
            'The textinput legend itself accepts keywords (but not colors). ',\
            '\nNote: the keywords themselves are formatted and can point to keywords. ',\
            'Try inputing test2={_test1_} without the underscores (test2 name will become test1 name). ',\
                   ]
        self.addpart( draw.obj_textinput('test1',20,(640,400),legend='name of test 1') )
        self.addpart( draw.obj_textinput('test2',20,(640,600),legend='name of test 2. keyword value: {test2}') )


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
        self.addpart( draw.obj_textbox("The test gender was:",(200,460)) )
        textchoice=draw.obj_textchoice('test_he')
        textchoice.addchoice('1. A guy','he',(440,460))
        textchoice.addchoice('2. A girl','she',(740,460))
        textchoice.addchoice('3. A thing','it',(1040,460))
        textchoice.addchoice('4. The keyword: {test1}','{test1}',(640,560))
        textchoice.addkey('test_his',{'he':'his','she':'her','it':'its','{test1}':'{test1}ss'})# additional key and analogies
        self.addpart( textchoice )
    def page(self,controls):
        pass
        # print(share.words.dict['test_he'])# can access key value directly
        

class obj_scene_textbox(obj_testpage):
    def setup(self):
        self.name='Textbox Basics'    
        self.text=[
            'Textbox Basics: Placed anywhere, can customize font and color. ',\
            'Accepts existing keywords like ',('{test1}',share.colors.green),'. ',\
            'Acts like an image: Can reset[space], move [Arrows], flip [q,e], scale[w,s], rotate90 [a,d]. ',\
            'Can rotate[f] but use sparingly (enlargens-memory issues). ',\
                   ]
        self.addpart(draw.obj_textbox('textbox',(340,260),color=share.colors.blue))#customize font and color
        self.addpart(draw.obj_textbox('small',(340,360),color=share.colors.blue, fontsize='tiny'))
        self.addpart(draw.obj_textbox('large',(340,460),color=share.colors.blue, fontsize='big'))
        self.addpart(draw.obj_textbox('from keyword: {test1}',(340,660),color=share.colors.green))
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
                   'It has optionally a legend, that accepts keywords like ',\
                   ('{test1}',share.colors.green),' (but not colors). ',\
                   'A drawing needs a background of same name in folder ./shadows. ',\
                   'It is saved in folder ./drawings. ',\
                   'If replacing the shadow erase the drawing as well (or new drawing may glitch). ',\
                   ]
        self.addpart( draw.obj_drawing('testimage1',(640,360),legend='draw me. Keyword:{test1}') )


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
                   'set sequence maxlength to length of other, and record for that duration. ',\
                   '(then return to this page to see both animations in sync). ',\
                   ]
        animation1=draw.obj_animation('testanimation1','testimage1',(340,360))# cannot edit
        animation2=draw.obj_animation('testanimation2','testimage2',(940,360),record=True)# can edit
        animation2.sequence.maxlength=animation1.sequence.length# set same length
        self.addpart(animation1)
        self.addpart(animation2)


# Scene: test create/show animation
class obj_scene_testanimationplayback(obj_testpage):
    def setup(self):
        self.name='Animation Playback'       
        self.text=['Animation Playback: ',\
                   'During playback, animation accepts permanent changes: move,flip, scale, rotate90,rotate. ',\
                   'use rotate sparingly (enlargens leading to potential memory issues). ',\
                   'Always record animation WITHOUT any permanent changes. ',\
                   'Test permanent changes here: [Arrows] Move, [w,s] scale, [a,d] rotate90, [f,g] rotate45, [q,e] flip. ',\
                   'The permanent changes modify animation movements too',\
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
        if controls.f and controls.fc: self.animation.rotate(45)
        if controls.g and controls.gc: self.animation.rotate(-45)
        if controls.w and controls.wc: self.animation.scale(2)
        if controls.s and controls.sc: self.animation.scale(0.5)
        if controls.space and controls.spacec: self.animation.setup()
        #

            

# Scene: test animation group move
class obj_scene_testdispgroup(obj_testpage):
    def setup(self):
        self.name='Display group'        
        self.text=['Display Group (or dispgroup): A group of elements that can be transformed while conserving its structure. ',\
                   'accepted elements are: textbox, image, animation. ',\
                   'Test here applying permanent changes to the dispgroup: [arrow keys] to move. ',\
                   '[q] and [e] to flip. [w] and [s] to 2x scale (dont repeat, it degrades images). ',\
                   '[a] and [d] for rotate90. [f] [g] to rotate 45 (dont repeat, it enlargens images).',\
                   ' Reset this page with [space]. ',\
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
        if controls.f and controls.fc: self.dispgroup.rotate(45)
        if controls.g and controls.gc: self.dispgroup.rotate(-45)
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


####################################################################################################################



