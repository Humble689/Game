class Loaction:
    def __init__(self, name, description, enemy=None):
        self.name =name
        self.description = description
        self.enemy = enemy
    

    def enter(self, player):
        print(f"\nYou enter {self.nmae}: {self.description}")
        if self.enemy:
            combat(player, self.enemy)
        else:
            print (f"{self.name} is a peacefu place. Nothing happens here.")
