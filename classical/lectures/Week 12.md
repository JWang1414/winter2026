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
