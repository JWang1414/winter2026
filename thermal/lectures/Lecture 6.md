- This lecture is available only as a recording

In the last lecture, we defined temperature. However, interestingly this definition requires interacting systems. So, how might we define temperature in an isolated system then?

We can accomplish something similar by assuming system $A$ is far smaller than $B$. This is called a *reservoir*, or *bath*.
- Changes in the system are insignificant in $B$, but they are very significant in $A$
- This is roughly identical to the case we considered where $A$ consisted of just a single particle!
# Ensembles
If the system is decoupled or isolated from $B$, the fixed variables in $A$ are as usual, $(E, V, N)$. This is called the *micro-canonical ensemble*

If the system can exchange heat with the bath, then the energy can fluctuate, but it's temperature must match the bath, the fixed variables are $(T, V, N)$. This is called the *canonical ensemble*.

If the system can exchange heat and particles with the bath, $E$, and $N$ fluctuate but $(T, V, \mu)$ are fixed. This is the *grand-canonical ensemble*
- $\mu$ is the chemical potential

- For all the above, assume the bath is at equilibrium
# Thermodynamic potentials
Recall that,
$$
dS = \frac{1}{T} dE + \frac{P}{T} dV - \frac{\mu}{T} dN
$$
That is, entropy is a function of extensive variables $(E, V, N)$, and is the quantity we use to describe isolated systems

Define the Helmholtz free energy
$$
F = E-TS
$$
Where $E$ is energy, $T$ is temperature, and $S$ is entropy.
1. Independent of energy
2. Negative entropy at fixed temperature. It is minimum at equilibrium
3. Thermodynamic identity $dF=-S \, dT - P \, dV + \mu \, dN$

- This is called a Legendre transformation. Where we have swapped the dependence on $E$ with a dependence on $T$. The conjugate variable
![[Pasted image 20260125214942.png]]
A screenshot of all the thermodynamic potentials, and their characteristics.
# Probabilistic definition of entropy
Consider a large number $N$ identical copies of a system. Each copy and occupy one of $M$ possible microstates. The macrostate is characterized by $\{ n_{i} \}$ where $i=[1, M]$. Each $n$ is the number of copies of some microstate within each of the systems. Note that because every microstate can only appear once, we have,
$$
\sum_{i} n_{i} = N
$$
The number of microscopic realizations consistent with these occupation numbers is given by the multinomial coefficient:
$$
\Omega (N, \{ n_{i} \}_{n=1, \dots, M}) = \frac{N!}{n_{1}!\dots n_{M}!}
$$
Substitute this into the Boltzmann entropy to find,
$$
\frac{S}{k} = \ln N! - \sum_{i} \ln n_{i}!
$$
Introduce the quantity $p_{i}=n_{i} /N$ and consider the thermodynamic limit when $N\to \infty$ to find the entropy per copy:
$$
s \equiv  \frac{S}{Nk} = - \sum_{i} p_{i} \ln p_{i}
$$
- This quantity arises from the Stirling formula approximation
# Lagrange multiplier
We want to find the extrema of a multivariable function $f$, subject to the constraint $g(\vec{x})=c$.

Introduce the auxiliary function (called the Lagrangian):
$$
L(\vec{x}, \lambda) = f(\vec{x}) - \lambda [g(\vec{x})-c]
$$
And we can obtain the constraints through
$$
\nabla L=0 \qquad \frac{ \partial L }{ \partial \lambda } =0
$$
---
Example:
$$
\begin{align}
f(p, q) & = -p\ln p - q\ln q \\
p+q & =1
\end{align}
$$
Define the Lagrangian
$$
L = -p\ln p - q\ln q - \lambda \left[ p+q-1 \right]
$$
$$
\nabla L = \begin{bmatrix}
-\ln p -\frac{p}{p} - \lambda \\
-\ln q - \frac{q}{q} - \lambda
\end{bmatrix} = \begin{bmatrix}
1-\ln p - \lambda \\
1 - \ln q - \lambda
\end{bmatrix} =0
$$
Results in the system of equations:
$$
\begin{align}
\ln p & = -1-\lambda \\
\ln q & = -1-\lambda \\
p+q & =1
\end{align}
$$
Solve the system:
$$
\ln p - \ln q =0
$$
$$
q=1-p
$$
$$
\ln p = \ln(1-p) \implies  p = 1-p \implies  p=\frac{1}{2}
$$
Which is the correct answer.

---

Now, lets used this method to find the probability of microstates in the micro-canonical ensemble.

By the maximum entropy principle, we are interested in maximizing
$$
S = -k \sum_{i} p_{i} \ln p_{i}
$$
Under the constraint
$$
\sum_{i} p_{i}=1
$$
If you solve this problem, you find that all microstates are equally probable with,
$$
p_{i} = \Omega ^{-1}
$$
Which recovers the Boltzmann definition of entropy
$$
S = -k \sum_{i} p_{i} \ln p_{i} = k \ln \Omega
$$
In the canonical ensemble another constraint arises:
$$
\sum_{i} E_{i} p_{i} = \left< E \right>
$$
This is because the energy fluctuates, but is sharply peaked around the average due to the law of large numbers.

The Lagrangian requires has two constraints now, and this is expressed like:
$$
L = S + \alpha \left( 1-\sum_{i}p_{i} \right) + \beta \left( \left< E \right> - \sum_{i} E_{i}p_{i} \right)
$$
Which has,
$$
\nabla L =0 \implies  \ln p_{i} = -1-\alpha - \beta E_{i}
$$
This tells us that microstates in the canonical ensemble are Poisson distributed in energy:
$$
p_{i}(E_{i}) = \frac{1}{Z} e^{ -\beta E_{i} } \qquad Z = \sum_{i} e^{ -\beta E_{i} }
$$
The multiplier $\beta$ is called the inverse temperature:
$$
S = \frac{\beta k}{Z} \sum_{i} E_{i} p_{i} = \beta k\left< E \right> \qquad \beta=\frac{1}{k} \frac{ \partial S }{ \partial \left< E \right>  } = \frac{1}{kT}
$$
In the grand-canonical we have yet another constraint arising from the fluctuating number of particles:
$$
\sum_{i} N_{i}p_{i} = \left< N \right> \approx N
$$
From which we have,
$$
p_{i}(E_{i}, N_{i}) = \frac{1}{\Theta} e^{ -\beta(E_{i}-\mu N_{i}) }
$$
Where $\Theta$ is the grand partition function.
# Formal definition of thermodynamic potentials
Generically speaking, applying the maximum entropy principle under constraints leads to probability distributions proportional to the Boltzmann distribution
$$
p_{i} \propto \exp \left[ -\beta \left( E_{i} + \sum_{j} \mu_{j}I_{j} \right) \right] \qquad \beta=\frac{1}{kT}
$$
Where the variables allowed to fluctuate are notated by $O_{j}$ with the pre-factor $\mu_{j}$, the associated intensive conjugate variable.

The normalization of these probability distributions are called the partition functions. For example in the canonical ensemble we have,
$$
Z = \sum_{i}p_{i}
$$
With the thermodynamic potential,
$$
F = - kT \ln Z
$$
The thermodynamic potentials are related to each other through:
$$
F+TS = \left< E + \sum_{j}\mu_{j}O_{j} \right>
$$
These quantities are called the *thermodynamic identities*.

Similarly, from the fundamental identity:
$$
dS = \frac{1}{T} dE + \frac{P}{T} dV - \frac{\mu}{T} dN \iff dE = T\, dS - P \, dV + \mu \, dN
$$
We derive the *fundamental identities* for the thermodynamic potentials.
- Note that these quantities are included in the 2nd and final columns of the table in [this section](#Thermodynamic potentials)
