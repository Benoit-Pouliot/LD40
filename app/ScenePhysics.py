from app.settings import *
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState

class ScenePhysics:
    def __init__(self, sceneData):
        self.sceneData = sceneData

    def update(self):
        self.applyFrictionPlayer(self.sceneData.player)
        self.applyFrictionItems(self.sceneData.itemGroup)
        self.applyGravity(self.sceneData.allSprites)

    def applyFrictionPlayer(self, sprite):
        try:
            if (sprite.isFrictionApplied == True):
                if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                    sprite.speedx -= FRICTION
                elif sprite.speedx > 0:
                    sprite.speedx = 0

                if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                    sprite.speedx += FRICTION
                elif sprite.speedx < 0:
                    sprite.speedx = 0

                if sprite.speedy > 0 and sprite.speedy - FRICTION > 0:
                    sprite.speedy -= FRICTION
                elif sprite.speedy > 0:
                    sprite.speedy = 0

                if sprite.speedy < 0 and sprite.speedy + FRICTION < 0:
                    sprite.speedy += FRICTION
                elif sprite.speedy < 0:
                    sprite.speedy = 0
        except AttributeError:
            pass

    def applyFrictionItems(self, items):
        for sprite in items:
            try:
                if sprite.isFrictionApplied == True:# and isinstance(sprite.state, IdleState):
                    if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                        sprite.speedx -= FRICTION
                    elif sprite.speedx > 0:
                        sprite.speedx = 0

                    if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                        sprite.speedx += FRICTION
                    elif sprite.speedx < 0:
                        sprite.speedx = 0

                    if sprite.speedy > 0 and sprite.speedy - FRICTION > 0:
                        sprite.speedy -= FRICTION
                    elif sprite.speedy > 0:
                        sprite.speedy = 0

                    if sprite.speedy < 0 and sprite.speedy + FRICTION < 0:
                        sprite.speedy += FRICTION
                    elif sprite.speedy < 0:
                        sprite.speedy = 0
            except AttributeError:
                pass

    def applyGravity(self, allSprites):
        for sprite in allSprites:
            try:
                if sprite.isGravityApplied == True:
                    sprite.speedy += GRAVITY
            except AttributeError:
                pass