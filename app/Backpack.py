import random

class Backpack():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = [[None for x in range(width)] for y in range(height)]

    def addItem(self, item):
        coordinate = self.nextFreeCoordinate();
        if coordinate != None:
            self.items[coordinate[0]][coordinate[1]] = item

    def nextFreeCoordinate(self):
        x = 0
        y = 0

        for list in self.items:
            for item in list:
                if item == None:
                    return (x,y)
                y += 1
            x += 1
            y = 0
        return None

    def getTotalWeight(self):
        totalWeight = 0

        for list in self.items:
            for item in list:
                if item != None:
                    totalWeight += item.weight

        return totalWeight

    def getTotalValue(self):
        totalValue = 0

        for list in self.items:
            for item in list:
                if item != None:
                    totalValue += item.value

        return totalValue

    def empty(self):
        for list in self.items:
            for index in range(len(list)):
                list[index] = None

    def returnFirstItemCoordinates(self):
        x = 0
        y = 0

        for list in self.items:
            for item in list:
                if item != None:
                    return (x,y)
                y += 1
            x += 1
            y = 0

        return None

    def removeItem(self, x, y):
        self.items[x][y] = None

    def isEmpty(self):
        numberOfItem = 0
        for list in self.items:
            for index in range(len(list)):
                if list[index]:
                    numberOfItem = numberOfItem + 1
        return numberOfItem == 0

    def isFull(self):
        numberOfItem = 0
        for list in self.items:
            for index in range(len(list)):
                if list[index]:
                    numberOfItem = numberOfItem + 1
        return numberOfItem == (self.width * self.height)

