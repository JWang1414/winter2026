# Spontaneous Emission
Last time, we discussed the energy resulting from a state transitioning to a lower energy state. For example, if something swapped from the 2nd ring down to the 1st ring, we might have,
$$
A_{21} = \frac{1}{4\pi\epsilon_{0}} \frac{2e^{2}\omega^{2}_{21}}{me^{3}} f_{21}
$$
Where $f_{21}$ has been defined in the previous lecture.
- This notates the decay rate from 2 to 1

Generally speaking, we can use this to define the total decay rate (probability decay rate):
$$
A_{n} = \sum_{m} A_{nm}
$$
If we for example have some lifetime $\tau_{n} = A_{2}^{-1}$ then the rate at which it decays is something like,
$$
\frac{dN_{2}}{dt} = - A_{2} N_{2}
$$
Which is an ODE we can solve. Particularly, in a two level system we also have the transition:
$$
\frac{dN_{1}}{dt} = - \frac{dN_{2}}{dt} = A_{2} N_{2}
$$
# Absorption
$$
\frac{d^{2}}{dt^{2}} \vec{x} + 2\beta \frac{d}{dt} \vec{x} + \omega_{0}^{2} \vec{x} = \frac{e}{m}\vec{E}
$$
This is an old equation, but we have introduced the new damping term (the second term) quantified by the $\beta$.

This system is being driven by the electric field, typically something like
$$
\vec{E} = E_{0} \vec{\epsilon} \cos(\omega t-\theta)
$$
For simplicity, we will choose $\theta=0$ (no phase change) and $\vec{\epsilon}$ linear. These conditions drastically simplify the equation. Also, we will assume everything is pointing along the same axis here, so we can go back to 1-D equations.

Okay, now lets try to have a response in the form:
$$
x = ae^{ -i\omega t }
$$
Work out $a$ and you should get,
$$
a = \frac{(e /m)E_{0}}{-\omega^{2}-2\varepsilon \beta \omega + \omega_{0}^{2}}
$$
In the real world this translates to
$$
\vec{x}(t) = \mathrm{Re}\{ \vec{a} e^{ -i\omega t } \} = \mathrm{Re}\{ a \} \cos \omega t + \mathrm{Im}\{ a \} \sin \omega t
$$
So what is the average radiated power from this system?
$$
\overline{\frac{dW}{dt}} = \overline{\vec{F}\cdot \vec{v}}
$$
If you work out this quantity, you will find that it is proportional only to $\mathrm{Im}\{ a \}$. And in fact we get something like,
$$
\frac{eE_{0}\omega}{2} \mathrm{Im}\{ a \} = \frac{e^{2}E_{0}^{2}}{m} \frac{\beta \omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2} + 4\beta^{2}\omega^{2}}
$$
# Near-resonant approximation
This is in the case for,
$$
\omega-\omega_{0} \ll \omega_{0}
$$
Where absorption is strongest because $\beta\ll \omega_{0}$
- This is based on experimental example. This is oftentimes true, it can be untrue in many contexts, like in biological physics.

Given this assumption we can say:
$$
(\omega_{0}^{2}-\omega^{2}) = (\omega_{0}-\omega)(\omega_{0}+\omega) \approx 2\omega_{0}(\omega_{0}-\omega)
$$
So our previous expansion simplifies into,
$$
\frac{dW}{dt} \approx \frac{e^{2}E_{0}^{2}}{4m} \frac{\beta}{(\omega-\omega_{0})^{2} + \beta^{2}}
$$
- Notice that this function roughly has the form of a Lorentzian $(1+x^{2})^{-1}$

On resonance this becomes,
$$
\frac{dW}{dt} \bigg|_{\omega=\omega_{0}} = \frac{e^{2}E_{0}^{2}}{4m\beta}
$$
You can also apply the quantum correction quite intuitively here,
$$
\frac{dW}{dt} \bigg|_{\omega=\omega_{0}} = \frac{e^{2}E_{0}^{2}}{4m\beta} f
$$
Take the two relations,
$$
I = \frac{1}{2}  c\epsilon_{0} E_{0}^{2} \qquad \omega_{0}\lambda_{0} = 2\pi c
$$
Substitute this into our equation to find,
$$
\frac{dW}{dt} \bigg|_{\omega=\omega_{0}} = \frac{e^{2}E_{0}^{2}}{4m\beta} = \frac{2\pi c^{2}}{\omega_{0}^{2}} I = \frac{1}{2\pi} \lambda_{0}^{2} I
$$
- Something interesting that arises here is the fact that photons will "reflect" or ripple off atoms as if they are the size of a wavelength. This is strangely despite the fact that atoms are usually far smaller than a single wavelength. This is because of the wave nature of light (we cannot imagine them as particles/bullets travelling through space)
