from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player
from app.settings import *

class SceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("CavernMap", "StartPointWorld", (SCREEN_WIDTH,SCREEN_HEIGHT))

        self.player = Player(50, 50, self)
        self.camera.add(self.player)