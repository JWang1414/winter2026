# Question 1
---
a.
Equalize gravity and friction:
$$
cv^{2} = mg \implies  v^{2} = \frac{mg}{c}
$$
And therefore the terminal velocity must be:
$$
v_\text{ter} = \sqrt{ \frac{mg}{c} }
$$
---
b.
During the upward journey, drag and gravity point in the same direction:
$$
m\ddot{x} = mg + cv^{2} \implies  \dot{v} = g + \frac{cv^{2}}{m}
$$
Note that:
$$
\left( \frac{v}{v_\text{ter}} \right)^{2} = \left( v\sqrt{ \frac{c}{mg} } \right)^{2} = \frac{cv^{2}}{mg}
$$
And therefore the magnitude of acceleration can be expressed as:
$$
\dot{v} = g + g \left( \frac{v}{v_\text{ter}} \right)^{2} = g \left[ 1 + \left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Adapt this quantity to the coordinate system where $g$ is negative to obtain:
$$
\dot{v} = -g \left[ 1+ \left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
As needed.

---
c.
First, re-arrange the equation to find:
$$
\frac{dv}{dt} \left[ 1 + \left( \frac{v}{v_\text{ter}} \right)^{2} \right] ^{-1} =-g
$$
Integrate both sides, using substitution on the left-hand side:
$$
\int_{v_{0}}^{v} \left[ 1 + \left( \frac{v}{v_\text{ter}} \right)^{2} \right] ^{-1} \, dv = -g \int dt
$$
The result is:
$$
v_\text{ter} \arctan\left( \frac{v}{v_\text{ter}} \right) - v_\text{ter} \arctan\left( \frac{v_{0}}{v_\text{ter}} \right) = -gt
$$
Which can be re-arranged to find:
$$
v(t) = v_\text{ter}\tan\left( \arctan\left( \frac{v_{0}}{v_\text{ter}} \right) - \frac{gt}{v_\text{ter}} \right)
$$
To solve for $v(y)$, begin by using the chain rule on the original expression:
$$
\frac{dv}{dt} = \frac{dv}{dy} \frac{dy}{dt} = \frac{dv}{dy} v = -g \left[ 1 + \left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Integrate both sides:
$$
\int_{v_{0}}^{v} \frac{v}{1 + (v /v_\text{ter})^{2}} \, dv =-g \int dy
$$
The result is:
$$
\frac{v_\text{ter}^{2}}{2} \left[ \ln(v_\text{ter}^{2}+v^{2}) - \ln(v_\text{ter}^{2}+v_{0}^{2}) \right] = -gy
$$
Which can be re-arranged to:
$$
v^{2}(y) = \exp \left[ \ln(v_\text{ter}^{2}+v_{0}^{2})-\frac{2gy}{v_\text{ter}^{2}} \right] - v_\text{ter}^{2}
$$
Or equivalently:
$$
v(y) = \sqrt{ \exp \left[ \ln(v_\text{ter}^{2}+v_{0}^{2})-\frac{2gy}{v_\text{ter}^{2}} \right] - v_\text{ter}^{2} }
$$
Solving for $y(v)$ instead yields:
$$
y(v) = -\frac{v_\text{ter}^{2}}{2g} \left[ \ln(v_\text{ter}^{2}+v^{2}) - \ln(v_\text{ter}^{2}+v_{0}^{2}) \right]
$$
Or equivalently:
$$
y(v) = \frac{v_\text{ter}^{2}}{2g} \ln\left( \frac{v_\text{ter}^{2}+v_{0}^{2}}{v_\text{ter}^{2}+v^{2}} \right)
$$
---
d.
The baseball will reach maximum height when $v=0$. According to $y(v)$ this is:
$$
y(v) = \frac{v_\text{ter}^{2}}{2g} \ln\left( \frac{v_\text{ter}^{2}+v_{0}^{2}}{v_\text{ter}^{2}} \right)
$$
As needed.

---
e.
Drag and gravity now point in opposite directions
$$
m\ddot{x} = mg - cv^{2}
$$
Re-arrange to find an expression for $\dot{v}$:
$$
\dot{v} = g\left( 1 - \left( \frac{v}{v_\text{ter}} \right)^{2} \right)
$$
Align the direction so that $g$ is negative:
$$
\dot{v} = -g \left[ 1-\left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Apply the chain rule:
$$
\frac{dv}{dt} = \frac{dv}{dy} \frac{dy}{dt} = v \frac{dv}{dy} = -g \left[ 1-\left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Integrate both sides:
$$
\int_{v_{0}}^{v} \frac{v}{1-(v /v_\text{ter})^{2}} \, dv = -g \int dy
$$
The result is:
$$
-\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = -gy
$$
After some algebra:
$$
\ln \left| v_\text{ter}^{2}-v^{2} \right| = \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|
$$
Simplify the absolute value by making the assumption that $v^{2}\leq v_\text{ter}^{2}$:
$$
v^{2} - v_\text{ter}^{2} = \exp \left[ \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right| \right]
$$
Solve for $v$:
$$
v(y) = \sqrt{ v_\text{ter}^{2} + \exp \left[ \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right| \right] }
$$
---
f.
Instead of using the final equation, I will instead substitute $y_\text{max}$ into this midpoint:
$$
\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = gy
$$
Which yields:
$$
\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = -\frac{v_\text{ter}^{2}}{2} \ln\left( \frac{v_\text{ter}^{2}+v_{0}^{2}}{v_\text{ter}^{2}} \right)
$$
Apply the properties of logarithms to simplify the expression into:
$$
\ln\left( \frac{\left| v_\text{ter}^{2}-v^{2} \right| }{\left| v_\text{ter}^{2}-v_{0}^{2} \right| } \right) = \ln \left( \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}} \right)
$$
If I assume that $v_{0}<v_\text{ter}$ and $v<v_\text{ter}$ I obtain:
$$
\frac{v^{2}-v_\text{ter}^{2}}{v_{0}^{2}-v_\text{ter}^{2}} = \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
Re-arrange:
$$
v^{2} = \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}} (v_{0}^{2}-v_\text{ter}^{2}) + v_\text{ter}^{2} = \frac{2v_\text{ter}^{2}v_{0}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
Aligning the directions, the velocity when the ball hits the ground is,
$$
v_{g} = - \frac{\sqrt{ 2 }v_\text{ter}^{2}v_{0}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
- This is a factor $\sqrt{ 2 }$ off the correct answer. Not sure why
# Question 2
---
a.
- Done in Python
---
b.
Forward Euler has linear error
- Well, I already knew this
# Question 3
In polar coordinates, Newton's 2nd law states:
$$
\begin{align}
F_{r} & = m (\ddot{r} - r \dot{\theta}^{2}) \\
F_{\theta} & = m (2\dot{r} \dot{\theta} + r \ddot{\theta})
\end{align}
$$
For this problem:
$$
\begin{align}
0 & = m (\ddot{r} - r \dot{\theta}^{2}) \\
3m \dot{r} \dot{\theta} & = m (2\dot{r} \dot{\theta} + r \ddot{\theta})
\end{align}
$$
Simplify,
$$
\begin{align}
\ddot{r} & = r \dot{\theta}^{2} \\
\dot{r} \dot{\theta} & = r \ddot{\theta}
\end{align}
$$
According to the 2nd equation,
$$
\frac{\dot{r}}{r} = \frac{\ddot{\theta}}{\dot{\theta}} = \frac{\dot{\omega}}{\omega}
$$
Where $\omega=\dot{\theta}$. Integrate both sides:
$$
\frac{1}{r} \frac{dr}{dt} = \frac{1}{\omega} \frac{d\omega}{dt} \implies  \int_{r_{0}}^{r} \frac{1}{r} \, dr = \int_{\omega_{0}}^{\omega} \frac{1}{\omega} \, d\omega
$$
The result is:
$$
\ln\left( \frac{r}{r_{0}} \right) = \ln\left( \frac{\omega}{\omega_{0}} \right) \implies  \frac{r}{r_{0}} = \frac{\omega}{\omega_{0}}
$$
Solve for $\omega$:
$$
\dot{\theta} = \omega = \frac{\omega_{0}}{r_{0}} r
$$
According to the first equation
$$
\ddot{r} = \frac{dv}{dt} = \frac{dv}{dr} \frac{dr}{dt} = v \frac{dv}{dr} = r \dot{\theta}^{2} = r \left( \frac{\omega_{0}}{r_{0}}r \right)^{2} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{3}
$$
Where $v$ is the radial velocity. The above yields the ODE:
$$
v \frac{dv}{dr} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{3}
$$
Solve using separation of variables by integrating both sides,
$$
\int_{v_{0}}^{v} v \, dv = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} \int_{r_{0}}^{r} r^{3} \, dr \implies  v^{2} - v_{0}^{2} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} (r^{4}-r_{0}^{4})
$$
Re-arrange,
$$
v = \dot{r} = \pm\sqrt{ \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{4} - \omega_{0}^{2}r_{0}^{2} + v_{0}^{2} } = \pm \sqrt{ Ar^{4} + B }
$$
Where,
$$
A = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} \qquad B = v_{0}^{2} - \omega_{0}^{2} r_{0}^{2}
$$
As needed.

Furthermore, by definition, we have,
$$
\dot{r} = \frac{dr}{dt}
$$
Using separation of variables, and integrating both sides,
$$
\int_{t_{0}}^{t} dt = \int_{r_{0}}^{r} \frac{dr'}{\dot{r}'}
$$
We are interested in the limit where $r\to \infty$ so this becomes,
$$
\Delta t = \int_{r_{0}}^{\infty} \frac{dr}{\dot{r}} = \int_{r_{0}}^{\infty}  \left[ \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{4} - \omega_{0}^{2}r_{0}^{2} + v_{0}^{2} \right]^{-1/2}  \, dr
$$
Where I have chosen the positive branch of $\dot{r}$ since we assume $\dot{r}>0$, and denoted $\Delta t=t-t_{0}$. In the limit where $r\to \infty$ the expression within the integral is approximately equal to,
$$
\left[ \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{4} - \omega_{0}^{2}r_{0}^{2} + v_{0}^{2} \right]^{-1/2} \approx \left[ \left( \frac{\omega_{0}}{r_{0}} \right)^{2}r^{4} \right] ^{-1/2} = \frac{r_{0}}{\omega_{0}} \frac{1}{r^{2}}
$$
Since $B=v_{0}^{2}-\omega_{0}^{2}r_{0}^{2}$ is just a constant. Therefore, the amount of time taken to reach $r\to \infty$ is:
$$
\Delta t \approx \frac{r_{0}}{\omega_{0}} \int_{r_{0}}^{\infty} \frac{1}{r^{2}} \, dr = \frac{1}{\omega_{0}}
$$
And therefore the amount of time $\Delta t$ to reach $r\to \infty$ is finite, as needed.
# Question 4
---
a.
Recall from lecture that for two commensurate frequencies, if,
$$
r = \frac{\omega_{1}}{\omega_{2}} = \frac{m}{n}
$$
And $m /n$ has been reduced to the lowest terms, the superposed signal has period,
$$
mT_{1} = nT_{2}
$$
For this signal,
$$
\omega_{1} = \frac{25}{4} \qquad \omega_{2} = 7
$$
Therefore,
$$
r = \frac{25}{28} = \frac{m}{n}
$$
And the period is:
$$
nT_{2} = 28 \left( \frac{2\pi}{7} \right) = 8\pi
$$
---
b.
The velocity of the two vibrations are:
$$
v_{1} = 3 \frac{d}{dt} \cos\left( \frac{25}{4}t + \frac{\pi}{5} \right) = -\frac{75}{4} \sin\left( \frac{25}{4}t+\frac{\pi}{5} \right)
$$
$$
v_{2} = 4 \frac{d}{dt} \cos \left( 7t + \frac{\pi}{8} \right) = -28 \sin\left( 7t + \frac{\pi}{8} \right)
$$
- The rest is done in Python
---
c.
Recall the identities:
$$
\sin x = \frac{e^{ ix } - e^{ -ix }}{2i} \qquad \cos x = \frac{e^{ ix }+e^{ -ix }}{2}
$$
Express $z$ in complex exponential form:
$$
z = \frac{5}{2i} (e^{ i\omega t } - e^{ -i\omega t }) + \frac{6}{2} (e^{ i\omega t } + e^{ -i\omega t })
$$
Re-arrange and isolate the two exponentials:
$$
z = \left( 3-\frac{5i}{2} \right) e^{ i\omega t } + \left( 3+\frac{5i}{2} \right) e^{ -i\omega t }
$$
Notice that this is a complex term and its complex conjugate. Recall that:
$$
\alpha e^{ i\omega t } + \alpha ^* e^{ -i\omega t } = \mathrm{Re} \{ 2\alpha e^{ i\omega t } \}
$$
And so the above is equivalent to:
$$
z = \left( 3-\frac{5i}{2} \right) e^{ i\omega t } + \left( 3+\frac{5i}{2} \right) e^{ -i\omega t } = \mathrm{Re}\left\{  2\left( 3-\frac{5i}{2} \right) e^{ i\omega t }  \right\}
$$
I conclude:
$$
A = 2\left( 3-\frac{5i}{2} \right) \qquad \phi=0
$$
