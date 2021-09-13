from AI import AI
from Human import Human

class Game:
    def __init__(self):
        self.player_one = ''
        self.player_two = ''
        self.score_to_win = 2
    def run_game(self):
        pass
    def welcome_message(self):
        #### Display rules and welcome
        pass
    def player_selection(self):
        player_one = Human()
        user_input = 'playerz'
        while user_input == 'playerz':
            user_input = input("Would you like to play single-player or multiplayer? Enter '1' for single-player or '2' for multiplayer.")
            if user_input == '1':
                print("You have selected single-player! You will play against an AI opponent.")
                player_one.set_name = input("What is your name?")
                player_two = AI()
            elif user_input == '2':
                player_two = Human()
                print("You have selected multiplayer! please enter your name below. ")
                player_one.set_name = input("Player 1, what is your real name??")
                player_two.set_name = input("What is player 2's name?")
            else:
                user_input = 'playerz'
                print("Let's make a logical selection here")
        self.player_one = player_one
        self.player_two = player_two
        # print(self.player_one.name)
        # print(self.player_two.name)
    def compare_player_choices(self, player1, player2):
        comparator = ((int(player1) - int(player2)) % 5)
        if comparator == 1 or comparator == 2:
            print ("Player wins!")
        elif comparator == 3 or comparator == 4:
            print ("Computer wins!")
        else:
            print ("Player and computer tie!")
        return ""
        pass
        
    def best_of_wins(self):
        pass
    def score_tracker(self, winner):
        winner.round_wins += 1
    def display_winner(self, player1, player2):
        if player1.round_wins > player2.round_wins:
            print('Player 1 has won!')
        else:
            print('Player 2 has won!')
