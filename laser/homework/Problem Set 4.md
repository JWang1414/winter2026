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

# Question 2
---
a.
The form for this beam is,
$$
E(x, y, z, t) = E_{0} \exp \left( -\frac{x^{2}+y^{2}}{w_{0}^{2}} \right)e^{ -i\omega t }
$$
Fraunhofer approximation:
$$
\mathcal{E}(x, y, z) = -\frac{i}{\lambda z} e^{ ikz } \exp\left( \frac{ik}{2z} (x^{2}+y^{2}) \right) \iint \mathcal{E}(x', y', 0) \exp\left( -\frac{ik}{z}(xx'+yy') \right) \, dx' \, dy'
$$
Compute,
$$
\iint E_{0} \exp \left( -\frac{x'^{2}+y'^{2}}{w_{0}^{2}} \right)e^{ -i\omega t } \exp\left( -\frac{ik}{z}(xx'+yy') \right) \, dx' \, dy'
$$
$$
E_{0} e^{ -i\omega t } \int e^{ -x'^{2}/w_{0}^{2} } e^{ -ikxx'/z } \, dx ' \int e^{ -y'^{2}/w_{0}^{2} } e^{ -ikyy'/z } \, dy'
$$
There is really just one integral here,
$$
\int \exp\left( -\frac{x'^{2}}{w_{0}^{2}} - \frac{ik}{z}xx' \right) \, dx' = \sqrt{ \pi } w_{0}\exp \left[ -\left( \frac{kw_{0}x}{2z} \right)^{2} \right]
$$
$$
E_{0} e^{ -i\omega t } \pi w_{0}^{2} \exp \left[ -\left( \frac{kw_{0}}{2z} \right)^{2}(x^{2}+y^{2}) \right]
$$
Total function is,
$$
\mathcal{E}(x, y, z) = -\frac{i}{\lambda z} e^{ ikz } \exp\left( \frac{ik}{2z} (x^{2}+y^{2}) \right) \left[ E_{0} \pi w_{0}^{2} \exp \left[ -\left( \frac{kw_{0}}{2z} \right)^{2}(x^{2}+y^{2}) \right] \right]
$$
$$
\mathcal{E}(x, y, z) = -\frac{i\pi w_{0}^{2}}{\lambda z} E_{0} e^{ ikz } \exp\left( \frac{ik}{2z} (x^{2}+y^{2}) \right) \exp \left[ -\left( \frac{kw_{0}}{2z} \right)^{2}(x^{2}+y^{2}) \right]
$$
By observation, the spot size of this new beam is,
$$
w(z) = \left( \frac{kw_{0}}{2z} \right)^{-1} = \frac{2z}{kw_{0}} = \frac{\lambda z}{\pi w_{0}} = \frac{w_{0}z}{z_{0}}
$$
The amplitude is decaying like,
$$
\frac{\pi w_{0}^{2}}{\lambda z}E_{0} = \frac{w_{0}}{w(z)} E_{0}
$$
And the phase front curvature $R(z)$ is still spherical as revealed by the term:
$$
\exp \left[ \frac{ik}{2z}(x^{2}+y^{2}) \right]
$$
So, in comparison to the PWE equation, the curvature is still spherical, but the amplitude now decays according to $z^{-1}$ and the spot size increases linearly with $z$.

The limit where the PWE solution matches this solution is when,
$$
w_{0}\sqrt{ 1+\frac{z^{2}}{z_{0}^{2}} } \to  \frac{w_{0}z}{z_{0}}
$$
Which is the case when $z\gg z_{0}$, where the beam width expands linearly.

---
b.
Fresnel Approximation:
$$
E(x, y, z) = -\frac{i}{\lambda z} e^{ ikz } e^{ ik(x^{2}+y^{2})/2z } \iint E(x', y', 0) \exp \left[ \frac{ik}{2z}(x'^{2}+y'^{2}) \right] \exp \left[ -\frac{ik}{z}(xx'+yy') \right]  \, dx' \, dy'
$$
Compuyte,
$$
\iint \exp \left( -\frac{x'^{2}+y'^{2}}{w_{0}^{2}} \right) \exp \left[ \frac{ik}{2z}(x'^{2}+y'^{2}) \right] \exp \left[ -\frac{ik}{z}(xx'+yy') \right]  \, dx' \, dy'
$$
Once again can be split into duplicates of the same integral,
$$
\iint \exp \left[ -\frac{x'^{2}}{w_{0}^{2}} + \frac{ik}{2z}x'^{2} - \frac{ik}{z}xx' \right] \, dx' = \iint \exp\left[ -\left( \frac{1}{w_{0}^{2}} - \frac{ik}{2z} \right)x'^{2}-\frac{ik}{z}xx' \right] \, dx'
$$
Gaussian integral:
$$
\int_{-\infty}^{\infty} e^{ -ax^{2}-bx } \, dx = \sqrt{ \frac{\pi}{a} } e^{ b^{2}/4a }
$$
In this case,
$$
a = \frac{1}{w_{0}^{2}} - \frac{ik}{2z} = \frac{1}{w_{0}^{2}}\left( 1- \frac{ikw_{0}^{2}}{2z} \right) = \frac{1}{w_{0}^{2}}\left( 1-\frac{iz_{0}}{z} \right) \qquad b=\frac{ikx'}{z}
$$
Integral result:
$$
\sqrt{ \frac{\pi}{(1-iz_{0} /z) /w_{0}^{2}} } \exp\left( \frac{(ikx' /z)^{2}}{4(1-iz_{0} /z) /w_{0}^{2}} \right) = \sqrt{ \frac{\pi w_{0}^{2}}{1-iz_{0} /z} } \exp\left( -\frac{(kw_{0}x /z)^{2}}{4(1-iz_{0} /z)} \right)
$$
Total:
$$
-\frac{i}{\lambda z} e^{ ikz } e^{ ik(x^{2}+y^{2})/2z } \frac{\pi w_{0}^{2}}{1-iz_{0} /z} E_{0} \exp \left[ -\left( \frac{kw_{0}}{2z} \right)^{2} \frac{x^{2}+y^{2}}{1-iz_{0} /z} \right]
$$
$$
- \frac{iz_{0}}{z} \frac{E_{0}}{1-i z_{0} /z} e^{ ikz } e^{ ik(x^{2}+y^{2})/2z } E_{0} \exp \left[ -\left( \frac{kw_{0}}{2z} \right)^{2} \frac{x^{2}+y^{2}}{1-iz_{0} /z} \right]
$$
- I suspect that this version is supposed to be more similar to the PWE solution but I'm struggling to come up with anything here
# Question 3
Propagate 20 cm, go through a lens, and then enter a slab of glass.
$$
\begin{bmatrix}
1 & 0 \\
0 & n_{1} /n_{2}
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & d \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
1 & d \\
-\frac{n_{1}}{fn_{2}} & \frac{n_{1}}{n_{2}}-\frac{n_{1}d}{fn_{2}}
\end{bmatrix}
$$
$$
q_{f} = \frac{q_{i}+d}{-(n_{1} /fn_{2})q_{i}+(n_{1} /n_{2} - n_{1}d /fn_{2})} = -\frac{fn_{2}(d+q_{i})}{n_{1}(d-f+q_{i})}
$$
$$
= - \frac{2(1.5)(20+q_{i})}{1(20-2+q_{i})} = -\frac{3(q_{i}+20)}{q_{i}+18}
$$
$$
q_{i} = z+iq_{0} = -20+iq_{0}
$$
$$
q_{f} = -\frac{3(-20-iz_{0})+20}{-20-iz_{0}+18}
$$
$$
\frac{1}{q_{f}} = \frac{1}{R} + i \frac{\lambda}{\pi n_{2}w^{2}} = -\frac{3z_{0}^{2}+80}{9z_{0}^{2}+1600} - i \frac{34z_{0}}{9z_{0}^{2}+1600}
$$
Equate the real and imaginary parts:
$$
\frac{1}{R} = -\frac{3z_{0}^{2}+80}{9z_{0}^{2}+1600}
$$
$$
\frac{\lambda}{\pi nw^{2}} = - \frac{34z_{0}}{9z_{0}^{2}+1600}
$$
Where,
$$
z_{0}= \frac{\pi n_{1}w_{0}^{2}}{\lambda} = \frac{\pi w_{0}^{2}}{\lambda} = \frac{\pi(50\times 10^{-4})^{2}}{0.5\times 10^{-4}} = 0.5\pi \text{ cm}
$$
