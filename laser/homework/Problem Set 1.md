# Question 1
---
a.
Set $a=0$ and $p=0$ to find
$$
\dot{N}_{2} = -aN_{2}q - \Gamma N_{2} + p = -(0)N_{2}q - \Gamma N_{2} + (0) = -\Gamma N_{2}
$$
$$
\dot{q} = aN_{2}q - bq = (0)N_{2}q - bq = -bq
$$
Rewrite
$$
\dot{N}_{2} = -\Gamma N_{2} \qquad \dot{q}=-bq
$$
Solve the ODE for $N_{2}$
$$
N_{2}(t) = c_{1} e^{ -\Gamma t }
$$
For some constant $c_{1}$.
- $\Gamma$ is intended to model the spontaneous emission from the laser

For greater $\Gamma$, the number of atoms in the excited state within the laser decays quicker, and vice versa
- I am assuming $\Gamma\geq 0$. Otherwise there is energy spontaneously going into the laser
![[Pasted image 20260108211716.png]]
A typical $N_{2}(t)$, it is simply the exponential $e^{ -x }$. The variable $\Gamma$ controls the steepness of the curve.

---
b.
Set $a=0$ but $p\neq 0$.
$$
\dot{N}_{2} = -\Gamma N_{2}+p \qquad \dot{q} = -bq
$$
Solve for $N_{2}$
$$
N_{2}(t) = c_{1} e^{ -\Gamma t } + \frac{p}{\Gamma}
$$
$p / \Gamma$ moves the full function up and down. It not only increases the initial $N_{2}$, but prevents it from decaying to zero.

Since $p$ representing the pumping in the laser, this implies that if a laser is properly pumped, although spontaneous emission will still occur, the number of excited particles inside the laser will eventually decay to roughly $p /\Gamma$.

---
c.
Set $a=0$
$$
\dot{q} = -bq
$$
Solve for $q$,
$$
q(t) = c_{1} e^{ -bt }
$$
Mathematically, $b$ is equivalent to $\Gamma$. $b$ is the decay rate of the photons, and $\Gamma$ is the decay rate of the number of excited atoms.

- Note: Both a and c call for the meaning of $\Gamma ^{-1}$ and $b^{-1}$ as opposed to $\Gamma$ and $b$, but I'm pretty sure it's the same thing but inverted

---
d.
First equation
$$
0=-aN_{2}q - \Gamma N_{2}+p \implies aN_{2}q + \Gamma N_{2} = N_{2} (aq+\Gamma) =p
$$
$$
N_{2} = \frac{aq+\Gamma}{p}
$$
Second equation:
$$
0=aN_{2}q - bq = a \left( \frac{aq+\Gamma}{p} \right)q - bq = \frac{a^{2}}{p} q^{2} + \left( \frac{a\Gamma}{p}-b \right)q
$$
Factor out $q$,
$$
\left[ \frac{a^{2}}{p} q + \left( \frac{a\Gamma}{p}-b \right) \right] q =0
$$
Which implies that $q=0$ or,
$$
q = \frac{p}{a^{2}} \left( b-\frac{a\Gamma}{p} \right) = \frac{bp-a\Gamma}{a^{2}}
$$
Substitute into $N_{2}$,
$$
N_{2} = \frac{aq+\Gamma}{p} = \frac{1}{p} \left[ a\left( \frac{bp-a\Gamma}{a^{2}} \right) + \Gamma \right] = \frac{b}{a}
$$
In summary:
$$
\bar{q} = \frac{bp-a\Gamma}{a^{2}} \qquad \bar{N}_{2} = \frac{b}{a}
$$
---
e.
$$
\bar{q}= \frac{bp-a\Gamma}{a^{2}} >0 \implies bp-a\Gamma>0
$$
$$
bp>a\Gamma
$$
In terms of just the pumping rate this is,
$$
p > \frac{a\Gamma}{b}
$$
---
f.
The rate of change in the photons is,
$$
\dot{q} = aN_{2}q - bq = aN_{2}q - ab\bar{N}_{2}q = aq(N_{2} - \bar{N}_{2})
$$
- I believe this is the output of the laser, but I'm not sure how to interpret it

Another possible answer is to use the stimulated emission term in the $N_{2}$ equation $aN_{2}q$ but I'm not sure how to use it

---
g.
The spontaneous emission term is $\Gamma N_{2}$
- Don't really know how to continue from here
# Question 2
