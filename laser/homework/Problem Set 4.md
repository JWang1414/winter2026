# Question 1
---
a.
Since the waist has been placed at the lens, the $q$ parameter for the input beam is,
$$
q_\text{in} = z_\text{in} -iz_{0, \text{in}} = z_\text{in} -\frac{i\pi w_\text{in}^{2}}{\lambda} = -\frac{i\pi w_\text{in}^{2}}{\lambda}
$$
Because $z_\text{in}=0$. The ABCD matrix for this system is,
$$
\begin{bmatrix}
1 & l \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} = \begin{bmatrix}
1-l /f & l \\
-1 /f & 1
\end{bmatrix}
$$
According to the Mobius transform,
$$
q_\text{out} = \left[ \frac{1}{R(l)} + \frac{i\lambda}{\pi w_\text{out}^{2}} \right] ^{-1} = \frac{(1-l /f)q_\text{in}+l}{(-1 /f)q_\text{in}+1}
$$
Evaluate,
$$
q_\text{out} = \frac{fq_\text{in}}{f-q_\text{in}}+l \implies  l = z_\text{out} -\frac{i\pi w_\text{out}^{2}}{\lambda} + \frac{fi\pi w_\text{in}^{2} /\lambda}{f+i\pi w_\text{in}^{2} /\lambda}
$$
So, for a Gaussian beam, $l \neq f$. Now, equating the real parts of the above expression yields,
$$
R(l) = \frac{(l /z_{0, \text{in}}) + (1-l /f)^{2}}{l /z_{0, \text{in}}^{2} - (1 /f)(1-l /f)}
$$
The new beam waist will occur when $R(l)\to \infty$ and so,
$$
\frac{l}{z_{0, \text{in}}^{2}} - \frac{1}{f} \left( 1-\frac{l}{f} \right) =0 \implies  l=\frac{f}{1+f^{2} /z_{0, \text{in}}^{2}}
$$
The limit when $l=f$ occurs when $z_{0, \text{in}}\to \infty$. That is, when the Gaussian beam no longer widens, and so resembles a straight line.

---
b.
Equating the imaginary portions of the previous expression,
$$
w^{2}(l) = w_\text{in}^{2} \left( 1-\frac{l}{f} \right)^{2} + w_\text{in}^{2}\left( \frac{l}{z_{0}} \right)^{2}
$$
Substitute in the value of $l$ from above to find,
$$
w^{2}\left( \frac{f}{1+f^{2} /z_{0, \text{in}}^{2}} \right) = w_\text{in}^{2} \left( 1-\frac{1}{f}\left( \frac{f}{1+f^{2} /z_{0, \text{in}}^{2}} \right)  \right)^{2} + w_\text{in}^{2}\left( \frac{1}{z_{0}} \left( \frac{f}{1+f^{2} /z_{0, \text{in}}^{2}} \right)  \right)^{2}
$$
$$
w(l) = \frac{\lambda f}{\pi w_\text{in}} \frac{1}{\sqrt{ 1+f^{2} /z_{0, \text{in}}^{2} }}
$$
---
c.
In the case where $f\gg z_{0, \text{in}}$ we have that,
$$
\frac{f^{2}}{z_{0, \text{in}}^{2}} \to  \infty \implies  \sqrt{ 1+\frac{f^{2}}{z_{0, \text{in}}^{2}} } \to \infty
$$
Which means,
$$
w(l) \to 0
$$
 And so the waist is being focused to a very small point here.

---
# Question 3
