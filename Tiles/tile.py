from enum import Enum


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

    def isInRadius(self):
        return True

    def enterEnemy(self, enemy):
        self.enemies.append(enemy)

    def exitEnemy(self, enemy):
        self.enemies.remove(enemy)
