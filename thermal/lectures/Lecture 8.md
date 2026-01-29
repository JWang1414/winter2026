# Equipartition theorem
Each independent, active, quadratic degree of freedom contributes $kT /2$ to total energy in the canonical ensemble.

So lets say we have some energy contribution like,
$$
E_{i} = \alpha x^{2} + \tilde{E}_{i}(\vec{y})
$$
Where the lower order terms have been grouped into the second term. Notice that they are independent, that is, the second term does not depend on $x$.

In the canonical ensemble we are interested in computing $\mathcal{Z}(T)$
$$
\mathcal{Z}(T) = \sum_{i} e^{ -\beta E_{i} } = \sum_{x, \vec{y}} e^{ -\beta \alpha x^{2} } e^{ -\beta \tilde{E}_{i}(\vec{y}) }
$$
Which we can factorize into,
$$
\sum_{x} e^{ -\alpha \beta x^{2} } \sum_{\vec{y}} e^{ -\beta \tilde{E}_{i}\vec{y} } = \mathcal{Z}_{x} \mathcal{Z}_\text{rest}
$$
So we have the partition split into the quadratic terms and everything else. Now, the ensemble average energy in this system is:
$$
\left< E \right> = -\frac{ \partial \ln \mathcal{Z} }{ \partial \beta } =- \frac{ \partial \ln \mathcal{Z}_{x} }{ \partial \beta } - \frac{ \partial \ln \mathcal{Z_\text{rest}} }{ \partial \beta }
$$
In the continuum limit we have,
$$
\mathcal{Z}_{x} = \sum_{x} e^{ -\alpha \beta x^{2} } = \int_{-\infty}^{\infty} e^{ -\alpha \beta x^{2} } \, \frac{dx}{\delta x} = \frac{1}{\delta x} \sqrt{ \frac{\pi}{\alpha \beta} }
$$
So now we can compute the energy,
$$
\ln \mathcal{Z}_{x} = \frac{1}{2} \ln\left( \frac{\pi}{\alpha\delta x^{2}} \right) = \frac{1}{2} \ln \beta
$$
$$
-\frac{ \partial \ln \mathcal{Z} }{ \partial \beta } = \frac{1}{2\beta} = \frac{kT}{2}
$$
So the final energy in the system is,
$$
\left< E \right> = \frac{1}{2} kT + E_\text{rest}
$$
$$
C_{V}^\text{molar} = \frac{R}{2} (\text{\# indep. quad. DOF})
$$
