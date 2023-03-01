"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
print("Please provide prefix notation equation.")
print("If only 1 operand provided we'll use 0 for operand 2.")
print("Press q to quit.")


while True:
    user_input = input("Equation: ")
    tokens = user_input.split(' ')
    if 'q' in tokens:
        break
    if len(tokens) < 2:
        print("Please provide operands.")
        continue

    operator = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2] if len(tokens) > 2 else "0"

    if not num1.isdigit() or not num2.isdigit():
        print("Please provide numbers.")
        continue

    num1 = float(num1)
    num2 = float(num2)

    result = None

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    elif operator == "square":
        result = square(num1)
    elif operator == "cube":
        result = cube(num1)
    elif operator == "pow":
        result = power(num1, num2)
    elif operator == "mod":
        result = mod(num1, num2)
    else:
        print("Please review available operations and try again")
        continue

    print(result)
