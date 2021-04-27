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
                   'The third grandmaster is a sailor, asking the hero to steal a treasure on skull island. ',\
                   'Draw the sailor head (with an eyelid)',\
                   ]
        self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2)  )
        drawing=draw.obj_drawing('sailorface',(640,450),legend='Draw the sailor (facing right)',shadow=(200,200))
        self.addpart( drawing )
    def endpage(self):
        super().endpage()
        # combine sitckhead+sailorface=sailorbaldhead
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickhead',(640,360),scale=2,path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('sailorface',(640,360)) )
        dispgroup1.snapshot((640,360,200,200),'sailorbaldhead')

class obj_scene_ch6p2(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p1())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def setup(self):
        self.text=[\
                   'And add a sailor hat',\
                   ]
        self.addpart( draw.obj_image('sailorbaldhead',(640,450)) )
        self.addpart( draw.obj_drawing('sailorhat',(640,450-200),shadow=(250,150)) )
        self.addpart( draw.obj_textbox('Add a sailor hat',(640,680),color=share.colors.instructions) )
    def endpage(self):
        super().endpage()
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



class obj_scene_ch6p3(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p2())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def setup(self):
        self.text=['This is what the sailor looks like. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','sailorbase',(360,360),record=True))
        self.addpart(draw.obj_animation('ch1_hero1','herobase',(360+200,360),record=True))


class obj_scene_ch6p4(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p3())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())
    def setup(self):
        self.text=[\
                   'The sailor lives on the beach. Draw palm tree and wave. ',\
                   ]
        self.addpart( draw.obj_drawing('palmtree',(340,450),legend='Palm Tree',shadow=(200,200)) )
        self.addpart( draw.obj_drawing('wave',(940,450),legend='Wave',shadow=(200,100)) )

class obj_scene_ch6p5(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p4())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def setup(self):
        self.text=[\
                   'Sailor says: well this is embarassing, I lost my boat. ',\
                   'Get me some wood to buil one, 10 logs.',\
                   ]


class obj_scene_ch6p6(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p5())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=[\
                   'Chop some trees to build a boat, then meet the sailor on the beach.',\
                   ]
        # self.world=world.obj_world_travel(self,start='home',goal='nowhere',chapter=6)
        self.world=world.obj_world_travel(self,start='home',goal='beach',chapter=6,minigame='logs',sailorwait=True)
        self.addpart(self.world)

class obj_scene_ch6p7(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p6())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def setup(self):
        self.text=[\
                   'Draw the sailor ship ',\
                   ]
        self.addpart( draw.obj_drawing('sailboat',(640,450-100),legend='Saiboat (facing right)',shadow=(300,300)) )


class obj_scene_ch6p8(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p7())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def setup(self):
        self.text=[\
                   'The inhabitants of skull island are spooky skeletons. ',\
                   'Draw  a skull. ',\
                   ]
        # self.addpart( draw.obj_image('stickhead',(640,450),path='premade',scale=2)  )
        self.addpart( draw.obj_drawing('skeletonhead',(640,450),legend='Skull (Facing Right)',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        # combine skeletonhead+stickbody = skeletonbase
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        # dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
        # dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
        # dispgroup1.addpart('part6',draw.obj_image('scar',(640,200),scale=0.5) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase')
        # skeleton with hair
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        dispgroup1.addpart('part4',draw.obj_image('partnerhair',(640,200)) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_partnerhair')
        # skeleton with sailor hat
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('stickbody',(640,460),path='premade') )
        dispgroup1.addpart('part2',draw.obj_image('stickheadnocontours',(640,200),path='premade') )
        dispgroup1.addpart('part3',draw.obj_image('skeletonhead',(640,200),scale=0.5) )
        dispgroup1.addpart('part5',draw.obj_image('sailorhat',(640,200-100),scale=0.5) )
        dispgroup1.snapshot((640,360-15,200,300+15),'skeletonbase_sailorhat')


class obj_scene_ch6p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def setup(self):
        self.text=['This is what the skeletons looks like. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase',(360,360)))
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase_partnerhair',(360-300,360)))
        self.addpart(draw.obj_animation('ch1_hero1','skeletonbase_sailorhat',(360+300,360)))

class obj_scene_ch6p10(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p9())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def setup(self):
        self.text=[\
                   'Sail to skull island with the boat',\
                   ]
        self.world=world.obj_world_travel(self,start='beach',goal='island',boat=True,chapter=6,sailor=True)
        self.addpart(self.world)

class obj_scene_ch6p11(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p10())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def setup(self):
        self.text=[\
                   'Wait until night then infiltrate and steal the treasure. ',\
                   ]


class obj_scene_ch6p12(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p11())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def setup(self):
        self.text=[\
                   'stealth minigame... ',\
                   ]

class obj_scene_ch6p13(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p12())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def setup(self):
        self.text=[\
                   'The treasure is a cow that provides superior milk with a calcium boost ',\
                   ]
        self.addpart( draw.obj_drawing('cow',(640,450),legend='Cow (Facing Right)',shadow=(300,200),brush=share.brushes.pen6) )
    def endpage(self):
        super().endpage()
        # combine herobase+cow=heroridecow
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('herobase',(640,360-100),scale=0.5) )
        dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecow')
        # combine herobase+cow=heroridecow
        dispgroup1=draw.obj_dispgroup((640,360))
        dispgroup1.addpart('part1',draw.obj_image('herobaseangry',(640,360-100),scale=0.5) )
        dispgroup1.addpart('part2',draw.obj_image('cow',(640,360+100)) )
        dispgroup1.snapshot((640,360+25,300,300-25),'heroridecowangry')

class obj_scene_ch6p14(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p13())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def setup(self):
        self.text=[\
                   'Alert, said the skeletons. Someone is stealing our cow. And a chase began... ',\
                  'Quick said the sailor, come reach the boat. ride the cow. ',\
                  'This is what the hero riding the cow looks like. ',\
                   ]
        self.addpart(draw.obj_animation('ch1_hero1','heroridecow',(360,360)))
        self.addpart(draw.obj_animation('ch1_hero1','heroridecowangry',(360+300,360)))
        # self.addpart(draw.obj_image('heroridecow',(640,360)) )

class obj_scene_ch6p15(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p14())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def setup(self):
        self.text=['cow minigame tutorial: avoid rocks and palm trees',\
                   ]
        self.world=world.obj_world_ridecow(self)
        self.addpart(self.world)
        self.world.tutorial=True# is world tutorial


class obj_scene_ch6p16(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p15())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p17())
    def triggernextpage(self,controls):
        return (share.devmode and controls.enter and controls.enterc) or self.world.done
    def setup(self):
        self.text=['cow minigame',\
                   ]
        self.world=world.obj_world_ridecow(self)
        self.addpart(self.world)

class obj_scene_ch6p17(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p16())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch6p18())
    def setup(self):
        self.text=[\
                   'go back home. Leave the sailor in front of mailbox. He says can keep the ship. ',\
                  'And last part of password is probably "sailor" ',\
                 'Finish day (diner, serenade, kiss, go tosleep) happy because will save partner the next day ',\
                   ]

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
