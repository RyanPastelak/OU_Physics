# Topic 5 Part 2: Domestic Energy

## Summary

Domestic energy accounts for ~29% of UK energy, with 80% used for heating. Understanding heat transfer through conduction, convection, and radiation is essential for efficient home heating.

## Key Concepts

### Heat Transfer

**Heat**: Transfer of energy due to temperature difference (hot → cold)

**Power**: Rate of energy transfer
P = E/t (W = J/s)

### Heat Conduction Equation

**P = -kA(ΔT)/l**

Where:
- P = power (rate of energy transfer) (W)
- k = thermal conductivity (W m⁻¹ K⁻¹)
- A = surface area (m²)
- ΔT = T_in - T_out (temperature difference) (K or °C)
- l = thickness of material (m)

**Negative sign**: Energy flows from hot to cold (system loses energy)

### Thermal Conductivities

| Material | k (W m⁻¹ K⁻¹) |
|----------|---------------|
| Air | 0.024 |
| Rock mineral wool | 0.032-0.044 |
| Expanded polystyrene | 0.034-0.038 |
| Plasterboard | 0.21 |
| Brickwork (inner) | 0.60 |
| Brickwork (outer) | 0.84 |
| Glass | 0.93 |
| Concrete | 1.28 |
| Copper | 390 |

**Good insulators**: LOW thermal conductivity
**Poor insulators**: HIGH thermal conductivity

### Layered Insulation

For multiple layers in contact:

**ΔT = -P/A × (l_A/k_A + l_B/k_B + ...)**

Each layer contributes a term l/k

### Cavity Walls

Example calculation (15°C temperature difference):
- Two 120mm brick walls + 120mm air gap
- Power loss: ~2.84 W per m² (vs 43.8 W/m² for solid wall)

**Most temperature drop occurs across the air gap** (best insulator)

### Convection

- Transfer of energy by physical movement of fluid (gas or liquid)
- Hot air rises, cool air sinks
- Creates circulation patterns
- **Cavity wall insulation** (wool/polystyrene) prevents convection while keeping low conductivity

### Thermal Radiation

**P_rad = AεσT⁴**

Where:
- P_rad = radiated power (W)
- A = surface area (m²)
- ε = emissivity (0 to 1; ~0.9 for painted surfaces)
- σ = Stefan-Boltzmann constant = 5.67 × 10⁻⁸ W m⁻² K⁻⁴
- T = temperature in **Kelvin**

**Key points:**
- All objects above 0 K radiate
- Warmer objects emit more radiation
- Net radiation = radiated - received
- "Radiators" actually transfer most heat by **convection** (air is poor conductor)

---

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| P = -kAΔT/l | Heat conduction | Power through insulating material |
| P = AεσT⁴ | Stefan-Boltzmann | Power radiated by surface |
| T(K) = T(°C) + 273.15 | Temperature conversion | Celsius to Kelvin |

---

## Problems and Solutions

### Problem 2.1: Heat Transfer Through Brick Wall

Calculate the rate of heat transfer through 1 m² of outer brick wall (k = 0.84 W m⁻¹ K⁻¹) that is 240 mm thick when ΔT = 12.5°C.

**Solution:**
P = kA(ΔT)/l (ignoring negative sign for magnitude)
P = (0.84 W m⁻¹ K⁻¹) × (1 m²) × (12.5 K) / (0.240 m)
P = 10.5 / 0.240
P = **43.8 W**

---

### Problem 2.2: Required Concrete Wall Thickness

How thick should a concrete wall be if the rate of heat loss through 1 m² for a 12.5 K temperature difference is to be 40 W?

**Solution:**
Rearranging P = kAΔT/l for l:
l = kAΔT/P
l = (1.28 W m⁻¹ K⁻¹) × (1 m²) × (12.5 K) / (40 W)
l = 16.0 / 40
l = **0.40 m = 400 mm**

---

### Problem 2.3: Shape and Heat Loss

A sphere, cube, and irregular shape have the same volume and wall thickness. Which loses heat fastest?

**Solution:** The **irregular shape** loses heat fastest.

Heat loss is proportional to surface area (P ∝ A). For a given volume:
- A **sphere** has the **smallest** surface area to volume ratio
- A **cube** has an intermediate surface area to volume ratio
- An **irregular shape** typically has the **largest** surface area to volume ratio

Therefore: sphere loses heat slowest, irregular shape loses heat fastest.

(This is why animals in cold climates tend to be more spherical/compact, and animals in hot climates more elongated.)

---

### Problem 2.4: Air vs Cavity Wall Insulation

Compare the thermal conductivity of air with expanded polystyrene. Why is cavity wall insulation used instead of just air?

**Solution:**
- Air: k = 0.024 W m⁻¹ K⁻¹
- Expanded polystyrene: k = 0.034-0.038 W m⁻¹ K⁻¹

Air actually has **lower thermal conductivity** than polystyrene (better insulator in terms of conduction alone). However, cavity wall insulation is used because:

1. **Prevents convection**: Air gaps allow convection currents to form (hot air rises, cool air falls), transferring heat much more efficiently than conduction alone
2. **The insulation prevents air movement**, trapping air in tiny pockets where convection cannot occur
3. Combined effect: insulation + trapped air provides better overall insulation than an open air gap

---

### Problem 2.5: Radiator Power Calculation

Calculate the power radiated by a radiator at 65°C with surface area 1.2 m² and emissivity 0.9. What is the net power if the room is at 21°C?

**Solution:**

**Step 1:** Convert temperatures to Kelvin
- T_radiator = 65 + 273 = 338 K
- T_room = 21 + 273 = 294 K

**Step 2:** Power radiated by radiator
P_rad = AεσT⁴
P_rad = (1.2 m²) × (0.9) × (5.67 × 10⁻⁸ W m⁻² K⁻⁴) × (338 K)⁴
P_rad = 1.08 × 5.67 × 10⁻⁸ × 1.30 × 10¹⁰
P_rad = **798 W** (radiated by radiator)

**Step 3:** Power received from room (at room temperature)
P_rec = AεσT_room⁴
P_rec = 1.2 × 0.9 × 5.67 × 10⁻⁸ × (294)⁴
P_rec = 1.08 × 5.67 × 10⁻⁸ × 7.47 × 10⁹
P_rec = **457 W** (received from room)

**Step 4:** Net power radiated
P_net = P_rad - P_rec = 798 - 457 = **341 W**

---

### Problem 2.6: Which Material is Best Insulator?

Rank these materials from best to worst insulator: glass, concrete, air, copper.

**Solution:** Best to worst insulator (lowest to highest k):

1. **Air** (k = 0.024) - Best insulator
2. **Glass** (k = 0.93)
3. **Concrete** (k = 1.28)
4. **Copper** (k = 390) - Worst insulator (best conductor)

---

## Activities

### Activity 5.1 Calculating heat loss

Estimate heat loss through different parts of a house:
- Walls, roof, windows, floor
- Consider area, material, and thickness
- Sum contributions to find total heat loss rate
