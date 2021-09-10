class Player:
    def __init__(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.gesture_choice = 0
        self.players = []
        
    def set_gesture_choice(self, choice):
        self.gesture_choice = choice
