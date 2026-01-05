"""
Python 2: Functions and Packages
SM123 Physics and Space

Summary:
This module builds on Python 1, introducing more Python commands and structures,
with emphasis on writing programs for physics calculations. Key new concepts include
user-defined functions and the numpy package.

Key Learning Outcomes:
- Design algorithms for physics-related calculations
- Write and use functions as part of programs
- Calculate frequency and wavelength of photons from hydrogen transitions
- Apply good practice in software development

Estimated Study Time: 7 hours
"""

# =============================================================================
# PART 1: PRINT INSTRUCTIONS FOR MULTIPLE VARIABLES
# =============================================================================

# You can print multiple values in a single print statement
mass = 5.0          # kg
velocity = 10.0     # m/s
energy = 0.5 * mass * velocity**2

print("Mass:", mass, "kg")
print("Velocity:", velocity, "m/s")
print("Kinetic energy:", energy, "J")

# Using f-strings for formatted output (recommended)
print(f"An object of mass {mass} kg moving at {velocity} m/s has kinetic energy {energy} J")

# Formatting numbers with specific decimal places
pi = 3.141592653589793
print(f"Pi to 3 decimal places: {pi:.3f}")
print(f"Scientific notation: {energy:.2e}")


# =============================================================================
# PART 2: OPERATIONS WITH LISTS
# =============================================================================

# Creating a list
wavelengths = [400, 450, 500, 550, 600]  # wavelengths in nm

# Accessing elements (zero-indexed)
first_wavelength = wavelengths[0]    # 400
last_wavelength = wavelengths[-1]    # 600
print(f"First wavelength: {first_wavelength} nm")
print(f"Last wavelength: {last_wavelength} nm")

# Slicing lists
middle_values = wavelengths[1:4]     # [450, 500, 550]
print(f"Middle values: {middle_values}")

# Appending to lists
wavelengths.append(650)              # Add 650 to end of list
print(f"Updated list: {wavelengths}")

# List length
num_wavelengths = len(wavelengths)
print(f"Number of wavelengths: {num_wavelengths}")

# Iterating through a list
print("All wavelengths:")
for w in wavelengths:
    print(f"  {w} nm")


# =============================================================================
# PART 3: COMPOUND OPERATORS
# =============================================================================

# These operators modify a variable in place

# Addition assignment (+=)
count = 0
count += 1          # Equivalent to: count = count + 1
print(f"After += 1: count = {count}")

# Subtraction assignment (-=)
temperature = 100
temperature -= 10   # Equivalent to: temperature = temperature - 10
print(f"After -= 10: temperature = {temperature}")

# Multiplication assignment (*=)
value = 5
value *= 3          # Equivalent to: value = value * 3
print(f"After *= 3: value = {value}")

# Division assignment (/=)
distance = 100
distance /= 4       # Equivalent to: distance = distance / 4
print(f"After /= 4: distance = {distance}")

# Power assignment (**=)
base = 2
base **= 3          # Equivalent to: base = base ** 3
print(f"After **= 3: base = {base}")


# =============================================================================
# PART 4: THE abs() FUNCTION
# =============================================================================

# abs() returns the absolute value (removes negative sign)

negative_number = -42
positive_result = abs(negative_number)
print(f"abs({negative_number}) = {positive_result}")

# Useful for calculating differences regardless of order
value1 = 15
value2 = 23
difference = abs(value1 - value2)
print(f"Difference between {value1} and {value2} is {difference}")


# =============================================================================
# PART 5: USER-DEFINED FUNCTIONS
# =============================================================================

# Functions allow you to reuse code and make programs more organized
# Structure:
#   def function_name(argument1, argument2, ...):
#       """Docstring explaining what the function does"""
#       # Function body (indented)
#       return result

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy using E_k = 0.5 * m * v^2
    
    Parameters:
        mass: mass in kg
        velocity: velocity in m/s
    
    Returns:
        kinetic energy in Joules
    """
    energy = 0.5 * mass * velocity**2
    return energy


# Using the function
m = 2.0  # kg
v = 5.0  # m/s
E_k = calculate_kinetic_energy(m, v)
print(f"Kinetic energy: {E_k} J")


# Function with multiple return values
def calculate_momentum_and_energy(mass, velocity):
    """Calculate both momentum and kinetic energy"""
    momentum = mass * velocity
    energy = 0.5 * mass * velocity**2
    return momentum, energy


p, E = calculate_momentum_and_energy(m, v)
print(f"Momentum: {p} kg m/s, Energy: {E} J")


# Function with default parameter
def gravitational_pe(mass, height, g=9.81):
    """
    Calculate gravitational potential energy
    Default g = 9.81 m/s^2 (Earth's surface)
    """
    return mass * g * height


# Using default g
E_g_earth = gravitational_pe(10, 5)
print(f"PE on Earth: {E_g_earth} J")

# Using custom g (Moon)
E_g_moon = gravitational_pe(10, 5, g=1.62)
print(f"PE on Moon: {E_g_moon} J")


# =============================================================================
# PART 6: NUMPY PACKAGE AND LINSPACE
# =============================================================================

import numpy as np

# numpy provides powerful array operations and mathematical functions

# Creating arrays
array1 = np.array([1, 2, 3, 4, 5])
print(f"NumPy array: {array1}")

# linspace: Create evenly spaced values
# np.linspace(start, stop, num_points)
x_values = np.linspace(0, 10, 5)  # 5 values from 0 to 10
print(f"linspace(0, 10, 5): {x_values}")

# More points for smoother calculations
x_fine = np.linspace(0, 2*np.pi, 100)  # 100 points from 0 to 2π

# Array operations (applied element-wise)
y_values = np.sin(x_fine)

# Mathematical constants in numpy
print(f"Pi: {np.pi}")
print(f"e: {np.e}")

# Useful numpy functions
values = np.array([1, 4, 9, 16, 25])
print(f"Square roots: {np.sqrt(values)}")
print(f"Sum: {np.sum(values)}")
print(f"Mean: {np.mean(values)}")


# =============================================================================
# PART 7: PHYSICS APPLICATION - HYDROGEN ATOM TRANSITIONS
# =============================================================================

"""
Key equations from Topic 4 (Quantum Mechanics):
    E_n = -13.6 eV / n^2     (energy level of hydrogen)
    E_photon = h * f          (photon energy)
    c = f * λ                 (wave equation)
    
Constants:
    h = 6.63 × 10^-34 J s    (Planck's constant)
    c = 3.00 × 10^8 m/s      (speed of light)
    1 eV = 1.60 × 10^-19 J   (electronvolt)
"""

# Physical constants
h = 6.63e-34      # Planck's constant (J s)
c = 3.00e8        # Speed of light (m/s)
eV_to_J = 1.60e-19  # Conversion factor


def hydrogen_energy_level(n):
    """
    Calculate energy level of hydrogen atom
    
    Parameters:
        n: principal quantum number (positive integer)
    
    Returns:
        energy in Joules
    """
    energy_eV = -13.6 / n**2
    energy_J = energy_eV * eV_to_J
    return energy_J


def photon_wavelength(energy):
    """
    Calculate wavelength of photon with given energy
    
    Parameters:
        energy: photon energy in Joules
    
    Returns:
        wavelength in metres
    """
    frequency = abs(energy) / h
    wavelength = c / frequency
    return wavelength


def hydrogen_transition(n_initial, n_final):
    """
    Calculate properties of photon emitted/absorbed in hydrogen transition
    
    Parameters:
        n_initial: initial quantum number
        n_final: final quantum number
    
    Returns:
        Dictionary with energy, frequency, and wavelength
    """
    E_initial = hydrogen_energy_level(n_initial)
    E_final = hydrogen_energy_level(n_final)
    
    # Energy of photon (positive = emitted, negative = absorbed)
    delta_E = E_initial - E_final
    
    frequency = abs(delta_E) / h
    wavelength = c / frequency
    
    if delta_E > 0:
        transition_type = "emission"
    else:
        transition_type = "absorption"
    
    return {
        'energy_J': abs(delta_E),
        'energy_eV': abs(delta_E) / eV_to_J,
        'frequency_Hz': frequency,
        'wavelength_m': wavelength,
        'wavelength_nm': wavelength * 1e9,
        'type': transition_type
    }


# Example: Balmer series (transitions to n=2)
print("\n" + "="*60)
print("HYDROGEN BALMER SERIES (transitions to n=2)")
print("="*60)

for n in range(3, 7):
    result = hydrogen_transition(n, 2)
    print(f"\nn={n} → n=2:")
    print(f"  Energy: {result['energy_eV']:.2f} eV")
    print(f"  Wavelength: {result['wavelength_nm']:.1f} nm")
    print(f"  Type: {result['type']}")


# =============================================================================
# PART 8: HYDROGEN-LIKE IONS
# =============================================================================

def hydrogen_like_energy(n, Z):
    """
    Calculate energy level of hydrogen-like ion
    
    Parameters:
        n: principal quantum number
        Z: atomic number (number of protons)
    
    Returns:
        energy in Joules
    """
    energy_eV = -13.6 * Z**2 / n**2
    energy_J = energy_eV * eV_to_J
    return energy_J


# Example: He+ ion (Z=2)
print("\n" + "="*60)
print("He+ ION ENERGY LEVELS (Z=2)")
print("="*60)

for n in range(1, 5):
    E = hydrogen_like_energy(n, Z=2)
    E_eV = E / eV_to_J
    print(f"n={n}: E = {E_eV:.2f} eV")


# =============================================================================
# SUMMARY OF NEW PYTHON CONCEPTS
# =============================================================================

"""
KEY PYTHON CONCEPTS FROM THIS MODULE:

1. PRINT INSTRUCTIONS
   print("text", variable, "more text")
   print(f"formatted {variable:.2f}")

2. LIST OPERATIONS
   list.append(item)     # Add to end
   list[0]               # First element
   list[-1]              # Last element
   list[1:4]             # Slice from index 1 to 3

3. COMPOUND OPERATORS
   +=   (add and assign)
   -=   (subtract and assign)
   *=   (multiply and assign)
   /=   (divide and assign)
   **=  (power and assign)

4. abs() FUNCTION
   abs(-5) returns 5

5. USER-DEFINED FUNCTIONS
   def function_name(param1, param2=default):
       '''Docstring'''
       # body
       return result

6. NUMPY PACKAGE
   import numpy as np
   np.linspace(start, stop, num)
   np.array([1, 2, 3])
   np.pi, np.e
   np.sin(), np.cos(), np.sqrt()
"""

