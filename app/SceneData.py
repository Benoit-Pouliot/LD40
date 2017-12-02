from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player
from app.settings import *
from app.Sprites.enemy.scheduledShooter import ScheduledShooter
import pygame

class SceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("CavernMap", "StartPointWorld", (SCREEN_WIDTH,SCREEN_HEIGHT))

        self.player = Player(self.spawmPointPlayerx, self.spawmPointPlayery, self)

        self.traps = []
        self.bulletGroup = pygame.sprite.Group()

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "Trap":
                shooter = ScheduledShooter(obj.x, obj.y, self)
                self.allSprites.add(shooter)
                self.traps.append(shooter)


        self.camera.add(self.allSprites)
