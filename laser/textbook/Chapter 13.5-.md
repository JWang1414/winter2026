# Complex Degree of Coherence
The normalized form for the mutual coherence function is called the complex degree of coherence.

Consider a source of radiation that has reached a "steady-state" operation. This property is called *stationarity*. In particular, for stationary fields, the mutual coherence function depends only on the difference $t_{2}-t_{1}$. That is:
$$
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) = \Gamma(\vec{r}_{1}, t_{1}+s; \vec{r}_{2}, t_{2}+s)
$$
For some time increment $s$ and:
$$
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) = \Gamma(\vec{r}_{1}, \vec{r}_{2}, t_{2}-t_{1})
$$
As it turns out, for a stationary field the intensity simplifies into:
$$
\left< I(P, t) \right>  = \left< I(P) \right> = \frac{c\epsilon_{0}}{2} \Gamma(P, P, 0)
$$
As an example, lets consider a monochromatic field:
$$
\begin{align}
\Gamma(\vec{r}_{1}, t_{1}; \vec{r}_{2}, t_{2}) & = \left< E^*(\vec{r}, t_{1})E(\vec{r}_{2}, t_{2}) \right> \\
 & = \left< \mathcal{E}^*(\vec{r}_{1}) \mathcal{E}(\vec{r}_{2}) e^{ -i\omega(t_{2}-t_{1}) } \right>  \\
 & = \left< \mathcal{E}^*(\vec{r}_{1}) \mathcal{E}(\vec{r}) \right> e^{ -i\omega \tau }
\end{align}
$$
Where the difference is $\tau=t_{2}-t_{1}$.

In the two-slit experiment, the intensity becomes,
$$
\left< I(P, t) \right> = I_{1} + I_{2} + c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\left\{  \Gamma\left( S_{1}, S_{2}, \frac{l}{c} \right)  \right\}
$$
Where, similarly, $l=l_{2}-l_{1}$.

Substituting in our results of a monochromatic field,
$$
\left< I(P) \right> = I_{1}+I_{2}+c\epsilon_{0} \lvert K_{1}K_{2} \rvert  \mathrm{Re}\{ \mathcal{E}^*(S_{1}) \mathcal{E}(S_{2}) e^{ -i\omega l /c } \}
$$
Now, if you suppose that $\mathcal{E}(S_{1})=\mathcal{E}_{0}$ and $\mathcal{E}(S_{2})=\mathcal{E}_{0}e^{ -i\phi }$, then the intensity becomes,
$$
\left< I(P) \right> = I_{1}+I_{2}+ 2\sqrt{ I_{1}I_{2} } \cos\left( \frac{2\pi l}{\lambda} + \phi \right)
$$
Physically, imagine the case when $\phi=0$. Then constructive interference occurs when $l$ is an integer number of wavelength, and destructive when $l$ is a half-integer. A mathematical formulation of what we had already concluded earlier.

Now, if $\phi \neq 0$ then constructive interference occurs at $P$ when:
$$
\frac{2\pi l}{\lambda} + \phi = 2\pi n \implies  l=\left( n + \frac{\phi}{2\pi} \right)\lambda
$$
For small angles:
$$
Y_{n}^{\text{max}} = \left( n+\frac{\phi}{2\pi} \right) \frac{\lambda L}{d} \qquad Y_{n}^{\text{min}} = \left( n+\frac{\phi}{2\pi}+\frac{1}{2} \right) \frac{\lambda L}{d}
$$
Which tell us that the phase difference $\phi$ shifts the positions of the maxima and minima, but the separation $\Delta Y$ is unchanged from $\phi=0$.