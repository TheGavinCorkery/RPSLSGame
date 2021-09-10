from Player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def set_name(self, name):
        self.name = name
