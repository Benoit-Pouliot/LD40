from LDEngine.ldLib.scene.LogicHandler import LogicHandler
from LDEngine.ldLib.collision.collisionNotifySprite import collisionNotifySprite
from LDEngine.app.sprites.bullet import Bullet

from app.ScenePhysics import ScenePhysics
from app.settings import *

import pygame


class LogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = ScenePhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.physics.update()
        self.handleCollision()
        self.handleBulletCollision()


    def handleCollision(self):
        for sprite in self.gameData.sceneData.allSprites:
            collisionNotifySprite(sprite, SOLID, self.gameData.sceneData)

    def handleBulletCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.bulletGroup,
                                                    False)
        for bullet in collisionList:
            if isinstance(bullet, Bullet):
                bullet.detonate()
            self.sceneData.player.hurt()
