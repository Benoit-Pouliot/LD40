import os
import sys
import pygame

from LDEngine.ldLib.scene.Scene import Scene
from LDEngine.ldLib.scene.GameData import GameData

from app.SceneData import SceneData
from app.LogicHandler import LogicHandler
from app.EventHandler import EventHandler
from app.SceneHandler import SceneHandler

from app.Drawer import Drawer

from app.settings import *

if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)
    screen.fill(WHITE)

    pygame.display.set_caption("Weight in Gold")

    # Init
    pygame.mixer.pre_init(22050, -16, 2, 4096)
    # pygame.mixer.init()
    pygame.init()
    pygame.font.init()

    # Hide the mouse
    # pygame.mouse.set_visible(False)

    initNameMap = "GameMap"
    if TAG_BP == 1:
        initNameMap = "CavernMap"

    sceneHandler = SceneHandler(screen)
    sceneHandler.mainLoop()
