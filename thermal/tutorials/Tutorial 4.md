We begin by considering the partition function for a single atom of mass $m$ vibrating with frequency $\omega$.

Recall that the partition function in the canonical ensemble is,
$$
\mathcal{Z} = \sum_{i} e^{ -\beta E_{i} }
$$
Where we have $\beta=1 /kT$.

Under the continuum limit,
$$
\sum_{i} \to  \int \frac{dq dp}{h}
$$
Where $h$ is Planck's constant. 

The Hamiltonian, or total energy in this oscillator is,
$$
H = T+V = \frac{p^{2}}{2m} + \frac{1}{2} m\omega^{2}q^{2}
$$
Substitute this into the energy of the partition function, and take the integral to find,
$$
\mathcal{Z} = \int \exp \left[ -\beta \left( \frac{p^{2}}{2m} + \frac{m\omega^{2}q^{2}}{2} \right) \right]  \, \frac{dpdq}{h}
$$
The result from this integral is,
$$
\mathcal{Z} = \frac{2\pi kT}{h\omega}
$$
Now lets expand this analysis to 3-D. Where the Hamiltonian becomes:
$$
H = T+V = \frac{\vec{p}^{2}}{2m} + \frac{1}{2} m\omega^{2}\vec{q}^{2}
$$
Repeating the same steps, we find that,
$$
\mathcal{Z}^{\text{3D}} = \left( \frac{2\pi kT}{h\omega} \right)^{3}
$$
For $N$ particles, the partition function is simply the product of the single particle function
$$
\mathcal{Z}^\text{3D}_{N} = (\mathcal{Z}^\text{3D}) = \left( \frac{2\pi kT}{h\omega} \right)^{3N}
$$
Inside of an ideal gas, we include an extra counting factor,
$$
\mathcal{Z}_{N} = \frac{1}{N!} \mathcal{Z}^{N}
$$
Which arises because the particles inside an ideal gas are indistinguishable from each other. However, inside the crystal lattice we are working with, everything is countable and so we drop this factor.

---

The average energy for the whole crystal is,
$$
\left< E \right> = - \frac{ \partial \ln \mathcal{Z}_{N} }{ \partial \beta } = -\frac{ \partial  }{ \partial \beta } \ln \left[ \left( \frac{2\pi}{\beta n\omega} \right) ^{3N} \right]
$$
Which is equal to,
$$
\left< E \right> = 3NkT
$$
The number of atoms in our solid is,
$$
N = nN_{A}
$$
Where $n$ is the number of moles and $N_{A}$ is Avagadro's number. Work this out, and substitute in the ideal gas constant to obtain,
$$
\left< E \right> = 3nN_{A}kT = \frac{\left< E \right> }{n} = 3N_{A}kT = 3RT
$$
Which is the molar energy $e$ inside the solid. The molar specific heat is,
$$
c_{v} = \frac{ \partial e }{ \partial T } = 3R
$$
As needed.

---

Assume that each bound atom inside our solid is bound in 6 directions, 2 binds in each dimension. So, we have 3 translational, and 3 vibrational degrees of freedom. 6 DOF in total.

Equipartition theorem predicts a molar energy of $fRT$ and $fR /2$ molar specific heat. With $f=6$, you see that this agrees with our previous results.

---

Assume that the microstates have energy $e_{n}=\hbar \omega n$

The 1-D partition function is,
$$
\mathcal{Z}_{1} = \sum_{i} e^{ -\beta E_{i} } = \sum_{n=0}^{\infty} e^{ -\beta \hbar \omega n } = \frac{1}{1-e^{ -i\beta \hbar \omega }}
$$
Where we have expressed the summation as a geometric series

We expect the quantum result to reduce to the classical version under some limits. For example, in the high $T$ limit,
$$
\beta \hbar \omega = \frac{\hbar \omega}{kT} \to  0
$$
Use the Taylor series on the partition function we just found,
$$
\mathcal{Z}_{1} \approx \frac{1}{1-(1-\beta \hbar \omega)} = \frac{kT}{\hbar \omega} = \frac{2\pi kT}{h\omega}
$$
Which is the same result we found earlier

Recall that for $N$ particles in 3-D, the partition function becomes,
$$
\mathcal{Z}_{1}^{3N}
$$
Now lets compute $c_{v}$
$$
e = -3N_{A} \frac{ \partial  }{ \partial \beta } \ln(\mathcal{Z}) = -3N_{A} \frac{\hbar \omega}{e^{ \beta \hbar \omega } -1}
$$
$$
c_{v} = \frac{ \partial e }{ \partial T } = 3R \frac{\chi^{2}}{\sinh \chi^{2}}
$$
Where we have defined $\chi=\beta \hbar \omega /2$
- Note that this result is identical to what we got before, but with an extra factor with $\chi$ and $\sinh$ at the end. This is the model breaking down.