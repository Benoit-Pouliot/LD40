from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player
from app.settings import *
from app.Sprites.enemy.scheduledShooter import ScheduledShooter
from app.ItemDatabase import ItemDatabase
from app.Sprites.MenuItem import MenuItem
from app.Backpack import Backpack
from app.Drawer import Drawer
import pygame

class SceneData(SceneDataTMX):
    def __init__(self, drawer):
        super().__init__("CavernMap", "StartPointWorld", (SCREEN_WIDTH,SCREEN_HEIGHT))

        self.player = Player(50, 50, self)
        self.drawer = drawer

        self.traps = []
        self.bulletGroup = pygame.sprite.Group()

        self.itemDatabase = ItemDatabase()
        self.backpack = Backpack(5, 5)
        self.backpack.addItem(self.itemDatabase.itemList[0])
        self.backpack.addItem(self.itemDatabase.itemList[0])
        self.backpack.items[1][1] = self.itemDatabase.itemList[0]
        self.menuItem = MenuItem(self.backpack, self.itemDatabase, self.drawer)
        self.spritesHUD.add(self.menuItem)
        self.notifyGroup.add(self.menuItem)

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "Trap":
                shooter = ScheduledShooter(obj.x, obj.y, self)
                self.allSprites.add(shooter)
                self.traps.append(shooter)

        self.camera.add(self.allSprites)
