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
        self.handleBulletCollision()
        self.handleBridgeCollision()

    def handleBulletCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.bulletGroup,
                                                    False)
        for bullet in collisionList:
            if isinstance(bullet, Bullet):
                bullet.detonate()
            self.sceneData.player.hurt()

    def handleBridgeCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.bridgeGroup,
                                                    False)

        playerOnBridge = False

        for bridge in collisionList:
            if bridge.animation.currentFrame == 0:
                if self.sceneData.player.rect.centery < bridge.rect.top:
                    self.sceneData.player.onCollision(SOLID, DOWN)
                    playerOnBridge = True
                else:
                    playerOnBridge = False
            else:
                playerOnBridge = False

        if len(collisionList) == 0:
            playerOnBridge = False

        if self.sceneData.player.isOnBridge != playerOnBridge:
            self.sceneData.player.isOnBridge = playerOnBridge