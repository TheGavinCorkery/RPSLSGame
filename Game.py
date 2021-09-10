from AI import AI
from Human import Human

class Game:
    def __init__(self):
        pass
    def run_game(self):
        pass

    def welcome_message(self):
        #### Display rules and welcome
        pass
    def player_selection(self):
        user_input = 'playerz'
        while user_input == 'playerz':
            user_input = input("Would you like to play single-player or multiplayer? Enter '1' for single-player or '2' for multiplayer.")
            if user_input == '1':
                print("You have selected single-player! You will play against an AI opponent.")
                player_one = input("What is your name?")
                player_two = "Player2"
            elif user_input == '2':
                print("You have selected multiplayer! please enter your name below. ")
                player_one = input("Player 1, what is your real name??")
                player_two = input("What is player 2's name?")
            else:
                user_input = 'playerz'
                print("Let's make a logical selection here")
        self.player_one = player_one
        self.player_two = player_two
    def compareplayerchoices(self, player1, player2):
        # Rock crushes Scissors
        # Rock crushes Lizard
        # Paper covers Rock
        # Paper disproves Spock
        # Scissors cuts Paper
        # Scissors decapitates Lizard
        # Lizard poisons Spock
        # Lizard eats Paper
        # Spock smashes Scissors
        # Spock vaporizes Rock
        # 0 — rock 
        # 1 — Spock 
        # 2 — paper 
        # 3 — lizard 
        # 4 — scissors 
        #each choice wins against the preceding two choices and loses against the following two choices 
        # (if rock and scissors are thought of as being adjacent using modular arithmetic).
        pass

    def bestofwins(self):

        pass
    def score_tracker(self):
        pass
    def display_winner(self):
        pass
