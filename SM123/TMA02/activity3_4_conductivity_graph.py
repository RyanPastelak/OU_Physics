"""
Activity 3.4: Electrical Conductivity of Ionic Compounds
SM123 Physics and Space - TMA02 Question 4

This program plots conductivity vs concentration for sodium chloride (NaCl)
and magnesium chloride (MgCl2), with best-fit straight lines.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from Table 3.2
concentration = np.array([0.086, 0.172, 0.346, 0.885])  # mol l^-1
conductivity_NaCl = np.array([8.2, 16.0, 30.2, 70.1])   # mS cm^-1
conductivity_MgCl2 = np.array([13.7, 25.2, 46.4, 94.5]) # mS cm^-1

# Calculate best-fit lines using numpy polyfit (degree 1 = linear)
# Returns [slope, intercept]
coeffs_NaCl = np.polyfit(concentration, conductivity_NaCl, 1)
coeffs_MgCl2 = np.polyfit(concentration, conductivity_MgCl2, 1)

# Create x values for plotting the best-fit lines (extended slightly beyond data)
x_fit = np.linspace(0, 1.0, 100)

# Calculate y values for best-fit lines
y_fit_NaCl = coeffs_NaCl[0] * x_fit + coeffs_NaCl[1]
y_fit_MgCl2 = coeffs_MgCl2[0] * x_fit + coeffs_MgCl2[1]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot data points
ax.scatter(concentration, conductivity_NaCl, marker='o', s=80, color='blue', 
           label='Sodium chloride (NaCl)', zorder=5)
ax.scatter(concentration, conductivity_MgCl2, marker='^', s=80, color='red', 
           label='Magnesium chloride (MgCl₂)', zorder=5)

# Plot best-fit lines
ax.plot(x_fit, y_fit_NaCl, 'b--', linewidth=1.5, alpha=0.7,
        label=f'NaCl best fit (y = {coeffs_NaCl[0]:.1f}x + {coeffs_NaCl[1]:.1f})')
ax.plot(x_fit, y_fit_MgCl2, 'r--', linewidth=1.5, alpha=0.7,
        label=f'MgCl₂ best fit (y = {coeffs_MgCl2[0]:.1f}x + {coeffs_MgCl2[1]:.1f})')

# Add vertical line at target concentration (0.465 mol/l)
target_conc = 0.465
y_NaCl_at_target = coeffs_NaCl[0] * target_conc + coeffs_NaCl[1]
y_MgCl2_at_target = coeffs_MgCl2[0] * target_conc + coeffs_MgCl2[1]

ax.axvline(x=target_conc, color='green', linestyle=':', alpha=0.5, linewidth=1.5)
ax.plot(target_conc, y_NaCl_at_target, 'bs', markersize=10, markerfacecolor='none', 
        markeredgewidth=2, label=f'NaCl at 0.465: {y_NaCl_at_target:.0f} mS cm⁻¹')
ax.plot(target_conc, y_MgCl2_at_target, 'r^', markersize=10, markerfacecolor='none',
        markeredgewidth=2, label=f'MgCl₂ at 0.465: {y_MgCl2_at_target:.0f} mS cm⁻¹')

# Labels and title
ax.set_xlabel('Concentration / mol l⁻¹', fontsize=12)
ax.set_ylabel('Conductivity / mS cm⁻¹', fontsize=12)
ax.set_title('Electrical Conductivity of Sodium Chloride and Magnesium Chloride Solutions', 
             fontsize=14, fontweight='bold')

# Set axis limits
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 110)

# Add grid
ax.grid(True, linestyle='-', alpha=0.3)

# Add legend
ax.legend(loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('SM123/TMA02/conductivity_graph.png', dpi=150, bbox_inches='tight')
print("Graph saved as 'SM123/TMA02/conductivity_graph.png'")

# Display best-fit line equations
print("\n--- Best-fit Line Equations ---")
print(f"NaCl:   Conductivity = {coeffs_NaCl[0]:.2f} x Concentration + {coeffs_NaCl[1]:.2f}")
print(f"MgCl2:  Conductivity = {coeffs_MgCl2[0]:.2f} x Concentration + {coeffs_MgCl2[1]:.2f}")

print("\n--- Conductivity at 0.465 mol/l ---")
print(f"NaCl:   {y_NaCl_at_target:.1f} mS/cm")
print(f"MgCl2:  {y_MgCl2_at_target:.1f} mS/cm")

# Show the plot
plt.show()

