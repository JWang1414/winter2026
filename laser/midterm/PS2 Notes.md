# Question 1
---
a.
The cross-section for absorption is,
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
For a Doppler-broadened medium we have,
$$
S(\nu) = \frac{1}{\delta \nu} \sqrt{ \frac{4\ln 2}{\pi} } \exp \left\{  -4\ln 2 \frac{(\nu-\nu_{0})^{2}}{(\delta \nu)^{2}}  \right\}
$$
Where we have,
$$
S(\nu_{0}) = \frac{1}{\delta \nu} \sqrt{ \frac{4\ln 2}{\pi} }
$$
Which has units of 1/frequency or $1 /\text{Hz}$.

If you substitute in the values for,
$$
\sigma(\nu_{0}) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu_{0})
$$
Then you should find,
$$
2.7 \times 10^{-15} \text{ m}^{2}
$$
---
b.
Comparing the two values:
$$
\frac{\sigma(\nu_{0})}{\lambda_{0}^{2}} = 0.007
$$
So $\sigma(\nu_{0})$ is two orders of magnitude smaller. This arises because most atoms are off-resonance, and $\sigma \approx \lambda^{2}$ applied only in the case of resonant scattering.

---
c.
Absorption length is,
$$
a = \sigma_{0} \rho
$$
Where $\rho$ is the density.

The result you should find for the fractional absorption is,
$$
\exp \{ -aL \} = \exp \{ -\sigma_{0}\rho L \} \approx 0.58
$$
Where $L$ is the length of the cylinder.

---
d.
I did this portion correctly. The FWHM I find is correct.

---
e.
For the final case with $\rho=10^{17}$ the peak absorption swaps to 99.5% and a FWHM 1.7, about 70% wider that the original

This arises because the FWHM is for $S(\nu)$ and $a(\nu)$, but $T(\nu) \propto \exp \{ S(\nu) \}$. Because this isn't a linear mapping, the absorption around resonance is saturated.
# Question 2
---
c.
Assume the Lorentzian line shape:
$$
S(\nu) = \frac{1}{\pi} \frac{\Gamma}{(\nu-\nu_{0})^{2}+p^{2}} = \frac{1}{\pi\Gamma} \frac{1}{1+x^{2}}
$$
Where we have defined,
$$
x \equiv \frac{\nu-\nu_{0}}{\Gamma}
$$
Under this notation, the cross-section for this line shape is,
$$
\sigma(\nu) = \sigma(\nu_{0}) \frac{1}{1+x^{2}}
$$
So,
$$
a(\nu) = a_{0}(\nu) \frac{1}{1+s} = a_{0}(\nu_{0}) \frac{1}{1+x^{2}} \frac{1}{1+s}
$$
Recall that,
$$
s = \frac{\sigma(\nu)}{\sigma(\nu_{0})} \frac{I_{\nu}}{I^{\text{sat}}_{\nu_{0}}} = \frac{1}{1+x^{2}} \frac{I}{I_\text{so}}
$$
The final result you should find is,
$$
\frac{a(\nu)}{a(\nu_{0})} = \frac{1}{1+x^{2}} \frac{1}{1+ \frac{1}{1+x^{2}}(I /I_{s})} = \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2} + \Gamma^{2}(I /I^{\text{sat}}_{\nu_{0}})}
$$
So the pre-factor of interest is $\Gamma^{2}$

---
d.
Fundamentally, what's happening is that for larger $I_{\nu} /I_{\nu_{0}}^{\text{sat}}$ the peak will broaden. This is most obvious if the peaks are normalized.
