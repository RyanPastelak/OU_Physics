# Topic 8: Mathematics Practice - Coordinate Geometry and Vectors

## Summary

This practice module applies mathematical concepts to Solar System modelling. It uses **coordinate geometry** (circles, spheres, parabolas) to model the shapes and positions of planets and orbits. It also introduces **vectors** to describe position, velocity, and motion in 2D space, essential for planning spacecraft trajectories and understanding orbital dynamics.

## Key Equations

| Equation | Name | Description |
|----------|------|-------------|
| $(x-a)^2 + (y-b)^2 = r^2$ | Circle Equation | Circle with radius $r$ and center $(a,b)$. |
| $x^2 + y^2 + z^2 = r^2$ | Sphere Equation | Sphere centered at origin $(0,0,0)$. |
| $\mathbf{v} = v_x \mathbf{i} + v_y \mathbf{j}$ | Vector Notation | Vector with components $v_x$ and $v_y$. |
| $|\mathbf{v}| = \sqrt{v_x^2 + v_y^2}$ | Magnitude | Length (speed) of vector $\mathbf{v}$. |
| $\mathbf{v}_{total} = \mathbf{v}_{orbit} + \mathbf{v}_{rotation}$ | Relative Velocity | Adding velocity vectors. |

## Key Concepts

-   **Modelling Objects:**
    -   Planets/Moons modelled as circles (2D cross-section) or spheres (3D).
    -   Orbits modelled as circles, ellipses, or parabolas (for escaping comets).

-   **Intersections (Collisions):**
    -   Finding if/where a meteoroid hits Earth involves solving the equations of the path (line) and the Earth (circle) simultaneously.
    -   $b^2 - 4ac < 0$ (Discriminant) means no real solutions $\to$ No collision.

-   **Vectors in Orbits:**
    -   **Orbital Velocity:** Direction changes constantly (tangent to orbit). Speed may be constant (circular) or varying (elliptical).
    -   **Rotational Velocity:** Speed of a point on the equator due to planet's spin.
    -   **Launch Strategy:** Launching in the direction of Earth's rotation and orbit ("Prograde") gives a free speed boost.

## Problems and Solutions

### Activity 1: Coordinate Equations
**Problem:** Earth radius 6370 km. Center at origin.
1.  **Earth Surface (2D):** $x^2 + y^2 = 6370^2$.
2.  **Moon (2D):** Center $(0, 384400)$, Radius 1740. Equation: $x^2 + (y-384400)^2 = 1740^2$.

### Activity 3: Collision Course
**Problem:** Meteoroid path $y = 1.5x - 3245$. Earth $x^2 + y^2 = 6370^2$. Do they intersect?
**Solution:**
Substitute line equation into circle equation:
$x^2 + (1.5x - 3245)^2 = 6370^2$
Expand and solve quadratic for $x$.
If real solutions exist, calculate corresponding $y$.
Result: They intersect at two points. The first one reached is the impact site.

### Activity 5: Adding Velocities
**Problem:**
-   Rotational Velocity: $1670 \text{ km/h}$ East (vector $\mathbf{i}$).
-   Orbital Velocity: $108,000 \text{ km/h}$ in direction $\mathbf{j}$.
**Solution:**
Total Velocity Vector $\mathbf{v} = 1670\mathbf{i} + 108000\mathbf{j}$.
Magnitude $|\mathbf{v}| = \sqrt{1670^2 + 108000^2} \approx 108,013 \text{ km/h}$.
Launch East to add these magnitudes!
