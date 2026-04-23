# Complex Degree of Coherence
The normalized form for the mutual coherence function is called the complex degree of coherence.

Consider a source of radiation that has reached a "steady-state" operation. This property is called *stationarity*. In particular, for stationary fields, the mutual coherence function depends only on the difference $t_{2}-t_{1}$. That is:
$$
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) = \Gamma(\vec{r}_{1}, t_{1}+s; \vec{r}_{2}, t_{2}+s)
$$
For some time increment $s$ and:
$$
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) = \Gamma(\vec{r}_{1}, \vec{r}_{2}, t_{2}-t_{1})
$$
As it turns out, for a stationary field the intensity simplifies into:
$$
\left< I(P, t) \right>  = \left< I(P) \right> = \frac{c\epsilon_{0}}{2} \Gamma(P, P, 0)
$$
As an example, lets consider a monochromatic field:
$$
\begin{align}
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) & = \left< E^*(\vec{r}, t_{1})E(\vec{r}_{2}, t_{2}) \right> \\
 & = \left< \mathcal{E}^*(\vec{r}_{1}) \mathcal{E}(\vec{r}_{2}) e^{ -i\omega(t_{2}-t_{1}) } \right>  \\
 & = \left< \mathcal{E}^*(\vec{r}_{1}) \mathcal{E}(\vec{r}) \right> e^{ -i\omega \tau }
\end{align}
$$
Where the difference is $\tau=t_{2}-t_{1}$.

In the two-slit experiment, the intensity becomes,
$$
\left< I(P, t) \right> = I_{1} + I_{2} + c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\left\{  \Gamma\left( S_{1}, S_{2}, \frac{l}{c} \right)  \right\}
$$
Where, similarly, $l=l_{2}-l_{1}$.

Substituting in our results of a monochromatic field,
$$
\left< I(P) \right> = I_{1}+I_{2}+c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\{ \mathcal{E}^*(S_{1}) \mathcal{E}(S_{2}) e^{ -i\omega l /c } \}
$$
Now, if you suppose that $\mathcal{E}(S_{1})=\mathcal{E}_{0}$ and $\mathcal{E}(S_{2})=\mathcal{E}_{0}e^{ -i\phi }$, then the intensity becomes,
$$
\left< I(P) \right> = I_{1}+I_{2}+ 2\sqrt{ I_{1}I_{2} } \cos\left( \frac{2\pi l}{\lambda} + \phi \right)
$$
Physically, imagine the case when $\phi=0$. Then constructive interference occurs when $l$ is an integer number of wavelength, and destructive when $l$ is a half-integer. A mathematical formulation of what we had already concluded earlier.

Now, if $\phi \neq 0$ then constructive interference occurs at $P$ when:
$$
\frac{2\pi l}{\lambda} + \phi = 2\pi n \implies  l=\left( n + \frac{\phi}{2\pi} \right)\lambda
$$
For small angles:
$$
Y_{n}^{\text{max}} = \left( n+\frac{\phi}{2\pi} \right) \frac{\lambda L}{d} \qquad Y_{n}^{\text{min}} = \left( n+\frac{\phi}{2\pi}+\frac{1}{2} \right) \frac{\lambda L}{d}
$$
Which tell us that the phase difference $\phi$ shifts the positions of the maxima and minima, but the separation $\Delta Y$ is unchanged from $\phi=0$.

It is convenient to write the intensity on the observation screen as:
$$
\left< I(P) \right> = I_{1}+I_{2} + 2\sqrt{ I_{1}I_{2} } \mathrm{Re}\{ \gamma(S_{1}, S_{2}, l /c) \}
$$
Where the dimensionless complex number $\gamma$ is:
$$
\gamma(S_{1}, S_{2}, l /c) = \frac{c\epsilon_{0}}{2} \frac{\lvert K_{1}K_{2} \rvert }{\sqrt{ I_{1}I_{2} }} \Gamma(S_{1}, S_{2}, l /c) = \frac{c\epsilon_{0}}{2} \frac{\Gamma(S_{1}, S_{2}, l /c)}{\sqrt{ \left< I(S_{1}) \right> \left< I(S_{2}) \right>  }}
$$
Which is generally expressed as:
$$
\gamma(\vec{r}_{1}, \vec{r}_{2}, \tau) = \frac{\Gamma(\vec{r}_{1}, \vec{r}_{1}, \tau)}{\sqrt{ \Gamma(\vec{r}_{1}, \vec{r}_{2}, 0)\Gamma(\vec{r}_{2}, \vec{r}_{2}, 0) }}
$$
$\gamma(\vec{r}_{1}, \vec{r}_{2}, \tau)$ is called the complex degree of coherence.
# Quasi-Monochromatic Fields and Visibility
In the case of a monochromatic field, the complex degree of coherence is,
$$
\gamma(\vec{r}_{1}, \vec{r}_{2}, \tau) = e^{ -i\omega \tau }
$$
For quasi-monochromatic light, we assume this changes to,
$$
\gamma = \lvert \gamma(\vec{r}_{1}, \vec{r}_{2}, \tau) \rvert e^{ -i\phi }e^{ -i\omega \tau }
$$
Where $\omega$ is the central frequency, and $\lvert \gamma(\vec{r}_{1}, \vec{r}_{2}, \tau) \rvert$ varies quite slowly in comparison with $e^{ -i\omega \tau }$.

The associated intensity function is,
$$
\left< I(P) \right> = I_{1}+I_{2} + 2\sqrt{ I_{1}I_{2} } \left\lvert  \gamma\left( S_{1}, S_{2}, \frac{l}{c} \right)  \right\rvert \cos\left( \frac{2\pi l}{\lambda}+\phi \right)
$$
Now, since $\lvert \gamma(\vec{r}_{1}, \vec{r}_{2}, \tau) \rvert$ varies much slower than $e^{ -i\omega \tau }$, this cosine function will rapidly oscillate in the same way. The maximum and minimum in the neighbourhood of some point $P$ is:
$$
I_\text{max} = I_{1}+I_{2}+2\sqrt{ I_{1}I_{2} } \lvert \gamma \rvert \qquad I_\text{min} = I_{1}+I_{2}-2\sqrt{ I_{1}I_{2} } \lvert \gamma \rvert
$$
Yielding a fringe visibility:
$$
V = \frac{2\sqrt{ I_{1}I_{2} }\lvert \gamma \rvert }{I_{1}+I_{2}}
$$
So the complex degree of coherence is a direct measure of the fringe visibility. In the sense that $V\propto \lvert \gamma \rvert$.

In the special case where $I_{1}=I_{2}$, $V=\lvert \gamma \rvert$.

Since $0\leq V\leq 1$, this naturally means that $0\leq \lvert \gamma \rvert\leq 1$ as well. This describes the range from incoherent light to completely coherence light.

Recall that as the separation $\tau=\lvert t_{2}-t_{1} \rvert$ increases, we expect the mutual coherence function $\Gamma$ to decrease. One commonly used model for the mutual coherence function that exhibits this property is:
$$
\Gamma = \left< \mathcal{E}^*_{0}(\vec{r}_{1})\mathcal{E}_{0}(\vec{r}_{2}) \right> e^{ -\lvert \tau/\tau _\text{coh} \rvert  } e^{ -i\omega_{L}\tau }
$$
Where $\tau _\text{coh}$ is the correlation time. The field is poorly correlated when the time displacement is greater than $\tau _\text{coh}\approx \lvert t_{2}-t_{1} \rvert$.

> The Wiener-Khintchine theorem states that the stationary field's spectrum $S(\omega)$ is the Fourier transform of the mutual coherence function.

In this case that is,
$$
S(\omega) = 2\pi \left< \mathcal{E}^*_{0}(\vec{r}_{1})\mathcal{E}_{0}(\vec{r}_{2}) \right> \frac{1}{\pi \tau _\text{coh}} \frac{1}{(\omega-\omega_{L}^{2}+\tau _\text{coh}^{-2})}
$$

Note that, for a monochromatic field,
$$
\lvert \gamma \rvert =1
$$
So the idealized monochromatic field always has perfect fringe visibility. However, it is also possible for non-monochromatic fields to satisfy the condition $\lvert \gamma \rvert=1$ for complete coherence.
# Spatial Coherence Of Light From Ordinary Sources
We have seen two examples where a phase shift $\phi$ appears in an expression for the intensity. An ordinary source of light essentially introduces a difference phase shift $\phi$ from each of its infinitely many radiating units.

Such a source cannot give rise to an intensity function with interference fringes. But, if there is substantial distance between the source and points on the observation screen, the field can be coherence in a very subtle way.

First, we isolate the spatial characteristics of the mutual coherence function. Take $t_{1}=t_{2}=t$ then $\Gamma(\vec{r}_{1}, t; \vec{r}_{2}, t)$ is the mutual coherence of the fields at two points in space at the same time. This is the spatial coherence. For stationary sources, spatial coherence is characterized by the mutual coherence function $\Gamma(\vec{r}_{1}, \vec{r}_{2}, 0)$ and the complex degree of coherence $\gamma(\vec{r}_{1}, \vec{r}_{2}, 0)$.

From this point, we will always assume stationarity.

Experimentally, we might place two pinholes $P_{1}$ and $P_{2}$ on a screen to detect the mutual coherence. If the light from these pinholes result in fringes on a second observation screen, then they are coherent. Note that the light phases at $P_{1}$ and $P_{2}$ will not be constant, but the phase difference between the two can be constant. In that case, an interference pattern will appear.

We will focus on a quasi-monochromatic field, with $\lambda$ as the central wavelength, and $\delta \lambda$ as the spread in wavelengths.

Note that for a point source of radiation, one with dimensions $\ll \lambda$, will always produce spatially coherent radiation. The variations will be perfectly correlated across any wavefront, and the emitted field is spatially coherent.
![[Pasted image 20260421155315.png]]
An image of interference fringes resulting from two point sources.

Say we have two independent point sources. Imagine one is on the axis, and one is $\rho$ off-axis. Since they are point sources, they produce spatial coherence light.
![[Pasted image 20260421172245.png]]
The point on axis is equidistant from the two slits, and so produces fringes of perfect visibility according to:
$$
Y_{n}^{\text{max}} = n \frac{\lambda L}{d} \qquad Y_{n}^{\text{min}} = \left( n+\frac{1}{2} \right) \frac{\lambda L}{d}
$$
For the second point source, however, the distance in path length from the two slits is,
$$
D = \frac{\rho d}{R} \implies  \phi = \frac{2\pi D}{\lambda} = \frac{2\pi \rho d}{\lambda R}
$$
Because of this phase difference, it produces a shifted phase pattern. This pattern is shifted by a distance:$$
\frac{\phi}{2\pi} \frac{\lambda L}{d} = \frac{\rho L}{R}
$$
If the displacement between the interference patterns is small compared to the fringe spacing $\Delta Y$, then there will still remain a series of interference fringes even if both sources are present. This means:
$$
\frac{\rho L}{R} < \Delta Y = \frac{\lambda L}{d} \implies  d < \frac{\lambda}{\rho}R
$$
Note that $\lambda /\rho$ is approximately the diffraction angle for light of wavelength $\lambda$ incident upon and aperture of radius $\rho$.
## Van Cittert-Zernike Theorem
Related the mutual coherence function of the field from an ordinary source to the diffraction pattern for an aperture of the same dimensions as the source.
![[Pasted image 20260421192951.png]]
Consider a plane circular disk source of radius $\rho$. The van Cittert-Zernike theorem tells us that:
$$
\lvert \gamma(\vec{r}_{1}, \vec{r}_{2}, 0) \rvert = \left| \frac{2J_{1}(x)}{x} \right| \qquad x=\frac{2\pi \rho}{\lambda R}\lvert \vec{r}_{1}-\vec{r}_{2} \rvert  = \frac{2\pi \rho d}{\lambda R}
$$
Where $J_{1}$ is the first-order Bessel function. Note that $\lvert \gamma(\vec{r}_{1}, \vec{r}_{2}, 0) \rvert^{2}$ is the Airy pattern associated with the Fraunhofer diffraction by a uniformly illuminated circular aperture of radius $\rho$.

Based on somewhat arbitrary measures, the radiation is considered to have a high degree of spatial coherence over a circular area:
$$
\frac{2\pi \rho d}{\lambda R}\leq 1 \implies  d_\text{coh} = \frac{1}{2\pi} \frac{\lambda R}{\rho} \approx 0.16 \frac{\lambda R}{\rho} = 0.16 \frac{\lambda}{\theta}
$$
Where $\theta=\rho /R$ is the angle subtended by the source at the observation plane.

This coherence distance is what justifies the results of the two-slit experiment described earlier. The light has spatial coherence over a limited area $\approx \pi d^{2}_\text{coh} /4$ and so if the slits move further apart, the coherence of the fields at the two slits decreases. Furthermore, if we decrease $R$ then the coherence distance will also decrease.

This effectively tells us that light from an ordinary source is most coherent when it is far away, and the observation plane is small.
