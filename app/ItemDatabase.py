import pygame, os
from app.Item import Item

class ItemDatabase():
    def __init__(self):
        self.itemList = []

        self.itemList.append(Item(10, 20, pygame.image.load(os.path.join('img', 'RedRupee.png'))))