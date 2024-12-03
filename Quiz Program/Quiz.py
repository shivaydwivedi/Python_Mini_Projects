# Quiz Program

def display_welcome():
    """Display a welcome message."""
    print("Welcome to the Quiz Program!")
    print("Answer the questions to the best of your ability.")
    print("Type the letter of your choice (a, b, c, or d) and press Enter.\n")

def load_questions():
    """Load a list of quiz questions."""
    return [
        {
            "question": "What is the capital of France?",
            "choices": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
            "correct": "a"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
            "correct": "b"
        },
        {
            "question": "What is the largest mammal?",
            "choices": ["a) Elephant", "b) Blue Whale", "c) Great White Shark", "d) Giraffe"],
            "correct": "b"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "choices": ["a) Mark Twain", "b) Harper Lee", "c) J.K. Rowling", "d) Jane Austen"],
            "correct": "b"
        },
        {
            "question": "What is the square root of 64?",
            "choices": ["a) 6", "b) 7", "c) 8", "d) 9"],
            "correct": "c"
        }
    ]

def ask_question(question, choices):
    """Ask a single question and return the user's response."""
    print(question)
    for choice in choices:
        print(choice)
    answer = input("\nYour answer: ").lower()
    return answer

def main():
    display_welcome()
    questions = load_questions()
    score = 0
    
    for index, item in enumerate(questions, start=1):
        print(f"\nQuestion {index}:")
        user_answer = ask_question(item["question"], item["choices"])
        
        if user_answer == item["correct"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {item['correct']}.")
    
    print("\nQuiz Complete!")
    print(f"Your final score is: {score}/{len(questions)}.")
    
    if score == len(questions):
        print("🎉 Excellent! You got everything correct!")
    elif score >= len(questions) // 2:
        print("👍 Good job! You passed the quiz.")
    else:
        print("😔 Better luck next time. Keep practicing!")

if __name__ == "__main__":
    main()
