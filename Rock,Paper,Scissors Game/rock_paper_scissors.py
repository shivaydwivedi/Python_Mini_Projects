# Rock, Paper, Scissors Game

import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nEnter your choice:")
        print("rock, paper, scissors, or 'q' to quit")
        
        user_choice = input("Your choice: ").strip().lower()
        
        if user_choice == 'q':
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
