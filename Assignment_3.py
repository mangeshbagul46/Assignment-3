# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python
# Task 1: Calculate Factorial Using a Function
#
#
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial
# using a loop or recursion.

'''def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

ans  = factorial(5)
print(f'factorial of 5 is {ans}')
'''


# Task 2: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results

from math import *

user = int(input("Enter a number :"))
print("square root :", sqrt(user))
print('logarithm :', log(user))
print("sine :", sin(user))