"""
Python 3: Code Examples from Jupyter Notebooks
SM123 Physics and Space

This file contains all the Python code examples from the Python 3 Jupyter Notebooks.
Source: SM123/python/3/ notebooks
Focus: Numpy Arrays and Plotting with Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# NOTEBOOK 1: ARRAYS
# =============================================================================

# --- Section 1.1: Defining an array ---

# Create array with integer numbers
a = np.array([1, 7, 4, 3], int)
print("Array a:", a)

# Create array with real numbers (float)
a_float = np.array([2.0, 4.0, 8.0])
print("Array a_float:", a_float)

# Specifying type explicitly
b = np.array([2, 4, 8], float)
print("Array b:", b)

# Convert list to array
items = [1.45, 2, 0.25, 4.4, 1.9]
mass_of_items = np.array(items, float)
print("Mass of items:", mass_of_items)


# --- Section 1.2: Initialising arrays ---

# Array of zeros
initial_values = np.zeros(6, int)
print("Zeros array:", initial_values)

# Empty array (values are uninitialized garbage until set)
c = np.empty(5, float)
c[0] = 1.3
c[1] = c[0] + 3.1
print("Partially filled array c:", c)


# --- Section 1.3: Functions that work on arrays ---

a = np.array([1.9, 7.1, 4.6, 3.2, 1.9], float)

# Print specific element (index starts at 0)
print("Second element (index 1):", a[1])

# Length of array
print("Length:", len(a))

# Sum of elements
print("Sum:", sum(a))


# --- Section 1.4: Operating on arrays ---

# Adding a scalar to all elements
temperature = np.array([17.5, 12.1, 23.0], float)
increase = float(input("What is the temperature increase? (e.g., 2.5): "))
new_temperature = temperature + increase
print("New temperatures:", new_temperature)

# Using arrays in loops vs vector operations
power = np.array([2, 4, 6, 8, 10], int)
for p in power:
    print(f"2 to the power {p} is {2**p}")

# Operating on specific element
temperature[1] = temperature[1] + 0.1
print("Modified temperature array:", temperature)


# --- Section 1.5: Working with multiple arrays ---

mass = np.array([3.1, 0.98, 2.6, 154], float)
speed = np.array([0.21, 1.63, 0.88, 0.76], float)

# Multiply arrays element-wise
momentum = mass * speed
print("Momentum:", momentum, "kg m/s")

# Adding two arrays
increase_array = np.array([0.1, 0.4, 0.3], float)
# Note: arrays must be same size
# new_temp = temperature + increase_array 
# print(new_temp)


# --- Section 1.7: Arrays and matrices (2D arrays) ---

# Create 4x2 array of zeros
initial_values_2d = np.zeros([4, 2], int)
print("2D zeros:\n", initial_values_2d)

# Assign values
initial_values_2d[0, 0] = 1
initial_values_2d[1, 1] = 3
print("Modified 2D array:\n", initial_values_2d)

# Create 2D array directly
values_to_add = np.array([[4, 3], [2, 1], [2, 4], [6, 8]], int)
print("Values to add:\n", values_to_add)

# Sum matrices
sum_of_matrices = initial_values_2d + values_to_add
print("Sum:\n", sum_of_matrices)

# Shape and size
print("Shape (rows, cols):", values_to_add.shape)
print("Total elements:", values_to_add.size)


# =============================================================================
# NOTEBOOK 2: PLOTTING WITH PYTHON
# =============================================================================

# --- Section 2.1: The pyplot module ---

# Define x values using linspace (start, stop, number_of_points)
x = np.linspace(-10, 10, 20)
print("x values:", x)

# Calculate y values
y1 = 0.05 * x**3 + 20
y2 = 6 * np.exp(-x**2/10) # Example function

# Plotting
plt.figure() # Create new figure
plt.plot(x, y1)
plt.plot(x, y2)
plt.title("An example of a plot")
# plt.show() # Uncomment to display in script mode


# =============================================================================
# ACTIVITY: RADIOACTIVE DECAY (Possible Solution Structure)
# =============================================================================

"""
Goal: Plot amount of isotope remaining vs time: P = P0 * (1/2)^(t/tau)
"""

def calculate_decay(N0, half_life, time_points):
    """Calculate remaining nuclei."""
    decay_constant = np.log(2) / half_life
    N_t = N0 * np.exp(-decay_constant * time_points)
    return N_t

# Example usage
isotope_name = "Carbon-14"
half_life = 5730 # years
N0 = 1000 
t_max = 5 * half_life
t = np.linspace(0, t_max, 100)

N = calculate_decay(N0, half_life, t)

plt.figure()
plt.plot(t, N, 'b-', label=f'{isotope_name} Decay')
plt.xlabel('Time (years)')
plt.ylabel('Amount Remaining')
plt.title(f'Radioactive Decay of {isotope_name}')
plt.legend()
plt.grid(True)
# plt.savefig('radioactive_decay_plot.png')


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

"""
NUMPY ARRAYS
------------
- Fixed size, same data type (int, float)
- Vector operations (a + b, a * 2) are fast and apply to all elements
- Creation:
    np.array([1, 2, 3])
    np.zeros(5)
    np.empty(5)
    np.linspace(start, end, num_points)
- 2D Arrays: np.zeros([rows, cols]), shape attribute

PLOTTING (matplotlib.pyplot)
----------------------------
- plt.plot(x, y)
- plt.title("Title")
- plt.xlabel("Label"), plt.ylabel("Label")
- plt.show() to display
- plt.savefig("filename.png") to save
"""
