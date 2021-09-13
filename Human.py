from Player import Player

class Human(Player):
    def __init__(self):
        self.name = ''
        super().__init__()

    def set_name(self):
        name = input("What is your name?")
        self.name = name
