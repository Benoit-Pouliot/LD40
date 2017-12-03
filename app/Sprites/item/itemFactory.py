from LDEngine.ldLib.Sprites.SpriteFactory import SpriteFactory
from app.Sprites.item.genericItem import GenericItem

#
# Need to add all the enemy you gwant to generate.
# Otherwise, the enemy will not be created.
#

class ItemFactory(SpriteFactory):
    def __init__(self):
        self.dictSprite = {"item": GenericItem}
