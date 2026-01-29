Last time, we discussed under and over-damped harmonic oscillators.
# Critical damping
In this case, the general solution to the ODE equation modelling SHM reduces to
$$
x(t) = (c_{+} + c_{-}) e^{ -\gamma t }
$$
Assuming $c$ is constant, then the velocity is,
$$
v(t) = -\gamma x(t)
$$
Which, for $x_{0}\neq 0$ and $v_{0}=0$, is actually an overconstrained problem, with exclusively trivial solutions.

In fact, the general solution here is actually:
$$
x(t) = (A+Bt) e^{ -\gamma t }
$$
Where $A,B\in \mathbb{R}$. The velocity becomes,
$$
v(t) = (B-\gamma A-\gamma Bt) e^{ -\gamma t }
$$
![[Pasted image 20260128095433.png]]
A plot of the "oscillation" of a critically damped oscillator.

The decay here is actually quicker than in the overdamped case. In a critically damped oscillator, $\gamma=\omega_{0}$ is the rate of decay.
- Recall that $\omega_{0}^{2}=\gamma^{2}$ for the critically damped oscillator
![[Pasted image 20260128100845.png]]
A comparison of all the cases

In way to understand critical damping is that it is the quickest to return to equilibrium without overshooting.

![[Pasted image 20260128101137.png]]
Here is the phase plot of all the cases
- Origin is the attractor
- None of the motions are periodic, because they never loop back onto themselves

---
Example:
Define $m=2.5$ and $k=600$

To find when the damping is critical, we require:
$$
\gamma=\omega_{0} = \sqrt{ \frac{k}{m} } \approx 15.5
$$
$$
b=2m\gamma = 77.5
$$
Assume a critically damped mass:
$$
x(t) = (A+Bt) e^{ -\gamma t }
$$
At rest such that $x(0)=0$
$$
x(t) = A=0 \implies  x(t) = Bte^{ -\gamma t }
$$
Use the initial velocity to solve for $B$
$$
v(t) = B(1-\gamma t) e^{ -\gamma t } \implies  v(0) = v_{0}=B
$$
We obtain the system of equations:
$$
\begin{align}
x(t) & = v_{0}te^{ -\gamma t } \\
v(t) & = v_{0}(1-\gamma t) e^{ -\gamma t }
\end{align}
$$
Maximum displacement will occur when,
$$
v(t)=0 \implies  t=\gamma ^{-1}
$$
Substitute into $x(t)$ to find the maximum displacement:
$$
x(\gamma ^{-1}) = \frac{v_{0}}{\gamma} e^{ ^{-1} } \approx 3.6 \text{cm}
$$
---
# Driving an undamped harmonic oscillator
For the purposes of this class, the forcing will be sinusoidal, with a well defined frequency.

Imagine a mass attached to a spring, but this time, the system is combined with an oscillating engine instead of a fixed wall. The frequency of the engine's oscillation is $\omega$, called the driving frequency.

Call the position of the engine
$$
\xi = A_{f} \cos(\omega t)
$$
The phase will be defined with reference to the driving, and so the phase of the driving force is always 0. The force of the spring on the mass is,
$$
F = -k[x-\xi(t)]
$$
Now, according to Newton's 2nd law,
$$
m\ddot{x} = -k[x-A_{f} \cos(\omega t)] \implies  \ddot{x}+\omega_{0}^{2}x = \omega_{0}^{2} A_{f} \cos(\omega t)
$$
Where $\omega_{0}^{2}=k /m$.

Since this is inhomogeneous, the solution is the sum of a particular solution with the solution to the homogeneous equation. That solution to the homogeneous version is, of course, SHM.

We solve this problem by swapping into complex space,
$$
\ddot{z} + \omega_{0}^{2}z = \omega_{0}^{2} A_{f} e^{ i\omega t }
$$
Adopt the exponential $z=Ze^{ rt }$ to find,
$$
(r^{2}+\omega_{0}^{2}) Ze^{ rt } = \omega_{0}^{2}A_{f} e^{ i\omega t }
$$
Valid solutions exist only for $r=i\omega$, which tells us that the response of an oscillator to a driving at frequency $\omega$ is an oscillation at the same frequency $\omega$.
$$
Z = \frac{\omega_{0}^{2}A_{f}}{\omega_{0}^{2}-\omega^{2}}
$$
By observation, the amplitude of oscillation will depend on the frequency of forcing.

To determine the phase of oscillation, we consider the polar representation of $Z$
$$
Z(\omega) = A(\omega) e^{ -i\delta }
$$
Since $A(\omega)$ must be real and positive, this is necessarily
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\left| \omega_{0}^{2}-\omega^{2} \right| } \qquad e^{ -i\delta } = \text{sign}(\omega_{0}^{2}-\omega^{2})
$$
In the case $\omega<\omega_{0}$ we have $\delta=0$. The response is therefore,
$$
x(t) = \mathrm{Re}\{ Z \} = A(\omega) \cos(\omega t)
$$
In the limit where $\omega /\omega_{0}\to 0$ we have,
$$
\delta=0 \qquad A /A_{f} \to  1
$$
Physically, this means that when the engine moves very slowly, the spring neither compresses nor stretches.

In the case $\omega>\omega_{0}$ we have $\text{sign}(\omega_{0}^{2}-\omega^{2})=e^{ -i\delta }=-1$ and so $\delta=\pi$. The response is therefore,
$$
x(t) = \mathrm{Re}\{ Z \} = A(\omega)\cos(\omega t-\pi)
$$
And so the engine and mass oscillate at the same frequency, but with opposite phase.

In the limit where $\omega /\omega_{0}\to \infty$ we have $A /A_{f} =0$ so the mass hardly moves in this case.

The case where $\omega=\omega_{0}$ is called resonance. In this case we have $A(\omega)\to \infty$ and so the amplitude endlessly increases to infinity
- Imagine this as the driving force repeatedly supplying energy to the system
- The solution to the ODE changes, but we aren't required to know it
![[Pasted image 20260128130945.png]]
Here is a plot of the amplitude of the mass oscillating with a resonant driving force
# General solution for a damped and driven oscillator
Recall that the undamped driven oscillator is given by the ODE:
$$
\ddot{z} + \omega_{0}^{2}z = \omega m_{0}^{2}A_{f} e^{ i\omega t }
$$
Where $z\in \mathbb{C}$.
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
## Position
Note that the numerator of $A(\omega)$ is constant, and so to maximize $A(\omega)$ we are interested in minimizing the denominator.
$$
\frac{d}{d\omega} (4\gamma^{2}\omega^{2} + (\omega_{0}^{2}-\omega^{2}))^{2} = 4\omega (2\gamma^{2}-(\omega_{0}^{2}-\omega^{2}))
$$
Which is minimized under the condition,
$$
\omega^{2} = \omega_{0}^{2} - 2\gamma^{2} = \omega_{0}^{2} \left( 1-\frac{2}{Q^{2}} \right)
$$
Substitute in this value of $\omega$ to find the maximum amplitude:
$$
A_\text{max} = \frac{Q}{2\sqrt{ 1-1 /Q^{2} }} A_{f}
$$
In the limit where there is no damping, $Q\to \infty$, $\omega _\text{max}\to \omega_{0}$ and $A_\text{max}\to QA_{f} /2$, but otherwise, $\omega _\text{max}<\omega_{0}$.

For most practical purposes, when $Q$ is a reasonable value,
$$
\omega _\text{max} \approx \omega_{0} \qquad A_\text{max} \approx \frac{QA_{f}}{2}
$$
## Velocity
Recall that for,
$$
x = A(\omega) \cos[\omega t-\delta(\omega)]
$$
We have,
$$
v = V(\omega) \cos\left[ \omega t-\delta(\omega) + \frac{\pi}{2} \right]
$$
Where we have defined $V(\omega)=\omega A(\omega)$ as the velocity amplitude.
$$
V(\omega) = \omega_{0}A_{f} \left[ \left( \frac{\omega_{0}}{\omega} - \frac{\omega}{\omega_{0}} \right)^{2} + \frac{4\gamma^{2}}{\omega_{0}^{2}} \right] ^{-1/2}
$$
By observation, one can see:
- $V(\omega)\to 0$ at low frequency
- $V_\text{max}$ occurs at $\omega=\omega_{0}$
- A phase shift by $\pi /2$ means the new phase lag between forcing and velocity response is $\delta-\pi /2$. So, at resonance, velocity and forcing are exactly in phase
# Varying the damping
For the purposes of this simulation, the $Q$-factor will be varied as opposed to the damping factor. However, this is effectively the same thing.
![[Pasted image 20260129174907.png]]
Plots of the amplitude and phase lag as a function of $\omega /\omega_{0}$ while $Q$ is varied.

Notice that the maximum amplitude can be predicted by a divergent line going along the $y$-axis.
