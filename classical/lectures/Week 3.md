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
# Introduction to Damped Oscillators
Assume the mass feels some friction,
$$
F_\text{damping} = -bv=b\dot{x}
$$
Which as we can see is proportional to the velocity.
- We assume that the friction force scales linearly with velocity here. This is an approximation for slowly moving systems

Implementing the damping force, the new equation of motion is,
$$
m\ddot{x} = -kx - b\dot{x} \implies  \ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x=0
$$
Where we have defined,
$$
\gamma=\frac{b}{2m} \qquad  \omega_{0}^{2}=\frac{k}{m}
$$
Which are called the damping factor and natural angular frequency of the oscillator, respectively.

To solve this system, we will attempt the trial solution,
$$
x(t) = c e^{ rt }
$$
Plugging this in we obtain,
$$
(r^{2}+2\gamma r + \omega_{0}^{2}) x(t) =0 \implies  r^{2}+2\gamma r + \omega_{0}^{2} =0
$$
The solutions to this polynomial are,
$$
r = -\gamma \pm \sqrt{ \gamma^{2}-\omega_{0}^{2} }
$$
According to superposition the general solution is,
$$
x(t) = \mathrm{Re}\{ c_{+} e^{ r_{+}t } + c_{-} e^{ r_{-}t } \}
$$
- Note that the above expression breaks down when $\omega_{0}^{2}=\gamma^{2}$
- We can recover simple harmonic motion when $\gamma=0$

Substitute $r$ back into the full expression to find,
$$
x(t) = e^{ -\gamma t } \mathrm{Re}\{ \dots \}
$$
And so the magnitude of oscillation decays like $e^{ -\gamma t }$
- $\gamma ^{-1}$ is called the e-folding decay scale or decay time scale

There are three regimes of interest
1. $\gamma^{2}<\omega_{0}^{2}$: Underdamped or light-damping. The pendulum can still oscillate, but it is decaying
2. $\gamma^{2}>\omega_{0}^{2}$: Overdamped or heavy-damping. The pendulum cannot oscillate even once
3. $\gamma^{2}=\omega_{0}^{2}$: The solution to the ODE changes. This is called critical damping
# Light damping
Define the variables,
$$
\omega_{d}^{2} = \omega_{0}^{2}-\gamma^{2}>0 \qquad T_{d} = \frac{2\pi}{\omega_{d}}
$$
Which simplifies our previously defined variables to:
$$
r_{\pm} = -\gamma\pm i\omega_{d} \qquad x(t) = e^{ -\gamma t } (c_{+} e^{ i\omega_{d}t } + c_{-} e^{ -i\omega_{d}t })
$$
Since our signal must be real, we also have,
$$
c_{+} = c_{-}^* = c
$$
Solving this equation for some given initial position and velocity yields:
$$
x_{0} = c + c^* = 2 \mathrm{Re}\{ c \}
$$
$$
v_{0} = -2\omega_{d} \mathrm{Im}\{ c \} - \gamma x_{0}
$$
Combining the real and imaginary parts of $c$ we find,
$$
c = \frac{1}{2} \left( x_{0} - i \frac{\gamma x_{0}+v_{0}}{\omega_{d}} \right)
$$
![[Pasted image 20260122140532.png]]
An example of underdamped oscillatory motion.

Here we call the "period" the pseudo-period $T_{d}=2\pi /\omega_{d}$ because the decay term breaks the perfect periodicity.
# Logarithmic decrement
Define,
$$
A_{0} = 2 \lvert c e^{ (i\omega_{d}-\gamma)t } \rvert _{t=0} = 2\lvert c \rvert
$$
Which we call the initial position amplitude. Now, notice that we may define two points separated by one pseudo-period liek so:
$$
A_{n} = A_{0} e^{ -\gamma nT_{d} } \qquad A_{n+t} = A_{0} e^{ -\gamma(n+1)T_{d} }
$$
The logarithmic ratio of the two is called the logarithmic decrement
$$
\frac{A_{n}}{A_{n+1}} = e^{ \gamma T_{d} } \implies  \ln\left( \frac{A_{n}}{A_{n+1}} \right) = \gamma T_{d}
$$
Which determine by how quickly the solution decays or decrements.
# Quality factor of an oscillator
Measures the decay between oscillations. Serves a similar purpose as the logarithmic decrement, but it can also be expanded to overdamped oscillators. It is roughly defined by the ratio,
$$
Q = \frac{\text{tendency to oscillate}}{\text{tendency to damp}}
$$
In the lightly damped oscillator, when $\gamma\ll \omega_{0}$ this is typically approximated to be,
$$
Q = \frac{\omega_{0}}{\gamma}
$$
- Note that there is no rigorous definition for the $Q$ factor

The pseudo-angular frequency can be written in terms of the $Q$ factor like,
$$
\omega_{d}^{2} = \omega_{0}^{2} \left( 1-\frac{1}{Q^{2}} \right)
$$
You can also think of the $Q$ factor as the number of cycles an oscillator can achieve within one duration $\tau=\gamma ^{-1}$. If the number of natural cycles during $\tau$ is $n=\tau /T_{0}$ then,
$$
Q = 2\pi n
$$
Which is valid because $T_{0}\approx T_{d}$

When an oscillator is lightly damped, the logarithmic decrement and the $Q$ factor quantify the same thing. Assuming $\omega_{0}\approx \omega_{d}$ we have,
$$
\gamma T_{d} \approx \gamma T_{0} = \frac{2\pi \gamma}{\omega_{0}} = \frac{2\pi}{Q}
$$
# Heavy damping
Recall that heavily damped oscillators do not even oscillate.

Define the new variable,
$$
\alpha = \sqrt{ \gamma^{2}-\omega_{0}^{2} } \implies r_{\pm} = -\gamma\pm \alpha
$$
Reducing the general solution to,
$$
x(t) = c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha) }t
$$
Which is a superposition of two real-valued, decaying exponentials.

Curiously, the coefficients $c_{\pm}$ are the same as in the underdamped case with $i\omega_{d}$ replaced with $\alpha$
$$
c_{\pm} = \frac{1}{2} \left( x_{0} \pm \frac{v_{0}+\gamma x_{0}}{\alpha} \right)
$$
![[Pasted image 20260122142303.png]]
An example of an overdamped oscillator.
