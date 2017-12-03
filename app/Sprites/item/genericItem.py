from LDEngine.ldLib.Sprites.GenericSprite import GenericSprite
from app.ItemDatabase import ItemDatabase
from LDEngine.ldLib.collision.collisionMask import CollisionMask
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpring import CollisionWithSpring
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpike import CollisionWithSpike
from LDEngine.ldLib.collision.CollisionRules.CollisionWithLadder import CollisionWithLadder
from LDEngine.ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from app.Sprites.environment.CollisionWithBridge import CollisionWithBridge

#
# Generic item to create
#

class GenericItem(GenericSprite):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.mapData = None
        self.name = "item"
        self.type = "item"

        self.itemDatabase = ItemDatabase()

        self.dictProperties = {"itemId": self.setId}

        self.speedx = 0
        self.speedy = 0
        self.springJumpSpeed = 35

        self.isFrictionApplied = False
        self.isGravityApplied = False
        self.isCollisionApplied = False

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []

    def update(self):
        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y
        self.updateCollisionMask()
        self.capSpeed()

    def capSpeed(self):
        if self.speedy > 14:
            self.speedy = 14

    def setId(self, id):
        self.id = int(id)

        self.setImg(self.id)

    def setImg(self, id):

        intId = int(id)
        if intId < self.itemDatabase.size:
            self.image = self.itemDatabase.itemList[intId].image
            tempRect = self.image.get_rect()
            self.rect.width = tempRect.width
            self.rect.height = tempRect.height
            self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def pickedUp(self):
        self.kill()

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

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y
