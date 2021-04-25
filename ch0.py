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
    def setup(self):
        self.text=['-----   Prologue: The Book of Things   -----   ',\
                   '\nIn the Beginning, there was Nothing. Absolutely Nothing. \nBut one Could Press [Enter] to Continue.']
        self.addpart(draw.obj_textbox('Press [Enter] to Continue',(640,500),color=share.colors.instructions))



class obj_scene_ch0p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_prologue())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())
    def setup(self):
        self.text=['One Could Press [Enter] to Continue, or [Tab] to go back. It was always like that.',\
                   '\n']
        self.addpart(draw.obj_textbox('Press [Enter] to Continue',(640,500),color=share.colors.instructions))
        self.addpart(draw.obj_textbox('Press [Tab] to Go Back',(640,600),color=share.colors.instructions))



# Scene: Draw Pen
class obj_scene_ch0p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())
    def setup(self):
        self.text=['There was going to be a pen. ',\
                   'The pen was drawn with [Left Mouse] and erased with [Backspace].',\
                   ]
        self.textkeys={'pos':(50,50),'xmin':50,'xmax':760,'linespacing':55,'fontsize':'medium'}# same as ={}
        self.addpart( draw.obj_drawing('pendraw',(940,360),legend=' Draw a Pen') )
        self.addpart(draw.obj_textbox('Hold [Left Mouse] to Draw',(420,500),color=share.colors.instructions))
        self.addpart(draw.obj_textbox('Press [Backspace] to Erase',(420,600),color=share.colors.instructions))
    def endpage(self):
        super().endpage()
        # image pen is actually 66% scale of drawing
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('pendraw',(640,360),scale=0.666))
        dispgroup1.snapshot((640,360,100,200),'pen')


class obj_scene_ch0p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())
    def setup(self):
        self.text=['The Pen liked to move around a little. it was a happy pen.',\
                   ]
        self.addpart( draw.obj_animation('penmove','pen',(640,360)) )



# Scene: Draw Eraser
class obj_scene_ch0p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())
    def setup(self):
        self.text=['Along with the pen, there was going to be an eraser.',\
                   '\nThe eraser was drawn with [Left Mouse] and erased with [Backspace]',\
                   ]
        self.addpart( draw.obj_drawing('eraserdraw',(900,450), legend='Draw an Eraser') )
        self.addpart( draw.obj_animation('penmove2','pen',(640,360)) )

    def endpage(self):
        super().endpage()
        # image eraser is actually 66% scale of drawing
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('eraserdraw',(640,360),scale=0.666))
        dispgroup1.snapshot((640,360,135,135),'eraser')

class obj_scene_ch0p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p6())
    def setup(self):
        self.text=['The Pen and Eraser looked like this, and they were very happy.',\
                   'They danced together all day.',\
                   ]
        animation1=draw.obj_animation('penmove2','pen',(640,360))
        animation2=draw.obj_animation('erasermove','eraser',(640,360),sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )



class obj_scene_ch0p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())
    def setup(self):
        self.text=['Because in the Beginning, there was Nothing, It was unclear how the pen had been drawn.',\
                   'And when there would be nothing again, it was unclear how the eraser would be erased.',\
                   ' But it didnt matter much right now because there were many more things to draw and erase.',\
                   ]
        animation1=draw.obj_animation('penmove2a','pen',(640,360))
        animation2=draw.obj_animation('erasermovea','eraser',(640,360),sync=animation1)
        self.addpart( animation1 )
        self.addpart( animation2 )



class obj_scene_ch0p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())
    def setup(self):
        self.text=['There was going to be a book. A very mysterious book [draw].',\
                   ]
        self.addpart( draw.obj_drawing('bookdraw',(640,390), legend='Draw an Open Book') )
        self.addpart( draw.obj_animation('penmove3','pen',(640-100,360)) )
        self.addpart( draw.obj_animation('erasermove3','eraser',(640+100,360)) )
    def endpage(self):
        super().endpage()
        # image book is actually 66% scale of drawing
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('bookdraw',(640,360),scale=0.666))
        dispgroup1.snapshot((640,360,210,180),'book')


class obj_scene_ch0p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch0end())
    def setup(self):
        self.text=['It was the book of things. The book of all things were all things would be.',
                   'With the help of the pen and eraser, there would be many things to write in the book.',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )


class obj_scene_ch0end(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch0p8())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch0unlocknext())
    def setup(self):
        self.text=['And so the book began...',\
                   ]
        share.datamanager.updateprogress(chapter=1)# chapter 1 becomes available

# class obj_scene_ch0unlocknext(page.obj_chapterpage):
#     def prevpage(self):
#         share.scenemanager.switchscene(obj_scene_ch0end())
#     def setup(self):
#         self.text=['You have unlocked ',('Chapter I',share.colors.instructions),\
#                     '! Open it from the menu. ',\
#                    'You can always reopen older chapters to modify them. ',\
#                   'For example, you can redraw the book, pen and eraser in the ',\
#                   ('Prologue',share.colors.instructions),'. '\
#                    '',\
#                    ]
#         share.datamanager.updateprogress(chapter=1)
#         for c,value in enumerate(['book','pen','eraser']):
#             self.addpart( draw.obj_image(value,(340+c*300,400), scale=0.5) )









####################################################################################################################
