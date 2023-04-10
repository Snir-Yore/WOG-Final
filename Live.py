from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_game
# from Utils import screen_cleaner
# from MainScores import score_server
from Score import *

def welcome():
    clean_score_file()
    name = input("please write your name:")
    print(f"Hello, {name} and welcome to the World of Games", "\n""Here you can find many cool games to play.")


welcome()



def load_game():

    game_choice = input(
        "Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    try:
        while game_choice not in ['1', '2', '3']:
            game_choice = input("Invalid input. Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        choose_difficulty(game_choice)
    except ValueError:
        print("Invalid choice. Please try again.")


def choose_difficulty(game_choice):
    global difficulty
    difficulty = input("Please choose game difficulty from 1 to 5:\n")
    while difficulty not in ['1', '2', '3', '4', '5']:
        difficulty = input("Invalid input. Please choose game difficulty from 1 to 5:\n")

    if game_choice == '1':
        from MemoryGame import play
        play(difficulty)
    elif game_choice == '2':
        from GuessGame import play
        play(difficulty)
    elif game_choice == '3':
        from CurrencyRouletteGame import play
        play(difficulty)
    else:
        print("An error occurred, please restart")

    if True:
       from Score import add_score
       add_score(difficulty)


    while True:

        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            game_choice = load_game()

        else:
            print("Thanks for playing WOG, see you next time")
            import MainScores
            break
            exit()

load_game()










