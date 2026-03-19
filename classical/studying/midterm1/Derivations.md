# Lecture 2
I believe these are the problems where you do derivations with Newton's 2nd law. We have,
$$
\mathbf{F} = m\mathbf{a} = m \ddot{\mathbf{x}}
$$
If the force depends on position we have,
$$
F(x) = m \frac{d^{2}x}{dt^{2}} \implies  \iint dt = m \iint \frac{1}{F(x)} \, dx
$$
On velocity,
$$
F(v) = m\dot{v} = m \frac{dv}{dt} \implies  \int dt = m \int \frac{1}{F(v)} \, dv
$$
On time,
$$
F(t) = m \frac{d^{2}x}{dt^{2}} \implies  \iint F(t) \, d^{2}t = m \iint d^{2}x
$$
## From Lecture notes
The time dependent case is done with,
$$
m \frac{dv}{dt} = F(t) \implies  m \int_{v_{0}}^{v} dv = \int_{t_{0}}^{t} F(t) \, dt
$$
$$
m [v(t) - v_{0}] = \int_{t_{0}}^{t} F(t) \, dt
$$
$$
v(t) = v_{0} + \frac{1}{m} \int_{t_{0}}^{t} F(t) \, dt
$$
Since $v=\dot{x}$ we have:
$$
x(t) = x_{0} + \int_{t_{0}}^{t} v(t) \, dt
$$
For a velocity dependent force,
$$
m \frac{dv}{dt} = F(v) \implies  m \int_{v_{0}}^{v} \frac{1}{F(v)} \, dv = \int_{t_{0}}^{t}  \, dt
$$
For a position dependent force,
$$
\frac{dv}{dt} = \frac{dv}{dx} \frac{dx}{dt} = v \frac{dv}{dx}
$$
$$
mv \frac{dv}{dx} = F(x) \implies  m \int_{v_{0}}^{v} v \, dv = \int_{x_{0}}^{x} F(x) \, dx
$$
It is possible to evaluate the left side in the case, but not the right,
$$
m \int_{v_{0}}^{v} v \, dv = m \left[ \frac{v^{2}}{2} \right]^{v}_{v_{0}} = \frac{1}{2}m (v^{2} - v_{0}^{2})
$$
# Lecture 3
Recall that,
$$
\hat{r} = \cos\theta \hat{x} + \sin\theta \hat{y} \qquad \hat{\theta} = - \sin\theta \hat{x} + \cos \theta \hat{y}
$$
The derivative of these unit vectors are:
$$
\frac{d}{dt} \hat{r} = -\dot{\theta} \sin\theta \dot{x} + \dot{\theta} \cos\theta \hat{y} = \dot{\theta} \hat{\theta}
$$
And,
$$
\frac{d}{dt} \hat{\theta} = -\dot{\theta} \cos\theta \dot{x} - \dot{\theta} \sin\theta \hat{y} = -\dot{\theta} \hat{r}
$$
The velocity is therefore,
$$
\vec{v} = \frac{d}{dt} r\hat{r} = \dot{r}\hat{r} + r \dot{\theta} \hat{\theta}
$$
And the acceleration is,
$$
\vec{a} = \ddot{r}\hat{r} + \dot{r} (\dot{\theta} \hat{\theta}) + \dot{r} \dot{\theta} \hat{\theta} + r \ddot{\theta} \hat{\theta} + r\dot{\theta} (-\dot{\theta}\hat{r})
$$
Collect like terms,
$$
\vec{a} = (\ddot{r}-r\dot{\theta}^{2}) \hat{r} + (2\dot{r} \dot{\theta} + r \ddot{\theta}) \hat{\theta}
$$
# Lecture 4
This is the section about commensurate waves and beating. Beating occurs when two waves with similar frequencies interfere.

For two commensurate frequencies $\omega_{1}$ and $\omega_{2}$ we require $\omega_{1}=r\omega_{2}$ where,
$$
r = \frac{m}{n}
$$
And the superposed signal is periodic with,
$$
mT_{1} = nT_{2}
$$
Assuming $r=m /n$ has been reduced to the lowest terms.
- $T_{1}$ and $T_{2}$ are the original period lengths of the two signals

The combination of these formulae tell us,
$$
r = \frac{m}{n} = \frac{\omega_{1}}{\omega_{2}} = \frac{T_{2}}{T_{1}}
$$
Assuming we have two waves,
$$
x_{1} = \cos(\omega_{1}t) \qquad x_{2} = \cos(\omega_{2}t)
$$
Define,
$$
\omega_{1}t = \alpha+\beta \qquad \omega_{2}t = \alpha-\beta
$$
Superpose these two waves,
$$
\cos(\omega_{1}t) + \cos(\omega_{2}t) = \mathrm{Re}\{ e^{ i\omega_{1}t } + e^{ i\omega_{2}t } \}
$$
Inside the brackets,
$$
e^{ i(\alpha+\beta) } + e^{ i(\alpha-\beta) } = e^{ i\alpha } (e^{ i\beta } + e^{ -i\beta }) = e^{ i\alpha } (2\cos \beta)
$$
Therefore,
$$
\mathrm{Re}\{ e^{ i\alpha }(2\cos \beta) \} = 2 \cos \alpha \cos \beta
$$
Solve for $\alpha$ and $\beta$
$$
\alpha = \frac{1}{2} (\omega_{1}+\omega_{2})t \qquad \beta = \frac{1}{2} (\omega_{1}-\omega_{2})t
$$
Substitute,
$$
x_{1}+x_{2} = 2 \cos \left[ \frac{1}{2}(\omega_{1}+\omega_{2})t \right] \cos \left[ \frac{1}{2} (\omega_{1}-\omega_{2})t \right]
$$
The first term $\omega_{1}+\omega_{2}$ is called carrier wave and the second $\omega_{1}-\omega_{2}$ is the envelope.
# Lecture 5
## Sinusoidal Oscillation Forms
I won't write all the forms here, just some algebra

First form:
$$
\dot{x} = -\omega A\sin(\omega t) + \omega B \cos(\omega t)
$$
$$
x(0) = A \qquad \dot{x}(0) = \omega B
$$
Therefore we have,
$$
A = x_{0} \qquad B = \frac{v_{0}}{\omega}
$$
Second form:
$$
\dot{x} = -\omega C\sin(\omega t+\phi)
$$
$$
x(0) = C \cos \phi=x_{0} \qquad \dot{x}(0) = -\omega C \sin \phi =v_{0}
$$
$$
C = \frac{x_{0}}{\cos \phi} = -\frac{v_{0}}{\omega \sin \phi}
$$
$$
\tan \phi = -\frac{v_{0}}{\omega x_{0}} = -\frac{B}{A}
$$
Third form:
$$
\dot{x} = \omega D \cos(\omega t+\psi)
$$
$$
x(0) = D \sin \psi =x_{0} \qquad \dot{x}(0) = \omega D \cos \psi =v_{0}
$$
$$
D = \frac{x_{0}}{\sin \psi} = \frac{v_{0}}{\omega \cos \psi}
$$
$$
\tan \psi = \frac{\omega x_{0}}{v_{0}} = \frac{A}{B}
$$
Fourth form:
$$
\dot{x} = i\omega E e^{ i\omega t } - i\omega Fe^{ -i\omega t } = i\omega(Ee^{ i\omega t } - Fe^{ -i\omega t })
$$
$$
x(0) = E+F = x_{0} \qquad \dot{x}(0) = i\omega(E-F) = v_{0}
$$
You can solve this system of equations. You should find that $F=E^*$ where the star indicates complex conjuate
- This results because $x(t)$ must be real

This result also means that,
$$
\mathrm{Re}\{ Ee^{ i\omega t } + Fe^{ -i\omega t } \} = 2E \cos(\omega t)
$$
Which you can apply to the next part,
$$
\mathrm{Re}\{ Ge^{ i\omega t } \} = G \cos(\omega t)
$$
And therefore conclude that, since they must be equivalent, $G=2E$
## General solution to SHM
Assuming a spring, the force on the mass is,
$$
F=-kx_{0}
$$
And according to Newton's 2nd law we obtain,
$$
m\ddot{x} = -kx \implies  m\ddot{x} + kx =0
$$
Or,
$$
\ddot{x} + \omega_{0}^{2}x = 0 \qquad \text{where } \omega_{0}^{2} = \frac{k}{m}
$$
The solution to this is,
$$
x(t) = Ee^{ i\omega t } + E^* e^{ -i\omega t }
$$
Alternatively we can actually solve this system with a trial solution: $c e^{ rt }$
$$
\ddot{x} + \omega_{0}^{2}x = c r^{2} e^{ rt } + \omega_{0}^{2} c e^{ rt } = (r^{2}+\omega_{0}^{2}) c e^{ rt } =0
$$
Which tells us that,
$$
r^{2}+\omega_{0}^{2} =0 \implies  r^{2} =-\omega_{0}^{2} \implies  r = \pm i\omega_{0}
$$
Which are the two possible branches of this system

You can solve the system of equations to find $E$. But it is,
$$
E = \frac{1}{2} \left( x_{0} - i \frac{v_{0}}{\omega_{0}} \right)
$$
# Lecture 6
I believe this just arises from the solution of the ODE?

Use the trial solution: $ae^{ rt }$
$$
\ddot{x} + 2\gamma \dot{x} + \omega^{2}x =0
$$
$$
(r^{2}+2\gamma r + \omega^{2}) ae^{ rt } =0
$$
$$
r^{2}+2\gamma r+\omega^{2} =0
$$
Solve using quadratic formula,
$$
a=1 \qquad b=2\gamma \qquad c=\omega^{2}
$$
$$
r = \frac{-b\pm \sqrt{ b^{2}-4ac }}{2a} = \frac{-2\gamma \pm \sqrt{ 4\gamma^{2} - 4\omega^{2} }}{2}
$$
$$
r = -\gamma \pm \sqrt{ \gamma^{2}-\omega^{2} }
$$
Which has the three regimes:
$$
\gamma < \omega, \gamma=\omega, \gamma>\omega
$$
Where in these cases the solution is imaginary, real, or real. In the case where $\gamma=\omega$ the solution changes, and we have critical damping.

The general form is:
$$
x(t) = \mathrm{Re}\{ a_{1} \exp \left[ (-\gamma+\sqrt{ \gamma^{2}-\omega^{2} })t \right] + a_{2} \exp \left[ (-\gamma - \sqrt{ \gamma^{2}-\omega^{2} })t \right]  \}
$$
You can simplify this to,
$$
x(t) = e^{ -\gamma t } \mathrm{Re}\left\{ a_{1} e^{ \sqrt{ \gamma^{2}-\omega^{2} } } + a_{2} e^{ -\sqrt{ \gamma^{2}-\omega^{2} } } \right\}
$$
