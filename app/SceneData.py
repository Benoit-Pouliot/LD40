from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX

from app.Sprites.Player import Player

class SceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("AnimateMap")

        self.player = Player(50, 50, self)
        self.camera.add(self.player)