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
        self.rect.x = self.x
        self.rect.y = self.y

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        self.selectedItem = None
        self.selectedSlot = None

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        pass

    def notify(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                pos = pygame.mouse.get_pos()
                backpackCoordinateClicked = ((pos[0] - self.x)//(self.menuGrid.slotWidth + self.menuGrid.lineWidth), (pos[1] - self.y)//(self.menuGrid.slotHeight + self.menuGrid.lineWidth))
                if backpackCoordinateClicked[0] < self.backpack.width and backpackCoordinateClicked[0] >= 0 and backpackCoordinateClicked[1] < self.backpack.height and  backpackCoordinateClicked[1] >= 0:
                    if self.selectedItem == None:
                        self.select(backpackCoordinateClicked[0], backpackCoordinateClicked[1])
                        if self.selectedItem != None:
                            self.drawer.imageOnMouse = self.selectedItem.image
                        else:
                            self.drawer.imageOnMouse = None
                    else: # We had an item selected
                        item = self.backpack.items[(pos[0] - self.x)//(self.menuGrid.slotWidth + self.menuGrid.lineWidth)][(pos[1] - self.y)//(self.menuGrid.slotHeight + self.menuGrid.lineWidth)]
                        itemDestination = self.backpack.items[self.selectedSlot[0]][self.selectedSlot[1]]
                        self.backpack.items[(pos[0] - self.x)//(self.menuGrid.slotWidth + self.menuGrid.lineWidth)][(pos[1] - self.y)//(self.menuGrid.slotHeight + self.menuGrid.lineWidth)] = self.backpack.items[self.selectedSlot[0]][self.selectedSlot[1]]
                        self.backpack.items[self.selectedSlot[0]][self.selectedSlot[1]] = None
                        self.drawer.imageOnMouse = None
                        self.selectedItem = None
                        self.selectedSlot = None
                        self.updateItemImages()
        # if event.type == pygame.MOUSEMOTION:
        #     if self.selectedItem != None:
        #         self.drawer
        #         pos = pygame.mouse.get_pos()
        #         self.surface.blit(self.selectedItem.image, pos)

    def select(self, x, y):
        if x < self.backpack.width and y < self.backpack.height:
            self.selectedItem = self.backpack.items[x][y]
            self.selectedSlot = (x, y)
            if self.selectedItem == None:
                self.selectedItem = None
                self.selectedSlot = None
        else:
            self.selectedItem = None
            self.selectedSlot = None

    def updateItemImages(self):
        self.surface.fill(WHITE)
        self.surface.blit(self.menuGrid.image, (0,0))
        for i in range(self.backpack.width):
            for j in range(self.backpack.height):
                item = self.backpack.items[i][j]
                if item != None:
                    self.surface.blit(item.image, self.menuGrid.getBoxPixelCoordinate(i, j))