from enemy import Enemy


class EnemyManager:
    def __init__(self, grid):
        self.enemies = []
        self.grid = grid

    def spawnEnemy(self, startTile):
        enemy = Enemy(startTile, 1)
        self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def update(self):
        for enemy in self.enemies:
            enemy.update(self.grid)