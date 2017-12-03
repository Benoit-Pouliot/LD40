import pygame
from app.settings import *
from app.Sprites.MenuGrid import MenuGrid
from LDEngine.ldLib.collision.collisionMask import CollisionMask

class MenuItem(pygame.sprite.Sprite):
    def __init__(self, backpack, itemDatabase, drawer):
        super().__init__()

        self.drawer = drawer
        self.backpack = backpack
        self.itemDatabase = itemDatabase
        self.x = 50
        self.y = 50

        self.menuGrid = MenuGrid(self.x, self.y, backpack.width, backpack.height, 32, 32, 1)
        self.surface = pygame.Surface((self.menuGrid.totalWidth, self.menuGrid.totalHeight))
        self.surface.blit(self.menuGrid.image, (0,0))

        for i in range(backpack.width):
            for j in range(backpack.height):
                item = backpack.items[i][j]
                if item != None:
                    self.surface.blit(item.image, self.menuGrid.getBoxPixelCoordinate(i, j))

        self.image = self.surface
        self.rect = self.surface.get_rect()

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        self.selectedItem = None

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        pass

    def notify(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                pos = pygame.mouse.get_pos()
                self.select(pos[0]//(self.menuGrid.slotWidth + self.menuGrid.lineWidth + self.x), pos[1]//(self.menuGrid.slotHeight + self.menuGrid.lineWidth + self.y))
                if self.selectedItem != None:
                    self.drawer.imageOnMouse = self.selectedItem.image
                else:
                    self.drawer.imageOnMouse = None
        # if event.type == pygame.MOUSEMOTION:
        #     if self.selectedItem != None:
        #         self.drawer
        #         pos = pygame.mouse.get_pos()
        #         self.surface.blit(self.selectedItem.image, pos)

    def select(self, x, y):
        if x < self.backpack.width and y < self.backpack.height:
            self.selectedItem = self.backpack.items[x][y]
            if self.selectedItem == 0:
                self.selectedItem = None
        else:
            self.selectedItem = None
