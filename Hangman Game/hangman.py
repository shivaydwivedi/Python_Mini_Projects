import random

def choose_word():
    """Choose a random word from a predefined list."""
    words = ["python", "hangman", "programming", "challenge", "development"]
    return random.choice(words)

def display_word_progress(word, guessed_letters):
    """Display the current progress of the guessed word."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    print("Welcome to Hangman!")
    
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts_left = 6
    
    while attempts_left > 0:
        print("\n" + display_word_progress(word_to_guess, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts_left -= 1
            
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
