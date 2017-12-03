from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player
from app.settings import *
from app.Sprites.enemy.scheduledShooter import ScheduledShooter
from app.Sprites.environment.bridge import Bridge
import pygame

class SceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("CavernMap", "StartPointWorld", (SCREEN_WIDTH,SCREEN_HEIGHT))

        self.player = Player(self.spawmPointPlayerx, self.spawmPointPlayery, self)

        self.traps = []
        self.bulletGroup = pygame.sprite.Group()
        self.bridgeGroup = pygame.sprite.Group()

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "Trap":
                # TODO: Add direction parameter
                shooter = ScheduledShooter(obj.x, obj.y, self)
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

        self.camera.add(self.allSprites)
