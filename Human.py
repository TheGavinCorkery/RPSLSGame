from Player import Player

class Human(Player):
    def __init__(self):
        self.name = ''
        super().__init__()

    def set_name(self):
        name = None
        while name == None:
            name = input("What is your name? ")
            if name.replace(" ", "").isalpha():
                pass
            else:
                print('Please enter a valid name.')
                name = None
        self.name = name
