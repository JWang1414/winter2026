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
---
1.
$$
F = -\nabla U =- \epsilon \frac{d}{dr} \left[ \left( \frac{r_{m}}{r} \right)^{12} - 2 \left( \frac{r_{m}}{r} \right)^{6} \right] = \frac{12\epsilon r_{m}^{6}}{r^{13}} (r^{6}_{m} - r^{6})
$$
- Stable equilibrium point is at the minimum $r=r_{m}$
- It is repelling when $r<r_{m}$ and attracting when $r>r_{m}$
- So the equilibrium point at the minimum is a stable equilibrium. It is a universally attracting equilibrium
- I got this from plotting it in Desmos, but I believe the intention is to take another derivative
---
2.
$$
V(r) = r^{-12} - 2r^{-6} \qquad F(r) =-\nabla V= \frac{12}{r^{13}} (1-r^{6})
$$
- The rest has been completed in Python
---
3.
- The motion does indeed look approximately sinusoidal
- I compute the average period of oscillation to be 0.746 atomic time units
---
4.
$$
x=r-1 \implies  r=x+1
$$
$$
V(r) = r^{-12} - 2r^{-6} = (x+1)^{-12} - 2(x+1)^{-6}
$$
Taylor series definition,
$$
\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^{n} \approx \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^{2}
$$
Taylor series in question are,
$$
(x+1)^{-12} \approx 1-12x + 78x^{2}
$$
$$
(x+1)^{-6} \approx 1-6x+21x^{2}
$$
Substitute back in,
$$
V(x) \approx (1-12x + 78x^{2}) -2 (1-6x+21x^{2}) = 36x^{2}-1
$$
Recall that,
$$
\omega^{2} = \frac{U_{0}''(x_{0})}{m}
$$
In this case $U_{0}(x_{0})$ is approximately the Taylor expanded $V(x)$, and $m=1$. Therefore,
$$
\omega^{2} = \frac{d^{2}}{dx^{2}}(36x^{2}-1) = 72 \implies  \omega =\sqrt{ 72 }
$$
Convert to the period length,
$$
T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{ 72 }} \approx 0.7405
$$
Which is just around 0.0055 off from the numerically predicted value.

---
5.
As $r_{0}$ decreases, the period of oscillation decreases, until the particle eventually escapes the potential well and no longer oscillates (0.85).

Furthermore, the oscillatory behaviour displayed when $r_{0}=0.90$ was high eccentric. The particle appears to escape to roughly 1.4 before slowly turning back. Once it goes back into the potential well, it quickly shoots back out again to repeat the same manoeuvre.

This phenomena can be easily understood by picturing the potential well. When $r_{0}=0.85$, the initial potential energy of the particle is quite high, because it is deep in the repelling regime of the LJ potential. Which is why, in this case, the particle does not even oscillate, it has enough potential energy to escape the well and travel to $r\to \infty$.

When $r_{0}=0.90$, however, the particle does not have enough energy to escape the potential well, and so it continues to oscillate inside. However, because for large $r$ the well is particularly shallow, the acceleration of the particle is comparatively small, causing it to shoot outwards before eventually returning, like throwing a boomerang.

In the case where $r_{0}=0.95$, the oscillation is still relatively small, and so very regular. But because it has more potential than if $r_{0}=1.02$, the period length and amplitude are slightly larger.

Note: I have to place most of this writing into a markdown cell, not sure how I'm going to do that but I'll probably place it inside a LaTeX file and a markdown cell.
# Question 2
---
1.
