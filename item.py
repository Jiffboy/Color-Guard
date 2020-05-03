import pygame
import tileFactory


class Item:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, name, startPos, dims):
        self.x = startPos[0]
        self.y = startPos[1]
        self.width = dims[0]
        self.height = dims[1]

        x = self.x + (self.width / 4)
        y = self.y + (self.height / 4)
        size = self.height / 2

        self.tile = tileFactory.getTile(name, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        self.tile.draw(screen)

    def getTile(self):
        return tileFactory.getTile(self.tile.name, self.tile.x, self.tile.y, self.tile.size)