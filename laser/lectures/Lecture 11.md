- Online lecture.
# Cavity Ray Stability
![[Pasted image 20260228161819.png]]
Notice how the cavity with the flat mirrors is unstable, if the ray is off centre it will eventually leave.

Our analysis of cavity stability will consider a beam originating from the centre of a cavity, propagating towards one mirror, bouncing off, reaching the other mirror, bouncing off, and the propagating back to the middle of the cavity.

The points of interest are highlighted in this diagram:
![[Pasted image 20260228162442.png]]

The series of ABCD matrices for this system looks like:
$$
M = \begin{bmatrix}
1 & L /2 \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-2 /R & 1
\end{bmatrix} \begin{bmatrix}
1 & L \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-2 /R & 1
\end{bmatrix} \begin{bmatrix}
1 & L /2 \\
0 & 1
\end{bmatrix}
$$
The values in the matrix according to:
$$
M = \begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
$$
Are:
$$
\begin{align}
A & = D = \frac{2L^{2}-4LR-R^{2}}{R^{2}} \\
B & = -\frac{L(2R-L)(L-R)}{R^{2}} \\
C & = \frac{4(L-R)}{R^{2}} \\
\end{align}
$$
Notice that this models just a single pass through the cavity. Therefore, we are interested in the case $M^{N}$ where $N$ is the number of passes through the cavity.

Our goal to accomplish this is to diagonalize $M$, and than analyze the eigenvalues $\lambda_{\pm}$. For the system to be stable, we want $\lambda^{N}_{\pm}$ to be finite as $N\to \infty$, and so we would like $\lambda_{\pm}<1$.

However, recall that if we have a system with no index changes $\det \{ M \}=1$ and therefore we also have $\det \{ M \} = \lambda_{+}\lambda_{-}$. So, the only compatible value for both eigenvalues is 1.
$$
\lvert \lambda_{+} \rvert = \lvert \lambda_{-} \rvert =1
$$
Since the magnitude must be 1, we will express the two eigenvalues in the polar complex form,
$$
\lambda_{+}=e^{ i\phi } \qquad \lambda_{-} = e^{ -i\phi }
$$
This is true because,
$$
\lambda_{+}\lambda_{-} = 1 \implies  \lambda_{+} = \frac{1}{\lambda_{-}}
$$
So now, lets relate the stability criteria we found to the physical characteristics of the cavity. That is, the length and radius of curvature of the cavity.

Lets solve for the eigenvalues,
$$
\det \lvert M-\lambda \hat{1} \rvert =0 \implies  \begin{vmatrix}
A-\lambda & B \\
C & D-\lambda
\end{vmatrix} =0
$$
Which can be reduced to the quadratic,
$$
\lambda^{2}-(A+D)\lambda + AD-BC = \lambda^{2}- \text{Tr}\{ M \}\lambda + 1=0
$$
Where $\text{Tr}\{ M \}$ is the trace of $M$. and $AD-BC=1$ since it is equivalent to the determinant of $M$.

Apply the quadratic formula to find,
$$
\lambda_{\pm} = \frac{1}{2} \text{Tr}\{ M \} \pm \sqrt{ \left( \frac{1}{2} \text{Tr}\{ M \} \right)^{2}-1  }
$$
This is the most general form of the eigenvalues. For our specific case, this becomes:
$$
\lambda_{\pm} = A \pm \sqrt{ A^{2}-1 } = A\pm i\sqrt{ 1-A^{2} } = e^{ \pm i\phi } = \cos \phi \pm i\sin \phi
$$
Splitting this into the real and imaginary parts, this therefore means,
$$
A = \cos \phi
$$
Which also tells us that $-1\leq A\leq 1$. According to our previous expression for $A$ this means that,
$$
-2\leq  2 \frac{L}{R} \left( \frac{L}{R}-2 \right) \leq  0
$$
The stable zone indicated by this equivalence is best visualized as a graph
![[Pasted image 20260228173118.png]]
You can see the two types of unstable cavities on the left and right sides. One where the radius of curvature is too small, and one where the radius of curvature is convex and so has no stability at all.
# Analyzing stable cavities
This leads us to conclude that a few cavities that might be stable will look like this:
![[Pasted image 20260228173310.png]]

A common convention to simplify the math for some cavity with $R_{1}$ and $R_{2}$ like so:
![[Pasted image 20260228173611.png]]
Is to define two new variables,
$$
g_{1} = 1-\frac{L}{R_{1}} \qquad g_{2} = 1-\frac{L}{R_{2}}
$$
Which gives us,
$$
\frac{1}{2} \text{Tr}\{ M \} = 2g_{1}g_{2}-1
$$
And so the stability condition becomes,
$$
-1\leq  2g_{1}g_{2}-1\leq 1 \implies  0\leq  g_{1}g_{2}\leq 1
$$
The plot as a function of $g_{1}$ and $g_{2}$ is therefore,
![[Pasted image 20260228173846.png]]

Here is another depiction of this same plot, but as a function of $L /R_{1}$ and $L /R_{2}$ instead.
![[Pasted image 20260228174438.png]]
There are two notable groups here, notated with I and II.
1. These are the cases with one diverging mirror $R<0$. In these cases, one mirror is divergent, and one is convergent, so the convergent mirror in a sense "saves" the ray from leaving the cavity.
2. The line along the middle is the symmetric case. That is, for $R_{1}=R_{2}$ and $0\leq L /R\leq 2$ we have a stable cavity.
# Canonical cavities
Confocal:
$$
R_{1}=R_{2}=L
$$
Concentric:
$$
R_{1}=R_{2}=\frac{L}{2}
$$
Planar:
$$
R_{1}=R_{2}=\infty
$$
- Recall that this one is marginally stable
Hemisphere:
$$
R_{1}=\infty \qquad L<R_{2}<\infty
$$
- There is a very detailed diagram of all the regimes depicted in the lecture notes, I won't include them all here.
