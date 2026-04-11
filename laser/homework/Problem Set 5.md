# Question 3
---
a.
For each wavelength $\lambda_{1}$ and $\lambda_{2}$, the associated Gaussian line shape with $e^{-2}$ width $\sigma$ is:
$$
S_{i} (\omega) = \frac{I}{\sigma \sqrt{ \pi }} \exp \left[ - \frac{(\omega-\omega_{i})^{2}}{\sigma^{2}} \right]
$$
Where $\omega_{i}$ are the angular frequencies $\omega_{i}=2\pi c /\lambda_{i}$.

According to the Wiener-Khinchin theorem, the mutual coherence and the power spectrum are a Fourier transform pair. From lecture, we have:
$$
\Gamma(\tau) = \frac{1}{2\pi} \int S(\omega) e^{ -i\omega \tau } \, d\omega
$$
Compute:
$$
\begin{align}
\Gamma(\tau) & = \frac{I}{\sigma \sqrt{ \pi }} \int_{-\infty}^{\infty} e^{ -(\omega-\omega_{i})^{2}/\sigma^{2} } e^{ -i\omega \tau } \, d\omega  \\
 & = \frac{I}{\sigma \sqrt{ \pi }} \left( \sigma \sqrt{ \pi } e^{ -(\sigma \tau/2)^{2} } e^{ -i\omega_{i}\tau } \right)  \\
 & = I e^{ -(\sigma \tau/2)^{2} } e^{ -i\omega_{i}\tau }
\end{align}
$$
The total coherence function should be a summation with both frequencies:
$$
\begin{align}
\Gamma(\tau) & = I e^{ -(\sigma \tau/2)^{2} } e^{ -i\omega_{1}\tau } + I e^{ -(\sigma \tau/2)^{2} } e^{ -i\omega_{2}\tau } \\
 & = I e^{ -(\sigma \tau/2)^{2} } (e^{ -i\omega_{1}\tau } + e^{ -i\omega_{2}\tau })
\end{align}
$$
Note that the mutual coherence is defined to be:
$$
\gamma(\tau) = \frac{\Gamma(\tau)}{\Gamma(0)}
$$
Evaluate the denominator:
$$
\Gamma(0) = I e^{ 0 } (e^{ 0 } + e^{ 0 }) = 2I
$$
So the mutual coherence of the light from this source is,
$$
\gamma(\tau) = \frac{1}{2} e^{ -(\sigma \tau/2)^{2} } (e^{ -i\omega_{1}\tau } + e^{ -i\omega_{2}\tau })
$$
---
b.
According to lecture, the visibility is,
$$
V = \frac{\text{max}-\text{min}}{\text{max}+\text{min}} = \lvert \gamma(\tau) \rvert
$$
Therefore,
$$
\begin{align}
V(\tau) & = \frac{1}{4} e^{ -(\sigma \tau)^{2}/2 } (e^{ -i\omega_{1}\tau } + e^{ -i\omega_{2}\tau }) (e^{ i\omega_{1}\tau } + e^{ i\omega_{2}\tau }) \\
 & = \frac{1}{2} e^{ -(\sigma \tau)^{2}/2 } (\cos((\omega_{1}-\omega_{2})\tau)+1)
\end{align}
$$
So we are interested in plotting this function with,
$$
\sigma=3 \times 10^{11} \qquad \omega_{i} = \frac{2\pi c}{\lambda_{i}}
$$
Using the provided values $\sigma=3 \times 10^{11}$ and $\lambda=600\pm 0.3$ nm resulted in plots that could not be shown due to machine precision. So, instead I have scaled the values by dividing the angular frequencies by $c$, and scaling the $\tau$ axis by $10^{8}$. The values I used were:
$$
\sigma= 3\times 10^{3} \qquad \omega_{i} = \frac{1}{10^{8}} \frac{2\pi}{\lambda_{i}}
$$


# Question 4
---
a.
The intensity at the output of a Michelson interferometer is:
$$
I = I^{(1)} + I^{(2)} + 2 \mathrm{Re}\{ \Gamma(\tau) \}
$$
Where $\Gamma$ is the mutual coherence function. The complex degree of coherence is:
$$
\gamma(\tau) = \frac{\Gamma(\tau)}{\Gamma(0)} = \frac{\Gamma(\tau)}{\sqrt{ I^{(1)}I^{(2)} }}
$$
In polar form I have that,
$$
\gamma(\tau) = \lvert \gamma(\tau) \rvert  e^{ i\phi(\tau) } = \frac{\Gamma(\tau)}{\sqrt{ I^{(1)}I^{(2)} }}
$$
Therefore the intensity at the output has the form,
$$
I =  I^{(1)} + I^{(2)} + 2 \sqrt{ I^{(1)}I^{(2)} } \lvert \gamma(l) \rvert  \cos(k_{0}l + \phi)
$$
Where I have swapped from the coherence time to the coherence length, to match the provided function more accurately. Matching coefficients with the given function:
$$
I = 2I_{0} + I_{0} e^{ -(l/l_{c})^{2} } \cos(k_{0}l)
$$
Tells me that:
$$
I^{(1)} + I^{(2)} = 2I_{0} \qquad 2\sqrt{ I^{(1)}I^{(2)} } = I_{0}
$$
Using the identity:
$$
\begin{align}
\left[ I^{(1)} - I^{(2)} \right] ^{2} & = \left[ I^{(1)} + I^{(2)} \right] ^{2} - 4I^{(1)} I^{(2)} \\
 & = 4I_{0}^{2} - 4\left( \frac{I_{0}^{2}}{4} \right) \\
 & = 3I_{0}^{2} \\
\left[ I^{(1)} - I^{(2)} \right] & = \sqrt{ 3 }I_{0}
\end{align}
$$
Solving this system of equations,
$$
I_{i} = I_{0} \left( 1\pm\frac{\sqrt{ 3 }}{2} \right)
$$
Which is the balance of intensities from each arm in the interferometer.

---
b.
Using the same strategy, the complex degree of coherence for this function is:
$$
\gamma(l) = e^{ -(l/l_{c})^{2} } e^{ ik_{0}l }
$$
Solve for the normalization constant:
$$
A\int_{-\infty}^{\infty} e^{ -2(l/l_{c})^{2} } \, dl = A \sqrt{ \frac{\pi}{2} }l_{c}=1 \implies  A = \frac{\sqrt{ 2 }}{\sqrt{ \pi }l_{c}}
$$
The normalized mutual coherence function is therefore:
$$
\gamma(l) = \frac{\sqrt{ 2 }}{\sqrt{ \pi }l_{c}} e^{ -(l/l_{c})^{2} } e^{ ik_{0}l }
$$
---
c.
According to the Wiener-Khinchin theorem, the spectral distribution will be the Fourier transform of the mutual coherence function:
$$
\begin{align}
S(k) & = \frac{\sqrt{ 2 }}{\sqrt{ \pi }l_{c}} \int_{-\infty}^{\infty} e^{ -(l/l_{c})^{2} } e^{ ik_{0}l } e^{ -ikl } \, dl \\
  & = \frac{\sqrt{ 2 }}{\sqrt{ \pi }l_{c}} \sqrt{ \pi }l_{c} e^{ -(k_{0}-k)^{2}l^{2}_{c}/4 } \\
 & = \sqrt{ 2 } e^{ -(k_{0}-k)^{2}l^{2}_{c}/4 } \\
\end{align}
$$
# Question 2
---
a.
The Fraunhofer diffraction pattern for a rectangular aperture with dimensions $\Delta x$ nd $\Delta y$ is defined to be:
$$
I(x, y, z) = I_{0} \left( \frac{\Delta x\Delta y}{\lambda z} \right)^{2} \text{sinc}^{2}\left( \frac{\pi\Delta x}{\lambda z}x \right) \text{sinc}^{2} \left( \frac{\pi\Delta y}{\lambda z}y \right)
$$
According to the array theorem, for some array of identical apertures, the resulting field will be:
$$
E(x, y, z) = \left[ \sum_{n=1}^{N} e^{ -ik(xx'_{n}+yy'_{n})/z } \right] \left[ -i \frac{e^{ ikz }e^{ ik(x^{2}+y^{2})/2z }}{\lambda z} \right] \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} E_\text{aperture}(x', y', 0) e^{ -ik(xx'+yy') } \, dy'  \, dx'
$$
Now, suppose that the apertures are positioned at,
$$
x'_{n} = \left( n-\frac{N+1}{2} \right)a \qquad y'_{n}=0
$$
Then the summation in the array theorem becomes,
$$
\sum_{n=1}^{N} \exp \left[ -\frac{ik}{z}(xx'_{n} + yy'_{n}) \right] = \exp \left[ \frac{ikax}{z} \frac{N+1}{2} \right] \sum_{n=1}^{N} e^{ -ikaxn/z }
$$
This is a geometric series. Evaluating,
$$
= e^{ ik(N+1)xa/2z }e^{ -ikax/z } \frac{e^{ -ikaxN/z } -1}{e^{ -ikax/z }-1} = \frac{\sin(Nkax /2z)}{\sin(kax /2z)}
$$
Substituting this factor into the array theorem, and removing the $y$ dependence yields:
$$
I = I_{0} \text{sinc}^{2} \left( \frac{\pi\Delta x}{\lambda z}x \right) \frac{\sin ^{2}(N\pi ax /\lambda z)}{N^{2} \sin ^{2}(\pi ax /\lambda z)}
$$
Now, substituting in,
$$
\frac{\pi\Delta x}{\lambda z}x = \frac{1}{2}bk\theta = \beta \qquad \frac{\pi ax}{\lambda z} = \frac{1}{2}ak\theta = \gamma
$$
Since $k=2\pi /\lambda$ and $\theta=x /z$, the resulting intensity pattern is,
$$
I = I_{0} \left( \frac{\sin \beta}{\beta} \right)^{2} \left( \frac{\sin(N\gamma)}{N \sin\gamma} \right)^{2}
$$
As needed.

---
b.
First, note that the zeroes of this function occur when,
$$
\sin(N\gamma) =0 \implies  N\gamma = m\pi
$$
Where $m$ is an integer. The first-order spot is located at,
$$
\gamma = \frac{1}{2} ak\theta = \frac{1}{2} ak \left( \frac{\lambda}{a} \right) = \frac{1}{2} \left( \frac{2\pi}{\lambda} \right) \lambda = \pi \implies  N\gamma=N\pi
$$
The first zero will therefore appear when,
$$
N\gamma = (N\pm 1)\pi \implies  \gamma = \frac{(N+1)\pi}{N} = \pi + \frac{\pi}{N}
$$
Therefore the half-width is,
$$
\Delta\gamma = \frac{1}{2} ak\Delta\theta = \frac{\pi}{N} \implies  \Delta\theta = \frac{2\pi}{akN} = \frac{\lambda}{Na}
$$
To move the spot by one half-width, first note that a wavelength shift displaces the first-order spot by,
$$
\theta=\frac{\lambda}{a} \implies  \delta\theta = \frac{\Delta \lambda}{a}
$$
For a displacement by one half-width,
$$
\frac{\Delta \lambda}{a} = \frac{\lambda}{Na} \implies  \frac{\Delta \lambda}{\lambda} = \frac{1}{N}
$$
---
c.
The van Cittert-Zernike theorem states that,
$$
\Gamma(x_{1}, x_{2}) = \int I(x_{s}) e^{ ikx_{s}(x_{2}-x_{1}) } \, dx_{s}
$$
Modelling the source as a uniformly lit slit of width $w$, the intensity is $I(x_{s})=I_{0}$ for $\lvert x_{s} \rvert\leq w /2$, and 0 otherwise. This integral therefore becomes,
$$
\Gamma(x_{1}, x_{2}) = \int_{-w /2}^{w /2} e^{ ikx_{s}(x_{2}-x_{1})/L } \, dx_{s} = w \text{ sinc}\left( \frac{kw(x_{2}-x_{1})}{2L} \right)
$$
This mutual coherence function falls to zero when the argument in the sinc function is $\pi$,
$$
\frac{kw(x_{2}-x_{1})}{2L} = \pi \implies  x_{2}-x_{1} = l_{c} = \frac{\lambda L}{w}
$$
Where $l_{c}$ is the transverse coherence length. Physically, to maximize the resolving power I would like to maximize the number of slits used in the diffraction grating. In this case, the greatest number of diffracted beams are contributing to the resulting diffraction pattern. Therefore the transverse coherence length should be,
$$
l_{c} \geq  Na
$$
Substituting in the requirement from the van Cittert-Zernike theorem,
$$
\frac{\lambda L}{w} \geq  Na \implies  \frac{w}{L} \leq  \frac{\lambda}{Na}
$$
