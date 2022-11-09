"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    input_string = input("What would you like to calculate? ")
    tokens = input_string.split(' ')
        
    if "q" in tokens:
        print("Exiting calculator")
        break
    elif len(tokens) < 2:
        print("Not enough information")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"
    else: 
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    if tokens[1].isalpha():
        print("That's not a number")
        continue
 
    if "+" in tokens:
        print(add(float(num1), float(num2)))

    elif "-" in tokens:
        print(subtract(float(num1), float(num2)))

    elif "*" in tokens:
        print(multiply(float(num1), float(num2)))

    elif "/" in tokens:
        print(divide(float(num1), float(num2)))
    
    elif "square" in tokens:
        print(square(float(num1)))

    elif "cube" in tokens:
        print(cube(float(num1)))

    elif "power" in tokens:
        print(power(float(num1), float(num2)))

    elif "mod" in tokens:
        print(mod(float(num1), float(num2)))

    else: 
        print("Please enter an operator or a command and two numbers")
        