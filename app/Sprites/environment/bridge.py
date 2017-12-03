import pygame
import os

from LDEngine.app.sprites.enemy.enemy import Enemy
from app.Sprites.enemy.bullet import FireBullet
from LDEngine.app.tools.animation import Animation

from LDEngine.app.settings import *
import random


class Bridge(Enemy):
    def __init__(self, x, y, theMap=None, direction="Left"):
        super().__init__(x, y, os.path.join('Sprite', 'bridgebottomleft.png'))

        self.name = "Bridge"

        if direction== "Left":
            self.imageRaised = pygame.image.load(os.path.join('Sprite', 'bridgebottomleft.png'))
            self.imageDropped = pygame.image.load(os.path.join('Sprite', 'bridgeloweredbottomleft.png'))
        else:
            self.imageRaised = pygame.image.load(os.path.join('Sprite', 'bridgebottomright.png'))
            self.imageDropped = pygame.image.load(os.path.join('Sprite', 'bridgeloweredbottomright.png'))

        self.frames = [self.imageRaised, self.imageDropped]
        self.animation = Animation(self,self.frames,100)

        self.rect = self.imageRaised.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0
        self.speedy = 0

        self.theMap = theMap

        self.setDirection(direction)

        self.isGravityApplied = False
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


    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def dead(self):
        self.soundDead.play()
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision):
        pass