import pygame
from app.settings import *
from app.Sprites.MenuGrid import MenuGrid

class MenuItem(pygame.sprite.Sprite):
    def __init__(self, backpack, itemImageBank):
        super().__init__()

        self.backpack = backpack
        self.itemImageBank = itemImageBank

        self.menuGrid = MenuGrid(50, 50, 5, 5, 32, 32, 4)
        self.surface = pygame.Surface((self.menuGrid.totalWidth, self.menuGrid.totalHeight))

        for i in range(backpack.width):
            for j in range(backpack.height):
                itemID = backpack[i][j]
                if itemID != 0:
                    self.surface.blit(itemImageBank[itemID])

        self.image = self.surface
        self.rect = self.surface.get_rect()