- Midterm this week so this is just one lecture

Recall that the position of a damped driven mass and spring system is:
$$
\ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x = \omega_{0}^{2} A_{f} \cos(\omega t)
$$
The solution to this ODE is of course the sum of the homogeneous solution and a particular solution:
$$
x(t) = x_{h}(t) + x_{p}(t)
$$
The particular solution is:
$$
x_{p}(t) = A(\omega) \cos[\omega t-\delta(\omega)]
$$
Where,
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }} \qquad \delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
Where $0\leq\delta<\pi$ so that the system remains physical. From here, it is easy to show that the velocity is,
$$
v = V(\omega) \sin[\omega t-\delta(\omega)]
$$
Where $V(\omega)=-\omega A(\omega)$.
# Transient Response
The transient phase refers to the period of time in which multiple forms coexist. For this system, this is before the oscillations have times to establish.

Recall that the general case for the unforced damped oscillations were:
$$
x_{h}(t) = A_{h} e^{ -\gamma t } \cos(\omega_{d}t+\phi)
$$
Where $A_{h}$ and $\phi$ are constants determined by the initial conditions. Now, notice that in the driven version, the ODE contains no arbitrary constants.

So this portion of the solution is determined by the initial conditions, describing the transient behaviour.
![[Pasted image 20260205112540.png]]
The summation of the undriven (top) and driven (bottom) solutions to the inhomogeneous ODE reveals what the transient behaviour of the oscillator might look like.
# Power absorbed by damping during forced oscillations
The power provided by a force $\vec{F}$ on a particle travelling with velocity $\vec{v}$ is $\vec{F}\cdot \vec{v}$. Bringing in the frictional force we have,
$$
P = -F_\text{friction}v = bv^{2} = bV^{2}(\omega) \sin ^{2}(\omega t-\delta)
$$
Which varies over time. However, most of the time we are simply interested in the average power drain:
$$
\bar{P}(\omega) = \frac{1}{T} \int_{t_{0}}^{t_{0}+T} P(\omega, T) \, dt \qquad \text{where }T=\frac{2\pi}{\omega}
$$
$T$ is the period length, and so we are finding the average over one cycle.

Integrate to find,
$$
\int_{t_{0}}^{t_{0}+T} \sin ^{2}(\omega t-\delta) \, dt = \frac{T}{2}
$$
Therefore we have,
$$
\bar{P}(\omega) = bV^{2}(\omega) \left( \frac{T}{2} \right) = \frac{b\omega_{0}^{2}A_{f}^{2}}{2} \left[ \left( \frac{\omega_{0}}{\omega} - \frac{\omega}{\omega_{0}} \right)^{2} + \frac{4\gamma^{2}}{\omega_{0}^{2}} \right] ^{-1}
$$

- **Check if this equation is correct**
- **Missing notes here**

![[Pasted image 20260205114220.png]]
Plot of the power a a function of $\omega$. It looks symmetrical, but this is only true for small $\gamma$.

Note here that the full-width half-max of this curve is denoted $\omega _\text{fwhh}$, which is the "full-width half-height".

To determine an expression for $\omega _\text{fwhh}$, we make the approximation that $\omega \approx \omega_{0}$. From this we havev,
$$
\left( \frac{\omega_{0}}{\omega} - \frac{\omega}{\omega_{0}} \right)^{2} \approx \frac{(\omega_{0}^{2}-\omega^{2})^{2}}{(\omega \omega_{0})^{2}}
$$
And we can claim,
$$
\omega^{2}-\omega_{0}^{2} = (\omega-\omega_{0})(\omega+\omega_{0}) \approx 2\omega_{0}\Delta \omega
$$
Where we have defined $\Delta \omega=\omega-\omega_{0}$. Replacing the remaining instances of $\omega$ with $\omega_{0}$ we have,
$$
\bar{P}(\omega) = \frac{b\omega_{0}^{4}A_{f}^{2}}{8} \left[ (\Delta \omega)^{2}+\gamma^{2} \right] ^{-1} = \frac{\bar{P}_\text{max}}{1+(\Delta \omega /\gamma)^{2}}
$$
We solve for $\omega _\text{fwhh}$ by setting $\bar{P} /\bar{P}_\text{max} = 1 /2$, which yields,
$$
1 + \left( \frac{\Delta \omega}{\gamma} \right)^{2} \approx 2 \implies  \Delta \omega \approx \gamma
$$
By the definition of the full-width half-max we therefore have,
$$
\omega _\text{fwhh} = 2(\Delta \omega) \approx 2\gamma = \frac{2\omega_{0}}{Q}
$$
This tells us a few things
- As $\gamma$ decreases, the power resonance curve is narrower
- With a high $Q$ oscillator, it is easier to miss resonance
- Once resonance is attained, it dissipates a lot more power
![[Pasted image 20260205115155.png]]
A plot of the power as a function of $\omega /\omega_{0}$.

This yields yet another interpretation of the quality factor:
$$
Q = \frac{\omega_{0}}{\gamma} \approx \frac{2\omega_{0}}{\omega _\text{fwhh}} = 2 \times \frac{\text{Resonance frequency}}{\text{FWHM of power curve}}
$$
---
Example: Absorption lines

The spectral peak in the absorption spectrum of an atom occurs at wavelength 500 nm, with FWHM $1.2\times 10^{-5}$. Model the excited atom as a damped oscillator and deduce its lifetime.

Recall that the lifetime of a damped oscillator is $1 /\gamma$, and that $\omega=2\pi c /\lambda$.

We would like to solve for the lifetime with the identity: $\omega _\text{fwhh}=2\gamma$.

Begin by solving for the frequency from the wavelength,
$$
\Delta \omega = \frac{ \partial \omega }{ \partial \lambda } \Delta \lambda = -\frac{2\pi c}{\lambda^{2}} \Delta \lambda
$$
Taking the absolute value, this tells us
$$
\omega _\text{fwhh} = \frac{2\pi c}{\lambda^{2}} \lambda _\text{fwhh}
$$
The lifetime is therefore,
$$
\tau = \frac{1}{\gamma} = \frac{2}{\omega _\text{fwhh}} = \frac{\lambda_{0}^{2}}{\pi c\lambda _\text{fwhh}} \approx 2.7 \times 10^{-8} \text{ seconds}
$$
Which corresponds to a $Q$-factor of roughly 92 million. Explaining why atomic clocks are so accurate.

---
# More general forcing terms
## Superposition of sinusoids
What if we now supposed the driving force is:
$$
F(t) = F_{01} \cos(\omega_{1}t) + F_{02} \cos(\omega_{2}t) + \dots
$$
Curiously, using the principle of superposition, the solution to this is the superposition of the solutions for each of the sinusoids,
$$
\begin{align}
\ddot{x}_{1} + 2\gamma \dot{x}_{1} + \omega_{0}^{2} x_{1} & = \omega_{0}^{2} A_{f, 1} \cos(\omega_{1}t) \\
\ddot{x}_{2} + 2\gamma \dot{x}_{2} + \omega_{0}^{2} x_{2} & = \omega_{0}^{2} A_{f, 2} \cos(\omega_{2}t)
\end{align}
$$
- Remember to include the homogeneous solution too

The solution here will be exactly what we are used to:
$$
x_{p} = A_{f, 1} a(\omega_{1}) \cos[\omega_{1}t-\delta(\omega_{1})] + A_{f, 2} a(\omega_{2}) \cos[\omega_{2}t-\delta(\omega_{2})] + \dots
$$
With the resonance curves,
$$
a(\omega) = \frac{\omega_{0}^{2}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }} \qquad \delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
As per usual.

Something a bit more exotic than this might be a square wave, or a sawtooth wave. Well in this case we would need to apply Fourier's theorem, to decompose the periodic signal into a superposition of sines and cosines.
