Recall that last lecture we delved into the transition from discrete coupled oscillators to continuous waves. Today, we will describe waves on a string.
# The phase speed
The canonical wave equation is:
$$
\frac{ \partial^{2}y }{ \partial t^{2} } -v^{2} \frac{ \partial^{2}y }{ \partial x^{2} } =0
$$
Where $v$ is the phase speed.

In different contexts, $v$ can describe different things. The speed of a transverse wave on a taut string, EM waves in a vacuum, sounds waves, seismic pressure waves etc.

We will swap to waves in a string because they are easy to visualize. In this case we have,
$$
v = \sqrt{ \frac{F}{\mu} }
$$
- $F$ is the tension in the string, to avoid confusion with the period, $T$

Now, imagine the string is forced with a Gaussian pulse of the form,
$$
y(t) = A \exp \left[ -\frac{(t-t_{0})^{2}}{\sigma^{2}_{t}} \right]
$$
If the wave is not dispersive, the pule will retain its shape and the Gaussian function will propagate forward at $v$,
$$
y(x, t) = A \exp\left[ -\left( \frac{x-vt}{\sigma_{x}} \right)^{2} \right]= A\exp \left[ -\left( \frac{t-x /v}{\sigma_{t}} \right)^{2} \right]
$$
- This pulse has a typical spatial width $2\sigma_{x}=2v\sigma_{t}$
![[Pasted image 20260324230028.png]]
Generally speaking, we will interpret $v$ as a constant, as seen in this example.
# Normal modes of the wave equation
Use the initial conditions,
$$
y(x=0)=y(x=L)=0
$$
Recall that to solve the wave equation under these conditions, we can use separation of variables,
$$
y(x, t) = f(x)h(t)
$$
Going through the motions, the solution is the familiar series,
$$
y(x, t) = \sum_{n=1}^{\infty} [\alpha_{n} \cos(\omega_{n}t) + \beta_{n} \sin(\omega_{n}t)] \sin(k_{n}x)
$$
Notes on the resulting motion:
- We have nodes and anti-nodes appearing again
- Node $n=1$ is called the fundamental mode or first harmonic. The next is called the second harmonic and so on.
- $n^{th}$ harmonic has $n-1$ nodes and $n$ anti-nodes

$k_{n}$ is the wave number of the $n^{th}$ mode.
$$
\lambda_{n} = \frac{2\pi}{k_{n}} = \frac{2L}{n}
$$
Where $\lambda_{n}$ is the wavelength of the corresponding wave number.
# Different Boundary Conditions
The force applied from one part of the string to the next is $\vec{F}$ so that $F_{y}=F\sin\theta$. When angles are small we have,
$$
F_{y} \approx F\theta \approx F \tan\theta = F \frac{ \partial y }{ \partial x }
$$
Which yields,
$$
\frac{ \partial y }{ \partial x } \bigg|_{\text{end}} =0
$$
As the boundary condition where the end of the string is attached to nothing.
- Recall that this is a Neumann boundary condition
- A Dirichlet boundary condition is when $y|_{\text{end}}=A$

Going through separation of variables again, you will find that,
$$
f(x) = A \cos(k_{n}x) \qquad k_{n} = \frac{\pi n}{L}
$$
Instead of $\sin(k_{n}x)$.
# Central Forces and Conservation Laws
A force is said to be central if its potential depends only on $r$
$$
\vec{F} = F(r) \hat{r}
$$
Recall that for a force to be conservative we require:
1. $\vec{F}=\vec{F}(\vec{r})$, so the force does not depend on time or velocity
2. $\vec{F}=-\nabla U$, so the force can be expressed as the gradient of a potential

Since our force is central, there is no theta dependence and our function can be written as:
$$
F(r) = -\frac{dU}{dr}
$$
And so we can conclude central forces are conservative.

Integrating $F$, we also find that,
$$
U(r) - U_{0} = - \int_{r_{0}}^{r} F(r') \, dr'
$$
In practice we typically attempt to use an $r_{0}$ such that $U_{0}=0$.
# Rate of change of the mechanical energy
For the kinetic energy,
$$
K = \frac{1}{2} mv^{2} = \frac{1}{2} m\vec{v}\cdot \vec{v} \implies  \dot{K} = \frac{m}{2} (\dot{v}\cdot v+v\cdot \dot{v}) = m\dot{v}\cdot v
$$
Which can be simplified into:
$$
\dot{K} = \vec{F}\cdot \vec{v}
$$
This is true for any force in 3D.

For the potential energy,
$$
\dot{U} = \frac{dU}{dt} = \frac{ \partial U }{ \partial x } \dot{x} + \frac{ \partial U }{ \partial y } \dot{y} + \frac{ \partial U }{ \partial z } \dot{z} = \vec{v}\cdot \nabla U
$$
Since for conservative forces $\vec{F}=-\nabla U$ this becomes,
$$
\dot{U}=-\vec{F}\cdot \vec{v}=-\vec{K} \implies  \dot{E}=0
$$
This is true for any conservative force, and so also true for central forces.
# Central forces conserve angular momentum
Recall the angular momentum is,
$$
\vec{L} = \vec{r}\times \vec{p}
$$
Where $\vec{p}=m\vec{v}$ is the momentum of a particle.

Note that:
- If a particle is subject to only a central force, $\vec{L}$ is conserved
- If $\vec{L}$ is conserved, the plane of motion is fixed

If the plane of motion is fixed, it can be convenient to define the third dimension $\hat{z}=\hat{r}\times\hat{\theta}$ such that $\vec{L}=L\hat{z}$.
# Kinematics and dynamics under conservation of $\vec{L}$
Recall that the force in polar coordinates as:
$$
F_{r} = m(\ddot{r}-r\dot{\theta}^{2}) \qquad F_{\theta} = m(2\dot{r}\dot{\theta}+r \ddot{\theta})
$$
In the case of our central force, these equations simplify into:
$$
m(\ddot{r}-r\dot{\theta}^{2}) = -\frac{dU}{dr} \qquad m(2\dot{r}\dot{\theta}+r \ddot{\theta})=0
$$
This second statement implies the conservation of angular momentum,
$$
\vec{L}=\vec{r}\times p\vec{r} = mr^{2}\dot{\theta}(\hat{r}\times\hat{\theta}) \equiv L\hat{z}
$$
Where we have defined $L=mr^{2}\dot{\theta}$.
# Solving the central force problem
First, we have,
$$
L = mr^{2}\dot{\theta} \implies  \dot{\theta} = \frac{L}{mr^{2}}
$$
Therefore, according to Newton's 2nd law we have,
$$
m(\ddot{r} - r\dot{\theta}^{2}) = - \frac{dU}{dr} \implies  m\ddot{r} = mr\dot{\theta}^{2} - \frac{dU}{dr}
$$
Which, using the previous relation can be written as,
$$
m\ddot{r} = -\frac{dU}{dr} - \frac{d}{dr} \left( \frac{L^{2}}{2mr^{2}} \right) = -\frac{dU_\text{eff}}{dr}
$$
Where we have defined,
$$
U_\text{eff}(r) = U(r) + \frac{L^{2}}{2mr^{2}}
$$
The total conservative energy is now:
$$
E = \frac{1}{2} m\dot{r}^{2} + U_\text{eff}(r)
$$
However, the kinetic energy here has been changed to:
$$
K = \frac{1}{2} mv^{2} + \frac{1}{2} m(v_{r}^{2}+v_{\theta}^{2}) = \frac{1}{2} m \left( \dot{r}^{2}+\frac{L^{2}}{m^{2}r^{2}} \right)
$$
