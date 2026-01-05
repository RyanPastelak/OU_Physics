# Topic 2: Mathematics Practice - Energy

## Summary

This mathematics practice applies concepts from MST124 Unit 3 (functions) to energy physics. Energy equations are mathematical functions - one quantity depends on another. For a known mass, kinetic energy is a function of speed, and gravitational potential energy is a function of height.

**Mathematical Concepts Applied:**
- Functions and their notation
- Domain, codomain, and image set
- Inverse functions
- The reciprocal function
- Vertical scaling and translation

**Physics Applications:**
- Kinetic energy as a function of speed
- Gravitational potential energy as a function of height
- Planetary gravitational potential energy

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| E_k = ½mv² | Kinetic Energy (M1) | Function of speed for given mass |
| E_g = mgh | Gravitational PE (M2) | Function of height for given mass |
| E_g = -GMm/r | Gravitational PE (M3) | General form for two masses |

**Function Notation:**
- f_k(v) = ½mv² (kinetic energy function)
- f_g(h) = mgh (gravitational PE function)

---

## Activities

### Activity 1

(a) Write Equations M1 and M2 in function notation, assuming in both cases that the mass, m, is a given constant. Call the kinetic energy f_k and the potential energy f_g.

(b) Specify a domain for each function, and restrict each domain to one that makes physical sense in these cases.

(c) Given the restricted domains from part (b), what are the codomain and image set for each function? Are these physically meaningful?

(d) Sketch a graph of each function over the restricted domains. Comment on the physical meaning of any important points.

(e) Looking at your plots from part (d), comment on whether the rule of each function converts each input value to exactly one output value. What is the physical significance of this?

(f) Specify intervals of the restricted domains over which f_k and f_g are increasing and/or decreasing. What does this mean physically? Consider also f_g on the unrestricted domain ℝ.

(g) Consider the variable h, which we set to be 0 at sea level. Define a new function f_g,hill(h) which gives the gravitational potential energy of a skier relative to the top of a 2500m hill as f_g,hill(h) = mgh − mg(2500m). Using your knowledge of translation of graphs, sketch a graph of f_g(h) and f_g,hill(h) on the same axes.

(h) Rather than define a new function, define a new variable h₁ which is 0 at the top of the hill. Then f_g(h₁) = mgh₁ where h₁ = h − 2500m. Sketch a graph of f_g(h₁) on the h-axis as a function of h. Comment on any similarities to your answer to part (g).

---

### Activity 2

(a) A function must be invertible in order to have an inverse. What condition must a function satisfy in order to be invertible? State whether the functions for kinetic and gravitational potential energy are invertible on the restricted domains from Activity 1 (b), and comment on the physical meaning of this.

(b) How would your answer to part (a) differ if we had not restricted the domain in Activity 1 (b)? What, if anything, would you need to do in order to find the inverse functions?

(c) Find the inverse functions f_k⁻¹(y_k) and f_g⁻¹(y_g), where y_k is the kinetic energy and y_g is the gravitational potential energy of a given mass.

(d) What are the domain, codomain and image set of f_k⁻¹(y_k) and f_g⁻¹(y_g), and do they all make physical sense?

(e) The kinetic energy of a molecule in an ideal gas is equal to (3/2)k_B T, where k_B = 1.38×10⁻²³ J K⁻¹ is the Boltzmann constant, and T is the temperature in Kelvin. At room temperature (20°C = 293K), an average air molecule has kinetic energy (3/2)k_B T = 6.07×10⁻²¹ J.

Use your inverse kinetic energy function from part (c) to find the average speed of:
- A Nitrogen molecule with mass 4.68×10⁻²⁶ kg
- An Oxygen molecule with mass 5.34×10⁻²⁶ kg

Comment on the difference in speed between the different molecules.

(f) Comment on what the shape of the inverse kinetic energy function tells us physically about the relationship between average kinetic energy (temperature) and speed.

---

### Activity 3

(a) Write the reciprocal function in terms of the variable r. Sketch a graph of the reciprocal function.

(b) Obtain a function (in terms of r) describing the gravitational potential energy of Equation M3, by applying an appropriate vertical scaling to the reciprocal function. What is your value of c?

(c) What is the domain of the reciprocal function, and has it been affected by the vertical scaling?

(d) Comment on the physical meaning of r = 0, and whether this mathematical restriction limits applicability to gravitational potential energy.

(e) Consider the rest of the domain of the reciprocal function and restrict it to a physically meaningful one if necessary.

(f) Recall the value of c (vertical scaling) from part (b). How does the sign of c alter the reciprocal function? Comment on any change in whether the function is increasing or decreasing. How does this reflect the physical situation?

(g) What are the asymptotes of your vertically scaled reciprocal function, and what do they mean physically?

---

## Solutions

### Solution to Activity 1

(a) The two functions are:
- f_k(v) = ½mv²
- f_g(h) = mgh

(b) **Domain restrictions:**
- f_k: [0, c] where c = 3×10⁸ m s⁻¹ (speed of light) - speed cannot be negative or exceed c
- f_g: [0, ∞) for height above ground level (though h can be negative if reference point is above object)

(c) **Codomain**: ℝ for both functions
- Image set of f_k: [0, ½mc²]
- Image set of f_g: [0, ∞)

(d) f_k is a parabola (right half) with vertex at origin; f_g is a line through origin with positive slope

(e) Each input maps to exactly one output (definition of function). Physically: a specific speed gives unique kinetic energy.

(f) Both f_k and f_g are increasing over their restricted domains. As speed increases, kinetic energy increases. As height increases, gravitational PE increases.

(g-h) Vertical translation or horizontal translation can both be used to shift the reference point (0 of the axis) to a different location.

### Solution to Activity 2

(a) A function must be **one-to-one** to be invertible. Both functions are one-to-one on restricted domains.

(b) f_g is one-to-one on ℝ, but f_k is not (both v and -v give same E_k). Would need to restrict domain.

(c) **Inverse functions:**
- v = √(2y_k/m) - speed from kinetic energy
- h = y_g/(mg) - height from gravitational PE

(d) Domains, codomains, and image sets match the image sets and domains of original functions respectively.

(e) **Molecular speeds at room temperature:**
- Nitrogen: v = √(2×6.07×10⁻²¹/4.68×10⁻²⁶) = **509 m s⁻¹**
- Oxygen: v = √(2×6.07×10⁻²¹/5.34×10⁻²⁶) = **477 m s⁻¹**

Heavier molecules move slower for the same kinetic energy/temperature.

(f) The inverse function has a square root shape. As kinetic energy increases, speed increases but more slowly (as the square root). If temperature quadruples, average speed only doubles.

### Solution to Activity 3

(a) Reciprocal function: f(r) = 1/r

(b) E_g = -GMm × (1/r), so c = -GMm (negative scaling)

(c) Domain: (−∞, 0) ∪ (0, ∞), unchanged by scaling

(d) r = 0 means masses overlap - physically meaningless. The point-mass model assumption breaks down.

(e) Restrict domain to (0, ∞) since distance cannot be negative.

(f) Negative c reflects function in x-axis. Instead of decreasing (reciprocal), E_g is increasing on (0, ∞). As r increases, E_g increases (becomes less negative) - planets further from Sun have more gravitational PE.

(g) Asymptotes are coordinate axes:
- As r → ∞, E_g → 0 (maximum value)
- As r → 0, E_g → −∞

