"""
Python 4: Code Examples from Jupyter Notebooks
SM123 Physics and Space

This file contains all the Python code examples from the Python 4 Jupyter Notebooks.
Source: SM123/python/4/ notebooks
Focus: Data Analysis, Reading Files, Linear Fitting, Quality of Fit
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

# =============================================================================
# NOTEBOOK 1: REVISION AND NEW COMMANDS
# =============================================================================

# --- Section 1.1: Operating with arrays (Revision) ---

x = np.array([0.053, 0.042, 0.029, 0.025], float)
F = np.array([7.05, 5.93, 4.08, 4.01], float)

print('Sum of F:', sum(F))
print('Length of x:', len(x))
print('Ratio F/x:', F/x)


# --- Section 1.2: Plotting appearance ---

x_values = np.array([1, 2, 3, 4, 5], float)
y_values = np.array([1.9, 2.1, 3.6, 4.2, 4.9], float)

# Plot using red squares ('sr')
plt.figure()
plt.plot(x_values, y_values, 'sr')

# Other symbols: 'o' circle, '^' triangle up, 'D' diamond
# Colors: 'b' blue, 'g' green, 'r' red, 'k' black
# Example: Blue triangles
plt.plot(x_values, y_values * 0.5, '>b') 


# --- Section 1.3 & 1.4: Saving plots and labels ---

plt.xlabel('time / seconds')
plt.ylabel('position / metres')
plt.title('Plotting Symbols Example')
# plt.savefig("figure.png") # Saves to file


# --- Section 1.5: Reading from a CSV file ---

# Assuming 'Extension_force.csv' exists with columns 'Extension' and 'Force'
# This code block demonstrates the pattern:

extension_list = []
force_list = []

# Uncomment to run if file exists
# with open('Extension_force.csv', mode='r') as input_file:
#     data = csv.DictReader(input_file)
#     for row in data:
#         extension_list.append(row['Extension'])
#         force_list.append(row['Force'])

# Convert to arrays for analysis
# x_array = np.array(extension_list, float)
# F_array = np.array(force_list, float)


# =============================================================================
# NOTEBOOK 2: FITTING A STRAIGHT LINE
# =============================================================================

# --- Section 2.1: Using polyfit ---

# Data
x_data = np.array([0.053, 0.042, 0.029, 0.002], float)
y_data = np.array([7.05, 5.93, 4.08, 0.452], float)

# Fit a polynomial of degree 1 (straight line: y = mx + c)
# Returns [gradient, intercept]
grad, intc = np.polyfit(x_data, y_data, deg=1)

print(f"Gradient: {grad}")
print(f"Intercept: {intc}")

# Plot data and best-fit line
plt.figure()
plt.plot(x_data, y_data, 'sr', label='Data')
plt.plot(x_data, x_data * grad + intc, 'b-', label='Fit')
plt.legend()


# --- Activity 2.1: Hubble Constant (Skeleton) ---

def fit_hubble_law(distances, velocities):
    """
    Perform linear fit to find Hubble Constant.
    v = H0 * d  (intercept should be near 0)
    """
    coeffs = np.polyfit(distances, velocities, 1)
    H0 = coeffs[0]
    intercept = coeffs[1]
    return H0, intercept

# Example Usage
d_vals = np.array([10, 20, 50], float) # Mpc
v_vals = np.array([700, 1500, 3400], float) # km/s

H0, c = fit_hubble_law(d_vals, v_vals)
print(f"Hubble Constant H0: {H0:.2f} km/s/Mpc")


# =============================================================================
# NOTEBOOK 3: ASSESSING QUALITY OF FIT
# =============================================================================

# --- Section 3.1: Root Mean Square Deviation (RMSD) ---

def rmsd(y_data, y_model):
    """
    Calculate Root Mean Square Deviation.
    RMSD = sqrt( mean( (y_observed - y_calculated)^2 ) )
    """
    dev = y_data - y_model
    square_dev = dev**2
    sum_square_dev = sum(square_dev)
    mean_square_dev = sum_square_dev / len(square_dev)
    root_mean_square_dev = np.sqrt(mean_square_dev)
    return root_mean_square_dev

# Using the previous fit
y_model_vals = x_data * grad + intc
error = rmsd(y_data, y_model_vals)
print(f"RMSD of fit: {error}")


# --- Section 3.2: Rydberg Constant Activity (Skeleton) ---

"""
Theory: E_photon = R/nf^2 - R * (1/ni^2)
Fit equation: y = b + ax
    y = E_photon
    x = 1/ni^2
    a = -R  (Gradient)
    b = R/nf^2 (Intercept)
"""

def analyze_hydrogen_spectrum(ni_values, energy_values):
    # Prepare x axis values
    x_axis = 1.0 / (ni_values**2)
    
    # Fit line
    gradient, intercept = np.polyfit(x_axis, energy_values, 1)
    
    # Extract constants
    R = -gradient
    nf = np.sqrt(R / intercept)
    
    return R, nf

# Example Data
ni = np.array([3, 4, 5, 6], float)
E = np.array([3.03e-19, 4.09e-19, 4.58e-19, 4.84e-19], float) # Approx values

R_calc, nf_calc = analyze_hydrogen_spectrum(ni, E)
print(f"Calculated Rydberg Constant: {R_calc:.2e}")
print(f"Calculated Final State n_f: {nf_calc:.2f}")


# =============================================================================
# KEY CONCEPTS SUMMARY
# =============================================================================

"""
DATA ANALYSIS WORKFLOW
----------------------
1. Read Data:
   - Use csv.DictReader to read CSV files into lists.
   - Convert lists to numpy arrays for calculation.

2. Plot Data:
   - Use symbols (e.g., 'sr', 'bo') for data points.
   - Always label axes (plt.xlabel, plt.ylabel).

3. Fit Model:
   - Use np.polyfit(x, y, 1) for linear regression.
   - Returns [gradient, intercept].
   - Construct model values: y_model = gradient * x + intercept.

4. Assess Fit:
   - Plot data vs best-fit line.
   - Calculate RMSD to quantify error.
   - Save figures using plt.savefig().
"""
