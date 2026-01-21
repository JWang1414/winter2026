Few things that were omitted from last time.

Beer-Lambert Law:
$$
a(\nu) \approx \frac{\lambda^{2} A_{21} g_{2}}{8\pi g_{1}} \tilde{N}_{1} S(\nu)
$$
Where $a$ is the absorption coefficient and $\tilde{N}_{1}$ is the number of atoms per volume
# Threshold of a Laser
- **Insert image here**
	- Should be a diagram of a laser highlighting the reflectivity and the output of the laser
	- Each of the mirrors within a laser may suffer from some scattering, because they cannot be perfectly smooth
For this laser, let us define the reflection and transmission coefficients $r$ and $t$. Then, assume that it is ideal such that $r+t=1$.

The condition for gain to exceed the loss at the mirrors is,
$$
r_{1}r_{2} e^{ 2g_{t}l }=1
$$
Where here we have the threshold gain $g_{t}$.

We can solve this equation for $g_{t}$
$$
g_{t} = - \frac{1}{2l} \ln(r_{1}r_{2})
$$
Apply the Taylor series expansion of $\ln (1+x)$ to find,
$$
g_{t} \approx \frac{1}{2l} (1-r_{1}r_{2})
$$
For example, lets suppose that the back mirror is perfect, and so the reflectivity according to the output is $r_{2}=1-t_\text{out}$ which gives us,
$$
g_{t} \approx \frac{1}{2l} t_\text{out}
$$
# What is the required population inversion?
From the last lecture, the gain coefficient as a function of $\nu$ is defined to be,
$$
g(\nu) = \sigma(\nu) \left[ \tilde{N}_{2} - \frac{g_{2}}{g_{1}} \tilde{N}_{1} \right] \equiv \sigma(\nu) \Delta \tilde{N}
$$
Where $\sigma(\nu)$ is the cross section and $\Delta \tilde{N}$ is the population inversion per volume.

Solve for $\Delta \tilde{N}$, and using $g_{t}=g(\nu)$ to obtain,
$$
\Delta \tilde{N} = \frac{g_{t}}{\sigma(\nu)} = \frac{8\pi g_{t}}{\lambda^{2}A S(\nu)}
$$
Which is called the threshold population inversion.
- Recall that $S(\nu)$ is the lineshape function
# Model for a laser
Recall our original model for a laser
- **Insert image here**
	- Diagram of the variables we defined in our laser. How we gain photons, lose atoms etc

From continuity, we also know that,
$$
\frac{ \partial I^{(+)} }{ \partial z } +\frac{1}{c} \frac{ \partial I^{(+)} }{ \partial t } = g I^{(+)}
$$
$$
-\frac{ \partial I^{(-)} }{ \partial z } +\frac{1}{c} \frac{ \partial I^{(-)} }{ \partial t } = g I^{(-)
}
$$
Inside of a gain medium. This equation is identical for the positive and negative going intensities. $I^{(+)}$ and $I^{(-)}$. The difference is that,
$$
\frac{ \partial I^{(+)} }{ \partial z } \qquad -\frac{ \partial I^{(-)} }{ \partial z }
$$
So this single term is negative in the other version.

Integrating the first term over $dz$, we discover that, if you add up the intensities of the positive and negative intensities, the total intensity is approximately constant, called the uniform field approximation. It is valid when the gain is small.

With this knowledge, we can drastically simplify our problem and find,
$$
\frac{dI}{dt} = \frac{cl}{L} g I
$$
- This equation we written down, but I don't know where it came from and what it means
$$
I = \frac{h\nu q}{v}c
$$
Going back to our initial model of a laser, we can use these equations to illuminate what the arbitrary variables we previously defined might be.
$$
\frac{dq}{dt} = (\text{pop} - \text{threshold})q = \frac{cl}{L} (g-g_{t}) q
$$
From which we can tell $aN$ is the $g$ portion and $b$ is the $g_{t}$ portion.
