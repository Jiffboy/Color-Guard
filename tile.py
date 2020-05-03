

class Tile:
    x = 0
    y = 0
    size = 0
    name = ""

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pass

    def updatePos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
