- I missed this one so I'm taking notes from the answers
# Question 1
Note that according to conservation of energy we have,
$$
\frac{1}{2} mv^{2} + mgy = \frac{mv_{0}^{2}}{2}
$$
Which can be re-arranged to find,
$$
v = \sqrt{ v_{0}^{2}-2gy }
$$
We are interested in keeping the purely vertical portion of this velocity constant.
$$
\dot{y} = v \sin\theta
$$
Where $\theta$ is the angle between the wire and the $x$-axis. Note that the slope of the wire is,
$$
\tan\theta = \frac{dy}{dx} = y'
$$
Use the trig identity:
$$
\sin\theta = \frac{\tan\theta}{\sqrt{ 1+\tan ^{2}\theta }} = \frac{y'}{\sqrt{ 1+(y')^{2} }}
$$
We require $\dot{y}=-v_{0}$ and so,
$$
v\sin\theta = \sqrt{ v_{0}^{2}-2gy } \left[ \frac{y'}{\sqrt{ 1+(y')^{2} }} \right] =-v_{0}
$$
Skipping through the algebra,
$$
y'=\frac{dy}{dx}=-\frac{v_{0}}{\sqrt{ -2gy }}
$$
Solve this ODE with separation of variables to obtain the function,
$$
y = - \frac{(3gv_{0}x)^{2/3}}{2g}
$$
# Question 2
---
a.
Substitute this into our expression for the conservation of energy,
$$
E = \frac{1}{2} mv^{2} - A\lvert x \rvert ^{n} = 0 \implies  \frac{mv^{2}}{2} = A\lvert x \rvert ^{n}
$$
Assume $v>0$ to make the problem a little easier to work with. If $v<0$, that just means it's going in the opposite direction.
$$
v=\frac{dx}{dt} = \sqrt{ \frac{2A}{m} } \lvert x \rvert ^{n/2}
$$
Use separation of variables,
$$
t = \sqrt{ \frac{m}{2A} } \int_{x_{0}}^{0} \frac{1}{\lvert x \rvert ^{n/2}} \, dx
$$
Where $t$ is the total time required to reach the origin.

Note that this integral is finite only when $n /2<1$ and so we require that $n<2$.

---
b.
This time, we instead have,
$$
E = \frac{mv^{2}}{2} - A\lvert x \rvert ^{n} > 0 \implies  v=\frac{dx}{dt} = \sqrt{ \frac{2}{m} (E+A\lvert x \rvert ^{n}) }
$$
Use separation of variables to obtain the integral,
$$
t = \sqrt{ \frac{m}{2} } \int_{x_{0}}^{\infty} \frac{1}{\sqrt{ E+A\lvert x \rvert ^{n} }} \, dx
$$
When $x$ is large, this integral is approximately,
$$
\frac{1}{\sqrt{ A }} \int_{x_{0}}^{\infty} \frac{1}{\lvert x \rvert ^{n/2}} \, dx
$$
Which converges when $n /2>1$. Therefore $t$ is finite when $n>2$.
# Question 3
By conservation of energy,
$$
E = \frac{mv^{2}}{2} + A\lvert x \rvert >0
$$
The turning points in this system will be at,
$$
E=A\lvert x \rvert \implies x = \pm \frac{E}{A}
$$
The particle oscillates between these two points.

Replace $v$ with $dx /dt$, and substitute into the conservation of energy to find,
$$
\frac{m}{2} \left( \frac{dx}{dt} \right) ^{2} = E-A\lvert x \rvert
$$
Use separation of variables, and re-arrange to obtain,
$$
dt = \sqrt{ \frac{m}{2} } \int \frac{1}{\sqrt{ E-A\lvert x \rvert  }} \, dx
$$
The period will be the time it takes to get go from one turning point to the other, and then go back,
$$
T = 2\sqrt{ \frac{m}{2} } \int_{-E /A}^{E /A} \frac{1}{\sqrt{ E-A\lvert x \rvert  }} \, dx
$$
Compute this integral to solve for the period of oscillation:
$$
T = \frac{4}{A} \sqrt{ 2mE }
$$
