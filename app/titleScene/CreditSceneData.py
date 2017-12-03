
import pygame
import os

from LDEngine.ldLib.GUI.Button import Button
from LDEngine.ldLib.scene.SceneData import SceneData
from LDEngine.ldLib.GUI.messageBox.MessageBox import MessageBox

from app.settings import *

import weakref


class CreditSceneData(SceneData):
    def __init__(self):
        super().__init__()

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('Sprite', 'menu.png'))
        self.background.rect = self.background.image.get_rect()

        self.spritesBackGround.add(self.background)

        self.player = None
        self.camera = None

        widthCreditBox = 0.5*SCREEN_WIDTH
        heightCreditBox = 0.6*SCREEN_HEIGHT

        self.createCreditBox(SCREEN_WIDTH/2-widthCreditBox/2, 1*SCREEN_HEIGHT / 7, widthCreditBox, heightCreditBox)

        buttonWidth = 0.55 * SCREEN_WIDTH - 100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH / 2 - buttonWidth / 2, 16 * SCREEN_HEIGHT / 20),
                                              (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)

        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

    def createCreditBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height,fontSize=12)
        self.textGoal.textList.append('Weight in Gold was made for Ludum Dare 40')
        # self.textGoal.textList.append('')
        self.textGoal.textList.append('December 1-4 2017')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('A Game by:')
        # Team members go here
        self.textGoal.textList.append('André Gagné-Bouchard')
        self.textGoal.textList.append('Philippe Gendreau')
        self.textGoal.textList.append('Charles-Olivier Magnan')
        self.textGoal.textList.append('Benoît Pouliot')
        # Music sources go here
        self.textGoal.textList.append('')
        self.textGoal.textList.append('Featuring the following music tracks:')
        self.textGoal.textList.append('Stance Gives You Balance by Hogan Grip')
        self.textGoal.textList.append('(http://freemusicarchive.org/music/Hogan_Grip/)')
        self.textGoal.textList.append('Cylinder Nine by Chris Zabriskie')
        self.textGoal.textList.append('Readers! Do You Read? by Chris Zabriskie')
        self.textGoal.textList.append('(http://freemusicarchive.org/music/Chris_Zabriskie/)')

        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCREEN

    def beforeLeavingScene(self,screen):
        pass
