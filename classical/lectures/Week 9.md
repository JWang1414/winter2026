In this lecture we will develop the transition between simple oscillators and wave behaviour.
# Two Pendulums and a Spring
Two identical masses $m$ hang from two identical pendulums of length $l$. The two masses are connected with a spring of stiffness $k$.
![[Pasted image 20260311100528.png]]
$A$ is the mass on the right, and $B$ is the mass on the left. $x$ will notate the horizontal distances from rest.
## Symmetric Normal Mode
If both masses are initially held still with $x_{A}=x_{B}=C$, then once released both will oscillate at the same natural frequency $\omega_{p}=\sqrt{ g /l }$.

Their oscillation will be in perfect synchronous fashion such that,
$$
x_{A}(t) = x_{B}(t) = C \cos(\omega_{1}t)
$$
And the spring plays no role in the motion. This is called a normal mode, when all elements of the coupled system oscillate at the same frequency.
## Antisymmetric Normal Mode
Alternatively, we might also have initial conditions $x_{A}=-x_{B}=C$, again with no initial velocity. In this case the positions will oscillate perfectly out of phase, with a single angular frequency $\omega_{2}$.

There is no third normal mode, because there are only two degrees of freedom in the system.
# General Derivation
The horizontal angle of the pendulum when $\theta \neq 0$ is $x_{A}=l\sin\theta \approx l\theta$.

The force of tension in the $y$ direction, opposing the force of gravity is,
$$
T_{y} = \lvert \vec{T} \rvert  \cos\theta \approx \lvert \vec{T} \rvert
$$
And the vertical position is,
$$
y = l(1-\cos\theta) \approx \frac{l\theta^{2}}{2}
$$
The vertical acceleration in the $y$ direction is negligible, because we are assuming that the angles are small, so $y$ changes very slowly in comparison to $T$ and $mg$.

We therefore make the approximation,
$$
T_{y} - mg \approx 0 \implies  \lvert \vec{T} \rvert \approx mg
$$
The horizontal projection of the tension is therefore,
$$
-\lvert \vec{T} \rvert \sin\theta \approx -\frac{mgx_{A}}{l}
$$
And the spring force is,
$$
-k(x_{A}-x_{B})
$$
Newton's 2nd law therefore tells us,
$$
m\ddot{x}_{A} = -\frac{mg}{l}x_{A} - k(x_{A}-x_{B})
$$
Which yields the differential equation,
$$
\ddot{x}_{A} + \omega^{2}_{p} x_{A} + \omega_{s}^{2}(x_{A} - x_{B}) =0
$$
Where we have used,
$$
\omega_{p} = \sqrt{ \frac{g}{l} } \qquad \omega_{s} = \sqrt{ \frac{k}{m} }
$$
Which are the natural angular frequencies of the pendulum and the mass A + spring systems, respectively.

By symmetry, we also have that,
$$
\ddot{x}_{B} + \omega^{2}_{p} x_{B} + \omega_{s}^{2}(x_{B} - x_{A}) =0
$$
# Change of variables
This system of coupled ODEs can be solved with the change of variables,
$$
q_{1}=x_{A}+x_{B} \qquad q_{1}=x_{A}-x_{B}
$$
Add and subtract the two coupled ODEs to obtain,
$$
\ddot{q}_{1} + \omega_{p}^{2}q_{1}=0 \qquad \ddot{q}_{2} + (\omega_{p}^{2}+2\omega_{s}^{2})q_{2}=0
$$
In fact, these two quantities correspond to the symmetric and anti-symmetric modes that we found prior.
$$
\omega_{1}=\omega_{p}\qquad \omega_{2}^{2} = \omega_{p}^{2}+2\omega_{s}^{2}
$$
- The modes of oscillation in such a system are no longer simple oscillations. They are a global concept in which all component of one coupled system oscillate in phase, at the same frequency
- The oscillations of each individual component are not independent from each other, but the modes are completely independent. $q_{1}$ doesn't appear in the equation for $q_{2}$, and vice versa.
	- Therefore, in the full system, there are just two modes. They do not exchange momentum so long as the system is linear
- $q_{n}$ are the normal coordinates/modes with respective normal frequencies $\omega_{n}$.
# Independence of the Modes
The two modes are both solutions to difference SHO equations with the expressions,
$$
q_{1}=C_{1} \cos(\omega_{1}t+\phi_{1}) \qquad q_{2}=C_{2} \cos(\omega_{2}t+\phi_{2})
$$
Which in physical coordinates is,
$$
x_{A} = \frac{q_{1}+q_{2}}{2} \qquad x_{B} = \frac{q_{1}-q_{2}}{2}
$$
So any motion is a linear superposition of the two modes.
## Energetic independence of the modes
The kinetic energy, and potential energy from gravity are,
$$
K_{A, B} = \frac{1}{2} m (\dot{x}_{A, B})^{2} \qquad U^{(g)}_{A, B} = \frac{1}{2} m\omega_{p}^{2} x_{A, B}^{2}
$$
And the energy stored in the spring is,
$$
U^{(s)} = \frac{1}{2} k(x_{A} - x_{B})^{2} = \frac{1}{2} m\omega^{2}_{s} (x_{A} - x_{B})^{2}
$$
So the total energy in the system is,
$$
E = K_{A, B} + U^{(g)}_{A, B} + U^{(s)} = E_{1}+E_{2}
$$
Where the subscript $A, B$ terms represent the sum of the energy in $A$ and $B$.

The representations for $E_{1}$ and $E_{2}$ are,
$$
E_{n} = \frac{1}{4} m\left[ \dot{q}_{n}^{2} + \omega_{n}^{2}q_{n}^{2} \right]
$$
Notice that each reservoir of energy $E_{n}$ is uncoupled from each other, and so there is no exchange of energy from one mode of motion to the other. This is true for any system of coupled oscillators, as long as the linear model is valid.
# Beating Phenomenon
When $\omega_{1}\approx \omega_{2}$, we observe beating in the physical space for each mass position.

If we choose the initial conditions $C_{1}=C_{2}=C$ and $\phi_{1}=\phi_{2}=0$ we obtain the configuration,
$$
x_{A} = C \cos(\Omega t) \cos(\Delta \omega t) \qquad x_{B} = C \sin(\Omega t) \sin(\Delta \omega t)
$$
Where,
$$
\Delta \omega = \frac{1}{2} (\omega_{2}-\omega_{1}) \qquad \Omega = \frac{1}{2} (\omega_{1}+\omega_{2})
$$
If $\lvert \Delta \omega \rvert\ll \Omega$ then we observe:
![[Pasted image 20260311110125.png]]
Notice the characteristic beating in the oscillation amplitude of $x_{A}$.
# Introduction to Matrix Equations
We will be going back to our example with the coupled oscillators,
$$
\begin{align}
m\ddot{x}_{A} + \frac{mg}{l} x_{A} + k(x_{A} - x_{B})  & =0 \\
m\ddot{x}_{B} + \frac{mg}{l} x_{B} + k(x_{B} - x_{A})  & =0
\end{align}
$$
Where, in this system, we have the natural angular frequency of the pendulum $\omega_{p}$ and of each mass $\omega_{s}$ defined like so:
$$
\omega_{p} = \sqrt{ \frac{g}{l} } \qquad \omega_{s} = \sqrt{ \frac{k}{m} }
$$
We will be using some general results from linear algebra here. Recall that the eigenvalues can be found using the equation:
$$
\det(A-\lambda I_{n})=0
$$
Where $\lambda$ are the eigenvalues and $I_{n}$ is the $n$ dimensional identity.

If there are $n$ unique eigenvalues, then the matrix is diagonalizable, and the set of eigenvectors forms a basis for the space of solutions,
$$
\sum_{i=1}^{n} a_{i}\vec{V}_{i} = \vec{X}
$$
If a matrix $A$ is real symmetric, so $A=A^{T}$ and all elements of $A$ are real, then if two eigenvectors are associated with distinct eigenvalues, then they are also orthogonal vectors.
# Coupled pendulums
Lets define our problem in matrix form. Define the state vector,
$$
\vec{X} = \begin{bmatrix}
x_{A} \\
x_{B}
\end{bmatrix}
$$
Which contains the positions of each mass. Now, define the matrices,
$$
M = \begin{bmatrix}
m & 0 \\
0 & m
\end{bmatrix} \qquad K = \begin{bmatrix}
\frac{mg}{l}+k & -k \\
-k & \frac{mg}{l}+k
\end{bmatrix}
$$
Which gives us,
$$
M \ddot{\vec{X}} + K\vec{X} = \begin{bmatrix}
m\ddot{x}_{A} + \frac{mg}{l} x_{A} + k(x_{A} - x_{B}) \\
m\ddot{x}_{B} + \frac{mg}{l} x_{B} + k(x_{B} - x_{A})
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix}
$$
We will solve this using the adopt an exponential method.
$$
\vec{Z} = \vec{Z}_{0} e^{ i\omega t } \qquad \vec{Z}_{0} \in \mathbb{C}^{2}, \omega \in \mathbb{R}
$$
Then,
$$
M \ddot{\vec{X}} + K\vec{X} = M \ddot{\vec{Z}} + K\vec{Z} = M(-\omega^{2}) \vec{Z} + K\vec{Z} = (K-\omega^{2}M)\vec{Z}=0
$$
So,
$$
K\vec{Z} = \omega^{2}M\vec{Z} \implies  M^{-1}K\vec{Z} = \omega^{2}\vec{Z}
$$
Recall that a matrix equation $RV=0$ has non-trivial solutions iff $\det \{ R \}=0$.

Hence, we would like to have,
$$
\det(K-\omega^{2}M)=0
$$
If you go through the algebra this yields,
$$
m^{2} [(\omega^{2}_{p} - \omega^{2})(\omega^{2}_{p}+2\omega^{2}_{s}-\omega^{2})] =0
$$
Yielding the two roots,
$$
\omega = \omega_{p}, \sqrt{ \omega^{2}_{p}+2\omega^{2}_{s} }
$$
The same roots that we found last time.

Now, we are interested in using the initial conditions to solve for,
$$
\vec{Z}_{0} = \vec{C}e^{ i\phi }
$$
To make finding $\vec{C}$ easier, split it into $C\vec{Y}$ where $C$ is the scalar amplitude and $\vec{Y}$ now has norm 1.

Substituting this into the system we have,
$$
(K-\omega^{2}M)\vec{Z} = C(K-\omega^{2}M)\vec{Y} e^{ i(\omega t+\phi) } =0 \implies  (K-\omega^{2}M)\vec{Y} =0
$$
Let,
$$
\vec{Y}= \begin{bmatrix}
a \\
b
\end{bmatrix} \qquad \sqrt{ a^{2}+b^{2} }=1
$$
Going through the algebra you should find,
$$
(K-\omega^{2}M)\vec{Y} = \begin{bmatrix}
m[(\omega^{2}_{p}+\omega^{2}_{s}-\omega^{2})a-\omega^{2}_{s}b] \\
m[-\omega^{2}_{s}a+(\omega^{2}_{p}+\omega^{2}_{s}-\omega^{2})b]
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix}
$$
In the case where $\omega^{2}=\omega_{1}^{2}=\omega^{2}_{p}$ we have,
$$
\begin{bmatrix}
ka-kb \\
-ka+kb
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix} \implies  a=b
$$
Hence,
$$
\sqrt{ a^{2}+b^{2} } =1 \implies  a=b=\frac{1}{\sqrt{ 2 }}
$$
If you do the same, but in the other case where $\omega^{2}=\omega_{2}^{2}=\omega^{2}_{p}+2\omega^{2}_{s}$ then you will find,
$$
-\omega^{2}_{s}(a+b)=0 \implies  a=-b = \frac{1}{\sqrt{ 2 }}
$$
# Eigenvectors as a basis for all the solutions
So far we have:
- $\vec{Y}_{1}$ and $\vec{Y}_{2}$ as eigenvectors for the matrix problem
- $\omega_{1}^{2}$ and $\omega_{2}^{2}$ as the eigenvalues or normal angular frequencies
- $\vec{X}_{1}=\mathrm{Re}\{ \vec{Z}_{1} \}$ and $\vec{X}_{2}=\mathrm{Re}\{ \vec{Z}_{2} \}$ as the eigenmodes of oscillation, or normal modes

Going back to earlier, two eigenvectors form a basis for all vectors. That is, all solutions can be written as,
$$
\vec{X} = C_{1}\vec{Y}_{1} \cos(\omega_{1}t+\phi_{1}) + C_{2}\vec{Y}_{2} \cos(\omega_{2}t + \phi_{2})
$$
And the velocity is of course the derivative of $\vec{X}$
# Amplitudes and phases
A useful trick to note is that, since $(K-\omega^{2}M)=(K-\omega^{2}M)^{T}$, we have:
$$
\vec{Y}_{n} \cdot \vec{Y}_{m} = \delta_{nm}
$$
Where $\delta_{nm}$ is the Kronecker delta.

Therefore, for any set of initial conditions $\vec{X}_{0}$ and $\vec{V}_{0}$ you can find the amplitude and phase of each mode and dotting with $\vec{Y}_{n}$.

For example,
$$
\vec{X}(t=0) \cdot \vec{Y}_{1} = C_{1} \vec{Y}_{1}\cdot \vec{Y}_{1} \cos(\phi_{1}) + C_{2} \vec{Y}_{2}\cdot \vec{Y}_{1} \cos(\phi_{2}) = \frac{1}{\sqrt{ 2 }} (x_{A_{0}} + x_{B_{0}})
$$
$$
\vec{V}(t=0)\cdot \vec{Y}_{1} = -\omega_{1}C_{1} \sin(\phi_{1}) = \frac{1}{\sqrt{ 2 }} (v_{A_{0}}+v_{B_{0}})
$$
Repeat with $\vec{Y}_{2}$ and you obtain a system of 4 equations, which you should be able to solve.

---
Example
Imagine the masses held and released from symmetric and antisymmetric initial positions. Both velocities are zero, and so $\phi_{1}=\phi_{2}=0$.

Now, lets say $x_{A_{0}}=x_{B_{0}}=D$. So we have the symmetric mode. The initial conditions are,
$$
\vec{X}_{0}=\begin{bmatrix}
x_{A}(t=0) \\
x_{B}(t=0)
\end{bmatrix} = \begin{bmatrix}
D \\
D
\end{bmatrix} = \sqrt{ 2 } D\vec{Y}_{1} + 0 \vec{Y}_{2}
$$
So the antisymmetric mode is zero, as we would expect.

What if $x_{A_{0}}=-x_{B_{0}}=D$? Well then,
$$
\vec{X}_{0} = \begin{bmatrix}
D \\
-D
\end{bmatrix} = 0 \vec{Y}_{1} + \sqrt{ 2 }D \vec{Y}_{2}
$$
So the symmetric mode is zero.

---
