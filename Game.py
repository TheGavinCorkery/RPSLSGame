from AI import AI
from Human import Human

class Game:
    def __init__(self):
        self.players = []
        self.score_to_win = 2
        self.continue_playing = True
    def run_game(self):
        self.welcome_message() #Display welcome/rules
        self.player_selection()# Get # of players
        while self.continue_playing == True:
            self.play_match() #Plays the match
            self.continue_playing = self.keep_playing_game()
        
            
    def keep_playing_game(self):
        continue_game = 0
        while continue_game == 0:
            continue_game = int(input('Would you like to continue playing? If yes enter 1 if no enter 2: '))
            if continue_game == 1:
                return True
            elif continue_game == 2:
                return False
            else:
                continue_game = 0
        

    def play_match(self):
        self.score_to_win = int(self.set_match_game())
        nowinner = True
        roundcounter = 0
        while nowinner == True:
            roundcounter+=1
            print('Round ', roundcounter, " fight!:")
            self.pick_a_card(self.players[0])# display gestures and collect choices
            self.pick_a_card(self.players[1])
            self.compare_player_choices(self.players[0].gesture_choice, self.players[1].gesture_choice)# compare choices
            print('Player 1 has ', self.players[0].round_wins, ' wins, Player 2 has ', self.players[1].round_wins, ' wins')
            nowinner = self.best_of_wins()# check scores
        if nowinner == False:
            self.display_winner()

    def welcome_message(self):
        print("Welcome to the game of Rock Paper Scissors Lizard Spock\n\n Scissors decapitate Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors\n\n\n Good luck, and may the odds be in your favor!")
    def player_selection(self):
        player_one = Human()
        user_input = ''
        while user_input == '':
            user_input = input("Would you like to play single-player or multiplayer? Enter '1' for single-player or '2' for multiplayer: ")
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
        # print('player 1s choice = ', player1)
        # print('player 2 choice: ', player2)
        comparator = ((player1 - player2) % 5)
        # print('compare value: ', comparator)
        if comparator == 1 or comparator == 2:
            print ("Player 1 wins!")
            self.players[0].round_wins += 1
        elif comparator == 3 or comparator == 4:
            self.players[1].round_wins += 1
            print ("Player 2 wins!")
        else:
            print ("It's a tie")
        return ""
        
    def best_of_wins(self):
        if self.players[0].round_wins == self.score_to_win:
            return False
        elif self.players[1].round_wins == self.score_to_win:
            return False
        else:
            return True

    def pick_a_card(self, player):
        if player.name != "Computer":
            player.display_gesture_choices()
            thechosenone = None

            while thechosenone == None:
                thechosenone = int(input("Pick your gesture: "))
                if thechosenone < 0 or thechosenone > 4:
                    print('Please choose a choice between 0 and 4')
                    thechosenone = None

            player.gesture_choice = thechosenone

        else:
            thechosenone = player.choose_gesture()
            return thechosenone
            
    def display_winner(self):
        if self.players[0].round_wins >= self.score_to_win:
            print('Player 1 has won the entire game!')
        elif self.players[1].round_wins >= self.score_to_win:
            print('Player 2 has won the entire game!')
    
    def set_match_game(self):
        setscore = True
        while setscore:
            getmatchscore = int(input('Do you want to play best of 3, 5, or 7?'))
            if getmatchscore == 3:
                setscore = False
                return 2
            elif getmatchscore == 5:
                setscore = False
                return 3
            elif getmatchscore == 7:
                setscore = False
                return 5
            else:
                print("Please enter 3, 5, or 7")
            