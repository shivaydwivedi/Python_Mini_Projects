# Guessing Game

import random

def guessing_game():
    print("Welcome to the Guessing Game!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    guessing_game()
