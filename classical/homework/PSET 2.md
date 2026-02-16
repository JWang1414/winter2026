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
From lecture, the motion of a heavily damped oscillator is governed by:
$$
x(t) = c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha)t }
$$
With the coefficients:
$$
c_{\pm} = \frac{1}{2} \left( x_{0} \pm \frac{v_{0} + \gamma x_{0}}{\alpha} \right)
$$
For the oscillator to avoid crossing the origin,
$$
x(t) = c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha)t } > 0
$$
For $t>0$. Notably, the behaviour of $x(t)$ is dominated by the first term, so the problem is reduced to:
$$
c_{+} e^{ -(\gamma-\alpha)t }  > 0 \implies  c_{+} > 0
$$
Which arises because the exponential is always positive. Now, solve for $v_{0}$,
$$
\begin{align}
\frac{1}{2} \left( x_{0} + \frac{v_{0}+\gamma x_{0}}{\alpha} \right) & >0 \\
\alpha x_{0} + v_{0} + \gamma x_{0} & > 0 \\
x_{0}(\alpha+\gamma) & > -v_{0}
\end{align}
$$
The negative sign is a result of the velocity being directed towards the origin. Substituting in the fact that $\alpha=\sqrt{ \gamma^{2}-\omega_{0}^{2} }$:
$$
v_{0}^{\text{max}} = x_{0}\left( \gamma + \sqrt{ \gamma^{2}-\omega_{0}^{2} } \right)
$$
---
c.
Potential energy from a spring is,
$$
\frac{1}{2} k(\Delta x)^{2}
$$
Maximum velocity occurs when this is fully converted to kinetic energy:
$$
\frac{1}{2} mv^{2} = \frac{1}{2}k(\Delta x)^{2} \implies  v^{2} = \frac{k}{m} (\Delta x)^{2}
$$
Which yields a max velocity:
$$
v_\text{max}^{(1)} = \omega_{0} x_{0}
$$
According to lecture, the velocity of a critically damped mass is:
$$
v(t) = (B-\gamma A - \gamma Bt) e^{ -\gamma t }
$$
So the velocity is:
$$
\frac{dv}{dt} = a(t) = \gamma e^{ -\gamma t } (\gamma A + \gamma Bt - 2B)
$$
This function has one root at:
$$
\gamma A + \gamma Bt - 2B =0 \implies  t = \frac{2B - \gamma A}{\gamma B}
$$
Substitute this in to find the maximum velocity,
$$
v(t) = \left( B-\gamma A - \gamma B \left( \frac{2B - \gamma A}{\gamma B} \right) \right)  e^{ -\gamma \left( \frac{2B - \gamma A}{\gamma B} \right)  } = -B \exp \left\{  \frac{\gamma A}{B} -2  \right\}
$$
According to lecture, $A$ and $B$ with respect to the initial conditions are:
$$
A = x_{0} \qquad B = v_{0}+\gamma x_{0} = \gamma x_{0}
$$
The final result is therefore:
$$
v_\text{max}^{(2)} = -\frac{\gamma x_{0}}{e} = - \frac{\omega_{0}x_{0}}{e}
$$
Adjusting for the direction, this satisfies:
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
# Question 2
---
a.
The equation of motion for this system according to Newton's 2nd law is:
$$
m\ddot{x} = -k[x-\xi(t)] - b \frac{d}{dt}[x-\xi(t)]
$$
Define $y=x-\xi(t)$ to simplify this to,
$$
m\ddot{x} = -ky - b\dot{y} \implies  \ddot{x} + 2\gamma \dot{y} + \omega_{0}^{2}y =0
$$
Where I have used,
$$
\omega_{0}^{2} = \frac{k}{m} \qquad \gamma = \frac{b}{2m}
$$
Now, solve for $\ddot{x}$.
$$
\begin{align}
y & = x-\xi \\
x & = y+\xi \\
\ddot{x} & = \ddot{y} + \ddot{\xi} = \ddot{y} - \omega^{2}A_{f} \cos(\omega t)
\end{align}
$$
Substitute this back in to find,
$$
\ddot{y} + 2\gamma \dot{y} + \omega_{0}^{2}y = \omega^{2} A_{f} \cos(\omega t)
$$
As needed.

---
b.
The complex variation for the equation of motion is:
$$
\ddot{y} + 2\gamma \dot{y} + \omega_{0}^{2}y = \omega^{2} A_{f} e^{ i\omega t }
$$
Adapting the method from lecture and adopting an exponential $\beta e^{ rt }$ the amplitude is:
$$
\beta = \frac{\omega^{2}A_{f}}{\omega_{0}^{2} - \omega^{2} + 2i\gamma \omega}
$$
Based on the definition of $x=y+\xi$ it should have the complex amplitude:
$$
\beta + A_{f} = \frac{\omega^{2}A_{f}}{\omega_{0}^{2} - \omega^{2} + 2i\gamma \omega} + A_{f} = \left( \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \right) A_{f}
$$
The real amplitude for $x$ will therefore be:
$$
A(\omega) = \left| \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \right| A_{f}
$$
I will compute this norm separately so that it is easier to read.
$$
\begin{align}
\left| \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \right| & = \sqrt{ \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \frac{\omega_{0}^{2}  - 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} - 2i\gamma \omega} } \\
 & = \sqrt{ \frac{\omega_{0}^{4} + 4\gamma^{2}\omega^{2}}{(\omega_{0}^{2}-\omega^{2}) + 4\gamma^{2}\omega^{2}} } \\
 & = \sqrt{ \frac{\omega_{0}^{4} + 4\gamma^{2}\omega^{2}}{\omega_{0}^{4} + 4\gamma^{2}\omega^{2} + \omega^{4} - 2\omega_{0}^{2}\omega^{2}} }
\end{align}
$$
Divide the numerator and denominator by $\omega_{0}^{4}+4\gamma^{2}\omega^{2}$,
$$
\left| \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \right| = \sqrt{ \frac{1}{1 + \frac{(\omega^{2}-2\omega_{0}^{2})\omega^{2}}{\omega_{0}^{4} + 4\gamma^{2}\omega^{2}}} } = \frac{1}{\sqrt{ 1 + \frac{(\omega^{2}-2\omega_{0}^{2})\omega^{2}}{\omega_{0}^{4} + 4\gamma^{2}\omega^{2}} }}
$$
So,
$$
A(\omega) = \left| \frac{\omega_{0}^{2}  + 2i\gamma \omega}{\omega_{0}^{2}-\omega^{2} + 2i\gamma \omega} \right| A_{f} = \frac{A_{f}}{\sqrt{ 1 + \frac{(\omega^{2}-2\omega_{0}^{2})\omega^{2}}{\omega_{0}^{4} + 4\gamma^{2}\omega^{2}} }} = \frac{A_{f}}{\sqrt{ 1+C(\omega) }}
$$
As needed.

---
c.
In order to decrease $A(\omega)$, we would like to have $C(\omega)\to \infty$ so that $A(\omega)\to 0$. Notice that $C(\omega)\propto 1 /\gamma^{2}$ and so $C(\omega)\to \infty$ implies $\gamma\to 0$.

However, at resonance $\omega=\omega_{0}$,
$$
C(\omega_{0}) = \frac{(\omega_{0}^{2} - 2\omega_{0}^{2})\omega_{0}^{2}}{\omega_{0}^{4} + 4\omega_{0}^{2}\gamma^{2}} = -\frac{\omega_{0}^{4}}{\omega_{0}^{4} + 4\omega_{0}^{2}\gamma^{2}}
$$
In this case $\gamma\to 0$ results in:
$$
C(\omega_{0}) = -\frac{\omega_{0}^{4}}{\omega_{0}^{4}} =-1 \implies  A(\omega_{0}) = \frac{A_{f}}{\sqrt{ 1-1 }} \to \infty
$$
Based on this analysis I conclude that the dashpot acts as an amplifier when the vibrations are off resonance, and a dampener on resonance. The dashpot should therefore be tuned so that is has a small value, so it cannot amplify vibrations off resonance, but large enough so that vibrations cannot blow up at resonance.