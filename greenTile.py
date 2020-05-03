import tile
import pygame


class GreenTile(tile.Tile):
    name = "green"

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.size, self.size))
