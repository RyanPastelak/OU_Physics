import numpy as np
import matplotlib.pyplot as plt

def fit_hubble_law(distances, velocities):
    """
    Perform a linear fit to distance vs velocity data to find the Hubble Constant.
    
    Parameters:
    distances (array): Distances in Mpc
    velocities (array): Recession velocities in km/s
    
    Returns:
    float: Hubble Constant (gradient)
    float: Intercept
    """
    # Fit a polynomial of degree 1 (straight line: y = mx + c)
    # coeffs will be [gradient, intercept]
    coeffs = np.polyfit(distances, velocities, 1)
    return coeffs

def calculate_rmsd(y_observed, y_predicted):
    """
    Calculate Root Mean Square Deviation.
    """
    residuals = y_observed - y_predicted
    rmsd = np.sqrt(np.mean(residuals**2))
    return rmsd

def main():
    # Sample Data (approximate values for illustration)
    # Galaxy Distances (Mpc)
    d = np.array([10, 20, 50, 80, 100])
    # Recession Velocities (km/s)
    v = np.array([700, 1500, 3400, 5700, 7100])
    
    # Perform Fit
    coeffs = fit_hubble_law(d, v)
    H0 = coeffs[0]
    c = coeffs[1]
    
    print(f"Best fit line: v = {H0:.2f} * d + {c:.2f}")
    print(f"Calculated Hubble Constant (H0): {H0:.2f} km/s/Mpc")
    
    # Generate predicted values for plotting the line
    v_pred = np.polyval(coeffs, d)
    
    # Calculate Quality of Fit
    rmsd = calculate_rmsd(v, v_pred)
    print(f"RMSD of fit: {rmsd:.2f} km/s")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(d, v, 'bo', label='Observed Data') # 'bo' = blue circles
    plt.plot(d, v_pred, 'r-', label=f'Best Fit (H0={H0:.1f})') # 'r-' = red line
    
    plt.xlabel('Distance (Mpc)')
    plt.ylabel('Recession Velocity (km/s)')
    plt.title('Hubble\'s Law: Velocity vs Distance')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    plt.savefig('hubble_law_plot.png')
    print("Plot saved as hubble_law_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
