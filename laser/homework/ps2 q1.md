# Question 1
---
a.
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
Lineshape function is,
$$
L(\nu) = \frac{1}{\pi} \frac{\delta}{(\nu-\nu_{0})^{2}+\delta^{2}}
$$
Where $\delta$ is the half-width at half-maximum. Under the condition $\nu_{L}=\nu_{0}$ we have
$$
L(\nu) = \frac{1}{\pi} \frac{\delta}{\delta^{2}} = \frac{1}{\pi} \frac{1}{\delta}
$$
Cross-section should be,
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} \frac{1}{\pi} \frac{1}{\delta} = \frac{\lambda^{2}A_{21}}{8\pi^{2}\delta}
$$
$$
\frac{(600\times 10^{-9})^{2}(2\times 10^{8})}{8\pi^{2}(10^{9} /2)} \approx 1.82 \times 10^{-15}
$$
Check units:
$$
\frac{\text{m}^{2} \times \text{s}^{-1}}{\text{s}^{-1}} = \text{m}^{2}
$$
So the cross section has units of area, as one would expect.

---
b.
Note that
$$
\lambda_{0}^{2} = (600\times 10^{-9})^{2} \propto 10^{-13}
$$
The result I obtain is within the order of $10^{-15}$. Two orders of magnitude smaller.
- Maybe it's smaller because of Doppler broadening? But I would expect "broadening" to make the cross section larger
---
c.
According to lecture the transmitted intensity of light is,
$$
I_{\nu}(z) = I_{\nu}(0) e^{ g(\nu)z }
$$
Where $z$ is the distance travelled, $I_{\nu}$ is the intensity, and $g(\nu)$ is the gain coefficient.

Ignoring degeneracy, and assuming all atoms remain in the ground state ($N_{2}=0$),
$$
\frac{I_{\nu}(z)}{I_{\nu}(0)} = e^{ g(\nu)z } = e^{ -N_{1}\sigma(\nu)z }
$$
For $\nu_{L}=\nu_{0}$ this becomes,
$$
\exp \left\{  -\frac{N_{1}\lambda^{2}A_{21}}{8\pi^{2}(\delta \nu_{0})}z  \right\}
$$
- This can be computed to be a number
- $N_{1}$ should be the volume from the cross section multiplied by the particle density
- I have to change the formatting of everything anyways so I'm not going to bother changing this
---
d.
Since $\nu_{L}$ is no longer constant the function turns into:
$$
e^{ -N_{1}\sigma(\nu)z } = \exp \left\{ -N_{1} \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\delta \nu_{0}}{(\nu_{L}-\nu_{0})^{2}+(\delta \nu_{0})^{2}} z \right\}
$$
Plot as a function of $\nu_{L} /(\delta \nu)$ so set $\delta \nu=1$ and plot as a function of $\nu_{L}$.
$$
\exp \left\{ -N_{1} \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{1}{(\nu_{L}-\nu_{0})^{2}+1} z \right\}
$$
---
e.
Mathematically, this question appears to have no new math. Just plug a new number into the equations.

TODO: Compute numbers, plot the data, and interpret e