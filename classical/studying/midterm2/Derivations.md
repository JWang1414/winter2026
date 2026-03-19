# Lecture 8
## General solution for a damped and driven oscillator
Beginning with the equation,
$$
\ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x = \omega_{0}^{2} A_{f} \cos(\omega t)
$$
Move to the complex space,
$$
\ddot{z} + 2\gamma \dot{z}+\omega_{0}^{2}z = \omega_{0}^{2}A_{f} e^{ i\omega t }
$$
Now, adopt an exponential $z=Ze^{ i\omega t }$
$$
(-\omega^{2}+ 2i\omega\gamma + \omega_{0}^{2}) Z = \omega_{0}^{2}A_{f}
$$
Therefore,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{2i\omega\gamma+\omega_{0}^{2}-\omega^{2}}
$$
Now, the amplitude of $Z$ is $A(\omega)$, and the phase difference between the driving and the response is $\delta(\omega)$. This gives us $Z=A(\omega)e^{ -i\delta(\omega) }$.

The amplitude is the norm of $Z$,
$$
\lvert Z \rvert = \left| \frac{\omega_{0}^{2}A_{f}}{\omega_{0}^{2}-\omega^{2}+2i\omega\gamma} \right| = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }}
$$
- During this calculation it helps to define $p=\omega_{0}^{2}-\omega^{2}$ and $q=2\gamma \omega$

Now, keep in mind that,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{p+iq} \qquad A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ p^{2}+q^{2} }}
$$
Since, by definition $Z=A(\omega)e^{ ii\delta(\omega) }$ we therefore also have,
$$
e^{ -i\delta } = \frac{Z}{A(\omega)} = \frac{\sqrt{ p^{2}+q^{2} }}{p+iq} \frac{p-iq}{p-iq} = \frac{p-iq}{\sqrt{ p^{2}+q^{2} }}
$$
According to Euler's identity $e^{ -i\delta }=\cos\delta-i\sin\delta$,
$$
\cos\delta = \frac{p}{\sqrt{ p^{2}+q^{2} }} \qquad \sin\delta = \frac{q}{\sqrt{ p^{2}+q^{2} }}
$$
Which nicely simplifies when we solve for the tangent function,
$$
\tan\delta = \frac{\sin\delta}{\cos\delta} = \frac{q}{p} = \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}}
$$
$$
\delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
## Varying the forcing frequency
When $\omega\ll \omega_{0}$ or $\omega\to 0$ we have,
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }} \to  A_{f}
$$
$$
\delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right) \to  \arctan(0) =0
$$
When $\omega\gg \omega_{0}$ or $\omega\to \infty$ we have,
$$
A(\omega) \to 0
$$
Graphically, you will find that:
$$
\tan\delta \approx \frac{2\gamma}{-\omega} \to  0 \implies  \lim_{ \omega \to \infty } \delta=\pi
$$
Which arises because $0<\delta<2\pi$

When $\omega=\omega_{0}$ we have,
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{2\gamma \omega} = \frac{QA_{f}}{2}
$$
And $\delta=\pi /2$ here by definition.

To find where the maxima for $A(\omega)$ is, we will analyze the denominator. Since the numerator is constant. Our goal is therefore to find when it is at a minimum.
$$
\frac{d}{d\omega} ((\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2}) = 4\omega(2\gamma^{2}-(\omega_{0}^{2}-\omega^{2}))
$$
To avoid the trivial case, we require that,
$$
\omega^{2}=\omega_{0}^{2}-2\gamma^{2}=\omega_{0}^{2}\left( 1-\frac{2}{Q^{2}} \right)
$$
Which is where the maximum amplitude occurs. You will find that,
$$
A_\text{max} = \frac{Q}{2\sqrt{ 1-1 /Q^{2} }}A_{f}
$$
However, for all practical purposes we have $\omega _\text{max}\approx \omega_{0}$ and so,
$$
A_\text{max} \approx \frac{QA_{f}}{2}
$$
In the case that $Q\to \infty$ we have $\omega _\text{max}\to \omega_{0}$ and if you plug this into $A(\omega)$ you get back that,
$$
A_\text{max} = \frac{QA_{f}}{2}
$$
# Lecture 9
The velocity of a damped, driven oscillator is,
$$
V(\omega) = \frac{\omega_{0}A_{f}}{\sqrt{ \left( \frac{\omega_{0}}{\omega} - \frac{\omega}{\omega_{0}} \right)^{2}+\frac{4\gamma^{2}}{\omega_{0}^{2}} }}
$$
Which has peaks at $\omega=\omega_{0}$, the resonance frequency.

The power absorbed by damping during oscillations is,
$$
P = -F_\text{friction}v = bv^{2}=bV^{2}(\omega) \sin ^{2}(\omega t-\delta)
$$
We are more interested in the time average for this quantity,
$$
\int_{t_{0}}^{t_{0}+T} \sin ^{2}(\omega t-\delta) \, dt = \frac{1}{\omega} \int_{\omega t_{0}}^{\omega t_{0}+2\pi} \sin ^{2}(y-\delta) \, dy =\frac{\pi}{\omega} = \frac{T}{2}
$$
The average is defined to be,
$$
\bar{P}(\omega) = \frac{1}{T} \int_{t_{0}}^{t_{0}+T} P(\omega, t) \, dt
$$
And therefore the average for the above is simply 1/2. Now, substituting in $V(\omega)$ into the equation for the power and we get,
$$
\bar{P}(\omega) = \frac{b\omega_{0}^{2}A_{f}^{2}}{2} \left[ \left( \frac{\omega_{0}}{\omega}-\frac{\omega}{\omega_{0}} \right)^{2}+\frac{4\gamma^{2}}{\omega_{0}^{2}} \right]^{-1}
$$
Note that around the maximum power, the variations in $\bar{P}$ originate from the term in the denominator. To simplify this, we make a few approximations:
$$
\left( \frac{\omega_{0}}{\omega}-\frac{\omega}{\omega_{0}} \right)^{2} = \frac{(\omega_{0}^{2}-\omega^{2})^{2}}{(\omega \omega_{0})^{2}}
$$
For small deviations in $\omega$ we have approximately,
$$
\frac{(\omega_{0}^{2}-\omega^{2})^{2}}{\omega_{0}^{4}}
$$
Furthermore,
$$
\omega^{2}-\omega_{0}^{2} = (\omega-\omega_{0})(\omega+\omega_{0}) \approx 2\omega_{0}\Delta \omega
$$
This results in,
$$
\left( \frac{\omega_{0}}{\omega}-\frac{\omega}{\omega_{0}} \right)^{2} = \frac{(2\omega_{0}\Delta \omega)^{2}}{\omega_{0}^{4}} = \frac{(2\Delta \omega)^{2}}{\omega_{0}^{2}}
$$
So,
$$
\bar{P}(\omega) = \frac{b\omega_{0}^{4}A_{f}^{2}}{8} \frac{1}{(\Delta \omega)^{2}+\gamma^{2}} = \frac{\bar{P}_\text{max}}{1+(\Delta \omega /\gamma)^{2}}
$$
Now, to find the full-width half-height we solve for when,
$$
\frac{\bar{P}}{\bar{P}_\text{max}} = \frac{1}{2} \implies  1+\left( \frac{\Delta \omega}{\gamma} \right)^{2}=2 \implies  \Delta \omega \approx \gamma
$$
This is the half-width, the full-width will be,
$$
\omega _\text{fwhh} = 2(\Delta \omega) \approx 2\gamma = \frac{2\omega_{0}}{Q}
$$
# Lecture 12
In general, if energy is conserved we have,
$$
E=a \dot{q}^{2}+bq^{2}
$$
Where $E$ is constant. Since we know that the solution will be simple harmonic motion, take the derivative to obtain,
$$
\dot{E} = 2a \dot{q} \ddot{q} + 2bq \dot{q} = 2\left( \ddot{q} + \frac{b}{a} q \right)a \dot{q} =0
$$
From which we have that,
$$
\ddot{q} =-\frac{b}{a}q
$$
Which is the equation for SHM with natural angular frequency $\sqrt{ b /a }$.

To approximate small amplitude oscillations around an equilibrium, we first need to Taylor expand our potential to the second order. Once we have done so, we can simply use the equation,
$$
\omega^{2} = \frac{U_{0}''(x_{0})}{m}
$$
Where $U_{0}$ is the potential.