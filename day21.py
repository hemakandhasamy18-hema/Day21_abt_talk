# Week 3 Sprint Challenge
# Recursion + Stack
# No sort(), sum(), max(), min()

# --------------------------------
# 1. RECURSION - FACTORIAL
# --------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# --------------------------------
# 2. STACK - BALANCED PARENTHESES
# --------------------------------

def is_balanced(expression):
    stack = []

    for char in expression:

        # Opening brackets
        if char == '(' or char == '[' or char == '{':
            stack.append(char)

        # Closing brackets
        elif char == ')' or char == ']' or char == '}':

            # No opening bracket available
            if len(stack) == 0:
                return False

            top = stack.pop()

            # Check matching brackets
            if char == ')' and top != '(':
                return False

            if char == ']' and top != '[':
                return False

            if char == '}' and top != '{':
                return False

    # Stack should be empty
    if len(stack) == 0:
        return True

    return False


# --------------------------------
# MAIN PROGRAM
# --------------------------------

print("===== WEEK 3 SPRINT CHALLENGE =====")

# Recursion
number = int(input("\nEnter a number for factorial: "))

if number < 0:
    print("Factorial is not possible for negative numbers.")
else:
    result = factorial(number)
    print("Factorial of", number, "=", result)


# Stack
expression = input("\nEnter brackets to check: ")

if is_balanced(expression):
    print("Result: Balanced")
else:
    print("Result: Not Balanced")