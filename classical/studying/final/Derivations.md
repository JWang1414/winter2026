# Lecture 2
As an ODE, Newton's 2nd law becomes $F=m\ddot{x}$.

If we have a time dependence force,
$$
F=m\dot{v}=F(t) \implies  m \frac{dv}{dt} = F(t)
$$
According to separation of variables,
$$
m \int_{v_{0}}^{v} dv = \int_{t_{0}}^{t} F(t) \, dt  \implies  m(v(t)-v_{0}) = \int_{t_{0}}^{t} F(t) \, dt
$$
Re-arrange to find,
$$
v(t) = v_{0} + \frac{1}{m} \int_{t_{0}}^{t} F(t) \, dt
$$
Which we can integrate again to solve for the position,
$$
x(t) = x_{0} + \int_{t_{0}}^{t} v(t) \, dt
$$
In the case of a position dependent force $F(x)$, we must first apply chain rule to the acceleration,
$$
a=\frac{dv}{dt} = \frac{dv}{dx} \frac{dx}{dt} = \frac{dv}{dx} v
$$
Now, according to Newton's 2nd law,
$$
mv \frac{dv}{dx} = F(x) \implies  m \int_{v_{0}}^{v} v \, dv =\int_{x_{0}}^{x} F(x) \, dx
$$
Which eventually yields,
$$
\frac{1}{2}m (v^{2}-v_{0}^{2}) = \int_{x_{0}}^{x} F(x) \, dx
$$
When the force depends on the velocity $F(v)$,
$$
m \frac{dv}{dt} = F(v) \implies  \frac{m}{F(v)} \, dv = dt \implies  t-t_{0} = m \int_{v_{0}}^{v} \frac{1}{F(v)} \, dv
$$
# Lecture 3
Recall that, in polar coordinates, we have,
$$
x=r\cos\theta \qquad y=\sin\theta
$$
The unit vectors are now,
$$
\hat{r} = \cos\theta \hat{x} + \sin\theta \hat{y} \qquad \hat{\theta}=-\sin\theta \hat{x} + \cos\theta \hat{y}
$$
$$
\hat{x}=\cos\theta \hat{r} - \sin\theta \hat{\theta} \qquad \hat{y}=\sin\theta \hat{r} + \cos\theta \hat{\theta}
$$
The position vector is therefore,
$$
\vec{r}=x\hat{x}+y\hat{y}=r\hat{r}
$$
So the velocity is,
$$
\vec{v}=\frac{d}{dt} \vec{r} = \frac{d}{dt} (r\hat{r}) = \dot{r}\hat{r} + r \frac{d}{dt} \hat{r}
$$
Computing the derivative of $\hat{r}$,
$$
\frac{d}{dt} \hat{r} = -\dot{\theta} \cos\theta \hat{x} + \dot{\theta} \sin\theta \hat{y} = \dot{\theta}\hat{\theta}
$$
Which yields,
$$
\vec{v} = \dot{r}\hat{r} + r\dot{\theta} \hat{\theta}
$$
Applying the chain rule one more time to solve for the acceleration,
$$
\vec{a} = \ddot{r} \hat{r} + \dot{r} \frac{d}{dt} \hat{r} + \dot{r}\dot{\theta}\hat{\theta} + r \ddot{\theta} \hat{\theta} + r\dot{\theta} \frac{d}{dt} \hat{\theta}
$$
Once again, noting that,
$$
\frac{d\hat{r}}{dt} = \dot{\theta}\hat{\theta} \qquad \frac{d\hat{\theta}}{dt} = -\dot{\theta} \hat{r}
$$
Yields,
$$
\vec{a} = (\ddot{r}-r\dot{\theta})^{2} \hat{r} + (2\dot{r}\dot{\theta} + r \ddot{\theta})\hat{\theta}
$$
# Lecture 4
Suppose we have two distinct signals with the form:
$$
x_{i} = \cos(\omega_{i}t)
$$
The superposition of these two signals is,
$$
x_{1}+x_{2} = \cos(\omega_{1}t) + \cos(\omega_{2}t) = \mathrm{Re}\{ e^{ i\omega_{1}t } + e^{ i\omega_{2}t } \}
$$
Define the new variables,
$$
\omega_{1}t=\alpha+\beta \qquad \omega_{2}t=\alpha-\beta
$$
Which simplifies the above into:
$$
\begin{align}
 & = \mathrm{Re}\{ e^{ i(\alpha+\beta) + e^{ i(\alpha-\beta) } } \} \\
 & = \mathrm{Re}\{ e^{ i\alpha }(e^{ i\beta }+e^{ -i\beta }) \} \\
 & = 2\cos \alpha \cos \beta \\
 & = 2 \cos \left[ \frac{(\omega_{1}-\omega_{2})t}{2} \right] \cos \left[ \frac{(\omega_{1}+\omega_{2})t}{2} \right]
\end{align}
$$
Notice how, when $\omega_{1}\approx \omega_{2}$, this new signal is now composed of two waves, one slow oscillating, and one quick oscillating. The results in the creation of envelopes characteristic of beating.
# Tutorial 2
These five expressions are equivalent methods of expressing simple harmonic oscillation.
$$
x(t)=A\cos(\omega t) + B \sin(\omega t) \qquad C\cos(\omega t+\phi)
$$
$$
D \sin(\omega t+\psi) \qquad Ee^{ i\omega t } + Fe^{ -i\omega t }
$$
$$
\mathrm{Re}\{ Ge^{ i\omega t } \}
$$
Specifically, if we choose the initial conditions $x(0)=x_{0}$ and $\dot{x}(0)=v_{0}$ we have:
$$
A=x_{0} \qquad B=\frac{v_{0}}{\omega} \qquad C\sqrt{ x_{0}^{2}+\frac{v_{0}^{2}}{\omega^{2}} }
$$
By initial conditions you will also find that,
$$
\cos \phi = \frac{x_{0}}{C} \qquad \sin \phi=-\frac{v_{0}}{\omega C}
$$
Dividing the two by each other tells us,
$$
\tan \phi = -\frac{v_{0}}{\omega x_{0}}
$$
Such that $C>0$. This second condition is necessary because there are numerous possible values for $\phi$. Following similar steps, you will also obtain,
$$
C=D \qquad \psi=\phi+\frac{\pi}{2}
$$
Substituting the initial conditions into 5, you obtain a system of equations. Solving this system yields,
$$
E=\frac{1}{2} \left( x_{0}-i \frac{v_{0}}{\omega} \right) \qquad F=\frac{1}{2} \left( x_{0}+i \frac{v_{0}}{\omega} \right)
$$
So $F=E^*$. If you plug this back into the equation we just solved, we find,
$$
x(t) = Ee^{ i\omega t } + E^* e^{ -i\omega t } = 2\mathrm{Re}\{ E e^{ i\omega t } \}
$$
Which tells us exactly what $G$ is. For this to be true, $G=2E$.
# Lecture 5
In simple harmonic oscillation, there is just one force,
$$
F=-kx_{0}
$$
Apply Newton's 2nd law to obtain the ODE,
$$
\ddot{x}+\omega_{0}^{2}x=0
$$
Where we have defined $\omega_{0}^{2}=k /m$.

The solutions to this ODE are the ones discussed in the Tutorial 2 section. They depend on the initial position and velocity $x_{0}$ and $v_{0}$, as just seen prior.
# Lecture 6
Now, in combination with SHM, add a few damping force,
$$
F_{d} = -bv=-b\dot{x}
$$
According to Newton's 2nd law we have,
$$
m\ddot{x}=-kx-b\dot{x}
$$
Which yields,
$$
\ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x=0
$$
Where,
$$
\gamma=\frac{b}{2m} \qquad \omega_{0}^{2}=\frac{k}{m}
$$
Substitute in the trial solution $x=c e^{ rt }$,
$$
(r^{2}+2\gamma r+\omega_{0}^{2}) x(t)=0 \implies  r^{2}+2\gamma r+\omega_{0}^{2}=0
$$
This is a polynomial with solutions,
$$
r_{\pm} = -\gamma\pm \sqrt{ \gamma^{2}-\omega_{0}^{2} }
$$
The general solution to the ODE will be a superposition of the two possible solutions,
$$
\begin{align}
x(t) & = \mathrm{Re}\{ c_{+} e^{ r_{+}t } + c_{-} e^{ r_{-}t } \} \\
 & = e^{ -\gamma t } \mathrm{Re}\{ c_{+} e^{ \sqrt{ \Delta }t } + c_{-} e^{ -\sqrt{ \Delta }t } \}
\end{align}
$$
Where the differential $\Delta=\gamma^{2}-\omega_{0}^{2}$.

From here, there are three regimes of damping. $\omega_{0}^{2}>\gamma^{2}$, $\omega_{0}^{2}<\gamma^{2}$ and $\omega_{0}=\gamma$. These are light damping, heavy damping, and critical damping, respectively.

In the case of light damping $\Delta<0$ so $r_{\pm}$ are two imaginary numbers. The general solution in this case becomes,
$$
x(t) = e^{ -\gamma t } (c_{+}e^{ i\omega_{d}t } + c_{-}e^{ -i\omega_{d}t })
$$
When we have heavy damping, the general solution becomes,
$$
x(t)=c_{+} e^{ -(\gamma-\alpha)t } + c_{-} e^{ -(\gamma+\alpha)t }
$$
Which is a summation of two decaying exponentials.
- Note that in the case of critical damping, the general solution we found is no longer valid, and so a different solution must be found
# Lecture 7
Assume the force applied onto a mass is now,
$$
F=-k[x-A_{f}\cos(\omega t)]
$$
Where $A_{f}$ is the amplitude of the driving force. From Newton's 2nd law, we obtain the ODE,
$$
\ddot{x} + \omega_{0}^{2}x = \omega_{0}^{2}A_{f}\cos(\omega t)
$$
Note that the general solution includes the homogeneous version, with $A_{f}=0$. This is the solution found from last time. To find the particular solution, however, we move from the real space to the complex space:
$$
\ddot{z}+\omega_{0}^{2}z=\omega_{0}^{2}A_{f} e^{ i\omega t }
$$
Adopt the exponential $z=Z e^{ rt }$
$$
(r^{2}+\omega_{0}^{2})Ze^{ rt } = \omega_{0}^{2} A_{f} e^{ i\omega t }
$$
The exponential on both sides must match, revealing that $r=i\omega$. Now, solving for $Z$ we have,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{\omega_{0}^{2}-\omega^{2}}
$$
In the polar representation,
$$
Z(\omega) = A(\omega)e^{ -i\delta }
$$
The real and positive amplitude $A(\omega)$ is,
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\lvert \omega_{0}^{2}-\omega^{2} \rvert }
$$
So the phase is therefore,
$$
e^{ -i\delta } = \text{sign}(\omega_{0}^{2}-\omega^{2})
$$
- This strange form arises because $Z(\omega)$ is entirely real, and so $e^{ -i\delta }$ must also follow this constraint.

The second part is showing why,
$$
x(t) = \frac{1}{2} A_{f} \omega_{0}t \cos\left( \omega_{0}t-\frac{\pi}{2} \right)
$$
Is a solution of,
$$
\ddot{x}+\omega_{0}^{2}x = \omega_{0}^{2}A_{f} \cos(\omega_{0}t)
$$
At resonance, when $\omega=\omega_{0}$. Pretty sure this is just algebra, and I do not want to do this, so I will not.
# Lecture 22
From $L=mr^{2}\dot{\theta}$ we have,
$$
\dot{\theta} = \frac{L}{mr^{2}}
$$
Furthermore, using the chain rule,
$$
\dot{r} = \frac{dr}{dt} = \frac{dr}{d\theta} \frac{d\theta}{dt} = \frac{L}{mr^{2}} \frac{dr}{d\theta}
$$
Substituting in $h=L /m$ and $y=r^{-1}$, this becomes,
$$
\dot{r} = hy^{2} \frac{d}{d\theta}y^{-1} = hy^{2} \left( -\frac{1}{y^{2}} \right) \frac{dy}{d\theta} = -h \frac{dy}{d\theta}
$$
The second time derivative of this is,
$$
\ddot{r} = -h \frac{d}{dt}  \frac{dy}{d\theta} = -h \frac{d}{d\theta} \frac{dy}{dt} = -h \frac{d}{d\theta} \frac{dy}{d\theta} \frac{d\theta}{dt} = -h^{2}y^{2} \frac{d^{2}y}{d\theta^{2}}
$$
Recall that the acceleration in radius coordinates is,
$$
a_{r} = \ddot{r}-r\dot{\theta}^{2} = -h^{2}y^{2} \frac{d^{2}y}{d\theta^{2}} - \frac{(hy^{2})^{2}}{y} = -h^{2}y^{2} \left( \frac{d^{2}y}{d\theta^{2}}+y \right)
$$
As needed.
# Lecture 19
---
i.
The wave equation is:
$$
\frac{ \partial^{2}y }{ \partial t^{2} } -v^{2} \frac{ \partial^{2}y }{ \partial x^{2} } =0
$$
Use separation of variables,
$$
y(x, t) = X(x)T(t)
$$
Substitute into the wave equation,
$$
XT'' - v^{2}X''T=0 \implies  XT'' = v^{2}X''T \implies  \frac{T''}{T} = v^{2}\frac{X''}{X}
$$
This form may only be true if both sides are equal to the same constant. Call this constant $-\omega^{2}$.

Solve for $T(t)$,
$$
\frac{T''}{T} = -\omega^{2} \implies  T''=-\omega^{2}T
$$
Which has the familiar solution,
$$
T(t) = h_{0} \cos(\omega t+\phi)
$$
Where $h_{0}$ is some amplitude and $\phi$ is some phase. The same can be repeated for $X(x)$:
$$
v^{2} \frac{X''}{X} = -\omega^{2} \implies  X''=-\frac{\omega^{2}}{v^{2}}X = -k^{2}X
$$
Where $k=\omega /v$. This has the same solution,
$$
X(x) = A \cos(kx) + B \sin(kx)
$$
Writing it in the different form for convenience. The full solution is therefore,
$$
y(x, t) = X(x)T(t) = h_{0} \cos(\omega t+\phi) \left[ A\cos(kx) + B\sin(kx) \right]
$$
---
ii.
From here you can apply boundary conditions like $y(x=0)=y(x=L)=0$ to solve for the constants.

In this class, it'll be useful to remember the facts that,
$$
B\sin(kL) =0 \implies  kL=n\pi \implies  k_{n} = \frac{n\pi}{L}
$$
So on and so forth. The solution is now written as the summation:
$$
y(x, t) = \sum_{n=1}^{\infty} \left[ \alpha_{n}\cos(\omega_{n}t) + \beta_{n}\sin(\omega_{n}t) \right] \sin(k_{n}x)
$$
# Lectures 11, 12
Assume we have conserved energy in the form,
$$
E = a \dot{q}^{2}+bq^{2} = \text{Constant}
$$
Where $q$ is some variable related to position. The derivative with respect to time of this expression is,
$$
\dot{E} = 2a \dot{q} \ddot{q} + 2b q \dot{q}^{2} = 2\left( \ddot{q} + \frac{b}{a}q \right)a \dot{q} =0
$$
Which gives us,
$$
\ddot{q} + \frac{b}{a}q=0
$$
The equation for simple harmonic oscillation, with natural angular frequency $\omega_{0}=\sqrt{ b /a }$.

General potentials can be approximated as a quadratic so long as the 2nd derivative is non zero. If we, for example, approximate some potential $U(x)$ a small distance $\varepsilon$ we have,
$$
U(x) = U(x_{0}+\varepsilon) \approx U(x_{0}) + \varepsilon \underbrace{ U'(x_{0}) }_{ =0 } + \frac{1}{2} \varepsilon^{2}U''(x_{0})
$$
This segment being 0 because $x_{0}$ is chosen to be at a minimum. Now, if we re-define the energy to be $\bar{E}=E-U(x_{0})$ then the total energy is,
$$
\bar{E} = K + \frac{1}{2}\varepsilon^{2} U''(x_{0}) = \frac{1}{2} m\dot{\varepsilon}^{2}+\frac{1}{2} U''(x_{0})\varepsilon^{2}
$$
As an equation for the approximate energy. The angular frequency, using our previous method is therefore,
$$
\omega^{2} = \frac{U''(x_{0})}{m}
$$
# Lecture 8
Assume we have,
$$
\ddot{x} + 2\gamma \dot{x} + \omega_{0}^{2}x = \omega_{0}^{2}A_{f} \cos(\omega t)
$$
Move into the complex space,
$$
\ddot{z} + 2\gamma \dot{z} + \omega_{0}^{2}z = \omega_{0}^{2}A_{f} e^{ i\omega t }
$$
Adopt the exponential $z=Ze^{ rt }$ and you should find that,
$$
r=i\omega \qquad (-\omega^{2}+2i\gamma \omega + \omega_{0}^{2})Z = \omega_{0}^{2} A_{f}
$$
Therefore yielding,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{\omega_{0}^{2}-\omega^{2}+2i\gamma \omega}
$$
Simplify this expression by defining the new quantities,
$$
p=\omega_{0}^{2}-\omega^{2} \qquad q=2\gamma \omega
$$
Express $Z$ in polar form is $Z=A(\omega)e^{ -i\delta(\omega) }$. Solve for the amplitude,
$$
\lvert Z \rvert  = A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ p^{2}+q^{2} }} = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }}
$$
To solve for the phase, begin by decomposing $Z$ into its real and imaginary parts,
$$
Z = \frac{\omega_{0}^{2}A_{f}}{p+iq} \frac{p-iq}{p-iq} = \frac{\omega_{0}^{2}A_{f}(p-iq)}{p^{2}+q^{2}}
$$
Therefore,
$$
\frac{Z}{A(\omega)} = \frac{\omega_{0}^{2}A_{f}(p-iq)}{p^{2}+q^{2}} \frac{\sqrt{ p^{2}+q^{2} }}{\omega_{0}^{2}A_{f}} = \frac{p-iq}{\sqrt{ p^{2}+q^{2} }} = e^{ -i\delta }
$$
Decomposing the phase portion with Euler's identity we have,
$$
\cos\delta -i \sin\delta = \frac{p-iq}{\sqrt{ p^{2}+q^{2} }}
$$
So,
$$
\cos\delta = \frac{p}{\sqrt{ p^{2}+q^{2} }} \qquad \sin\delta = \frac{q}{\sqrt{ p^{2}+q^{2} }}
$$
Dividing these two yields,
$$
\tan\delta = \frac{\sin\delta}{\cos\delta} = \frac{q}{p} \implies  \delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
Apply a few limiting behaviours:

Low frequency $\omega\ll \omega_{0}$,
$$
A(\omega) = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ (\omega_{0}^{2}-\omega^{2})^{2}+4\gamma^{2}\omega^{2} }} = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ \omega_{0}^{4} }} = A_{f}
$$
And the phase is,
$$
\delta(\omega) = \arctan(0) =0
$$

High frequency $\omega\gg \omega_{0}$,
$$
A(\omega) \approx \frac{\omega_{0}^{2}A_{f}}{\sqrt{ \omega^{4}+4\gamma^{2}\omega^{2} }} \to 0
$$
$$
\tan\delta \approx \frac{2\gamma}{-\omega} \to  0_{-} \implies  \lim_{ \omega \to \infty } \delta=\pi
$$

At resonance $\omega=\omega_{0}$,
$$
A(\omega_{0}) = \frac{\omega_{0}A_{f}}{2\gamma} = \frac{Q}{2}A_{f}
$$
Furthermore,
$$
\delta(\omega) = \arctan\left( \frac{2\gamma \omega_{0}}{0} \right) = \arctan(\infty) \to  \frac{\pi}{2}
$$
# Lectures 20-21
The rate of change of the kinetic energy is,
$$
\vec{K} = \frac{d}{dt} \left( \frac{1}{2} m \vec{v}\cdot \vec{v} \right) = \frac{m}{2} (\dot{\vec{v}}\cdot \vec{v} + \vec{v}\cdot \dot{\vec{v}}) = m \frac{d\vec{v}}{dt} \cdot \vec{v} = m\vec{a}\cdot \vec{v} = \vec{F}\cdot \vec{v}
$$
For a conservative force, the rate of change in the potential energy is,
$$
\dot{U} = \frac{dU}{dt} = \frac{ \partial U }{ \partial x } \dot{x} + \frac{ \partial U }{ \partial y } \dot{y} + \frac{ \partial U }{ \partial z } \dot{z} = \vec{v}\cdot \vec{\nabla}U
$$
Recall that for a conservative force we have $\vec{F}=-\vec{\nabla}U$ and so,
$$
\dot{U} = -\vec{F}\cdot \vec{v}
$$
The rate of change in the mechanical energy is therefore,
$$
\dot{E} = \dot{K} + \dot{U} = \vec{F}\cdot \vec{v} - \vec{F}\cdot \vec{v} =0
$$
True for any conservative force, and therefore also true for central forces, which are an example of a conservative force.

The definition of angular momentum is:
$$
\vec{L} = \vec{r}\times \vec{p}
$$
Where $\vec{p}=m\vec{v}$. The rate of change in the angular momentum is therefore,
$$
\dot{\vec{L}} = \dot{\vec{r}} \times \vec{p} + \vec{r}\times \dot{\vec{p}}
$$
Notice that,
$$
\dot{\vec{p}} = m\dot{\vec{v}} = a\vec{m} = \vec{F}
$$
$\dot{\vec{L}}$ becomes,
$$
\dot{\vec{L}} = \underbrace{ \vec{v}\times m\vec{v} }_{ =0 } + \vec{r} \times \vec{F}
$$
Now, notice that, if we have a central force, then $\vec{F}$ and $\vec{r}$ are parallel. So, $\vec{r}\times \vec{F}=0$. Therefore $\dot{\vec{L}}=0$ and the angular momentum is also conserved.

Going back to the expression of $\vec{v}$ is polar coordinates,
$$
\vec{v} = \dot{r}\hat{r} + r\dot{\theta} \hat{\theta}
$$
The angular momentum can also be expressed as,
$$
\vec{L} = \vec{r}\times \vec{p} = m(\vec{r}\times \vec{v}) = m(r\hat{r} \times (\dot{r}\hat{r} + r\dot{\theta} \hat{\theta})) = mr^{2}\dot{\theta} (\hat{r}\times\hat{\theta}) = L\hat{z}
$$
Where we have defined the angular momentum to be $L=mr^{2}\dot{\theta}$.

Uniquely, the kinetic energy in this system is,
$$
K = \frac{1}{2}mv^{2} = \frac{1}{2} m(v_{r}^{2}+v_{\theta}^{2}) = \frac{1}{2}m(\dot{r}^{2} + r^{2}\dot{\theta}^{2}) = \frac{1}{2}m \left( \dot{r}^{2} + \frac{L^{2}}{m^{2}r^{2}} \right)
$$
Which motivates the definition of the effective potential energy such that,
$$
E = K+U = \frac{1}{2} m\dot{r}^{2} + \frac{L^{2}}{2mr^{2}} + U(r) = \frac{1}{2}m\dot{r}^{2} + U_\text{eff}(r)
$$
If we think of the effective potential as some force, then we have,
$$
F_\text{eff} = -\frac{dU_\text{eff}}{dr} = \frac{L^{2}}{mr^{3}} - \frac{dU}{dr}
$$
Recall that in the regime where $0<dU /dr<L^{2} /mr^{3}$ the effective potential will have a potential well. The radius where the centrifugal force and the central forces are balanced is where we will find a circular orbit.

The orbital frequency will be,
$$
\dot{\theta} = \frac{L}{mr_{0}^{2}} = \omega _\text{orbit}
$$
And the period is,
$$
T = \frac{2\pi mr_{0}^{2}}{L}
$$
Small deviations from the circular orbit can occur. To find the frequency of oscillation about these deviations, we can model the mechanical energy as a quadratic function with Taylor series:
$$
E = \frac{1}{2}m\dot{r}^{2} + U_\text{eff}(r)
$$
Taylor expand the effective potential,
$$
U_\text{eff}(r) \approx U_\text{eff}(r_{0}) + qU'_\text{eff}(r_{0}) + \frac{1}{2}q^{2} U''_\text{eff}(r_{0})
$$
Using the same strategy as before, we obtain,
$$
\bar{E} = \frac{1}{2}m \dot{q}^{2} + \frac{1}{2} U''_\text{eff}(r_{0}) q^{2}
$$
Revealing that we have simple harmonic oscillations with the angular frequency,
$$
\omega=\sqrt{ \frac{U''_\text{eff}(r_{0})}{m} }
$$
In the case where the potential is $U=-\alpha /r$, you should find that the radius of orbit is,
$$
r_{0} = \frac{L^{2}}{m\alpha}
$$
So the frequency of orbits is,
$$
\omega _\text{orbit} = \frac{L}{mr_{0}^{2}} = \frac{m\alpha^{2}}{L^{3}}
$$
Solve for the frequency of perturbations to find,
$$
U''_\text{eff}(r_{0}) = \frac{d^{2}}{dr^{2}}\left( \frac{L^{2}}{2mr^{2}} - \frac{\alpha}{r} \right) = \frac{3L^{2}}{mr_{0}^{4}} - \frac{2\alpha}{r_{0}^{3}} = \frac{m^{3}\alpha^{4}}{L^{6}}
$$
$$
\omega _\text{perturbations} = \sqrt{ \frac{U''_\text{eff}(r_{0})}{m} } = \frac{m\alpha^{2}}{L^{3}}
$$
So the frequency of oscillation for the perturbations and the orbits are the same.
# Lecture 16, 17
How to solve for the normal frequencies of coupled oscillators using linear algebra.

Define each mass position to be one component of a state vector,
$$
\vec{X} = \begin{bmatrix}
x_{A} \\
x_{B}
\end{bmatrix} \implies  \ddot{\vec{X}} = \begin{bmatrix}
\ddot{x}_{A} \\
\ddot{x}_{B}
\end{bmatrix}
$$
Our system of equations can now be re-written as:
$$
M\ddot{\vec{X}} + K\vec{X}=0
$$
Where we have defined the matrices,
$$
M = \begin{bmatrix}
m & 0 \\
0 & m
\end{bmatrix} \qquad K= \begin{bmatrix}
\frac{mg}{l}+k & -k \\
-k & \frac{mg}{l}+k
\end{bmatrix}
$$
Now, we can apply a series of steps to solve this system.

Begin by adopting an exponential $\vec{Z}=\vec{Z}_{0}e^{ i\omega t }$,
$$
M\ddot{\vec{Z}} = M(-\omega^{2})\vec{Z} = -\omega^{2}M\vec{Z}
$$
From which we have the new system,
$$
-\omega^{2}M\vec{Z} + K\vec{Z} =0 \implies  (K-\omega^{2}M)\vec{Z}=0
$$
A matrix equation can only have non-trivial solutions if the determinant is zero. Therefore,
$$
\det(K-\omega^{2}M)=0
$$
Which is an equation you can solve. The resulting characteristic polynomial contains the two roots,
$$
\omega_{1}=\omega_{p} \qquad \omega_{2}=\sqrt{ \omega_{p}^{2}+2\omega_{s}^{2} }
$$
These eigenvalues are the two modes we are interested in. They represent the angular frequency of the two eigenmodes of the system