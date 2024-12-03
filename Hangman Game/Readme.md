# **Hangman Game**

Hangman is a timeless word-guessing game that has entertained people for generations. This Python implementation brings the classic game to life on the command line, providing an engaging and interactive experience for players.

---

## **Overview**

The Hangman game challenges players to guess a hidden word, letter by letter. Players have a limited number of attempts, and each incorrect guess reduces the remaining chances. The goal is to guess the entire word before running out of attempts.

---

## **How to Play**

1. **Start the Game**:
   - Run the script in your terminal to begin the game.

2. **Objective**:
   - Guess the hidden word by entering one letter at a time.

3. **Gameplay**:
   - You have six attempts to guess the word.
   - After each guess:
     - Correct guesses reveal the positions of the letter in the word.
     - Incorrect guesses reduce the number of attempts left.
   - You can view the progress of the word, guessed letters, and the remaining attempts after each round.

4. **Winning and Losing**:
   - Win: Guess all the letters in the word before running out of attempts.
   - Lose: Use up all your attempts without guessing the word.

---

## **Features**

### **1. Random Word Selection**
The program selects a random word from a predefined list. This ensures variety in gameplay, and the word list can easily be expanded.

### **2. Interactive Feedback**
The game provides real-time feedback for each guess:
- Displays the current progress of the word.
- Informs the player whether the guessed letter is correct or incorrect.
- Tracks the letters guessed so far.

### **3. Limited Attempts**
Players are given six attempts to guess the word, adding an element of challenge and urgency.

### **4. Progress Display**
After every guess, the game shows:
- The current state of the word (e.g., `_ _ a _ _ _`).
- The letters guessed so far.
- The number of attempts remaining.

### **5. Simple and User-Friendly**
The program runs entirely in the terminal, requiring no additional setup or graphical interface.

---

## **Example Gameplay**

Below is an example of a game session:

```plaintext
Welcome to Hangman!

_ _ _ _ _ _ _
Attempts left: 6
Guessed letters: None

Enter a letter: p
Good job! 'p' is in the word.

p _ _ _ _ _ _
Attempts left: 6
Guessed letters: p

Enter a letter: x
Oops! 'x' is not in the word.

p _ _ _ _ _ _
Attempts left: 5
Guessed letters: p, x

Enter a letter: y
Good job! 'y' is in the word.

p y _ _ _ _ _
Attempts left: 5
Guessed letters: p, x, y

...

Congratulations! You guessed the word: python
```

---

## **How to Run the Game**

### **Prerequisites**
Ensure that you have Python installed on your computer. This program works with Python 3.6 and above.

### **Steps to Run**
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `hangman.py` file.
3. Run the following command:
   ```bash
   python hangman.py
   ```

---

## **Customization**

### **Modify the Word List**
The word list is defined in the `choose_word()` function. You can expand the list to include your own words:

```python
words = ["python", "hangman", "programming", "challenge", "development", "your_custom_word"]
```

### **Change the Number of Attempts**
The default number of attempts is 6. You can modify this by changing the `attempts_left` variable in the `play_hangman()` function:

```python
attempts_left = 8  # Change to your desired number of attempts
```

---

## **Key Concepts Used in the Code**

1. **Randomization**:
   - The `random.choice()` function is used to select a random word from the word list.

2. **String Manipulation**:
   - The current progress of the word is displayed using list comprehensions to replace unguessed letters with underscores (`_`).

3. **Sets for Tracking**:
   - Guessed letters are stored in a set to efficiently track and prevent duplicate guesses.

4. **Looping and Conditionals**:
   - A `while` loop manages the game flow, checking for win/loss conditions after each guess.

5. **User Input Validation**:
   - Input is validated to ensure it’s a single alphabetical character.

---

## **Future Enhancements**
Here are some ideas to expand the game:
- Add a graphical representation of the hangman using ASCII art.
- Allow players to choose difficulty levels, where each level has words of varying lengths or attempts.
- Include hints or clues for the word to make the game more engaging.
- Enable saving and resuming game progress.

---

Dive in and have fun guessing the word! Let me know if you have suggestions or feedback to improve the game. 😊