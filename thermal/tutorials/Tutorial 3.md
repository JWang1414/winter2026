# Diffusive equilibrium
---
1a.
The total number of positions in $N$, and we choose $n_{L}$ positions.
$$
\Omega(n_{L}) = \begin{pmatrix}
N \\
n_{L}
\end{pmatrix} = \frac{N!}{n_{L}!(N-n_{L})!}
$$
---
1b.
Note that there are $n_{L}$ particles on the left side. Furthermore, the probability that any one of these individual particles is found on the left-side is $p$.

From particle 1 to $n_{L}$, the probability they'll be on the left is $p$. From particles $n_{L}+1$ to $N$ the probability they're on the right is $q=1-p$.

The total probability is therefore,
$$
p_{i}(n_{L}) = p^{n_{L}} q^{n_{R}}
$$
---
1c.
We will determine the entropy with a "probabilistic expression":
$$
S = - k \sum_{j} p_{j} \ln p_{i}
$$
Where $j$ is summing over all the microstates.

Recall that we found for some microstate $i$ there are $n_{L}^{i}$ particles on the left and $N-n_{L}^{i}$ particles on the right
$$
p^{n_{L}^{i}}q^{N-n_{L}^{i}}
$$
Group the microstates by their macrostates $n_{L}$ and write:
$$
\frac{S(N;p)}{k} =- \sum _\text{microstates} p_{i} \ln p_{i} = - \sum_{n=0}^{N} \sum _{\text{microstates with }n=n_{L}} p_{i} \ln p_{i}
$$
Since these are the $p_{i}$ calculated earlier, the inside sum reduces to:
$$
\sum_{\text{microstates } n=n_{L}} p_{i} \ln p_{i} = p_{i} \ln p_{i} + p_{i} \ln p_{i} + \dots + = \begin{pmatrix}
N \\
n
\end{pmatrix} p_{i} \ln p_{i}
$$
This sum is therefore,
$$
\frac{S(N;p)}{k} = - \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} p_{i} \ln p_{i} = - \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} p^{n} q^{N-n} \ln[p^{n}q^{N-n}]
$$
Simplify the logarithm,
$$
- \ln p \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} n p^{n} p^{N-n} - \ln q \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} (N-n) p^{n} p^{N-n}
$$
Simplify this second term using $m=N-n$
$$
\ln q \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} (N-n) p^{n} p^{N-n} = \ln q \sum_{m=0}^{N} \begin{pmatrix}
N \\
N-m
\end{pmatrix} m p^{N-m} q^{m}
$$
According to an identity this is equal to,
$$
\ln q \sum_{n=0}^{N} \begin{pmatrix}
N \\
n
\end{pmatrix} np^{N-n} q^{n}
$$
Where we have replaced $m$ with $n$.

Substituting this back in, and applying a binomial identity this becomes,
$$
\frac{S}{k} = -\ln p Np (p+q)^{N} - \ln q Nq (p+q)^{N}
$$
Recall that $q=1-p$ and so $p+q=1$
$$
S = -kN (p\ln p + q\ln q)
$$
---
1d.
Intuitively, the entropy is maximized when,
$$
p=q=\frac{1}{2}
$$
Which is true