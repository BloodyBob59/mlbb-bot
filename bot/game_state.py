class GameState:
    def __init__(self):
        self.hero = None
        self.position = (0, 0)
        self.health = 100
        self.enemies = []
        self.allies = []
        self.minions = []
        self.towers = []
        # Add other game information as needed

    def update_hero(self, hero):
        self.hero = hero

    def update_position(self, x, y):
        self.position = (x, y)

    def update_health(self, health):
        self.health = health

    def update_enemies(self, enemies):
        self.enemies = enemies

    def update_allies(self, allies):
        self.allies = allies

    def update_minions(self, minions):
        self.minions = minions

    def update_towers(self, towers):
        self.towers = towers

    # Add other methods for managing game state as needed
