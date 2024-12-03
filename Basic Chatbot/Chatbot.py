# Simple Chatbot

import datetime

def get_response(user_input):
    """Generate a response based on user input."""
    user_input = user_input.lower()
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How are you doing?",
        "how are you": "I'm just a program, but I'm here to help you!",
        "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
        "date": f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.",
        "weather": "I'm not connected to a weather service yet, but you can check out the Weather Program we created earlier!",
        "bye": "Goodbye! Have a great day!",
    }

    # Match user input to a response
    for key, value in responses.items():
        if key in user_input:
            return value
    
    # Fallback response
    return "I'm not sure how to respond to that. Could you rephrase?"

def main():
    """Main loop for the chatbot."""
    print("HIE!")
    print("Type 'bye' to exit the conversation.\n")

    while True:
        user_input = input("You: ")
        
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
