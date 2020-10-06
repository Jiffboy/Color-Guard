import math
import pygame


class Projectile:
    speed = 5

    def __init__(self, origin, color, target, damage):
        self.x = origin[0]
        self.y = origin[1]
        self.color = color
        self.target = target
        self.damage = damage

    def update(self):
        xDist = abs(self.target.x - self.x)
        yDist = abs(self.target.y - self.y)
        if xDist == 0:
            theta = 90
        elif yDist == 0:
            theta = 0
        else:
            theta = math.atan(yDist/xDist)
        xChange = math.cos(theta) * self.speed
        yChange = math.sin(theta) * self.speed
        if self.target.x < self.x:
            self.x -= xChange
        elif self.target.x > self.x:
            self.x += xChange
        if self.target.y < self.y:
            self.y -= yChange
        elif self.target.y > self.y:
            self.y += yChange

        hit = self.target.isHit((self.x, self.y))
        if hit:
            self.target.takeDamage(self.damage, self.color)
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x + 4, self.y + 4, 8, 8))
