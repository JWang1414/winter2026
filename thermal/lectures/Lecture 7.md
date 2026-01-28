- This lecture was cancelled. These are notes from the readings
# Why study the ideal gas?
Statistical mechanics tells us which function encodes the equilibrium properties:
- Entropy for the microcanonical
- Partition function of Helmholtz free energy for the canonical
- Grand partition function or grand potential for the grand canonical

Recall that, once this function is known, the probability of every microstate is determined. All thermodynamic observables can be derives from it.

We study the ideal gas as a simplest complete example. It is how we see how statistical mechanics yields experimentally verified laws.
# Ideal gas in the canonical ensemble
In the ideal gas, none of the particle interact, so the total energy is the sum of kinetic energies:
$$
E(\vec{p}_{j}) = \sum_{j=1}^{N} K(\vec{p}_{j}) \qquad K(\vec{p}_{j}) = \frac{\lvert \vec{p}_{j} \rvert ^{2}}{2m}
$$
Where $j\in[1, N]$ and $K$ denotes the kinetic energy.

In the canonical ensemble, $(T, V, N)$ are fixed, and so we are interested in computing the partition function $Z_{N}$ and deducing thermodynamic quantities from it
- Why do we know this is what we have to do?

The canonical partition function factorizes into a fairly simple quantity:
$$
\mathcal{Z}_{N} = \frac{1}{N!} \sum_{i_{1}, \dots, i_{N}} e^{ -\beta \sum_{j}e(i_{j}) } = \frac{1}{N!} \left[ \sum_{i_{j}} e^{ -\beta e(i_{j}) } \right] ^{N} = \frac{\mathcal{Z}_{1}^{N}}{N!}
$$
- I'm not sure what the notation in the first summation implies
- I don't really get how this factorization works
# Maxwell distribution and one-particle partition function
To convert sums of microstates into integrals, consider the elementary cell of volume:
$$
\delta p\delta q=h
$$
Which $h$, Planck's constant, is the smallest phase-space cell allowed by Heisenberg uncertainty. Apply the continuum limit and the one-particle partition function becomes:
$$
\mathcal{Z}_{1} = \int \frac{d^{d}\vec{q}d^{d}\vec{p}}{(\delta p\delta q)^{d}} \exp \left[ -\frac{\beta p^{2}}{2m} \right] = \mathcal{Z}_{1} =V  \int \frac{d^{d}\vec{p}}{h^{d}} \exp \left[ -\frac{\beta p^{2}}{2m} \right]
$$
- Where did this equation come from?
The probability to observe a certain norm of the velocity/momentum takes the form:
$$
P_{MB}(v=\lvert \vec{v} \rvert ) = K(d) v^{d-1} e^{ -m\beta v^{2}/2 }
$$
- How is this form determined? From the previous equation?
Where $K(d)$ is a constant proportional to the area of the unit sphere in $d$ dimensions. $P_{MB}$ is known as the Maxwell-Boltzmann distribution of velocities.

The momentum integral in $\mathcal{Z}_{1}$ is Gaussian, and therefore can be evaluated to be,
$$
\mathcal{Z}_{1} = \frac{V}{\lambda^{d}_{dB}} \qquad \lambda_{dB} = \frac{h}{\sqrt{ 2m\pi kT }}
$$
Where $\lambda_{dB}$ is called the thermal de Broglie wavelength, used to represent the typical quantum size of a particle's wavepacket. The partition function measures the number of distinct phase‑space regions accessible to one particle.

The condition for classical behaviour is
$$
V\gg N\lambda^{d_{dB}}
$$
Which tells us that the inter-particle spacing should be larger than the quantum wavelength.

The many-body partition function and the Helmholtz free energy is:
$$
\mathcal{Z}_{N} = \frac{1}{N!} \left( \frac{V}{\lambda^{d}_{dB}} \right)^{N} \qquad F=-kT\ln \mathcal{Z}_{N} = -NkT \left[ \ln\left( \frac{V}{N\lambda^{d}_{dB}} \right) -1 \right]
$$
# Ideal gas law
The pressure directly follows from the Helmholtz free energy
$$
P = - \frac{ \partial F }{ \partial V } = \frac{NkT}{V} \implies  PV=NkT
$$
Which is the familiar law of ideal gases.

Other forms of the equation include using the density $n=N /V$ or the molar concentration $n_\text{mole}=N /N_{A}$ as opposed to the number $N$. The other versions are:
$$
P=nRT \qquad PV=n_\text{mole}RT
$$
Where $R=kN_{A}$ is called the ideal gas constant.
# Other thermodynamic quantities
The internal energy is obtained from:
$$
E = -\frac{ \partial \ln \mathcal{Z}_{N} }{ \partial \beta } = \frac{d}{2} NkT
$$
Which tells us that the energy per particle is proportional to temperature, as we would expect.

The Sackur-Tetrode equation is:
$$
S = - \frac{ \partial F }{ \partial T } = Nk \left[ \ln\left( \frac{V}{N\lambda^{d}_{dB}} \right) - \frac{d+2}{2} \right]
$$
