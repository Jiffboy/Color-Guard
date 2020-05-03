import item
import math


class Menu:
    x = 0
    y = 0
    itemHeight = 0
    itemWidth = 0
    items = []

    def __init__(self, startPos, itemDims):
        self.x = startPos[0]
        self.y = startPos[1]
        self.itemWidth = itemDims[0]
        self.itemHeight = itemDims[1]

        self.items.append(item.Item("red", (self.x, self.y), (self.itemWidth, self.itemHeight)))
        self.items.append(item.Item("blue", (self.x + self.itemWidth, self.y), (self.itemWidth, self.itemHeight)))
        self.items.append(item.Item("green", (self.x + self.itemWidth * 2, self.y), (self.itemWidth, self.itemHeight)))

    def draw(self, screen):
        for menuItem in self.items:
            menuItem.draw(screen)

    def isInMenu(self, pos):
        if self.x <= pos[0] <= self.x + self.itemWidth * len(self.items):
            if self.y <= pos[1] <= self.y + self.itemHeight:
                return True
        return False

    def getItem(self, pos):
        itemNum = math.floor((pos[0] - self.x) / self.itemWidth)
        return self.items[itemNum].getTile()