# Question 1
# Force 1
---
a.
$$
\begin{align}
W & = \int_{O}^{Q} (F_{x} \, dx + F_{y} \, dy) + \int_{Q}^{P} (F_{x} \, dx + F_{y} \, dy) \\
 & = \int_{O}^{Q} F_{x} \, dx + \int_{O}^{Q} F_{y} \, dy + \int_{Q}^{P} F_{x} \, dx + \int_{Q}^{P} F_{y} \, dy
\end{align}
$$
Where $F_{x}$ is the $x$ component, and $F_{y}$ is the $y$ component. The total work is therefore,
$$
\begin{align}
W & = \int_{0}^{1} x^{2} \, dx + \int_{0}^{0} 2xy \, dy + \int_{1}^{1} x^{2} \, dx + \int_{0}^{1} 2xy \, dy  \\
 & = \int_{0}^{1} x^{2} \, dx + 2 \int_{0}^{1} y \, dy  \\
 & = \left[ \frac{x^{3}}{3} \right] ^1_{0} + 2 \left[ \frac{y^{2}}{2} \right] ^1_{0} \\
 & = \frac{1}{3} + 1 \\
 & = \frac{4}{3}
\end{align}
$$
---
b.
Since $y=x^{2}$,
$$
\vec{F} = \begin{bmatrix}
x^{2} \\
2xy
\end{bmatrix} = \begin{bmatrix}
x^{2} \\
2x(x^{2})
\end{bmatrix} = \begin{bmatrix}
x^{2} \\
2x^{3}
\end{bmatrix}
$$
Using the hint,
$$
\begin{align}
W & = \int_{O}^{P} (F_{x} \, dx + F_{y} \, dy) \\
 & = \int_{O}^{P} (F_{x} \, dx + F_{y}(2x) \, dx) \\
 & = \int_{0}^{1} x^{2} + 2x^{3}(2x) \, dx \\
 & = \int_{0}^{1} x^{2} \, dx  + 4 \int_{0}^{1} x^{4} \, dx  \\
 & = \left[ \frac{x^{3}}{3} \right] ^1_{0} + 4 \left[ \frac{x^{5}}{5} \right] ^1_{0} \\
 & = \frac{1}{3} + \frac{4}{5} = \frac{17}{15}
\end{align}
$$
---
c.
$$
x=t^{3} \implies  dx = 3t^{2} \, dt \qquad y=t^{2} \implies  dy=2t \, dt
$$
Integral is from $t=0$ to $t=1$ so,
$$
W = \int_{0}^{1} x^{2} \, dx + 2xy \, dy = \int_{0}^{1} (t^{3})^{2}(3t^{2}) \, dt + 2(t^{3})(t^{2})(2t) \, dt
$$
$$
W = 3\int_{0}^{1} t^{8} \, dt + 4 \int_{0}^{1} t^{6} \, dt = 3\left( \frac{1}{9} \right) + 4\left( \frac{1}{7} \right) = \frac{19}{21}
$$
---

Either my calculations are horribly wrong, or this force is not conservative.
# Force 2
---
a.
On the first line, $y=0$,
$$
\int_{0}^{1} F_{x} \, dx = \int_{0}^{1} 2xy \, dx =0
$$
On the second line, $x=1$,
$$
\int_{0}^{1} F_{y} \, dy = \int_{0}^{1} x^{2} \, dy = \int_{0}^{1} dy =1
$$
The work is therefore,
$$
W = 0+1 =1
$$
---
b.
Using the hint,
$$
W = \int_{0}^{1} 2xy \, dx + x^{2}(2x) \, dx = \int_{0}^{1} 2x^{3} + 2x^{3} \, dx = 4\int_{0}^{1} x^{3} \, dx = 4\left( \frac{1}{4} \right) = 1
$$
---
c.
According to the parametrization,
$$
\vec{F} = \begin{bmatrix}
2xy \\
x^{2}
\end{bmatrix} = \begin{bmatrix}
2(t^{3})(t^{2}) \\
(t^{3})^{2}
\end{bmatrix} = \begin{bmatrix}
2t^{5} \\
t^{6}
\end{bmatrix}
$$
And, from the previous question,
$$
dx = 3t^{2} \, dt \qquad dy = 2t\, dt
$$
Therefore,
$$
\begin{align}
W & = \int_{0}^{1} 2t^{5}(3t^{2}) + t^{6}(2t) \, dt \\
 & = \int_{0}^{1} 6t^{7} + 2t^{7} \, dt \\
 & = 8 \int_{0}^{1} t^{7} \, dt \\
 & = 8 \left( \frac{1}{8} \right) = 1
\end{align}
$$
---

I conclude that the first force is not conservative, but the second is.
# Question 3
