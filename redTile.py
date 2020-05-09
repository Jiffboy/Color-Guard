import tile
import pygame


class RedTile(tile.Tile):
    name = "red"
    isTower = True
    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, (150, 0, 0), (self.x, self.y, self.size, self.size))
