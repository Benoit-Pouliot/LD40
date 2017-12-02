from LDEngine.ldLib.scene.LogicHandler import LogicHandler
from LDEngine.ldLib.collision.collisionNotifySprite import collisionNotifySprite

from app.ScenePhysics import ScenePhysics
from app.settings import *

class LogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = ScenePhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.physics.update()
        self.handleCollision()


    def handleCollision(self):
        for sprite in self.gameData.sceneData.allSprites:
            collisionNotifySprite(sprite, SOLID, self.gameData.sceneData)
