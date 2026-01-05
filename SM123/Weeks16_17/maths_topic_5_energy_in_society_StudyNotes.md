# Topic 5: Mathematics Practice - Energy in Society

## Summary

This mathematics practice explores the connection between work and force using calculus from MST124 Units 6-8. Work is energy transfer due to force acting over distance.

## Key Equations

| Equation | Description |
|----------|-------------|
| W = Fs | Work done by constant force (1D) |
| W = ½kx² | Work done extending a spring |
| F = kx | Hooke's Law (force to extend spring) |
| W = F·s | Work as scalar product (vector form) |
| W = ∫F(s)ds | General work integral |

## Key Concepts

### Work and Force (Constant Force)

**W = Fs** (Equation M1)

- Gradient of W vs s graph = Force
- Force = rate of change of work with respect to displacement
- F = dW/ds

### Work and Force (Variable Force - Spring)

**W = ½kx²** (Equation M2)

Taking derivative: F = dW/dx = kx (Hooke's Law)

**Observations:**
- Force is NOT constant (varies with extension)
- F > 0 for extension (positive x)
- F < 0 for compression (negative x)
- F = 0 at equilibrium (x = 0)
- Minimum work at x = 0 (stationary point)

### Integration for Work

**W = ∫[a to b] F(s) ds** (Equation M3)

- Area under force-displacement graph
- Necessary when force varies with displacement

### Vector Form

**W = F·s = |F||s|cos θ** (Equation M4)

Where θ is angle between force and displacement:
- θ = 0 (same direction): W = Fs
- θ = π (opposite direction): W = -Fs
- θ = π/2 (perpendicular): W = 0
- θ = π/3: W = ½Fs

---

## Activities

### Activity 1

(a) Plot W vs s for a car (M = 1000 kg, g = 10 m s⁻², F = 10000 N).

(b) Calculate the gradient. Include units.

(c) What physical quantity does the gradient represent?

(d) Confirm the units are consistent.

(e) Interpret force in terms of work.

---

### Activity 2

(a) Write the relationship F = rate of change of work in Lagrange and Leibniz notation.

(b) Find the gradient of W = Fs by differentiation.

---

### Activity 3

(a) Find the force on a spring by differentiating W = ½kx². Is the force constant?

(b) Does this look familiar?

(c) Using k = 5 N m⁻¹, find force for:
   (i) extension of 1 m
   (ii) compression of 1 m
   (iii) extension of 0 m

(d) Plot W vs x for extensions and compressions up to 7 m.

(e) Where is the graph increasing/decreasing?

(f) What does this tell us about force direction?

(g) Find minimum of W using first and second derivative tests.

(h) Explain physically what happens at the stationary point.

---

### Activity 4

(a) Plot F vs s for constant force F = 10000 N.

(b) Write definite integral for work from s = 0 to s = 4 m.

(c) Find work by calculating area under graph.

(d) Perform the integral and confirm same answer.

---

### Activity 5

(a) Why can't we use W = Fs for Hooke's law?

(b) Plot F vs s for spring (k = 5 N m⁻¹).

(c) Write definite integral for work extending spring to x = 6 m.

(d) Find work from area under graph.

(e) Perform integration and confirm same answer.

(f) Integrate ∫ks ds from 0 to x and verify W = ½kx².

---

### Activity 6

(a) Is scalar product of two vectors a scalar or vector?

(b) Why is this significant for work?

(c) Rewrite W = F·s using |F||s|cos θ.

(d) What work is done if F and s are in same direction?

(e) What work is done if F and s are in opposite directions?

(f) Relevance to 1D treatment?

(g) What work is done if F and s are perpendicular?

(h) What work is done if θ = π/3?

---

## Solutions

### Solution to Activity 1

(a) Straight line through origin: W = 10000s

(b) Gradient = rise/run = 40000 J / 4 m = 10000 J m⁻¹

(c) Using W = ms + c form: m = F, c = 0. Gradient = Force

(d) 1 N = 1 J m⁻¹ ✓

(e) Force = rate of change of work with respect to displacement

### Solution to Activity 2

(a) F = W'(s) or F = dW/ds

(b) d/ds(Fs) = F (since F is constant)

### Solution to Activity 3

(a) W'(x) = d/dx(½kx²) = kx. Force varies with x (not constant).

(b) This is Hooke's Law!

(c) (i) F = 5 × 1 = 5 N
    (ii) F = 5 × (-1) = -5 N (negative = toward equilibrium)
    (iii) F = 5 × 0 = 0 N (no force at equilibrium)

(d) Parabola with minimum at x = 0

(e) Decreasing for x < 0, increasing for x > 0

(f) Force direction matches extension/compression direction

(g) W'(x) = kx = 0 when x = 0. W''(x) = k > 0, so minimum.

(h) At x = 0: equilibrium, no force. Moving away requires increasing force.

### Solution to Activity 4

(a) Horizontal line at F = 10000 N

(b) W = ∫₀⁴ 10000 ds

(c) Area = base × height = 4 m × 10000 N = 40000 J

(d) ∫₀⁴ 10000 ds = [10000s]₀⁴ = 40000 J ✓

### Solution to Activity 5

(a) F varies with displacement, so can't use constant F formula

(b) Straight line through origin: F = 5s

(c) W = ∫₀⁶ 5s ds

(d) Area of triangle = ½ × 6 m × 30 N = 90 J

(e) ∫₀⁶ 5s ds = [½ × 5 × s²]₀⁶ = 90 J ✓

(f) ∫₀ˣ ks ds = ½ks² |₀ˣ = ½kx² ✓

### Solution to Activity 6

(a) Scalar (hence "scalar product")

(b) Work is a scalar quantity, consistent with scalar product output

(c) W = |F||s|cos θ

(d) θ = 0, cos 0 = 1: W = Fs

(e) θ = π, cos π = -1: W = -Fs

(f) In 1D, vectors are either parallel (θ = 0) or antiparallel (θ = π)

(g) θ = π/2, cos(π/2) = 0: W = 0

(h) θ = π/3, cos(π/3) = ½: W = ½Fs

