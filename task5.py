#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math
nums = (5,-2,12,-8,14,16)
for i in nums:
    if i > 0:
        ii = i ** 0.5
        print(f"the square root of {i} is {ii}.")
    elif i < 1:
        print(f"{i} is not a positive number; will not squareroot it.")
