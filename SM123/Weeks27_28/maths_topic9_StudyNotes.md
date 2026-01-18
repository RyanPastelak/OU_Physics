# Topic 9: Mathematics Practice - The Scale Factor

## Summary

This practice module introduces the mathematical framework for cosmic expansion. It uses the **Scale Factor**, $R(t)$, to describe how distances in the Universe change over time. It relates $R(t)$ to the observable **Hubble Parameter** ($H$) and **Deceleration Parameter** ($q$), and uses **Taylor Polynomials** (from MST124) to approximate the relationship between **Redshift** ($z$) and **Look-back Time**.

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| $D(t) / D(t_0) = R(t) / R(t_0)$ | Scale Factor Definition | Relates distance $D$ at time $t$ to present distance $D_0$. |
| $v(t) = H(t) D(t)$ | Hubble's Law (General) | Recession speed $v$ related to distance $D$ and parameter $H$. |
| $H(t) = \dot{R}(t) / R(t)$ | Hubble Parameter | Rate of change of scale factor divided by scale factor. |
| $z = R(t_0) / R(t) - 1$ | Redshift Definition | Relates redshift to the scale factor. |
| $z \approx H_0 (t_0 - t)$ | Linear Approximation | Redshift is roughly proportional to look-back time ($t_0 - t$). |

## Key Concepts

-   **Scale Factor $R(t)$:**
    -   A function of time that tracks the "size" of the Universe relative to today.
    -   $R(t_0)$ (today) is usually set to 1.
    -   If $R(t)$ doubles, all distances between galaxies double.

-   **Hubble Parameter $H(t)$:**
    -   It is not constant in time! It changes as the expansion speeds up or slows down.
    -   Defined as the fractional rate of expansion: $H = \dot{R}/R$.

-   **Deceleration Parameter $q(t)$:**
    -   Measures how the expansion rate is changing.
    -   $q > 0$: Decelerating (gravity wins).
    -   $q < 0$: Accelerating (dark energy wins).
    -   Current value $q_0 \approx -0.55$ (Accelerating).

-   **Taylor Polynomials:**
    -   Used to approximate $R(t)$ for times close to today ($t \approx t_0$).
    -   **Linear approx:** $R(t) \approx R_0 [1 + H_0(t - t_0)]$.
    -   **Quadratic approx:** Adds a term with $q_0$. Essential for accurate redshift calculations at large distances.

## Problems and Solutions

### Activity 2: Deriving Hubble's Law
**Problem:** Show that $v = \dot{R}/R \times D$.
**Derivation:**
$D(t) = [R(t)/R_0] D_0$.
Differentiate wrt time: $v = \dot{D} = [\dot{R}/R_0] D_0$.
Substitute $D_0 = [R_0/R] D$:
$v = [\dot{R}/R_0] [R_0/R] D = (\dot{R}/R) D$.
This confirms $H = \dot{R}/R$.

### Activity 5: Redshift and Scale Factor
**Problem:** What is the scale factor when redshift $z = 1$?
**Solution:**
$z = R_0/R(t) - 1$.
$1 = R_0/R(t) - 1 \implies 2 = R_0/R(t)$.
$R(t) = R_0 / 2$.
So, at $z=1$, the Universe was **half** its current size.

### Activity 7: Linear Redshift
**Problem:** Use the linear approximation for $z$ at $t = 12$ billion years ($t_0 = 14$ billion years).
**Solution:**
$z \approx H_0 (t_0 - t)$.
Assume $H_0 \approx 1/t_0 = 1/14 \text{ Gyr}^{-1}$.
$z \approx (1/14) \times (14 - 12) = 2/14 \approx 0.14$.
(Exact formula gives $z = 0.167$, so the approximation is decent for small look-back times).
