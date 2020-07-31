from Tiles import tile
from projectile import Projectile
import pygame
import math
import time


class TowerTile(tile.Tile):
    name = "green"
    isTower = True
    color = (0, 255, 0)
    greyColor = (0, 100, 0)
    tilesInRange = []
    radius = 100
    fireRate = 1
    lastShot = 0

    def __init__(self, x, y, size):
        tile.Tile.__init__(self, x, y, size)

    def draw(self, screen):
        if not self.isGreyed:
            pygame.draw.rect(screen, self.color, (self.x + 4, self.y + 4, self.size - 8, self.size - 8))
            if self.selected:
                pygame.draw.circle(screen, self.color, (math.floor(self.x + self.size / 2), math.floor(self.y + self.size / 2)), self.radius, 1)
        else:
            pygame.draw.rect(screen, self.greyColor, (self.x + 4, self.y + 4, self.size - 8, self.size - 8))
            if self.selected:
                pygame.draw.circle(screen, self.greyColor, (math.floor(self.x + self.size / 2), math.floor(self.y + self.size / 2)), self.radius, 1)

    def updateViewableTiles(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].isInRadius():
                    if grid[i][j].isRoad:
                        self.tilesInRange.append(grid[i][j])

    def update(self):
        if time.time() - self.lastShot >= self.fireRate:
            for tile in self.tilesInRange:
                for enemy in tile.enemies:
                    if enemy.isInRange((self.x, self.y), self.radius):
                        self.lastShot = time.time()
                        shot = Projectile((self.x + self.size / 2, self.y + self.size / 2), self.color, enemy)
                        return shot
        return None
