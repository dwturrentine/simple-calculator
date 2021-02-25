
num1 = float(input("Enter first number: "))  # Float allows for input to be a number
op = input("Enter operator: ")  # Operator to perform calculation
num2 = float(input("Enter second number: "))

# Condition check for operator input

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator.")
