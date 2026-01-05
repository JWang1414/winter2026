Imagine we have a piston pressing onto a region full of air. To attempt to model the force of each air particle on the piston, we will assume each particle does not interact with each other.

Upon reflecting off the piston, the velocity of the particle swaps from $v_x$ to $-v_x$. Which we can see changes the momentum of the particle. This momentum must have been applied to the piston on contact, which is something like:
$$
\Delta p = 2m v_x
$$
Which happens at a rate of,
$$
\Delta t = \frac{2L}{v_x}
$$
- This is the amount of time it takes for the particle to make a round trip

The effective force is therefore,
$$
F_p = \sum_{part} a_\text{to wall} = \sum_{part} \frac{\Delta p}{\Delta t} = \sum_{part} \frac{m v^2_x}{L} = \frac{m}{L} N <v^2_x> = mnS<v^2_x>
$$
- Suppose to be an angle brackets but I don't know how to insert them

Here, notice that if we double the number of particle and the volume, if $L$ doubles, then the value doesn't scale, but if $S$ doubles, it does. This is the idea of extensive and intensive values. They are values that scale with the number of particles, and values that do not scale, respectively.