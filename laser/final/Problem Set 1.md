# Question 1
---
a.
$$
\dot{N}_{2} = -aN_{2}q - \Gamma N_{2} + p \implies  \dot{N}_{2} = - \Gamma N_{2}
$$
$$
N_{2}(t) = A e^{ -\Gamma t }
$$
Where $A$ is some constant. $\Gamma$ appears to model the decay rate for the number of excited atoms in the gain medium.

---
b.
$$
\dot{N}_{2} = - \Gamma N_{2} + p
$$
$$
N_{2}(t) = Ae^{ -\Gamma t } + \frac{p}{\Gamma}
$$
$p /\Gamma$ is the horizontal asymptote for $N_{2}(t)$.

The number of excited atoms in the gain medium reaches an equilibrium based on the ratio between the decay rate and the pumping rate.

---
c.
$$
\dot{q}=-bq
$$
$$
q(t) = Ae^{ -bt }
$$
$b$ is the decay rate for the number of photons in the laser cavity. 

---
d.
$$
-aN_{2}q - \Gamma N_{2} + p=0 \qquad aN_{2}q-bq=0
$$
$$
aN_{2}q=bq \implies  aN_{2}=b \implies  N_{2}=\frac{b}{a}
$$
$$
-a\left( \frac{b}{a} \right)q - \Gamma \left( \frac{b}{a} \right) + p = -bq-\frac{\Gamma b}{a} + p=0
$$
$$
-bq = \frac{\Gamma b}{a} -p \implies  q=\frac{p}{b} - \frac{\Gamma}{a}
$$
Therefore we have,
$$
\bar{N}_{2} = \frac{b}{a} \qquad \bar{q}=\frac{p}{b} - \frac{\Gamma}{a}
$$
---
e.
$$
\bar{q}>0 \implies  \frac{p}{b} - \frac{\Gamma}{a} > 0 \implies  \frac{p}{b} > \frac{\Gamma}{a}
$$
$$
p > \frac{\Gamma b}{a}
$$
So the pump rate must be greater than $\Gamma b /a$.

---
f.
Assuming we are still in the steady state,
$$
\bar{q} = \frac{p}{b} - \frac{\Gamma}{a}
$$
The term representing the photons leaving the laser through the output is $-bq$. So the output in photons/second should be:
$$
b\bar{q}= b \left( \frac{p}{b} - \frac{\Gamma}{a} \right) = p-\frac{\Gamma b}{a}
$$
Which mirrors the threshold condition from before. The output from the laser is the pumping rate minus the threshold pumping rate.

---
g.
Once again, assuming we are still in the steady state,
$$
\bar{N}_{2} = \frac{b}{a}
$$
The term representing spontaneous emission in the laser-model equations is:
$$
\Gamma N_{2} = \frac{\Gamma b}{a}
$$
The number if photons/second lost to spontaneous emission is equivalent to the threshold pump rate.