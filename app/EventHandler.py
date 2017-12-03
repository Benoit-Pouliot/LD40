import pygame
import sys

class EventHandler():
    def __init__(self, sceneData):
        self.menuItem = sceneData.menuItem
        self.sceneData = sceneData

    def eventHandle(self,notifySet):
        self.notifySet = notifySet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    self.toggleItemMenu()
                if event.key == pygame.K_m:
                    self.sceneData.playSounds = not self.sceneData.playSounds

            for obj in self.notifySet:
                obj.notify(event)

    def toggleItemMenu(self):
        if self.sceneData.menuItemIsDisplayed:
            self.sceneData.menuItem.unselectItem()
            self.sceneData.spritesHUD.remove(self.menuItem)
            self.sceneData.notifyGroup.remove(self.menuItem)
            self.sceneData.menuItemIsDisplayed = False
        else:
            self.sceneData.spritesHUD.add(self.menuItem)
            self.sceneData.notifyGroup.add(self.menuItem)
            self.sceneData.menuItemIsDisplayed = True
