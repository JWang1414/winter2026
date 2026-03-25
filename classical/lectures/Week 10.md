Lets begin with a system of two masses and three springs.
![[Pasted image 20260324211218.png]]
Recall that this is a problem from tutorial. The equations modelling this system are:
$$
m\ddot{x}_{A} = kx_{A} + k(x_{B}-x_{A}) = kx_{B} - 2kx_{A}
$$
$$
m\ddot{x}_{B} = -k(x_{B}-x_{A}) -kx_{B} = kx_{A} -2kx_{B}
$$
Simplify this system by dividing through with $m$,
$$
\ddot{x}_{A} = \omega^{2}_{s} (x_{B} - 2x_{A})
$$
$$
\ddot{x}_{B} = \omega^{2}_{s} (x_{A} - 2x_{B})
$$
Where we have defined $\omega^{2}_{s}=k /m$. To find the normal modes of the system, we will look for solutions of the form $\vec{X}=C\vec{Y}\cos(\omega t+\phi)$.

Substituting in this vector yields the system,
$$
\begin{align}
\omega^{2}_{s} (2x_{A}-x_{B}) & = \omega^{2}x_{A} \\
\omega^{2}_{s}(2x_{B}-x_{A}) & = \omega^{2}x_{B}
\end{align}
$$
If we define,
$$
M^{-1}K = \omega^{2}_{s} \begin{bmatrix}
2 & -1 \\
-1 & 2
\end{bmatrix}
$$
Then the above system can be written as $M^{-1}K\vec{X}=\omega^{2}\vec{X}$. And we can solve for the eigenvalues with,
$$
\det(M^{-1}K-\omega^{2}I_{2}) =0
$$
Skipping through the algebra, the solutions are $\omega_{1}=\omega_{s}$ and $\omega_{2}=\sqrt{ 3 }\omega_{s}$.

If we define $\vec{Y}=\begin{bmatrix}a & b\end{bmatrix}$ and substitute $a=x_{A}$ and $b=x_{B}$ in the system of equations, we find that for $\omega=\omega_{s}$ $a=b=1 /\sqrt{ 2 }$ and when $\omega=\sqrt{ 3 }\omega_{s}$ we have $a=-b$.

These two components make up $\vec{Y}_{n}$, and the two eigenvectors are orthogonal to each other. Combining everything together, the solution to the coupled oscillator system is,
$$
\vec{X} = \frac{C_{1}}{\sqrt{ 2 }} \begin{bmatrix}
1 \\
1
\end{bmatrix} \cos(\omega _{s}t+\phi_{1}) + \frac{C_{2}}{\sqrt{ 2 }} \begin{bmatrix}
1 \\
-1
\end{bmatrix} \cos(\sqrt{ 3 }\omega_{s}t+\phi_{2})
$$
# $N$ masses and $N+1$ springs
Here, we can simply repeat the exact same methods used in the case with two masses. The problem is largely symmetrical and so easily expands into the case with $N$ masses.

- There is a lot of Python output here. Look at the lecture notes for this.

- The points on the string of masses that do not move are the nodes. Two nodes are separated by half a wavelength.
- Between the nodes are the anti-nodes, where the movement is greatest.
- The larger the mode number, or frequency, the more nodes there are. This is a general feature of standing waves
- Modes with more nodes are called higher modes, and less nodes low modes or grave modes. This arises from sound waves, there "grave" corresponds with lower frequency.
# The continuum approximation
We expect that for more modes, the behaviour will begin to more closely resemble a string.

Imagine we have $N\gg 1$ masses aligned over some distance $L$. The distance between masses is:
$$
a = \frac{L}{N+1} \ll L
$$
Lets define a few variables.
- $x$ is the total distance from the beginning of the chain
- $x_{n}(t)$ is the total distance of mass $n$ from the beginning of the chain
- $x_{n_{0}}=na$ is the rest position of mass $n$
- $y_{n}(t)=x_{n}(t)=x_{n_{0}}$ is the derivation from rest position.

Applying our knowledge of the forces along the chain, the equation of motion for some mass in the chain will be,
$$
\ddot{y}_{n} = \frac{k}{m} (y_{n+1} - 2y_{n} + y_{n-1})
$$
In physical contexts, the wavelength is typically far larger than $a$. Consecutive $y_{n}$'s are very close to each other, and so we can use Taylor expansions to claim,
$$
y_{n\pm 1}(t) = y(x_{n_{0}}\pm a, t)\approx y(x_{n_{0}}, t) \pm a \frac{ \partial y }{ \partial x } \bigg|_{x=x_{n_{0}}} + \frac{a^{2}}{2} \frac{ \partial^{2}y }{ \partial x^{2} } \bigg|_{x=x_{n_{0}}}
$$
Where $y(x_{n_{0}}, t)$ is a function that tell us how far a mass is from its rest position.

If we substitute this Taylor series into our equation of motion we will find that,
$$
\ddot{y}_{n} \approx \frac{ka^{2}}{m} \frac{ \partial^{2}y }{ \partial x^{2} } \bigg|_{x=x_{n_{0}}} = \frac{\sigma}{\mu}  \frac{ \partial^{2}y }{ \partial x^{2} } \bigg|_{x=x_{n_{0}}}
$$
Where we have defined the mass density of the medium $\mu=m /a$ and "stretchiness modulus" of the chain $\sigma=ka$.

In the case where $N\to \infty$, we can treat all $x$ as the resting position of a mass, therefore:
$$
x_{n_{0}} \to  x \qquad y_{n}(t) \to y(x, t)
$$
Which results in the canonical wave equation,
$$
\frac{ \partial^{2}y }{ \partial y^{2} } -v^{2} \frac{ \partial^{2}y }{ \partial x^{2} } =0
$$
Where in this case $v^{2}=\sigma /\mu$.
- $v$ is called the phase speed of the waves
