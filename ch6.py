#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# chapter6.py: ...
#
##########################################################
###########################################################

import share
import tool
import draw
import page
import world

##########################################################
##########################################################

# Chapter VI: ...
# *CHAPTER VI

class obj_scene_chapter6(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p0())
    def triggernextpage(self,controls):
        return True



class obj_scene_ch6p0(page.obj_chapterpage):
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def setup(self):
        self.text=['-----   Chapter VI: Treasure Hunt   -----   ',\
                  '\n Sorry this chapter isnt ready yet, come back later. ',\

                   ]
        animation1=draw.obj_animation('ch1_book1','book',(640,360),record=False)
        animation2=draw.obj_animation('ch1_pen1','pen',(900,480),record=False,sync=animation1,scale=0.5)
        animation3=draw.obj_animation('ch1_eraser1','eraser',(900,480),record=False,sync=animation1,scale=0.5)
        self.addpart(animation1)
        self.addpart(animation2)
        self.addpart(animation3)


class obj_scene_ch6p1(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p0())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p2())
    def setup(self):
        self.text=[\
                   'Draw the sailor with an eyelid',\
                   ]
        self.addpart( draw.obj_image('herohead',(640,450)) )
        drawing=draw.obj_drawing('eyelid',(640,450),legend='Add an eyelid',shadow=(200,200),brush=share.brushes.bigpen)
        self.addpart( drawing)
    def endpage(self):
        super().endpage()
        # save angry head
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('herohead',(640,360),scale=1))
        dispgroup1.addpart('part2',draw.obj_image('eyelid',(640,360)))
        dispgroup1.snapshot((640,360,200,200),'headeyelid')

class obj_scene_ch6p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def setup(self):
        self.text=[\
                   'And add a sailor hat',\
                   ]
        self.addpart( draw.obj_image('headeyelid',(640,450)) )
        self.addpart( draw.obj_drawing('sailorhat',(640,450-200),shadow=(250,150)) )
        self.addpart( draw.obj_textbox('Add a sailor hat',(640,680),color=share.colors.instructions) )
    def endpage(self):
        super().endpage()
        # save angry head
        dispgroup1=draw.obj_dispgroup((640,450))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('headeyelid',(640,450),scale=1))
        dispgroup1.addpart('part2',draw.obj_image('sailorhat',(640,450-200)))
        dispgroup1.snapshot((640,325+50,250,275),'sailorhead')


class obj_scene_ch6p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def setup(self):
        self.addpart( draw.obj_image('sailorhead',(640,360)) )


class obj_scene_ch6p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())


class obj_scene_ch6p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())


class obj_scene_ch6p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())


class obj_scene_ch6p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())


class obj_scene_ch6p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())


class obj_scene_ch6p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())


class obj_scene_ch6p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())


class obj_scene_ch6p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())


class obj_scene_ch6p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())


class obj_scene_ch6p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())


class obj_scene_ch6p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())


class obj_scene_ch6p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())


class obj_scene_ch6p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())


class obj_scene_ch6p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())


class obj_scene_ch6p18(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p19())


class obj_scene_ch6p19(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())


class obj_scene_ch6p20(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p19())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())


class obj_scene_ch6p21(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p20())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())


class obj_scene_ch6p22(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p21())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())


class obj_scene_ch6p23(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p22())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())


class obj_scene_ch6p24(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p23())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())


class obj_scene_ch6p25(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p24())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())


class obj_scene_ch6p26(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p25())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())


class obj_scene_ch6p27(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p26())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())


class obj_scene_ch6p28(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p27())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p29())


class obj_scene_ch6p29(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p28())
    # def nextpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch6p30())


class obj_scene_ch6end(page.obj_chapterpage):
    # def prevpage(self):
    #     share.scenemanager.switchscene(obj_scene_ch6p28())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6unlocknext())
    def setup(self):
        self.text=['And thats it for today, said the book of things. ',
                   'But we will be back tomorrow for more! ',\
                   ]
        self.addpart( draw.obj_animation('bookmove','book',(640,360)) )



class obj_scene_ch6unlocknext(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch5end())
    def setup(self):
        self.text=['You have unlocked a new chapter, ',\
                    ('Chapter VII',share.colors.instructions),'! Access it from the menu. ',\
                   ]
        share.datamanager.updateprogress(chapter=7)# chapter 7 becomes available
