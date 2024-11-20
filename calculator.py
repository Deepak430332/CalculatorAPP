def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    valid_operations = {
        '1': 'Addition',
        '2': 'Subtraction',
        '3': 'Multiplication',
        '4': 'Division'
    }
    
    while True:
        print("\nAvailable Operations:")
        for key, value in valid_operations.items():
            print(f"{key}: {value}")
        
        choice = input("\nEnter operation number (1-4): ")
        if choice in valid_operations:
            return choice
        print("Invalid choice! Please select a valid operation.")

def calculator():
    print("Welcome to the Calculator App!")
    
    while True:
        # Get operation choice
        operation = get_operation()
        
        # Get number inputs
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        try:
            if operation == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
        
        except ValueError as e:
            print(f"\nError: {e}")
        
        # Ask if user wants to continue
        if input("\nDo you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break
    
    print("\nThank you for using the Calculator App!")

if __name__ == "__main__":
    calculator() 