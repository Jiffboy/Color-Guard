import tile
import pygame


class RoadTile(tile.Tile):
    name = "road"

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (155, 118, 83), (self.x, self.y, self.size, self.size))
