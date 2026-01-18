# Python 3: Arrays and Plotting

## Summary

This week introduces advanced Python concepts for scientific computing: **arrays** (using `numpy`) and **plotting** (using `matplotlib.pyplot`). These tools allow for efficient manipulation of large datasets and visualization of results. The week culminates in writing a program to calculate radioactive decay and sharing it for **peer review**, emphasizing the importance of clear comments, testing, and constructive feedback in software development.

## Key Concepts

-   **Arrays (Numpy):**
    -   Lists of numbers that can be manipulated mathematically as a single object.
    -   More efficient than standard Python lists for large datasets.
    -   **One-dimensional arrays:** Like a single row of data (vector).
    -   **Two-dimensional arrays:** Like a table or matrix (rows and columns).
    -   Operations (e.g., `sum`, `len`) work on the whole array or specific elements.

-   **Plotting (Matplotlib):**
    -   Using the `pyplot` module to create graphs.
    -   Essential for visualizing data (e.g., Kepler's Third Law, radioactive decay curves).
    -   Commands to label axes, add titles, and change line styles/markers.

-   **Software Development Best Practices:**
    -   **Algorithm Design:** Planning the logic before writing code.
    -   **Incremental Testing:** Writing and testing small chunks of code at a time.
    -   **Comments:** Crucial for making code understandable to others (and your future self).
    -   **Peer Review:** Providing constructive, supportive feedback to improve code quality.

## Activities

### Python Activity 3.1: Radioactive Decay
**Task:** Write a program to calculate the amount of radioactive isotope remaining after a given time.
**Physics:** Based on the exponential decay law (from Topic 6).
**Requirements:**
-   Design the algorithm first.
-   Implement in Python.
-   Include clear comments.
-   Test with known values (e.g., half-life definitions).

### Python Activity 3.2: Peer Review
**Task:** Share your program and review another student's work.
**Review Criteria:**
1.  **Correctness:** Does it produce the right answers?
2.  **Usability:** Are prompts and instructions clear?
3.  **Readability:** Are comments sufficient?
4.  **Learning:** What did they do better/differently than you?

## Key Commands (Reference)

| Command/Function | Description |
|------------------|-------------|
| `import numpy as np` | Import the numerical python library. |
| `import matplotlib.pyplot as plt` | Import the plotting library. |
| `np.array([1, 2, 3])` | Create a numpy array from a list. |
| `np.zeros(5)` | Create an array of 5 zeros. |
| `np.shape(arr)` | Get dimensions of array `arr`. |
| `plt.plot(x, y)` | Plot `y` versus `x`. |
| `plt.xlabel("Label")` | Label the x-axis. |
| `plt.ylabel("Label")` | Label the y-axis. |
| `plt.title("Title")` | Add a title to the plot. |
| `plt.show()` | Display the plot. |
