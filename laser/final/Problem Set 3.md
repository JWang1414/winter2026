# Question 2
---
a.
Assume that:
$$
\frac{I_{R}}{I_\text{in}} = R \left| \frac{1-e^{ i\phi }}{1-R e^{ i\phi }} \right| ^{2}
$$
Expand the exponential,
$$
= \frac{4R \sin ^{2}(\phi /2)}{(1-R)^{2}+4R \sin ^{2}(\phi /2)}
$$
The transmitted intensity is:
$$
\frac{I_{T}}{I_\text{in}} = 1-\frac{I_{R}}{I_\text{in}} = \frac{(1-R)^{2}}{(1-R)^{2}+4R\sin ^{2}(\phi /2)}
$$
Define $F=4R /(1-R)^{2}$, and the above simplifies into:
$$
\frac{I_{T}}{I_\text{in}} = \frac{1}{1+F\sin ^{2}(\phi /2)}
$$
---
b.
Plotted this before. It's a series of tall bumps. Here's a example of what you might expect from the textbook:
![[Pasted image 20260420145607.png]]

---
c.
- No clue how to solve this problem. Check the answer sheet here
# Question 1
---
a.
Light propagates some distance to a lens, is refracted by the lens, and then propagates some distance to form an image.
$$
\begin{bmatrix}
1 & s_\text{image} \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & s_\text{obj} \\
0 & 1
\end{bmatrix} = \frac{1}{f} \begin{bmatrix}
f-s_\text{image} & fs_\text{image}+fs_\text{obj} - s_\text{image}s_\text{obj} \\
-1 & f-s_\text{obj}
\end{bmatrix}
$$
Apply the condition that $B=0$,
$$
s_\text{obj} + s_\text{image} - \frac{s_\text{obj}s_\text{image}}{f}=0
$$
Divide by $s_\text{obj}s_\text{image}$ to find,
$$
\frac{1}{s_\text{image}} + \frac{1}{s_\text{obj}} - \frac{1}{f}=0 \implies  \frac{1}{f} = \frac{1}{s_\text{image}} + \frac{1}{s_\text{obj}}
$$
As needed.

---
b.
Replacing the variables,
$$
\frac{1}{f} \begin{bmatrix}
f-(f+x') & f(f+x') + f(f+x) - (f+x)(f+x') \\
-1 & f-(f+x)
\end{bmatrix}
$$
$$
\frac{1}{f} \begin{bmatrix}
-x' & f^{2}-xx' \\
-1 & -x
\end{bmatrix} = \frac{1}{f} \begin{bmatrix}
-x' & 0 \\
-1 & -x
\end{bmatrix}
$$
Include the sample ray $\begin{bmatrix}y_{1} & \theta_{1}\end{bmatrix}$
$$
\begin{bmatrix}
y_{2} \\
\theta_{2}
\end{bmatrix} = -\frac{1}{f} \begin{bmatrix}
x' & 0 \\
1 & x
\end{bmatrix} \begin{bmatrix}
y_{1} \\
\theta_{1}
\end{bmatrix} = -\frac{1}{f} \begin{bmatrix}
y_{1}x' \\
\theta_{1}x+y_{1}
\end{bmatrix}
$$
The magnification of the image is,
$$
M = \frac{y_{2}}{y_{1}} = \frac{-(1 /f)(y_{1}x')}{y_{1}} = -\frac{x'}{f}
$$
---
c.
Light passes through a lens, and then propagates $f$ distance
$$
\begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} = \begin{bmatrix}
0 & f \\
-1 /f & 1
\end{bmatrix}
$$
Now,
$$
\begin{bmatrix}
y_\text{final} \\
\alpha _\text{final}
\end{bmatrix} = \begin{bmatrix}
0 & f \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
y_\text{init} \\
\alpha _\text{init}
\end{bmatrix} = \begin{bmatrix}
f\alpha _\text{init} \\
\alpha _\text{init}-y_\text{init} /f
\end{bmatrix}
$$
Therefore,
$$
y_\text{final} = f\alpha _\text{init}
$$
As needed.

---
d.
Light travels some distance $f$, goes through a lens, travels some distance $2f$, and then creates an image after propagating $f$ distance.
$$
\begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & 2f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} = -\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
$$
\begin{bmatrix}
y_{2} \\
\theta_{2}
\end{bmatrix} = - \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} \begin{bmatrix}
y_{1} \\
\theta_{2}
\end{bmatrix} = - \begin{bmatrix}
y_{1} \\
\theta_{1}
\end{bmatrix}
$$
The magnification is therefore,
$$
M = \frac{y_{2}}{y_{1}} = -\frac{y_{1}}{y_{1}}=-1
$$
So the image is flipped, but has unity spatial magnification, as needed.

---
e.
$$
\begin{bmatrix}
1 & f+x \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & 2f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & f+x \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
-1 & -2x \\
0 & -1
\end{bmatrix} = -\begin{bmatrix}
1 & 2x \\
0 & 1
\end{bmatrix}
$$
- Spatial magnification is not independent from $x$ here. I remember something about it looking blurrier because of the $x$ dependence on the angle.
- Check the answer sheet here
---
f.
Light travels some distance $f$, goes through a lens with focal length $f$, travels $f$, reflects off the flat mirror, travels $f$, goes through the lens again, and then travels some distance.

The ABCD matrix for a flat mirror is,
$$
\begin{bmatrix}
1 & 0 \\
-1 /\infty & 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
So the identity. This tells me that the final system can be modelled identically to the system presented in part D.

I conclude that the system shares the same properties as the system in part D. Furthermore, if the emitter is moved, it would share the same properties as the system in part E.

Light from the emitter at $y_\text{init}=0$ would exit the emitter, reflect off the mirror, and then after going back through the lens, end up in the same location. The light will, however, have the opposite polarization.