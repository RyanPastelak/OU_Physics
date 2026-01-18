# Topic 7 Part 2: Planetary Systems and Their Motion

## Summary

This part focuses on the Solar System and the laws governing planetary motion. It classifies the various objects orbiting the Sun (planets, dwarf planets, satellites, etc.) and introduces **Kepler's Laws** of planetary motion. These laws describe orbital shapes (ellipses), speeds, and the relationship between orbital period and distance. The section extends these concepts to **exoplanets** (planets orbiting other stars), explaining how they are detected using the transit and radial velocity methods.

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| $e$ | Eccentricity | Describes the shape of an orbit ($0$ = circle, $0 < e < 1$ = ellipse). |
| $P^2 = k a^3$ | Kepler's Third Law (General) | Square of period ($P$) proportional to cube of semimajor axis ($a$). |
| $P^2 = \left[\frac{4\pi^2}{GM}\right] a^3$ | Kepler's Third Law (Physics) | Relates period to central mass $M$. Assumes $M \gg m_{planet}$. |
| $P^2 = a^3$ | Kepler's Third Law (Solar) | Simplified for Solar System when $P$ is in years and $a$ in AU. |
| $\text{Transit Depth} = \left(\frac{R_{planet}}{R_{star}}\right)^2$ | Transit Equation | Fraction of starlight blocked during a transit. |
| $v_{rad} \propto \frac{M_{planet} \sin i}{\sqrt{M_{star} a_{planet}}}$ | Radial Velocity | Amplitude of star's wobble depends on planet mass and inclination. |

## Key Concepts

-   **Solar System Classification:**
    -   **Terrestrial Planets:** Rocky, inner solar system (Mercury, Venus, Earth, Mars).
    -   **Giant Planets:** Gaseous/Icy, outer solar system (Jupiter, Saturn, Uranus, Neptune).
    -   **Dwarf Planets:** Massive enough to be spherical but haven't cleared their orbit (e.g., Pluto, Ceres).
    -   **Satellites:** Moons orbiting planets.
    -   **Asteroids/Comets:** Smaller rocky/icy bodies.

-   **Kepler's Laws:**
    1.  **First Law:** Orbits are **ellipses** with the Sun at one focus.
    2.  **Second Law:** Planets move faster when closer to the Sun (perihelion) and slower when further away (aphelion).
    3.  **Third Law:** The square of the orbital period is proportional to the cube of the semi-major axis ($P^2 \propto a^3$).

-   **Exoplanet Detection:**
    -   **Transit Method:** Measuring the dip in brightness as a planet passes in front of its star. Gives **radius** of the planet.
    -   **Radial Velocity:** Measuring the Doppler shift of the star as it wobbles due to the planet's gravity. Gives **mass** (lower limit) of the planet.
    -   **Direct Imaging:** Very rare, used for distant, hot planets.

-   **Proxima b:** The nearest exoplanet, orbiting Proxima Centauri (4.2 ly away). It is in the "habitable zone" where liquid water could exist.

## Problems and Solutions

### Question: Using Kepler's Third Law
**Problem:** An asteroid has a semi-major axis $a = 4$ AU. What is its orbital period $P$?
**Solution:**
Using $P^2 = a^3$ (in years and AU):
$P^2 = 4^3 = 64$
$P = \sqrt{64} = 8 \text{ years}$.

### Activity 2.2: Mass of Jupiter
**Aim:** To determine the ratio of the Sun's mass to Jupiter's mass using the orbits of their satellites.
**Method:**
1.  Plot $P^2$ vs $a^3$ for planets orbiting the Sun. Gradient $m_{sun} = k/M_{sun}$.
2.  Plot $P^2$ vs $a^3$ for Galilean moons orbiting Jupiter. Gradient $m_{jup} = k/M_{jup}$.
3.  Ratio of masses $M_{sun}/M_{jup} = \text{Gradient}_{jup} / \text{Gradient}_{sun}$.
**Result:** The Sun is approximately 1000 times more massive than Jupiter.

### Question: Transit Depth
**Problem:** A planet with radius $R_p = 0.1 R_{star}$ transits its star. What is the % dip in brightness?
**Solution:**
$\text{Depth} = (R_p/R_{star})^2 = (0.1)^2 = 0.01$.
This corresponds to a **1%** dip in brightness.

## Activities

### Activity 2.4: Transit Investigation
**Observations:**
-   Larger planet $\to$ Deeper transit (more light blocked).
-   Larger star $\to$ Shallower transit (planet blocks smaller fraction).
-   Inclination must be near $90^\circ$ (edge-on) to see a transit at all.

### Activity 2.5: Radial Velocity
**Observations:**
-   More massive planet $\to$ Larger velocity amplitude (stronger gravity tug).
-   Closer orbit $\to$ Larger velocity amplitude (stronger gravity).
-   Inclination $90^\circ$ gives max amplitude; $0^\circ$ (face-on) gives zero radial velocity.
