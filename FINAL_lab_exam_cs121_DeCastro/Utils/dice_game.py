# dice_game.py

import random

class DiceGame:
    def __init__(self):
        self.user = None
        self.points = 0
        self.stage_wins = 0

    def play_game(self):
        print("Starting a new game...")
        self.points = 0
        self.stage_wins = 0
        for stage in range(1, 4):
            print(f"Stage {stage}:")
            player_roll = self.roll_dice()
            opponent_roll = self.roll_dice()
            print(f"Player rolled: {player_roll}")
            print(f"Opponent rolled: {opponent_roll}")
            if player_roll > opponent_roll:
                print("You win this round!")
                self.points += 1
            elif player_roll < opponent_roll:
                print("You lose this round!")
            else:
                print("It's a tie! Rolling again...")
                continue
            if self.points == stage:
                self.stage_wins += 1
                print("Congratulations! You win this stage!")
                if stage < 3:
                    choice = input("Do you want to continue to the next stage? (1: Yes, 0: No): ")
                    if choice == '0':
                        break
            else:
                print("GAME OVER. You didn't win any stages.")
                break
        print(f"Total points earned: {self.points}")
        print(f"Number of stages won: {self.stage_wins}")

    def roll_dice(self):
        return random.randint(1, 6)

    def show_top_scores(self):
        print("Showing top scores:")
        # Load and display top scores from file

    def logout(self):
        self.user = None
        print("Logged out successfully.")

    def menu(self):
        print("Menu:")
        print("1. Start Game")
        print("2. Show Top Scores")
        print("3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.play_game()
        elif choice == '2':
            self.show_top_scores()
        elif choice == '3':
            self.logout()
        else:
            print("Invalid choice. Please try again.")