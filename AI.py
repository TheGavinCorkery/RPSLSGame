from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def choose_gesture(self):
        chosen_gesture = random.random(0, 5)
        self.gesture_choice = chosen_gesture