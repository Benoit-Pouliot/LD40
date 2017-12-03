import os
import pygame
import math

from LDEngine.ldLib.tools.ImageBox import rectSurface
from LDEngine.ldLib.animation.Animation import Animation
from LDEngine.ldLib.collision.collisionMask import CollisionMask
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpring import CollisionWithSpring
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpike import CollisionWithSpike
from LDEngine.ldLib.collision.CollisionRules.CollisionWithLadder import CollisionWithLadder
from LDEngine.ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from LDEngine.ldLib.collision.collisionTile import collisionCenterWithTile
from app.Sprites.environment.CollisionWithBridge import CollisionWithBridge
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState
from LDEngine.ldLib.Sprites.Player.JumpState import JumpState
from LDEngine.ldLib.Sprites.Player.FallingState import FallingState
from LDEngine.ldLib.Sprites.Player.ClimbingState import ClimbingState

from app.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "player"

        # Code for animation
        self.animCache = SetupAnimations()
        self.animation = self.animCache.idleR
        self.image = self.animation.update()
        #End of code for animation

        self.imageTransparent = rectSurface((32, 32), WHITE, 3)
        self.imageTransparent.set_colorkey(COLORKEY)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 7
        self.maxSpeedyUp = 35
        self.maxSpeedyDown = 10
        self.jumpSpeed = 25
        self.springJumpSpeed = 35
        self.accx = 2
        self.accy = 2

        # At this value, the player is slowed to 1/2 of his speed.
        self.halfTagWeight = 100

        self.isFrictionApplied = True
        self.isGravityApplied = True
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.leftShiftPressed = False
        self.spacePressed = False
        self.leftMousePressed = False
        self.rightMousePressed = False

        self.mapData = sceneData
        self.mapData.player = self
        self.isOnBridge = False

        self.isAlive = True

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithLadder())  # Need to be second
        self.collisionRules.append(CollisionWithBridge())
        self.collisionRules.append(CollisionWithSolid())
        self.collisionRules.append(CollisionWithSpring())
        self.collisionRules.append(CollisionWithSpike())

        self._state = IdleState()
        self.nextState = None

    def update(self):
        # Update image with animation
        self.image = self.animation.update()

        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        # If on a ladder, we fix him
        if isinstance(self.state, ClimbingState):

            tileWidth = self.mapData.tmxData.tilewidth
            decal = (int)(tileWidth/2) - (int)((self.collisionMask.rect.right - self.collisionMask.rect.left)/2)
            self.rect.x = (int)((self.collisionMask.rect.left + self.collisionMask.rect.right)/2/tileWidth)*tileWidth + decal

            # If not moving in x, we hard-fix him to help to pass between floor
            if self.speedx == 0:
                self.x = self.rect.x



        # Update animation instead
        if self.speedx > 0 or (self.speedx == 0 and self.facingSide == RIGHT):
            if isinstance(self.state, IdleState):
                if self.speedx == 0:
                    self.animation = self.animCache.idleR
                else:
                    self.animation = self.animCache.idleMoveR
            elif isinstance(self.state, ClimbingState):
                if self.speedy == 0:
                    self.animation = self.animCache.climbR
                else:
                    self.animation = self.animCache.climbMoveR
            elif isinstance(self.state, JumpState):
                self.animation = self.animCache.jumpR
            elif isinstance(self.state, FallingState):
                self.animation = self.animCache.fallR
            self.facingSide = RIGHT
        elif self.speedx < 0 or (self.speedx == 0 and self.facingSide == LEFT):
            if isinstance(self.state, IdleState):
                if self.speedx == 0:
                    self.animation = self.animCache.idleL
                else:
                    self.animation = self.animCache.idleMoveL
            elif isinstance(self.state, ClimbingState):
                if self.speedy == 0:
                    self.animation = self.animCache.climbL
                else:
                    self.animation = self.animCache.climbMoveL
            elif isinstance(self.state, JumpState):
                self.animation = self.animCache.jumpL
            elif isinstance(self.state, FallingState):
                self.animation = self.animCache.fallL
            self.facingSide = LEFT

        self.updateCollisionMask()
        self.updatePressedKeys()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)

    def capSpeed(self):

        if self.speedx > 0 and self.speedx > self.maxSpeedx * self.decSpeed():
            self.speedx = self.maxSpeedx * self.decSpeed()
        if self.speedx < 0 and self.speedx < -self.maxSpeedx * self.decSpeed():
            self.speedx = -self.maxSpeedx * self.decSpeed()

        capSpeedDown = self.maxSpeedyDown
        capSpeedUp = self.maxSpeedyUp
        if isinstance(self.state, ClimbingState):
            capSpeedDown = self.maxSpeedx * self.decSpeed()
            capSpeedUp = self.maxSpeedx

        if self.speedy > 0 and self.speedy > capSpeedDown:
            self.speedy = capSpeedDown
        if self.speedy < 0 and self.speedy < -capSpeedUp * self.decSpeed():
            self.speedy = -capSpeedUp * self.decSpeed()

    def updateSpeedRight(self):
        self.speedx += self.accx

    def updateSpeedLeft(self):
        self.speedx -= self.accx

    def updateSpeedUp(self):
        self.speedy -= self.accy

    def updateSpeedDown(self):
        if isinstance(self.state, ClimbingState):
            self.speedy += self.accy

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def dead(self):
        self.isAlive = False

    def onSpike(self):
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                #On colle le player sur le mur à droite
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.left -= (self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
            if sideOfCollision == DOWN:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                #self.speedy = 0
            if sideOfCollision == UP:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0

    def notify(self, event):
        self.nextState = self.state.handleInput(self, event)

        if self.nextState != None:
            self.state = self.nextState
            self.nextState = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state.exit(self)
        self._state = value
        self._state.enter(self)


    def updatePressedKeys(self):
        if self.rightPressed:
            self.updateSpeedRight()
        if self.leftPressed:
            self.updateSpeedLeft()
        if self.upPressed:
            self.updateSpeedUp()
        if self.downPressed:
            self.updateSpeedDown()
        if self.leftMousePressed:
            pass
        if self.rightMousePressed:
            pass
        if self.leftShiftPressed:
            pass
        if self.spacePressed:
            pass

    def jump(self):
        self.speedy = -self.jumpSpeed * self.decSpeed()

    def hurt(self):
        # TODO: Destroy best treasure and make the player invincible for a little bit(see LD39)
        pass

    # Decelerate speed
    def decSpeed(self):

        backPackWeight = 0
        if TAG_BP == 1:
            backPackWeight = 50
        if TAG_AGB == 1:
            backPackWeight = 25

        if backPackWeight < self.halfTagWeight:
            return 1 - backPackWeight / self.halfTagWeight / 2
        else:
            return 1/2*math.exp(1-backPackWeight / self.halfTagWeight)

class SetupAnimations():
    def __init__(self):

        # Code for animation
        # imageShapeRight = [pygame.image.load(os.path.join('img', 'playerRight.png')),
        #                         pygame.image.load(os.path.join('img', 'playerRight1.png')),
        #                         pygame.image.load(os.path.join('img', 'playerRight2.png'))]
        # imageShapeLeft = [pygame.transform.flip(img, True, False) for img in imageShapeRight]

        sizeX = 30
        sizeY = 45

        imgIdleR = [rectSurface((sizeX, sizeY), PURPLE)]
        imgIdleMoveR = [rectSurface((sizeX, sizeY), ORANGE)]
        imgJumpR = [rectSurface((sizeX, sizeY), BLUE)]
        imgClimbR = [rectSurface((sizeX, sizeY), RED)]
        imgClimbMoveR = [rectSurface((sizeX, sizeY), GREEN)]
        imgFallR = [rectSurface((sizeX, sizeY), YELLOW)]

        imgIdleL = [pygame.transform.flip(img, True, False) for img in imgIdleR]
        imgIdleMoveL = [pygame.transform.flip(img, True, False) for img in imgIdleMoveR]
        imgJumpL = [pygame.transform.flip(img, True, False) for img in imgJumpR]
        imgClimbL = [pygame.transform.flip(img, True, False) for img in imgClimbR]
        imgClimbMoveL = [pygame.transform.flip(img, True, False) for img in imgClimbMoveR]
        imgFallL = [pygame.transform.flip(img, True, False) for img in imgFallR]

        self.idleR = Animation(imgIdleR, 30, True)
        self.idleL = Animation(imgIdleL, 30, True)
        self.idleMoveR = Animation(imgIdleMoveR, 30, True)
        self.idleMoveL = Animation(imgIdleMoveL, 30, True)
        self.jumpR = Animation(imgJumpR, 30, True)
        self.jumpL = Animation(imgJumpL, 30, True)
        self.climbR = Animation(imgClimbR, 30, True)
        self.climbL = Animation(imgClimbL, 30, True)
        self.climbMoveR = Animation(imgClimbMoveR, 30, True)
        self.climbMoveL = Animation(imgClimbMoveL, 30, True)
        self.fallR = Animation(imgFallR, 30, True)
        self.fallL = Animation(imgFallL, 30, True)
