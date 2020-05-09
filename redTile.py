import tile
import pygame


class RedTile(tile.Tile):
    name = "red"
    isTower = True
    color = (255, 0, 0)
    greyColor = (100, 0, 0)

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.size, self.size))
