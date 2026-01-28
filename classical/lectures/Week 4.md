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