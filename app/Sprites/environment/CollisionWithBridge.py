__author__ = 'Bobsleigh'
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState

class CollisionWithBridge(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        if sprite.isOnBridge:
            sprite.state = IdleState()

