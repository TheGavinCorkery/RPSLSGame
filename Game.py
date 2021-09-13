from AI import AI
from Human import Human

class Game:
    def __init__(self):
        self.players = []
        self.score_to_win = 2
    def run_game(self):
        pass        
    def welcome_message(self):
        #### Display rules and welcome
        pass
    def player_selection(self):
        player_one = Human()
        user_input = ''
        while user_input == '':
            user_input = input("Would you like to play single-player or multiplayer? Enter '1' for single-player or '2' for multiplayer.")
            if user_input == '1':
                print("You have selected single-player! You will play against an AI opponent.")
                player_one.set_name()
                player_two = AI()
                self.players.append(player_one)
                self.players.append(player_two)
                
            elif user_input == '2':
                player_two = Human()
                print("You have selected multiplayer! please enter your name below. ")
                print('Player one:')
                player_one.set_name()
                print('Player two:')
                player_two.set_name()
                self.players.append(player_one)
                self.players.append(player_two)
                
            else:
                user_input = ''
                print("Let's make a logical selection here")
        
        # print(self.player_one.name)
        # print(self.player_two.name)
    def compare_player_choices(self, player1, player2):
        comparator = ((int(player1) - int(player2)) % 5)
        if comparator == 1 or comparator == 2:
            print ("Player 1 wins!")
            player1.round_wins += 1
        elif comparator == 3 or comparator == 4:
            player2.round_wins += 1
            print ("Player 2 wins!")
        else:
            print ("It's a tie")
        return ""
        
    def best_of_wins(self, scoretowin):
        if self.player_one.score >= int(scoretowin):
            pass
        elif self.player_two.score >= int(scoretowin):
            pass

    def pick_a_card(self, player):
        if player.name != "Computer":
            player.display_gesture_choices()
            thechosenone = int(input("Pick a your gesture")) - 1
            return thechosenone
        else:
            thechosenone = player.choose_gesture()
            return thechosenone
            
    def score_tracker(self, winner):
        winner.round_wins += 1
    def display_winner(self, player1, player2):
        if player1.round_wins > player2.round_wins:
            print('Player 1 has won!')
        else:
            print('Player 2 has won!')
