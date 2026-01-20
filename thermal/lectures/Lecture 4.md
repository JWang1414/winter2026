- This lecture was cancelled. This is based on provided notes
Consider two isolated thermodynamic subsystems $A$ and $B$ that can exchange energy with each but nothing else. The total energy $E_{t}=E_{A} + E_{B}$ is fixed, but the individual energies can fluctuate.

By extensivity, the entropy of the total isolated system is the sum of the two subsystems:
$$
S_{t}(E_{t}, E_{A}) = S_{A}(E_{A}) + S_{B}(E_{B})
$$
Recall that $E_{B}$ and $E_{A}$ are dependent on each other.

Equilibrium occurs when $S_{t}$ is maximized with respect to $E_{A}$, and so $\partial_{E_{A}}S_{t}=0$. Applying the chain rule and the fact that $\partial_{E_{A}}E_{B}=-1$ we have,
$$
\frac{ \partial S_{A} }{ \partial E_{A} } = \frac{ \partial S_{B} }{ \partial E_{B} }
$$
This is the definition of thermal equilibrium.

Arising from this definition is the statistical definition of temperature:
$$
\frac{1}{T} = \left(  \frac{ \partial S }{ \partial E }  \right)_{\varepsilon \neq E}
$$
- I think the subscript indicates that the number of particles in the system is constant
- We know this just because the original derivative has units of inverse temperature
# Temperature as energy per particle
Consider an ideal gas with total energy $E$, consisting of $N$identical point-like particles of mass $m$ that do not interact. A microstate compatible with $(N, e)$ is specified by the set of velocities $\{ v_{j} \}_{j=1,\dots,N}$under the constraint
$$
\sum_{j=1}^{N} v^{2}_{j, x} + v^{2}_{j, y} + v^{2}_{j, z} = \frac{2E}{m}
$$
The entropy of this system is,
$$
S=\frac{3}{2} N \ln E + \ln f(N) \qquad N\gg 1
$$
And from the previously established definition of temperature,
$$
T = \frac{ \partial S }{ \partial E } ^{-1} = \frac{2}{3} \frac{E}{N}
$$
So the temperature is proportional to the average energy per particle. (As we might think)
## Boltzmann distribution
Take a very extreme case of two subsystems where $A$ has just one particle of energy $\varepsilon$, and $B$ has the rest of the particles. The energy in $B$ is roughly constant,
$$
E_{B} = E_{t} - \varepsilon \approx E_{t} \gg \varepsilon
$$
The probability $A$ has energy $\varepsilon$ is equal to the probability $B$ has the energy of everything else, which is proportional to the number of microstates in $B$ with this energy,
$$
P_{A}(E_{A}) \propto \exp \left[ \frac{S_{B}(E_{t}-\varepsilon)}{k} \right]
$$
Use a Taylor series expansion of $S_{B}$ around $E_{t}$,
$$
S_{B}(E_{t}-\varepsilon) \approx S_{B}(E_{t}) - \varepsilon \left( \frac{ \partial S_{B} }{ \partial E_{B} }  \right)_{E_{t}} + \dots
$$
- The higher order terms vanish because of the extensivity of $S_{B}$ and $E_{B}$

Further approximating $S_{B}\approx S_{t}$ and $E_{B}\approx E_{t}$ we obtain,
$$
P_{A}(\varepsilon) = c_{1} e^{ -\beta\varepsilon } \qquad \beta=\frac{1}{kT}, \qquad T^{-1} = \frac{ \partial S }{ \partial E }
$$
Which is the Boltzmann distribution. It shows that the same definition of temperature governs both macroscopic equilibrium and microscopic energy fluctuations.

If the number of particle states with energy $\varepsilon \in[0, \infty)$ (also called the degeneracy) takes the form $g(\varepsilon)\propto\varepsilon^{p}$ the normalization and mean energy are,
$$
c_{1} = \frac{\beta^{p+1}}{p!} \qquad \left< \varepsilon \right> = \int_{0}^{\infty} \varepsilon e^{ -\beta\varepsilon }g(\varepsilon) \, d\varepsilon = (p+1) kT
$$
