from LDEngine.ldLib.Sprites.GenericSprite import GenericSprite
from app.ItemDatabase import ItemDatabase
from LDEngine.ldLib.collision.collisionMask import CollisionMask

#
# Generic item to create
#

class GenericItem(GenericSprite):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.name = "item"
        self.type = "item"

        self.itemDatabase = ItemDatabase()

        self.dictProperties = {"itemId": self.setId}

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
