# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y
# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main function to take user input and perform calculations
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take user input for operation
    choice = input("Enter operation number (1/2/3/4): ")

    # Take user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations based on user choice
    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    else:
        print("Invalid Input")

# Run the calculator
if __name__ == "__main__":
    main()
