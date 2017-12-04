__author__ = 'Bobsleigh'
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState
from LDEngine.ldLib.Sprites.Player.JumpState import JumpState
from LDEngine.ldLib.Sprites.Player.FallingState import FallingState

class CollisionWithBridge(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        if (sprite.isOnBridge and not isinstance(sprite.state, JumpState) and not isinstance(sprite.state, FallingState)) or\
           (sprite.isOnBridge and sprite.speedy >= 0 and isinstance(sprite.state, JumpState)) or\
           (sprite.isOnBridge and sprite.speedy >= 0 and isinstance(sprite.state, FallingState)):
            sprite.state = IdleState()

