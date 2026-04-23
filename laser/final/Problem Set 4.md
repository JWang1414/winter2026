# Question 1
---
a.
Recall,
$$
q=z+iz_{0} \qquad q'=\frac{Aq+B}{Cq+D}
$$
The beam encounters a lens, changing the location of the beam waist, and the Rayleigh range according to the ABCD matrix:
$$
\begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix}
$$
Since the waist is at the lens, the $q$ parameter simplifies into:
$$
q = z+iz_{0} = iz_{0}
$$
The new $q$ parameter is:
$$
q'=\frac{iz_{0}}{(-1 /f)iz_{0}+1} = \frac{1}{f^{2}+z_{0}^{2}}\left[ iz_{0}\left( 1+i \frac{z_{0}}{f} \right)f^{2} \right]
$$
$$
z'+iz_{0}'= \frac{1}{f^{2}+z_{0}^{2}} (-z_{0}^{2}f + iz_{0}f^{2})
$$
The new location of the beam waist is:
$$
z'= l =-\frac{z_{0}^{2}f}{f^{2}+z_{0}^{2}} \neq -f
$$
It is apparent that the predictions made by ray optics is incorrect for the Gaussian beam.
- I'm supposed to express this in terms of $w_\text{in}$ and $\lambda$ instead of $z_{0}$, but it's effectively just a change of variables.

Re-arrange this into,
$$
l=-\frac{z_{0}^{2}f}{z_{0}^{2}(f^{2} /z_{0}^{2}+1)} = -\frac{f}{f^{2} /z_{0}^{2}+1}
$$
Which, under the limit $z_{0}\to \infty$ becomes,
$$
l = -\frac{f}{f^{2} /\infty^{2}+1} = -f
$$
As predicted by ray optics. This implies that for the predictions of ray optics to apply to Gaussian beams, the Rayleigh range must be infinite. Physically, this means that the beam never widens or decays, just as you would expect a ray would.

---
b.
From above we have,
$$
z_{0}' = \frac{z_{0}f^{2}}{f^{2}+z_{0}^{2}}
$$
Using the fact that,
$$
z_{0}=\frac{kw_{0}^{2}}{2} = \left( \frac{2\pi}{\lambda} \right) \frac{w_{0}^{2}}{2} = \frac{\pi w_{0}^{2}}{\lambda}
$$
This becomes,
$$
\frac{\pi w_\text{out}^{2}}{\lambda} = \frac{(\pi w_{0}^{2} /\lambda)f^{2}}{f^{2}+(\pi w_{0}^{2} /\lambda)^{2}}
$$
Therefore,
$$
w_\text{out}^{2} = \frac{(f\lambda w_{0})^{2}}{f^{2}\lambda^{2}+\pi^{2}w_{0}^{4}} \implies  w_\text{out} = \frac{f\lambda w_{0}}{\sqrt{ f^{2}\lambda^{2}+\pi^{2}w_{0}^{4} }}
$$
Where I have used $w_\text{out}$ to denote the beam waist of the output beam.

---
c.
$$
z_{0}' = \frac{z_{0}f^{2}}{f^{2}+z_{0}^{2}} = \frac{z_{0}f^{2}}{f^{2}(1+z_{0}^{2} /f^{2})}
$$
$$
z_{0}' = \frac{z_{0}}{1+z_{0}^{2} /f^{2}}
$$
In the case where $f\gg z_{0}$ this becomes,
$$
z_{0}'=z_{0} \implies  w_\text{out} = w_\text{in}
$$
Where $w_\text{out}$ and $w_\text{in}$ are the beam waists of the output and input beams, respectively.

Physically, this means that if the focal length of the lens is very large, than the beam waist of the output beam will be approximately the same size as the input beam.

# Question 2
---
a.
We have,
$$
\mathcal{E}(x, y, z=0) = E_{0} \exp\left( -\frac{x^{2}+y^{2}}{w_{0}^{2}} \right)e^{ -i\omega t }
$$
Fraunhofer approximation:
$$
- \frac{ie^{ ikz }e^{ (ik/2z)(x^{2}+y^{2}) }}{\lambda z} \iint_{\text{aperture}} E(x', y', 0) e^{ -(ik/z)(xx'+yy') } \, dx' \, dy'
$$
Integral of interest is:
$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \exp\left( -\frac{x'^{2}+y'^{2}}{w_{0}^{2}} \right) \exp\left( -\frac{ik}{z}(xx'+yy') \right) \, dx'  \, dy'
$$
Split this into two identical integrals
$$
\int_{-\infty}^{\infty} e^{ -x'^{2}/w_{0}^{2} }e^{ -ikxx'/z } \, dx'
$$
Gaussian Fourier transform:
$$
\int_{-\infty}^{\infty} e^{ -ax^{2} } e^{ ibx } \, dx = \sqrt{ \frac{\pi}{a} } e^{ -b^{2}4a }
$$
Results in the integrals:
$$
\sqrt{ \pi } w_{0} \exp \left[ -\left( \frac{kw_{0}x}{2z} \right)^{2} \right]
$$
Combine this with $y$ to obtain the full solution:
$$
E(x', y', 0) = -\frac{ikw_{0}^{2}}{2z} E_{0} e^{ ikz } e^{ (ik/2z)(x^{2}+y^{2}) } \exp\left( -\frac{x^{2}+y^{2}}{w(z)} \right)
$$
Where we have defined the beam width,
$$
w(z) = \frac{2z}{kw_{0}} = \frac{\lambda z}{\pi w_{0}}
$$
The amplitude profile in this version is still Gaussian, and the wavefront is also spherical.

The beam diverges linearly with $z$ in this case, which occurs only at large $z$ for the PWE solution.

---
b.
- Do not know how to answer this one. Read the answers later
# Question 3
The beam goes through a lens, and then enters the glass block.

The matrix for the system is:
$$
\begin{bmatrix}
1 & 0 \\
0 & n_{1} /n_{2}
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\
-n_{1} /fn_{2} & n_{1} /n_{2}
\end{bmatrix}
$$
Note that we begin in air, so $n_{1}=1$. Therefore,
$$
z'+iz_{0}' = \frac{z+iz_{0}}{(-1 /fn_{2})(z+iz_{0}) + (1 /n_{2})}
$$
$$
= \frac{(z+iz_{0})n_{2}f}{f-z-iz_{0}} = \frac{\left[ (z(f-z)-z_{0}^{2})+iz_{0}f \right] n_{2}f}{(f-z)^{2}+z_{0}^{2}}
$$
The new beam waist is located at,
$$
z'= \frac{(z(f-z)-z_{0}^{2})n_{2}f}{(f-z)^{2}+z_{0}^{2}}
$$
Notably, the Rayleigh range before entering the glass slab is,
$$
z_{0}= \frac{\pi w_{0}^{2}}{\lambda} = \frac{\pi(50 \times 10^{-6})^{2}}{0.5 \times 10^{-6}} = \frac{\pi}{200}
$$
Therefore,
$$
z' \approx -0.03331 \text{ m}
$$
I conclude that the beam will come to a focus approximately 3.33 cm into the glass slab.