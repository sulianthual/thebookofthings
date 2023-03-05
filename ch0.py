#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter0.py: prologue
#
##########################################################
##########################################################

import share
import tool
import draw
import page
import world

##########################################################
##########################################################

# Chapter: Game Prologue
# *PROLOGUE
class obj_scene_prologue(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p1())
    def soundnextpage(self):
        pass# no sound
    def setup(self):
        share.datamanager.setbookmark('ch0_start')
        self.text=[\
                    '-----   Prologue: The book of things   -----   ',\
                    '\nIn the beginning, there was nothing. Absolutely nothing.',\
                    'But one could press [next] to continue.'
                    ]
        #
        self.addpart( draw.obj_music('tension') )


class obj_scene_ch0p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_prologue())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())
    def setup(self):
        self.text=['One could press [next] to continue. ',\
        'One could also press [esc] to go back to the main menu. ']
        # self.addpart(draw.obj_textbox('press [next] to continue',(640,400),color=share.colors.instructions))
        # self.addpart(draw.obj_textbox('press [back] to go back',(640,500),color=share.colors.instructions))
        # self.addpart(draw.obj_textbox('press [esc] to return to menu',(640,600),color=share.colors.instructions))
        #
        self.sound=draw.obj_sound('unlock')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


# Scene: Draw Pen
class obj_scene_ch0p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())
    def setup(self):
        share.datamanager.setbookmark('ch0_drawpen')
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempo2='['+share.datamanager.controlname('mouse2')+']'
        self.text=['There was going to be a pen. ',\
                   'The pen was drawn with '+tempo1+' and erased with '+tempo2+'. ',\
                   'It didnt have to follow the grayed area exactly. ',\
                  '\n ',\
                   ]# last line for [back][next] adjustment
        self.textkeys={'pos':(50,20),'xmin':50,'xmax':760,'linespacing':55,'fontsize':'medium'}# same as ={}
        self.addpart(draw.obj_drawing('pendraw',(940,360),legend=' Draw a Pen') )
        self.addpart(draw.obj_textbox('hold '+tempo1+' to draw',(420,400),color=share.colors.instructions))
        self.addpart(draw.obj_textbox('press '+tempo2+' to erase',(420,500),color=share.colors.instructions))
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())
    def setup(self):
        self.text=['The Pen liked to move around a little. it was a happy pen.',\
                   ]
        animation=draw.obj_animation('penmove','pen',(640,360))
        self.addpart( animation )
        # self.addpart( draw.obj_soundplacer(animation,'pen') )
        animation.addsound( "pen", [12, 113, 132],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


# Scene: Draw Eraser
class obj_scene_ch0p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())
    def setup(self):
        share.datamanager.setbookmark('ch0_draweraser')
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempo2='['+share.datamanager.controlname('mouse2')+']'
        self.text=['Along with the pen, there was going to be an eraser.',\
                   'The eraser was drawn with '+tempo1+' and erased with '+tempo2+'',\
                   ]
        self.addpart( draw.obj_drawing('eraserdraw',(900,450), legend='Draw an Eraser') )
        self.addpart( draw.obj_animation('penmove2','pen',(640,360)) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())
    def setup(self):
        self.text=['The pen and eraser looked like this, and they were very happy.',\
                   'They danced together all day.',\
                   ]
        animation=draw.obj_animation('penmove2','pen',(640,360))
        animation2=draw.obj_animation('erasermove','eraser',(640,360),sync=animation)
        self.addpart( animation )
        self.addpart( animation2 )
        # self.addpart( draw.obj_soundplacer(animation,'pen','eraser') )
        animation.addsound( "pen", [22, 49] )
        animation.addsound( "eraser", [75],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


# class obj_scene_ch0p6(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch0p5())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch0p7())
#     def setup(self):
#         self.text=['Because in the beginning, there was nothing, It was unclear how the pen had been drawn.',\
#                    'And when there would be nothing again, it was unclear how the eraser would be erased.',\
#                    ' But it didnt matter much right now because there were many more things to draw and erase.',\
#                    ]
#         animation=draw.obj_animation('penmove2a','pen',(640,360))
#         animation2=draw.obj_animation('erasermovea','eraser',(640,360),sync=animation)
#         self.addpart( animation )
#         self.addpart( animation2 )
#         #
#         animation.addsound( "pen", [26, 99] )
#         animation.addsound( "eraser", [236, 311],skip=1 )
#         #
#         self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())
    def setup(self):
        share.datamanager.setbookmark('ch0_drawbook')
        self.text=['There was going to be a book. A very mysterious book.',\
                   ]
        self.addpart( draw.obj_drawing('bookdraw',(640,390), legend='Draw an Open Book') )
        self.addpart( draw.obj_animation('penmove3','pen',(640-100,360)) )
        self.addpart( draw.obj_animation('erasermove3','eraser',(640+100,360)) )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p9())
    def setup(self):
        self.text=['It was the book of things. The book of all things where all things would be.',
                   'With the help of the pen and eraser, there would be many things to write in the book.',\
                   ]
        animation1=draw.obj_animation('bookmove','book',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [270] )
        animation1.addsound( "book1", [200],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p10())
    def setup(self):
        self.text=['And so the book began...']
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p11())
    def textboxset(self):
        self.textboxopt={'xy':(640,650),'text':'[confirm]','align':'center'}
    def setup(self):
        share.datamanager.setbookmark('ch0_meetbook')
        tempo1='['+share.datamanager.controlname('mouse1')+']'
        tempom='['+share.datamanager.controlname('mouse')+']'
        tempok='['+share.datamanager.controlname('keyboard')+']'
        self.text=['Well hello, said the book of things, ',\
                'very nice to meet you. ',\
                    'How are you feeling today. ',\
                 ]
        self.addpart( draw.obj_textbox('select the box with '+tempo1+' and type a mood with the '+tempok+'. ',(50,220),color=share.colors.instructions,xleft=True) )
        self.addpart( draw.obj_textinput('playermood',30,(640,330), legend='write down your mood') )
        self.addpart( draw.obj_textbox('select an option with '+tempo1,(50,450),color=share.colors.instructions,xleft=True) )
        #
        yref=560
        self.addpart( draw.obj_textbox('how much: ',(180,yref)) )
        textchoice=draw.obj_textchoice('playermoodhowmuch')
        textchoice.addchoice('1. a bit','a bit',(440,yref))
        textchoice.addchoice('2. kinda','kinda',(640,yref))
        textchoice.addchoice('3. very','very',(840,yref))
        textchoice.addchoice('4. sooooo','sooooo',(1040,yref))
        self.addpart( textchoice )
        #
        animation1=draw.obj_animation('ch0_bookinstructions','book',(640,360-300),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch0_bookinstructionsmark','exclamationmark',(640,360-300),record=True,sync=animation1,path='data/premade')
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        # self.addpart(draw.obj_animation('ch1_pen2','pen',(1180,400),record=False,scale=0.5))
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [28] )
        animation1.addsound( "book2", [170],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p13())
    def setup(self):
        self.text=[\
                    'Very nice to meet you, ',\
                    'said the book of things, ',\
                    'I am also feeling ',\
                    ('{playermoodhowmuch}',share.colors.player),' ',\
                    ('{playermood}',share.colors.player),'! ',\
                    ]
        animation1=draw.obj_animation('bookmove','book',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [270] )
        animation1.addsound( "book1", [200],skip=1 )
        #
        self.sound=draw.obj_sound('bookscene')
        self.addpart(self.sound)
        self.sound.play()
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p13b())
    def setup(self):
        share.datamanager.setbookmark('ch0_checkcontrols')
        self.doazertymode=share.datamanager.doazerty# True/False
        if self.doazertymode:
            tempo='azerty'
        else:
            tempo='qwerty'
        self.text=[\
                    'These are the game controls. ',\
                    'Keyboard mode is currently ',\
                    (tempo,share.colors.red),\
                    ' (if you have a french keyboard go to the settings and select azerty mode). ',\
                   ]
        #
        # Game controls instructions
        self.addpart( draw.obj_image('instructions_controls_domousebrowse',(640,420),path='data/premade') )
        self.addpart( draw.obj_textbox('[left mouse]',(927,311),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[right mouse]',(1136,252),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[space]',(564,533),color=share.colors.black) )

        if self.doazertymode:
            self.addpart( draw.obj_textbox('[zqsd]',(430,260),color=share.colors.red) )
        else:
            self.addpart( draw.obj_textbox('[wasd]',(430,260),color=share.colors.red) )
        self.addpart( draw.obj_textbox(   'or',(508,267),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[arrows]',(555,320),color=share.colors.black) )
        self.addpart( draw.obj_textbox('[esc]',(153,249),color=share.colors.black) )
        #
        self.addpart( draw.obj_textbox('draw',(930,370),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('select',(930,437),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('erase',(1174,305),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('play',(501,438),color=share.colors.instructions,fontsize='larger') )
        self.addpart( draw.obj_textbox('exit',(136,325),color=share.colors.instructions,fontsize='larger') )

        #
        animation1=draw.obj_animation('ch0_bookinstructions','book',(640,360),record=False)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch0_bookinstructionsmark','exclamationmark',(640,360),record=False,sync=animation1,path='data/premade')
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "book1", [28] )
        animation1.addsound( "book2", [170],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )


class obj_scene_ch0p13b(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0end())
    def setup(self):
        share.datamanager.setbookmark('ch0_drawingtips')
        # self.text=[\
        #             'There are still many ',\
        #             ('drawings',share.colors.red),\
        #             ' to do: ',\
        #             'you dont need to draw them perfectly, and you dont need to fill up all the drawing area. ',\
        #             'But remember, everything is up to you! This story will be whatever you make of it.  ',\
        #             ]
        #
        self.text=[\
                    'When ',('drawing',share.colors.red),\
                    ' it is better not to go near the edges, but it is entirely up to you. ',\
                    'Just draw what you feel like. ',\
                    ]
        ydr=420
        xdr1=640-200
        xdr2=640+200
        # self.addpart( draw.obj_image('stickbase',(640,390),scale=0.5,path='data/premade') )
        self.addpart( draw.obj_image('drawtip_good',(xdr1,ydr),scale=0.5,path='data/premade') )
        drawing1=draw.obj_drawing('drawtip1',(xdr1,ydr),legend='Good',shadow=(150,200))
        drawing1.brush.makebrush(share.brushes.emptypen)# cant draw
        self.addpart(drawing1)
        #
        self.addpart( draw.obj_image('drawtip_bad',(xdr2,ydr),scale=0.5,path='data/premade') )
        drawing1=draw.obj_drawing('drawtip2',(xdr2,ydr),legend='Not So Good',shadow=(150,200))
        drawing1.brush.makebrush(share.brushes.emptypen)# cant draw
        self.addpart(drawing1)
        #
        animation1=draw.obj_animation('ch0_bookinstructions','book',(640-1040,360),record=False,imgfliph=True)
        self.addpart( animation1 )
        animation2=draw.obj_animation('ch0_bookinstructionsmark','exclamationmark',(640-1040,360),imgfliph=True,sync=animation1,path='data/premade')
        animation2.addimage('empty',path='data/premade')
        self.addpart( animation2 )
        #
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [270] )
        animation1.addsound( "book1", [200],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )



# class obj_scene_ch0p14(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch0p13b())
#     def nextpage(self):
#         share.scenemanager.switchscene(obj_scene_ch0end())
#     def setup(self):
#         share.datamanager.setbookmark('ch0_learnbrowse')
#         self.text=[\
#                     'You can return to any previous drawing from the main menu, ',\
#                     'you can always go back from the main menu with [esc]. ',\
#                     ]
#         animation1=draw.obj_animation('ch5whatbook1','book',(640,360),record=False)
#         self.addpart( animation1 )
#         # self.addpart(draw.obj_textbox('press [esc] to return to the main menu',(640,200),color=share.colors.instructions))
#         #
#         # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
#         animation1.addsound( "book1", [13] )
#         animation1.addsound( "book2", [170] )
#         animation1.addsound( "book3", [155],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch0end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p13b())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0unlocknext())
    def setup(self):
        self.text=['That is all for now, lets get started! ',
                   ]
        animation1=draw.obj_animation('bookmove','book',(640,360),record=False)
        self.addpart( animation1 )
        #
        # self.addpart( draw.obj_soundplacer(animation1,'book1','book2','book3') )
        animation1.addsound( "bookscene", [1] )
        animation1.addsound( "book3", [107] )
        animation1.addsound( "book2", [270] )
        animation1.addsound( "book1", [249],skip=1 )
        #
        self.addpart( draw.obj_music('piano') )

class obj_scene_ch0unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0end())
    def setup(self):
        share.datamanager.setbookmark('ch0_endunlock')
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter I',share.colors.instructions),'! ',\
                    'You can access it from the ',\
                    ('main menu',share.colors.instructions),'.'\
                   ]
        share.datamanager.updateprogress(chapter=1)# chapter 1 becomes available
        #
        sound1=draw.obj_sound('unlock')
        self.addpart(sound1)
        sound1.play()
        #
        self.addpart( draw.obj_music('piano') )





####################################################################################################################
