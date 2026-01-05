# Topic 4: Mathematics Practice - The Quantum Realm

## Summary

This mathematics practice explores waves using trigonometric functions from MST124 Unit 4. Both travelling waves and standing waves are fundamental to quantum mechanics - electromagnetic radiation travels as waves, electron beams behave as waves, and electrons in atoms form standing waves.

## Key Equations

### Travelling Waves

| Equation | Name | Description |
|----------|------|-------------|
| v = fλ | Wave speed | Speed = frequency × wavelength |
| f = 1/T | Frequency | Frequency = 1/period |
| y(x) = A sin(kx + φ) | Wave profile | Displacement vs position |
| y(t) = A sin(ωt + φ) | Wave oscillation | Displacement vs time |
| y(x,t) = A sin(kx - ωt + φ) | Travelling wave | Complete wave equation |

### Key Parameters

| Symbol | Name | Definition | Units |
|--------|------|------------|-------|
| A | Amplitude | Max displacement from equilibrium | m |
| k | Angular wavenumber | k = 2π/λ | m⁻¹ (rad m⁻¹) |
| ω | Angular frequency | ω = 2π/T = 2πf | s⁻¹ (rad s⁻¹) |
| φ | Phase constant | Initial phase | radians |
| λ | Wavelength | Distance between peaks | m |
| T | Period | Time between peaks | s |
| f | Frequency | Oscillations per second | Hz (s⁻¹) |

### Standing Waves

**Formation**: Superposition of two travelling waves in opposite directions:
- y₁ = A sin(kx - ωt) (travelling right)
- y₂ = A sin(kx + ωt) (travelling left)

**Result**: y(x,t) = 2A sin(kx) cos(ωt)

**Nodes**: Points where displacement is always zero
- Occur when sin(kx) = 0
- At x = 0, ±λ/2, ±λ, ±3λ/2, ...
- Separation between nodes: λ/2

**Antinodes**: Points of maximum oscillation
- Occur when sin(kx) = ±1
- At x = ±λ/4, ±3λ/4, ±5λ/4, ...
- Separation between antinodes: λ/2

## Trigonometric Relationships

### Sine and Cosine Properties
- cos θ = cos(-θ) (even function)
- sin θ = -sin(-θ) (odd function)
- sin θ = cos(θ - π/2)
- cos θ = sin(θ + π/2)

### Zeros and Maxima
**Cosine function** y = cos θ:
- y = 0 when θ = ±π/2, ±3π/2, ... = ±(2n-1)π/2
- y = +1 when θ = 0, ±2π, ±4π, ...
- y = -1 when θ = ±π, ±3π, ...

**Sine function** y = sin θ:
- y = 0 when θ = 0, ±π, ±2π, ... = ±nπ
- y = +1 when θ = π/2, 5π/2, ...
- y = -1 when θ = -π/2, 3π/2, ...

---

## Activities

### Activity 1

(a) What are the arguments of cos θ for which cos θ = 0? For which cos θ = ±1? How is cos θ related to cos(-θ)?

(b) What are the arguments of sin θ for which sin θ = 0? For which sin θ = ±1? How is sin θ related to sin(-θ)?

(c) How is sin θ related to cos θ?

---

### Activity 2

A sinusoidal wave travelling along a string has wavelength 10 cm, period 0.05 s, and amplitude 2 cm.

(a) Sketch displacement vs position at a certain instant.

(b) Sketch displacement vs time at a certain position.

(c) If initial phase is zero, write down an equation for this travelling wave.

(d) Evaluate the amplitude at x = 90 cm and t = 0.4 s.

---

### Activity 3

Consider the wave y(z,t) = A sin(kz - ωt), where A = 2 m, k = 3 m⁻¹ and ω = 4 s⁻¹.

(a) What is the amplitude of the wave?

(b) What is the wavelength of the wave?

(c) What is the period of the wave?

(d) What is the phase constant of the wave?

---

### Activity 4

For the standing wave y(x,t) = 2A sin(kx) cos(ωt):

(a) For what values of x will y = 0?

(b) What is the separation between successive nodes?

(c) For what values of x will y oscillate between maximum and minimum?

(d) What is the separation between successive antinodes?

---

### Activity 5

Two sinusoidal waves with the same wavelength and amplitude travel in opposite directions on a string at 0.2 m s⁻¹. If the time between moments when the string is perfectly flat is 0.5 s, what is the wavelength? Describe the appearance 0.25 s after it is flat.

---

## Solutions

### Solution to Activity 1

(a) cos θ = 0 when θ = ±(2n-1)π/2 for any integer n
    cos θ = ±1 when θ = ±nπ for any integer n
    cos θ = cos(-θ) for all θ (even function)

(b) sin θ = 0 when θ = ±nπ for any integer n (including zero)
    sin θ = ±1 when θ = ±(2n-1)π/2 for any integer n
    sin θ = -sin(-θ) for all θ (odd function)

(c) sin θ = cos(θ - π/2) or cos θ = sin(θ + π/2)

### Solution to Activity 2

(a) & (b) Sinusoidal curves with amplitude ±2 cm, repeat distance 10 cm, repeat time 0.05 s

(c) k = 2π/(10 cm), ω = 2π/(0.05 s), A = 2 cm, φ = 0
    y(x,t) = (2 cm) sin(2πx/10cm - 2πt/0.05s)

(d) At x = 90 cm, t = 0.4 s:
    y = (2 cm) sin(18π - 16π) = (2 cm) sin(2π) = **0**

### Solution to Activity 3

(a) Amplitude A = **2 m**
(b) λ = 2π/k = 2π/3 m = **(2π/3) m**
(c) T = 2π/ω = 2π/4 s = **(π/2) s**
(d) Phase constant φ = **0**

### Solution to Activity 4

(a) y = 0 when sin(kx) = 0, i.e., kx = 0, ±π, ±2π, ...
    So x = 0, ±π/k, ±2π/k, ... = 0, ±λ/2, ±λ, ...

(b) Separation between nodes = **λ/2**

(c) y oscillates between ±2A when sin(kx) = ±1
    At x = ±π/2k, ±3π/2k, ... = ±λ/4, ±3λ/4, ...

(d) Separation between antinodes = **λ/2**

### Solution to Activity 5

String is flat when maxima of one wave coincide with minima of the other.
Next flat state: waves move λ/2 each in 0.5 s → full wavelength in 1 s
Period T = 1 s, frequency f = 1 Hz

Wavelength: λ = v/f = 0.2 m s⁻¹ / 1 Hz = **0.2 m**

After 0.25 s: Waves moved λ/2 relative to each other → maxima coincide
Appearance: **Sine wave with twice the amplitude of individual waves**

