import pygame
import os

from LDEngine.ldLib.scene.SceneData import SceneData
from LDEngine.ldLib.GUI.Button import Button
from LDEngine.ldLib.GUI.messageBox.MessageBox import MessageBox

from app.settings import *

import weakref

class InstructionSceneData(SceneData):
    def __init__(self):
        super().__init__()
        self.nextScene = None

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('Sprite', 'menu.png'))
        self.background.rect = self.background.image.get_rect()

        self.spritesBackGround.add(self.background)

        boxWidth = 0.7 * SCREEN_WIDTH
        self.createControlBox(SCREEN_WIDTH/2-boxWidth/2, 1*SCREEN_HEIGHT / 7, boxWidth,4 * SCREEN_HEIGHT / 7)

        buttonWidth = 0.55 * SCREEN_WIDTH-100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 16 * SCREEN_HEIGHT / 20), (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)
        #self.allSprites.add(self.backToTitleScreenButton)
        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

    def createControlBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height)
        self.textGoal.textList.append('Legends say the caves underneath the metros of')
        self.textGoal.textList.append('Montreal are filled with riches. Tired of your day job,')
        self.textGoal.textList.append('you decide to check for yourself if the rumors are real.')
        self.textGoal.textList.append('Beware, traveler! Ill-prepared adventurers')
        self.textGoal.textList.append('soon feel the weight of the riches they acquire.')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('Move with the ARROW KEYS.')
        self.textGoal.textList.append('Jump with SPACE.')
        self.textGoal.textList.append('Your inventory is controlled with the MOUSE.')
        self.textGoal.textList.append('Toggle it on or off with SHIFT.')
        self.textGoal.textList.append('Mute the game with the M key.')
        self.textGoal.textList.append('Your performance will be timed.')
        self.textGoal.updateText()
        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCREEN

    def beforeLeavingScene(self,screen):
        pass
