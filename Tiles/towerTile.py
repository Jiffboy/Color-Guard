from Tiles import tile
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
        else:
            pygame.draw.rect(screen, self.greyColor, (self.x, self.y, self.size, self.size))
        if self.selected:
            pygame.draw.arc(screen, self.color, [self.x-self.radius + self.size/2, self.y-self.radius + self.size/2, 2*self.radius, 2*self.radius], math.pi, 2*math.pi)
            pygame.draw.arc(screen, self.color, [self.x-self.radius + self.size/2, self.y-self.radius + self.size/2, 2*self.radius, 2*self.radius], 2*math.pi, math.pi)

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
                        return None
        return None
