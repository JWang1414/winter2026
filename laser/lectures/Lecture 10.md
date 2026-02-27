# Ray Matrices
Rays are a geometric way of imagining light by modelling them as straight lines.
![[Pasted image 20260226204825.png]]
It ignores diffraction, and so is typically applied in regimes where diffraction is insignificant.

We will define the rays within the vector $\begin{bmatrix}r & r'\end{bmatrix}$ where $r'=dr /dz$ is the angle of propagation, notated as $\alpha$ in the above diagram.
- Paraxial rays have $\alpha\ll 1$ and $\tan \alpha \approx \alpha$

A ray matrix maps an initial vector to a final vector,
$$
\begin{bmatrix}
r \\
\alpha
\end{bmatrix}_{i} \to  \begin{bmatrix}
r \\
\alpha
\end{bmatrix} _{f}
$$
Perhaps something like,
$$
\begin{bmatrix}
r \\
\alpha
\end{bmatrix}_{f} = \begin{bmatrix}
1 & z_{2}-z_{1} \\
0 & 1
\end{bmatrix} \begin{bmatrix}
r \\
\alpha
\end{bmatrix}_{i}
$$
Where we have defined $z_{2}$ and $z_{1}$ according to:
![[Pasted image 20260226205410.png]]
This is the ray matrix for free propagation.

So what is the ray matrix for free propagation? Here we will model the lens as infinitely thin, and claim that only the angle charges after passing through the lens.

Recall that the ray matrix for this is,
$$
\begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix}
$$
Where $f$ is the focal length of the lens
![[Pasted image 20260226210034.png]]

And for curved mirrors the ray matrix is,
$$
\begin{bmatrix}
1 & 0 \\
-2 /R & 1
\end{bmatrix}
$$
Where $R$ is the radius of curvature.
- The factor of 2 arises because although the radius of curvature is $R$, the focal point is actually at $R /2$.

Note that for a ray propagating in the $-z$ direction, $\begin{bmatrix}r & -dr /dz\end{bmatrix}$ so the lower element is $>0$ when $r$ increases.

Also recall that diverging lenses and mirrors have $f<0$ and $R<0$.

Generally, we used ray matrices you describe a full optical system. The system is often notated with,
$$
M = \begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
$$
Often referred to as ABCD matrices. Lets investigate this form.

What does $A=0$ imply? Well,
$$
\begin{bmatrix}
r_{f} \\
\alpha_{f}
\end{bmatrix} = \begin{bmatrix}
0 & B \\
C & D
\end{bmatrix} \begin{bmatrix}
r_{i} \\
\alpha_{i}
\end{bmatrix}
$$
Which means that $r_{f}=\beta\alpha_{i}$ and so the final position is independent of $r_{i}$.
- This is very powerful, because it means there is a focus at the exit regardless of $r_{i}$.

Furthermore, we have $\det M=1$ for uniform index systems.