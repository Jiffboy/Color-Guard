from enum import Enum


class Dir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    NONE = 5


class Tile:
    name = ""
    entry = Dir.NONE
    exit = Dir.NONE
    isTerrain = False
    isTower = False
    isGreyed = False

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pass

    def updatePos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def isInTile(self, pos):
        if self.x <= pos[0] <= self.x + self.size:
            if self.y <= pos[1] <= self.y + self.size:
                return True
        return False
