1. What is the momentum transfer from some particle that hits a piston inside a closed chamber. Assume a perfectly elastic collision.

After the collision, the $z$ component of the velocity swaps from positive to negative, with the same magnitude. So we have,
$$
mv_{z} \to -mv_{z}
$$
And the net change in momentum for the piston is,
$$
\Delta p_{z} = 2mv_{z}
$$
For a single particle

2. What is the average time between collisions between the piston and particle?

Well that particle is moving at some constant velocity $v_{z}$. Assuming it has to travel a distance $z$ from one side of the chamber to the other, the total distance from the piston back to the piston is $2z$. Therefore we have,
$$
v = \frac{d}{t} \implies v_{z} = \frac{2z}{\Delta t} \implies \Delta t = \frac{2z}{v_{z}}
$$
Lets approximate the force,
$$
\vec{F} = \frac{dp}{dt} \approx \frac{\Delta p}{\Delta t} = \frac{2mv_{z}}{2z /v_{z}} = \frac{mv_{z}^{2}}{z}
$$

3. Assume isotropic velocity distribution. What is the force on the piston $\left< F \right>$ in terms of the average kinetic energy $\left< K \right>$

- We call $\left< \cdot \right>$ the ensemble average. Roughly speaking, it is the average of a quantity taken over many hypothetical copies of the same system
	- Roughly the same as expectation values. So my intuition of the system is pretty much correct

The total force is,
$$
F = \sum_{i=1}^{N} \frac{mv_{z}^{2}}{z} = \frac{Nmv^{2}_{z}}{z}
$$
The ensemble average is,
$$
\left< F \right> = \frac{Nm}{z} \left< v^{2}_{z} \right>
$$
Note that the ensemble average of the kinetic energy is something like:
$$
\left< K \right> = \frac{1}{2}m \left[ \left< v^{2}_{x} \right> + \left< v^{2}_{y} \right> + \left< v^{2}_{z} \right>  \right]
$$
We assume the velocity distribution is isotropic so,
$$
\left< v^{2}_{x} \right> = \left< v^{2}_{y} \right> = \left< v^{2}_{z} \right>
$$
Therefor we approximate,
$$
\left< K \right> = \frac{3}{2}m \left< v^{2}_{z} \right>
$$
Substituting this back into the force we have,
$$
\left< F \right> = \frac{N}{z} \frac{2}{3} \left< K \right>
$$
4. What is the equilibrium point of the piston?

Denote the mass of the piston as $M$. Then,
$$
\left< F \right> = Mg \implies \frac{2}{3} \frac{N}{z} \left< K \right> = Mg
$$
Solve for $z$,
$$
z = \frac{2}{3} \frac{N}{Mg} \left< K \right>
$$

(Bonus) What is the frequency of oscillation around the equilibrium?

Use Newton's 2nd law,
$$
\Sigma F = ma \implies \left< F \right>  - F_{g} = M\ddot{z}
$$
Model the position of the piston as,
$$
z_{eq} + \delta z
$$
Where $z_{eq}$ is the equilibrium and $\delta$ is some small constant. Therefore,
$$
\ddot{z} = \delta \ddot{z}
$$
Substituting these back in,
$$
M \delta \ddot{z} = \frac{2}{3} \frac{N}{z_{eq}+\delta z} \left< K \right> - Mg
$$
Apply the approximation,
$$
\frac{1}{z_{eq}+\delta z} \approx \frac{1}{z_{eq}} - \frac{\delta z}{z^{2}_{eq}}
$$
RHS simplifies into,
$$
\frac{2}{3} \frac{N}{z_{eq}} \left< K \right> - Mg - \frac{2}{3} \frac{N\delta z}{z_{eq}^{2}} \left< K \right>
$$
Notice that, from our previous calculation first and second terms are equal. Cancel the two out to obtain,
$$
M\delta \ddot{z} = - \frac{2}{3} \frac{N\delta z}{z^{2}_{eq}} = - \frac{Mg}{z_{eq}} \delta z
$$
Equate this to the general model of a harmonic oscillator:
$$
\delta \ddot{z} = -\omega^{2} \delta z \implies \omega = \sqrt{ \frac{g}{z_{eq}} }
$$

5. For a fixed density $n$ how does the force scale with the area $A$ of the piston?

Compute the density by the definition:
$$
n = \frac{N}{V} = \frac{N}{Az} \implies N = nAz
$$
Substitute this quantity into $\left< F \right>$ to find:
$$
\left< F \right>  = \frac{2n}{3} A \left< K \right>
$$
Therefore the force scales linearly as the area increases.

6. Assuming the piston has sides 10cm, $v_\text{rms}=300$ m/s, how many collisions per second occur for $N=10^{22}$?

$$
\text{Rate for one particle} \approx \frac{\text{Speed towards piston}}{\text{Distance to piston}} = \frac{\lvert v_{z} \rvert }{2z_{eq}}
$$
For $N$ particles,
$$
\left< \text{Rate} \right> = \frac{N\left< \lvert v_{z} \rvert  \right> }{2z_{eq}}
$$
We have been given,
$$
v_\text{rms} = \sqrt{ \left< v^{2} \right>  }
$$
Assuming isotropic system,
$$
\left< v^{2} \right> = 3 \left< v_{z}^{2} \right> \implies \left< v^{2}_{z} \right> = \frac{1}{3} \left< v^{2} \right>
$$
Apple the common approximation that,
$$
\sqrt{ \left< v^{2} \right>  } \approx \left< \lvert v \rvert  \right>
$$
To obtain the quantity,
$$
\left< \lvert v_{z} \rvert  \right> \approx \frac{1}{\sqrt{ 3 }} \sqrt{ \left< v^{2} \right>  } = \frac{v_\text{rms}}{\sqrt{ 3 }}
$$
Substitute back into the rate to find,
$$
\left< \text{Rate} \right> = \frac{Nv_\text{rms}}{2\sqrt{ 3 }z_{eq}}
$$
If you numerically evaluate this expression, it should be within the order of $10^{24}$. In the following question, we are tasked to find how often the particles collide with each other, and you obtain something within the order of $10^{7}$. So, the assumption we made that the particles do not interact with each other is actually quite a good one.