# Topic 7: Mathematics Practice - Orbits and Series

## Summary

This practice focuses on **geometric sequences** applied to planetary orbits. It explores the **Titius-Bode Law**, an empirical rule that predicts the spacing of planets, and **Dermott's Law**, a more general form applied to satellites and exoplanets. It reinforces skills in working with powers, logarithms, and linearizing exponential relationships.

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| $x_n = b r^{n-1}$ | Geometric Sequence | $n$-th term with first term $b$ and common ratio $r$. |
| $a_n = 0.4 + (0.3 \times 2^n)$ | Titius-Bode Law | Predicts semi-major axis (AU) for $n = -\infty, 0, 1, 2...$ |
| $T_n = T_0 A^n$ | Dermott's Law | Predicts orbital period $T_n$ for $n$-th satellite. |
| $\log T_n = \log T_0 + n \log A$ | Linear Form | Logarithmic form of Dermott's Law ($y = mx + c$). |

## Key Concepts

-   **Geometric Sequence:** A sequence where each term is multiplied by a constant factor ($r$) to get the next.
-   **Titius-Bode Law:**
    -   Successfully predicted Uranus and Ceres.
    -   Failed for Neptune (predicted 38.8 AU, actual 30.1 AU).
    -   Likely due to orbital resonances rather than a fundamental force.
-   **Dermott's Law:**
    -   Generalizes the spacing rule to $T_n = T_0 A^n$.
    -   Works well for Jupiter's moons ($A \approx 2$) and Saturn's/Uranus's moons.
    -   Also fits many exoplanetary systems.
-   **Linearizing Data:**
    -   If $T = T_0 A^n$, plotting $T$ vs $n$ is a curve.
    -   Taking logs: $\log T = (\log A) n + \log T_0$.
    -   Plotting $\log T$ vs $n$ gives a **straight line** with gradient $\log A$ and intercept $\log T_0$.

## Problems and Solutions

### Activity 2: Titius-Bode Predictions
**Problem:** Calculate the first few Titius-Bode predictions ($n = -\infty, 0, 1, 2$) and compare to planets.
**Solution:**
-   $n=-\infty$: $a = 0.4 + 0 = 0.4$ AU (Mercury 0.39) - Good fit.
-   $n=0$: $a = 0.4 + 0.3(1) = 0.7$ AU (Venus 0.72) - Good fit.
-   $n=1$: $a = 0.4 + 0.3(2) = 1.0$ AU (Earth 1.00) - Exact fit.
-   $n=2$: $a = 0.4 + 0.3(4) = 1.6$ AU (Mars 1.52) - Reasonable fit.
-   $n=3$: $a = 0.4 + 0.3(8) = 2.8$ AU (Ceres/Asteroid Belt) - **Prediction verified**.

### Activity 5: Testing Dermott's Law
**Problem:** How do you determine $A$ and $T_0$ from data?
**Method:**
1.  Assign integers $n=1, 2, 3...$ to the satellites/planets in order.
2.  Plot $\log(\text{Period})$ on y-axis vs $n$ on x-axis.
3.  Draw best fit line.
4.  Gradient = $\log A$. Intercept = $\log T_0$.

### Activity 8: Jupiter's Moons
**Problem:** For Io ($P=1.77$d), Europa ($P=3.55$d), Ganymede ($P=7.15$d), show they follow Dermott's Law with $A \approx 2$.
**Solution:**
-   Ratio Europa/Io = $3.55/1.77 \approx 2.0$.
-   Ratio Ganymede/Europa = $7.15/3.55 \approx 2.0$.
-   Since ratio is constant (~2), they follow a geometric progression (Dermott's Law).
-   This "2:1 resonance" is a famous feature of the Galilean moons.
