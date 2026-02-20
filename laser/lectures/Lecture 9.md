- I missed this class due to illness. These notes are taken from the textbook.
# Fabry Perot Etalon
![[Pasted image 20260219212507.png]]
Consider a monochromatic plane wave incident upon a Fabry-Perot etalon. The first interface ($n'\to n$) between the two media has reflection and transmission coefficients $r$ and $t$, respectively. For the second interface, we denote the coefficients to be $r'$ and $t'$.
- Recall that these coefficients are given by the Fresnel formulas

If $A_\text{in}$ is the complex amplitude of the incident wave, then the amplitude of the wave reflected from the first interface is:
$$
A_{0} = \sqrt{ r } A_\text{in} e^{ i\pi } = -\sqrt{ r } A_\text{in}
$$
Where the phase shift by $\pi$ results from the assumption $n>n'$.

Another possible form of reflected wave is one where it bounces between the two interfaces one time, and then reflects out. This one would have amplitude,
$$
\sqrt{ tr't' } A_\text{in}
$$
It would have the more complicated phase shift:
$$
\frac{2\pi}{\lambda} (2dn) = \frac{4\pi \nu nd}{c} = \Phi
$$
The full complex amplitude can be found to be,
$$
A_{1} = \sqrt{ r'tt' } e^{ i\Phi } A_\text{in}
$$
Now, consider the cases where light bounces around in the inside 2, 3, or more times. The total reflected field from these reflections is:
$$
A_{R} = A_{0} + A_{1} + \dots = \left[ -\sqrt{ r } + \sqrt{ r' } \sqrt{ tt' } e^{ i\Phi } \left( 1 + \sqrt{ r'r' } e^{ i\Phi } + \sqrt{ r'r'r'r' } e^{ 2i\Phi } + \dots \right)  \right] A_\text{in}
$$
Furthermore, from the Fresnel formulas we know:
$$
r=r' = \left( \frac{n-n'}{n+n'} \right)^{2}
$$
Define the new variables,
$$
R=r=r' \qquad T = \sqrt{ tt' }
$$
Where from energy conservation and the Fresnel formulas,
$$
R+T=1
$$
Using this notation we can simplify the above to:
$$
\frac{A_{R}}{A_\text{in}} = -\sqrt{ R } \left[ 1 - Te^{ i\Phi } (1 + R e^{ i\Phi } + R^{2} e^{ 2i\Phi } + \dots) \right]
$$
Which is a geometric series, and so can therefore be evaluated be,
$$
\frac{A_{R}}{A_\text{in}} = -\sqrt{ R } \left( 1-\frac{Te^{ i\Phi }}{1 - R e^{ p\Phi }} \right) = - \frac{1-e^{ i\Phi }}{1-R e^{ i\Phi }} \sqrt{ R }
$$
The fraction of the incident intensity is given by the Airy formula,
$$
\frac{I_{R}}{I_\text{in}} = \left| \frac{A_{R}}{A_\text{in}} \right| ^{2} = \frac{4R \sin ^{2}(\Phi /2)}{(1-R)^{2} + 4R \sin ^{2}(\Phi /2)}
$$
And the associated transmitted intensity is,
$$
\frac{I_{T}}{I_\text{in}} = \frac{(1-R)^{2}}{(1-R)^{2} + 4R \sin ^{2}(\Phi /2)}
$$
It can be shown for any non-normal incidence we simply replace $\Phi$ with the new representation,
$$
\Phi = \frac{4\pi \nu nd}{c} \cos\theta
$$
So by observation we can tell the Fabry-Perot etalon perfectly transmits when,
$$
\frac{\Phi}{2} = m\pi \qquad m\in \mathbb{N}
$$
Which is the same condition we obtain considering just a single reflection inside the etalon.

So, how does the transmission fall off as the frequency $\nu$ is displaced from the resonance frequency? To make this easier, re-write the reflection intensity as,
$$
\frac{I_{R}}{I_\text{in}} = \frac{1}{1+F \sin ^{2}(\Phi /2)} \qquad F = \frac{4R}{(1-R)^{2}}
$$
The transmitted intensity therefore looks something like:
![[Pasted image 20260219214752.png]]
Notice how for larger $F$ ($R\to 1$) a narrower band of frequencies is transmitted. This physically manifests as a trade-off between the throughput and resolution of the bandwidths for transmitted frequencies.

The resonance frequency spacing is called the *free spectral range* of the Fabry-Perot etalon. The ratio of the free spectral range to the half-width of the frequency band centred on a resonance frequency may be shown to be,
$$
\mathcal{F} = \frac{\pi}{2} \sqrt{ F } = \frac{\pi \sqrt{ R }}{1-R}
$$
Where $\mathcal{F}$ is called the finesse of the Fabry-Perot etalon. The greater the *finesse*, the sharper the bands of transmitted frequencies relative to their separation.
- $\mathcal{F}$ is typically around 30-100
