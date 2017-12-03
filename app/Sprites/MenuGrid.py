import pygame
from app.settings import *

class MenuGrid(pygame.sprite.Sprite):
    def __init__(self, x, y, horizontalSlotQty, verticalSlotQty, slotWidth, slotHeight, lineWidth):
        super().__init__()
        self.x = x
        self.y = y
        self.slotWidth = slotWidth
        self.slotHeight = slotHeight
        self.totalWidth = horizontalSlotQty * slotWidth + (horizontalSlotQty + 1) * lineWidth
        self.totalHeight = verticalSlotQty * slotHeight + (verticalSlotQty + 1) * lineWidth
        self.lineWidth = lineWidth
        self.surface = pygame.Surface((self.totalWidth, self.totalHeight))
        self.surface.fill(WHITE)

        # draw vertical lines
        for i in range(horizontalSlotQty + 1):
            firstPoint = ((slotWidth + lineWidth) * i,0)
            secondPoint = ((slotWidth + lineWidth) * i, verticalSlotQty * slotHeight + (verticalSlotQty + 1) * lineWidth)
            pygame.draw.line(self.surface, BLACK, firstPoint, secondPoint, lineWidth)

        # draw horizontal lines
        for i in range(verticalSlotQty + 1):
            firstPoint = (0, (slotHeight + lineWidth) * i)
            secondPoint = (horizontalSlotQty * slotWidth + (horizontalSlotQty + 1) * lineWidth, (slotHeight + lineWidth) * i)
            pygame.draw.line(self.surface, BLACK, firstPoint, secondPoint, lineWidth)

        self.image = self.surface
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def getBoxPixelCoordinate(self, x, y):
        pixelX = self.slotWidth * x + (self.lineWidth + 1) * x
        pixelY = self.slotHeight * y + (self.lineWidth + 1) * y
        return (pixelX, pixelY)