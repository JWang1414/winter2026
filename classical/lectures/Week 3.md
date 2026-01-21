# Simple harmonic oscillators
A system where a restoring force (a force that always tries to bring back (restore) the system to its equilibrium) is the only one to balance inertia

Consider this spring-mass system:
![[Pasted image 20260121095801.png]]
Where this is an ideal spring of stiffness $k>0$, with an object of mass $m$ attached to it.

Pull the mass away from equilibrium, and the applied force from the spring is governed by Hooke's law,
$$
F = -kx_{0}
$$
The negative sign here indicates that it is a *restoring force*. According to Newton's 2nd law,
$$
ma = m\ddot{x} = -kx
$$
Rearrange to find,
$$
\ddot{x} + \omega_{0}^{2}x=0 \qquad \omega_{0}^{2} = \frac{k}{m}
$$
Which is the same simple harmonic oscillating system we solved previously.
# General Solutions
The general solutions to
$$
\ddot{x}+\omega_{0}^{2}x=0
$$
Look something like,
$$
A \cos(\omega_{0}t+\phi) \qquad B\sin(\omega_{0}t+\psi) \qquad C\cos(\omega_{0}t) + D \sin(\omega_{0}t)
$$
$$
Ee^{ i\omega_{0}t } + E^* e^{ -i\omega_{0}t } \qquad \mathrm{Re}\{ G e^{ i\omega_{0}t } \}
$$
Of course, because we have a 2nd order ODE, there are always two free parameters. Physically, this means our solution is determined entirely by $x_{0}$ and $v_{0}$. This type of motion is called *simple harmonic motion* (SHM)
# "Adopt an Exponential"
A simple strategy used to help determine what the solution to an ODE might look like. We'll use the SHO equation as an example.

Use this function $x(t)$ as the test function.
$$
x(t) = c e^{ rt } \qquad c, r \in \mathbb{C}
$$
- $x$ can be complex right now, for physically realistic solutions, we need to verify if it is once we are done

Plug in $x(t)$ into our ODE to find,
$$
(r^{2}+\omega_{0}^{2})x(t)=0
$$
Which implies $x(t)=0$ or $r^{2}=-\omega_{0}^{2}$. Avoiding the trivial solution,
$$
r^{2}=-\omega_{0}^{2} \implies  r=\pm i\omega_{0}
$$
Which tell us that there are two linearly independent solutions that satisfy this equation. Use superposition to combine these:
$$
x(t) = c_{1} e^{ i\omega_{0}t } + c_{2} e^{ -i\omega_{0}t }
$$
In order for $x$ to be real, we require that $c_{2}=c_{1}^*$.
# Phase space representation of an oscillation
A plot of velocity or momentum versus position, parameterized by time.
![[Pasted image 20260121102949.png]]
Here is an example with simple harmonic motion.

What can we learn from this plot? Well,
- Points of extrema are located when $x=0$ or $v=0$
- It proceeds clockwise, the negative direction. Tells us that $v$ precedes $x$ in phase. That is, when $v$ is at its minimal value, $x$ will be at its minimum one-quarter cycle later
# The pendulum
Consider a mass $m$ at the end of a pendulum of length $\mathscr{l}$. Assume small angles.
![[Pasted image 20260121104011.png]]
Recalling from the first lecture that azimuthal acceleration is,
$$
2\dot{r} \dot{\theta} + r \ddot{\theta}
$$
And since $r=\mathscr{l}$, $\dot{r}=\ddot{r}=0$ for this pendulum,
$$
a_{\theta} = \mathscr{l}\ddot{\theta}
$$
Now, the mass $m$ is subject to the tension $\vec{T}$ from the pendulum, and its weight $-mg\vec{z}$. In polar coordinates, the force from gravity becomes,
$$
F_{\theta} = -mg\sin\theta
$$
Combine the two expressions according to Newton's 2nd law,
$$
F_{\theta} = ma_{\theta} \implies \ddot{\theta} = -\frac{g}{\mathscr{l}} \sin\theta
$$
Which is a non-linear 2nd order homogeneous ODE. It is non-linear because of the $\sin\theta$ term.

Note:
- In general, non-linear ODEs do not follow superposition, but linear ODEs always do

Instead of solving this analytically, we will use the small small angle approximation to linearize this equation.
$$
\ddot{\theta} + \frac{g}{\mathscr{l}} \theta =0
$$
Which is the same ODE that we solved prior. Solutions are of the same force,
$$
\theta(t) = \theta_{0} \cos (\omega_{0}t) + \frac{\dot{\theta}_{0}}{\omega_{0}} \sin(\omega_{0}t)
$$
