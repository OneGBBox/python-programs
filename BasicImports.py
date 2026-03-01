# Pattern 1 - Basic Imports
# This file contains basic Python functions that can be imported into other scripts.

from math import sqrt  # Example of importing a specific function from the math module
# Example of importing the datetime class from the datetime module
from datetime import datetime
import math
import random
math.sqrt(16)  # Example of using the math module

# pattern 2 - Importing specific functions
print("Square root of 16 is", sqrt(16))
print("Cosine of 0 is", math.cos(0))
print("Sine of 0 is", math.sin(0))
print("Tangent of 0 is", math.tan(0))

print("Current date and time is", datetime.now())
print("Current year is", datetime.now().year)
print("Current month is", datetime.now().month)
print("Current day is", datetime.now().day)
# Using the walrus operator to assign and print the date
print(today := datetime.now().date())
print("Current time is", datetime.now().time())
print(today.strftime("%Y-%m-%d"))  # Formatting the date as a string

print("Random number between 1 and 10 is", random.randint(1, 10))
# Example of using random.choice
print(random.choice(['apple', 'banana', 'cherry']))
