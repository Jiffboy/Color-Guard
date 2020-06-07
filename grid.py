from enemyManager import EnemyManager
from Tiles.tile import Dir
import tileFactory
import math
import random
import copy
import pygame


class Grid:
    x = 0
    y = 0
    rows = 0
    cols = 0
    tileSize = 0
    grid = []
    start = (0, 0)

    def __init__(self, startPos, startDims, tileSize):
        self.x = startPos[0]
        self.y = startPos[1]
        self.rows = startDims[0]
        self.cols = startDims[1]
        self.tileSize = tileSize
        self.enemyManager = EnemyManager(self)

        for i in range(0, self.cols):
            self.grid.append([])
            for j in range(0, self.rows):
                self.grid[i].append(tileFactory.getTile("empty", self.x + tileSize * i, self.y + tileSize * j, tileSize))

        self.constructRoad(18)
        self.enemyManager.spawnEnemy(self.grid[self.start[0]][self.start[1]])

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), (self.x - 3, self.y - 3, self.tileSize * self.cols + 6, self.tileSize * self.rows + 6))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.tileSize * self.cols, self.tileSize * self.rows))
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self.grid[i][j].draw(screen)
        self.enemyManager.draw(screen)

    def update(self):
        self.enemyManager.update()

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
        col = math.floor(xDist / self.tileSize)
        row = math.floor(yDist / self.tileSize)
        self.setTile(col, row, tile)

    def getTileAtPos(self, pos):
        xDist = pos[0] - self.x
        yDist = pos[1] - self.y
        col = math.floor(xDist / self.tileSize)
        row = math.floor(yDist / self.tileSize)
        return self.grid[col][row]

    def isPlaceableAtPos(self, pos):
        try:
            xDist = pos[0] - self.x
            yDist = pos[1] - self.y
            col = math.floor(xDist / self.tileSize)
            row = math.floor(yDist / self.tileSize)
            if (not self.grid[col][row].isTerrain) and (not self.grid[col][row].isTower):
                return True
            return False
        except:
            return False

    def showLines(self, show):
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                if self.grid[i][j].name == "empty":
                    if show:
                        self.grid[i][j].isGreyed = False
                    else:
                        self.grid[i][j].isGreyed = True

    def constructRoad(self, length):
        grid = []
        result = []
        even = False

        if length % 2 == 0:
            even = True

        while True:
            top = random.randrange(self.cols - 1)
            bot = random.randrange(self.cols - 1)

            # if the number of tiles that needs to be traveled isn't the same odd/even as the distance,
            # a path will not be able to be generated, cause math
            if (top + bot + self.rows-1) % 2 == even:
                break

        start = (top, 0)
        end = (bot, self.rows - 1)

        for i in range(0, self.cols):
            grid.append([])
            for j in range(0, self.rows):
                grid[i].append(0)

        result = self.findAllPaths(grid, start, end, length, result)
        path = result[random.randrange(len(result) - 1)]

        for i in range(0, self.cols):
            self.grid.append([])
            for j in range(0, self.rows):
                if path[i][j] == 1:
                    self.grid[i][j] = tileFactory.getTile("road", self.x + self.tileSize * i, self.y + self.tileSize * j, self.tileSize)

        index = (start[0], start[1])
        self.grid[index[0]][index[1]].entry = Dir.NORTH
        while index != end:
            path[index[0]][index[1]] = -1
            # North if able
            if index[1] != 0:
                if path[index[0]][index[1]-1] > 0:
                    self.grid[index[0]][index[1]].exit = Dir.NORTH
                    self.grid[index[0]][index[1]-1].entry = Dir.SOUTH
                    index = (index[0], index[1]-1)
                    continue

            # West if able
            if index[0] != 0:
                if path[index[0]-1][index[1]] > 0:
                    self.grid[index[0]][index[1]].exit = Dir.WEST
                    self.grid[index[0]-1][index[1]].entry = Dir.EAST
                    index = (index[0]-1, index[1])
                    continue

            # South if able
            if index[1] != self.rows - 1:
                if path[index[0]][index[1] + 1] > 0:
                    self.grid[index[0]][index[1]].exit = Dir.SOUTH
                    self.grid[index[0]][index[1] + 1].entry = Dir.NORTH
                    index = (index[0], index[1] + 1)
                    continue

            # East if able
            if index[0] != self.cols - 1:
                if path[index[0] + 1][index[1]] > 0:
                    self.grid[index[0]][index[1]].exit = Dir.EAST
                    self.grid[index[0] + 1][index[1]].entry = Dir.WEST
                    index = (index[0] + 1, index[1])
                    continue

        self.start = start

    def findAllPaths(self, grid, start, end, length, results):

        # if been here before
        if grid[start[0]][start[1]] == 1:
            return results

        # if touches any tile other than previous
        if self.getNumGridNeighbors(grid, start) > 1:
            return results
        
        grid[start[0]][start[1]] = 1
        length = length - 1

        # if exhausted length allowance
        if length == 0:
            # if at the targeted ending point
            if start == end:
                temp = copy.deepcopy(grid)
                results.append(temp)
            grid[start[0]][start[1]] = 0
            return results

        # Recurse North if able
        if start[1] != 0:
            results = self.findAllPaths(grid, (start[0], start[1] - 1), end, length, results)

        # Recurse West if able
        if start[0] != 0:
            results = self.findAllPaths(grid, (start[0] - 1, start[1]), end, length, results)

        # Recurse South if able
        if start[1] != self.rows - 1:
            results = self.findAllPaths(grid, (start[0], start[1] + 1), end, length, results)

        # Recurse East if able
        if start[0] != self.cols - 1:
            results = self.findAllPaths(grid, (start[0] + 1, start[1]), end, length, results)

        grid[start[0]][start[1]] = 0

        return results

    def getNumGridNeighbors(self, grid, point):
        count = 0

        if point[0] != 0:
            if grid[point[0] - 1][point[1]] == 1:
                count += 1

        if point[0] != self.cols - 1:
            if grid[point[0] + 1][point[1]] == 1:
                count += 1

        if point[1] != 0:
            if grid[point[0]][point[1] - 1] == 1:
                count += 1

        if point[1] != self.rows - 1:
            if grid[point[0]][point[1] + 1] == 1:
                count += 1

        return count
