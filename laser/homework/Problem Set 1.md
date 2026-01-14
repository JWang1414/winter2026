# Question 1
---
a.
Set $a=0$ and $p=0$ to find
$$
\dot{N}_{2} = -aN_{2}q - \Gamma N_{2} + p = -(0)N_{2}q - \Gamma N_{2} + (0) = -\Gamma N_{2}
$$
Solve the ODE for $N_{2}$
$$
\dot{N}_{2} = -\Gamma N_{2} \implies N_{2}(t) = c_{1} e^{ -\Gamma t }
$$
For some constant $c_{1}$. For greater $\Gamma$, the number of atoms in the excited state within the laser decays quicker, and vice versa. Since $\Gamma$ models the spontaneous emission, this tell be that when more spontaneous emission occurs, the number of excited atoms in the gain medium will decrease quicker.

This means that for smaller $1/\Gamma$ $N_{2}(t)$ will decay quicker, and for larger $1 /\Gamma$ $N_{2}(t)$ will decay slower.
![[Pasted image 20260108211716.png]]
A example of a typical $N_{2}(t)$. Shown here is the exponential $e^{ -t/2 }$. The variable $\Gamma$ controls the steepness of the curve ($\Gamma=1 /2$ in this case).

---
b.
Set $a=0$ but $p\neq 0$.
$$
\dot{N}_{2} = -\Gamma N_{2}+p
$$
This is a differential equation with the solution:
$$
N_{2}(t) = c_{1} e^{ -\Gamma t } + \frac{p}{\Gamma}
$$
Mathematically, the additive factor of $p /\Gamma$ shifts the exponential function up and down. Increasing $p /\Gamma$ increases the initial $N_{2}$, and stops it from decaying to 0.

This implies that if a laser is properly pumped, although spontaneous emission will still occur, the number of excited atoms inside the gain medium will eventually decay to roughly $p /\Gamma$.

An example of a typical $N_{2}(t)$ when $p\neq 0$. Shown here is the exponential $e^{ -t /2 } + 2$. $\Gamma$ controls the steepness of the curve, and $p$ applies a vertical shift. In this case $\Gamma+1 /2$ and $p=1$. Notice that, with non-zero pumping, $N_{2}(t)$ no longer decays to zero.

---
c.
Set $a=0$
$$
\dot{q} = -bq
$$
The solution to this differential equation is:
$$
q(t) = c_{1} e^{ -bt }
$$
Mathematically, $b$ is equivalent to $\Gamma$. Physically, $b$ is the decay rate of the number of photons, and $\Gamma$ is the rate of spontaneous emission. Equivalently, for smaller $1 /b$ $q(t)$ will decay quicker, and for larger $1 /b$ $q(t)$ will decay slower.

---
d.
Setting $\dot{q}=0$ results in the separated equation:
$$
\dot{q}=0 \implies aN_{2}q-bq = (aN_{2}-b)q=0
$$
Which implies that $q=0$ or,
$$
N_{2} = \frac{b}{a}
$$
Substituting this newfound quantity into $\dot{N}_{2}=0$ I find that:
$$
\dot{N}_{2} =0 \implies -a\left( \frac{b}{a} \right)q - \Gamma\left( \frac{b}{a} \right) + p = -bq - \frac{\Gamma b}{a} + p=0
$$
Which can be simplified and isolated for $q$:
$$
bq = p-\frac{\Gamma b}{a} \implies q = \frac{p}{b} - \frac{\Gamma}{a}
$$
In summary,
$$
\bar{N}_{2} = \frac{b}{a} \qquad \bar{q} = \frac{p}{b} - \frac{\Gamma}{a}
$$
---
e.
Setting $\bar{q}>0$ implies,
$$
\frac{p}{b} - \frac{\Gamma}{a} > 0 \implies \frac{p}{b} > \frac{\Gamma}{a}
$$
In terms of just the pump rate,
$$
p > \frac{b}{a} \Gamma
$$
---
f.
Applying the previously found expression $b=a\bar{N}_{2}$ to the expression for $\dot{q}$ yields:
$$
\dot{q} = aN_{2}q - bq = aN_{2}q - ab\bar{N}_{2}q = aq(N_{2} - \bar{N}_{2})
$$
So the output of the laser is proportional to the excess number of excited electrons $N_{2}-\bar{N}_{2}$.

---
g.
Recall that above the threshold,
$$
\frac{p}{b} > \frac{\Gamma}{a} \implies \frac{1}{b} > \frac{\Gamma}{pa}
$$
In the form $1 /b$, the decay rate in the number of photons appears to depend linearly on the spontaneous emission of excited atoms, and inversely on the pumping rate.
# Question 2
---
a.
$$
\rho(\nu) = \frac{8\pi \nu^{2}}{c^{3}} \frac{h\nu}{e^{ h\nu/k_{B}T } -1}
$$
- Spectral density of the blackbody spectra have been plotted using Python
- I used 298.15 K for room temperature, and 5800 K for the temperature of the Sun
- Linear scale, and assumed the bandwidth "cutoff" would be roughly 1/3 of the max height
- Wavelength has been pasted at the bottom of the code
---
b.
- The coherence time for room temperature is also pasted at the bottom of the code