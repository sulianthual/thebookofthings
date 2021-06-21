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
# Note: All tests are init on menu init (which is problematic, loads all assets at once)
class obj_scene_testmenu(page.obj_page):
    def setup(self):
        self.nrow=14# number of rows one column
        self.list=[]# list of tests
        self.loadtests()
        self.addpart(draw.obj_textbox('Appendix Developer Tests',(640,50),fontsize='medium'))
        self.sprite_back=draw.obj_textbox('[back]',(420,50),fontsize='medium',hover=True)
        self.addpart(self.sprite_back)
        #
        self.textboxclickdict={}
        for i,test in enumerate(self.list):
            if i<=self.nrow-1:
                xref=240

            elif i>self.nrow-1 and i<=2*self.nrow-1:
                xref=640
            else:
                xref=1040
            tempo=draw.obj_textbox(test.pagename(),(xref,130+i%(self.nrow)*40),fontsize='smaller',hover=True)
            self.textboxclickdict[str(i)]=tempo
            self.addpart(tempo)
        #
        self.sound_menugo=draw.obj_sound('menugo')# sound is loaded but not played
        self.addpart( self.sound_menugo )
        self.sound_menuback=draw.obj_sound('menuback')# sound is loaded but not played
        self.addpart( self.sound_menuback )
        #
        self.addpart( draw.obj_music(None) )
    def page(self,controls):
        if self.sprite_back.isclicked(controls):
            self.sound_menuback.play()
            share.scenemanager.switchscene(share.titlescreen,initstart=True)# go back to menu
        #
        for i in self.textboxclickdict.keys():
            if self.textboxclickdict[str(i)].isclicked(controls):
                share.scenemanager.switchscene(self.list[int(i)],initstart=True)

        if controls.gb and controls.gbc:
            self.sound_menuback.play()
            share.scenemanager.switchscene(share.titlescreen)

    def loadtests(self):# load all tests
        # developper
        self.list.append(obj_scene_testmessage())
        self.list.append(obj_scene_testdevnotes())
        self.list.append(obj_scene_testdevnotesfiles())
        self.list.append(obj_scene_testdevmodeinfo())
        # page
        self.list.append(obj_scene_testpagefunctions())
        self.list.append(obj_scene_testpagebookmark())
        self.list.append(obj_scene_testpagebacknext())
        self.list.append(obj_scene_testheadermaker())
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
        self.list.append(obj_scene_testimageplacer())
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
        # audio
        self.list.append(obj_scene_testmusic())
        self.list.append(obj_scene_testsounds())
        self.list.append(obj_scene_testsoundplacer())
        # drafts
        self.list.append(obj_scene_alldrawings())
        self.list.append(obj_scene_testdrafting())
        #
        # ideas
        self.list.append(obj_scene_testbreakfastdrinking())
        #
        self.listlen=len(self.list)




# Template for test page = chapter page with modified functionalities
#
# 1) Does not initstart at init (allows to make inventory of empty testpages)
#    (as a result **kwargs are omitted by init)
# 2) pagename() is used to make an inventory of testpages
#
class obj_testpage(page.obj_chapterpage):
    def __init__(self,**kwargs):
        pass# no initstart
    def pagename(self):
        return 'Test Page'
    def presetup(self):
        super().presetup()
        self.textkeys={'fontsize':'small','linespacing': 45}# modified main text formatting
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def exitpage(self):
        share.scenemanager.switchscene(obj_scene_testmenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def textboxplace(self):# always top left
        self.textboxprevpage_xy=( 10,690 )
        self.textboxnextpage_xy=( 190,690 )
    def triggerprevpage3(self,controls):
        return self.triggerprevpage2(controls) or (controls.gb and controls.gbc)
    def triggernextpage3(self,controls):
        return self.triggernextpage2(controls) or (controls.ga and controls.gac)




#########################################################################
#########################################################################
# All Tests Here




class obj_scene_testmessage(obj_testpage):
    def pagename(self):
        return 'Message from the Developer'
    def setup(self):
        self.text=['Message from the Developer: ',\
                   '\n\nThis is an appendix for tests by the Game Developer. ',\
                   'If you are not the Game Developer get out of here!',\
                   '\n ',\
                   ]
        self.textkeys={}# defaut text formatting


class obj_scene_testdevnotes(obj_testpage):
    def pagename(self):
        return 'Code Architecture'
    def setup(self):
        self.text=['Code Architecture: ',\
                    ('()=files imported by this file. ',share.colors.darkgreen),\
                    ('**=share, page, draw, world, tool. ',share.colors.darkgreen),\
                    #
                    '\n ',('Top: ',share.colors.red),\
                    ('main.py',share.colors.blue),(' (share)',share.colors.darkgreen),\
                    '=runs main loop. ',\
                    ('share.py',share.colors.blue),(' (core, datb, menu)',share.colors.darkgreen),\
                    '=defines and stores shared content',\
                    ' (global variables, instances of main game objects). ',\
                    #
                    '\n ',('Modules: ',share.colors.red),\
                    ' these only hold classes/functions. ',\
                    ('page.py',share.colors.blue),(' (share, draw, tool)',share.colors.darkgreen),\
                    '=base structure for any page (or scene) in the game. ',\
                    ('draw.py',share.colors.blue),(' (share, core, tool)',share.colors.darkgreen),\
                    '=elements that can be added to a page',\
                    ' (text, image, animations, music, sounds...). ',\
                    ('core.py',share.colors.blue),(' (share, tool, pygame)',share.colors.darkgreen),\
                    '=game engine (manages display, audio, controls, sprites and switches scenes). ',\
                    'edit pygame handling here (e.g., dirtysprites, etc). ',\
                    ('tool.py',share.colors.blue),(' (external only)',share.colors.darkgreen),\
                    '=all external modules (math,os...) linked here. ',\
                    #
                    '\n ',('Content: ',share.colors.red),\
                    ' these only hold classes/functions. ',\
                    ('menu.py',share.colors.blue),(' (**,ch0,ch1..., test)',share.colors.darkgreen),\
                    '=main menu, settings pages. ',\
                    ('ch0.py,ch1...',share.colors.blue),(' (**)',share.colors.darkgreen),\
                    '=book chapters pages. ',\
                    ('tests.py',share.colors.blue),(' (**)',share.colors.darkgreen),\
                    '=developper tests pages. ',\
                    ('world.py',share.colors.blue),(' (share, draw, core, tool)',share.colors.darkgreen),\
                    '=worlds that can be displayed on a page (e.g. minigames). ',\
                    ('datb.py',share.colors.blue),(' (draw, core, tool)',share.colors.darkgreen),\
                    '=handles data. ',\
                   ]

class obj_scene_testdevnotesfiles(obj_testpage):
    def pagename(self):
        return 'File Architecture'
    def setup(self):
        self.text=['File Architecture: ',\
                    '\n ',\
                    '\n ',('./',share.colors.blue),' = all code (.py), LICENSE, README.md (with screenshot.png),   ',\
                    '\n ',('animations/',share.colors.blue),' = all game animations (text files).  ',\
                    '\n ',('book/',share.colors.blue),' = all player saved data (drawings .png, settings.txt, progress.txt, words.txt ). ',\
                    'can be shared (by replacing same folder on other computer). ',\
                    'erases when book is deleted. ',\
                    '\n ',('data/',share.colors.blue),' = some game data (fonts .ttf, .png for window icon, brushes, error image, also stores .xcf).  ',\
                    '\n ',('musics/',share.colors.blue),' = all game musics (prefer .ogg, maybe .wav, but .mp3 wont work with pygame 2.0).  ',\
                    '\n ',('premade/',share.colors.blue),' = all premade drawings (.png).  ',\
                    '\n ',('shadows/',share.colors.blue),' = premade shadows used for drawings (.png, also stores .xcf).  ',\
                    'these are image layers (e.g. gray or white surfaces) that are added to some drawings. ',\
                    '\n ',('sounds/',share.colors.blue),' = all game sounds (prefer .ogg, maybe .wav, but .mp3 wont work with pygame 2.0).  ',\
                    '\n ',('.git, .gitignore',share.colors.blue),' = dont remove, used for version control with git.  ',\

                   ]

class obj_scene_testdevmodeinfo(obj_testpage):
    def pagename(self):
        return 'Devmode'
    def setup(self):
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
                   ' not affected. ',\
                   'You can also print mouse position in terminal with [Right Mouse]. ',\
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
    def pagename(self):
        return 'Page Basics'
    def setup(self):
        self.text=['Pages Basics: each page in the book is a scene from a template (see obj_page). ',\
                   'In \"setup\", addpart(element) adds element to list of managed elements. ',\
                   'Managed elements are updated and displayed by the page in the order they were added,',\
                   ' which determines their layering, ',\
                   'and finished (=saved) on page exit if necessary. ',\
                   ' Elements can alo be managed manually (not recommended). ',\
                   'Page object should only be created when switching with scenemanager (except testpages). ',\
                   '',\
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

# Scene: page bookmark
class obj_scene_testpagebookmark(obj_testpage):
    def pagename(self):
        return 'Page Bookmark'
    def setup(self):
        self.text=['Page Bookmark: from the main menu (obj_titlescreen in menu.py), pages by bookmarks. ',\
                   'Only certain chapter pages are bookmarked. ',\
                  '\n1) To bookmark a chapter page, add a setbookmark in the setup(). ',\
                  '2) then edit  menu.py obj_gotobookmark to add the id and corresponding scene object',\
                  ' (there ids added to the self.dict are visible from the menu)',\
                   ]
        # share.datamanager.setbookmark('ch0_drawpen')# this in a regular chapter page sets a bookmark


# Scene: page bookmark
class obj_scene_testpagebacknext(obj_testpage):
    def prevpage(self):
        pass
    def triggerprevpage(self,controls):# this turns off the trigger from click
        return False
    def textboxprevpage(self):# this does show the [Back] textbox
        pass
    def pagename(self):
        return 'Page [Back] [Next]'
    def textboxplace(self):# This modifies the position of the textboxes
        self.textboxprevpage_xy=(1050,660)
        self.textboxnextpage_xy=(1230,660)
    def setup(self):
        self.text=['Page [Back] [Next]: by default all chapter pages have these clickable textboxes',\
                   'Placement methods are  in page.py, obj_chapterpage (textboxplace, textboxprevpage, etc...). ',\
                   'These textboxes try to go right after main text, but sometimes further adjustment are necessary ',\
                   '\n (note: option domousebrowse has become permanent, must always remain =True) ',\
                   ]
        # share.datamanager.setbookmark('ch0_drawpen')# this in a regular chapter page sets a bookmark



# Scene: page basics
class obj_scene_testheadermaker(obj_testpage):
    def pagename(self):
        return 'Header Maker'
    def setup(self):
        self.text=['Header Maker: add this to quickly build the code headers for pages in a chapter. ',\
                   'check the file book/aaa.txt for the code output. ',\
                  'Page must start above 0. Last nextpage is commented (for if next page doesnt exist) ',\
                   ]
        # self.addpart( draw.obj_headermaker('ch3',10,25) )# for chapter 3, page 10 to 25
        self.addpart( draw.obj_headermaker('ch5',1,80) )# for chapter 3, page 10 to 25


class obj_scene_interactivetext(obj_testpage):
    def pagename(self):
        return 'Text Basics'
    def setup(self):
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
    def pagename(self):
        return 'Text input'
    def setup(self):
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
        self.addpart( draw.obj_textinput('test2',20,(640,600),color=share.colors.blue,legend='name of test 2. keyword value: {test2}') )


class obj_scene_textchoice(obj_testpage):
    def pagename(self):
        return 'Text Choice'
    def setup(self):
        self.text=[
            'textchoice: Hover with [Mouse] and click with [Left Mouse] to select among choices. ',\
            'The current choice is the circled one. ',\
            'This saves keywords (in words.txt) similar to textinput. ',\
            'Refresh this page to see changes: \n "',('{test_he}',share.colors.red),' was the test". ',\
            '\nA textchoice can have additional keys: ',\
            'a choice for the base key determines the choices of the additional keys using analogies. ',\
            '\n "The test hero made ',('{test_his}',share.colors.red),' choice". ',\
            '\n It is possible to set a default choice (here value is always when refreshing the page)',\
            ]
        y1=450
        self.addpart( draw.obj_textbox("The test gender was:",(200,y1)) )
        textchoice=draw.obj_textchoice('test_he')# optional to set default choice
        textchoice.addchoice('1. A guy','he',(440,y1))
        textchoice.addchoice('2. A girl','she',(640,y1))
        textchoice.addchoice('3. A thing','it',(840,y1))
        textchoice.addkey('test_his',{'he':'his','she':'her','it':'its'})# additional key and analogies
        self.addpart( textchoice )
        #
        y2=600
        self.addpart( draw.obj_textbox("Default value was:",(200,y2)) )
        textchoice2=draw.obj_textchoice('test_value',default='one')# optional to set default choice
        textchoice2.addchoice('1. one','one',(440,y2))
        textchoice2.addchoice('2. two','two',(740,y2))
        textchoice2.addchoice('3. three','three',(1040,y2))
        self.addpart( textchoice2 )

#*TEXTBOX
class obj_scene_textbox(obj_testpage):
    def pagename(self):
        return 'Textbox Basics'
    def setup(self):
        self.text=[
            'Textbox Basics:',\
            '\n 1) can customize font, color (including filling), line-adjustment. ',\
            'Accepts existing keywords like ',('{test1}',share.colors.green),'. ',\
            '\n 2) Can be transformed: ',\
            '[arrows alone]:move. ',\
            '[lmouse +arrows]:scale, rotate90. ',\
            '[rmouse +left/right]:flip. ',\
            '[rmouse +up]:rotate45 (use sparingly cf enlargens-memory issues). ',\
            '[rmouse +down]:save an image (useful to animate). ',\
            '[lmouse +rmouse]:reset. ',\
            '\n 3) can be hovered ',\
                   ]
        self.addpart(draw.obj_textbox('textbox',(140,560)))# standard
        self.addpart(draw.obj_textbox('custom',(240,460),color=share.colors.blue, fontsize='big',fillcolor=share.colors.black))#customize font and color
        self.addpart(draw.obj_textbox('xleft-ytop',(240,560),xleft=True,ytop=True))# line adjusted
        self.addpart(draw.obj_textbox('from keyword: {test1}',(240,660),color=share.colors.green))
        self.textbox=draw.obj_textbox('textbox:move me',(840,560),color=share.colors.red,fillcolor=share.colors.blue)
        self.addpart(self.textbox)
        self.textbox2=draw.obj_textbox('hoverable (print when clicked)',(640,460),hover=True)
        self.addpart(self.textbox2)
        self.textbox3=draw.obj_textbox('hoverable ',(640,660),hover=True,hovercolor=share.colors.blue)
        self.addpart(self.textbox3)# hoverable (hovercolor default is purple)
        self.dx,self.dy=5,5
    def page(self,controls):
        #
        if controls.gm1:
            if controls.gu and controls.guc: self.textbox.scale(2)
            if controls.gd and controls.gdc: self.textbox.scale(0.5)
            if controls.gl and controls.glc: self.textbox.rotate90(90)
            if controls.gr and controls.grc: self.textbox.rotate90(-90)
            if controls.gm2: self.textbox.setup()
        elif controls.gm2:
            if controls.gu and controls.guc: self.textbox.rotate(45)
            if controls.gd and controls.gdc: self.textbox.snapshot('testimagetextbox',path='book')
            if controls.gl and controls.glc: self.textbox.fliph()
            if controls.gr and controls.grc: self.textbox.flipv()
        else:
            if controls.gu: self.textbox.movey(-self.dy)
            if controls.gd: self.textbox.movey(self.dy)
            if controls.gl: self.textbox.movex(-self.dx)
            if controls.gr: self.textbox.movex(self.dx)
        if self.textbox2.isclicked(controls):
            print('textbox 2 is clicked')# very useful
        # if self.textbox3.ishovered(controls):
        #     print('textbox 3 is hovered')




# Scene: test draw something
class obj_scene_testdrawing(obj_testpage):
    def pagename(self):
        return 'Drawing Basics'
    def setup(self):
        self.text=['Drawing Basics: Draw with [Left Mouse], Erase with [Right Mouse] ',\
                   '(when mouse is in drawing area). ',\
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
    def pagename(self):
        return 'Drawing Base'
    def setup(self):
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
    def pagename(self):
        return 'Image Basics'
    def setup(self):
        self.text=['Image Basics: ',\
            'Try it: ',\
            '[arrows alone]:move. ',\
            '[lmouse+arrows]:scale, rotate90. ',\
            '[rmouse+left/right]:flip. ',\
            '[rmouse+up]:rotate45 (use sparingly cf enlargens-memory issues). ',\
            '[rmouse+down]:save/load (includes transformations). ',\
            '[lmouse+rmouse]: reset. ',\
            'Image drawn by player are in folder /book, but one can also read from /data or from /premade. ',\
            'If image doesnt exist the error image is read.  ',\
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
        #
        if controls.gm1:
            if controls.gu and controls.guc: self.image2.scale(2)
            if controls.gd and controls.gdc: self.image2.scale(0.5)
            if controls.gl and controls.glc: self.image2.rotate90(90)
            if controls.gr and controls.grc: self.image2.rotate90(-90)
            if controls.gm2: self.image2.setup()
        elif controls.gm2:
            if controls.gu and controls.guc: self.image2.rotate(45)
            if controls.gd and controls.gdc:
                self.image2.save('testimage1')
                self.image1.load('testimage1')
            if controls.gl and controls.glc: self.image2.fliph()
            if controls.gr and controls.grc: self.image2.flipv()
        else:
            if controls.gu: self.image2.movey(-5)
            if controls.gd: self.image2.movey(5)
            if controls.gl: self.image2.movex(-5)
            if controls.gr: self.image2.movex(5)


# Scene: test image placer
class obj_scene_testimageplacer(obj_testpage):
    def pagename(self):
        return 'Image Placer'
    def setup(self):
        self.text=['Image Placer: allows developer to quickly place images on screen. ',\
                    'the file book/aaa.txt is edited live, and the code can be quickly copied to a page. ',\
                   '[W,S or Up,Down:scale], [A,D or Left,Right:rotate], [Q,E: flip], [F: browse image], [G: Reset].',\
                   ' [LMouse: Place Image], [RMouse: Remove Last Image]',\
                   ' [R or Exit Page: Output to Code File]',\
                   '. These commands are received only in active mode: .',\
                   ' [T: Toggle Active Mode ]',\
                   ]
        self.addpart( draw.obj_imageplacer(self, 'testimage1','testimage2' ) )

        # These images below obtained quickly by copying content of book/aaa.txt
        # self.addpart( draw.obj_image('testimage1',(570,414),scale=1,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('testimage1',(905,328),scale=1.63,rotate=0,fliph=False,flipv=False) )
        #
        # Alternative where code is for adding content to an an actor named "staticactor"
        # self.addpart( draw.obj_imageplacer(self, 'testimage1','testimage2',actor='staticactor' ) )
        # self.staticactor.addpart( "img1", draw.obj_image('testimage1',(402,473),scale=1,rotate=0,fliph=False,flipv=False) )
        # self.staticactor.addpart( "img2", draw.obj_image('testimage2',(777,377),scale=1,rotate=0,fliph=False,flipv=False) )


#########################################################################
# Tests Animations

# Scene: test create/show animation
class obj_scene_testanimation(obj_testpage):
    def pagename(self):
        return 'Animation Record'
    def setup(self):
        self.text=['Animation Record: Animation has two modes, Record and Playback. Toggle Mode with [T]. ',\
                   '\n(You must be in Dev Mode to do so, which is Toggled by [CTRL]). ',\
                    '\n-- While in Record Mode:',\
                    '\nRed Line tracks image center for all frames.',\
                    '\nBlue cross shows animation reference position.',\
                    '\n[G]: Erase all frames',\
                    '\n[Hold LMouse]: Append new frames',\
                    '\n[A-D]: Rotate around center',\
                    '\n[W-S]: Scale',\
                    '\n[Q-E]: Flip Horizontal/Vertical',\
                    '\n[F]: Change Image (if several exist)',\
                    '\n[R]: Save Animation to File (!)',\
                    '\n[Left-Right]/[Up-Down]: Tune Rotate/Scale Rates',\
                   '\n-- While in Playback Mode: Animation loop-plays.',\
                   ]
        animation=draw.obj_animation('testanimation1','testimage1',(640,360),record=True)
        animation.addimage('testimage2')
        animation.addimage('testimage3')
        self.addpart(animation)


# Scene: test animation alongside animation
class obj_scene_testanimationanimation(obj_testpage):
    def pagename(self):
        return 'Animation Sync'
    def setup(self):
        self.text=['Animation Sync: ',\
                   'Use \"sync\" to ensure an animation 2  has the same duration as animation 1. ',\
                   'To record: 1) hold RMouse (rewinds animation 1 to current frame of animation 2),',\
                   ' 2) Hold LMouse (starts recording animation 2 while playing animation1), ',\
                   '3) optionnally release LMouse for adjustments. 4) Record until the end of animation 1, save. ',\
                   '5) Exit or refresh the page (to sync perfectly). ',\
                  'Only one animation per page should be recordable (with record=True). ',\
                   ]
        animation1=draw.obj_animation('testanimation1','testimage1',(340,360))# cannot edit
        animation2=draw.obj_animation('testanimation2','testimage2',(940,360),record=True,sync=animation1)# can edit
        self.addpart(animation1)
        self.addpart(animation2)


# Scene: test create/show animation
class obj_scene_testanimationplayback(obj_testpage):
    def pagename(self):
        return 'Animation Playback'
    def setup(self):
        self.text=['Animation Playback: ',\
                   'During playback, animation accepts additional transformations. ',\
                   'Always record animation WITHOUT these transformations. ',\
                   'Try it: ',\
                   '[arrows alone]:move. ',\
                   '[lmouse+arrows]:scale, rotate90. ',\
                   '[rmouse+left/right]:flip. ',\
                   '[rmouse+up/down]:rotate45 (use sparingly cf enlargen memory issue). ',\
                   '[lmouse+rmouse]: reset. ',\
                   ]
        self.animation=draw.obj_animation('testanimation1','testimage1',(640,360))
        self.dx,self.dy=5,5
    def page(self,controls):
        self.animation.update(controls)# manual update
        #
        if controls.gm1:
            if controls.gu and controls.guc: self.animation.scale(2)
            if controls.gd and controls.gdc: self.animation.scale(0.5)
            if controls.gl and controls.glc: self.animation.rotate90(90)
            if controls.gr and controls.grc: self.animation.rotate90(-90)
            if controls.gm2: self.animation.setup()
        elif controls.gm2:
            if controls.gu and controls.guc: self.animation.rotate(45)
            if controls.gd and controls.gdc: self.animation.rotate(-45)
            if controls.gl and controls.glc: self.animation.fliph()
            if controls.gr and controls.grc: self.animation.flipv()
        else:
            if controls.gu: self.animation.movey(-self.dy)
            if controls.gd: self.animation.movey(self.dy)
            if controls.gl: self.animation.movex(-self.dx)
            if controls.gr: self.animation.movex(self.dx)


# Scene: test dispgroup move
class obj_scene_testdispgroup(obj_testpage):
    def pagename(self):
        return 'Display group'
    def setup(self):
        self.text=['Display Group (or dispgroup): A group of elements (textboxes,images or animations)',\
                    ' that can be transformed while conserving general structure. ',\
                   'Try it: ',\
                   '[arrows alone]:move. ',\
                   '[lmouse+arrows]:scale, rotate90. ',\
                   '[rmouse+left/right]:flip. ',\
                   '[rmouse+up/down]:rotate45 (use sparingly cf enlargen memory issue). ',\
                   '[lmouse+rmouse]: reset. ',\
                   'Beware: elements of dispgroup dont update, they play! some restrictions like cant hover textbox, etc... ',\
                   ]
        self.dispgroup=draw.obj_dispgroup((640,360))# create dispgroup
        self.dispgroup.addpart( "key_element1", draw.obj_image('testimage1',(440,360)) )# add image
        self.dispgroup.addpart( "key_element2", draw.obj_textbox('Move this',(640,360)) )# add textbox
        self.dispgroup.addpart( "key_element3", draw.obj_animation('testanimation2','testimage2',(840,360)) )# add animation
        # Note: each element of dispgroup must have an unique key
        self.dx,self.dy=5,5
    def page(self,controls):
        self.dispgroup.update(controls)
        if controls.gm1:
            if controls.gu and controls.guc: self.dispgroup.scale(2)
            if controls.gd and controls.gdc: self.dispgroup.scale(0.5)
            if controls.gl and controls.glc: self.dispgroup.rotate90(90)
            if controls.gr and controls.grc: self.dispgroup.rotate90(-90)
            if controls.gm2: self.setup()
        elif controls.gm2:
            if controls.gu and controls.guc: self.dispgroup.rotate(45)
            if controls.gd and controls.gdc: self.dispgroup.rotate(-45)
            if controls.gl and controls.glc: self.dispgroup.fliph()
            if controls.gr and controls.grc: self.dispgroup.flipv()
        else:
            if controls.gu: self.dispgroup.movey(-self.dy)
            if controls.gd: self.dispgroup.movey(self.dy)
            if controls.gl: self.dispgroup.movex(-self.dx)
            if controls.gr: self.dispgroup.movex(self.dx)

# Scene: test dispgroup snapshot
class obj_scene_testdispgroupsnapshot(obj_testpage):
    def pagename(self):
        return 'Display group Snapshot'
    def setup(self):
        self.text=['Display group Snapshot: snapshots a dispgroup (only its images). Useful to combine several drawings/images. ',\
                   'Try it: [arrows]: move. [lmouse]: take a snapshot (and refresh it on page).',\
                   'Note: the snapshot manager (in datb) automatically remakes all related snapshots each time a drawing is remade',\
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
        self.dx,self.dy=5,5
    def page(self,controls):
        self.dispgroup.update(controls)
        if controls.gu: self.dispgroup.movey(-self.dy)
        if controls.gd: self.dispgroup.movey(self.dy)
        if controls.gl: self.dispgroup.movex(-self.dx)
        if controls.gr: self.dispgroup.movex(self.dx)
        if controls.gm1 and controls.gm1c:
            self.dispgroup.snapshot(self.snaprect,self.snapimage)# take snapshot
            self.removepart(self.snapshot)# refresh image of snapshot on page
            self.snapshot=draw.obj_image('testsnapshot',(640,360))
            self.addpart(self.snapshot)


class obj_scene_testworld(obj_testpage):
    def pagename(self):
        return 'World Basics'
    def setup(self):
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
        if controls.gu: self.rigidbody.movey(-5)
        if controls.gd: self.rigidbody.movey(5)
        if controls.gl: self.rigidbody.movex(-5)
        if controls.gr: self.rigidbody.movex(5)


class obj_scene_testworldgrandactor(obj_testpage):
    def pagename(self):
        return 'World Grand Actor'
    def setup(self):
        self.text=['World Grand Actor: ',\
                   'A simple actor (obj_actor) does basic functions. ',\
                   'A grand actor (obj_grandactor) is more elaborate: ',\
                   'it has a hitbox (r,rx,ry), ',\
                   'it can have elements (textbox, image, animation or dispgroup), ',\
                   'and it can be transformed.',\
                  'Try it: ',\
                  '[arrows alone]:move. ',\
                  '[lmouse+arrows]:scale, rotate90. ',\
                  '[rmouse+left/right]:flip. ',\
                  '[lmouse+rmouse]: reset. ',\
                  '[ctrl]: toggle dev mode (see grand actor hit box). ',\
                   ]
        self.world=world.obj_world(self)# world template
        self.hero=world.obj_grandactor(self.world,(640,360))# a grand actor
        self.hero.addpart("element1",draw.obj_image('testimage1',(640,640),scale=2))
        self.hero.addpart("element2",draw.obj_textbox('textbox attached to actor',(640,840),fontsize='large'))
        self.hero.scale(0.5)
    def page(self,controls):
        self.world.update(controls)
        if controls.gm1:
            if controls.gu and controls.guc: self.hero.scale(2)
            if controls.gd and controls.gdc: self.hero.scale(0.5)
            if controls.gl and controls.glc: self.hero.rotate90(90)
            if controls.gr and controls.grc: self.hero.rotate90(-90)
            if controls.gm2: self.setup()
        elif controls.gm2:
            if controls.gl and controls.glc: self.hero.fliph()
            if controls.gr and controls.grc: self.hero.flipv()
        else:
            if controls.gu: self.hero.movey(-5)
            if controls.gd: self.hero.movey(5)
            if controls.gl: self.hero.movex(-5)
            if controls.gr: self.hero.movex(5)



class obj_scene_testrigidbody(obj_testpage):
    def pagename(self):
        return 'Actors with Rigid Bodies'
    def setup(self):
        self.text=['Actors with Rigid Bodies: ',\
                   'a grand actor with rigidbody dynamics (external forces, internal friction). ',\
                  'Try it: ',\
                  '[arrows alone]:move. ',\
                  '[lmouse+arrows]:apply forces. ',\
                  '[rmouse]: force stall. ',\
                  '[lmouse+rmouse]: reset. ',\
                   ]
        self.world=world.obj_world(self)# world template
        self.world.addrule('rule_rigidbody_bdry',world.obj_rule_bdry_bounces_rigidbody(self.world) )
        bdry=world.obj_actor_bdry(self.world)
        self.rigidbody=world.obj_rbodyactor(self.world,(640,360))# actor rigidbody template
        self.rigidbody.addpart( 'img',draw.obj_image('testimage1',(640,360)) )
    def page(self,controls):
        self.world.update(controls)
        if controls.gm1:
            if controls.gu and controls.guc: self.rigidbody.forcey(-5)
            if controls.gd and controls.gdc: self.rigidbody.forcey(5)
            if controls.gl and controls.glc: self.rigidbody.forcex(-5)
            if controls.gr and controls.grc: self.rigidbody.forcex(5)
            if controls.gm2: self.setup()
        elif controls.gm2:
            self.rigidbody.stall()
        else:
            if controls.gu: self.rigidbody.movey(-5)
            if controls.gd: self.rigidbody.movey(5)
            if controls.gl: self.rigidbody.movex(-5)
            if controls.gr: self.rigidbody.movex(5)




class obj_scene_testmusic(obj_testpage):
    def pagename(self):
        return 'Music'
    def setup(self):
        self.text=['Music: ',\
                    '\n\n1) Each page has a unique music, which addpart() overrides. Default is silence (music=None) ',\
                    '\n2) If a page has new music, the new music is played ',\
                    '\n3) If a page has same music as previous ones, previous music keeps playing (without rewinding) ',\
                    '\n4) If a page has no music, previous music stops (if any) ',\
                    '\n\nMusic is managed globally on a single music channel. ',\
                    'Page music is launched on first page update instead of page init and setup (to avoid playing several musics if several pages are preloaded)',\
                    ]
        self.addpart( draw.obj_music('test') )
        # self.addpart( draw.obj_music(None) )# mute music


class obj_scene_testsounds(obj_testpage):
    def pagename(self):
        return 'Sounds'
    def setup(self):
        self.text=['Sounds:',\
                ' \n\n1) Can add sounds to a page, then call them. Try it: [Up: play sound]',\
                ' \n\n2) Can add sound to an animation (specify frames where played). ',\
                ' By default, sounds are played each animation loop. Specificy skip>0 to play silent loops in between (affects all animation sounds) ',\
                ' \n\n3) Sounds can be looped. For example to do a background ambience into a page (on top of music). ',\
                '\n\n4) For safety, all sounds (notably looped) are stopped upon page init and page exit. '
                    ]
        self.sound1=draw.obj_sound('test1')# sound is loaded but not played
        self.addpart( self.sound1 )
        #
        animation1=draw.obj_animation('testanimation1','testimage1',(340,360))
        self.addpart(animation1)
        # animation1.addsound('test2',[0,10])# frame 0 not played on first read
        # animation1.addsound('test2',[1,10])# play on frame 1 and 10
        animation1.addsound('test2',[1,10,20,30])# works too if single frame
        # animation1.addsound('test2',20,skip=1)# animation skips playing any sound every 1 loop
        # ambience sound
        self.sound3=draw.obj_sound('test4')
        self.addpart( self.sound3 )
        self.sound3.play(loop=True)# looped sound
    def page(self,controls):
        if controls.gu and controls.guc: self.sound1.play()



class obj_scene_testsoundplacer(obj_testpage):
    def pagename(self):
        return 'Sound Placer'
    def setup(self):
        self.text=['Sound Placer:',\
                    'generate code to easily place sounds alongside animation. Output code is in book/aaa.txt',\
                    '\n[T]=toggle record mode (default on) ',\
                    '\n[R]=output code from recorded sounds',\
                    '\n[G]=clear all recorded sounds ',\
                    '\n[wasd,q,e,f]=play sound (or record in record mode) ',\
                    '\n\n[Rmouse]=rewind animation ',\
                    ]
        # animation
        animation=draw.obj_animation('testanimation1','testimage1',(340,360))
        self.addpart(animation)
        # sound placer
        # self.stuff=draw.obj_soundplacer(animation,'pen')
        # self.addpart( draw.obj_soundplacer(animation,'pen') )
        self.addpart( draw.obj_soundplacer(animation,'test3a','test3b','test3c','test3d','test1','test2','test3') )# up to 7 sound inputs at same time
        #
        # example of code from book/aaa.txt to copy on page
        # animation.addsound( "test3a", [45] )
        # animation.addsound( "test3b", [74, 85] )
        # animation.addsound( "test3c", [101] )


class obj_scene_alldrawings(obj_testpage):
    def pagename(self):
        return 'All Drawings'
    def setup(self):
        y1=50
        dy1=100
        x1=50
        dx1=100
        ss=0.2
        for c,value in enumerate(['herohead','bed','fish','hook','sun','moon']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['partnerhead','love','mailbox','mailletter','saxophone','musicnote','house','pond','bush','flower']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['villainhead','gun','bullet','tower','mountain','bug']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['bunnyhead','nightstand','alarmclock8am','cave','tree']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['elderhead','cloud','lightningbolt','rock','paper','scissors']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['sailorhead','skeletonhead','cow','sailboat','palmtree','wave']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        y1+=dy1
        for c,value in enumerate(['cake']):
            self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )
        # y1+=dy1
        # for c,value in enumerate(['partyhat','drink','coffeecup','flowervase','flame']):
        #     self.addpart( draw.obj_image(value,(x1+c*dx1,y1), scale=ss) )


class obj_scene_testdrafting(obj_testpage):
    def pagename(self):
        return 'Drafting Board'


    def textboxprevpage(self):
        pass
    def textboxnextpage(self):
        pass
    def triggerprevpage(self,controls):
        return False
    def triggernextpage(self,controls):
        return False

    def setup(self):
        self.text=['Drafting Board: ']
        #
        # Controls instructions (redraft)
        if False:
            drawing=draw.obj_drawing('instructions_controls',(640,360+100),legend='controls',shadow=(600,200))
            self.addpart(drawing)
            #
            text='or [esc] [tab] [space] [enter] w a s d [w a s d] [arrows] [mouse] [right mouse] [left mouse] [backspace]'
            text='draw erase next exit back play minigames'
            # self.textbox=draw.obj_textbox(text,(640,200),fontsize='huge')
            # self.textbox=draw.obj_textbox(text,(640,200),fontsize='huge',color=share.colors.instructions)
            # self.textbox=draw.obj_textbox(text,(640,200))
            self.textbox=draw.obj_textbox(text,(640,200),fontsize='larger',color=share.colors.instructions)
            self.textbox.snapshot('instructions_snap')
            self.addpart( self.textbox)
        #
        # Image from textbox
        # self.textbox=draw.obj_textbox('start!',(640,360),fontsize='huge')
        # self.textbox.snapshot('messagestart')
        #
        # drawing=draw.obj_drawing('mechsparks',(640,360),legend='sparks',shadow=(50,50))
        # self.addpart(drawing)
        #
        # Make main menu animations
        if True:
            # decorations
            self.text=[]
            self.addpart(draw.obj_textbox('The Book of Things',(640,80),fontsize='big'))
            # menu
            xref=640
            yref=200#+100
            dyref=55
            xleftref=False
            fontref='small'
            self.sprite_chapters=draw.obj_textbox('read',(xref,yref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_settings=draw.obj_textbox('settings',(xref,yref+dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.sprite_exit=draw.obj_textbox('exit',(xref,yref+2*dyref),fontsize=fontref,xleft=xleftref,hover=True)
            self.addpart(self.sprite_chapters)
            self.addpart(self.sprite_settings)
            self.addpart(self.sprite_exit)
        #
        # Place images: by chapters
        # self.addpart( draw.obj_imageplacer(self,'book','eraser','pen') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','herobasefish','sun','moon','bed','fish') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase','love','house','pond','bush','flower','saxophone','musicnote','sun','moon') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','villainbase','bug','tower','mountain','gun','bullet') )
        # self.addpart( draw.obj_imageplacer(self,'bunnybase','cave','tree','nightstand','alarmclock8am') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','mountain','cloud','lightningbolt','rock','paper','scissors') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','elderbase','mountain','cloud','lightningbolt','sun','moon','tree','bush') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','cow','skeletonbase','skeletonbase_sailorhat','sailboat','palmtree','wave','bush','moon') )
        #
        # Place images: by main categories
        # self.addpart( draw.obj_imageplacer(self,'heromechbase','villainmechbase','house','tree','mountain','cloud','moon') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','herobasefish','partnerbase','villainbase','bug','cow','heromechbase','villainmechbase') )
        # self.addpart( draw.obj_imageplacer(self,'bunnybase','elderbase','sailorbase','skeletonbase','skeletonbase_sailorhat') )
        # self.addpart( draw.obj_imageplacer(self,'sun','moon','mountain','cloud','tree','bush','palmtree','wave','flower') )
        # self.addpart( draw.obj_imageplacer(self,'house','pond','tower','cave','lightningbolt','sailboat') )
        # self.addpart( draw.obj_imageplacer(self,'bed','fish','saxophone','musicnote','gun','bullet','nightstand','alarmclock8am','cake') )
        #
        # Place images: by ideas
        # self.addpart( draw.obj_imageplacer(self,'fish','hook') )
        # self.addpart( draw.obj_imageplacer(self,'bed','nightstand','alarmclock8am','moon') )
        # self.addpart( draw.obj_imageplacer(self,'cake') )
        # self.addpart( draw.obj_imageplacer(self,'sailboat','wave','cloud','sun') )
        # self.addpart( draw.obj_imageplacer(self,'saxophone','musicnote','bug','partnerhead') )
        # self.addpart( draw.obj_imageplacer(self,'skeletonbase','skeletonbase_sailorhat','skeletonbase_partnerhair') )
        # self.addpart( draw.obj_imageplacer(self,'cow','palmtree','bush','moon') )
        # self.addpart( draw.obj_imageplacer(self,'tower','mountain','cloud','sun','tree','bush','herobase','herozapped') )
        # self.addpart( draw.obj_imageplacer(self,'elderbase','lightningbolt') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','sun','moon','bed','fish') )
        # self.addpart( draw.obj_imageplacer(self,'villainbase','flower','love') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase','love') )
        # self.addpart( draw.obj_imageplacer(self,'house','flower','mailbox','pond','bush') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase','cow','bush','palmtree','rock') )
        # self.addpart( draw.obj_imageplacer(self,'book','eraser','pen') )
        # self.addpart( draw.obj_imageplacer(self,'fish') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','skeletonbase','skeletonbase_sailorhat','palmtree','bush','mountain','moon') )
        # dxref=330
        # dyref=300
        # self.addpart( draw.obj_imageplacer(self,'herobase','sailorbase','skeletonbase','palmtree','wave','cloud','sailboat','mountain','bush') )
        # self.addpart( draw.obj_imageplacer(self,'bunnybase','elderbase','sailorbase') )
        # self.addpart( draw.obj_imageplacer(self,'herobase','partnerbase','love') )
        # self.addpart( draw.obj_imageplacer(self,'mountain','cloud','moon','wave') )
        # self.addpart( draw.obj_imageplacer(self,'mailletter','mailbox','flower','bush') )


        # self.addpart( draw.obj_image('partnerbase',(320,426),scale=0.54,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('musicnote',(485,278),scale=0.36,rotate=0,fliph=False,flipv=False) )
        # self.addpart( draw.obj_image('musicnote',(356,189),scale=0.22,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailbox',(1073,463),scale=1,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('bush',(772,595),scale=0.54,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(586,587),scale=0.44,rotate=0,fliph=False,flipv=False) )
        self.addpart( draw.obj_image('flower',(444,556),scale=0.39,rotate=0,fliph=True,flipv=False) )
        self.addpart( draw.obj_image('mailletter',(252,96),scale=0.39,rotate=0,fliph=False,flipv=False) )


####################################################################################################################
####################################################################################################################
# Other ideas (not in game yet, written as chapter pages)


######################

class obj_scene_testbreakfastdrinking(page.obj_chapterpage):
    def pagename(self):
        return 'Minigame breakfast drinking'
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_testbreakfastdrinking2())
    def setup(self):
        self.text=['Minigame breakfast drinking: ',\
                   'can recycle into stealth (cut rope, pickpocket, stab....) ',\
                   ]
        self.addpart( draw.obj_drawing('coffeecup',(200+10,450-50),legend='coffee cup',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('flowervase',(1280-200-10,450-50),legend='flower vase',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('drink',(640,450-50),legend='drink',shadow=(200,200)) )


class obj_scene_testbreakfastdrinking2(page.obj_chapterpage):
    def prevpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def nextpage(self):# no browsing
        share.scenemanager.switchscene(obj_scene_testmenu())
    def setup(self):
        self.text=[]
        self.world=world.obj_world_breakfastdrinking(self)
        self.addpart(self.world)


######################







####################################################################################################################
####################################################################################################################




















#

























#
