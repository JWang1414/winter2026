# Question 1
---
a.
Cross-section should be,
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
Where the lineshape function is,
$$
L(\nu) = \frac{(\delta \nu_{0}) /\pi}{(\nu-\nu_{0})^{2}+(\delta \nu_{0})^{2}}
$$
Should be able to solve this from here by plugging in numbers.

---
c.
For this use we use,
$$
I_{\nu}(z) = I_{\nu}(0) e^{ g(\nu)z }
$$
So the result we are interested in is,
$$
e^{ g(\nu)z }
$$
And you can solve for the absorption coefficient using the $\sigma(\nu)$ from above.
# Question 2
---
a.
$$
\frac{\bar{N}_{2}}{N} = \frac{s}{1+s} \frac{1}{2}
$$
$$
\Delta \bar{N} = \bar{N}_{2} - \bar{N}_{1} = \bar{N}_{2} -(N - \bar{N}_{2}) = 2\bar{N}_{2} - N
$$
$$
\Delta \bar{N} = 2 \left( \frac{s}{1+s} \frac{N}{2} \right) - N
$$
$$
\frac{\Delta \bar{N}}{N} = \frac{s}{1+s} - 1
$$
---
b.
$$
-a(\nu) = \sigma(\nu) \left[ \bar{N}_{2} - \frac{g_{2}}{g_{1}} \bar{N}_{1} \right]
$$
In this problem,
$$
a(\nu) = \sigma(\nu) \left[ \bar{N}_{1} - \bar{N}_{2} \right]
$$
$$
\bar{N}_{1} - \bar{N}_{2} = N - \bar{N}_{2} - \bar{N}_{2} = N-2\bar{N}_{2}
$$
$$
N - 2 \left( \frac{s}{1+s} \frac{N}{2} \right) = \frac{N}{1+s}
$$
$$
a(\nu) = \sigma(\nu) \frac{1}{1+s} N = a_{0}(\nu) \frac{1}{1+s}
$$
Where $a_{0}(\nu)=\sigma(\nu)N$

---
c.
$$
a_{0}(\nu) = \sigma(\nu)N = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu) = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}}
$$
$$
a_{0}(\nu_{0}) = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu_{0}-\nu_{0})^{2}+\Gamma^{2}} = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{1}{\Gamma}
$$
$$
a(\nu) = \frac{\lambda^{2}A_{21}}{8\pi^{2}} \frac{\Gamma}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s} = a_{0}(\nu_{0})\frac{\Gamma^{2}}{(\nu-\nu_{0})^{2}+\Gamma^{2}} \frac{1}{1+s}
$$
- And then apparently I got this question wrong so I need to check the answers
