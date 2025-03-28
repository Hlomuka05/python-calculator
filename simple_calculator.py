# Simple Python Calculator

# Ask user for input
num1 = float(input("Enter the first number: 10 "))  
num2 = float(input("Enter the second number:5 "))  
operation = input("Enter the operation (+, -, *, /): + ")  

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation."

# Print the result
print(f"{num1} {operation} {num2} = {result}")
