# Question 1
---
a.
The drag force and gravity must be equal so:
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
---
c.
First, re-arrange the equation to find:
$$
\frac{dv}{dt} \left[ 1 + \left( \frac{v}{v_\text{ter}} \right)^{2} \right] ^{-1} =-g
$$
Use substitution and integrate both sides:
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
The baseball will reach maximum height when $y=0$. According to $y(v)$ this is:
$$
y(v) = \frac{v_\text{ter}^{2}}{2g} \ln\left( \frac{v_\text{ter}^{2}+v_{0}^{2}}{v_\text{ter}^{2}} \right)
$$
As needed.

---
e.
Downwards, gravity and drag point in the opposite directions:
$$
m\ddot{x} = mg-cv^{2}
$$

$$
\dot{v} = g - \frac{cv^{2}}{m} = g\left[ 1 - \left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
$$
\frac{dv}{dy} v = g\left[ 1 - \left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
$$
\int_{v_{0}}^{v} \frac{v}{1 - (v /v_\text{ter})^{2}} \, dv = g \int dy
$$
$$
-\frac{v_\text{ter}^{2}}{2} \left[ \ln(v_\text{ter}^{2}-v^{2}) + \ln(v_\text{ter}^{2}-v_{0}^{2}) \right] = gy
$$
$$
\ln(v_\text{ter}^{2}-v^{2}) + \ln(v_\text{ter}^{2}-v_{0}^{2}) = \frac{2gy}{v_\text{ter}^{2}}
$$
$$
\ln(v_\text{ter}^{2}-v^{2}) = \frac{2gy}{v_\text{ter}^{2}} - \ln(v_\text{ter}^{2}-v_{0}^{2})
$$
$$
v^{2} = v_\text{ter}^{2} - \exp \left[ \frac{2gy}{v_\text{ter}^{2}} - \ln(v_\text{ter}^{2}-v_{0}^{2}) \right]
$$
- I have an algebra mistake somewhere I think. Finish this question later
# Question 2
---
a.
- Done in Python
---
b.
Forward Euler has linear error
- Well, I already knew this
# Question 3
Equations of motion:
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
Result:
$$
\ln\left( \frac{r}{r_{0}} \right) = \ln\left( \frac{\omega}{\omega_{0}} \right) \implies  \frac{r}{r_{0}} = \frac{\omega}{\omega_{0}}
$$
Solve for $\omega$
$$
\dot{\theta} = \omega = \frac{\omega_{0}}{r_{0}} r
$$
According to the first equation
$$
\ddot{r} = \frac{dv}{dt} = \frac{dv}{dr} \frac{dr}{dt} = v \frac{dv}{dr} = r \dot{\theta}^{2} = r \left( \frac{\omega_{0}}{r_{0}}r \right)^{2} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{3}
$$
Where $v$ is the radial velocity, in this case. The above yields the ODE:
$$
v \frac{dv}{dr} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} r^{3}
$$
Solve using separation of variables by integrating both sides,
$$
\int_{v_{0}}^{v} v \, dv = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} \int_{r_{0}}^{r} r^{3} \, dr
$$
Result:
$$
v^{2} - v_{0}^{2} = \left( \frac{\omega_{0}}{r_{0}} \right)^{2} (r^{4}-r_{0}^{4})
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
- Finish this question later
# Question 4
---
a.
Recall that for two commensurate frequencies, if,
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
Compute the period:
$$
nT_{2} = 28 \left( \frac{2\pi}{7} \right) = 8\pi
$$
---
b.
Compute the velocity of the two functions
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
In conclude:
$$
A = 2\left( 3-\frac{5i}{2} \right) \qquad \phi=0
$$
