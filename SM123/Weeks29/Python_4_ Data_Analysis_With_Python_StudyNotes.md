# Python 4: Data Analysis with Python

## Summary

This final Python week focuses on techniques for analysing scientific data. It covers how to **import data** from files, customize **plots**, and most importantly, how to **fit functions** to data (linear regression) to extract physical parameters (like gradients and intercepts). It also introduces the **Root Mean Square Deviation (RMSD)** as a metric to assess the quality of a fit.

## Key Concepts

-   **Data Input/Output:**
    -   **Reading Data:** Using commands (like `np.loadtxt` or specific functions provided in the notebooks) to read numbers from text/CSV files into arrays.
    -   **Saving Plots:** Using `plt.savefig('filename.png')` to save graphs as image files.

-   **Plot Customization:**
    -   **Labels:** `plt.xlabel()`, `plt.ylabel()` to define what is being plotted.
    -   **Styles:** Changing marker shapes (`'o'`, `'x'`, `'+'`) and colors to make data distinct.

-   **Curve Fitting (Linear Regression):**
    -   **Goal:** To find the best straight line ($y = mx + c$) that describes a set of data points.
    -   **Physics:** The gradient ($m$) and intercept ($c$) often have physical meaning (e.g., Spring constant, Hubble constant).
    -   **Function:** `np.polyfit(x, y, 1)` fits a polynomial of degree 1 (a line) to data arrays `x` and `y`. It returns the coefficients $[m, c]$.

-   **Goodness of Fit:**
    -   **RMSD (Root Mean Square Deviation):** A measure of the average difference between the data points and the fitted line.
    -   Lower RMSD = Better fit.
    -   Used to distinguish between different models (e.g., is the trend linear or quadratic?).

## Activities

### Activity: Fitting Hubble's Law
**Task:** Write a program to determine the Hubble Constant ($H_0$).
**Method:**
1.  Read in galaxy distance ($d$) and velocity ($v$) data.
2.  Plot $v$ vs $d$.
3.  Use `np.polyfit` to find the gradient of the best-fit line.
4.  The gradient represents $H_0$.

### Activity: Assessing Fit Quality
**Task:** Calculate RMSD for a fit.
**Method:**
1.  Calculate predicted $y$ values using the fit line ($y_{pred} = mx + c$).
2.  Calculate residuals ($y_{data} - y_{pred}$).
3.  Square them, mean them, take square root.

## Key Commands (Reference)

| Command/Function | Description |
|------------------|-------------|
| `np.loadtxt('file.txt')` | Load data from a text file into an array. |
| `plt.savefig('plot.png')` | Save the current plot to a file. |
| `np.polyfit(x, y, 1)` | Fit a straight line to x, y data. Returns `[gradient, intercept]`. |
| `np.polyval(coeffs, x)` | Calculate y-values for a polynomial with given `coeffs` at points `x`. |
| `plt.legend()` | Show the legend on the plot. |
