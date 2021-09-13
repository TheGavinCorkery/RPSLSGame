from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def choose_gesture(self):
        chosen_gesture = random.randint(0, 4)
        print(f"The computer has chosen {chosen_gesture}")
        self.gesture_choice = chosen_gesture