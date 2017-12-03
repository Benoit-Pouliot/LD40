from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player
from app.settings import *
from app.Sprites.enemy.scheduledShooter import ScheduledShooter
from app.Sprites.item.itemFactory import ItemFactory
from app.ItemDatabase import ItemDatabase
from app.Sprites.environment.bridge import Bridge
from app.Sprites.MenuItem import MenuItem
from app.Backpack import Backpack
from app.Drawer import Drawer
import pygame

class SceneData(SceneDataTMX):
    def __init__(self, drawer, nameMap="GameMap"):
        super().__init__(nameMap, "StartPointWorld", (SCREEN_WIDTH,SCREEN_HEIGHT))

        self.score = 0

        self.drawer = drawer

        self.traps = []
        self.bulletGroup = pygame.sprite.Group()
        self.bridgeGroup = pygame.sprite.Group()

        self.itemDatabase = ItemDatabase()
        self.backpack = Backpack(5, 5)

        # self.backpack.addItem(self.itemDatabase.itemList[1])
        # self.backpack.addItem(self.itemDatabase.itemList[1])
        # self.backpack.addItem(self.itemDatabase.itemList[2])
        # self.backpack.addItem(self.itemDatabase.itemList[2])
        self.backpack.items[1][1] = self.itemDatabase.itemList[0]


        self.player = Player(self.spawmPointPlayerx, self.spawmPointPlayery, self)

        self.menuItem = MenuItem(self.backpack, self.itemDatabase, self.drawer, self.player)
        self.spritesHUD.add(self.menuItem)
        self.notifyGroup.add(self.menuItem)

        self.menuItemIsDisplayed = True

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "Trap":
                Direction = "Left"

                for nameProp, prop in obj.properties.items():
                    if nameProp == "direction":
                        Direction = prop

                shooter = ScheduledShooter(obj.x, obj.y, self, direction=Direction)
                self.allSprites.add(shooter)
                self.traps.append(shooter)
            elif obj.name == "Bridgeleft":
                bridge = Bridge(obj.x, obj.y, self, "Left")
                self.allSprites.add(bridge)
                self.bridgeGroup.add(bridge)
            elif obj.name == "Bridgeright":
                bridge = Bridge(obj.x, obj.y, self, "Right")
                self.allSprites.add(bridge)
                self.bridgeGroup.add(bridge)


        self.itemGroup = pygame.sprite.Group()
        itemFactory = ItemFactory()
        for obj in self.tmxData.objects:
            if obj.type == "item":
                item = itemFactory.create(obj, self)
                if item is not None:
                    self.allSprites.add(item)
                    self.itemGroup.add(item)

        self.camera.add(self.allSprites)


