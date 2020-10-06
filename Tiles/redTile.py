from Tiles import towerTile
import pygame


class RedTile(towerTile.TowerTile):
    name = "red"
    isTower = True
    color = (255, 0, 0)
    greyColor = (100, 0, 0)
    radius = 50
    damage = 10
    fireRate = 0.25

    def __init__(self, x, y, size):
        towerTile.TowerTile.__init__(self, x, y, size)
