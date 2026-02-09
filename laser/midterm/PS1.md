# Question 1
---
a.
$$
\dot{N}_{2} = -aN_{2}q - \Gamma N_{2}+p = - \Gamma N_{2}
$$
Solve with separation of variables,
$$
\frac{dN_{2}}{dt} = -\Gamma N_{2} \implies  N_{2}(t) =c_{1} e^{ -\Gamma t }
$$
Where $c_{1}$ is some constant.

$N_{2}$ decays slower for smaller $\Gamma$ and vice versa. This tells me that $\Gamma ^{-1}$ governs the decay speed for the number of atoms in the cavity. Larger $\Gamma ^{-1}$ corresponds with slower decay, and smaller $\Gamma ^{-1}$ corresponds with faster decay.

---
b.
$$
\dot{N}_{2} = -aN_{2}q - \Gamma N_{2}+p = -\Gamma N_{2} + p
$$
Solution is,
$$
N_{2}(t) = c_{1} e^{ -\Gamma t } + \frac{p}{\Gamma}
$$
Exponential with a constant additive term $p /\Gamma$. Changes the asymptotic behaviour of $N_{2}$. $N_{2}$ will eventually decay so that the number of atoms inside the cavity is $p /\Gamma$.

---
c.
$$
\dot{q} = a N_{2}q - bq = -bq
$$
Solve,
$$
\frac{dq}{dt} = -bq \implies  q(t) = c_{1}e^{ -bt }
$$
Mathematically the equivalent for $\Gamma$. $b^{-1}$ is the decay speed for the number of photons. Larger $b^{-1}$, slower decay.

---
d.
Steady state solutions imply,
$$
\frac{dN_{2}}{dt} =0 \qquad \frac{dq}{dt}=0
$$
$$
aN_{2}q-bq =0 \implies  aN_{2}q =bq
$$
$$
\bar{N}_{2} = \frac{b}{a}
$$
$$
-aN_{2}q - \Gamma N_{2}+p =0 \implies  -a \left( \frac{b}{a} \right)q - \Gamma\left( \frac{b}{a} \right) + p=0
$$
$$
-bq - \frac{\Gamma b}{a} + p=0 \implies  -q - \frac{\Gamma}{a} + \frac{p}{b} =0
$$
$$
\bar{q} = \frac{p}{b} - \frac{\Gamma}{a}
$$
In summary,
$$
\bar{N}_{2} = \frac{b}{a} \qquad \bar{q} = \frac{p}{b} - \frac{\Gamma}{a}
$$
---
e.
$$
\bar{q} >0 \implies  \frac{p}{b} - \frac{\Gamma}{a} > 0
$$
$$
\frac{p}{b} > \frac{\Gamma}{a} \implies  p > \frac{b\Gamma}{a}
$$
---
f.
Output is modelled by $bq$.
$$
\frac{p}{b} > \frac{\Gamma}{a} \implies  \frac{ap}{\Gamma} > b
$$
So the output is limited by,
$$
\frac{ap}{\Gamma}q > bq
$$
- Honestly no clue what this means
---
g.
Spontaneous emission modelled by $\Gamma N_{2}$.
$$
\frac{p}{b} > \frac{\Gamma}{a} \implies  \frac{ap}{b} > \Gamma
$$
So the spontaneous emission is bounded by,
$$
\frac{ap}{b}N_{2} > \Gamma N_{2}
$$
# Question 2
---
a.
Planck spectrum:
$$
\rho(\nu) = \frac{8\pi \nu}{c^{3}} \frac{h\nu}{e^{ h\nu/k_{B}T } -1}
$$
The goal of this question is to plot this data for the different temperatures $T$. Everything else is a constant, except for $\nu$, this is the dependent variable.

---
b.
$\Delta \nu$ is the FWHM. After you get $\Delta \nu$ from the plots, solving for $1 /\Delta \nu$ is trivial.