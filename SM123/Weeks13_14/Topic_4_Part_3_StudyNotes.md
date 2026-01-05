# Topic 4 Part 3: Quantum Mechanics and the Periodic Table

## Summary

The structure of the Periodic Table - its groups, periods, and blocks - is a direct consequence of quantum mechanics. The Pauli exclusion principle and the filling order of orbitals explain why elements have their characteristic properties.

## Key Concepts

### Quantum States in Many-Particle Systems
- Bound particles have quantised energies (discrete energy levels)
- All atoms have energy levels (electrons bound to nucleus)
- Molecules also have energy levels → discrete spectra

### Hydrogen-like Ions
Single-electron ions (H, He⁺, Li²⁺, etc.):
- Same orbital shapes as hydrogen (scaled by 1/Z)
- Energy levels: **E_n = -13.6 × Z² / n² eV**
- Higher Z = stronger binding = lower energy

### Letter Notation for Orbitals
| l value | Letter | Name |
|---------|--------|------|
| 0 | s | sharp |
| 1 | p | principal |
| 2 | d | diffuse |
| 3 | f | fundamental |

**Mnemonic**: "Science People Don't Forget"

**Notation**: Number (n) + letter (l)
- 1s: n=1, l=0
- 2p: n=2, l=1
- 3d: n=3, l=2
- 4f: n=4, l=3

### Multi-Electron Atoms
- Electrons repel each other (not just attracted to nucleus)
- Energy depends on both n AND l (unlike hydrogen)
- Outer electrons "screened" from nucleus by inner electrons

### The Pauli Exclusion Principle
**No two electrons can have the same quantum state (same four quantum numbers).**

Consequences:
- Each orbital (defined by n, l, mₗ) can hold maximum 2 electrons
- The two electrons must have opposite spins (mₛ = +½ and -½)
- This gives structure to the Periodic Table

### The Madelung Rule
**Orbitals fill in order of increasing (n + l). When (n + l) is equal, lower n fills first.**

Filling order:
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s → 5f → 6d → 7p

Note: 4s fills before 3d (both have n+l = 4, but 4s has lower n)

### Maximum Electrons per Orbital Type
| Orbital | l | Orbitals (2l+1) | Max electrons 2(2l+1) |
|---------|---|-----------------|----------------------|
| s | 0 | 1 | 2 |
| p | 1 | 3 | 6 |
| d | 2 | 5 | 10 |
| f | 3 | 7 | 14 |

### Electronic Configurations
Write orbitals with superscript showing number of electrons:

| Atom | Electrons | Configuration |
|------|-----------|---------------|
| H | 1 | 1s¹ |
| He | 2 | 1s² |
| Li | 3 | 1s² 2s¹ |
| Be | 4 | 1s² 2s² |
| B | 5 | 1s² 2s² 2p¹ |
| C | 6 | 1s² 2s² 2p² |
| N | 7 | 1s² 2s² 2p³ |
| O | 8 | 1s² 2s² 2p⁴ |
| F | 9 | 1s² 2s² 2p⁵ |
| Ne | 10 | 1s² 2s² 2p⁶ |

## Structure of the Periodic Table

| Block | Orbitals | Groups wide | Why |
|-------|----------|-------------|-----|
| s-block | s orbitals | 2 | 2 quantum states |
| p-block | p orbitals | 6 | 6 quantum states |
| d-block | d orbitals | 10 | 10 quantum states |
| f-block | f orbitals | 14 | 14 quantum states |

- **Period 1**: 1s only → 2 elements
- **Period 2**: 2s, 2p → 8 elements
- **Period 3**: 3s, 3p → 8 elements
- **Period 4**: 4s, 3d, 4p → 18 elements (includes transition metals)

**Elements in same group have similar properties because they have the same number of outer electrons.**

---

## Problems and Solutions

### Problem 3.1: Pauli Exclusion and Helium

Why does it not violate the Pauli exclusion principle for both electrons in He to be in 1s states?

**Solution:** The two electrons in helium have the **same n, l, and mₗ** values (1, 0, 0), but they have **different mₛ** values:
- One electron: mₛ = +½ (spin up)
- Other electron: mₛ = -½ (spin down)

Since all four quantum numbers are not identical for the two electrons, the Pauli exclusion principle is not violated. The 1s orbital can hold exactly 2 electrons because there are only 2 possible spin states.

---

### Problem 3.2: Li²⁺ Ground State Energy

The Li²⁺ ion has atomic number Z = 3 and one bound electron. Calculate the ground state energy.

**Solution:**
Using E_n = -13.6 × Z² / n² eV

For ground state (n = 1) with Z = 3:
E₁ = -13.6 × 3² / 1²
E₁ = -13.6 × 9 / 1
E₁ = **-122.4 eV**

(Much more strongly bound than hydrogen because of higher nuclear charge)

---

### Problem 3.3: 4p Orbital Quantum Numbers

What are the n and l quantum numbers of a 4p orbital?

**Solution:**
- The number 4 tells us **n = 4**
- The letter p corresponds to **l = 1**

So: n = 4, l = 1

---

### Problem 3.4: Quantum Numbers for N Electrons

How many quantum numbers are needed to describe the quantum states of an atom with N electrons?

**Solution:** Each electron requires **4 quantum numbers** (n, l, mₗ, mₛ).

For N electrons: **4N quantum numbers** are needed.

Example: Helium (N = 2) needs 8 quantum numbers to fully describe its state.

---

### Problem 3.5: Six 2p States

What are the quantum numbers of the six 2p states?

**Solution:**
For 2p: n = 2, l = 1

Possible mₗ values: -1, 0, +1
Possible mₛ values: +½, -½

| State | n | l | mₗ | mₛ |
|-------|---|---|----|----|
| 1 | 2 | 1 | -1 | +½ |
| 2 | 2 | 1 | -1 | -½ |
| 3 | 2 | 1 | 0 | +½ |
| 4 | 2 | 1 | 0 | -½ |
| 5 | 2 | 1 | +1 | +½ |
| 6 | 2 | 1 | +1 | -½ |

---

### Problem 3.6: Calcium Electron Configuration

Determine the ground state electron configuration for a Ca atom with 20 electrons.

**Solution:**
Following the Madelung rule filling order:
1s² → 2s² → 2p⁶ → 3s² → 3p⁶ → 4s²

Counting: 2 + 2 + 6 + 2 + 6 + 2 = 20 ✓

**Ca: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²**

(Note: 4s fills before 3d because 4s has lower energy in multi-electron atoms)

---

### Problem 3.7: Quantum States for d Orbitals

How many quantum states are associated with d orbitals?

**Solution:**
For d orbitals: l = 2

Number of orbitals = 2l + 1 = 2(2) + 1 = 5 orbitals

Each orbital can hold 2 electrons (2 spin states)

Total quantum states = 5 × 2 = **10 quantum states**

(This is why the d-block of the Periodic Table is 10 groups wide)

---

## Activities

### Activity 3.1 The Madelung rule

Allow approximately 15 minutes

Complete the (n + l) values:

| Orbital | n | l | n + l |
|---------|---|---|-------|
| 1s | 1 | 0 | **1** |
| 2s | 2 | 0 | **2** |
| 2p | 2 | 1 | **3** |
| 3s | 3 | 0 | **3** |
| 3p | 3 | 1 | **4** |
| 3d | 3 | 2 | **5** |
| 4s | 4 | 0 | **4** |
| 4p | 4 | 1 | **5** |
| 4d | 4 | 2 | **6** |
| 4f | 4 | 3 | **7** |

**Filling order based on n+l:**
- n+l = 1: 1s
- n+l = 2: 2s
- n+l = 3: 2p, 3s (2p has higher n, so 3s fills after 2p? No - lower n fills first when n+l equal, so 2p before 3s)
- n+l = 4: 3p, 4s (3p before 4s)
- n+l = 5: 3d, 4p (3d before 4p)
- n+l = 6: 4d, 5s, 5p...
