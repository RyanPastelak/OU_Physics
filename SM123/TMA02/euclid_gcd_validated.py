# Euclid's greatest common divisor algorithm
# With input validation - TMA02 Question 1(b)
# From SM123 Python 1, Notebook 2, Activity 2.2

# Ask user to input first integer with validation
# This line prompts user to input the first integer. Reads it in as a string, converts to integer and stores in n.
n = int(input("First integer"))
# This while loop checks if n is less than or equal to 0. If so, it displays an error and prompts the user again until a valid positive integer is entered.
while n <= 0:
    print("Error: Please enter an integer greater than zero.")
    n = int(input("First integer"))

# Ask user to input second integer with validation
# This line prompts user to input the second integer. Reads it in as a string, converts to integer and stores in m.
m = int(input("Second integer"))
# This while loop checks if m is less than or equal to 0. If so, it displays an error and prompts the user again until a valid positive integer is entered.
while m <= 0:
    print("Error: Please enter an integer greater than zero.")
    m = int(input("Second integer"))

# This while loop continues executing as long as n is not equal to m. The != operator means "not equal to". The loop terminates when both values become equal.
while (n != m):
  # The if/else checks which value is larger: if n > m, subtract m from n; otherwise subtract n from m. This repeatedly reduces the larger number until both are equal.
  if (n > m):
    n=n-m
  else: 
    m=m-n

# This line prints the GCD. At this point, both n and m contain the same value, which is the greatest common divisor.
print ("The greatest common divisor of the integers provided is",n)
