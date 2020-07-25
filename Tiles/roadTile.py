from Tiles.tile import Tile, Dir
import pygame


class RoadTile(Tile):
    name = "road"
    isRoad = True
    entry = Dir.NONE
    exit = Dir.NONE

    def __init__(self, x, y, size):
        Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (155, 118, 83), (self.x, self.y, self.size, self.size))
