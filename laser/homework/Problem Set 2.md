# Question 1
---
a.
The cross-section for absorption is defined to be:
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
Where $S(\nu)$ is the line function. Assuming a Lorentzian lineshape function, $S$ will be of the form:
$$
S(\nu) = L(\nu) = \frac{1}{\pi} \frac{\delta}{(\nu-\nu_{0})^{2}+\delta^{2}} = \frac{1}{\pi} \frac{\delta \nu}{(\nu-\nu_{0})^{2}+(\delta \nu)^{2}}
$$
Where $\delta \nu$ is the half-width at half-maximum. When $\nu_{L}=\nu_{0}$ the lineshape function reduces to:
$$
L(\nu_{0}) = \frac{1}{\pi} \frac{\delta \nu}{(\nu_{0}-\nu_{0})^{2}+(\delta \nu)^{2}} = \frac{1}{\pi(\delta \nu)}
$$
And the cross-section is:
$$
\sigma(\nu_{0}) = \frac{\lambda_{0}^{2}A_{21}}{8\pi} L(\nu_{0}) = \frac{\lambda_{0}^{2}A_{21}}{8\pi^{2}(\delta \nu)}
$$
Which is approximately equal to:
$$
\frac{(600\times 10^{-9})^{2}(2\times 10^{8})}{8\pi^{2}(10^{9} /2)} \approx 1.82 \times 10^{-15}
$$
Checking the units...
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
From lecture, the transmitted fraction of light is:
$$
I_{\nu}(z) = I_{\nu}(0) e^{ g(\nu)z }
$$
Where $z$ is the distance travelled, $I_{\nu}$ is the intensity, and $g(\nu)$ is the gain coefficient.

Ignoring degeneracy, setting $\nu_{L}=\nu_{0}$, and assuming all atoms remain in the ground state ($N_{2}=0$),
$$
\frac{I_{\nu}(z)}{I_{\nu}(0)} = e^{ g(\nu_{0})z } = e^{ -N_{1}\sigma(\nu_{0})z }
$$
Which is approximately,
$$
\exp \{ -(10^{16}) (1.82\times 10^{-15})(0.02) \} \approx 0.694
$$
So around 70% of light is transmitted.

---
d.
As a function of $\nu_{L}$, the transmitted fraction of light is,
$$
\exp \{ -N_{1} \sigma(\nu_{L})z \} = \exp \left\{  -N_{1} \frac{\lambda_{0}^{2}A_{21}}{8\pi^{2}} \frac{(\delta \nu)z}{(\nu_{L}-\nu_{0})^{2}+(\delta \nu)^{2}}  \right\}
$$
Where I have re-introduced the lineshape function, since $\nu_{L}$ is no longer held constant.

---
e.
The transmitted fraction of light becomes:
$$
\exp \{ -(10^{17})(1.82 \times 10^{-15}) (0.02) \} \approx 0.0261
$$
So only around 2.6% of light is transmitted in this case.

- I believe that because the gas inside is denser, it is more prone to absorbing the laser light. Therefore increasing the frequencies of light it can absorb.
# Question 2
---
a.
According to the definition of $\Delta \bar{N}$:
$$
\Delta \bar{N} = \bar{N}_{2} - \bar{N}_{1} = \bar{N}_{2} - (N - \bar{N}_2) = 2 \bar{N}_{2} - N = \frac{s}{1+s} \frac{N}{2} - N
$$
So the two plots of interest are:
$$
\frac{\bar{N}_{2}}{N} = \frac{1}{2} \frac{s}{1+s} \qquad \frac{\Delta \bar{N}}{N} = \frac{1}{2} \frac{s}{1+s} - 1
$$
![[Pasted image 20260126104131.png]]

---
b.
From lecture, the definition of the absorption coefficient is:
$$
-a(\nu) = \sigma(\nu) \left[ \bar{N}_{2} - \frac{g_{2}}{g_{1}} \bar{N}_{1} \right]
$$
Ignoring the effective of degeneracy, this becomes:
$$
a(\nu) = \sigma(\nu) \left( \bar{N}_{1} - \bar{N}_{2} \right)
$$
Compute,
$$
\begin{align}
\bar{N}_{1} - \bar{N}_{2} & = N - \bar{N}_{2} - \bar{N}_{2} \\
 & = N - 2 \left( \frac{s}{1+s} \frac{N}{2} \right) \\
 & = N \left( 1 - \frac{s}{1+s} \right) \\
 & = \frac{N}{1+s}
\end{align}
$$
Substitute back in,
$$
a(\nu) = \sigma(\nu) \frac{1}{1+s}N = a_{0}(\nu) \frac{1}{1+s}
$$
As needed.

---
c.
With this lineshape the cross-section is:
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu) = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}}
$$
And $a_{0}(\nu_{0})$ is therefore:
$$
a_{0}(\nu_{0}) = \sigma(\nu_{0})N = \frac{\lambda^{2}A_{21}}{8\pi} \frac{1}{\pi} \frac{1}{\Gamma} N = \frac{\lambda^{2}A_{21}}{8\pi^{2}\Gamma}N
$$
Expanding out the absorption coefficient I find:
$$
a(\nu) = \sigma(\nu) \frac{1}{1+s}N = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}N
$$
Absorbing some of these factors into $a_{0}(\nu_{0})$ places a $\Gamma$ into the numerator:
$$
a(\nu) = a_{0}(\nu_{0}) \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}
$$
Evaluate, and substitute in the definition for $s$:
$$
a(\nu) = a_{0}(\nu_{0}) \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2} + \left[ (\nu-\nu_{0})^{2}+\Gamma^{2} \right](I_{\nu} /I_{\nu}^{\text{sat}}) }
$$
The value of the spade is therefore,
$$
(\nu-\nu_{0})^{2} + \Gamma^{2}
$$
---
d.
The function of interest is:
$$
\frac{a(\nu)}{a_{0}(\nu_{0})} = \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+I_{\nu} /I_{\nu}^{\text{sat}}}
$$
![[Pasted image 20260128203846.png]]
Plots of $a(\nu) /a_{0}(\nu_{0})$ as a function of $(\nu-\nu_{0}) /\Gamma$ with $I_{\nu} /I_{\nu}^\text{sat}\in \{ 1 /100, 1 /10, 1, 10 \}$ in black, purple, blue, green, respectively
