import pygame
import os
import math

from LDEngine.ldLib.GUI.Button import Button
from LDEngine.ldLib.GUI.messageBox.MessageBox import MessageBox

from app.settings import *

import weakref

from LDEngine.ldLib.scene.SceneData import SceneData

POOR = 500
OKAY = 2000
GOOD = 4000
AMAZING = 8000

TIME_GOAL = 150


class EndingSceneData(SceneData):
    def __init__(self):
        super().__init__()

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('Sprite', 'performancereport.png'))
        self.background.rect = self.background.image.get_rect()
        # TODO WE NEED PLAYER ACCESS

        self.treasure = 5000
        self.time = 0
        self.internalScore = self.treasure * math.pow(0.9, (self.time/60))

        self.spritesBackGround.add(self.background)

        boxWidth = 0.55 * SCREEN_WIDTH
        self.createScoreBox(SCREEN_WIDTH/2-boxWidth/2, SCREEN_HEIGHT / 7, boxWidth, SCREEN_HEIGHT / 10)
        self.createTimeBox(SCREEN_WIDTH/2-boxWidth/2, 2*SCREEN_HEIGHT / 7, boxWidth, SCREEN_HEIGHT / 10)
        self.createMainMessageBox(SCREEN_WIDTH/2-boxWidth/2, 3*SCREEN_HEIGHT / 7, boxWidth, 3 * SCREEN_HEIGHT / 7)

        buttonWidth = 0.55 * SCREEN_WIDTH-100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 17 * SCREEN_HEIGHT / 20+20), (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)
        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

    def createScoreBox(self, x, y, width, height):
        self.textScore = MessageBox(x,y,width,height,fontSize=15)
        self.textScore.textList.append('Treasure gained: ' + str(self.treasure))

        self.allSprites.add(self.textScore)  # Add sprite
        pass

    def createTimeBox(self, x, y, width, height):
        self.textTime = MessageBox(x,y,width,height,fontSize=15)
        self.textTime.textList.append('Time it took: ' + str(self.time) + ' s')
        if self.time < TIME_GOAL:
            self.textTime.textList.append('Congratulations, you\'re a real Speedrunner!')
        self.allSprites.add(self.textTime)  # Add sprite
        pass

    def createMainMessageBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height,fontSize=15)

        if self.internalScore < POOR:
            self.textGoal.textList.append('You left your job for this?')
            self.textGoal.textList.append('What a waste of your time and money.')
            self.textGoal.textList.append('You may be back safe and sound, but you\'re')
            self.textGoal.textList.append('as poor as it gets. You search a basic job to')
            self.textGoal.textList.append('get back on your feet, and eventually find')
            self.textGoal.textList.append('a shoe store that will take you. You know')
            self.textGoal.textList.append('the thoughts are illogical, but as you')
            self.textGoal.textList.append('struggle with debts the cave yet beckons.')

        elif self.internalScore < OKAY:
            self.textGoal.textList.append('While you didn\'t get rich,')
            self.textGoal.textList.append('the trip at least paid for itself.')
            self.textGoal.textList.append('You\'re back safe and sound')
            self.textGoal.textList.append('and left to wonder what to do next.')
            self.textGoal.textList.append('Perhaps this dangerous trip was fruitful not for')
            self.textGoal.textList.append('the monetary gain at the end, but for the')
            self.textGoal.textList.append('lessons you learned from it. At least, that\'s')
            self.textGoal.textList.append('what you told your old boss to get your old')
            self.textGoal.textList.append('job back.')

        elif self.internalScore < GOOD:
            self.textGoal.textList.append('The riches you found in the cave aren\'t enough')
            self.textGoal.textList.append('to stop working entirely, in all likelihood,')
            self.textGoal.textList.append('but you still made a nice profit for the time being.')
            self.textGoal.textList.append('You take it easy for a while, but as your funds')
            self.textGoal.textList.append('slowly but surely start slipping through your fingers...')
            self.textGoal.textList.append('You can hear the cave whispering to you once more.')
            self.textGoal.textList.append('')
            self.textGoal.textList.append('Will you resist its call?')

        elif self.internalScore < AMAZING:
            self.textGoal.textList.append('Your exploits became the talk of the town!')
            self.textGoal.textList.append('Beyond the sustainable wealth you have acquired')
            self.textGoal.textList.append('from your journey, you also find within yourself')
            self.textGoal.textList.append('a passion for writing. Your autobiography sells')
            self.textGoal.textList.append('out within days. No matter the kind of book')
            self.textGoal.textList.append('you publish, it\'s bound to be a best seller.')
            self.textGoal.textList.append('')
            self.textGoal.textList.append('Money and fame, you\'ve got them!')
            self.textGoal.textList.append('Congratulations!')

        else:
            self.textGoal.textList.append('You got loads of money fast.')
            self.textGoal.textList.append('You did it all by yourself.')
            self.textGoal.textList.append('You buy an expensive house.')
            self.textGoal.textList.append('You buy a top of the line gaming rig.')
            self.textGoal.textList.append('You waste your time with strangers on social')
            self.textGoal.textList.append('media, trying to fill the growing void inside.')
            self.textGoal.textList.append('What do you do when you have it all? You think')
            self.textGoal.textList.append('about your old job. You had friends there. Why did')
            self.textGoal.textList.append('you throw it all away? It\'s so lonely at the top.')

        #self.textGoal.textList.append('Congratulations! You did it!')
        #self.textGoal.textList.append("You beat Superadmiral Kleido and")
        #self.textGoal.textList.append("restored peace to your community!")
        #self.textGoal.textList.append("It's time to go home and enjoy")
        #self.textGoal.textList.append('the fresh taste of unbranded cola.')
        #self.textGoal.textList.append('')
        #self.textGoal.textList.append('Go ahead, you deserve it.')
        # self.textGoal.textList.append('')
        # self.textGoal.textList.append('Press m to mute the game.')


        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCREEN

    def beforeLeavingScene(self,screen):
        pass
