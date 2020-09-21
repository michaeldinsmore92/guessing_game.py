"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""


import random
import sys


def start_game(highscore):
    # Store a random number as the answer/solution.
    choice = "y"
    while choice == "y":
        ANSWER = random.randint(1,10)
        attempts = 1
        if highscore == None:
            print("Currently, there is no high score! Set the stage!")
        else:    
            print("The current high score to beat is {} guesses. Good luck!".format(highscore))
        guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
        # Continuously prompt the player for a guess.
        try:
            guess = int(guess)
        except ValueError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))
            start_game(highscore)
        except TypeError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))
            start_game(highscore)  
        while guess != ANSWER:
            try:
                if guess > 10 or guess < 1:
                    print("That number is out of range! Choose a number between 1 and 10...")
                    attempts += 1
                    guess = int(input("Take another guess! "))
            #   If the guess greater than the solution, display to the player "It's lower".
                elif guess > ANSWER:
                    print("It's lower...")
                    attempts += 1
                    guess = int(input("Take another guess! "))
            #   If the guess is less than the solution, display to the player "It's higher".
                elif guess < ANSWER:
                    print("It's higher...")
                    attempts += 1
                    guess = int(input("Take another guess! "))
            except ValueError as err:
                print("Uh oh! That's not a valid value. Please try again...".format(err))
            except TypeError as err:
                print("Uh oh! That's not a valid value. Please try again...".format(err))            
        #   Once the guess is correct, stop looping, inform the user they "Got it"
        if guess == ANSWER:
            print("You got it, {}!".format(name))
            print("It took you {} attempts.".format(attempts))
            if highscore == None or attempts < highscore:
                highscore = attempts
                print("Whoa! Congratulations! You set the high score! {} attempts".format(highscore))
                choice = input("Would you like to play again? Y/N ")
                if choice.lower() == "n":
                    print("Thank you for playing, {}. Goodbye!".format(name))
                    sys.exit()
                else:
                    start_game(highscore)
            else:
                print("Try again to beat the high score! {}".format(highscore))
                choice = input("Would you like to play again? Y/N ")
                if choice.lower() != "n":
                    start_game(highscore)
                else:
                    print("Thank you for playing, {}. Goodbye!".format(name))
                    sys.exit()

if __name__ == '__main__':
    # Display an intro/welcome message to the player.
    name = input("Hello! What is your name? ")
    name = name.title()
    highscore = None
    print("Hi, {}! Welcome to the Number Guessing Game!".format(name))
    # Kick off the program by calling the start_game function.
    start_game(highscore)
