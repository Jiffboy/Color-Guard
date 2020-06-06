from Tiles import tile
import pygame


class Enemy:
    def __init__(self, startTile):
        self.currTile = startTile
        self.x = startTile.x + startTile.size / 2
        self.y = startTile.y
        self.tileSize = startTile.size

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x - self.tileSize/4, self.y- self.tileSize/4, self.tileSize / 2, self.tileSize / 2))
