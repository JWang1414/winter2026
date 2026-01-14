- Read about cases of broadening
# Broadened Absorbers
Broadening can generally happen due to the doppler effect or collisions.

Recall that prior, we had a Lorentzian lineshape function for the expected band of an atom:
$$
L(\nu) = \frac{\delta \nu_{0} /\pi}{(\nu-\nu_{0})^{2}+(\delta \nu_{0})^{2}}
$$
Which in particular is defined to have an integral of 1. We expected that after broadening, we will obtain a new lineshape function $S(\nu)$, but the integral will remain the same.

From last lecture,
$$
\frac{dW}{dt} = \frac{\lambda_{0}^{2}}{2\pi} I_{\nu} \frac{\beta^{2}}{(\omega-\omega_{0})^{2}+\beta^{2}}
$$
We note that the fractional term can be simplified with the Lorentzian lineshape function, and so the expression becomes:
$$
\frac{dW}{dt} = \frac{\lambda_{0}^{2}A_{21}}{8\pi} I_{\nu} L(\nu)
$$
Which is the energy absorption rate for a single atom

After broadening we take $\lambda_{0}\to \lambda$ and $L\to S$ so model the generalized absorption rate is,
$$
\frac{dW}{dt} = \frac{\lambda^{2}A_{21}}{8\pi} I_{\nu} S(\nu)
$$

Lets go back to our common model of an electron transitioning from level 1 to level 2. In this two level system we have established that the rate of change between the two levels is,
$$
\frac{dN_{2}}{dt} = - \frac{dN_{1}}{dt}
$$
Now that we have defined the energy absorption rate, if the energy per transition from one level to another is $h\nu$, then we can also claim,
$$
\frac{dN_{2}}{dt} = \frac{1}{h\nu} \frac{dW}{dt}
$$
# Absorption of Broadband Light
The total rate of absorption is a sum over the generalized absorption rate, governed by the lineshape curve $S(\nu)$
$$
\frac{dW}{dt} = \sum_{\nu} \frac{\lambda^{2}A_{21}}{8\pi} I_{\nu} S(\nu)
$$
Now apply the common continuum limit such that,
$$
\sum_{\nu}I_{\nu} = \int I_{\nu} \, d\nu
$$
- This function is equivalent to $I(\nu)=c\rho(\nu)$ where $\rho(\nu)$ is the EM density

And the resulting function is,
$$
\frac{dW}{dt} = \int \frac{\lambda^{2}cA_{21}}{8\pi} \rho(\nu) S(\nu) \, d\nu \approx \frac{\lambda_{0}^{2}cA_{21}}{8\pi} \rho(\nu_{0}) \int S(\nu) \, d\nu
$$
Recall that this integral is just 1.
- This approximation is valid for the case when the spectrum is far broader in frequency than the absorbing medium

In terms of the two-level system we have defined, we can translate this absorption rate into a numerical rate of change for the number of atoms transitioning between the two levels:
$$
\frac{dN_{1}}{dt} = -\frac{dN_{2}}{dt} = - B_{12} N_{1} \rho(\nu_{0})
$$
Where we have defined the coefficient $B_{21}$.
$$
B_{12} = \frac{A_{21}}{8\pi h} \frac{c^{3}}{\nu_{0}^{3}}
$$
- Notice that the original coefficient out front is equivalent to $h\nu B_{12}$.
