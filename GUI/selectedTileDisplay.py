from enum import Enum
from GUI.control import Control
from Tiles.towerTile import TowerTile
import globals
import pygame


class TileAction(Enum):
    DELETE = 0,
    NONE = 1


class SelectedTileDisplay:
    actions = []

    def __init__(self, startPos):
        self.x = startPos[0]
        self.y = startPos[1]
        self.tile = None
        self.midpoint = self.x + (globals.windowWidth - self.x) / 2
        delete = Control(( self.midpoint - 50, self.y + 200), (100, 25), "Delete", TileAction.DELETE)
        self.actions.append(delete)

    def draw(self, screen):
        if issubclass(self.tile.__class__, TowerTile):
            self.tile.drawInBounds(self.x + (globals.windowWidth - self.x) / 2, self.y + 50, 100, screen)
            for action in self.actions:
                action.draw(screen)
            font = pygame.font.Font(None, 30)
            range = font.render("Range: " + str(self.tile.radius), 1, (150, 150, 150))
            damage = font.render("Damage: " + str(self.tile.damage), 1, (150, 150, 150))
            fire = font.render("Fire Rate: " + str(self.tile.fireRate), 1, (150, 150, 150))
            screen.blit(range, (self.midpoint - range.get_rect().width / 2, self.y + 105))
            screen.blit(damage, (self.midpoint - damage.get_rect().width / 2, self.y + 138))
            screen.blit(fire, (self.midpoint - fire.get_rect().width / 2, self.y + 171))

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
