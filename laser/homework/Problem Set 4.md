# Question 1
---
a.
$q$-factor,
$$
\mathrm{Re}\left\{  \frac{1}{q}  \right\} = z + \frac{z_{0}^{2}}{z} \qquad \mathrm{Im}\left\{  \frac{1}{q}  \right\} = \frac{\lambda}{\pi w^{2}}
$$
$$
q=z+q_{0} = z-iz_{0}
$$
First is the radius of curvature. And $w(z)$ in the second is the spot size
$$
w(z) = w_{0}\sqrt{ 1+\frac{z^{2}}{z_{0}^{2}} }
$$
ABCD matrix approach.

Goes through lens, and then propagates some distance $l$ away

$$
\begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & l \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
1 & l \\
-1 /f & 1-l /f
\end{bmatrix}
$$
$$
q_{f} = \frac{Aq_{i} + B}{Cq_{i} + D} = \frac{q_{i}+l}{(-1 /f)q_{i} + (1-l /f)}
$$
$$
q_\text{out} = \frac{f(q_\text{in}+l)}{f-l-q_\text{in}}
$$
$$
l = \frac{fq_\text{out}}{f+q_\text{out}} - q_\text{in} = \frac{f(z_\text{out}-iz_{0, \text{out}})}{f+(z_\text{out}-iz_{0, \text{out}})} - (z_\text{in}-iz_{0, \text{in}})
$$
$$
\mathrm{Re}\{ l \} = \frac{fz_\text{out}}{f+z_\text{out}} - z_\text{in}
$$
$$
\mathrm{Im}\{ l \} = -\frac{fz_{0, \text{out}}}{-z_{0, \text{out}}} + z_{0, \text{in}} = z_{0, \text{in}} -f = \frac{\pi w_\text{in}^{2}}{\lambda} - f
$$
- I think this imaginary value is the one we're trying to find???
$$
q_\text{out} = \frac{f(q_\text{in}+f)}{-q_\text{in}} \implies  -q_\text{in}q_\text{out} = fq_\text{in} + f^{2}
$$
$$
f^{2}+fq_\text{in} + q_\text{in}q_\text{out} =0
$$
