# The damped, driven pendulum (DDP)
Lets go back to the non-linear pendulum we defined last class and add light damping with coefficient $\gamma$, driven at angular frequency $\omega_{f}$.

The equation of motion becomes,
$$
\ddot{\theta} + 2\gamma\dot{\theta} + \omega_{0}^{2} \sin\theta = \omega_{0}^{2} \beta \cos(\omega_{f}t)
$$
$\beta$ is a measure of hard hard the pendulum is driven.

Now, introduce the equations,
$$
x_{1} = \theta \qquad x_{2} = \dot{\theta} = \dot{x}_{1} \qquad x_{3}=\omega_{f}t
$$
And so the full equation can now be written instead as a system of equations,
$$
\begin{align}
\dot{x}_{1} & = x_{2} \\
\dot{x}_{2} & = -2\gamma x_{2} - \omega_{0}^{2}\sin x_{1} + \beta \omega_{0}^{2} \cos x_{3} \\
\dot{x}_{3} & = \omega_{f}
\end{align}
$$
## Poincaré sections
To make it easier to represent 3D sections, we can wrap the periodic axes. We will wrap $\theta$ and $\omega_{ft}$, both at $2\pi$.

This results in an interesting image where our object might phase and loop through the system at several points in time or space.
![[Pasted image 20260307193711.png]]
Notice how the movement from the red line loops at the cross, and at the empty circle.

A Poincare section is simply a single slice of this plane, at a single point in time. For the example above, the Poincare section results in just two dots.

Note that a perfectly periodic system would be represented as just a single dot.
# Numerical experiments
We have a system with natural oscillation frequency $\omega_{0}\approx 3.1$ Now, we will apply some damping $\gamma=\omega_{0} /4$ or $Q=4$ and forcing angular frequency $\omega_{f}=2\omega_{0} /3$.

From here, we gradually increase the forcing from small $\beta$ to larger amplitudes.

For each $\beta$ we will plot:
- Time series $\theta /\pi$ as a function of $t /T_{f}$
- $(\theta /\pi), \dot{\theta} /\pi \omega_{f}$ phase plots
- $\theta_{n}(\omega)$ Fourier coefficients
- Poincare sections

Starting with a small amplitude $\beta=0.2$ the time series reveals a relatively periodic solution without chaos. There is just some transient behaviour at the beginning of the series.
![[Pasted image 20260307194913.png]]
![[Pasted image 20260307194922.png]]
The phase plot reveals how eventually the pendulum settles into a periodic steady-state.
- The black dots are closer to the end of numerical integration
- The red line is the separatrix

Notice that this system has an *attractor*. As $t\to \infty$ the trajectory is attracting to the black ellipse in the centre. This is called a *line attractor*.

In the undriven, damped oscillator, there is a *point attractor* at $(0, 0)$

In the DDP, this attractor is a *single-period limit cycle*. After every period, the motion completes one full ellipse.
![[Pasted image 20260307195458.png]]
As we might expect, the Fourier coefficients are dominated by the peak at $\omega=\omega_{f}$.

![[Pasted image 20260307195531.png]]
The Poincare section is a dot, telling us that this system is very periodic
- We haven't captured the transient behaviour because only one dot is plotted every forcing period
- The Poincare section acts as a superharmonic filter. That is, we cannot see the superharmonic at $3\omega_{f}$ seen in the Fourier coefficients. We would need to plot every $T_{f} /3$ to see it.
# Approach to chaos for the DDP
A little less than required for chaos, we try $\beta=1.07$.
![[Pasted image 20260307201801.png]]
The time series now has two-cycle periodicity, that is, there are two minima in the system.

![[Pasted image 20260307201847.png]]
The Fourier plot reveals a slew of superharmonics, and now a few subharmonics as well.
![[Pasted image 20260307201929.png]]
The full cycle now appears to be split in two, but it's still closed and periodic. So, there are two characteristic periods present here. The time taken to cover an angle $2\pi$ around the graph $T_{f}$, and the time taken to go back to the initial position, $2T_{f}$.

![[Pasted image 20260307202201.png]]
The Poincare section now has two dots. The first period is the time taken to go from one dot to the other, and the second is the time it takes to return to the same dot.

Now, we set $\beta=1.077$. With initial position $(\theta_{0}, \dot{\theta}_{0})=(-\pi /2), 0$, the same as before, there is not much that changes in the system. However, swap the initial position from $-\pi /2$ to 0 and chaotic behaviour begins to show.
![[Pasted image 20260307202552.png]]
![[Pasted image 20260307202558.png]]
The phase plot reveals that the pendulum goes over the top, and then alternates between two potential wells.
![[Pasted image 20260307202706.png]]
The Poincare section has three dots, telling us that a three-period cycle is present in this system.

So, why was there such a significant difference upon changing the initial conditions?

In 3D, with high enough non-linearity, the phase space is separated into "basins of attraction": if the dynamics starts in one of these "basins", and if the driving isn't so high that it forces the system to cross basin boundaries, it will remain in it. By changing the initial condition, we change which basin of attraction we start in.
- The damping makes the trajectories fall into the centres of the basins, resulting in attractors, while the driving kicks them out
# Chaos
In this system, chaos occurs when $\beta=1.2$.
![[Pasted image 20260307220434.png]]
![[Pasted image 20260307220442.png]]
Notice how the pendulum clearly goes over the top a number of times, but now displays no signs of periodicity. This is a hallmark of chaos.

![[Pasted image 20260307220530.png]]
The Fourier spectrum shows us that the periodicity from the driving is still there, but a whole slew of other frequencies are present.

There are a number of superharmonics present, most of the them aren't multiples of $\omega_{f}$. The subharmonics are very prevalent here, indicating that long-term motions, like drifts between potential wells, have taken much more importance.

![[Pasted image 20260307220612.png]]
