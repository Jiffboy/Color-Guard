class ProjectileManager:
    projectiles = []

    def addProjectile(self, projectile):
        self.projectiles.append(projectile)

    def removeProjectile(self, projectile):
        self.projectiles.remove(projectile)

    def update(self):
        despawnList = []
        for projectile in self.projectiles:
            hit = projectile.update()
            if hit:
                despawnList.append(projectile)
        for projectile in despawnList:
            self.projectiles.remove(projectile)

    def draw(self, screen):
        for projectile in self.projectiles:
            projectile.draw(screen)

    def despawnProjectiles(self):
        self.projectiles = []

    def despawnProjectilesForEnemy(self, enemy):
        despawnList = []
        for projectile in self.projectiles:
            if projectile.target == enemy:
                despawnList.append(projectile)
        for projectile in despawnList:
            self.projectiles.remove(projectile)