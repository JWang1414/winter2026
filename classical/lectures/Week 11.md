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
