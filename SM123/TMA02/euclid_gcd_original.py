# Euclid's greatest common divisor algorithm
# From SM123 Python 1, Notebook 2, Activity 2.2

# Ask user to input two integers
# These two lines prompt user to input two integers. Reads them in as a string, converts to integer and stores in n and m.
n= int(input("First integer"))
m= int(input("Second integer"))

# This while loop continues executing as long as n is not equal to m. The != operator means "not equal to". The loop terminates when both values become equal.
while (n != m):
  # The if/else checks which value is larger: if n > m, subtract m from n; otherwise subtract n from m. This repeatedly reduces the larger number until both are equal.
  if (n > m):
    n=n-m
  else: 
    m=m-n

# This line prints the GCD. At this point, both n and m contain the same value, which is the greatest common divisor.
print ("The greatest common divisor of the integers provided is",n)