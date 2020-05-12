from Tiles import tile
import pygame


class EmptyTile(tile.Tile):
    name = "empty"

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)
        self.isGreyed = True

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y, self.size, self.size))
            pygame.draw.rect(screen, (255, 255, 255), (self.x + 1, self.y + 1, self.size - 2, self.size - 2))
