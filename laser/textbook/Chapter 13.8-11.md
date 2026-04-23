# Spatial Coherence of Laser Radiation
Lasers are particularly useful because they combine spatial coherence with high intensity.

Lasers oscillating with a single transverse mode have perfect spatial coherence. However, if there is more than one transverse mode, than the spatial coherence drops drastically. Laser operating on many transverse modes has spatial coherence properties much like those of ordinary sources of radiation, where the van Cittert–Zernike theorem is applicable.

This arises because difference transverse modes have different field distributions. The different modes are therefore being excited by different groups of active atoms, and so are associated with independent sources. This is close to the model for an ordinary source of radiation.

Experimentally, it is often quite important to maintain single mode oscillation. It does, however, come at the cost of power.
# Diffraction of Laser Radiation
For a spatially coherent beam propagating in free space, the divergence angle obeys the relation,
$$
\theta \propto \frac{\lambda}{D}
$$
Where $D$ is the beam diameter. If the beam is only partially coherent, the Huygens wavelets do not all add up coherently. So for a beam that is spatial coherence over distances $d<D$ across the beam,
$$
\theta \propto \frac{\lambda}{d} > \frac{\lambda}{D}
$$
So the divergence angle is greater.

The easiest way to reduce the divergence angle is to increase the beam diameter. This is often done through the use of a Keplerian telescope. The final and initial angles after passage through the telescope are related by:
$$
\frac{\theta_{f}}{\theta_{i}} = \frac{D_{i}}{D_{f}} = \frac{1}{M_{T}}
$$
Where $M_{T}$ is the magnification of the telescope.

Lasers cannot be focused to a point because of diffraction. Since diffraction sets the ultimate lower limit on the beam spread, we say we have reached the diffraction limit.
# Coherence and the Michelson Interferometer
If we take $\vec{r}_{1}=\vec{r}_{2}=\vec{r}$, then $\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2})$ measured the temporal coherence. The mutual coherence at the same point in space, but at two different times. Generally speaking, we are interested in $\Gamma(\vec{r}, \vec{r}, \tau)$ where $\tau=t_{2}-t_{1}$ is the difference in the times.
![[Pasted image 20260421231134.png]]
The textbook goes through the derivation for the intensity at the output of a Michelson interferometer. Recall that it is:
$$
\left< I(P) \right>  = \frac{1}{2} \left< I(R) \right> \left[ 1+\mathrm{Re}\{ \gamma(R, R, \tau) \} \right]
$$
Where $\left< I(R) \right>$ is the intensity of the input beam, and $\gamma$ is the complex degree of coherence.
$$
\gamma(R, R, \tau) = \frac{c\epsilon_{0}}{2} \frac{\Gamma(R, R, \tau)}{\left< I(R) \right> }
$$
The mutual coherence function for this system depends only on the path length difference:
$$
\frac{l_{1}-l_{2}}{c} = \tau
$$
In the case of perfectly monochromatic light, $\gamma$ is known. The intensity becomes:
$$
\left< I(P) \right> = \left< I(R) \right>  \cos ^{2}\left[ \frac{2\pi}{\lambda}(d_{1}-d_{2}) \right]
$$
Where $d_{i}$ are the distances of the arms.

Constructive and destructive interference occurs are $P$ when:
$$
\lvert d_{1}-d_{2} \rvert =\lambda \qquad \lvert d_{1}-d_{2} \rvert =\left( n+\frac{1}{2} \right)\lambda
$$
Where $n\in \mathbb{N}$. So, as the arm separation is varied, there is a sequence of alternately bright and dark spots.

For quasi-monochromatic light, the intensity is instead:
$$
\left< I(P) \right> = \frac{1}{2} \left< I(R) \right>  \left[ 1+ \lvert \gamma(R, R, \tau) \rvert \cos\left( \frac{2\pi}{\lambda}(d_{1}-d_{2}) \right) \right]
$$
And the visibility in this case is:
$$
V = \frac{\left< I(P) \right>_\text{max} - \left< I(P) \right>_\text{min} }{\left< I(P) \right>_\text{max} + \left< I(P) \right>_\text{min}} = \lvert \gamma(R, R, \tau) \rvert
$$
The Michelson interferometer is used to measure temporal coherence, as opposed to the Young two-slit interferometer, which is used to measure spatial coherence.
# Temporal Coherence
Experimentally, we find that the visibility will decrease for larger $\tau$ and for larger bandwidths $\delta \nu$.

Suppose we have some radiation of spectral width $\delta \lambda$ incident on a Michelson interferometer. Each wavelength component of the incident radiation is associated with a different pattern of bright and dark spots as $\lvert d_{1}-d_{2} \rvert$ is varied.

Assume that the intensity is constant for wavelength between $\lambda\pm \delta \lambda /2$ like so:
![[Pasted image 20260422234101.png]]

The interference pattern will be smeared out if the largest wavelength $\lambda+\delta \lambda /2$ corresponds with an intensity maximum, and $\lambda-\delta \nu /2$ corresponds with a minimum. This yields the following system of equations:
$$
\begin{align}
\lvert d_{1}-d_{2} \rvert  & = n \left( \lambda+\frac{1}{2}\delta \lambda \right) \\
\lvert d_{1}-d_{2} \rvert  & = \left( n+\frac{1}{2} \right) \left( \lambda - \frac{1}{2}\delta \lambda \right)
\end{align}
$$
Solving this system of equations yields the condition:
$$
\lvert d_{1}-d_{2} \rvert \left( \frac{1}{\lambda-\delta \lambda /2} - \frac{1}{\lambda+\delta \lambda /2} \right) = \frac{1}{2}
$$
Use the approximation $\delta \lambda\ll \lambda$ to find:
$$
\lvert d_{1}-d_{2} \rvert  = c \tau = \frac{\lambda^{2}}{2(\delta \lambda)}
$$
Now, since $\lambda=c /\nu$,
$$
\left| \frac{d\lambda}{d\nu} \right|  = \frac{c}{\nu^{2}} = \frac{\lambda}{\nu}
$$
Which therefore tells us that for small increments,
$$
\frac{\delta \lambda}{\delta \nu} = \frac{\lambda}{\nu} \implies  \frac{\delta \lambda}{\lambda} = \frac{\delta \nu}{\nu}
$$
Substitute this into our previous condition to obtain:
$$
c\tau = \frac{\lambda \nu}{2(\delta \nu)} = \frac{c}{2(\delta \nu)}
$$
Which can be further simplified into:
$$
\tau = \frac{\lvert d_{1}-d_{2} \rvert }{c} = \frac{1}{2(\delta \nu)}
$$
Physically, this is the path length difference in the Michelson interferometer where  the interference pattern will be smeared out. Any separation larger than $\tau$ should result in a very low visibility.

In agreement with experiments, $\tau$ decreases for increasing bandwidth $\delta \nu$.

Generally speaking, since intensity distributions are not uniform as we have modelled, it is conventional to define:
$$
\tau _\text{coh} = \frac{1}{2\pi(\delta \nu)}
$$
As the coherence time for quasi-monochromatic radiation of bandwidth $\delta \nu$. The associated coherence length of the Michelson interferometer is $c\tau _\text{coh}$.

- Lasers with a single transverse mode have perfect spatial coherence, but the temporal coherence has dependence on the longitudinal modes
- Generally, as the number of longitudinal modes increases, the temporal coherence will decrease
