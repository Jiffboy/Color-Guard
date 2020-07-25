import math
import pygame


class Projectile:
    speed = 3

    def __init__(self, origin, color, target):
        self.x = origin[0]
        self.y = origin[1]
        self.color = color
        self.target = target

    def update(self):
        xDist = abs(self.target.x - self.x)
        yDist = abs(self.target.y - self.y)
        theta = math.atan(yDist/xDist)
        xChange = math.sin(theta) * self.speed
        yChange = math.cos(theta) * self.speed
        if self.target.x < self.x:
            self.x -= xChange
        elif self.target.x > self.x:
            self.x += xChange
        if self.target.y < self.y:
            self.y -= yChange
        elif self.target.y > self.y:
            self.y += yChange

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x + 4, self.y + 4, 8, 8))
