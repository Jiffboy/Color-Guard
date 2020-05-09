import pygame
import tileFactory


class Item:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, name, startPos, dims):
        self.x = startPos[0]
        self.y = startPos[1]
        self.width = dims[0]
        self.height = dims[1]

        x = self.x + (self.width / 4)
        y = self.y + (self.height / 2.5)
        size = self.height / 2

        self.tile = tileFactory.getTile(name, x, y, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        self.tile.draw(screen)

        font = pygame.font.Font(None, 36)
        text = font.render(self.tile.name, 1, self.tile.greyColor)
        x = self.x + (self.width - text.get_rect().width) / 2
        y = (self.y + (self.y - self.tile.y) / 2) + text.get_rect().height
        screen.blit(text, (x, y))

    def getTile(self):
        return tileFactory.getTile(self.tile.name, self.tile.x, self.tile.y, self.tile.size)