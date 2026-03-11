In this lecture we will develop the transition between simple oscillators and wave behaviour.
# Two Pendulums and a Spring
Two identical masses $m$ hang from two identical pendulums of length $l$. The two masses are connected with a spring of stiffness $k$.
![[Pasted image 20260311100528.png]]
$A$ is the mass on the right, and $B$ is the mass on the left. $x$ will notate the horizontal distances from rest.
## Symmetric Normal Mode
If both masses are initially held still with $x_{A}=x_{B}=C$, then once released both will oscillate at the same natural frequency $\omega_{p}=\sqrt{ g /l }$.

Their oscillation will be in perfect synchronous fashion such that,
$$
x_{A}(t) = x_{B}(t) = C \cos(\omega_{1}t)
$$
And the spring plays no role in the motion. This is called a normal mode, when all elements of the coupled system oscillate at the same frequency.
## Antisymmetric Normal Mode
Alternatively, we might also have initial conditions $x_{A}=-x_{B}=C$, again with no initial velocity. In this case the positions will oscillate perfectly out of phase, with a single angular frequency $\omega_{2}$.

There is no third normal mode, because there are only two degrees of freedom in the system.
# General Derivation
The horizontal angle of the pendulum when $\theta \neq 0$ is $x_{A}=l\sin\theta \approx l\theta$.

The force of tension in the $y$ direction, opposing the force of gravity is,
$$
T_{y} = \lvert \vec{T} \rvert  \cos\theta \approx \lvert \vec{T} \rvert
$$
And the vertical position is,
$$
y = l(1-\cos\theta) \approx \frac{l\theta^{2}}{2}
$$
The vertical acceleration in the $y$ direction is negligible, because we are assuming that the angles are small, so $y$ changes very slowly in comparison to $T$ and $mg$.

We therefore make the approximation,
$$
T_{y} - mg \approx 0 \implies  \lvert \vec{T} \rvert \approx mg
$$
The horizontal projection of the tension is therefore,
$$
-\lvert \vec{T} \rvert \sin\theta \approx -\frac{mgx_{A}}{l}
$$
And the spring force is,
$$
-k(x_{A}-x_{B})
$$
Newton's 2nd law therefore tells us,
$$
m\ddot{x}_{A} = -\frac{mg}{l}x_{A} - k(x_{A}-x_{B})
$$
Which yields the differential equation,
$$
\ddot{x}_{A} + \omega^{2}_{p} x_{A} + \omega_{s}^{2}(x_{A} - x_{B}) =0
$$
Where we have used,
$$
\omega_{p} = \sqrt{ \frac{g}{l} } \qquad \omega_{s} = \sqrt{ \frac{k}{m} }
$$
Which are the natural angular frequencies of the pendulum and the mass A + spring systems, respectively.

By symmetry, we also have that,
$$
\ddot{x}_{B} + \omega^{2}_{p} x_{B} + \omega_{s}^{2}(x_{B} - x_{A}) =0
$$
# Change of variables
This system of coupled ODEs can be solved with the change of variables,
$$
q_{1}=x_{A}+x_{B} \qquad q_{1}=x_{A}-x_{B}
$$
Add and subtract the two coupled ODEs to obtain,
$$
\ddot{q}_{1} + \omega_{p}^{2}q_{1}=0 \qquad \ddot{q}_{2} + (\omega_{p}^{2}+2\omega_{s}^{2})q_{2}=0
$$
In fact, these two quantities correspond to the symmetric and anti-symmetric modes that we found prior.
$$
\omega_{1}=\omega_{p}\qquad \omega_{2}^{2} = \omega_{p}^{2}+2\omega_{s}^{2}
$$
- The modes of oscillation in such a system are no longer simple oscillations. They are a global concept in which all component of one coupled system oscillate in phase, at the same frequency
- The oscillations of each individual component are not independent from each other, but the modes are completely independent. $q_{1}$ doesn't appear in the equation for $q_{2}$, and vice versa.
	- Therefore, in the full system, there are just two modes. They do not exchange momentum so long as the system is linear
- $q_{n}$ are the normal coordinates/modes with respective normal frequencies $\omega_{n}$.
# Independence of the Modes
The two modes are both solutions to difference SHO equations with the expressions,
$$
q_{1}=C_{1} \cos(\omega_{1}t+\phi_{1}) \qquad q_{2}=C_{2} \cos(\omega_{2}t+\phi_{2})
$$
Which in physical coordinates is,
$$
x_{A} = \frac{q_{1}+q_{2}}{2} \qquad x_{B} = \frac{q_{1}-q_{2}}{2}
$$
So any motion is a linear superposition of the two modes.
## Energetic independence of the modes
The kinetic energy, and potential energy from gravity are,
$$
K_{A, B} = \frac{1}{2} m (\dot{x}_{A, B})^{2} \qquad U^{(g)}_{A, B} = \frac{1}{2} m\omega_{p}^{2} x_{A, B}^{2}
$$
And the energy stored in the spring is,
$$
U^{(s)} = \frac{1}{2} k(x_{A} - x_{B})^{2} = \frac{1}{2} m\omega^{2}_{s} (x_{A} - x_{B})^{2}
$$
So the total energy in the system is,
$$
E = K_{A, B} + U^{(g)}_{A, B} + U^{(s)} = E_{1}+E_{2}
$$
Where the subscript $A, B$ terms represent the sum of the energy in $A$ and $B$.

The representations for $E_{1}$ and $E_{2}$ are,
$$
E_{n} = \frac{1}{4} m\left[ \dot{q}_{n}^{2} + \omega_{n}^{2}q_{n}^{2} \right]
$$
Notice that each reservoir of energy $E_{n}$ is uncoupled from each other, and so there is no exchange of energy from one mode of motion to the other. This is true for any system of coupled oscillators, as long as the linear model is valid.
# Beating Phenomenon
When $\omega_{1}\approx \omega_{2}$, we observe beating in the physical space for each mass position.

If we choose the initial conditions $C_{1}=C_{2}=C$ and $\phi_{1}=\phi_{2}=0$ we obtain the configuration,
$$
x_{A} = C \cos(\Omega t) \cos(\Delta \omega t) \qquad x_{B} = C \sin(\Omega t) \sin(\Delta \omega t)
$$
Where,
$$
\Delta \omega = \frac{1}{2} (\omega_{2}-\omega_{1}) \qquad \Omega = \frac{1}{2} (\omega_{1}+\omega_{2})
$$
If $\lvert \Delta \omega \rvert\ll \Omega$ then we observe:
![[Pasted image 20260311110125.png]]
Notice the characteristic beating in the oscillation amplitude of $x_{A}$.
