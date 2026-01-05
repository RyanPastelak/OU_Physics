# Topic 5 Part 3: Energy in Transport

## Summary

Transport accounts for ~40% of UK energy consumption. The main forces opposing vehicle motion are rolling resistance, air resistance, and friction. Understanding how these scale with speed explains fuel consumption patterns.

## Key Concepts

### Transport Energy Usage (UK 2016: 56 Mtoe)
- Road: 41 Mtoe (74% of energy, 83% of distance)
- Air: 13 Mtoe
- Rail: 1.1 Mtoe (2% of energy, 10% of distance)
- Water: 0.56 Mtoe

### Rolling Resistance

Caused by deformation of tyres during rolling (squashing/unsquashing cycle).

**Energy dissipated:**
**E_RR = C_RR × Mgd**

**Power dissipated:**
**P_RR = C_RR × Mgv**

Where:
- C_RR = coefficient of rolling resistance (~0.010 for car tyres)
- M = mass (kg)
- g = 9.81 m s⁻²
- d = distance (m)
- v = speed (m s⁻¹)

**Key insight**: Energy doesn't depend on speed; Power is proportional to speed

### Air Resistance

Caused by pushing air out of the way as vehicle moves.

**Power dissipated:**
**P_air = ½ρC_D Av³**

Where:
- ρ = air density (~1.2 kg m⁻³)
- C_D = drag coefficient (depends on aerodynamics)
- A = frontal cross-sectional area (m²)
- v = speed (m s⁻¹)

**Key insight**: Power is proportional to v³ (cubic!)
- Double speed → 8× power required

### Drag Coefficients

| Object | C_D |
|--------|-----|
| Passenger airplane | 0.012 |
| Dolphin (in water) | 0.0036 |
| Passenger car | 0.26-0.5 |
| Formula 1 car | 0.7-1.1 |
| Bicycle + rider | 0.88-1.1 |
| Passenger train | 1.8 |
| Brick | 2.1 |

### Friction

Rule of thumb: ~15% of engine power lost to transmission
- 85% of engine power delivered to wheels

### Braking

**Kinetic energy dissipated when braking to standstill:**
**E_k = ½mv²**

Frequent braking significantly increases energy consumption (city driving).

### Speed Comparison

At 14 m/s (31 mph):
- Rolling resistance: ~1.9 kW
- Air resistance: ~1.2 kW
- Total: ~3.6 kW (including friction)

At 28 m/s (63 mph):
- Rolling resistance: ~3.8 kW (doubled)
- Air resistance: ~9.8 kW (8× increase!)
- Total: ~16 kW

### Fuel Economy

Petrol engine efficiency: ~25% under typical conditions

Example 14 km commute at 14 m/s:
- Energy dissipated: ~4.7 MJ
- Fuel energy required: ~19 MJ (at 25% efficiency)
- Fuel used: ~0.56 litres
- Economy: ~25 km/l

Real-world: ~12.4 km/l (cars optimized for 50-60 mph)

### Rail vs Road

Trains are more efficient per passenger:
- 50× more energy consumption than car
- But carry 250× more passengers
- Steel wheel on steel track: C_RR = 0.001 (10× better than rubber on road)

---

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| E_RR = C_RR × Mgd | Rolling resistance energy | Energy dissipated rolling |
| P_RR = C_RR × Mgv | Rolling resistance power | Power ∝ speed |
| P_air = ½ρC_D Av³ | Air resistance power | Power ∝ speed³ |
| E_k = ½mv² | Kinetic energy | Energy lost when braking |

---

## Problems and Solutions

### Problem 3.1: Rolling Resistance Power

Find the power dissipated due to rolling resistance for a 1400 kg car at 14 m/s. Use C_RR = 0.010.

**Solution:**
P_RR = C_RR × Mg × v
P_RR = 0.010 × 1400 kg × 9.81 m s⁻² × 14 m s⁻¹
P_RR = 0.010 × 1400 × 9.81 × 14
P_RR = **1923 W ≈ 1.9 kW**

---

### Problem 3.2: Air Resistance Power at Different Speeds

Calculate the power dissipated by air resistance for a car with C_D = 0.31, frontal area 2.41 m², travelling at (a) 14 m/s and (b) 28 m/s.

**Solution:**

**(a) At 14 m/s:**
P_air = ½ρC_D Av³
P_air = ½ × 1.2 kg m⁻³ × 0.31 × 2.41 m² × (14 m s⁻¹)³
P_air = 0.5 × 1.2 × 0.31 × 2.41 × 2744
P_air = **1229 W ≈ 1.2 kW**

**(b) At 28 m/s:**
P_air = ½ × 1.2 × 0.31 × 2.41 × (28)³
P_air = 0.5 × 1.2 × 0.31 × 2.41 × 21952
P_air = **9831 W ≈ 9.8 kW**

**Key observation:** Doubling speed (14 → 28 m/s) increases air resistance power by factor of 8 (because 2³ = 8), from 1.2 kW to 9.8 kW!

---

### Problem 3.3: Kinetic Energy and Braking

What is the kinetic energy of a 1400 kg car at 14 m/s? How much energy is dissipated if it brakes to standstill 8 times in a journey?

**Solution:**

**Kinetic energy at 14 m/s:**
E_k = ½mv²
E_k = ½ × 1400 kg × (14 m s⁻¹)²
E_k = 0.5 × 1400 × 196
E_k = **137,200 J = 137 kJ**

**Energy for 8 stops:**
E_total = 8 × 137 kJ = **1096 kJ ≈ 1.1 MJ**

This is a significant amount of energy - about 23% of the total energy needed for a typical 14 km journey. This is why city driving (frequent stops) uses much more fuel than highway driving.

---

### Problem 3.4: Speed Scaling

If speed doubles, by how much does air resistance power change? Rolling resistance power?

**Solution:**

**Air resistance power:**
P_air ∝ v³
If v doubles: P_air increases by factor of 2³ = **8**

**Rolling resistance power:**
P_RR ∝ v
If v doubles: P_RR increases by factor of **2**

This is why fuel economy drops dramatically at high speeds - air resistance dominates and scales with the cube of speed.

---

### Problem 3.5: Rail vs Road Efficiency

Why is rail transport more energy-efficient per passenger-kilometre than road transport?

**Solution:**

1. **Lower rolling resistance**: Steel wheels on steel tracks have C_RR ≈ 0.001, compared to 0.010 for rubber tyres on road - **10× better**

2. **Higher occupancy**: A train can carry ~250 passengers vs ~1.5 average in a car. Even though total energy use is higher, energy per passenger is much lower

3. **Shared air resistance**: Only the front carriage faces full air resistance; following carriages are partly shielded (drafting effect)

4. **Electrification**: Electric trains can regenerate energy during braking; electric motors are ~90% efficient vs ~25% for petrol engines

**Result**: Rail uses only 2% of UK transport energy but carries 10% of passenger-km (5× more efficient per passenger)

---

### Problem 3.6: Effect of Mass on Fuel Consumption

A driver considers buying a heavier SUV (2000 kg) instead of a lighter car (1200 kg). Ignoring air resistance, by what percentage would rolling resistance power increase?

**Solution:**
P_RR ∝ M (mass)

Percentage increase = (2000 - 1200)/1200 × 100% = 800/1200 × 100% = **67% increase**

The heavier vehicle would use about 67% more fuel just to overcome rolling resistance. This is why lightweight materials (aluminium, carbon fibre) are important for fuel efficiency.
