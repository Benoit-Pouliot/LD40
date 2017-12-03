from LDEngine.app.settings import *
from LDEngine.ldLib.scene.Scene import Scene
from app.titleScene.titleScreen import TitleScreen
from app.Drawer import Drawer
from app.titleScene.TitleSceneData import TitleSceneData
from app.titleScene.TitleSceneLogicHandler import TitleSceneLogicHandler
from app.titleScene.InstructionSceneData import InstructionSceneData
from app.titleScene.CreditSceneData import CreditSceneData
from app.titleScene.EndingSceneData import EndingSceneData

from app.LogicHandler import LogicHandler
from app.EventHandler import EventHandler
from app.SceneData import SceneData

from LDEngine.app.scene.platformScreen.platformScreen import PlatformScreen
from LDEngine.app.gameData import GameData


class SceneHandler:
    def __init__(self, screen):

        self.handlerRunning = True
        self.runningScene = TitleScreen
        self.screen = screen
        self.gameData = GameData()
        self.gameData.sceneData = TitleSceneData()
        self.logicHandler = TitleSceneLogicHandler(self.gameData)
        self.runningScene = TitleScreen(self.screen, self.gameData, self.logicHandler)


    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()
            self.logicHandler.handle()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == TITLE_SCREEN:
                self.gameData.sceneData = TitleSceneData()
                self.logicHandler = TitleSceneLogicHandler(self.gameData)
                self.runningScene = TitleScreen(self.screen, self.gameData, self.logicHandler)
            elif self.runningScene.nextScene == INSTRUCTION_SCREEN:
                self.gameData.sceneData = InstructionSceneData()
                self.logicHandler = TitleSceneLogicHandler(self.gameData)
                self.runningScene = TitleScreen(self.screen, self.gameData, self.logicHandler)
            elif self.runningScene.nextScene == CREDIT_SCREEN:
                self.gameData.sceneData = CreditSceneData()
                self.logicHandler = TitleSceneLogicHandler(self.gameData)
                self.runningScene = TitleScreen(self.screen, self.gameData, self.logicHandler)
            elif self.runningScene.nextScene == PLATFORM_SCREEN:
                # Create the test scene
                drawer = Drawer()
                self.gameData.sceneData = SceneData(drawer)
                logicHandler = LogicHandler(self.gameData)
                eventHandler = EventHandler(self.gameData.sceneData)

                testScene = Scene(self.screen, self.gameData, logicHandler, eventHandler, drawer)
                self.runningScene = testScene

