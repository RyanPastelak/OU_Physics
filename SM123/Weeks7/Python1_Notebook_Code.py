"""
Python 1: Code Examples from Jupyter Notebooks
SM123 Physics and Space

This file contains all the Python code examples from the Python 1 Jupyter Notebooks.
Source: SM123/python/1/ notebooks
"""

# =============================================================================
# NOTEBOOK 1: INTRODUCTION
# =============================================================================

# --- Section 1.1: Sequence ---
# The simplest Python program is a sequence of instructions

# Example: Adding two numbers
result = 3 + 7  # this line adds two numbers
print ("The sum of 3 and 7 is", result)  # this line prints the results

# Using different mathematical operators
output = ( (3**2) + (4**2) )**0.5  # calculation to determine the value assigned to output 
print (output)                      # this line prints the value of output

# --- Section 1.2: Selection ---
# If/else for conditional execution

# Weight calculation with latitude-dependent gravity
totmass = 10		# total mass in kilograms
latitude = 25		# latitude in degrees (N or S)

# The lines below correspond to an if statement. 
if latitude < 45 :  # if the value of latitude is smaller than 45, execute the line below
  acc = 9.79 		# acceleration in metres/(sec squared)
else:               # if the previous conditition (latitude is smaller than 45) is not fullfilled, 
                    # execute the line below
  acc = 9.82	 	# acceleration in metres/(sec squared)

weight = totmass * acc  # calculation of the weight

print ("Total weight:", weight, "newtons")

# --- More precise with three ranges of latitude ---
totmass = 10  # total mass in kilograms 
latitude = 25  # latitude in degrees (N or S)

if latitude < 30:    # if the value of latitude is smaller than 45, execute the line below
    acc = 9.78       # acceleration in metres/(sec squared) 
elif latitude < 60:  # if the value of latitude is smaller than 60, execute the line below
    acc = 9.81       # acceleration in metres/(sec squared) 
else:                # for all other values of latitude, execute the line below
    acc = 9.83       # acceleration in metres/(sec squared) 
    
weight = totmass * acc 

print ("Total weight:", weight, "newtons")

# --- Section 1.3: Combination (using and/or) ---
totmass = 10  # total mass in kilograms 
latitude = 25  # latitude in degrees (N or S) 

if latitude < 60 and latitude >= 30:  # if the value of latitude is smaller than 60 AND 
                                      # bigger or equal to 30 execute the line below
    acc = 9.81                        # acceleration in metres/(sec squared) 
elif latitude < 30: 
    acc = 9.78                        # acceleration in metres/(sec squared) 
else: 
    acc = 9.83                        # acceleration in metres/(sec squared) 

weight = totmass * acc 

print ("Total weight:", weight, "newtons")


# =============================================================================
# NOTEBOOK 2: ITERATIONS AND BUILT-IN FUNCTIONS
# =============================================================================

# --- Section 2.1: Iteration (while loop) ---

# Example: Count down from 10
count = 10

while count > 0:  # execute the two lines below while count is larger than zero
    print(count)   # print the current value of count on the screen
    count = count - 1  # reduce the value of count by one

print("Lift off!")  # this is not in the while loop block because it is not indented

# --- Section 2.2: Built-in functions ---

# Print function
print("Hello!")   # print() is a function
print("The sum of 3 and 7 is", 10)

# Input function - reads user input as a string
# name = input("What is your name?")  # Commented as requires interactive input
# print("Hello", name, "! Nice to meet you")

# Type conversion functions
# int() converts to integer
# float() converts to floating point

# --- Activity 2.1: Fizz Buzz ---
# Print numbers 1 to 100. For multiples of 3 print "fizz", 
# for multiples of 5 print "buzz", for multiples of both print "fizzbuzz"

"""
Fizz Buzz solution:

count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print("fizzbuzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)
    count = count + 1
"""

# --- Activity 2.2: Euclid's Greatest Common Divisor Algorithm ---
# This is the code from TMA02 Question 1

# Euclid's greatest common divisor algorithm

# Ask user to input two integers
# n= int(input("First integer"))
# m= int(input("Second integer"))

# Demonstration with fixed values:
n = 48
m = 18

print(f"\nEuclid's GCD Algorithm for {n} and {m}:")
original_n, original_m = n, m

while (n != m):
  if (n > m):
    n=n-m
  else: 
    m=m-n
    
print ("The greatest common divisor of the integers provided is",n)


# =============================================================================
# NOTEBOOK 3: CONCLUDING ACTIVITY
# =============================================================================

# --- Summary Activity: Kinetic Energy Calculation ---
# Kinetic energy = 0.5 * mass * velocity^2

# Using a fixed mass for demonstration
mass = 10.0  # kg

print("\nKinetic Energy Calculation:")
print(f"Mass = {mass} kg")
print("-" * 30)

# Calculate kinetic energy for speeds 1.0, 2.0, 3.0, 4.0 m/s
speed = 1.0
while speed <= 4.0:
    kinetic_energy = 0.5 * mass * speed**2
    print(f"Speed = {speed} m/s, Kinetic Energy = {kinetic_energy} J")
    speed = speed + 1.0

# Alternative using for loop (from later Python topics)
print("\nUsing a for loop:")
for speed in [1.0, 2.0, 3.0, 4.0]:
    kinetic_energy = 0.5 * mass * speed**2
    print(f"Speed = {speed} m/s, Kinetic Energy = {kinetic_energy} J")


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

"""
VARIABLES AND ASSIGNMENT
-------------------------
- Use = to assign a value to a variable
- Variable names should be meaningful
- Python is case-sensitive (count != Count != COUNT)

MATHEMATICAL OPERATORS
----------------------
+   Addition
-   Subtraction
*   Multiplication
/   Division
**  Power (exponentiation)
%   Modulo (remainder)

COMPARISON OPERATORS
--------------------
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to (note: double equals!)
!=  Not equal to

SELECTION (IF/ELIF/ELSE)
------------------------
if condition:
    # execute if condition is True
elif another_condition:
    # execute if previous conditions were False and this is True
else:
    # execute if all conditions were False

ITERATION (WHILE LOOP)
----------------------
while condition:
    # execute while condition is True
    # IMPORTANT: update variables to eventually make condition False!

COMBINATION OPERATORS
---------------------
and   - Both conditions must be True
or    - At least one condition must be True

BUILT-IN FUNCTIONS
------------------
print()   - Display output on screen
input()   - Read input from keyboard (returns a string)
int()     - Convert to integer
float()   - Convert to floating point number

COMMENTS
--------
# Single line comment (everything after # is ignored)

'''
Multi-line comment
using triple quotes
'''
"""
