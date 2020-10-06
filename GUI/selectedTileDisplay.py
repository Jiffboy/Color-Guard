from enum import Enum
from GUI.control import Control
from Tiles.towerTile import TowerTile
import globals


class TileAction(Enum):
    DELETE = 0,
    NONE = 1


class SelectedTileDisplay:
    actions = []

    def __init__(self, startPos):
        self.x = startPos[0]
        self.y = startPos[1]
        self.tile = None
        delete = Control((self.x + (globals.windowWidth - self.x) / 2 - 50, self.y + 125), (100, 25), "Delete", TileAction.DELETE)
        self.actions.append(delete)

    def draw(self, screen):
        if self.tile is not None:
            self.tile.drawInBounds(self.x + (globals.windowWidth - self.x) / 2, self.y + 50, 100, screen)
        if issubclass(self.tile.__class__, TowerTile):
            for action in self.actions:
                action.draw(screen)

    def updateSelectedTile(self, tile):
        if self.tile is not None:
            self.tile.selected = False
        self.tile = tile
        if tile is not None:
            tile.selected = True

    def getTile(self):
        return self.tile

    def getAction(self, pos):
        for action in self.actions:
            if action.inControl(pos):
                return action.control
        return TileAction.NONE
