# -- coding: utf-8 --

from pygame import *
import block
import windowGame
import os
from pygame import font 
import random
import time
import pygame.time  # Import the pygame.time module


MOVE_SPEED = 6
WIDTH = 32
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.5 # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.3 # скорость смены кадров
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами



ANIMATION_RIGHT = [('forgame/MainHeroR.png'), 
            ('forgame/MainHeroStepR.png'), 
            ('forgame/MainHeroJump.png'),
            ('forgame/MainHeroR.png'), 
            ('forgame/MainHeroStepR.png')]
ANIMATION_LEFT = [('forgame/MainHeroL.png'), 
            ('forgame/MainHeroStepLeft.png'),
            ('forgame/MainHeroJumpLeft.png'),
            ('forgame/MainHeroL.png'), 
            ('forgame/MainHeroStepLeft.png')]
ANIMATION_JUMP_LEFT = [('forgame/MainHeroJumpLeft.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('forgame/MainHeroJump.png', 0.1)]
ANIMATION_JUMP = [('forgame/MainHeroJump.png', 0.1)]
ANIMATION_STAY = [('forgame/MainHeroR.png', 0.1)]

class Player(sprite.Sprite):
    def __init__(self, x, y,levelcount):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.start_x = x 
        self.start_y = y

        self.start2x = 100
        self.start2y = 100

        self.start3x = 100
        self.start3y = 500

        self.start4x = 50
        self.start4y = 150

        self.start5x = 50
        self.start5y = 150

        self.start6x = 155
        self.start6y = 155
        self.yvel = 0 # скорость вертикального перемещения
        self.on_ground = False # На земле ли я?
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным

        self.level = 1

        #Анимация движения вправо
        bolt_anim = []
        for anim in ANIMATION_RIGHT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_right = windowGame.PygAnimation(bolt_anim)
        self.bolt_anim_right.play()
        #Анимация движения влево
        bolt_anim = []
        for anim in ANIMATION_LEFT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_left = windowGame.PygAnimation(bolt_anim)
        self.bolt_anim_left.play()

        self.bolt_anim_stay = windowGame.PygAnimation(ANIMATION_STAY)
        self.bolt_anim_stay.play()
        self.bolt_anim_stay.blit(self.image, (0, 0)) # По-умолчанию, стоим

        self.bolt_anim_jump_left= windowGame.PygAnimation(ANIMATION_JUMP_LEFT)
        self.bolt_anim_jump_left.play()

        self.bolt_anim_jump_right= windowGame.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.bolt_anim_jump_right.play()

        self.bolt_anim_jump= windowGame.PygAnimation(ANIMATION_JUMP)
        self.bolt_anim_jump.play()

        self.last_direction_change_time = time.time()
        self.direction_change_interval = 0.08 # Adjust the interval as needed (in seconds)

    def update(self, left, right, up, platforms, waters,coins,lians,levelcount,teleports,ices):
        """update"""
        print(f"Player: ({self.rect.x}, {self.rect.y})")
        for ice in ices:
            if sprite.collide_rect(self,ice):
                self.speed_up()


        for tp in teleports:
            if sprite.collide_rect(self,tp):
                self.teleporting(tp.teleport_x,tp.teleport_y)
        for coin in coins:
            print(f"Coin: ({coin.rect.x}, {coin.rect.y})")
            print(f"remainder: ({len(coins)})")

            if sprite.collide_rect(self, coin):
                coins.remove(coin)
                coin.image.set_alpha(0)

                if len(coins) == 0:
                    print(f"Moving TOTOTOTO level {self.level}")
                    levelcount += 1
                    print(f"lvl: ({levelcount})")
        # print(f"self.xvel: {self.xvel}")
        for water in waters:
            if sprite.collide_rect(self, water):
                self.slow_down()
                if up:  # Проверяем, нажата ли клавиша "вверх" (пробел)
                    self.float_up()
        for lian in lians:
            if sprite.collide_rect(self, lian):
                self.slow_down()
                if up:  # Проверяем, нажата ли клавиша "вверх" (пробел)
                    self.float_up()


        if up:
            if self.on_ground: # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.bolt_anim_jump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
            self.image.fill(Color(COLOR))
            if up: # для прыжка влево есть отдельная анимация
                self.bolt_anim_jump_left.blit(self.image, (0, 0))
            else:
                self.bolt_anim_left.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.bolt_anim_jump_right.blit(self.image, (0, 0))
            else:
                self.bolt_anim_right.blit(self.image, (0, 0))

        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.bolt_anim_stay.blit(self.image, (0, 0))


        if not self.on_ground:
            self.yvel +=  GRAVITY

        self.on_ground = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms,levelcount,left,right)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms,levelcount,left,right)

    def collide(self, xvel, yvel, platforms,level,left,right):
        """collide"""
        on_ice = False
        for p in platforms:
            if sprite.collide_rect(self, p):
                if isinstance(p, block.BlockDie) or isinstance(p, block.BlockTrapStatic):
                    self.die(levelcount=level)
                elif isinstance(p,block.BlockFire) or isinstance(p,block.TrapRunX):
                    self.die(levelcount=level)
                elif isinstance(p,block.TrapRunY) or isinstance(p,block.BlinkRunY):
                    self.die(levelcount=level)
                elif isinstance(p,block.MobX):
                    self.die(levelcount=level)
                elif isinstance(p, block.BlockRunY):
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.on_ground = True
                        self.yvel = 0
                elif isinstance(p, block.BlockIce):
                    on_ice = True
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.xvel = 5
                    elif xvel < 0:
                        self.rect.left = p.rect.right
                        self.xvel = -5
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.on_ground = True
                        self.yvel = 0
                    elif yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
                else:
                    if xvel > 0:                      # если движется вправо
                        self.rect.right = p.rect.left # то не движется вправо

                    if xvel < 0:                      # если движется влево
                        self.rect.left = p.rect.right # то не движется влево

                    if yvel > 0:                      # если падает вниз
                        self.rect.bottom = p.rect.top # то не падает вниз
                        self.on_ground = True          # и становится на что-то твердое
                        self.yvel = 0                 # и энергия падения пропадает

                    if yvel < 0:                      # если движется вверх
                        self.rect.top = p.rect.bottom # то не движется вверх
                        self.yvel = 0                 # и энергия прыжка пропадает
            if not (left or right):
                if on_ice:
                    current_time = time.time()
                    if current_time-self.last_direction_change_time>=self.direction_change_interval:
                        self.handle_ice_movement(random.choice([10, -10]))
                        self.last_direction_change_time = current_time
                else:
                    self.xvel = 0
    def handle_ice_movement(self, x_velocity):
        """ice_movement"""
        self.xvel = x_velocity
        
    def teleporting(self, go_x, go_y):
        """teleport"""
        self.rect.x = go_x
        self.rect.y = go_y
    def die(self,levelcount):
        """die"""
        pygame.time.wait(10)
        if levelcount == 1:
            self.teleporting(self.start_x, self.start_y) # перемещаемся в начальные координаты
        elif levelcount == 2:
            self.teleporting(self.start2x,self.start2y)
        elif levelcount == 3:
            self.teleporting(self.start3x,self.start3y)
        elif levelcount == 4:
            self.teleporting(self.start4x,self.start4y)
        elif levelcount == 5:
            self.teleporting(self.start2x,self.start2y)
        elif levelcount == 6:
            self.teleporting(self.start6x,self.start6y)
    def slow_down(self):
        """slow down"""
        self.xvel /= 2
        self.yvel /= 20

    def speed_up(self):
        """speed up"""
        self.xvel *= 50
    def float_up(self):
        """float up"""
        # Добавляем вертикальную скорость для всплытия
        self.yvel = -JUMP_POWER * 0.2  # Вы можете настроить коэффициент под свои нужды
