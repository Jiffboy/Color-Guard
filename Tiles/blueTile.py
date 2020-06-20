from Tiles import towerTile
import pygame


class BlueTile(towerTile.TowerTile):
    name = "blue"
    isTower = True
    color = (0, 0, 255)
    greyColor = (0, 0, 100)

    def __init__(self, x, y, size):
        towerTile.TowerTile.__init__(self, x, y, size)