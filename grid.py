import emptyTile
import math


class Grid:
    x = 0
    y = 0
    rows = 0
    cols = 0
    tileSize = 0
    grid = []

    def __init__(self, startPos, startDims, tileSize):
        self.x = startPos[0]
        self.y = startPos[1]
        self.rows = startDims[0]
        self.cols = startDims[1]
        self.tileSize = tileSize

        for i in range(0, self.cols):
            self.grid.append([])
            for j in range(0, self.rows):
                self.grid[i].append(emptyTile.EmptyTile(self.x + tileSize * i, self.y + tileSize * j, tileSize))

    def draw(self, screen):
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self.grid[i][j].draw(screen)

    def isInGrid(self, pos):
        if self.x <= pos[0] <= self.x + self.tileSize * self.cols:
            if self.y <= pos[1] <= self.y + self.tileSize * self.rows:
                return True
        return False

    def setTile(self, row, col, tile):
        tile.x = self.x + self.tileSize * row
        tile.y = self.y + self.tileSize * col
        tile.size = self.tileSize
        self.grid[row][col] = tile

    def setTileAtPos(self, pos, tile):
        xDist = pos[0] - self.x
        yDist = pos[1] - self.y
        row = math.floor(xDist / self.tileSize)
        col = math.floor(yDist / self.tileSize)
        self.setTile(row, col, tile)