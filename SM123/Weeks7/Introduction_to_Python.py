"""
Python 1: Introduction to Python
SM123 Physics and Space

Summary:
This module introduces Python programming fundamentals for physical science applications.
Programming moves you from passive to active computer use - a key skill for all physical scientists.
Learning to code develops analytical thinking by breaking problems into logical steps.

Key Learning Outcomes:
- Design simple algorithms to perform basic actions in Python
- Write Python programs for arithmetic operations
- Write programs with conditional execution (if/else)
- Understand good practice in software development

Estimated Study Time: 7 hours
"""

# =============================================================================
# PART 1: VARIABLES AND ASSIGNMENT
# =============================================================================

# Variables store data using the assignment operator (=)
mass = 10.0          # A floating point number (decimal)
num_objects = 5      # An integer (whole number)
name = "Physics"     # A string (text)

# Variable names should clearly identify what they represent
acceleration_gravity = 9.81  # m/s^2

# =============================================================================
# PART 2: ARITHMETIC OPERATORS
# =============================================================================

# Basic arithmetic operators: +, -, *, /, **
a = 10
b = 3

addition = a + b         # 13
subtraction = a - b      # 7
multiplication = a * b   # 30
division = a / b         # 3.333...
power = a ** b           # 10^3 = 1000

# Example: Calculate weight from mass
mass = 50  # kg
g = 9.81   # m/s^2
weight = mass * g  # in Newtons
print(f"Weight = {weight} N")

# =============================================================================
# PART 3: DATA TYPES
# =============================================================================

# Integers - whole numbers
count = 42

# Floating point - decimal numbers  
pi_approx = 3.14159

# Strings - text (in quotes)
message = "Hello, Physics!"

# Converting between types
number_string = "123"
number_int = int(number_string)     # Convert string to integer
number_float = float(number_string) # Convert string to float

# =============================================================================
# PART 4: DATA STRUCTURES - LISTS
# =============================================================================

# Lists store multiple values
measurements = [2.5, 3.1, 2.8, 3.0, 2.9]

# Useful list functions
total = sum(measurements)           # Sum all values
count = len(measurements)           # Number of items
average = total / count             # Calculate average

print(f"Total: {total}, Count: {count}, Average: {average}")

# =============================================================================
# PART 5: ITERATION - FOR LOOPS
# =============================================================================

# For loop - repeat for each item in a sequence
print("For loop example:")
for measurement in measurements:
    print(f"  Value: {measurement}")

# For loop with range
print("Range example:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"  i = {i}")

# =============================================================================
# PART 6: ITERATION - WHILE LOOPS
# =============================================================================

# While loop - repeat while condition is True
print("While loop example:")
counter = 0
while counter < 3:
    print(f"  Counter = {counter}")
    counter = counter + 1  # Don't forget to update!

# =============================================================================
# PART 7: SELECTION - IF/ELSE STATEMENTS
# =============================================================================

# If-else for conditional execution
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
else:
    print("It's cold!")

# =============================================================================
# PART 8: COMPARISON AND BOOLEAN OPERATORS
# =============================================================================

# Comparison operators: >, <, ==, !=, >=, <=
x = 5
y = 10

print(f"x > y: {x > y}")      # False
print(f"x < y: {x < y}")      # True
print(f"x == y: {x == y}")    # False (note: == not =)
print(f"x != y: {x != y}")    # True

# Boolean values: True, False
is_positive = x > 0  # True

# Combination operators: and, or
if x > 0 and y > 0:
    print("Both are positive")

if x > 100 or y > 5:
    print("At least one condition is True")

# =============================================================================
# PART 9: INPUT AND OUTPUT
# =============================================================================

# Output to screen - print function
print("This is output")
print("The value is:", weight, "Newtons")
print(f"Formatted: weight = {weight:.2f} N")  # 2 decimal places

# Input from keyboard - input function (returns a string!)
# Uncomment below to test interactively:
# user_input = input("Enter a number: ")
# number = float(user_input)  # Convert string to number
# print(f"You entered: {number}")

# =============================================================================
# PART 10: MATH MODULE FUNCTIONS
# =============================================================================

import math

# Mathematical constants
print(f"pi = {math.pi}")
print(f"e = {math.e}")

# Mathematical functions
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"sin(pi/2) = {math.sin(math.pi/2)}")
print(f"cos(0) = {math.cos(0)}")
print(f"exp(1) = {math.exp(1)}")
print(f"log(e) = {math.log(math.e)}")
print(f"log10(100) = {math.log10(100)}")

"""
Math Module Functions Reference:
-------------------------------
factorial(x)  - The factorial of x
exp(x)        - e to the power x
log(x)        - Natural logarithm (base e)
log10(x)      - Logarithm base 10
sin(x)        - Sine (x in radians)
cos(x)        - Cosine (x in radians)
tan(x)        - Tangent (x in radians)
asin(x)       - Arcsine (returns radians)
acos(x)       - Arccosine (returns radians)
atan(x)       - Arctangent (returns radians)
sqrt(x)       - Square root
e             - Euler's number (2.71828...)
pi            - Pi (3.14159...)
"""

# =============================================================================
# PART 11: COMMENTS
# =============================================================================

# Single line comments start with #
# Use comments to explain what your code does

# Good comment example:
# Calculating the weight from the mass and acceleration due to gravity
weight = mass * g

# Bad comment example (not helpful):
# Here I multiply two numbers
result = a * b

# =============================================================================
# GOOD PROGRAMMING PRACTICE
# =============================================================================

"""
1. VALIDATION AND VERIFICATION
   - Test your code: Does it do what you want?
   - Test your code: Does it do it correctly?
   - Use simple test cases with known answers

2. CLARITY OF CODE AND COMMENTING
   - Use meaningful variable names (mass, not m)
   - Add clear comments explaining the purpose
   - Organize code logically

3. DOCUMENTATION
   - Explain what the program does
   - Describe required inputs and outputs
   - Note any limitations or dependencies
"""

# =============================================================================
# EXAMPLE: COMPLETE PHYSICS CALCULATION
# =============================================================================

# Calculate the force on a charged particle in an electric field
# F = Q * E (Force = Charge * Electric field strength)

charge = 1.602e-19  # Coulombs (electron charge)
electric_field = 1.0e5  # N/C

force = charge * electric_field

print(f"\n--- Electric Force Calculation ---")
print(f"Charge: {charge} C")
print(f"Electric field: {electric_field} N/C")
print(f"Force: {force} N")
print(f"Force (scientific): {force:.3e} N")

