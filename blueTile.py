import tile
import pygame


class BlueTile(tile.Tile):
    name = "blue"
    isTower = True
    color = (0, 0, 255)
    greyColor = (0, 0, 100)
    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.size, self.size))
