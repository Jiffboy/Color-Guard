import tile
import pygame


class BlueTile(tile.Tile):
    name = "blue"
    isTower = True
    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, (0, 0, 150), (self.x, self.y, self.size, self.size))
