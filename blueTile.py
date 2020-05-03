import tile
import pygame


class BlueTile(tile.Tile):
    name = "blue"

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
