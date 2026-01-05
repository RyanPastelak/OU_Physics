# Topic 4 Part 2: A Quantum Theory of Hydrogen

## Summary

Hydrogen is the simplest atom: one electron (-1.60 × 10⁻¹⁹ C) bound to one proton (+1.60 × 10⁻¹⁹ C). The hydrogen emission spectrum shows only discrete colours/frequencies, which is impossible to explain with classical mechanics. Quantum mechanics explains this through **standing waves** and **quantised energy levels**.

## Key Concepts

### The Hydrogen Spectrum
- Light emitted from hydrogen contains only specific colours (discrete spectrum)
- Each colour = specific frequency = specific photon energy
- Discrete energies imply quantised energy levels in the atom

### Standing Waves
- Waves contained between fixed points
- **Nodes**: Points that don't move
- On a spring: nodes at ends, plus additional nodes for higher frequencies
- Higher frequency = more nodes
- On a membrane: circular nodes and linear nodes (along diameters)

### The Schrödinger Model
- Incorporates wave-like properties of electrons
- Predicts shapes of electron waveforms (**orbitals**)
- Shapes similar to standing waves on membranes
- Orbital shapes: spherical, dumb-bell, cloverleaf

### Probability and Electron Clouds
- Cannot predict exact electron position
- Larger wave amplitude = higher probability of finding electron
- **Electron cloud**: Fuzzy representation of all possible positions

## Quantum Numbers

Four quantum numbers uniquely identify each quantum state:

### 1. Principal Quantum Number (n)
- Can be any positive integer: n = 1, 2, 3, 4, ...
- Determines energy level (in hydrogen)
- Higher n = higher energy

### 2. Orbital Quantum Number (l)
- For given n: l can be 0, 1, 2, ... up to (n-1)
- Determines orbital shape
- l = 0: spherical (s orbitals)
- l = 1: dumb-bell (p orbitals)
- l = 2: cloverleaf (d orbitals)
- l = 3: complex (f orbitals)

### 3. Magnetic Quantum Number (mₗ)
- For given l: mₗ can be -l to +l (including 0)
- Total of (2l + 1) possible values
- Determines orbital orientation

### 4. Spin Quantum Number (mₛ)
- Can only be +½ or -½
- Intrinsic property of electron (like tiny magnet)
- Doubles number of quantum states

## Rules for Quantum Numbers (Box 2.1)

| Rule | Description |
|------|-------------|
| Rule 1 | n = 1, 2, 3, ... (any positive integer) |
| Rule 2 | l = 0, 1, 2, ... (n-1) |
| Rule 3 | mₗ = -l to +l (2l+1 values) |
| Rule 4 | mₛ = +½ or -½ |

**Total quantum states for each n**: 2n²

## Number of Quantum States

| l value | Orbitals (2l+1) | Quantum states 2(2l+1) |
|---------|-----------------|------------------------|
| 0 (s) | 1 | 2 |
| 1 (p) | 3 | 6 |
| 2 (d) | 5 | 10 |
| 3 (f) | 7 | 14 |

## Energy Levels of Hydrogen

**E_n = -13.6 eV / n²**

Where:
- E_n = energy of state with principal quantum number n
- n = principal quantum number
- Energy is negative (bound state)

### Energy Unit: Electronvolt
- 1 eV = 1.60 × 10⁻¹⁹ J
- Useful because atomic energies are typically a few eV

### Key Energy Values
- Ground state (n=1): E₁ = -13.6 eV
- n=2: E₂ = -3.4 eV
- n=3: E₃ = -1.51 eV

### Emission Spectrum
- Photon energy = difference between energy levels
- Visible hydrogen spectrum: transitions from n ≥ 3 to n = 2

---

## Problems and Solutions

### Problem 2.1: Energy Levels and Photon Energy

Calculate the energies of the n=2 and n=3 states. What is the energy of a photon emitted in a transition from n=3 to n=2?

**Solution:**

**n=2 state:**
E₂ = -13.6 eV / 2² = -13.6 eV / 4 = **-3.4 eV**

**n=3 state:**
E₃ = -13.6 eV / 3² = -13.6 eV / 9 = **-1.51 eV**

**Photon energy (n=3 → n=2):**
E_photon = E₃ - E₂ = (-1.51 eV) - (-3.4 eV) = **1.89 eV**

(This corresponds to red light at ~656 nm - part of the Balmer series)

---

### Problem 2.2: Energy Conversion to eV

A photon has energy 4.0 × 10⁻¹⁹ J. What is the energy in eV?

**Solution:**
Energy in eV = Energy in J / (1.60 × 10⁻¹⁹ J/eV)
Energy = (4.0 × 10⁻¹⁹ J) / (1.60 × 10⁻¹⁹ J/eV)
Energy = **2.5 eV**

---

### Problem 2.3: Nodes in Electron Cloud

If n = 3, how many rings of nodes can be seen in the cross-section of the electron cloud?

**Solution:** For an s orbital (l = 0) with n = 3:
- Number of spherical (radial) nodes = n - l - 1 = 3 - 0 - 1 = **2 rings of nodes**

(The cross-section shows 2 circular nodes between the nucleus and the outer boundary)

---

### Problem 2.4: Possible l Values

What are the possible values of l for states with n = 4?

**Solution:** Using Rule 2: l can be 0, 1, 2, ... (n-1)

For n = 4: l = 0, 1, 2, 3

Or in letter notation: **4s, 4p, 4d, 4f**

---

### Problem 2.5: Quantum States for n=2

How many different quantum states are there for n = 2?

**Solution:** Using formula: Total states = 2n²
Total = 2 × 2² = 2 × 4 = **8 quantum states**

**Breakdown:**
- n=2, l=0 (2s): 1 orbital × 2 spins = 2 states
- n=2, l=1 (2p): 3 orbitals × 2 spins = 6 states
- Total = 2 + 6 = **8 states**

---

### Problem 2.6: Possible mₗ Values

What are the possible values of mₗ for l = 2?

**Solution:** Using Rule 3: mₗ = -l to +l

For l = 2: mₗ = **-2, -1, 0, +1, +2** (5 values)

This matches (2l + 1) = 2(2) + 1 = 5 ✓

---

## Activities

### Activity 2.1 Waves on a circular membrane

Allow approximately 1 hour

Observe standing waves on a membrane. Classify by:
- Number of linear nodes along diameters (i)
- Number of circular nodes (j)
- Notation: (i, j)

Examples:
- (0, 1): No linear nodes, 1 circular node (edge)
- (1, 1): 1 linear node, 1 circular node

### Activity 2.2 Orbital shapes in hydrogen

Allow approximately 1.5 hours

Use interactive tool to explore orbital shapes:
- Set l = 0, mₗ = 0, vary n: See spherical orbitals with more shells
- Number of spherical nodes increases with n
- For n = 3: 2 rings of nodes visible in cross-section

### Activity 2.3 Orbital shapes in hydrogen (revisited)

Allow approximately 45 minutes

Explore shapes with different l values:
- l = 0: Spherical (s orbitals)
- l = 1: Dumb-bell (p orbitals)
- l = 2: Cloverleaf (d orbitals)

For l ≥ 1: Planes or lines of nodes pass through nucleus.
