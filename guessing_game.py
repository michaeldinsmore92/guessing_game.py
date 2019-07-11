"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

# THINGS TO CORRECT:
    # 1 ... script crashes with exception. enter "hello" when asked for num

import random
import sys

def play_again():
    play_again = input("Would you like to play again? Y/N ")
    if play_again.lower() != "n":
        start_game()
    else:
        print("Thank you for playing, {}. Goodbye!".format(name))
        sys.exit()

def start_game():
    # Store a random number as the answer/solution.
    ANSWER = random.randint(1,10)
    attempts = 1
    guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
    # Continuously prompt the player for a guess.
    try:
        guess = int(guess)
    except ValueError as err:
        print("Uh oh! That's not a valid value. Please try again...".format(err))
        start_game()
    except TypeError as err:
        print("Uh oh! That's not a valid value. Please try again...".format(err))
        start_game()  
    while guess != ANSWER:
        try:
            if guess > 10 or guess < 1:
                print("That number is out of range! Choose a number between 1 and 10...")
                attempts += 1
                guess = int(input("I am thinking of a number between 1 and 10, including both. Take a guess! "))
        #   If the guess greater than the solution, display to the player "It's lower".
            elif guess > ANSWER:
                print("It's lower...")
                attempts += 1
                guess = int(input("I am thinking of a number between 1 and 10, including both. Take a guess! "))
        #   If the guess is less than the solution, display to the player "It's higher".
            elif guess < ANSWER:
                print("It's higher...")
                attempts += 1
                guess = int(input("I am thinking of a number between 1 and 10, including both. Take a guess! "))
        except ValueError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))
        except TypeError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))            
    #   Once the guess is correct, stop looping, inform the user they "Got it"
    if guess == ANSWER:
        print("You got it, {}!".format(name))
        print("It took you {} attempts.".format(attempts))
        play_again()

if __name__ == '__main__':
    # Display an intro/welcome message to the player.
    name = input("Hello! What is your name? ")
    print("Hi, {}! Welcome to the Number Guessing Game!".format(name))
    print("There isn't a high score to beat... yet!")
    # Kick off the program by calling the start_game function.
    start_game()
