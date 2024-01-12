# -- coding: utf-8 --

   #T - Техтура земли
        #s - stoune
        #- - zemlya
        #F-FAKE PLATFORMS/SHIP
        #L- LOVUSKA
        #M - MONETKA
        #N - NEXT
        #W-WATER
        #B - BUTTON
        #P - TELEPORT
        #A - ART KILL
        #1 - полный снег
        #2 - снег только сверху
        
import pygame
from pygame import *
from pygame.locals import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (0,0,0)
#ICON_DIR = os.path.dirname(file) #  Полный путь к каталогу с файлами
"""Main class for create block"""
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("forgame/prozrscnii.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/prozrscnii.png")

class BlockFake(Platform):
    def __init__(self, x, y,lvl,stage):
        Platform.__init__(self, x, y)
        if lvl == 1:
            if stage == 1:
                self.image = image.load("forgame/prozrscnii.png")
            
        elif lvl == 2:
            if stage == 1:
                self.image = image.load("forgame/bambuk.jpg")
            elif stage == 2:
                self.image = image.load("forgame/bambuk.png")
                
        elif lvl == 3:
            if stage == 1:
                self.image = image.load("forgame/tree.jpg")
            elif stage == 2:
                self.image = image.load("forgame/groundWithGrass.png")
            elif stage == 3:
                self.image = image.load('forgame/barrel.png')
        elif lvl == 4:
            if stage == 1:
                self.image = image.load("forgame/col.jpg")
            elif stage == 2:
                self.image = image.load("forgame/col.jpg")
            elif stage == 3:
                self.image = image.load('forgame/col.jpg')
        elif lvl == 5:
            if stage == 1:
                self.image = image.load("forgame/fullsnow.jpg")
        elif lvl == 6:
            self.image = image.load("forgame/lava.jpg")

                
                
            
###############2LVL
class BlockBambuck1(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/bambuk.jpg")
        
class BlockBambuck2(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/bambuk.png")
        
        
#####################3LVL
class BlockBarrel(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/barrel.png")
class BlockTree(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/tree.jpg")
    
######################4LVL 
class BlockCol(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/col.jpg")


#######

######################5LVL
class BlockIce(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("forgame/ice.jpg")
        
class BlockSnow(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("forgame/snow.jpg")

class BlockFullSnow(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("forgame/fullsnow.jpg")
    
############################



########################6LVL

class BlockStone(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image = image.load("forgame/stone1.png")


class BlockFire(Platform):  # Предполагается, что Water также унаследован от Platform
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/lava.jpg")

###########################

class BlockWater(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/water.png")
        
class BlockMonetka(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/monetka.png")
        
class BlockLiana(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/liana.png")

class BlockTrapStatic(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/Blink.png")
class BlockRunY(Platform):
    def __init__(self, x, y, stageUP,stageDOWN,speed = 1):
        Platform.__init__(self, x, y)
        self.speed = speed
        self.direction = 1
        self.start_y = y
        self.image = image.load("forgame/m_runblock.png")
        self.stageUP = stageUP
        self.stageDOWN = stageDOWN
    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.bottom >= self.start_y + self.stageDOWN:
            self.direction *= -1
        elif self.rect.top <= self.start_y - self.stageUP:
            self.direction  *= -1

class BlockRunX(Platform):
    def __init__(self, x, y, stageLeft, stageRight, speed = 1):
        Platform.__init__(self, x, y)
        self.speed = speed
        self.direction = 1
        self.start_x = x
        self.stageLeft = stageLeft
        self.stageRight = stageRight
        self.image = image.load("forgame/m_runblock.png")
    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= self.start_x + self.stageRight or self.rect.left <= self.start_x - self.stageLeft:
            self.direction *= -1

class BlockTeleport(Platform):
    def __init__(self, x, y, teleport_x, teleport_y):
        Platform.__init__(self, x, y)
        self.teleport_x = teleport_x
        self.teleport_y = teleport_y

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            # Если произошла коллизия с персонажем, телепортируем его
            player.rect.x = self.teleport_x
            player.rect.y = self.teleport_y
    
class TrapRunX(Platform):
    def __init__(self, x, y, stageLeft, stageRight, speed = 5):
        Platform.__init__(self, x, y)
        self.speed = speed
        self.direction = 1
        self.start_x = x
        self.stageLeft = stageLeft
        self.stageRight = stageRight
        self.image = image.load("forgame/pila.png")
    def update(self):
        self.rect.x += self.speed*self.direction
        if self.rect.right >= self.start_x + self.stageRight or self.rect.left <= self.start_x - self.stageLeft:
            self.direction *= -1
class TrapRunY(Platform):
    def __init__(self, x, y, stageUP,stageDOWN,lvl):
        Platform.__init__(self, x, y)
        self.direction = 1
        self.start_y = y
        if lvl == 5:
            self.image = image.load("forgame/snegovik.png")
            self.speed = 1
        else:
            self.speed = 5
            self.image = image.load("forgame/pila.png")
        self.stageUP = stageUP
        self.stageDOWN = stageDOWN
    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.bottom >= self.start_y + self.stageDOWN or self.rect.top <= self.start_y - self.stageUP:
            self.direction *= -1
class BlinkRunY(Platform):
    """blinkruny"""
    def __init__(self, x, y,lvl,stage):
        Platform.__init__(self, x, y)
        # global blinBool1 
        self.image = image.load("forgame/Blink.png")  # Загрузите изображение для вашей ловушки
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.speed = 1
        self.start_y = y
        self.flag_speed = False  # Начальная позиция по оси Y
        self.level = lvl
        self.stage = stage
    def update(self):
        """update"""
        if self.level == 1:
            if self.rect.y <= 0 or bool(self.flag_speed) is True:
                self.flag_speed = True
                self.rect.y += self.speed
                if self.rect.y == 790:
                    self.flag_speed = False
            elif  not self.flag_speed:
                self.rect.y -= self.speed
        elif self.level == 5:
            # if self.stage == 1:
            #     if self.rect.y <= 200 or bool(self.flag_speed) is True:
            #         self.flag_speed = True
            #         self.rect.y += self.speed
            #         if self.rect.y == 500:
            #             self.flag_speed = False
            #     elif  not self.flag_speed:
            #         self.rect.y -= self.speed
            if self.stage == 1:
                if self.rect.y <= 550 or bool(self.flag_speed) is True:
                    self.flag_speed = True
                    self.rect.y += self.speed
                    if self.rect.y == 700:
                        self.flag_speed = False
                elif  not self.flag_speed:
                    self.rect.y -= self.speed

class Block1Level(Platform):
    """block level"""
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("forgame/block1lvl.png")

class MobX(Platform):
    def __init__(self, x, y, stageLeft, stageRight,lvl ,speed = 2):
        Platform.__init__(self, x, y)
        self.speed = speed
        self.direction = 1
        self.start_x = x
        self.stageLeft = stageLeft
        self.stageRight = stageRight
        self.level = lvl 
        if self.level == 6:
            self.image = image.load("forgame/skelet.png")
        elif self.level == 3:
            self.image = image.load('forgame/pirat.png')
        elif self.level == 4:
            self.image = image.load("forgame/ninja.png")
    def update(self):
        self.rect.x += self.speed*self.direction
        if self.level == 4:
            if self.rect.right >= self.start_x + self.stageRight or self.rect.left <= self.start_x - self.stageLeft:
                self.direction *= -1
                if self.direction == -1:
                    self.image = image.load("forgame/ninjal.png")
                else:
                    self.image = image.load("forgame/ninja.png")
                    
        elif self.level == 6:
            if self.rect.right >= self.start_x + self.stageRight or self.rect.left <= self.start_x - self.stageLeft:
                self.direction *= -1
                if self.direction == -1:
                    self.image = image.load("forgame/skeletr.png")
                else:
                    self.image = image.load("forgame/skelet.png")
