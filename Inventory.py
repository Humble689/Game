class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

    def use (self, player):