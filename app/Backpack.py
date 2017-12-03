
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
        return None