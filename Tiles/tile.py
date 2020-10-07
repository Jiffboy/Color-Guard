from enum import Enum
import math


class Dir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    NONE = 5


class Tile:
    name = ""
    isRoad = False
    isTower = False
    isRoad = False
    isGreyed = False
    selected = False
    enemies = []

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pass

    def drawInBounds(self, x, y, width, height):
        pass

    def update(self):
        pass

    def updatePos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def isInTile(self, pos):
        if self.x <= pos[0] <= self.x + self.size:
            if self.y <= pos[1] <= self.y + self.size:
                return True
        return False

    def isInRadius(self, tower, range):
        closestX = max(self.x, min(self.x + self.size, tower[0]))
        closestY = max(self.y, min(self.y + self.size, tower[1]))
        distX = tower[0] - closestX
        distY = tower[1] - closestY
        distance = math.sqrt(distX ** 2 + distY ** 2)
        return distance <= range

    def enterEnemy(self, enemy):
        self.enemies.append(enemy)

    def exitEnemy(self, enemy):
        self.enemies.remove(enemy)
