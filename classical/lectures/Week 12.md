# Central Forces Problems
Last time, we found that $F$ and $U$ were 1D, and so the 2D problem of the central field can be solved with intermediate 1D problems.

The equations are formally the same as those for conservative forces in 1D, and so we have the general solution that,
$$
t-t_{0} = \pm \sqrt{ \frac{m}{2} } \int_{r_{0}}^{r} \frac{1}{\sqrt{ E-U_\text{eff}(r') }} \, dr'
$$
And we can use the conservation of $L$ to find a general solution for $\theta(t)$,
$$
\theta-\theta_{0} = \frac{L}{m} \int_{t_{0}}^{t} \frac{1}{r^{2}(t')} \, dt'
$$
## Effective force
There are three major regimes in the effective radial force:
$$
F_\text{eff} = -\frac{U_\text{eff}}{dr} = \frac{L^{2}}{mr^{3}} - \frac{dU}{dr}
$$
The first term $L^{2} /mr^{3}$ is always positive. It is called the centrifugal force, or angular momentum barrier.

If $F(r)=-dU /dr > 0$ then $-dU_\text{eff} /dr>0$ and so the the effective force is repelling. The trajectories are unbounded and eventually $r\to \infty$.

If $F(r)<0$ and strong enough to overcome the centrifugal force, than we have a strongly attracting force.

In the middle of the two is the moderately attracting force. This is the case where there are orbits around the origin. $U_\text{eff}(r)$ looks like it has a potential well.

![[Pasted image 20260411173416.png]]
An image of the three regimes, plotted as functions of radius.
## Circular orbits
Assume there is a radius $r_{0}$ where $\dot{r}=0$ and the forces are balanced. The particle is expected to stay in this radius for infinity (so long as it is not disturbed).

The particle orbits with frequency,
$$
\dot{\theta} = \frac{L}{mr_{0}^{2}} = \omega _\text{orbit}
$$
The period of one orbit is therefore,
$$
T = \frac{2\pi mr_{0}^{2}}{L}
$$
## Deviations from circular orbits
What happens if we perturb the orbit such that,
$$
U''_\text{eff}(r_{0})>0
$$
Well, physically, these show up as variations in the radius.

For small amplitude perturbations, the oscillations are SHM in $r$. Recall that the energy in the system is:
$$
E = \frac{1}{2} m\dot{r}^{2} + U_\text{eff}(r)
$$
Taylor expand the potential,
$$
U_\text{eff}(r) = U_\text{eff}|_{r=r_{0}} + \frac{1}{2} q^{2}U''_\text{eff} | _{r=r_{0}}
$$
Where $U'_\text{eff}=0$. The conservation of energy becomes,
$$
\bar{E} = E-U_\text{eff}|_{r=r_{0}} = \frac{1}{2}m \dot{q}^{2} + \frac{1}{2} U''_\text{eff}|_{r=r_{0}} q^{2}
$$
So there are small oscillations,
$$
q(t) = A\cos(\omega t+\phi) \qquad \omega=\sqrt{ \frac{U''_\text{eff}|_{r=r_{0}}}{m} }
$$
![[Pasted image 20260411175410.png]]
An example orbit with a small perturbation.

There is a particular case when the potential has the form,
$$
U = -\frac{\alpha}{r} \implies U_\text{eff} = \frac{L^{2}}{2mr^{2}} - \frac{\alpha}{r}
$$
Which is the case for the gravitational and Coulomb forces (for two opposite charges). In this case, it works out that $\omega _\text{perturbation}=\omega _\text{orbit}$. Visually, this means that the orbits resemble an ellipse, possessing a perihelion and aphelion.
# Kepler's laws
1. The orbit of a planet is an ellipse with the Sun at one of the two foci.
2. A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.
3. The square of a planet's orbital period is proportional to the cube of the length of the semi-major axis of its orbit
## Kepler's second law
Derived from the conservation of angular momentum. Applied to any central force.
![[Pasted image 20260411231937.png]]
The area swept that subtends the angle $d\theta$ during $dt$ is,
$$
dA = \frac{r(rd\theta)}{2}
$$
For $dt\to 0$.Therefore,
$$
\frac{dA}{dt} = \frac{1}{2} r^{2}\dot{\theta} = \frac{L}{2m}
$$
Which is constant when $L$ is constant or conserved.
## Kepler's first law
Beyond here, it is convenient to introduce the quantity:
$$
h=\frac{L}{m} = r^{2}\dot{\theta}
$$
Where $h$ is called the specific angular momentum.
### The Binet equations
In polar coordinates,
$$
\vec{v}=\dot{r}\hat{r} + r\dot{\theta} \hat{\theta} \implies  v^{2}=\dot{r}^{2}+r^{2}\dot{\theta}^{2}
$$
By conservation of angular momentum we also have,
$$
\dot{\theta}=\frac{h}{r^{2}} = hy^{2}
$$
Where $y=r^{-1}$. Furthermore,
$$
\dot{r} = \frac{dr}{dt} = -h \frac{dy}{d\theta}
$$
Combining what we have the first Binet equation:
$$
v^{2} = h^{2}\left[ \left( \frac{dy}{d\theta} \right)^{2}+y^{2} \right]
$$
Furthermore,
$$
\ddot{r} = -h \frac{d}{dt} \left( \frac{dy}{d\theta} \right) = -h^{2}y^{2} \frac{d^{2}y}{d\theta^{2}}
$$
From which we find the second Binet equation:
$$
a_{r} = \ddot{r} - r\dot{\theta}^{2} = -h^{2}y^{2} \left( \frac{d^{2}y}{d\theta^{2}} +y \right)
$$
### Inverse square forces
Now, assume the force has the form,
$$
F=-\frac{\alpha}{r^{2}} = -\alpha y^{2}
$$
According the Newton's 2nd law, the second Binet equations yields,
$$
a_{r} = \frac{F}{m} \implies  -\frac{\alpha y^{2}}{m} = -h^{2}y^{2} \left( \frac{d^{2}y}{d\theta^{2}} +y \right)
$$
Assume that $y\neq 0$,
$$
\frac{d^{2}y}{d\theta^{2}} +y = \frac{\alpha}{mh^{2}} = \frac{m\alpha}{L^{2}} = \frac{1}{r_{0}}
$$
Recalling that $r_{0}=L^{2} /m\alpha$ for forces of this form. This ODE we obtain is similar to SHO with a constant driving force. The solution is,
$$
y = \frac{1}{r_{0}} + A \cos(\theta+\phi) = \frac{1+e\cos(\theta+\phi)}{r_{0}}
$$
Where we have defined $e=r_{0}A$
- Why would we choose $e$ as the variable??

Using polar coordinate system such that $\phi=0$ this becomes,
$$
r=\frac{r_{0}}{1+e\cos\theta}
$$
When $\theta=0$, $\dot{r}=0$ and the energy is,
$$
E = \frac{L^{2}}{2mr^{2}_{m}} - \frac{\alpha}{r_{m}} = \frac{L^{2}}{2mr_{0}^{2}}(1+e)^{2} - \frac{\alpha}{r_{0}}(1+e)
$$Using the fact that,
$$
\frac{L^{2}}{mr_{0}^{2}} = \frac{\alpha}{r_{0}} = \frac{m\alpha^{2}}{L^{2}}
$$
Therefore,
$$
E = \frac{m\alpha^{2}}{2L^{2}}(e^{2}-1) \implies  e = \sqrt{ 1+\frac{2EL^{2}}{m\alpha^{2}} }
$$
Assuming that $e>0$.
### Three types of orbits
Since, by definition, we have that $U\to 0$ when $r\to \infty$:
- $E>0$ means that infinitely far away, the particle will have some kinetic energy
- $E<0$ means the particle's motion is bounded to a potential well
- $E=0$ is the separatrix
![[Pasted image 20260411235230.png]]
A depiction of the energy as a phase plot.

We see the circular orbit at $r=r_{0}$ and $\dot{r}=0$ marked by a yellow cross, which corresponds to the minimum energy possible. The closed orbits are inside the green, dashed, $E=0$ separatrix, and the unbounded orbits outside of the separatrix. The separatrix goes on forever in the $r\to \infty$ direction.

Along the $\dot{r}=0$ axis,
$$
E = \frac{L^{2}}{2mr^{2}} -\frac{\alpha}{r}
$$
The trajectory at this point corresponds with a parabola in $(r, \theta)$ space.

Importantly, the equation for the radius:
$$
r=\frac{r_{0}}{1+e\cos\theta}
$$
Is also the equation for a conic section, where $e$ is the eccentricity, and $r_{0}$ is the semi-latus rectum, often denoted $l$.
![[Pasted image 20260412000141.png]]
In the case when $e>1$ we have,
$$
E = \frac{m\alpha^{2}}{2L^{2}}(e^{2}-1)>0
$$
And the shape of the section is a hyperbola. There is a minimum distance, but there is no maximum distance; the trajectories are unbounded.
- I don't really get the specifics of this section
![[Pasted image 20260412000500.png]]

When $e=1$, $E=0$. The trajectories form unbounded parabolas.

These physically correspond with an object starting off at some infinitely far point, getting attracted to the Sun, and slingshotting once around the Sun before being sent infinitely far away again.
![[Pasted image 20260412002452.png]]

When $e<1$, $E<0$, and we have ellipses. This is the case of most interest, and and the case where Kepler's first law applies. The radius is bounded by:
$$
\frac{r_{0}}{1+e} \leq  r \leq  \frac{r_{0}}{1-e}
$$

This case also includes the circular orbit case where $e=0$ and,
$$
E=-\frac{m\alpha^{2}}{2L^{2}}
$$
Which is typically the case covered previously with a circular orbit and some small perturbations. However, we now see that the perturbations need not be small after all.
## Kepler's third law
This law applies in the elliptical case only.

Mathematically, this law claims that,
$$
\frac{T^{2}}{a^{3}} = \text{Constant}
$$
Where $T$ is the orbital period, and $a$ is the length of the semi-major axis of its orbit.

To begin, we have,
$$
a=\frac{1}{2} \left( \frac{r_{0}}{1+e} + \frac{r_{0}}{1-e} \right) = \frac{r_{0}}{1-e^{2}}
$$
Recall that the area of an ellipse is $A=\pi ab$, where $b$ is the semi-minor axis. With some trigonometry we have,
$$
b = \frac{r_{0}}{\sqrt{ 1-e^{2} }} = \sqrt{ ar_{0} }
$$
The area of this ellipse is therefore $A=\pi \sqrt{ a^{3}r_{0} }$. According to Kepler's second law:
$$
A=\pi \sqrt{ a^{3}r_{0} } = \frac{LT}{2m}
$$
Which tells us that,
$$
\frac{T^{2}}{a^{3}} = \frac{4m^{2}\pi^{2}r_{0}}{L^{2}} = \frac{4m\pi^{2}}{\alpha^{2}}
$$
Where we have used the fact that $r=L^{2} /m\alpha$.

For an object of mass $m$ orbiting another object of mass $M$, $\alpha=GMm$ and therefore,
$$
\frac{T^{2}}{a^{3}} = \frac{4\pi^{2}}{GM}
$$
- Doesn't work for charged particles because $\alpha=-q_{1}q_{2} /4\pi\epsilon_{0}$ is not proportional to $m$
