"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import sys

def start_game():
    # Display an intro/welcome message to the player.
    name = input("Hello! What is your name? ")
    print("Hi, {}! Welcome to the Number Guessing Game!".format(name))
    # Show the current high score (least amount of points).
    high_score = 5
    print("The current High Score (lowest attempts) is {} attempts.".format(high_score))
    # Store a random number as the answer/solution.
    ANSWER = random.randint(1,10)
    attempts = 1
    # Continuously prompt the player for a guess.
    guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
    while guess != ANSWER:
        try:
            guess = int(guess)
        except ValueError as err:
            print("Uh oh! That's not a valid value. Please try again...".format(err))
            guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
        else:
            #   If the guess is outside the guessing range, try again.
            if guess > 10:
                print("That number is out of range! Choose a number between 1 and 10...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
            elif guess < 1:
                print("That number is out of range! Choose a number between 1 and 10...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
        #   If the guess greater than the solution, display to the player "It's lower".
            elif guess > ANSWER:
                print("It's lower...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
        #   If the guess is less than the solution, display to the player "It's higher".
            elif guess < ANSWER:
                print("It's higher...")
                guess = input("I am thinking of a number between 1 and 10, including both. Take a guess! ")
                guess = int(guess)
                attempts += 1
    #   Once the guess is correct, stop looping, inform the user they "Got it"
    if guess == ANSWER:
        print("You got it, {}!".format(name))
    if attempts < high_score:
        print("Alright! You beat the high score with only {} attempts!".format(attempts))
        play_again = input("Would you like to play again? Y/N ")
        if play_again.lower() == "y":
            start_game()
        else:
            print("Thank you for playing, {}. Goodbye!".format(name))
    else:
        play_again = input("Would you like to play again? Y/N ")
        if play_again.lower() == "y":
            start_game()
        else:
            print("Thank you for playing, {}. Goodbye!".format(name))

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()