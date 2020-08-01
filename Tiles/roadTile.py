from Tiles.tile import Tile, Dir
import pygame


class RoadTile(Tile):
    name = "road"
    isRoad = True
    entry = Dir.NONE
    exit = Dir.NONE
    color = (155, 118, 83)
    greyColor = (99, 78, 58)
    borderWidth = 1

    def __init__(self, x, y, size):
        Tile.__init__(self, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        if self.entry != Dir.NORTH and self.exit != Dir.NORTH:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.size, self.borderWidth))
        if self.entry != Dir.EAST and self.exit != Dir.EAST:
            pygame.draw.rect(screen, self.greyColor, (self.x + self.size - self.borderWidth, self.y, self.borderWidth, self.size))
        if self.entry != Dir.SOUTH and self.exit != Dir.SOUTH:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y + self.size - self.borderWidth, self.size, self.borderWidth))
        if self.entry != Dir.WEST and self.exit != Dir.WEST:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.borderWidth, self.size))
