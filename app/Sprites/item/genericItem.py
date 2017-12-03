from LDEngine.ldLib.Sprites.GenericSprite import GenericSprite
from app.ItemDatabase import ItemDatabase

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
        self.id = id

        self.setImg(self.id)

    def setImg(self, id):

        intId = int(id)
        if intId < self.itemDatabase.size:
            self.image = self.itemDatabase.itemList[intId].image

    def pickedUp(self):
        self.kill()
