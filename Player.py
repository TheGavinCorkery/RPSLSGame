class Player:
    def __init__(self):
        self.gestures = ['Rock', 'Spock', 'Paper', 'Lizard', 'Scissors']
        self.gesture_choice = 0
        self.players = []
        
    def set_gesture_choice(self, choice):
        self.gesture_choice = choice

    def display_gesture_choices(self):
        x = 0
        for gesture in self.gestures:
            print(f"Enter {x} for {gesture}")
            x += 1

    def add_player(self, player):
        self.players.append(player)