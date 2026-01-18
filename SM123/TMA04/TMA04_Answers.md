# TMA04 Answers - SM123 Physics and Space

---

## Question 1: Python 3 – Arrays and Plotting (20 marks)

### Part (a): Peer Review of Another Student
*[Paste your peer review comments here]*

### Part (b): Reflection on Feedback Received
*[Paste the feedback you received here]*

**Reflection (Max 150 words):**
*[Write your reflection here. Example: The feedback pointed out that my graph labels were too small. I will ensure all future plots use clearly readable font sizes and include units in the axis labels as standard practice. This aligns with good scientific communication principles.]*

---

## Question 2: Python 4 – Data Analysis (20 marks)

### Part (a): Jupyter Notebook
> **Action:** Save your Python program as a Jupyter Notebook (`.ipynb`) and include it in your submission zip file.

### Part (b): Rydberg Constant and RMSD Values

**Results from Analysis:**

| Dataset | Rydberg Constant ($R$) | Initial Quantum No. ($n_f$) | RMSD |
| :--- | :--- | :--- | :--- |
| **Lseries (Accurate)** | $1.36 \times 10^{1} \text{ eV}$ | $1.00$ | $1.62 \times 10^{-4} \text{ eV}$ |
| **Student (Rough)** | $1.38 \times 10^{1} \text{ eV}$ | $1.01$ | $1.16 \times 10^{-2} \text{ eV}$ |

**Comment:**
The Root Mean Square Deviation (RMSD) for the **Lseries** data ($1.6 \times 10^{-4}$) is significantly smaller (by two orders of magnitude) than for the **Student** measurements ($1.2 \times 10^{-2}$). This indicates that the fit to the Lseries data is much better, reflecting the higher precision of the experimental data compared to the student measurements.

### Part (c): Graphs
*[Paste your generated plots of Energy vs $1/n_i^2$ with best-fit lines here]*

### Part (d): Modifying for Wavelength

To use wavelength ($\lambda$) instead of energy ($E$), we use the relation $E = hc/\lambda$.
The Rydberg formula becomes:
$$ \frac{hc}{\lambda} = R \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right) $$
Dividing by $hc$:
$$ \frac{1}{\lambda} = \frac{R}{hc} \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right) = R_H \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right) $$
I would modify the program to:
1.  Read $\lambda$ from the file.
2.  Calculate $y = 1/\lambda$ (wavenumber).
3.  Fit $y$ against $x = 1/n_i^2$.
4.  The gradient would be $-R_H$ (Rydberg constant for hydrogen in $\text{m}^{-1}$) and the intercept would be $R_H/n_f^2$.

---

## Question 3: Topic 7 – Distance to the Moon (16 marks)

### Part (a): Measurements
*[Paste your measurements here: Coin diameter ($d_{coin}$), Distance to eye ($L$)]*

**Comment:**
*(Max 100 words)* e.g., Holding the coin steady at the exact distance where it just covered the Moon was challenging due to hand tremors. Repeatability was fair, with distance measurements varying by about 5%.

### Part (b): Calculation

**Theory:**
Using small angle approximation: $\theta_{rad} \approx \frac{d_{coin}}{L} \approx \frac{D_{Moon}}{D_{Earth-Moon}}$.
$$ D_{Earth-Moon} = D_{Moon} \times \frac{L}{d_{coin}} $$

**Calculation:**
*   $D_{Moon} \approx 3474 \, \text{km}$ (Diameter of Moon)
*   $d_{coin} = $ [Your Value] m
*   $L = $ [Your Value] m

$$ D_{Earth-Moon} = 3474 \times \frac{\text{[Your L]}}{\text{[Your d]}} \approx \text{[Result]} \, \text{km} $$

*(Example: If $d=0.02$ m and $L=2.2$ m, Distance $\approx 380,000$ km)*.

---

## Question 4: Topic 8 – Dust Grain Size (16 marks)

### Part (a): Table A1 Measurements
*[Paste your table rows here]*

### Part (b): Histogram
*[Paste your histogram of mean crater diameters here]*

**Comment:** *e.g., The distribution appears random/uniform across the range, or shows a peak around X $\mu$m.*

### Part (c): Mean and Median
*   **Mean:** [Value]
*   **Median:** [Value]
*   **Range:** [Value]

**Comment:** *If Mean $\neq$ Median, the distribution is skewed (e.g., mean > median implies positive skew/tail of large craters).*

### Part (d): Calculation using Mean
Using Equation 1.1 (Calibration): $D_{projectile} = m \times D_{crater} + c$.
*(Substitute your mean crater diameter into the calibration equation provided in the activity notes to find the projectile size).*

### Part (e): Calculation using Median
*(Repeat calculation using the median crater diameter).*

### Part (f): Sources of Error
1.  **Measurement Error:** Difficulty in defining the exact edge of the crater under the microscope.
2.  **Irregular Shapes:** Craters are not perfectly circular; averaging diameter helps but introduces uncertainty.
3.  **Calibration Uncertainty:** The equation linking crater size to particle size has its own experimental errors (upper/lower limits of gradient).

---

## Question 5: Topic 9 – Nucleosynthesis (16 marks)

### Part (a)(i): Primordial Nucleosynthesis Conditions
*   **Time:** Occurred from approx. **3 minutes** to **20 minutes** after the Big Bang.
*   **Temperature:** Cooled from approx. $10^9 \, \text{K}$ (1 billion K).
*   **Energy:** High enough for fusion but low enough for deuterium to survive (deuterium bottleneck).

### Part (a)(ii): Reactions and Products
**Five Principal Reactions:**
1.  $p + n \to D + \gamma$ (Deuterium formation)
2.  $D + D \to {}^3\text{He} + n$
3.  $D + D \to {}^3\text{H} (T) + p$
4.  $D + {}^3\text{He} \to {}^4\text{He} + p$
5.  $D + {}^3\text{H} \to {}^4\text{He} + n$

**Stable Nuclei Remaining:**
Hydrogen ($^1\text{H}$), Helium-4 ($^4\text{He}$), Deuterium ($D$ or $^2\text{H}$), Helium-3 ($^3\text{He}$), Lithium-7 ($^7\text{Li}$).

**Proportions (by mass):**
*   Hydrogen: $\approx 75\%$
*   Helium-4: $\approx 25\%$
*   Others (D, $^3\text{He}$, Li): Trace amounts ($< 0.01\%$).

### Part (b)(i): Stellar Nucleosynthesis
Stars fuse hydrogen into helium during their main sequence. In later stages (Red Giants), they fuse helium into carbon and oxygen (triple-alpha process). Massive stars continue fusing heavier elements up to **Iron (Fe)** (silicon burning). Elements heavier than iron are produced via the **s-process** (slow neutron capture) in asymptotic giant branch stars, creating elements like Barium and Lead.

### Part (b)(ii): Supernova Nucleosynthesis
Explosive nucleosynthesis in supernovae produces elements heavier than Iron via the **r-process** (rapid neutron capture). The immense flux of neutrons allows nuclei to capture neutrons faster than they decay, building up very heavy, neutron-rich isotopes (e.g., Uranium, Gold, Platinum). The explosion also disperses these elements into the interstellar medium.

---

## Question 6: Skills Reflection (12 marks)

### Part (a): Radar Diagrams Table

| Learning outcome | Previous diagram (TMA 03) | Current diagram (TMA 04) |
| :--- | :--- | :--- |
| **CS1** | *[Insert Image]* | *[Insert Image]* |
| **CS2** | *[Insert Image]* | *[Insert Image]* |
| **CS3** | *[Insert Image]* | *[Insert Image]* |
| **KS1** | *[Insert Image]* | *[Insert Image]* |
| **KS2** | *[Insert Image]* | *[Insert Image]* |
| **PPS4** | *[Insert Image]* | *[Insert Image]* |

### Part (b): Most/Least Improved
*   **Most Improved:** [e.g., PPS4]. *Reason: Writing the Python programs for data analysis has greatly improved my understanding of loops and functions, and I can now debug code more confidently.*
*   **Needs Improvement:** [e.g., KS1]. *Reason: I struggled with evaluating the sources of error in the dust grain experiment. I need to practice systematically identifying experimental uncertainties.*

### Part (c): Action Plan
*   **Skill:** [e.g., PPS4]
*   **Action:** *I plan to reuse the plotting code templates I created in this module for future data analysis tasks to save time and ensure consistent formatting.*
