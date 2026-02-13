# General definitions related to Fourier series
Recall we wanted to break a square wave into a summation of sines and cosines with Fourier series. Something like:
$$
F(t) = \frac{A_{0}}{2} \sum_{n=1}^{\infty} [A_{n} \cos(\omega_{n}t) + B_{n} \sin(\omega_{n}t)] \qquad \omega_{n} = \frac{2\pi n}{T}
$$
One can prove that the Fourier series for some function always exists, and is unique.

Recall that we solve for the coefficients with:
$$
A_{n} = \frac{2}{T} \int_{0}^{T} F(t)\cos(\omega_{n}t) \, dt \qquad B_{n} = \frac{2}{T} \int_{0}^{T} F(t)\sin(\omega_{n}t) \, dt
$$
- The interval can be any interval $T$ in length. $-T /2$ to $T /2$ also works.
# Orthogonality of Fourier modes
Define the inner product,
$$
f\cdot g = \frac{2}{T} \int_{-T /2}^{T /2} f(t)g(t) \, dt
$$
We have used the definition including the normalization factor $2 /T$. Which helps to keep the sine and cosine functions neat. Recall the orthogonality of the sine and cosine functions:
$$
\begin{align}
\sin(\omega_{m}t) \cdot \sin(\omega_{n}t) &= \delta_{mn} \\
\cos(\omega_{m}t) \cdot \cos(\omega_{n}t) &= \delta_{mn} \\
\sin(\omega_{m}t) \cdot \cos(\omega_{n}t) &= 0
\end{align}
$$
Where $\delta_{mn}$ is the familiar Kronecker delta,
$$
\delta_{mn} = \begin{cases}
1 & m=n \\
0 & \text{otherwise}
\end{cases}
$$
![[Pasted image 20260211160043.png]]
A graphical visualization of the orthogonality relations between two sine functions
# Simplifications related to function parity
For odd functions, $F(-t)=-F(t)$
$$
A_{n}=0 \qquad F(t) = \sum_{n=1}^{\infty} B_{n}\sin(\omega_{n}t)
$$
Because cosine is an even function. Furthermore, since the product of two odd numbers is always even, we need only compute the coefficient over half the interval, and multiply the result by 2,
$$
B_{n} = \frac{4}{T} \int_{0}^{T /2} F(t)\sin(\omega_{n}t) \, dt
$$
For even functions, $F(-t)=F(t)$,
$$
B_{n} = 0 \qquad F(t) = \frac{A_{0}}{2} + \sum_{n=1}^{\infty} A_{n} \cos(\omega_{n}t)
$$
And,
$$
A_{n} = \frac{4}{T} \int_{0}^{T /2} F(t) \cos(\omega_{n}t) \, dt
$$
# General principles of energy conservation
Consider a force that is a function of $x$,
$$
F(x) = ma = m \frac{dv}{dt}
$$
Which recall we solved using separation of variables:
$$
m \int_{v_{0}}^{v} v' \, dv' = \int_{x_{0}}^{x} F(x') \, dx'
$$
Define a few function,
$$
F(x) = -\frac{dU}{dx}
$$
Such that,
$$
U(x) = - \int_{x_{0}}^{x} F(x') \, dx' + U_{0}
$$
Substitute into our previous equation to find,
$$
\frac{1}{2} mv^{2} + U(x) = \frac{1}{2} mv_{0}^{2} + U_{0}
$$
Which is our expression of the conservation of energy.

We define the mechanical energy to be:
$$
E = \frac{1}{2} mv^{2} + U(x) = K(\dot{x}) + U(x)
$$
Where $U$ is the potential energy, and $K$ is the kinetic energy.

Now, consider the derivative of the kinetic energy,
$$
\frac{dK}{dt} = \frac{1}{2}m \frac{d}{dt} v^{2} = mv \frac{dv}{dt} = F(x, v, t)v
$$
Multiply both sides by $dt$,
$$
dK = F(x, v, t) v \, dt = F(x, v, t) \, dx
$$
Therefore we have,
$$
\Delta K = \int_{x_{1}}^{x_{2}} F(x, v, t) \, dx = W_{1\to  2}
$$
Which is the work-energy theorem.

The definition of a conservative force is that work done between $x_{1}$ and $x_{2}$ is agnostic to the path and time taken to move from $x_{1}$ to $x_{2}$. This applies exclusively to forces that depend only on position.
- Note that this property holds exclusively in 1-D
# Work
In 3-D, the kinetic energy changes in time like:
$$
\frac{dK}{dt} = \vec{F}\cdot \vec{v}
$$
Now multiply both sides by $dt$ to find,
$$
dK = \vec{F}\cdot \vec{v} \, dt = \vec{F} \cdot d\vec{r} = \delta W
$$
Which is the infinitesimal work done by a force $\vec{F}$ on an object during some displacement $d\vec{r}$. Notably, this tells us that if $\vec{F}$ and $d\vec{r}$ point in the same direction, the work is positive.

The total kinetic energy during some motion is,
$$
\Delta K = W = \int_{\vec{r}_{0}}^{\vec{r}} \vec{F}\cdot d\vec{r}'
$$
Which is the work-KE theorem.
- Recall that this is a line integral. The value of this integral is not agnostic to the path taken
## Potential energy and conservative forces
Picture some mass $m$ going from $\vec{r}_{1}$ to $\vec{r}_{2}$, with some initial kinetic energy $K_{1}$ and final kinetic energy $K_{2}$. Assume that this mass is subjected to a single force, which is responsible for some amount of work such that,
$$
K_{2} - K_{1} = W_{1\to 2}
$$
We would like to find forces that conserve the mechanical energy:
$$
E = K_{1}+U_{1} = K_{2}+U_{2} = \text{constant}
$$
It turns out that this is the case when the force can be written with respect to some potential:
$$
\vec{F} = -\vec{\nabla}U
$$
Which is notated as $U$ because it is identical to the potential energy. Applying the gradient related theorems, we have,
$$
W = \int_{\vec{r}_{1}}^{\vec{r}_{2}} \vec{F}\cdot d\vec{r} = \int_{\vec{r}_{1}}^{\vec{r}_{2}} -\vec{\nabla}U \cdot d\vec{r} = - U(\vec{r}_{2}) + U(\vec{r}_{1})
$$
In summary, this means that when $\vec{F}=-\vec{\nabla}U$ for some potential $U$, than the line integral is path independent and the force is conservative.

Note that if energy in the system is conserved we have,
$$
\Delta K + \Delta U =0 \implies  \Delta K =-\Delta U=W
$$
Which tells us that positive force accelerates a system, and negative work stores potential energy in a system.
# Summary: what makes a force conservative?
The force must depend only on the position $\vec{r}$

The force must also be equal to some $\vec{F}=-\vec{\nabla}U$ where $U$ is some scalar function.

This is drastically simplified in 1-D, where a force need only depend on the position $x$ to be conservative.
# A method to solve problems with energy conservation
Since we have,
$$
\frac{1}{2}m v^{2}=E-U(x)
$$
Where $E$ is constant in the system. Re-arrange to find:
$$
v(x) = \pm \sqrt{ \frac{2}{m} [E-U(x)] } = \dot{x}
$$
Which is a first order ODE that can be solved such that,
$$
t-t_{0} = \pm \int_{x_{0}}^{x} \left( \frac{2}{m}[E - U(x')] \right)^{-1/2} \, dx'
$$
We must take the positive sign here to guarantee $t>t_{0}$. From this statement we can solve for $t(x)$, and possible invert it to find $x(t)$, if the result is easy to work with.
