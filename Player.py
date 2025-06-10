class Player:
    def __init__ (self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.inventory= []
        self. experience = 1
        self.level = 1

    def attack(self, enemy):
        damage = max(self.strength - enemy.defense, 1)
        print (f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.health -=damage

    def heal(self, amount):
        self.health =+=amount
        print(f"{self.name} has been added to your inventory!")

    def add_item(self, item):
        self.inventory.append(item):
        print (f"{item} has been added toyour inventory!")

    def level_up(self):
        self.level += 1
        self.strength += 5
        self.health +=10
        slef.defense += 2
        print (f"{self.nmae} has leveled up! New Level: {self.level}")