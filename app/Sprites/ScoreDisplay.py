from LDEngine.app.settings import *
import pygame
import os

class ScoreDisplay(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, fontSize=26):
        super().__init__()

        self.x = x
        self.y = y
        self.sceneData = sceneData
        self.previousScore = 0
        self.image= pygame.Surface((150, 50))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hudFont = pygame.font.SysFont(MENU_FONT, fontSize)
        self.number = self.hudFont.render('Score: ' + str(self.sceneData.score), False, HUD_FONT_COLOR)
        self.image.blit(self.number, (0,0))

    def update(self):
        if self.sceneData.score != self.previousScore:
            self.image.fill(WHITE)
            self.number = self.hudFont.render('Score: ' + str(self.sceneData.score), False, HUD_FONT_COLOR)
            self.image.blit(self.number, (0,0))
            self.previousScore = self.sceneData.score
