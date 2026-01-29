# Question 2
---
a.
$$
\Delta \bar{N} = \bar{N}_{2} - \bar{N}_{1} = \bar{N}_{2} - (N - \bar{N}_2)
$$
$$
\Delta \bar{N} = 2 \bar{N}_{2} - N = \frac{s}{1+s} \frac{N}{2} - N
$$
$$
\frac{\Delta \bar{N}}{N} = \frac{1}{2} \frac{s}{1+s} -1
$$
Assuming this is correct than we have something like this
![[Pasted image 20260126104131.png]]

---
b.
According to the textbook, the absorption coefficient is,
$$
a(\nu) = \sigma(\nu) (\bar{N}_{1} - \bar{N}_{2}) = \frac{a_{0}(\nu)}{1+ I_{\nu} / I_{\nu}^{\text{sat}}}
$$
Where,
$$
a_{0}(\nu) = \sigma(\nu)N
$$
In this case we have,
$$
\bar{N}_{1} - \bar{N}_{2} = (N - \bar{N}_{2}) - \left( \frac{s}{1+s} \frac{N}{2} \right) = \left( N - \left( \frac{s}{1+s} \frac{N}{2} \right) \right) - \left( \frac{s}{1+s} \frac{N}{2} \right)
$$
$$
N \left( 1 - \frac{s}{s+1} \right) = \frac{N}{s+1}
$$
Substitute back into definition
$$
a(\nu) = \sigma(\nu) (\bar{N}_{1} - \bar{N}_{2}) = \sigma(\nu) \frac{1}{1+s} N = a_{0}(\nu) \frac{1}{1+s}
$$
As needed.

---
c.
Definition absorption coefficient:
$$
a(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} \left( \frac{g_{2}}{g_{1}} N_{1}-N_{2} \right) S(\nu) = \sigma(\nu) \left( \frac{g_{2}}{g_{1}} N_{1}-N_{2} \right)
$$
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu) = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}}
$$
$$
a_{0}(\nu_{0}) = \sigma(\nu_{0})N = \frac{\lambda^{2}A_{21}}{8\pi} \frac{1}{\pi} \frac{1}{\Gamma} N = \frac{\lambda^{2}A_{21}}{8\pi^{2}\Gamma}N
$$
$$
\sigma(\nu) \frac{1}{1+s}N = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu) \frac{1}{1+s} N = \frac{\lambda^{2}A_{21}}{8\pi} \frac{1}{\pi} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s} N
$$
Absorb the $a_{0}(\nu_{0})$
$$
\frac{\lambda^{2}A_{21}}{8\pi^{2}} N \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s} = a_{0}(\nu_{0}) \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}
$$
$$
a(\nu) = a_{0}(\nu_{0}) \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2} + \left[ (\nu-\nu_{0})^{2}+\Gamma^{2} \right](I_{\nu} /I_{\nu}^{\text{sat}}) }
$$
The value of the spade is therefore,
$$
(\nu-\nu_{0})^{2} + \Gamma^{2}
$$
---
d.
$$
\frac{a(\nu)}{a_{0}(\nu_{0})} = \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+I_{\nu} /I_{\nu}^{\text{sat}}}
$$
Plot should be something like:
$$
f(x) = \frac{1}{\xi^{2}+1} \frac{1}{1+I_{\nu} /I_{\nu}^\text{sat}}
$$
![[Pasted image 20260128203846.png]]
Plots with $I_{\nu} /I_{\nu}^\text{sat}\in \{ 1 /100, 1 /10, 1, 10 \}$ in black, purple, blue, green, respectively
