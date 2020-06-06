from enemy import Enemy


class EnemyManager:
    def __init__(self, grid):
        self.enemies = []
        self.grid = grid

    def spawnEnemy(self, startTile):
        enemy = Enemy(startTile)
        self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
