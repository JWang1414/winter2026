To determine a definition of temperature, we would like:
- $T$ to be uniform at equilibrium
- $T$ is intensive
- $T$ should be proportional to energy in the system

- Derivation for temperature in class is the same as the one provided in the notes, I'll just note down some things to remember
- Entropy is an extensive variable, and so $S_{TOT}(E_{TOT})=S_{A}(E_{A})+S_{B}(E_{B})$
- By definition, at equilibrium, the entropy should not change as a function of energy (within a subsystem)
	- It must be within a subsystem, because in a total system, energy cannot go in or out, so the energy is constant, always

This is the chain rule in the derivation:
$$
\frac{ \partial S_{t} }{ \partial E_{A} } =0 \implies \frac{ \partial S_{A} }{ \partial E_{A} } + \frac{ \partial S_{B} }{ \partial E_{B} } \frac{ \partial E_{B} }{ \partial E_{A} } =0
$$
And, as said in the write-up
$$
\frac{ \partial E_{A} }{ \partial E_{B} } =-1
$$
# Boltzmann distribution
- Setup is the same as in the write-up. $A$ has one particle, and $B$ has the rest of the particles
$S_{B}\approx S_{t}$ and the entropy in the system is proportional to:
$$
\Omega_{A}(\varepsilon) \propto P_{A}(\varepsilon) = P_{B}(E_{t}-\varepsilon) \propto \exp \left[ \frac{S_{B}(E_{t}-\varepsilon)}{k_{B}} \right]
$$
Use the Taylor series expansion of $S_{B}$
$$
S_{B}(E_{t} - \varepsilon) = S_{B}(E_{t}) - \varepsilon \frac{ \partial S_{B} }{ \partial E_{B} } \bigg|_{E_{t}} + \frac{\varepsilon^{2}}{2!} \left( \frac{ \partial S_{B} }{ \partial E_{B}^{2} }  \right)\bigg|_{E_{T}} + \dots
$$
The first term is constant, and the second term is intensive. The third term and beyond, however, all scale inversely with the number of particles, and so they drop out of the approximation. Therefore we have,
$$
P_{A}(\varepsilon) = c_{1} \exp \left( -\frac{\varepsilon}{k_{B}T} \right)
$$
This is the Boltzmann distribution

Recall that this function $P_{A}$ is the number of microscopic states in this system. This is how we know temperature governs both macroscopic equilibrium (original definition we found), and microscopic energy fluctuations
# Mean Energy per Particle
We know from the definition of the ensemble average that,
$$
\left< \varepsilon \right> = \int_{0}^{\infty} \varepsilon e^{ -\varepsilon/kT } g(\varepsilon) \, d\varepsilon \left[ \int_{0}^{\infty} e^{ -\varepsilon/kT } g(\varepsilon) \, d\varepsilon  \right] ^{-1} = \frac{(kT)^{2}}{kT} = kT
$$
Where $g(\varepsilon)$ is a degeneracy function
- Yea honestly I have no idea where these functions came from and how the average is computed this way. It makes intuitive sense but the precise details I don't get
# Thermodynamic Identities
Energy and temperature are conjugate variables of each other. Likewise, volume and pressure are also conjugate variables, so we might expect:
$$
P \propto \frac{ \partial S }{ \partial V } \bigg|_{E, N}
$$
- The subscript here indicates that $E$ and $N$ are held constant
The units of this derivative are:
$$
\frac{\text{Energy}}{\text{Temperature} \times\text{Volume}} = \frac{\text{Force}\times \text{Distance}}{\text{Temperature} \times\text{Volume}} = \frac{\text{Force}}{\text{Temperature}\times \text{Area}}
$$
Which is very close to the units of pressure, but we need to add a correction:
$$
\frac{P}{T} = \frac{ \partial S }{ \partial V } \bigg|_{E, N}
$$
