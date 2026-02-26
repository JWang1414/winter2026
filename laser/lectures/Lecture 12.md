- Lectures 10 and 11 will be online. This is supposed to be a continuation of the content covered there.

In the previous lectures, we used as ray image, without diffraction to model the propagation of light inside a cavity.

Today, we will remedy this by modelling our light as a wave. For our purposes, the governing equation manifests as the paraxial wave equation. (PWE).

Define some vector $\vec{k}=(k_{x}, k_{y}, k_{z})$ where $\{ k_{x}, k_{y} \}\ll k_{z}$. This is within the paraxial approximation. It can also be modelled by claiming $\theta\ll 1$.
# Wave equation
We begin our analysis starting with the wave equation.
$$
\nabla^{2}E(\vec{r}, t) - \frac{1}{c^{2}} \frac{ \partial^{2} }{ \partial t^{2} } E(\vec{r}, t) =0
$$
Inside the paraxial approximation we assume $E$ is scalar. Furthermore, our calculations will occur inside a vacuum, with a monochromatic or single optical frequency. This frequency will be defined to be $\omega=ck$.

Our wave of light will therefore look something like:
$$
E(\vec{r}, t) = \mathcal{E}(\vec{r}) e^{ -i\omega t }
$$
Which, substituting into the wave equation, derived the Helmholtz equation,
$$
\nabla^{2}\mathcal{E}(\vec{r}) + k^{2} \mathcal{E}(\vec{r})=0
$$
# Solutions to the Helmholtz equation
Among the solutions to the Helmholtz equations are spherical and plane waves,
$$
\text{Spherical wave} = \frac{A}{r} e^{ ikr } \qquad \text{Plane wave} = \mathcal{E}_{0} e^{ i\vec{k}\cdot \vec{r} }
$$
![[Pasted image 20260225193152.png]]
A drawing of a spherical wave and plane wave.

Neither of these look particularly like laser light, and so we will try to look for something like a plane wave:
$$
\mathcal{E} = \mathcal{E}_{0}(\vec{r}) e^{ ikz }
$$
Where we have defined the envelope function $\mathcal{E}_{0}$. This function should be responsible for limited the $x$ and $y$ components of the wave, so it appears more like a beam.

In the envelop function, we have a slow variation on the $\lambda$ scale, mathematically defined to be,
$$
\left| \frac{ \partial \mathcal{E}_{0} }{ \partial z }  \right| \ll k \lvert \mathcal{E}_{0} \rvert \qquad \left| \frac{ \partial^{2}\mathcal{E}_{0} }{ \partial z^{2} }  \right| \ll k \left| \frac{ \partial \mathcal{E}_{0} }{ \partial k }  \right|
$$

To determine our envelope function $\mathcal{E}_{0}$, we substitute this model into the Helmholtz equation, and we get something like,
$$
\nabla^{2}_{T}\mathcal{E}(x, y, z) + 2ik \frac{ \partial  }{ \partial z } \mathcal{E}_{0}(x, y, z) =0
$$
Where we have defined,
$$
\nabla_{T} = \frac{ \partial  }{ \partial x } + \frac{ \partial  }{ \partial y }
$$
In fact, this equation we get is indeed the paraxial wave equation.
- Gaussian beams are one solution of the paraxial wave equation

Now, lets investigate one common intensity profile for a laser beam:
$$
I = I_\text{pk} \exp \left[ -\frac{2(x^{2}+y^{2})}{w^{2}} \right]
$$
Where $w$ is the waist width (I think?)

Now, we would ideally like some envelope function that looks something like:
$$
\mathcal{E}_{0}(\vec{r}) = A e^{ ik(x^{2}+y^{2})/2q(z) } e^{ ip(z) }
$$
Where $A$ is a constant and $p$ and $q$ are both complex values.
- This particularly specific form of the envelope function arises just because this problem has been solved so many times. This form will make it easier to work with.

First, lets begin with some notes about the complex math,
$$
ip-ip^* = 2\mathrm{Im}\{ p \} \qquad \frac{i}{q} - \frac{i}{q^*} = -2\mathrm{Im}\left\{  \frac{1}{q}  \right\}
$$
And,
$$
\mathrm{Im}\left( \frac{1}{q} \right) = \frac{2}{kw^{2}} = \frac{\lambda}{\pi w^{2}}
$$
From here we would like to solve for the intensity,
$$
I = \left| \mathcal{E}_{0} \right| ^{2}
$$
- Which is where we will pick up next time.