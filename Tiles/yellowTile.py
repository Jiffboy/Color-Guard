from Tiles import towerTile
import pygame


class YellowTile(towerTile.TowerTile):
    name = "yellow"
    isTower = True
    color = (255, 255, 0)
    greyColor = (100, 100, 0)
    radius = 150

    def __init__(self, x, y, size):
        towerTile.TowerTile.__init__(self, x, y, size)
