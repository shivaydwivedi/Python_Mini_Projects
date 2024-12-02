# Enhanced Command Line Calculator

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    elif operation == '^':
        return num1 ** num2
    else:
        return "Invalid operation"

# Function to display menu and guide the user
def display_menu():
    print("\nWelcome to the Enhanced Command Line Calculator!")
    print("Choose an operation:")
    print(" + : Addition")
    print(" - : Subtraction")
    print(" * : Multiplication")
    print(" / : Division")
    print(" ^ : Exponentiation")
    print(" q : Quit")

# Main function to run the calculator
def main():
    while True:
        display_menu()
        operation = input("\nEnter operation: ").strip()
        
        if operation.lower() == 'q':
            print("Thank you for using the calculator! Goodbye!")
            break
        
        if operation in ['+', '-', '*', '/', '^']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculate(num1, num2, operation)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid operation! Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()
