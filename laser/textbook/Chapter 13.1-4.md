# Brightness
Recall that a thermal source of radiation has spectral energy density $\rho(\nu)$. If this wide band is divided into narrow elements $\delta \nu$ the intensity of radiation at some frequency $\nu$ is,
$$
I_{\nu} = \int_{\delta \nu} I(\nu) \, \delta \nu \approx I(\nu)\delta \nu = \frac{1}{2} c \rho(\nu)\delta \nu = \frac{(2\pi h\nu^{3} /c^{2})\delta \nu}{e^{ h\nu /k_{B}T }-1}
$$
The *brightness*, or *radiance* of a source is the emitted power per units area per units solid angle. Notably, the brightness of a source is invariant. It is, however, possible to change the intensity of the beam.

The brightness for the lowest-order Gaussian beam is:
$$
B = \frac{I_\text{max}}{\Omega} = \frac{2\text{Pwr}}{\lambda^{2}}
$$
Where the solid angle is,
$$
\Omega = \pi\theta^{2} = \frac{\lambda^{2}}{\pi w_{0}^{2}}
$$
And the intensity of a Gaussian beam at the waist is,
$$
I_\text{max} = \frac{2\text{Pwr}}{\pi w_{0}^{2}}
$$
Because lasers are very directional, the brightness of lasers tends to be very high.

Brightness is important experimentally because the intensity that can be obtained in the focal place of a lens is proportional to the brightness of the beam.
# The Coherence of Light
Recall that for two slits, separated by $d$, the difference in distance from the slits to the observation screen is approximately,
$$
l = d \sin\theta \approx d \frac{Y}{L}
$$
Where $l$ is the difference, and $\theta$ is the is the angle from the normal. $Y$ is the $y$-distance from the normal on the observation screen, and $L$ is the distance between the observation screen and the slits.

The intensity is maximized when the optical path difference is an integer number of wavelengths:
$$
\frac{\omega}{c}=\frac{2\pi}{\lambda} \implies  \frac{\omega(l_{2}-l_{1})}{c} = 2\pi n
$$
And at a minimum in half-wavelengths:
$$
\frac{\omega(l_{2}-l_{1})}{c} = 2\pi\left( n+\frac{1}{2} \right)
$$
In terms of the observation screen, this yields,
$$
Y_{n}^{\text{max}} = n \frac{\lambda L}{d} \qquad Y_{n}^{\text{min}} = \left( n+\frac{1}{2} \right) \frac{\lambda L}{d}
$$
The separation for an ideal, monochromatic source is therefore,
$$
\Delta Y = \frac{\lambda L}{d}
$$
However, for non-ideal sources, if the slits are too far away from each other, or the observation screen too close, we observe that the intensity patterns washes out and disappears.

If the difference in fringe separation for two wavelengths separated by $\delta \lambda$ is,
$$
\delta(\Delta Y) = \frac{(\delta \lambda)L}{d}
$$
Then the "washing out" of the interference pattern is minimal if:
$$
\frac{\delta(\Delta Y)}{\Delta Y} = \frac{\delta \lambda}{\lambda} = \frac{\delta \nu}{\nu} \ll 1
$$
If this inequality holds, then the bandwidth is called quasi-monochromatic.

The visibility of these interference fringes is defined to be,
$$
V = \frac{I_\text{max}-I_\text{min}}{I_\text{max}+I_\text{min}}
$$
$V=0$ when $I_\text{min}=I_\text{max}$, and $V=1$ when $I_\text{min}=0$. The visibility is a measure of the sharpness of the interference fringes, and the coherence of light.
# The Mutual Coherence Function
In the young's interferometer, the condition for diffraction to occur is $a\ll d$, where $a$ is the width of the slits, and $d$ is the distance between the slits. So the slits must be much narrower than their separation.

A perfectly monochromatic field is typically written like:
$$
E(\vec{r}, t) = \mathcal{E}(\vec{r}) e^{ -i\omega t }
$$
For some complex electric field. For a quasi-monochromatic field we instead use,
$$
E(\vec{r}, t) = \sum_{m} \mathcal{E}_{m}(\vec{r}) e^{ -i\omega_{m}t } \to  \int_{0}^{\infty} \tilde{\mathcal{E}}(\vec{r}, \omega) e^{ -i\omega t } \, d\omega
$$
However, it is typically more useful to write,
$$
E(\vec{r}, t) = \mathcal{E}(\vec{r}, t) e^{ -i\omega t }
$$
And assume that $\mathcal{E}(\vec{r}, t)$ varies slowly in time.

Now, given that:
$$
\mathrm{Re}\left[ E(\vec{r}, t) \right]  = \frac{1}{2} \left[ E(\vec{r}, t) + E^*(\vec{r}, t) \right]
$$
We may determine that:
$$
I(\vec{r}, t)= c\epsilon_{0} \left[ \mathrm{Re}\{ E(\vec{r}, t) \} \right] ^{2} \approx \frac{c\epsilon_{0}}{2} \lvert \mathcal{E}(\vec{r}) \rvert ^{2}
$$
This approximation arises because the terms oscillating with frequency $2\omega$ are undetectable and average to 0.

This result for the intensity is also valid the quasi-monochromatic case.

In addition to these rapid fluctuations in the intensity we have discarded, we must also account for the random fluctuations from spontaneous emission, and the fluctuations in the atmosphere and mechanical vibrations of the optical elements. We will accomplish this using an ensemble average. Using this notation, the intensity becomes,
$$
\left< I(P, t) \right> = \frac{c\epsilon_{0}}{2} \left< E(P, t) E^*(P, t) \right>
$$
Where $P$ is a point on the observation screen.

Now, the field $E(P, t)$ resulting from one of the slits $E(S_{1}, t)$ can be modelled by:
$$
E_{1}(P, t) = K_{1}\left( S_{1}, t-\frac{l_{1}}{c} \right)
$$
Where $K_{1}$ is a pure dimensionless imaginary number that is a function of the geometry of the experiment. The *retardation time* $l_{1} /c$ is the time it takes for light to propagation from $S_{1}$ to $P$.

The total field from both slits is:
$$
E(P, t) = E_{1}(P, t) + E_{2}(P, t)
$$
Which yields the intensity:
$$
I(P, t) = \frac{c\epsilon_{0}}{2} \left[ \left\lvert  K_{1} E\left( S_{1}, t-\frac{l_{1}}{c} \right)  \right\rvert ^{2}+\left\lvert  K_{2} E\left( S_{2}, t-\frac{l_{1}}{c} \right)  \right\rvert ^{2} \right] + c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\left\{  E^*\left( S_{1}, t-\frac{l_{1}}{c} \right) E\left( S_{2}, t-\frac{l_{2}}{c} \right)  \right\}
$$
Taking the ensemble average of this result:
$$
\left< I(P, t) \right>  = \frac{c\epsilon_{0}}{2} \left[\lvert K_{1} \rvert^{2}  \left< \left\lvert  E\left( S_{1}, t-\frac{l_{1}}{c} \right)  \right\rvert ^{2} \right> +\lvert K_{2} \rvert ^{2} \left< \left\lvert  E\left( S_{2}, t-\frac{l_{1}}{c} \right)  \right\rvert ^{2} \right>  \right] + c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\left< E^*\left( S_{1}, t-\frac{l_{1}}{c} \right) E\left( S_{2}, t-\frac{l_{2}}{c} \right) \right>
$$
This latter portion:
$$
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) = \left< E^*(\vec{r}_{1}, t_{1})E(\vec{r}_{2},t_{2}) \right>
$$
Is called the mutual coherence function of the fields at $\vec{r}_{1}, t_{1}$ and $\vec{r}_{2}, t_{2}$. In terms of the mutual coherence function, the intensity becomes,
$$
\left< I(P, t) \right> = \left< I_{1}(P, t) \right> + \left< I_{2}(P, t) \right> + c\epsilon_{0} \lvert K_{1}K_{2} \rvert \mathrm{Re}\left[ \Gamma\left( S_{1}, t-\frac{l_{1}}{c}; S_{2}, t-\frac{l_{2}}{c} \right) \right]
$$
Notice that $\left< I_{i}(P, t) \right>$ is the intensity that would be recorded at $P$ is slit $S_{i}$ were acting alone. This tells us that the total intensity at the observation screen is not simply the sum of the intensities $I_{1}$ and $I_{2}$, unless the mutual coherence function vanishes.