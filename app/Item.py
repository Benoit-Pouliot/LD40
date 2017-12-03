from LDEngine.ldLib.Sprites.GenericSprite import GenericSprite
from LDEngine.ldLib.collision.collisionMask import CollisionMask
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpring import CollisionWithSpring
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpike import CollisionWithSpike
from LDEngine.ldLib.collision.CollisionRules.CollisionWithLadder import CollisionWithLadder
from LDEngine.ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from app.Sprites.environment.CollisionWithBridge import CollisionWithBridge

class Item():
    def __init__(self,id, value, weight, image):
        self.id = id
        self.value = value
        self.weight = weight
        self.image = image

