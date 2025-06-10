class Enemy:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self. health = health
        self.strength = strength
        self.defense = defense


    def attack(self, player):
        damage = max(self.strength - player.defense, 1)
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.health -= damage