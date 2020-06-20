from Tiles.tile import Dir
import pygame


class Enemy:
    def __init__(self, startTile, speed):
        self.currTile = startTile
        self.x = startTile.x + startTile.size / 2
        self.y = startTile.y
        self.direction = Dir.SOUTH
        self.speed = speed
        self.pastHalf = False

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), (self.x - self.currTile.size / 4 - 1, self.y - self.currTile.size / 4- 1, self.currTile.size / 2 + 2, self.currTile.size / 2 + 2))
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.currTile.size/4, self.y - self.currTile.size/4, self.currTile.size / 2, self.currTile.size / 2))

    def update(self, grid):
        if self.direction == Dir.SOUTH:
            self.y = self.y + self.speed
            if not self.pastHalf and self.y >= self.currTile.y + self.currTile.size / 2:
                self.redirect()

        elif self.direction == Dir.NORTH:
            self.y = self.y - self.speed
            if not self.pastHalf and self.y <= self.currTile.y + self.currTile.size / 2:
                self.redirect()

        elif self.direction == Dir.EAST:
            self.x = self.x + self.speed
            if not self.pastHalf and self.x >= self.currTile.x + self.currTile.size / 2:
                self.redirect()

        elif self.direction == Dir.WEST:
            self.x = self.x - self.speed
            if not self.pastHalf and self.x <= self.currTile.x + self.currTile.size / 2:
                self.redirect()

        if not self.currTile.isInTile((self.x, self.y)):
            if grid.isInGrid((self.x, self.y)):
                self.currTile = grid.getTileAtPos((self.x, self.y))
                self.direction = self.getOppositeDirection(self.currTile.entry)
                self.pastHalf = False
            else:
                return True
        return False



    def redirect(self):
        if self.direction == Dir.SOUTH:
            excess = self.y - (self.currTile.y + self.currTile.size / 2)
            self.y -= excess

        if self.direction == Dir.NORTH:
            excess = (self.currTile.y + self.currTile.size / 2) - self.y
            self.y -= excess

        if self.direction == Dir.SOUTH:
            excess = self.x - (self.currTile.x + self.currTile.size / 2)
            self.x -= excess

        if self.direction == Dir.SOUTH:
            excess = (self.currTile.x + self.currTile.size / 2) - self.x
            self.x -= excess

        self.direction = self.currTile.exit
        self.pastHalf = True

    def getOppositeDirection(self, dir):
        if dir == Dir.NORTH:
            return Dir.SOUTH
        if dir == Dir.SOUTH:
            return Dir.NORTH
        if dir == Dir.EAST:
            return Dir.WEST
        if dir == Dir.WEST:
            return Dir.EAST

