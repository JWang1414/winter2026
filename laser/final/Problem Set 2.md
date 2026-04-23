# Question 2
---
a.
$$
\Delta \bar{N} = \bar{N}_{2} - \bar{N}_{1} = \frac{s}{1+s} \frac{N}{2} - (N-\bar{N}_{2})
$$
$$
\frac{s}{1+s} \frac{N}{2} - N + \frac{s}{1+s} \frac{N}{2} = \frac{s}{1+s} N - N
$$
$$
\Delta \bar{N} = \left( \frac{s}{1+s}-1 \right)N
$$
So we have,
$$
\frac{\bar{N}_{2}}{N} = \frac{1}{2} \frac{s}{1+s} \qquad \frac{\Delta \bar{N}}{N} = \frac{s}{1+s}-1
$$
---
b.
From lecture,
$$
g(\nu) = \sigma(\nu) \left[ \bar{N}_{2} - \frac{g_{2}}{g_{1}} \bar{N}_{1} \right]
$$
Assuming no degeneracy,
$$
a(\nu) = -\sigma(\nu) (\bar{N}_{2} - \bar{N}_{1}) = \sigma(\nu) (\bar{N}_{1} - \bar{N}_{2})
$$
Note that,
$$
\Delta \bar{N} = \bar{N}_{2} - \bar{N}_{1} \implies  \bar{N}_{1} - \bar{N}_{2} = -\Delta \bar{N}
$$
Therefore,
$$
a(\nu) = \sigma(\nu) (-\Delta \bar{N}) = \sigma(\nu) \left[ -\left( \frac{s}{1+s}-1 \right)N \right] = \sigma(\nu) \left( 1-\frac{s}{1+s} \right)N
$$
$$
1-\frac{s}{1+s} = \frac{1+s}{1+s} - \frac{s}{1+s} = \frac{1+s-s}{1+s} = \frac{1}{1+s}
$$
I conclude,
$$
a(\nu) = \sigma(\nu) \frac{1}{1+s}N = a_{0}(\nu) \frac{1}{1+s}
$$
Where $a_{0}(\nu)=\sigma(\nu)N$

---
c.
$$
a_{0}(\nu_{0}) = \sigma(\nu_{0})N = \frac{1}{\pi} \frac{\Gamma}{(\nu_{0}-\nu_{0})^{2}+\Gamma^{2}}N = \frac{1}{\pi} \frac{1}{\Gamma} N = \frac{N}{\pi\Gamma}
$$
$$
a(\nu) = \frac{1}{\pi} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}N = a_{0}(\nu_{0}) \frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}
$$
- This makes it looks like the spade is supposed to be $(\nu-\nu_{0})^{2}+\Gamma^{2}$ but I remember that being incorrect. There's supposed to be some other manipulation you can do, but I forgot it.
# Question 1
---
a.
Assume Lorentzian lineshape cross section
$$
\sigma(\nu) = \frac{\delta \nu_{0}}{\pi} \frac{1}{(\nu-\nu_{0})^{2}+(\delta \nu_{0})^{2}}
$$
Where the FWHM is $2\delta \nu_{0}$.

Assume $\nu_{L}=\nu_{0}$ so this becomes,
$$
\frac{\delta \nu_{0}}{\pi} \frac{1}{(\nu_{0}-\nu_{0})^{2}+(\delta \nu_{0})^{2}} = \frac{1}{\pi(\delta \nu_{0})}
$$
---
b.
$$
\sigma(\nu) = \frac{1}{\pi(\delta \nu_{0})} \approx 6.37 \times 10^{-10}
$$
$$
\lambda_{0}^{2} = 3.6 \times 10^{-13}
$$
Much larger than the cross section for an atom