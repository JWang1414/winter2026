# Phase diagrams
---
1.
$$
x(t) = 0.05\cos(2\pi t) e^{ -\pi t/2 }
$$
$$
v(t) = 0.05 \left[ -\frac{\pi}{2} e^{ -\pi t/2 } (4\sin(2\pi t) + \cos(2\pi t)) \right]
$$
- You should be able to plot this in Python pretty easily
---
2.
$$
\dot{z} = v_{0}-gt \implies  \dot{z}-v_{0} = -gt
$$
$$
gt = v_{0}-\dot{z} \implies  t = \frac{v_{0}-\dot{z}}{g}
$$
$$
z = z_{0} + v_{0}\left( \frac{v_{0}-\dot{z}}{g} \right)  - \frac{1}{2}g \left( \frac{v_{0}-\dot{z}}{g} \right) ^{2} = \frac{1}{2g} (v_{0}-z)(v_{0}+z) + z_{0}
$$
- Afterwards the question is just plotting
- The idea here is to see the derivative $\dot{z}$ as a function of the position $z$
# Simple harmonic oscillator classics
---
1a.
$$
F = -k_{1}\Delta x - k_{2}\Delta x = -(k_{1}+k_{2})\Delta x
$$
---
1b.
Define the total shift to be $x$ and the shift of the first spring to be $x'$. The force at the midpoint between both springs is,
$$
-k_{1}x_{1} + k_{2}(x-x') =0 \implies  x' = \frac{k_{2}x}{k_{1}+k_{2}}
$$
The force on the mass is,
$$
-k_{2}(x-x')
$$
Substitute in our solution for $x'$ to find,
$$
F = -k_{2}\left( x - \frac{k_{2}x}{k_{1}+k_{2}} \right) = -\left( \frac{k_{1}k_{2}}{k_{1}+k_{2}} \right)x
$$
Which you can simplify into,
$$
k_\text{eff} = \frac{1}{k_{1}} + \frac{1}{k_{2}}
$$
Similar to how resistance changes in parallel

---
2a.
$$
F = -\nabla U
$$
The force in this system is therefore,
$$
F = -\frac{dU}{dx} = \frac{6a}{x^{7}} - \frac{12b}{x^{13}}
$$
At equilibrium,
$$
\frac{6a}{x^{7}} = \frac{12b}{x^{13}} \implies  x = \left( \frac{2b}{a} \right)^{1/6}
$$
Which is the equilibrium separation

---
2b.
Compute the Taylor series,
$$
F(x) = F(x_{0}) + \frac{dF}{dx}\bigg|_{x=x_{0}} (x-x_{0}) + \mathcal{O}(h^{2})
$$
Compute this derivative to find,
$$
\frac{dF}{dx}\bigg|_{x=x_{0}} = -36a \left( \frac{a}{2b} \right)^{4/3}
$$
Which is our spring constant
