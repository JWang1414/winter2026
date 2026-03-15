# Question 1
# Force 1
---
a.
Along the first path from $O\to Q$, $y=0$, and along the second path $Q\to P$, $x=1$. According to the provided expression for the work done, and the hint, the total work is:
$$
W = \int_{O}^{P} (F_{x} \, dx + F_{y} \, dy) = \int_{0}^{1} x^{2} \, dx + \int_{0}^{1} 2xy \, dy
$$
Using the fact that $x=1$ is constant along the second path,
$$
W = \int_{0}^{1} x^{2} \, dx + 2 \int_{0}^{1} y \, dy 
$$
The total work is therefore,
$$
W = \left[ \frac{x^{3}}{3} \right] ^{1}_{0} + 2 \left[ \frac{y^{2}}{2} \right] ^{1}_{0} = \frac{1}{3} + 2\left( \frac{1}{2} \right) = \frac{1}{3} + 1 = \frac{4}{3}
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
Using the hint, the integral is therefore,
$$
W = \int_{O}^{P} (F_{x} \, dx + F_{y} \, dy) = \int_{O}^{P} (F_{x} \, dx + F_{y}(2x) \, dx)
$$
Substituting in $\vec{F}$,
$$
W = \int_{0}^{1} x^{2} \, dx + \int_{0}^{1} 2x^{3}(2x) \, dx  = \int_{0}^{1} x^{2} \, dx + 4 \int_{0}^{1} x^{4} \, dx 
$$
The total work is therefore,
$$
W = \left[ \frac{x^{3}}{3} \right] ^1_{0} + 4 \left[ \frac{x^{5}}{5} \right] ^1_{0} = \frac{1}{3} + 4\left( \frac{1}{5} \right) = \frac{17}{15}
$$
---
c.
According to this parametrization the differentials become:
$$
x=t^{3} \implies  dx = 3t^{2} \, dt \qquad y=t^{2} \implies  dy=2t \, dt
$$
The integral will be along the interval from $t=0$ to $t=1$. The expression for work becomes:
$$
W= \int_{O}^{P} (F_{x} \, dx + F_{y} \, dy) = \int_{0}^{1} x^{2} \, dx + 2xy \, dy = \int_{0}^{1} (t^{3})^{2}(3t^{2}) \, dt + 2(t^{3})(t^{2})(2t) \, dt
$$
Simply and collect like terms:
$$
W = 3\int_{0}^{1} t^{8} \, dt + 4 \int_{0}^{1} t^{6} \, dt
$$
The total work is therefore,
$$
W = 3 \left[ \frac{t^{9}}{9} \right] ^{1}_{0} + 4 \left[ \frac{t^{7}}{7} \right]^{1}_{0} = 3\left( \frac{1}{9} \right) + 4\left( \frac{1}{7} \right) = \frac{19}{21}
$$
Based on these calculations, the force is not conservative.
# Force 2
---
a.
Repeating the same process where $y=0$ on the first line and $x=1$ on the second:
$$
\int_{0}^{1} F_{x} \, dx = \int_{0}^{1} 2xy \, dx =0 \qquad \int_{0}^{1} F_{y} \, dy = \int_{0}^{1} x^{2} \, dy = \int_{0}^{1} dy =1
$$
The total work is therefore:
$$
W = 0+1 =1
$$
---
b.
Using the hint,
$$
W = \int_{0}^{1} 2xy \, dx + x^{2}(2x) \, dx = \int_{0}^{1} 2x^{3} + 2x^{3} \, dx = 4\int_{0}^{1} x^{3} \, dx
$$
So the total work is:
$$
W= 4 \left[ \frac{x^{4}}{4} \right]^{1}_{0} = 4\left( \frac{1}{4} \right) = 1
$$
---
c.
According to the parametrization, the force is:
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
Substitute into the expression for work:
$$
W = \int_{0}^{1} 2t^{5}(3t^{2}) + t^{6}(2t) \, dt = \int_{0}^{1} 6t^{7} + 2t^{7} \, dt = 8 \int_{0}^{1} t^{7} \, dt
$$
The total work is therefore:
$$
W = 8 \left[ \frac{t^{8}}{8} \right]^{1}_{0} = 8\left( \frac{1}{8} \right) = 1
$$
---

I conclude that the first force is not conservative, but the second is.
# Question 3
---
1.
By the relation between force and potential energy:
$$
F = -\nabla V =- \epsilon \frac{d}{dr} \left[ \left( \frac{r_{m}}{r} \right)^{12} - 2 \left( \frac{r_{m}}{r} \right)^{6} \right] = \frac{12\epsilon r_{m}^{6}}{r^{13}} (r^{6}_{m} - r^{6})
$$
There is just one equilibrium at $r=r_{m}$. Furthermore, the force is positive when $r<r_{m}$, and negative when $r>r_{m}$. These correspond to the repelling and attracting regimes, respectively.

The equilibrium at $r=r_{m}$ is stable because if $r<r_{m}$, then it will be repelled into the potential well, and if $r>r_{m}$ it will be attracted back into the potential well. That is, the potential at $r=r_{m}$ is a global minimum.

---
2.
The force according to this adjusted potential is:
$$
F(r) =-\nabla V= \frac{12}{r^{13}} (1-r^{6})
$$
- The rest has been completed in Python
---
3.
- The motion does indeed look approximately sinusoidal
- I compute the average period of oscillation to be 0.746 atomic time units
---
4.
Since $r=x+1$, $V(r)$ becomes:
$$
V(r) = r^{-12} - 2r^{-6} = (x+1)^{-12} - 2(x+1)^{-6}
$$
The Taylor series expansions for these two polynomials are:
$$
(x+1)^{-12} \approx 1-12x + 78x^{2}
$$
$$
(x+1)^{-6} \approx 1-6x+21x^{2}
$$
And so the quadratic approximation for this potential is:
$$
V(x) \approx (1-12x + 78x^{2}) -2 (1-6x+21x^{2}) = 36x^{2}-1
$$
Recall that for quadratic potentials the angular frequency is:
$$
\omega^{2} = \frac{U_{0}''(x_{0})}{m}
$$
In this case $U_{0}=V$, therefore:
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
As $r_{0}$ decreases, the period of oscillation increases, until the particle eventually escapes the potential well and no longer oscillates ($r_{0}=0.85$).

Furthermore, the oscillatory behaviour displayed when $r_{0}=0.90$ is highly eccentric. The particle appears to escape to roughly 1.4 before slowly turning back. Once it goes back into the potential well, it quickly shoots back out again to repeat the same manoeuvre.

This phenomena can be easily understood by picturing the potential well. When $r_{0}=0.85$, the initial potential energy of the particle is quite high, because it is deep in the repelling regime of the LJ potential. Which is why, in this case, the particle does not even oscillate, it has enough potential energy to escape the well and travel to $r\to \infty$.

When $r_{0}=0.90$, however, the particle does not have enough energy to escape the potential well, and so it continues to oscillate inside. However, because for large $r$ the well is particularly shallow, the acceleration of the particle is comparatively small, causing it to shoot outwards before eventually returning, like throwing a boomerang.

In the case where $r_{0}=0.95$, the oscillation is still relatively small, and so very regular. But because it has more potential than if $r_{0}=1.02$, the period length and amplitude are slightly larger.

Note: I have to place most of this writing into a markdown cell, not sure how I'm going to do that but I'll probably place it inside a LaTeX file and a markdown cell.
# Question 2
---
1.
If the mass moves to the right, than the length of the left spring increases, and the length of the right spring decreases. So the length of the left spring can be modelled $l+x$, and $l-x$ for the right spring. Accounting for the stretch in the $y$ direction, this becomes,
$$
r_{\pm} = \sqrt{ (l\pm x)^{2}+y^{2} } = \sqrt{ l^{2}\pm 2lx +x^{2}+y^{2} }
$$
Where I have defined $r_{\pm}$ to be the length of the springs. Factor out $l^{2}$ from inside the square root to obtain,
$$
r_{\pm} = l\sqrt{ 1\pm \frac{2x}{l} + \frac{x^{2}}{l^{2}} + \frac{y^{2}}{l^{2}} } = l\sqrt{ 1+\epsilon_{\pm} }
$$
Where I have defined,
$$
\epsilon_{\pm} = \frac{x^{2}}{l^{2}} + \frac{y^{2}}{l^{2}} \pm \frac{2x}{l}
$$
Now, use the fact that $\epsilon_{\pm}\ll 1$ to apply the Taylor series expansion. $r_{\pm}$ then becomes,
$$
r_{\pm} \approx l\left( 1 \pm \frac{x}{l} + \frac{y^{2}}{2l^{2}} \right) \approx l \pm x + \frac{y^{2}}{2l}
$$
I have dropped all terms with order higher than 2. Now, the potential energy at equilibrium is,
$$
U_{0} = 2\left( \frac{1}{2} k(l-l_{0})^{2} \right) = k(l-l_{0})^{2}
$$
And the potential energy at some position $(x, y)$ is,
$$
U = \frac{1}{2} k (r_{+}-l_{0})^{2} + \frac{1}{2} k(r_{-} - l_{0})^{2} = \frac{1}{2} k \left( l-l_{0} + x + \frac{y^{2}}{2l} \right)^{2} + \frac{1}{2} k \left( l-l_{0} - x + \frac{y^{2}}{2l} \right)^{2}
$$
Define the variable $\Delta l=l-l_{0}$,
$$
U = \frac{1}{2} k \left( \Delta l + x + \frac{y^{2}}{2l} \right)^{2} + \frac{1}{2} k \left( \Delta l - x + \frac{y^{2}}{2l} \right)^{2}
$$
$$
U = k \left[ (\Delta l)^{2}+\frac{(\Delta l)y^{2}}{l} + \frac{y^{4}}{4l^{2}} + x^{2} \right] \approx k \left[ (\Delta l)^{2}+\frac{(\Delta l)y^{2}}{l} + x^{2} \right]
$$
Once again dropping terms with order higher than 2. The difference between the two is,
$$
\Delta U = U-U_{0} = k \left[ (\Delta l)^{2}+\frac{(\Delta l)y^{2}}{l} + x^{2} \right] - k(\Delta l)^{2} = kx^{2}+\frac{k(\Delta l)}{l}y^{2}
$$
The coefficients are,
$$
k_{x} = 2k \qquad k_{y} = \frac{2k(l-l_{0})}{l}
$$
---
2.
The change in the energy is,
$$
\Delta U = kx^{2} + \frac{k(l-l_{0})}{l} y^{2}
$$
Taking two derivatives as a function of $y$,
$$
\frac{d}{dy} \Delta U = \frac{2k(l-l_{0})}{l}y \implies  \frac{d^{2}}{dy^{2}}\Delta U = \frac{2k(l-l_{0})}{l}
$$
At the origin, $y=0$ and so $d(\Delta U) /dy=0$, confirming that there is indeed an equilibrium there. However, if $l<l_{0}$, $d^{2}(\Delta U) /dy^{2}<0$, the negative second derivative indicates that, as a function of $y$, $\Delta U$ is at a maximum.

Therefore, if $y$ deviates from $y=0$, then the mass will continue moving away from the origin, instead opting to settle in a lower energy position.
