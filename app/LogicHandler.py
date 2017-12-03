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
        self.handleBridgeCollision()
        self.handleItemCollision()
        self.handleZoneCollision(self.sceneData.player)

    def handleCollision(self):
        for sprite in self.gameData.sceneData.bulletGroup:
            collisionNotifySprite(sprite, SOLID, self.gameData.sceneData)

    def handleBulletCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.bulletGroup,
                                                    False)
        for bullet in collisionList:
            if isinstance(bullet, Bullet):
                bullet.detonate()
            self.sceneData.player.hurt()

    def handleItemCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.itemGroup,
                                                    False)
        for item in collisionList:
            self.sceneData.player.pickUpItem(item.id)
            item.pickedUp()


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

    def handleZoneCollision(self, player):
        for obj in self.sceneData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "chest":
                    self.emptyBackpackInChest()

    def isPlayerIsInZone(self, player, zone):
        if player.rect.centerx  >= zone.x and \
           player.rect.centerx <= zone.x + zone.width and \
           player.rect.centery >= zone.y and \
           player.rect.centery <= zone.y + zone.height:
           return True
        else:
           return False

    def emptyBackpackInChest(self):
        self.sceneData.score += self.sceneData.backpack.getTotalValue()
        self.sceneData.backpack.empty()
        self.sceneData.player.backPackWeight = 0
        self.sceneData.menuItem.updateItemImages()
