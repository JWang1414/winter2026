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
