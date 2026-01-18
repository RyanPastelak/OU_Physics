import numpy as np
import matplotlib.pyplot as plt

def calculate_decay(N0, half_life, time_points):
    """
    Calculate the number of remaining nuclei at given time points.
    
    Parameters:
    N0 (float): Initial number of nuclei
    half_life (float): Half-life of the isotope
    time_points (array): Array of time values
    
    Returns:
    array: Number of remaining nuclei at each time point
    """
    decay_constant = np.log(2) / half_life
    N_t = N0 * np.exp(-decay_constant * time_points)
    return N_t

def main():
    # Parameters for Carbon-14 (example)
    isotope_name = "Carbon-14"
    half_life = 5730 # years
    N0 = 1000 # Initial percentage or amount (e.g., 100%)
    
    # Create time array (from 0 to 5 half-lives)
    t_max = 5 * half_life
    t = np.linspace(0, t_max, 100)
    
    # Calculate decay
    N = calculate_decay(N0, half_life, t)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(t, N, 'b-', label=f'{isotope_name} Decay')
    
    # Mark half-life points
    for i in range(1, 4):
        hl_time = i * half_life
        hl_amount = calculate_decay(N0, half_life, np.array([hl_time]))[0]
        plt.plot(hl_time, hl_amount, 'ro')
        plt.text(hl_time, hl_amount, f' {i} HL', verticalalignment='bottom')

    plt.xlabel('Time (years)')
    plt.ylabel('Amount Remaining')
    plt.title(f'Radioactive Decay of {isotope_name}')
    plt.grid(True)
    plt.legend()
    
    # Save the plot
    plt.savefig('radioactive_decay_plot.png')
    print("Plot saved as radioactive_decay_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
