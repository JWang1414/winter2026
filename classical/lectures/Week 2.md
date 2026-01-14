Example:
Find the radius of orbit $r$ of a planet in uniform circular motion around the Sun under the influence of gravity with $F_{r}=-GMm /r^{2}$, if the period is one year.

Because the radius is fixed, $\dot{r}=\ddot{r}=0$. In order, there is no azimuthal force $F_{\theta}=0$.

Recall that, in polar coordinates, Newton's 2nd law reduces to,
$$
F_{r} = m(\ddot{r}-r\dot{\theta}^{2})
$$
Therefore we have,
$$
-mr\dot{\theta}^{2} = - \frac{GMm}{r^{2}} \implies r = \left( \frac{GM}{\dot{\theta}^{2}} \right)^{1/3}
$$
The angular velocity in terms of the period is,
$$
\dot{\theta} = \omega = \frac{2\pi}{T} = \frac{2\pi}{365.25(24)(60^{2})}
$$
- Using the mass of the Sun, this derives Earth's radius of orbit. One astronomical unit
---
Example:
Consider a particle that feels an angular force only, of the form $F_{\theta}=m \dot{r}\dot{\theta}$. Show that $\dot{r}=\sqrt{ A\ln r+B }$ where $A$ and $B$ are constants of integration.

Applying Newton's laws we have,
$$
0=m(\ddot{r}-r\dot{\theta}^{2})
$$
$$
m\dot{r}\dot{\theta} = m (r \ddot{\theta} + 2\dot{r}\dot{\theta})
$$
Simplifying the second equation yields,
$$
-\dot{r}\dot{\theta} = r \ddot{\theta} \implies -\frac{\dot{r}}{r} = \frac{\dot{\omega}}{\omega}
$$
Integrate both sides,
$$
\frac{1}{r} \frac{dr}{dt} = -\frac{1}{\omega} \frac{d\omega}{dt} \implies \frac{dr}{r} = - \frac{d\omega}{\omega}
$$
$$
\int_{r_{0}}^{r} \frac{dr'}{r'} = - \int_{\omega_{0}}^{\omega} \frac{d\omega'}{\omega'} \implies \ln\left( \frac{r}{r_{0}} \right) = \ln\left( \frac{\omega_{0}}{\omega} \right)
$$
Solve for $\dot{\theta}$,
$$
\frac{r}{r_{0}} = \frac{\omega_{0}}{\omega} \implies \dot{\theta} = \frac{r_{0}\omega_{0}}{r}
$$
Substitute this back into the first ODE,
$$
\ddot{r} = r\dot{\theta}^{2} = r \left( \frac{r_{0}\omega_{0}}{r} \right)^{2} = \frac{r_{0}^{2}\omega_{0}^{2}}{r}
$$
Recall that from the chain rule,
$$
\ddot{r} = \frac{dv_{r}}{dt} = \frac{dv_{r}}{dr} \frac{dr}{dt} = v_{r} \frac{dv_{r}}{dt}
$$
Solve the resulting system,
$$
v_{r} \, dv_{r} = r_{0}^{2}\omega_{0}^{2} \frac{dr}{r} \implies \int_{v_{r_{0}}}^{v_{r}} v'_{r} \, dv'_{r} = r_{0}^{2}\omega_{0}^{2} \int_{r_{0}}^{r} \frac{dr'}{r}
$$
$$
\frac{1}{2} (v^{2}_{r} - v^{2}_{r_{0}}) = r_{0}^{2}\omega_{0}^{2} \ln\left( \frac{r}{r_{0}} \right)
$$
Therefore,
$$
\dot{r} = v_{r} = \sqrt{ 2r_{0}^{2}\omega_{0}^{2} \ln\left( \frac{r}{r_{0}} \right) + v^{2}_{r_{0}} }
$$
As needed.

---
# Numerical Solutions
Our goal is to solve the general system,
$$
a = \ddot{x} = \frac{F(x, v, t)}{m}
$$
Using numerical approximations such as central finite differences and Euler-Cromer methods.

---
Example:
Mass and spring system

The force applied to a mass attached to a spring is governed by Hooke's law,
$$
F_{H} = -kx
$$
Apply Newton's 2nd law to find,
$$
m\ddot{x} = -kx \implies \ddot{x}+\omega^{2}x=0
$$
Where I have defined the variable $\omega^{2} = k /m$. This ODE has the known solution,
$$
x = A_{1} \cos(\omega t) + A_{2} \sin(\omega t)
$$
$A_{1}$ and $A_{2}$ can be determined based on the initial conditions.

---

Recall that the Euler-Cromer method for Newton's 2nd law is,
$$
\begin{align}
v_{i+1} & = v_{i} + \Delta t \frac{F(t_{i}, x_{i}, v_{i})}{m} \\
x_{i+1} & = x_{i} + \Delta t v_{i+1}
\end{align}
$$
- Of course, $x_{i+1}$ is edited using the updates $v_{i+1}$ as opposed to the other way around.
![[Pasted image 20260114103650.png]]
A comparison between the analytical spring and the Euler-Cromer simulated one
