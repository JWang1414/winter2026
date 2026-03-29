# Question 2
---
a.
In the chain of coupled masses, the force on the final mass is:
$$
m\ddot{x}_{N} = -k(x_{N}-x_{N-1}) - kx_{N}
$$
Where the final $kx_{N}$ term represents the force from the spring between the mass and the wall. Without this factor, the force on the mass becomes:
$$
m\ddot{x}_{N} = -2kx_{N} + kx_{N-1} \to  m\ddot{x}_{N} = -kx_{N} + kx_{N-1}
$$
In the Python simulation of the system, this manifests as a change in the bottom right value of the matrix:
$$
\begin{bmatrix}
2 & -1 \\
-1 & 2 & -1 \\
 & . & . & . \\
 &  & -1 & 2 & -1 \\
 &  &  & -1 & 2
\end{bmatrix} \to  \begin{bmatrix}
2 & -1 \\
-1 & 2 & -1 \\
 & . & . & . \\
 &  & -1 & 2 & -1 \\
 &  &  & -1 & 1
\end{bmatrix}
$$
Notice the change in the bottom-rightmost entry of the matrix. Furthermore, to make the plots of the system look nicer, I stopped plotting the rightmost point in the system, the one associated with the wall.

The modes in this version of the system look like "half-waves". That is, on the side not connected to a wall, the wave always ends midway through, where an anti-node is.

---
b.
When the stiffness in the chain decreases linearly as a function of the mass in the chain, I notice that the amplitude of the anti-nodes will increase for the masses with a smaller stiffness. Additionally, the distance between nodes gradually decreases as the stiffness decreases.

---
c.
I chose to set the 3rd mass to $\times 10$ the original mass.

At low modes, I notice that the mass appears to be a turning point. Going from left-to-right, the amplitude of oscillations drastically increases once the heavier mass has been passed. The change in amplitude is sudden enough that it resembles a "corner" in a non-differentiable function.

Uniquely, at very high modes, the amplitudes of oscillations approach zero left of the heavy mass, suggesting that the energy no longer goes beyond the heavy mass, isolating it on the right. Interestingly, this results in the formation of wave envelopes. There are two envelopes present in mode 19, and one envelop in mode 20.