from GUI.item import Item
import copy
import pygame


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

        width = (pygame.display.get_surface().get_width() - 30 - (self.itemWidth * 3)) / 2

        self.items.append(Item("red", (self.x, self.y), (self.itemWidth, self.itemHeight)))
        self.items.append(
            Item("blue", (self.x + width + self.itemWidth, self.y), (self.itemWidth, self.itemHeight)))
        self.items.append(
            Item("green", (self.x + width * 2 + self.itemWidth * 2, self.y), (self.itemWidth, self.itemHeight)))

    def draw(self, screen):
        for menuItem in self.items:
            menuItem.draw(screen)

    def isInMenu(self, pos):
        for item in self.items:
            if item.isInItem(pos):
                return True
        return False

    def getItem(self, pos):
        for item in self.items:
            if item.isInItem(pos):
                return copy.deepcopy(item.tile)
