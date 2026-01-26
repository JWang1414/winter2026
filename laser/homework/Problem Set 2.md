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
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
$$
I_{\nu}^{\text{sat}} \approx h\nu_{0} \frac{A_{21}}{2\sigma(\nu)}
$$
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} \left( \frac{1}{\pi} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \right)
$$
---
d.
$$
\frac{\nu-\nu_{0}}{\Gamma} = \zeta \implies  \nu-\nu_{0} = \zeta \Gamma
$$
if I set $\Gamma=1$ than this is therefore a plot of
$$
\frac{1}{\zeta^{2}+1+\xi I_{\nu} /I_{\nu_{0}}^{\text{sat}}}
$$
- But I still need to find $\xi$ from the previous question