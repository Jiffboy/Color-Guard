import tile
import pygame


class EmptyTile(tile.Tile):
    name = "empty"

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 2, self.y + 2, self.size - 4, self.size - 4))