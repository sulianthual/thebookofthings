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

# import core
import share
import tool
import draw
import page
import world
#

##########################################################
##########################################################

# Test Menu
class obj_scene_testmenu(page.obj_page):
    def __init__(self):
        super().__init__()
    def setup(self):
        super().setup()
        share.ipage=1# current page number in chapter
        self.nrow=17# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Appendix Developer Tests [Enter: Read] [Tab: Back]',(640,50),fontsize='medium'))
        self.addpart(draw.obj_textbox('[Space: Menu]',(1120,700),fontsize='smaller'))
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
        if (controls.enter and controls.enterc):
            share.scenemanager.switchscene(self.list[share.itest],init=True)
        if (controls.esc and controls.escc) or (controls.space and controls.spacec):
            share.scenemanager.switchscene(share.titlescreen)


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
        self.list.append(obj_scene_testdispgroupsnapshot())
        #world
        self.list.append(obj_scene_testworld())
        self.list.append(obj_scene_testworldgrandactor())
        self.list.append(obj_scene_testrigidbody())
        #
        self.listlen=len(self.list)


# Template for test page = chapter page with slightly modified functionalities
class obj_testpage(page.obj_chapterpage):
    def __init__(self):
        self.name='Unamed'# needs name to display on test menu
        super().__init__()
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def exitpage(self):
        share.scenemanager.switchscene(obj_scene_testmenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())


#########################################################################
#########################################################################
# All Tests Here

class obj_scene_testmessage(obj_testpage):
    def setup(self):
        self.name='Message from the Developer'
        self.text=[(self.name,share.colors.red),': ',\
                   '\n\nThis is an appendix for tests by the Game Developer. ',\
                   'If you are not the Game Developer get out of here!',\
                   ]
        self.textkeys={}# defaut text formatting


class obj_scene_testdevnotes(obj_testpage):
    def setup(self):
        self.name='Developper Notes'
        self.text=[(self.name,share.colors.red),': ',\
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
                   ('grand actor (hitbox)',share.colors.devactor),', and ',\
                   ('drawing',share.colors.drawing),', ',\
                   ('textinput',share.colors.textinput),', except for ',\
                   ('textchoice',share.colors.textchoice),\
                   'not affected. ',\
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
        test=world.obj_grandactor(ww,(640,360))
        test.addpart("image", draw.obj_image('testimage2',(640,360)) )



# Scene: page basics
class obj_scene_testpagefunctions(obj_testpage):
    def setup(self):
        self.name='Page Basics'
        self.text=['Pages Basics: each page in the book is a scene from a template (see obj_page). ',\
                   'In \"setup\", addpart(element) adds element to list of managed elements. ',\
                   'Managed elements are updated and displayed by the page in the order they were added,',\
                   ' which determines their layering, ',\
                   'and finished (=saved) on page exit if necessary. ',\
                   'In \"page\" one can add additional update commands for an element. '
                   ' Elements can be managed manually but is is not recommended ',\
                   ]
        # managed elements can be: drawing,textinput,textbox,image,animation,dispgroup,world
        # element must have matching self.type to be managed by obj_page
        self.addpart(draw.obj_textbox('Managed elements here',(340,360),color=share.colors.red))
        self.addpart(draw.obj_drawing('testimage1',(340,560)))
        self.textbox=draw.obj_textbox('Non Managed elements here',(940,360),color=share.colors.blue)
        self.drawing=draw.obj_drawing('testimage2',(940,560))# new drawing
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
            'Save an image of textbox[g] (useful to animate it). ',\
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
        if controls.g and controls.gc: self.textbox.snapshot('testimagetextbox',path='book')

# Scene: test draw something
class obj_scene_testdrawing(obj_testpage):
    def setup(self):
        self.name='Drawing Basics'
        self.text=['Drawing Basics: Draw with [Left Mouse], Erase with [Right Mouse] ',\
                   '(only when the mouse is in drawing area). ',\
                   'You can draw shadows with [Middle Mouse] too. ',\
                   'Drawing can have a legend, that accepts keywords like ',\
                   ('{test1}',share.colors.green),' (but not colors). ',\
                   'Drawings are saved in folder ./book. ',\
                   '\nA standard drawing needs a shadow (grayed areas) of same name in folder ./shadows. ',\
                   'Drawing and shadow should be of same size. ',\
                   '\nOr one can make a drawing without shadow file if specifying the half-width and half-height (\"shadow=\"). ',\
                   ]
        self.addpart( draw.obj_drawing('testimage1',(340,460),legend='draw me. Keyword:{test1}') )
        self.addpart( draw.obj_drawing('testimage3',(940,460),legend='Drawing without shadow file',shadow=(100,100)) )


# Scene: test several drawings at the same time
class obj_scene_testdrawingbase(obj_testpage):
    def setup(self):
        self.name='Drawing Base'
        self.text=['Drawing Base: A drawing can be the base for other drawing ',\
                   '(of same dimensions). The other drawing should better have no shadows.',\
                   'Small glitches happen when coming back to existing drawings with base: in that case just erase and restart. ',\
                   ]
        drawing1=draw.obj_drawing('testimage1',(340,420),legend='base')
        self.addpart(drawing1)
        drawing2=draw.obj_drawing('testimage2',(940,420),base=drawing1,legend='drawing with base')
        # drawing2.clear()# clear it
        self.addpart(drawing2)


# Scene: test show image
class obj_scene_testimage(obj_testpage):
    def setup(self):
        self.name='Image Basics'
        self.text=['Image Basics: ',\
            'Test transformations here like move [Arrows], flip [q,e], scale [w,s], rotate90 [a,d], reset [space]. ',\
            'Can rotate [f] but use sparingly: it enlargens image each time leading to memory issues. ',\
            'An imagefill is an image of single color (preferentially the background) used to make layering. ',\
            'Press [r]: Image can quickly be saved and loaded which includes the transformations. ',\
            'Image drawn by player are in folder /book, but one can also read from /data or from /premade. ',\
                   ]
        self.image1=draw.obj_image('testimage1',(440,520), scale=2)# (can scale at creation)
        self.image2=draw.obj_image('testimage2',(840,520))
        self.image3=draw.obj_image('error',(1040,520),path='data')# read from other folder than /book
        # layering
        self.addpart(self.image3)
        self.addpart(self.image2)
        self.addpart(draw.obj_imagefill((share.colors.background,200,300),(260,360)))# filler on top
        self.addpart(self.image1)
    def page(self,controls):
        if controls.right: self.image2.movex(5)
        if controls.left: self.image2.movex(-5)
        if controls.up: self.image2.movey(-5)
        if controls.down: self.image2.movey(5)
        if controls.e and controls.ec: self.image2.fliph()# tests
        if controls.q and controls.qc: self.image2.flipv()# tests
        if controls.a and controls.ac: self.image2.rotate90(90)
        if controls.d and controls.dc: self.image2.rotate90(-90)
        if controls.w and controls.wc: self.image2.scale(2)
        if controls.s and controls.sc: self.image2.scale(0.5)
        if controls.space and controls.spacec: self.image2.setup()
        if controls.f and controls.fc: self.image2.rotate(45)
        if controls.r and controls.rc: # save and load
            self.image2.save('testimage1')
            self.image1.load('testimage1')




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
        self.name='Animation Sync'
        self.text=[(self.name,share.colors.red),': ',\
                   'Only one animation per page should be recordable. ',\
                   'Use \"sync\" to ensure an animation has the same duration as a reference one. ',\
                   'If a new animation, the recording will stop once reference length has been reached ',\
                   '(try it here and refresh the page to see the correct sync). ',\
                   'If an existing animation, it will load only up to the reference length ',\
                   '(try recording a shorter reference animation then come back to this page). ',\
                   ]
        animation1=draw.obj_animation('testanimation1','testimage1',(340,360))# cannot edit
        animation2=draw.obj_animation('testanimation2','testimage2',(940,360),record=True,sync=animation1)# can edit
        self.addpart(animation1)
        self.addpart(animation2)


# Scene: test create/show animation
class obj_scene_testanimationplayback(obj_testpage):
    def setup(self):
        self.name='Animation Playback'
        self.text=[(self.name,share.colors.red),': ',\
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

# Scene: test dispgroup move
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


# Scene: test dispgroup snapshot
class obj_scene_testdispgroupsnapshot(obj_testpage):
    def setup(self):
        self.name='Display group Snapshot'
        self.text=['Display group Snapshot: saves an image of a dispgroup (in designated area of screen). ',\
                   'Only works for images (useful to combine them). ',\
                   'Move dispgroup with [arrows]. Take a snapshot with [f] (prints the center area).',\
                   ]
        self.dispgroup=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup.addpart( "key_element1", draw.obj_image('testimage1',(440,360)) )# add image
        self.dispgroup.addpart( "key_element2", draw.obj_image('testimage2',(840,360)) )# add image
        self.dispgroup.addpart( "key_element3", draw.obj_textbox('textbox not saved',(640,360)) )# add textbox
        # dispgroup snapshot
        self.snaprect=640,360,300,200# center and radius of snapshot area on screen
        self.snapimage='testsnapshot'# name of snapshot image (saved in folder book)
        # image of snapshot
        self.snapshot=draw.obj_image('testsnapshot',(640,360))
        self.addpart(self.snapshot)
    def page(self,controls):
        self.dispgroup.update(controls)
        if controls.right: self.dispgroup.movex(5)
        if controls.left: self.dispgroup.movex(-5)
        if controls.up: self.dispgroup.movey(-5)
        if controls.down: self.dispgroup.movey(5)
        if controls.f  and controls.fc:
            self.dispgroup.snapshot(self.snaprect,self.snapimage)# take snapshot
            self.removepart(self.snapshot)# refresh image of snapshot on page
            self.snapshot=draw.obj_image('testsnapshot',(640,360))
            self.addpart(self.snapshot)

class obj_scene_testworld(obj_testpage):
    def setup(self):
        self.name='World Basics'
        self.text=['World Basics: ',\
                   'A World has actors in it as well as rules that manage interaction between actors. ',\
                   'The world checks all rules, and the rules may check and modify actors (but the actors dont check on rules). ',\
                   'Here the world has an actor=rigidbody, an actor=boundaries, and a rule=collision between the two. ',\
                   'Move the rigidbody around with [arrows] to test. ',\
                   '\nThere are several types of actors: simple actors (obj_actor), grand actors (obj_grandactor), ',\
                   'rigidbody actors (obj_rbodyactor),etc. One can make new actors as childs from the templates ',\
                   'but be careful with the init, setup, birth sequence (e.g. edit preferentially the setup). ',\
                   ]
        self.world=world.obj_world(self)# world template
        self.world.addrule('rule_rigidbody_bdry',world.obj_rule_bdry_bounces_rigidbody(self.world) )
        bdry=world.obj_actor_bdry(self.world)
        self.rigidbody=world.obj_rbodyactor(self.world,(640,360))# actor rigidbody template
        self.rigidbody.addpart( 'img',draw.obj_image('testimage1',(640,360)) )
    def page(self,controls):
        self.world.update(controls)
        # non rigid-body
        if controls.right: self.rigidbody.movex(5)
        if controls.left: self.rigidbody.movex(-5)
        if controls.up: self.rigidbody.movey(-5)
        if controls.down: self.rigidbody.movey(5)

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
        self.world=world.obj_world(self)# world template
        self.hero=world.obj_grandactor(self.world,(640,360))# a grand actor
        self.hero.addpart("element1",draw.obj_image('testimage1',(640,640),scale=2))
        self.hero.addpart("element2",draw.obj_textbox('textbox attached to actor',(640,840),fontsize='large'))
        self.hero.scale(0.5)
    def page(self,controls):
        self.world.update(controls)
        if controls.right: self.hero.movex(5)
        if controls.left: self.hero.movex(-5)
        if controls.down: self.hero.movey(5)
        if controls.up: self.hero.movey(-5)
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
        self.world.addrule('rule_rigidbody_bdry',world.obj_rule_bdry_bounces_rigidbody(self.world) )
        bdry=world.obj_actor_bdry(self.world)
        self.rigidbody=world.obj_rbodyactor(self.world,(640,360))# actor rigidbody template
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
