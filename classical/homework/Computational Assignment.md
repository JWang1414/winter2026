# Question 1
## Simulations
Applying the simplifications present in the setup, the equation of motion becomes,
$$
\ddot{\theta} = \sin\theta
$$
Defining a new variable $\phi=\dot{\theta}$ linearizes this into a set of two coupled ODEs:
$$
\dot{\theta}=\phi \qquad \dot{\phi} = \sin\theta
$$
Furthermore according to lecture, the kinetic and potential energy in the pendulum are:
$$
K = \frac{1}{2} mv_{\theta}^{2} = \frac{1}{2} m(l\dot{\theta})^{2} \qquad U = mgh = mgl(1-\cos\theta)
$$
The total energy in the system being the sum of these two terms.
## Observations
For the Euler-Cromer method, the energy oscillates. It increases and decreases over time. So, although it fluctuates, it is approximately constant overall.

The forward Euler method, however, constantly increases in energy over time. As time goes on, more energy is put into the system. For smaller time steps, the energy in the system increases slower.

These changes in the energy for the forward Euler method manifest as an increasing amplitude in the oscillation of the pendulum. As $t\to \infty$, one can expect the amplitude to diverge to infinity.

The Euler-Cromer method, however, stays stable over time. That is, the amplitude of the oscillations while using the Euler-Cromer integration method stays constant over time.
# Question 2
---
a.
Set $F=0$ to find,
$$
\frac{F}{m} =-\beta x-\alpha x^{3} \implies  -\beta x-\alpha x^{3}=0
$$
Therefore,
$$
-x(\beta+\alpha x^{2})=0
$$
Which is true when $x=0$ or:
$$
\begin{align}
\beta+\alpha x^{2} & =0 \\
\beta & =-\alpha x^{2} \\
x^{2} & =-\frac{\beta}{\alpha}
\end{align}
$$
So the fixed points of the system occur when,
$$
x=\pm i\sqrt{ \frac{\beta}{\alpha} }
$$
- I feel like this is wrong but I'm not really sure what this question is asking
---
b.
Given conditions:
$$
\alpha=1 \qquad \beta=-1 \qquad \gamma=0.08 \qquad x_{0}=2.0 \qquad \dot{x}_{0}=0
$$
Define the new variable
$$
y=\dot{x}
$$
The provided equation becomes:
$$
\dot{y}=-\gamma \dot{x} + \frac{F}{m} = - \gamma y + \frac{F}{m} = - \gamma y-\beta x-\alpha x^{3}
$$
The attractors appear to occur at $x=\pm 1$  and $\dot{x}=0$. There is another solution at $x=0$, $\dot{x}=0$, but it is unstable.

Including the new driving force results in,
$$
\ddot{x} + \gamma \dot{x} + \beta x+\alpha x^{3} = A_{d} \cos(\omega_{d}t)
$$
Therefore,
$$
\ddot{x} = -\gamma y - \beta x-\alpha x^{3} + A_{d} \cos(\phi)
$$
