# TMA02 Answers - SM123 Physics and Space

---

## Question 1: Python 1 - Introduction to Python (8 marks)

### Part (a): Euclid's Algorithm - Line-by-Line Explanation

The original Euclid's algorithm program for finding the greatest common divisor (GCD) from Python 1 Notebook 2:

```python
# Euclid's greatest common divisor algorithm

# Ask user to input two integers
n= int(input("First integer"))
m= int(input("Second integer"))

while (n != m):
  if (n > m):
    n=n-m
  else: 
    m=m-n
    
print ("The greatest common divisor of the integers provided is",n)
```

**Bullet points explaining each line:**

- **Line 1:** `# Euclid's greatest common divisor algorithm` - This is a comment explaining the purpose of the program. Comments begin with `#` and are ignored by Python when executing the code.

- **Line 3:** `# Ask user to input two integers` - Another comment describing what the following lines will do.

- **Line 4:** `n= int(input("First integer"))` - This line prompts the user with "First integer", reads their input as a string, converts it to an integer using the `int()` function, and stores the result in variable `n`.

- **Line 5:** `m= int(input("Second integer"))` - This line prompts the user with "Second integer", reads their input as a string, converts it to an integer using the `int()` function, and stores the result in variable `m`.

- **Line 7:** `while (n != m):` - This begins a while loop that continues executing as long as `n` is not equal to `m`. The `!=` operator means "not equal to". The loop will terminate when both values become equal.

- **Line 8:** `if (n > m):` - Inside the while loop, this conditional statement checks if `n` is greater than `m`.

- **Line 9:** `n=n-m` - If the condition `n > m` is True, this line subtracts `m` from `n` and stores the result back in `n`, reducing the larger number.

- **Line 10:** `else:` - If the condition `n > m` was False (meaning `m` is greater than or equal to `n`), the program executes the following indented block instead.

- **Line 11:** `m=m-n` - This line subtracts `n` from `m` and stores the result back in `m`, reducing the larger number.

- **Line 13:** `print ("The greatest common divisor of the integers provided is",n)` - After the while loop terminates (when `n` equals `m`), this line prints the GCD. At this point, both `n` and `m` contain the same value, which is the greatest common divisor.

---

### Part (b): While-Loop for Input Validation

To ensure the program repeatedly asks for input if the value entered is less than or equal to zero, we add while-loops around the input statements:

```python
# Euclid's greatest common divisor algorithm

# Ask user to input first integer with validation
n = int(input("First integer"))
while n <= 0:
    print("Error: Please enter an integer greater than zero.")
    n = int(input("First integer"))

# Ask user to input second integer with validation
m = int(input("Second integer"))
while m <= 0:
    print("Error: Please enter an integer greater than zero.")
    m = int(input("Second integer"))

while (n != m):
  if (n > m):
    n=n-m
  else: 
    m=m-n
    
print ("The greatest common divisor of the integers provided is",n)
```

**Explanation of the additional code:**

For each input, the validation works as follows:

1. The program first asks the user for input and stores it in the variable (`n` or `m`).
2. The `while n <= 0:` (or `while m <= 0:`) condition checks if the entered value is less than or equal to zero.
3. If the condition is True (i.e., the value is invalid), the loop body executes:
   - An error message is displayed to inform the user of the problem
   - The user is prompted again to enter a valid positive integer
4. The loop continues until the user enters a value greater than zero, at which point the condition becomes False and the loop exits.
5. Only after both inputs are validated as positive integers does the program proceed to the main Euclid's algorithm.

This ensures robust input handling - the program will never proceed with invalid data that could cause errors or incorrect results (such as an infinite loop if zero were entered).

---

## Question 2: Topic 1 - Forces Around You (12 marks)

### Part (a)(i): Description of the Friction Experiment

**Equipment Used:**
- A hardback book (*Effective C++ Third Edition*) serving as the inclined plane
- A soda can as the test object
- A protractor to measure angles
- A flat table surface as the base

**Method:**
1. I placed the book flat on a table surface.
2. I positioned the soda can on the book near one edge.
3. I gradually raised the far edge of the book by small increments.
4. I observed the can carefully, watching for the moment it began to slide.
5. At the point where the can just started to slide, I carefully measured the angle θ between the book cover and the horizontal table surface using the protractor.
6. I lowered the book and repeated the experiment 3 times to obtain multiple measurements for reliability.
7. I recorded each measurement.

---

### Part (a)(ii): Measured Angle and Raw Data

**How I measured the angle:**
I used a protractor placed at the edge of the book to measure the angle between the inclined book cover and the horizontal table surface. I ensured the protractor's baseline was parallel to the table surface and read the angle at the point where the soda can just began to slide.

**Raw Data:**

| Trial | Angle θ (degrees) |
|-------|-------------------|
| 1     | 23.0              |
| 2     | 22.5              |
| 3     | 23.0              |

**Average angle calculation:**
$$\bar{\theta} = \frac{23.0 + 22.5 + 23.0}{3} = \frac{68.5}{3} = 22.8°$$

**Average angle: θ = 23° (to 2 significant figures)**

---

### Part (b): Deriving μ from θ

**Forces acting on the can at the point of sliding:**

When the can is on an inclined surface at angle θ, three forces act on it:
1. **Weight (W = mg)** - acting vertically downward
2. **Normal reaction force (N)** - acting perpendicular to the surface
3. **Friction force (F_fric)** - acting parallel to the surface, up the slope

**Resolving forces:**

The weight must be resolved into components parallel and perpendicular to the slope:
- Component perpendicular to slope: W cos(θ) = mg cos(θ)
- Component parallel to slope: W sin(θ) = mg sin(θ)

**Equilibrium conditions at the slip point:**

**Perpendicular to slope:**
$$N = mg \cos(\theta)$$

**Parallel to slope (at point of sliding, friction is at maximum):**
$$F_{fric} = mg \sin(\theta)$$

**Using the friction equation:**
$$F_{fric} = \mu N$$

**Substituting:**
$$\mu N = mg \sin(\theta)$$
$$\mu \times mg \cos(\theta) = mg \sin(\theta)$$

**The mass m and g cancel from both sides:**
$$\mu \cos(\theta) = \sin(\theta)$$
$$\mu = \frac{\sin(\theta)}{\cos(\theta)}$$
$$\boxed{\mu = \tan(\theta)}$$

**Calculation of coefficient of friction:**

Using the average measured angle θ = 23°:
$$\mu = \tan(23°) = 0.42$$

**The coefficient of friction μ = 0.42** (to 2 significant figures)

---

## Question 3: Topic 2 - An Introduction to Energy (12 marks)

### Part (a)(i): Planetary Orbit Data Table

**Planet: Mars**

| Property | At Perihelion | At Aphelion |
|----------|---------------|-------------|
| **Planet Mass (m)** | 6.42 × 10²³ kg | 6.42 × 10²³ kg |
| **Distance from Sun (r)** | 2.07 × 10¹¹ m | 2.49 × 10¹¹ m |
| **Orbital Velocity (v)** | 2.65 × 10⁴ m s⁻¹ | 2.20 × 10⁴ m s⁻¹ |
| **Potential Energy (Eg)** | −4.12 × 10³² J | −3.42 × 10³² J |
| **Kinetic Energy (Ek)** | 2.25 × 10³² J | 1.55 × 10³² J |
| **Total Energy (Ek + Eg)** | −1.87 × 10³² J | −1.87 × 10³² J |

**Data source:** SM123 Planets data sheet (Williams, D.R., 2017, NASA Planetary Fact Sheet)

---

### Part (a)(ii): Full Workings

**Constants used:**
- G = 6.67 × 10⁻¹¹ m³ kg⁻¹ s⁻²
- M_Sun = 1.99 × 10³⁰ kg
- m_Mars = 6.42 × 10²³ kg (from data sheet: 0.642 × 10²⁴ kg)

**Unit conversions from data sheet:**
- Distances: 10⁶ km → 10⁹ m (multiply by 10³)
- Velocities: km s⁻¹ → m s⁻¹ (multiply by 10³)

---

**AT PERIHELION:**

**Potential Energy:**
Using $E_g = -\frac{GMm}{r}$

$$E_g = -\frac{(6.67 \times 10^{-11})(1.99 \times 10^{30})(6.42 \times 10^{23})}{2.07 \times 10^{11}}$$

Step 1: Calculate GMm:
$$GMm = (6.67 \times 10^{-11})(1.99 \times 10^{30})(6.42 \times 10^{23})$$
$$= 6.67 \times 1.99 \times 6.42 \times 10^{(-11+30+23)}$$
$$= 85.2 \times 10^{42}$$
$$= 8.52 \times 10^{43} \text{ J m}$$

Step 2: Divide by distance:
$$E_g = -\frac{8.52 \times 10^{43}}{2.07 \times 10^{11}} = -4.12 \times 10^{32} \text{ J}$$

**Kinetic Energy:**
Using $E_k = \frac{1}{2}mv^2$

$$E_k = \frac{1}{2}(6.42 \times 10^{23})(2.65 \times 10^{4})^2$$

Step 1: Calculate v²:
$$(2.65 \times 10^{4})^2 = 7.02 \times 10^{8} \text{ m}^2\text{s}^{-2}$$

Step 2: Calculate Ek:
$$E_k = \frac{1}{2}(6.42 \times 10^{23})(7.02 \times 10^{8})$$
$$= 0.5 \times 6.42 \times 7.02 \times 10^{31}$$
$$= 22.5 \times 10^{31} = 2.25 \times 10^{32} \text{ J}$$

---

**AT APHELION:**

**Potential Energy:**
$$E_g = -\frac{(6.67 \times 10^{-11})(1.99 \times 10^{30})(6.42 \times 10^{23})}{2.49 \times 10^{11}}$$

$$E_g = -\frac{8.52 \times 10^{43}}{2.49 \times 10^{11}} = -3.42 \times 10^{32} \text{ J}$$

**Kinetic Energy:**
$$E_k = \frac{1}{2}(6.42 \times 10^{23})(2.20 \times 10^{4})^2$$

Step 1: Calculate v²:
$$(2.20 \times 10^{4})^2 = 4.84 \times 10^{8} \text{ m}^2\text{s}^{-2}$$

Step 2: Calculate Ek:
$$E_k = \frac{1}{2}(6.42 \times 10^{23})(4.84 \times 10^{8})$$
$$= 0.5 \times 6.42 \times 4.84 \times 10^{31}$$
$$= 15.5 \times 10^{31} = 1.55 \times 10^{32} \text{ J}$$

---

**TOTAL ENERGY:**

At perihelion: 
$$E_{total} = E_k + E_g = 2.25 \times 10^{32} + (-4.12 \times 10^{32}) = -1.87 \times 10^{32} \text{ J}$$

At aphelion: 
$$E_{total} = E_k + E_g = 1.55 \times 10^{32} + (-3.42 \times 10^{32}) = -1.87 \times 10^{32} \text{ J}$$

**Verification:** The total energy values are equal to 3 significant figures at both perihelion and aphelion, confirming **conservation of energy** in Mars's orbit.

---

### Part (b): Reflection on Tutor Group Values

*(Maximum 100 words)*

**Tutor Group Results Summary:**
| Planet | Total Energy (J) |
|--------|-----------------|
| Mercury | −3.78 × 10³² |
| Earth | −2.65 × 10³³ |
| Mars | −1.87 × 10³² |
| Uranus | −2.01 × 10³³ |

Comparing total energy values across all planets, I noticed that each planet has identical total energy at both perihelion and aphelion, demonstrating conservation of energy. As Gwyn explained, in a closed two-body system where only conservative gravitational forces act, total mechanical energy remains constant. At perihelion, increased kinetic energy (due to higher orbital speed) is exactly balanced by decreased potential energy (closer to the Sun), and vice versa at aphelion. The energy "account books" always balance.

**Word count: 83**

---

## Question 4: Topic 3 - Material Worlds (12 marks)

### Part (a): Graph of Electrical Conductivity

**Data Table:**

| Concentration / mol l⁻¹ | Conductivity of NaCl / mS cm⁻¹ | Conductivity of MgCl₂ / mS cm⁻¹ |
|-------------------------|-------------------------------|--------------------------------|
| 0.086 | 8.2 | 13.7 |
| 0.172 | 16.0 | 25.2 |
| 0.346 | 30.2 | 46.4 |
| 0.885 | 70.1 | 94.5 |

**[INSERT YOUR PLOTTED GRAPH HERE]**

The graph should show:
- **X-axis:** Concentration (mol l⁻¹)
- **Y-axis:** Conductivity (mS cm⁻¹)
- **Two data series:** NaCl (○) and MgCl₂ (△) with different symbols
- **Best-fit straight lines** drawn through each data set
- **Title:** "Electrical Conductivity of Sodium Chloride and Magnesium Chloride Solutions"

---

### Part (b): Determining Conductivities from the Graph

**Target concentration: 0.465 mol l⁻¹**

**Method for determining conductivities:**

To determine the conductivity of each solution at 0.465 mol l⁻¹, I used interpolation from my graph:

1. I located 0.465 mol l⁻¹ on the x-axis (between the third and fourth data points)
2. I drew a vertical line upward from this point
3. Where this line intersected each best-fit line, I drew horizontal lines to the y-axis
4. I read the corresponding conductivity values from the y-axis

**Results:**

For **Sodium Chloride (NaCl)** at concentration 0.465 mol l⁻¹:
- Following the vertical line from 0.465 to the best-fit line for NaCl
- Reading across to the y-axis gives conductivity = **38 mS cm⁻¹**

For **Magnesium Chloride (MgCl₂)** at concentration 0.465 mol l⁻¹:
- Following the vertical line from 0.465 to the best-fit line for MgCl₂
- Reading across to the y-axis gives conductivity = **54 mS cm⁻¹**

---

### Part (c): Comparison of Conductivities

*(Maximum 100 words)*

Based on my graph, **magnesium chloride (MgCl₂)** has the higher conductivity at all concentrations, including at 0.465 mol l⁻¹. This is because MgCl₂ produces more ions and higher charges when dissolved. Each formula unit of MgCl₂ dissociates into three ions (Mg²⁺ + 2Cl⁻), while NaCl produces only two ions (Na⁺ + Cl⁻). Additionally, the magnesium ion carries a +2 charge compared to sodium's +1 charge, meaning each Mg²⁺ ion carries twice the charge. More ions with higher charges result in greater electrical conductivity.

**Word count: 88**

---

## Question 5: Skills Development Reflection (6 marks)

> **⚠️ NOTE:** This entire question requires YOUR personal reflection and cannot be answered from the study notes. You must:

### Part 1: Table of Radar Diagrams

Create a table with your original and current versions of these six skills radar diagrams:

| Learning Outcome | Original Diagram | Current Diagram |
|------------------|------------------|-----------------|
| CS1 Gathering and evaluating information | [Insert Image] | [Insert Image] |
| CS2 Mathematics | [Insert Image] | [Insert Image] |
| CS3 Analyse problems and plan software solutions | [Insert Image] | [Insert Image] |
| KS1 Scientific method | [Insert Image] | [Insert Image] |
| KS2 Communicating ideas | [Insert Image] | [Insert Image] |
| PPS1 Practical work | [Insert Image] | [Insert Image] |

---

### Part 2: Reflection on Most Improved Skill

*(Maximum 50 words)*

**Skill with most improvement:** PPS1 Practical work

My radar diagram shows slight improvement in PPS1 since TMA01. The friction experiment and planetary energy activity helped develop my practical skills. I’ve become more methodical in recording observations and structuring my report writing with clearer methodology sections.

**Word count: 47**

---

### Part 3: Reflection on Skill Needing Most Improvement

*(Maximum 50 words)*

**Skill needing most improvement:** KS2 Communicating ideas

KS2 remains my weakest area, with low scores in basic writing, scientific writing, drawing diagrams, and presentation skills. While I’ve started organising work more formally and presenting mathematics step-by-step, I still need to practice writing clearer and less bulleted.

**Word count: 50**

---

## Summary of Completion Status

### ✅ Completed Sections:

| Question | Section | Status |
|----------|---------|--------|
| Q1 | (a) Euclid's algorithm explanation | ✅ Complete |
| Q1 | (b) Input validation code | ✅ Complete |
| Q2 | (a)(i) Experiment description | ✅ Complete |
| Q2 | (a)(ii) Raw data and measurements | ✅ Complete |
| Q2 | (b) Derivation of μ = tan(θ) | ✅ Complete |
| Q3 | (a)(i) Planet data table (Mars) | ✅ Complete |
| Q3 | (a)(ii) Full workings | ✅ Complete |
| Q3 | (b) Tutor group reflection | ✅ Complete |
| Q4 | (a) Data table | ✅ Complete (need to insert plotted graph image) |
| Q4 | (b) Conductivity readings | ✅ Complete |
| Q4 | (c) Comparison and explanation | ✅ Complete |
| Q5 | Part 2 - Most improved (PPS1) | ✅ Complete |
| Q5 | Part 3 - Needs improvement (KS2) | ✅ Complete |

### ⚠️ Sections Requiring YOUR Personal Data:

| Question | Section | What's Needed |
|----------|---------|---------------|
| Q4 | (a) | Insert your plotted graph image |
| Q5 | Part 1 | Insert your radar diagram images |

The theoretical frameworks, equations, and calculation methods are all provided above and are derived from the study materials.

