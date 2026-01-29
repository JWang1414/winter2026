Recall that the undamped driven oscillator is modeled by the ODE:
$$
\ddot{z} + \omega_{0}^{2}z = \omega m_{0}^{2}A_{f} e^{ i\omega t }
$$
Where $z\in \mathbb{C}$.
# General solution for a damped and driven oscillator
$$
\ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x = \omega_{0}^{2} A_{F} \cos(\omega t)
$$
Where the damping has manifested as an extra $2\gamma \dot{x}$ term on the left-hand side.

Equivalently, in complex form,
$$
\ddot{z} + 2\gamma \dot{z} + \omega_{0}^{2}z = \omega_{0}^{2} A_{f} e^{ i\omega t }
$$
Adopting the exponential $z=Ze^{ rt }$ as a trial function we find,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{\omega_{0}^{2}-\omega^{2}+2i\gamma \omega}
$$
Use this value of $Z=A(\omega)e^{ i\delta }$ to determine the real amplitude $A(\omega)$
$$
\lvert Z \rvert =A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }}
$$
- Note that the denominator is strictly positive, and so the amplitude never diverges

To solve for the phase, it will be helpful to define the variables:
$$
p=\omega_{0}^{2}-\omega^{2} \qquad q=2\gamma \omega
$$
Now, decompose $Z /A(\omega)$ into real and imaginary parts,
$$
\frac{Z}{A(\omega)} = e^{ -i\delta } = \cos\delta - i \sin\delta = \frac{p}{\sqrt{ p^{2}+q^{2} }} - i \frac{q}{\sqrt{ p^{2}+q^{2} }}
$$
So we havem
$$
\cos\delta = \frac{p}{\sqrt{ p^{2}+q^{2} }}\qquad \sin\delta = \frac{q}{\sqrt{ p^{2}+q^{2} }}
$$
The phase is most simply expressed as:
$$
\tan\delta = \frac{\sin\delta}{\cos\delta} =\frac{q}{p} \implies  \delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
- Note defined when $\omega_{0}^{2}=\omega^{2}$. In this case, fall back to the original sine and cosine formulae
# Varying the forcing frequency
![[Pasted image 20260129114028.png]]
Plots of the amplitude and phase as a function of $\omega /\omega_{0}$ in the damped, driven case.
## Limiting behaviours
At very low frequency $\omega\ll \omega_{0}$
$$
\lim_{ \omega \to 0 } A = A_{f}
$$
$$
\lim_{ \omega \to 0 } \delta = \arctan(0) =0
$$
And it reduces to the undamped case.

At high frequency $\omega\gg \omega_{0}$
$$
A \approx \frac{\omega_{0}^{2}A_{f}}{\sqrt{ \omega^{4}+4\gamma^{2}\omega^{2} }} \approx \frac{\omega_{0}^{2}A_{f}}{\omega^{2}} \to  0
$$
$$
\tan\delta = \frac{2\gamma}{(-\omega)} \to  0
$$
Therefore we have $A=0$ and $\delta=\pi$, same as the undamped case.

At resonance $\omega=\omega_{0}$
$$
A = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ 4\gamma^{2}\omega_{0}^{2} }} = \frac{QA_{f}}{2}\text{ and } \delta=\frac{\pi}{2}
$$
Where we have used the quality factor $Q=\omega_{0} /\gamma$
# Maxima of the curves and resonance location
Note that the numerator of $A(\omega)$ is constant, and so to maximize $A(\omega)$ we are interested in minimizing the denominator.
$$
\frac{d}{d\omega} (4\gamma^{2}\omega^{2} + (\omega_{0}^{2}-\omega^{2}))^{2} = 4\omega (2\gamma^{2}-(\omega_{0}^{2}-\omega^{2}))
$$
- **Complete later**
