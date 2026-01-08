- Gain medium
	- We need a proper gain medium
	- Cannot be anything, mediums with too much absorption do not work
# Oscillating Dipole Moment
Often times we will express oscillating movement with the familiar equation
$$
\frac{d^{2}x}{dt^{2}} + \omega_{0}^{2}x=0
$$
Generally speaking, inside a gain medium we can use the dipole approximation. The monopole is non-existent, because we have a neutral medium, and quadrupoles are driven with $\nabla E$. Which, for $\lambda\gg a_{0}$ is incredibly weak. ($\lambda$ is the optical wavelength and $a_{0}$ is the atomic electron cloud)
- This arises in particular because the size of the electron cloud is so small in comparison to the wavelength. In this case the oscillating electric field has nearly no chance to change
# Radiative damping
$$
\text{Radiative power} = \frac{1}{4\pi\epsilon_{0}} \frac{2}{3c^{2}} \lvert \ddot{\mathbf{d}} \rvert ^{2}
$$
Where $\mathbf{d}$ is the dipole moment. Furthermore we also have,
$$
\vec{d} = e\vec{x} = e\left( \vec{x}_{0} \cos(\omega_{0}t) + \frac{\vec{v}_{0}}{\omega_{0}} \sin(\omega_{0}t) \right)
$$
However, from the oscillating motion equation we know that,
$$
\ddot{\mathbf{d}} = -\omega_{0}^{2} \mathbf{d}
$$
So,
$$
\text{Radiated power} = \frac{1}{4\pi\epsilon_{0}} \omega_{0}^{4} \frac{2}{3c^{2}} \lvert \mathbf{d} \rvert ^{2}
$$
Based on our equation for the dipole moment, we can see that the radiated power is oscillating. Now, if we take the time average of the radiated power we have,
$$
\omega_{0}^{4} \overline{\lvert \mathbf{d} \rvert }^{2} = \left( \frac{e^{2}x_{0}^{2}}{2} + \frac{v_{0}^{2}e^{2}}{2\omega_{0}^{2}} \right) \omega_{0}^{4} = e^{2} \omega_{0}^{2} \left( \frac{1}{2} \omega_{0}^{2} x_{0}^{2} + \frac{1}{2} v_{0}^{2} \right)
$$
This term in brackets is energy/m or W. Generally speaking, as power radiated from a system, the energy is decreasing, so we can therefore conclude,
$$
\frac{dw}{dt} = -Aw \qquad \text{where } A = \frac{1}{4\pi\epsilon_{0}} \frac{2}{3c^{2}} \frac{e^{2}\omega_{0}^{2}}{m}
$$
$A$ has just been pulled out from the equations and divided by $m$ to account for the units.
- Note that the inherent assumption that $-dw /dt=\text{Radiated power}$ uses the version of the oscillatory equation without the damping term. And so this is an approximate, perturbation solution
# Quantum Corrections
Instead of the Newtonian driving harmonic oscillator:
$$
\frac{d^{2}}{dt^{2}} \vec{x} + \omega_{0}^{2} \vec{x} = \frac{e}{m}\vec{E}
$$
We instead have,
$$
\frac{d^{2}}{dt^{2}} \left< \vec{x} \right> + \omega_{0}^{2} \left< \vec{x} \right>  = \frac{2e\omega}{\hbar} \vec{x}_{12} (\vec{x}_{12} \cdot \vec{E})
$$
We have used the notation,
$$
\vec{x}_{12} = \bra{2} \vec{x} \ket{1}
$$
Experimentally, there is a disagree between between the results and the values predicted by Lorentz' classical model. This can be explained by the quantum mechanical element:
$$
f = \frac{2m\omega_{0}}{\hbar} x_{12}^{2}
$$
Which we call the *oscillator strength*. For the quantum harmonic well, this element becomes,
$$
x^{2}_{12} = \bra{1} \hat{x} \ket{0}
$$
The terms in this cancel out the other parts of $f$ and it becomes 1. However, in general, this is not true.

Now that we have this perturbatory correction to our term, we can insert it into our previous solution and claim,
$$
A = \frac{f}{4\pi\epsilon_{0}} \frac{2}{3c^{2}} \frac{e^{2}\omega_{0}^{2}}{m}
$$
