import pygame
import os

from LDEngine.app.sprites.enemy.enemy import Enemy
from app.Sprites.enemy.bullet import FireBullet
from LDEngine.app.tools.animation import Animation

from LDEngine.app.settings import *
import random


class ScheduledShooter(Enemy):
    def __init__(self, x, y, theMap=None, direction="Left"):
        super().__init__(x, y, os.path.join('Sprite', 'trap.png'))

        self.name = "scheduledShooter"

        self.imageEnemy = pygame.image.load(os.path.join('Sprite', 'trap.png'))

        self.frames = [self.imageEnemy]
        self.animation = Animation(self,self.frames,20)

        self.rect = self.imageEnemy.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0
        self.speedy = 0

        self.theMap = theMap

        self.setDirection(direction)

        self.isGravityApplied = True
        self.isCollisionApplied = True

        self.imageIterShoot = random.randint(10,70)
        self.imageWaitNextShoot = 80

        self.dictProperties = {'direction': self.setDirection}

    def setDirection(self, direction):
        if direction is "Right":
            self.direction = "Right"
        else:
            self.direction = "Left"

    def setTheMap(self, theMap):
        self.theMap = theMap

    def update(self):

        self.animation.update(self)
        self.updateCollisionMask()

        self.imageIterShoot += 1
        if self.imageIterShoot > self.imageWaitNextShoot:

            if self.direction == "Right":
                bullet = FireBullet(self.rect.x + self.rect.width + 1, self.rect.centery, RIGHT, False)
            elif self.direction == "Left":
                bullet = FireBullet(self.rect.x - 10, self.rect.centery, LEFT, False)
            elif self.direction == "Up":
                bullet = FireBullet(self.rect.x - 10, self.rect.centery, UP, False)
            else:
                bullet = FireBullet(self.rect.x - 10, self.rect.centery, DOWN, False)

            self.theMap.camera.add(bullet)
            self.theMap.allSprites.add(bullet)
            self.theMap.bulletGroup.add(bullet)

            self.imageIterShoot = 0


    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def dead(self):
        self.soundDead.play()
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision):
        pass