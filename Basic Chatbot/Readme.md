
# **Basic Chatbot**

## **Overview**

The **Basic Chatbot** is a simple Python-based interactive chatbot that uses predefined responses to interact with the user. It doesn't rely on complex AI or external APIs, making it ideal for beginners to learn the fundamentals of Python programming, such as handling user input, using conditionals, and implementing loops.

This chatbot can provide responses to a few basic inputs like greetings and exit commands, and will also handle unrecognized inputs with a default message.

---

## **Features**

- **Predefined Responses**: The chatbot responds to common phrases like `hello`, `how are you`, and `bye`.
- **Exit Command**: Typing `bye` will end the conversation gracefully.
- **Handles Unrecognized Input**: If the chatbot doesn't recognize the input, it will respond with a default message: "Sorry, I didn't understand that."
- **Easy to Customize**: You can easily expand the chatbot's knowledge by adding more responses to the code.

---

## **How It Works**

The chatbot uses simple conditional statements to check if the user input matches any of the predefined responses. If a match is found, it returns the appropriate response. If no match is found, it will return a default message.

The bot continues to interact with the user in a loop until the user types `bye`, which will stop the program.

---

## **Installation & Setup**

To get started with the chatbot, follow these steps:

1. **Clone or Download the Repository**:
    - Clone the repository to your local machine using Git:
      ```bash
      git clone https://github.com/yourusername/Basic-Chatbot.git
      ```
    - Or download the project as a ZIP file and extract it.

2. **Ensure Python is Installed**:
    - This project requires Python 3.6 or higher. You can download Python from [here](https://www.python.org/downloads/).
    - To check if Python is installed, run the following command in your terminal:
      ```bash
      python --version
      ```

3. **Running the Chatbot**:
    - Open your terminal or command prompt.
    - Navigate to the folder where the chatbot script is located.
    - Run the chatbot by executing the following command:
      ```bash
      python Chatbot.py
      ```

---

## **How to Play**

1. **Start the Chatbot**:
   - Run the `Chatbot.py` script.
   - The chatbot will welcome you and prompt you for input.

2. **Interact with the Chatbot**:
   - You can type a variety of inputs, and the chatbot will respond accordingly:
     - Type `hello` → The chatbot will greet you.
     - Type `how are you` → The chatbot will respond that it is doing fine.
     - Type `bye` → The chatbot will end the conversation.

3. **Unrecognized Input**:
   - If you type something that the chatbot doesn't recognize, it will respond with:
     ```
     Sorry, I didn't understand that.
     ```

4. **Exit the Conversation**:
   - Type `bye` to exit the conversation and close the program.

---

## **Example Interaction**

Here’s an example of what the interaction might look like:

```
Welcome to the Basic Chatbot!
Type 'bye' to exit the conversation.

You: hello
Chatbot: Hi there! How can I help you today?

You: how are you
Chatbot: I'm just a bot, but I'm doing fine. Thanks for asking!

You: what is your name?
Chatbot: Sorry, I didn't understand that.

You: bye
Chatbot: Goodbye! Have a great day!
```

---

## **Customization**

- **Add More Responses**: To extend the chatbot's capabilities, you can easily add more responses by updating the `basic_responses` dictionary inside the `get_basic_response()` function.
  
  For example:
  ```python
  basic_responses = {
      "hello": "Hi there! How can I help you today?",
      "bye": "Goodbye! Have a nice day!",
      "how are you": "I'm just a bot, but I'm doing fine. Thanks for asking!",
      "your name": "I am a chatbot created by you!",
      # Add more responses here
  }
  ```

- **Improve the Responses**: You can modify the responses to be more dynamic or conversational by updating the text associated with each user input.

---

## **Contributing**

If you'd like to contribute to the project, feel free to:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and add meaningful commits.
4. Open a pull request to merge your changes into the main branch.

---

## **Licenses**

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## **Troubleshooting**

### 1. **Chatbot Not Responding**:
- Make sure you're typing one of the recognized inputs (`hello`, `how are you`, `bye`, etc.).
- Ensure that the program is running without errors. If you see an error, check the Python version and ensure there are no issues in the code.

### 2. **Unexpected Behavior**:
- If the chatbot isn't responding as expected, check the `basic_responses` dictionary and make sure the keys (user inputs) and values (responses) are correct.

---

