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

Chaos refers to the irregularity or unpredictability of certain motions. This unpredictability arises not because we do not understand the equations governing the system, but because the solutions cannot be predicted long in advance. This is called *deterministic chaos*.

The defining feature of chaotic systems is their sensitivity to initial conditions.

There is, however, a difference between *stochastic* and chaotic processes.
![[Pasted image 20260308134639.png]]
Notice that stochastic processes are not deterministic, because their behaviour is governed by random processes. Brownian motion, for example, is stochastic and unpredictable, but not chaotic.

Traditionally there are two types of chaotic systems.
- Hamiltonian systems, where mechanical energy is conserved. The system remembers its initial conditions, and the dynamics does not feature attractors.
- Dissipative-driven systems. Dynamics have attractors, and the initial conditions are quickly forgotten after the transient phase.
# Requirements for chaos in continuous time systems
Recall that any system of ODEs can be written as a series of first-order ODEs for some defined $x_{n}$. In continuous time systems, there are two conditions for chaos:
- $N\geq 3$
	- So the system of equations needs at least 3 "levels"
- The system is non-linear

Note that these conditions are necessary, but not sufficient. Some non-linear waves have infinite phase-space dimensions, and yet remain predictable.
## Requirements for chaos in the DDP
The equation for motion we defined for the DDP is,
$$
\ddot{\theta} + 2\dot{\gamma}\theta + \omega_{0}^{2}\sin\theta = \omega_{0}^{2}\beta \cos(\omega_{f}t)
$$
This system can be re-written as,
$$
\begin{align}
\dot{x}_{1} & = x_{2} \\
\dot{x}_{2} & = -2\gamma x_{2} - \omega_{0}^{2}\sin x_{1} + \beta \omega_{0}^{2} \cos x_{3} \\
\dot{x}_{3} & = \omega_{f}
\end{align}
$$
Which is a system of three first order equations, and the 2nd one is non-linear. Confirming the possibility of chaos.

Recall the system from last time, the one with $\beta=1.2$. We return to this problem, and integrate it for much longer periods of time. The phase plot turns into a mess of nothing, but the Poincare sections reveal a lot more about the behaviour of the system. Here are a few of them at different points in time:
![[Pasted image 20260308141133.png]]
![[Pasted image 20260308141157.png]]
![[Pasted image 20260308141205.png]]
These reveal to us that there is an attractor in the system, but is has a convoluted 3D structure. Furthermore, it is fuzzier than the limit cycles looking at in the previous lecture. This "fuzziness" is due to a fractal structure within the attractor, and the attractor is called a *strange attractor*.
# Fractal nature of the strange attractor
If we were able to zoom in on the Poincaré section easily, we would notice a complicated layered structure that occupies a compact region of phase space in the Poincaré section.

This is the reason why it's called a strange attractor, it doesn't really have a finite period of cycles.

The attractor has a self-similar structure: reappearance of certain patterns at smaller scales. This is a standard characteristic of a strange attractor. A shape like this is said to have a "fractal dimension".

When you have a strange attractor, your system is chaotic. The attractor is complex enough that you could be at any of an infinite number of points. We cannot measure the initial condition, and nor can we choose some point $(\theta, \dot{\theta})$ to try and derive the initial conditions. This arises because there is always a closer possibility, the fractal nature makes chaotic behaviour inherently unpredictable.
# Quantifying the approach to chaos
## The Feigenbaum number
On its way to chaos, we saw that the system first went into a period-doubling. Had there been more experiments, we could have seen the system progress into more and more doublings.

These period-doubling events, called *bifurcations*, move closer and closer in $\beta$. This is called a *subharmonic cascade*.

There is no way to predict these bifurcations analytically. They must be experimentally analyzed. Using some known values, we find that the bifurcations in our system occur at $\beta_{1}\approx 1.0663$, $\beta_{2}\approx 1.0793$, $\beta_{3}\approx 1.08$, $\beta_{4}\approx 1.0827$. After enough repetitions, you will find,
$$
\beta_{n+1} - \beta_{n} \approx \frac{1}{\delta} (\beta_{n} - \beta_{n-1})
$$
Where $\delta \approx 4.6692016$ is called the *Feigenbaum delta number*.

Now, what happens as $n\to \infty$? Define $\Delta_{n}=\beta_{n+1}-\beta_{n}$:
$$
\Delta_{n+1} = \delta ^{-1}\Delta_{n} = \delta ^{-1} \left( \delta ^{-1} \Delta _{n-1} \right) = \delta^{-n}\Delta_{1}
$$
The total distance from $\beta_{1}$ as $n\to \infty$ is therefore,
$$
\Delta_{1} + \Delta_{2} + \Delta_{3} + \dots = \Delta_{1} + \delta ^{-1} \Delta_{1} + \dots = \sum_{n=0}^{\infty} \delta^{-n}\Delta_{1} = \frac{\Delta_{1}}{1-\delta ^{-1}} \approx 0.16543
$$
Which gives us the critical point where the number of periods diverges to infinity, the threshold for chaos,
$$
\beta_{c} = \beta_{1} + \sum_{n=0}^{\infty} \delta^{-n}\Delta_{1} \approx 1.0829
$$
- Numerous chaotic systems also undergo subharmonic cascades. The progression to chaos is typically also characterized by this Feigenbaum number, or very close
# Bifurcation diagrams
What happens if we increase $\beta$ more? You might think more chaos, but eventually you return to another single period attractor.

$\beta=1.35$ for example, results in the phase plot
![[Pasted image 20260308151411.png]]
The pendulum is now continuously spinning around the top of the pendulum in one direction.

If you once again increase $\beta$ to higher numbers, you will find subharmonic cascades occur again, and discover another chaotic regime.

One method of visualizing this behaviour is by plotting the $\theta$ from your Poincare section as a function of $\beta$. When you have one period, plot one dot, when you have two, plot 2 dots. This is called a bifurcation diagram.

![[Pasted image 20260308151804.png]]
You can make a bifurcation diagram plotting either $\theta$ or $\dot{\theta}$, the shape is similar, but the exact values change.

Over a more restricted range of $\beta$ values, you can more closely see the Feigenbaum number
![[Pasted image 20260308152006.png]]

If you zoom in very close to the lower right split you will see
![[Pasted image 20260308152138.png]]
Something very similar to the fuller version above. Displaying the self-similar structure of the bifurcation diagram.
# Lyapunov exponent
Suppose we have two trajectories with initial values $\theta_{0}^{(1)}$ and $\theta_{0}^{(2)}=\theta_{0}^{(1)}+\epsilon$, everything else is identical. The difference between the two after some time is,
$$
\left| \theta^{(2)}(t) - \theta^{(1)}(t) \right| = \Delta\theta(t) \approx \lvert \epsilon \rvert e^{ \lambda t }
$$
Where $\lambda$ is the Lyapunov exponent.
- We also guess that the growth or decay is exponential

If $\lambda<0$ solutions will converge over time. If $\lambda=0$, the trajectories stay the same distance apart, and if $\lambda>0$ the trajectories will diverge.

We will use the simpler equation,
$$
\ln(\Delta\theta) = \lambda t + \ln \lvert \epsilon \rvert
$$
To solve for the exponent.
## Non-chaotic example
![[Pasted image 20260308152812.png]]
The logarithm decreases more or less linearly. Is it important to note that the stagnation at -35 arises because of machine precision.

Clearly, $\lambda<0$ here, and so the system is not chaotic.
## Chaotic example
![[Pasted image 20260308152957.png]]
The slope here is dirtier, but we can clearly see that it is increasing.

It is this divergence of trajectories that defines the sensitive dependence on initial
conditions. If we don't know the initial condition perfectly (which we can't) then we don't know what trajectory we are on, and hence we don't know where we will be on the strange attractor at some later time.
