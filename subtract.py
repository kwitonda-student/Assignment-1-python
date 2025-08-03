# Ask for two numbers and subtraction operation
num1 = int(input("Enter the first number (20): "))
num2 = int(input("Enter the second number (40): "))
operation = input("Enter the operation (-): ")

# Perform subtraction
if operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
else:
    print("Only subtraction (-) is allowed.")

    
    
    
