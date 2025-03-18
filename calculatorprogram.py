def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()

        operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2 if num2 != 0 else None}

        if operation in operations:
            result = operations[operation]
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
