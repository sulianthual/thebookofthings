#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The Book of Things
# Game by sul
# Started Sept 2020
#
# ideas.py: random note and ideas
#           this file not loaded
#
##########################################################
###########################################################

self.text=['Todo List:',\
           '\nx) No more advanced physics! Only simple goofy minigames',\
           '\nx) No more advanced drawings, only simple and goofy. Like same face on everything',\
           '\nx) Basis=3 chapter story: Hero, Partner, Villain. (with NO choices)',\
           '\nx) Then make alterations in Part II, Part III (Partner=He,She, Pet. Relation=love,friends,its complicated) ',\
           '\nx) Book celebrates perfect story after Chapter III, then wakes up with hangover and story is all out of place',\
           '\nx) In Subsequent Parts on can add alterations to the basic story (choose from list at beginning of the day)',\
           '\nx) Open new alterations with simple puzzles (get item from previous choice, etc...)',\
           '\nx)',\
           '\nx) Chapt 4: The Perfect Story. book of thing, pen/eraser have party to celebrate perfect story.',\
           '\nx) draw alcohol(or cocktail?) and party hat. Wakes up with hangover and story is all out of place.',\
           '\nx) hero/partner are in relationship=its complicated, partner is cheating with villain, and maybe 1 other change.',\
           '\nx) Chapt 5: Menage a Trois: explore more interactions between 3 characters. Open choice system' ,\
           '\nx)',\
           '\nx) Later on, theme changes: story is in space (draw space helmets, gravity is lowered in cutscenes)',\
           '\nx) story under the sea. story with cowboy hats, pirates... These may open unique questline (e.g. find pirate treasure)',\
           '\nx)',\
           '\nx) from chapt4 many event choices are added. Many of them lead to instant death (e.g. slapping partners ass)',
           ', and one has to restart the day. ',\
           'Another way to day is in specific minigames like fighting the villain. ',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           ]


self.text=['Mini Games Ideas:',\
           '\nx) Hunt = Arrow Parabolic Arc [A][D] then [W]',\
           '\nx) Situation? = Flappy Bird [W]',\
           '\nx) Fight = Play Pong [W][S]',\
           '\nx)',\
           '\nx) Fight = Mash [A][D]',\
           '\nx) Fight = Rock Paper Scissors (choose quickly on beat [A][W][D])',\
           '\nx) Mario level= move [A][D] and jump [W]',\
           '\nx) avoid falling boulders=[A][D]',\
           '\nx) space invaders=[A][D]',\
           '\nx) Kissing=[S] at right time for Hero/Princess moving opposite up down on left/right side of screen',\
           '\nx) Basketball=jump and shoot Holding [S] in moving hoop laterally ',\
           '\nx) Bait=guide monster to trap [WASD]. It charges straigth',\
           '\nx) Shooter=Cannon on fast rotating wheel, shoot stuff with [W]',\
           '\nx) Indiana jones ball behind=[A][D] to avoid obstacles',\
           '\nx) breakout game (pad, ball and horizontal layers of bricks)',\
           '\nx)',\
           '\nx) Chapt3: helicopter for hero/villain. flappy bird to use it and also shoots each flap.',\
           '\nx) first round boss fight hit him (he is flapping on right edge). second round he also shoots, avoid it.',\
           '\nx) bunny stomping game (ask Jing): bunnies multiply (you can stomp them, they can stomp you)',\
           '\nx) writing game: type quickly text or answer to it. What is your favorite color? ...etc...',\
           '\nx) jump/duck. Simple for bullets (increase rythm)',\
           '\nx) simple dinosaur game from google. just jump in time.',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           '\nx)',\
           ]









####################################################################################################################
####################################################################################################################
# Some drafts


# draw elements for mini game fight with helicopters
class obj_scene_ch3p9(page.obj_chapterpage):
    def prevpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p8())
    def nextpage(self):
        share.scenemanager.switchscene(obj_scene_ch3p10())
    def setup(self):
        self.text=[\
                  'This is going to be epic, said the book of things. ',\
                 ' Draw an ',('helicopter',share.colors.item),'around the ',\
                 ('hero',share.colors.hero),'\' s head and a ',\
                 ('cloud',share.colors.item),\
                 ' for a battle in the skies. ',\
                   ]

        self.addpart( draw.obj_drawing('helicopter',(400,450),legend='Helicopter (facing right)',shadow=(300,200)) )
        self.addpart( draw.obj_image('herohead',(500,450),scale=0.5) )
        self.addpart( draw.obj_drawing('cloud',(1000,450),legend='Cloud',shadow=(200,200)) )
    def endpage(self):
        super().endpage()
        # save heropter =hero+helicopter
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('helicopter',(400,450)) )
        dispgroup1.addpart('part2',draw.obj_image('herohead',(500,450),scale=0.5) )
        dispgroup1.snapshot((400,450,300,200),'heropter')
        # save villainpter=villain+helicopter
        dispgroup1=draw.obj_dispgroup((640,360))# create dispgroup
        dispgroup1.addpart('part1',draw.obj_image('helicopter',(400,450)) )
        dispgroup1.addpart('part2',draw.obj_image('villainhead',(500,450),scale=0.5) )
        dispgroup1.snapshot((400,450,300,200),'villainpter')

# Mini Game: fight in the air (like flapping)
class obj_world_airfight(obj_world):
    def setup(self):
        self.done=False# end of minigame
        self.goal=False# minigame goal reached
        # boundaries
        self.ymin=0+100
        self.ymax=720-60
        # sky background
        # self.sky=obj_grandactor(self,(640,360))
        # self.sky.addpart('img', draw.obj_image('cloud',(640,360),scale=0.5) )
        # hero (some dynamics for flapping)
        self.hero=obj_grandactor(self,(250,620))
        self.hero.addpart('img', draw.obj_image('heropter',(250,620),scale=0.3) )
        self.hero.addpart('imgr', draw.obj_image('heropter',(250,620),scale=0.3,rotate=15) )
        self.hero.dict['img'].show=True
        self.hero.dict['imgr'].show=False
        self.herodt=1# hero time increment
        self.herofy=0# hero force
        self.herov=0# hero velocity
        self.herog=1# gravity rate
        self.herod=0.1# dissipation rate
        self.heroj=20# jump rate
        self.hero.rx=50# hitbox
        self.hero.ry=30
        self.hero.r=30
        # villain (goes up and down in sin)
        self.villain=obj_grandactor(self,(1280-150,360))
        self.villain.addpart('img', draw.obj_image('villainpter',(1280-150,360),scale=0.5,fliph=True) )
        self.villainp=1# sin period
        self.villaina=0# time increment (angle )
        self.villaintimert1=160# first shot timer
        self.villaintimert2=40#80# consecutive shots
        self.villaintimershoot=tool.obj_timer(self.villaintimert1,cycle=True)#timer between shots
        self.villaintimershoot.start()
        # cannonballs
        self.cannonballs=[]# empty list
        # health bar
        self.maxherohealth=5# starting hero health
        self.herohealth=self.maxherohealth# updated one
        self.healthbar=obj_grandactor(self,(200,680))
        for i in range(self.maxherohealth):
            # self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(50+i*75,720-25),scale=0.125) )
            self.healthbar.addpart('heart_'+str(i), draw.obj_image('love',(50,720-50-i*75),scale=0.125) )
        # timer to done
        self.timerend=tool.obj_timer(80)# goal to done
    def makecannonball(self,x,y):
        cannonball=obj_grandactor(self,(x,y))
        cannonball.addpart('img', draw.obj_image('cannonball',(x,y),scale=0.5,path='premade') )
        cannonball.rx=15# hitbox
        cannonball.ry=15
        cannonball.r=15
        cannonball.speed=5#tool.randint(2,8)
        self.cannonballs.append(cannonball)
    def killcannonball(self,cannonball):
        self.cannonballs.remove(cannonball)
        cannonball.kill()
    def update(self,controls):
        super().update(controls)
        if not self.goal:
            # goal unreached state
            # hero dynamics
            self.herofy=0# force
            self.herofy += self.herog# gravity
            if controls.w and controls.wc:# flap
                self.herofy -= self.heroj
                self.herov=0# reset velocity
            # hero dynamics
            self.herov += self.herodt*(self.herofy-self.herod*self.herov)# dtv=g+flap-dv**2
            self.hero.movey(self.herodt*self.herov)# dty=v
            if self.herov<-5:
                self.hero.dict['img'].show=False
                self.hero.dict['imgr'].show=True
            else:
                self.hero.dict['img'].show=True
                self.hero.dict['imgr'].show=False
            # boundaries
            if self.hero.y>self.ymax:
                self.hero.movetoy(self.ymax)
                self.herov *= -0.5# loss from bounce
            elif self.hero.y<self.ymin:
                self.hero.movetoy(self.ymin)
                self.herov *= -0.5# losse from bounce
            # villain
            self.villain.movetoy( (1+tool.sin(self.villaina/self.villainp))/2*(self.ymax-self.ymin)+self.ymin )
            self.villaina += 1
            if self.villaina>360: self.villaina=0
            #villainshoot
            self.villaintimershoot.update()
            if self.villaintimershoot.ring:
                # faster consecutive shots after first one
                self.villaintimershoot.amount=self.villaintimert2
                self.makecannonball(self.villain.x-100,self.villain.y)
            #cannonballs
            if self.cannonballs:
                for i in self.cannonballs:
                    i.movex(-i.speed)
                    if i.x<-50: self.killcannonball(i)# disappears on left edge of screen
                    if tool.checkrectcollide(i,self.hero):# cannonball hits hero
                        self.killcannonball(i)
                        # hero looses health
                        self.herohealth -= 1
                        if self.herohealth>-1:
                            self.healthbar.dict['heart_'+str(self.herohealth)].show=False
        else:
            # goal reached state
            self.timerend.update()
            if self.timerend.ring:
                self.done=True# end of minigame




####################################################################################################################
















#
