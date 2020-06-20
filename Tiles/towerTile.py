from Tiles import tile
import pygame
import math


class TowerTile(tile.Tile):
    name = "green"
    isTower = True
    color = (0, 255, 0)
    greyColor = (0, 100, 0)
    radius = 100
    selected = False

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.size, self.size))
        if self.selected:
            pygame.draw.arc(screen, self.color, [self.x-self.radius + self.size/2, self.y-self.radius + self.size/2, 2*self.radius, 2*self.radius], math.pi, 2*math.pi)
            pygame.draw.arc(screen, self.color, [self.x-self.radius + self.size/2, self.y-self.radius + self.size/2, 2*self.radius, 2*self.radius], 2*math.pi, math.pi)