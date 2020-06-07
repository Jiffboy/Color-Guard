import pygame


class Control:
    def __init__(self, pos, dims, name, control):
        self.x = pos[0]
        self.y = pos[1]
        self.width = dims[0]
        self.height = dims[1]
        self.name = name
        self.control = control

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        font = pygame.font.Font(None, 30)
        text = font.render(self.name, 1, (150, 150, 150))
        x = self.x + (self.width - text.get_rect().width) / 2
        y = self.y + (self.height - text.get_rect().height) / 2
        screen.blit(text, (x, y))

    def inControl(self, pos):
        if self.x <= pos[0] <= self.x + self.width:
            if self.y <= pos[1] <= self.y + self.height:
                return True
        return False
