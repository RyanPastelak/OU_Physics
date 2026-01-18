import numpy as np
import pandas as pd
import csv

# --- TMA03 Q4 Calculations ---
sigma = 5.67e-8
epsilon = 0.78
A = 2.6
T_hot_C = 65
T_cold_C = 19
T_hot_K = T_hot_C + 273.15
T_cold_K = T_cold_C + 273.15

# a) Net power radiated
P_rad = epsilon * sigma * A * (T_hot_K**4 - T_cold_K**4)

# b) Power lost through insulation
l = 0.095 # meters
k = 0.034
delta_T = T_hot_C - T_cold_C
P_cond = k * A * delta_T / l

# c) CO2 savings
P_saved_kW = (P_rad - P_cond) / 1000
hours_per_year = 365 * 24
energy_saved_kWh = P_saved_kW * hours_per_year
co2_factor = 0.35
co2_saved = energy_saved_kWh * co2_factor

print("--- TMA03 Q4 ---")
print(f"P_rad: {P_rad:.2f} W")
print(f"P_cond: {P_cond:.2f} W")
print(f"CO2 saved: {co2_saved:.0f} kg")

# --- TMA04 Q2 Analysis ---
# Rydberg Constant fit: E = R(1/nf^2) - R(1/ni^2)
# y = E, x = 1/ni^2
# Gradient m = -R
# Intercept c = R/nf^2

def analyze_spectrum(filename):
    ni = []
    E = []
    
    # Try reading with different encodings/separators if needed, but standard csv expected
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Column names might vary, checking typical ones or first/second columns
                # Based on previous notebook code, likely 'n_i' and 'Energy / J' or similar
                # Let's inspect keys if needed, but assuming standard format from Python 4 folder
                keys = list(row.keys())
                # Assuming first column is ni, second is Energy
                ni.append(float(row[keys[0]]))
                E.append(float(row[keys[1]]))
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return

    ni = np.array(ni)
    E = np.array(E)
    x = 1.0 / (ni**2)
    
    m, c = np.polyfit(x, E, 1)
    
    R = -m
    nf = np.sqrt(R / c)
    
    # RMSD
    E_model = m * x + c
    rmsd = np.sqrt(np.mean((E - E_model)**2))
    
    print(f"\nAnalysis for {filename}:")
    print(f"Gradient (m): {m:.4e}")
    print(f"Intercept (c): {c:.4e}")
    print(f"Rydberg Constant (R): {R:.4e} J")
    print(f"Final State (nf): {nf:.2f}")
    print(f"RMSD: {rmsd:.4e} J")

print("\n--- TMA04 Q2 ---")
analyze_spectrum('python/4/Lseries.csv')
analyze_spectrum('python/4/Student-measurements.csv')
