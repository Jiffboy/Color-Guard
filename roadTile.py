import tile
import pygame


class RoadTile(tile.Tile):
    name = "road"
    isTerrain = True
    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, (155, 118, 83), (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, (106, 108, 110), (self.x, self.y, self.size, self.size))
