import pygame, os
from app.Item import Item

class ItemDatabase():
    def __init__(self):

        self.size = 3
        self.itemList = [None] * self.size

        # Value, Weight, Image
        self.itemList[0] = Item(10, 1, pygame.image.load(os.path.join('img', 'RedRupee.png')))
        # self.itemList[1] = Item(10, 1, pygame.image.load(os.path.join('img', 'BlueRupee.png')))
        # self.itemList[2] = Item(10, 1, pygame.image.load(os.path.join('img', 'GreenRupee.png')))
        self.itemList[1] = Item(10, 30, pygame.image.load(os.path.join('img', 'Chest.png')))
        self.itemList[2] = Item(10, 5, pygame.image.load(os.path.join('img', 'crown.png')))
