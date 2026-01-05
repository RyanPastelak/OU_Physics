# Topic 6: Mathematics Practice - Nuclei and Particles

## Summary

This mathematics practice document applies concepts from MST124 Unit 3 (exponential functions) to nuclear decay processes. The random nature of radioactive decay can be modelled by an exponential function, connecting your understanding of exponential decay from mathematics to the physical process of nuclear transformation.

**Mathematical Concepts Applied:**
- Exponential functions and their properties
- Natural logarithms
- Converting between exponential forms
- Halving period and half-life connection
- Scaling of exponential functions

**Physics Applications:**
- Radioactive decay as exponential decay
- Half-life calculations
- Comparing decay rates of different isotopes

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| f(x) = bˣ | Exponential function (M1) | Base form with b > 0, b ≠ 1 |
| f(x) = eᵏˣ | Alternative form (M2) | Using natural base e |
| P(n) = (½)ⁿ × P₀ | Half-life form (M3) | Parent atoms after n half-lives |
| P(t) = P₀e⁻ᵏᵗ | Continuous decay (M4) | Where k = (1/tₕ)ln2 |
| P(t) = P₀(½)^(t/tₕ) | Time-based form (M5/S1) | Equivalent to M4 |

## Key Concepts

### Exponential Function Properties
- For decay: f(t) = ae^(κt) with a > 0 and κ < 0
- Graph lies entirely above t-axis (positive values only)
- t-axis is an asymptote (approaches but never reaches zero)
- Rate of decrease slows as time increases

### Converting Between Forms
- If b = eᵏ, then bˣ = eᵏˣ
- For (½)ˣ: k = ln(½) = −ln2 ≈ −0.693
- So (½)ˣ = e^(−0.693x)

### Half-life and Decay Constant
- k = (1/tₕ) × ln2
- Halving period p = −ln(2)/κ = tₕ (the half-life)
- Shorter half-life → larger k → steeper decay curve

### Scaling Effects
- **Horizontal scaling**: Different half-lives stretch/compress the time axis
- **Vertical scaling**: Different initial quantities P₀ stretch/compress vertically
- Graph of y = f(x/c) is horizontal scaling by factor c
- Graph of y = cf(x) is vertical scaling by factor c

## Problems and Activities

### Activity 1 Exponential Function Basics

Consider the function f(x) = (½)ˣ.
(a) Find f(−1), f(0), f(1), f(2), f(3), and f(4).
(b) Sketch a graph of f(x) = (½)ˣ.
(c) Write f(x) = (½)ˣ in the form f(x) = eᵏˣ. Find k.
(d) Express your answer in the alternative exponential form.

**Solution to Activity 1**

(a) f(−1) = 2, f(0) = 1, f(1) = 0.5, f(2) = 0.25, f(3) = 0.125, f(4) = 0.0625

(b) Sketch: Decreasing exponential curve starting at (−1, 2), passing through (0, 1), approaching but never touching the x-axis.

(c) If (½) = eᵏ, then:
    ln(½) = k
    k = ln(2⁻¹) = −ln2 ≈ −0.693

(d) f(x) = e^(−0.693x)

---

### Activity 2 Comparing Exponential Models

Look at graphs of radioactive decay (Topic 6 Figures 2.3, Activity 2.1, Activity 2.2). Compare their shape to exponential decay curves from MST124 Unit 3.

**Solution to Activity 2**

The graphs from Topic 6 match the characteristic shape of exponential decay:
- Lie entirely above the t-axis (can't have negative atoms)
- t-axis is an asymptote (approaches but never reaches zero)
- Decreasing function that gets less steep as t increases
- Confirms exponential model with k < 0 is appropriate
- y-intercept equals P₀ (initial number of atoms)

---

### Activity 3 Using the Exponential Model

(a) Do the signs of P₀ and k in P(t) = P₀e^(−kt) confirm exponential decay?
(b) The half-life of Beryllium-11 is 13.8 s. How much of 1.00 g remains after 82.8 s?
(c) After 40.0 days, 20.0 mg of 640 mg iodine-131 remain. Find the half-life.
(d) Find the halving period of P(t) = P₀e^(−kt).

**Solution to Activity 3**

(a) Yes. For exponential decay f(t) = ae^(κt), we need a > 0 and κ < 0.
    Here a = P₀ > 0 (initial atoms must be positive)
    And the exponent is −kt where k = (ln2)/tₕ > 0, so κ = −k < 0 ✓

(b) k = (1/13.8s) × ln2 ≈ 0.0502 s⁻¹
    P(82.8) = 1.00g × e^(−0.0502 × 82.8) = 1.00g × e^(−4.16) ≈ 0.0156g = 15.6 mg

(c) 20.0 = 640 × e^(−k × 40)
    e^(−40k) = 1/32
    −40k = ln(1/32) = −ln32
    k = ln32/40 = 0.0866 day⁻¹
    tₕ = ln2/k = 0.693/0.0866 = 8.0 days

(d) Halving period p = −ln(2)/κ = −ln(2)/(−k) = ln(2)/k = ln(2)/[(1/tₕ)ln2] = tₕ
    The halving period equals the half-life, as expected!

---

### Activity 4 Converting Between Time Forms

(a) If half-life is 20 s, how many seconds after 2 half-lives?
(b) If half-life is 120 s, how many seconds after 3.5 half-lives?
(c) If half-life is tₕ seconds, how many seconds after n half-lives?
(d) Express n in terms of t and tₕ.
(e) Write Equation M3 in terms of t instead of n.
(f) Identify a and b so that P(t) = abᵗ.

**Solution to Activity 4**

(a) t = 2 × 20s = 40s

(b) t = 3.5 × 120s = 420s

(c) t = n × tₕ seconds

(d) n = t/tₕ

(e) Substituting n = t/tₕ into P(n) = (½)ⁿ × P₀:
    P(t) = P₀ × (½)^(t/tₕ)

(f) P(t) = P₀ × [(½)^(1/tₕ)]ᵗ
    So a = P₀ and b = (½)^(1/tₕ)

---

### Activity 5 Comparing Different Isotopes

(a) How many seconds is 8 days?
(b) Find k for Beryllium-11 (tₕ = 13.8s) and Iodine-131 (tₕ ≈ 8 days).
(c) How do their decay curves differ?
(d) How do different k values affect curve shapes?
(e) How would starting with 1g vs 3g affect the curve?
(f) How does this relate to vertical scaling?

**Solution to Activity 5**

(a) 8 days × 24 × 60 × 60 = 691,200 s ≈ 6.9 × 10⁵ s

(b) k_B = ln2/13.8 ≈ 0.0502 s⁻¹
    k_I = ln2/(6.9 × 10⁵) ≈ 1.0 × 10⁻⁶ s⁻¹

(c) Beryllium-11 decays much faster (shorter half-life), so fewer parent atoms remain at any given time. Iodine-131 curve is much flatter/stretched out.

(d) Larger |k| → steeper decay curve
    Smaller |k| → flatter decay curve
    The graph is horizontally scaled by factor −1/k

(e) Starting with 3g gives 3× as many atoms remaining at any time. The curve is vertically stretched by factor 3.

(f) Graph of y = P₀f(x) is vertical scaling by factor P₀.
    Larger P₀ stretches the graph vertically.

---

### Activity 6 Final Conversion

Write P(t) = P₀(½)^(t/tₕ) in the form P(t) = P₀e^(−kt).

**Solution to Activity 6**

Let b = (½)^(1/tₕ), so bᵗ = [(½)^(1/tₕ)]ᵗ

We need b = e^(−k):
ln(b) = −k
ln[(½)^(1/tₕ)] = −k
(1/tₕ)ln(½) = −k
−(1/tₕ)ln2 = −k
k = (1/tₕ)ln2

Therefore:
P(t) = P₀ × e^[−(ln2/tₕ)t] = P₀e^(−kt)

This confirms Equations M3 and M4 describe the same relationship!

