# Question 1
---
ai.
![[Pasted image 20260211163249.png]]

Define the displacement from equilibrium (in the spring) as $\Delta x$. Then,
$$
k\Delta x = m_{2}g
$$
Expressing $\Delta x$ in terms of $L$ and $d$,
$$
k(L-d) = m_{2}g \implies  k = \frac{m_{2}g}{L-d}
$$
---
aii.
Assuming there is no effect from damping, the amplitude of the oscillations must be,
$$
\Delta x = L-d
$$
And the period of the oscillations will be,
$$
T = \frac{2\pi}{\omega} = 2\pi \sqrt{ \frac{m_{1}}{k} } = 2\pi \sqrt{ \frac{m_{1}(L-d)}{m_{2}g} }
$$
---
b.
- Solve this question later

General solution,
$$
x(t) = c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha)t }
$$
Solve for $t$ when $x(t)=0$
$$
c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha)t } =0
$$
$$
c_{+} e^{ 2\alpha t } + c_{-} =0
$$
$$
2\alpha t  = \ln\left( -\frac{c_{-}}{c_{+}} \right)
$$
$$
t = \frac{1}{2\alpha} \ln\left( -\frac{c_{-}}{c_{+}} \right)
$$
Velocity,
$$
v(t) = -c_{+} (\gamma-\alpha) e^{ -(\gamma-\alpha)t } - c_{-} (\gamma+\alpha) e^{ -(\gamma+\alpha)t }
$$
$$
-2\alpha c_{-} \left( -\frac{c_{-}}{c_{+}} \right)^{-(\gamma+\alpha)/2\alpha} \leq 0
$$
$$
c_{-} =0 \implies  \frac{1}{2} \left( x_{0} - \frac{v_{0}+\gamma x_{0}}{\alpha} \right) =0
$$
$$
x_{0} - \frac{v_{0}+\gamma x_{0}}{\alpha} =0 \implies  \alpha x_{0} - v_{0}-\gamma x_{0} =0
$$
$$
x_{0}(\alpha-\gamma) = v_{0}
$$
---
c.
Potential energy from a spring is,
$$
\frac{1}{2} k(\Delta x)^{2}
$$
Convert to velocity to find,
$$
\frac{1}{2} mv^{2} = \frac{1}{2}k(\Delta x)^{2} \implies  v^{2} = \frac{k}{m} (\Delta x)^{2}
$$
$$
v = \omega x_{0}
$$
For a critically damped mass,
$$
v(t) = (B-\gamma A - \gamma Bt) e^{ -\gamma t }
$$
$$
a(t) = \gamma e^{ -\gamma t } (\gamma A + \gamma Bt - 2B)
$$
Has roots at,
$$
t = \frac{2B - \gamma A}{\gamma B}
$$
Max velocity is,
$$
-B e^{ (\gamma A/B) -2 }
$$
$$
A = x_{0} \qquad B = v_{0}+\gamma x_{0} = \gamma x_{0}
$$
$$
-\frac{\gamma x_{0}}{e} = - \frac{\omega_{0}x_{0}}{e}
$$
Which satisfies,
$$
v^{(1)}_\text{max} = e v_\text{max}^{(2)}
$$
As needed.
# Question 3
---
a.
- Everything is done in in the code here
- I did a sanity check with just the first coefficient and it looks alright
---
b.
- This one appears to be running the same file numerous times

The case with $\omega_{0}\ll 1$, in my case $\omega_{0}=0.1$ has changed it so that the oscillator barely sees any oscillation. Physically,
$$
\omega_{0} = \sqrt{ \frac{k}{m} } \ll  1 \implies  m\gg k
$$
Which implies that the spring is unable to move a mass this heavy, and so it stays put. The case with $w_{0}\gg 1$ is the opposite, $k\gg m$ and so the spring has no trouble getting the mass to move. In fact in this case we have,
$$
Q = \frac{\omega_{0}}{\gamma} \implies  \gamma = \frac{\omega_{0}}{Q} = 1
$$
Therefore, $\omega_{0}>\gamma$ and the system is clearly an under-damped oscillator.

As the quality factor decreases, I notice that the amplitude of the oscillations gradually decreases. Physically, the smaller Q-factor corresponds to more damping in the system, so the mass is unlikely to accelerate drastically from the forcing.

In particular, $Q=1$ implies $\omega_{0}=\gamma$ and so the oscillator is critically damped. From the position of the max $x(t)$, it is possible to see the mass quickly approaching $x=0$ before slowing down. Of course, the mass cannot settle due to the driving force, and it jerks away from the origin quickly because of it.

The period in all cases appears to be the same or very similar. So the period of oscillation is very strongly influenced and controlled by the driving force.
