import globals


class SelectedTileDisplay:
    def __init__(self, startPos):
        self.x = startPos[0]
        self.y = startPos[1]
        self.tile = None

    def draw(self, screen):
        if self.tile is not None:
            self.tile.drawInBounds(self.x + (globals.windowWidth - self.x) / 2, self.y + 50, 100, screen)

    def updateSelectedTile(self, tile):
        if self.tile is not None:
            self.tile.selected = False
        self.tile = tile
        if tile is not None:
            tile.selected = True

    def getTile(self):
        return self.tile