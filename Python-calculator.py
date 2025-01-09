def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

def calculator():
    """Simple calculator that performs basic arithmetic operations."""
    while True:
        # Display the menu
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Exit the calculator
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Ensure the choice is valid
        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice. Please select a valid operation.")
            continue

        # Get user input for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the operation
        if choice == '1':
            print("The sum is:", add(num1, num2))
        elif choice == '2':
            print("The difference is:", subtract(num1, num2))
        elif choice == '3':
            print("The product is:", multiply(num1, num2))
        elif choice == '4':
            print(divide(num1, num2))

# Run the calculator
if __name__ == "__main__":
    calculator()
