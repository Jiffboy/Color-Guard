from Tiles.tile import Dir
import pygame
import math


class Enemy:
    def __init__(self, startTile, speed):
        self.currTile = startTile
        self.x = startTile.x + startTile.size / 2
        self.y = startTile.y
        self.direction = Dir.SOUTH
        self.speed = speed
        self.pastHalf = False
        self.health = 100
        self.damageTaken = 0
        self.color = (255, 255, 255)
        startTile.enterEnemy(self)

    def draw(self, screen):
        length = (self.currTile.size / 2) * (1 - self.damageTaken / self.health)
        red = math.floor(255 * ((self.health - self.damageTaken) / self.health) + self.color[0] * (self.damageTaken / self.health))
        green = math.floor(255 * ((self.health - self.damageTaken) / self.health) + self.color[1] * (self.damageTaken / self.health))
        blue = math.floor(255 * ((self.health - self.damageTaken) / self.health) + self.color[2] * (self.damageTaken / self.health))

        if red < 0:
            red = 0
        if green < 0:
            green = 0
        if blue < 0:
            blue = 0
        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255

        pygame.draw.rect(screen, (150, 150, 150), (self.x - self.currTile.size / 4 - 1, self.y - self.currTile.size / 4- 1, self.currTile.size / 2 + 2, self.currTile.size / 2 + 2))
        pygame.draw.rect(screen, (red, green, blue), (self.x - self.currTile.size/4, self.y - self.currTile.size/4, self.currTile.size / 2, self.currTile.size / 2))
        pygame.draw.rect(screen, (255,255,255), (self.x - (length / 2), self.y - 2, length, 4))


    def isInRange(self, tower, range):
        return True

    def isHit(self, point):
        lowerX = self.x - self.currTile.size / 4
        upperX = lowerX + self.currTile.size / 2
        lowerY = self.y - self.currTile.size / 4
        upperY = lowerY + self.currTile.size / 2
        if lowerX <= point[0] <= upperX:
            if lowerY <= point[1] <= upperY:
                return True
        return False

    def takeDamage(self, damage, color):
        self.damageTaken += damage
        if self.damageTaken != 0:
            red = math.ceil(color[0] * (damage / self.damageTaken) +
                            self.color[0] * ((self.damageTaken - damage) / self.damageTaken))
            green = math.ceil(color[1] * (damage / self.damageTaken) +
                            self.color[1] * ((self.damageTaken - damage) / self.damageTaken))
            blue = math.ceil(color[2] * (damage / self.damageTaken) +
                            self.color[2] * ((self.damageTaken - damage) / self.damageTaken))
            self.color = (red, green, blue)
        else:
            self.color = color

    def despawn(self):
        self.currTile.exitEnemy(self)

    def update(self, grid):
        if self.damageTaken >= self.health:
            return True
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
                self.currTile.exitEnemy(self)
                self.currTile = grid.getTileAtPos((self.x, self.y))
                self.currTile.enterEnemy(self)
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

