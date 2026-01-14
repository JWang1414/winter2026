# Question 1
For some very small angle $d\theta$ the tension force is,
$$
\vec{T}(\theta) = \begin{bmatrix}
-\sin\left( \frac{d\theta}{2} \right) \\
-\cos\left( \frac{d\theta}{2} \right)
\end{bmatrix} T(\theta) \qquad \vec{T}(\theta+d\theta) = \begin{bmatrix}
-\sin\left( \frac{d\theta}{2} \right) \\
\cos\left( \frac{d\theta}{2} \right)
\end{bmatrix} T(\theta+d\theta)
$$
The net forces around the pole are therefore,
$$
F_{x} = N - \sin\left( \frac{d\theta}{2} \right) (T(\theta) + T(\theta + d\theta)) =0
$$
$$
F_{y} = -F_{s} + \cos\left( \frac{d\theta}{2} \right) (T(\theta+d\theta) - T(\theta)) =0
$$
Where $N$ is the normal force and $F_{s}$ is the force resulting from the static friction. Now that we have this expression for the force, we will take the limit as $d\theta\to 0$ and approximate the sines, cosines, and $T(\theta+d\theta)$ using just their first order Taylor series components.
$$
T(\theta + d\theta) = T(\theta) + T'(\theta) d\theta
$$
Our original equations become:
$$
N - \frac{d\theta}{2} (T(\theta) + T(\theta) + T'(\theta)d\theta) =0
$$
$$
-F_{s}+  (T(\theta) + T'(\theta)d\theta - T(\theta))=0
$$
We can remove the term in the first equation that goes by $d\theta^{2}$ because it is very small. From which we obtain,
$$
N = T(\theta) d\theta
$$
$$
\mu_{s}N + T'(\theta) d\theta =0
$$
Substitute these equations into each other to find,
$$
\mu_{s} T(\theta) d\theta + T'(\theta) d\theta =0 \implies T' = \mu_{s}T
$$
Which is the differential equation you can solve to find the tension
# Question 2
---
1.
Given the equation:
$$
\vec{r} = \vec{r}_{0} + \vec{v}_{0}t + \frac{1}{2} \vec{a} t^{2}
$$
Define the firefighter's initial location to be (0, 0).

The initial velocity of the water is:
$$
v_{x} = v_{0} \cos\theta_{0} \qquad v_{y} = v_{0} \sin\theta_{0}
$$
The acceleration is always,
$$
a_{y} = -g
$$
Resulting from gravity. This gives two equations.
$$
D = v_{0}\cos\theta_{0}t \qquad H = v_{0}\sin\theta_{0}t - \frac{g}{2} t^{2}
$$
Substitute the first equation into the second.
$$
H = v_{0} \sin\theta_{0} \left( \frac{D}{v_{0}\cos\theta_{0}} \right) - \frac{g}{2} \left[ \frac{D}{v_{0}\cos\theta_{0}} \right] ^{2}
$$
Apply the identity:
$$
\frac{1}{\cos ^{2}\theta} = 1 + \tan ^{2}\theta
$$
And simplify:
$$
H = D \tan\theta - \frac{g}{2} \frac{D^{2}}{v_{0}^{2}} (1+\tan ^{2}\theta)
$$
Note that this is a quadratic. Use the substitution $u=\tan ^{2}\theta$ and solve for $u$. Then determine the two possible solutions for $\theta$.

---
2.
- Not done
# Question 3
- The acceleration from gravity is always vertically downwards. So wouldn't this be the case whenever $N=0$ or at the very top of the hoop?

Assume the bead never leaves the hoop. The tangential acceleration is,
$$
a_{t} = g \sin\theta
$$
And the radial acceleration is,
$$
a_{R} = \frac{v^{2}}{R} = \frac{2gh}{R}
$$
- This substitution results from conservation of energy.

The height of the bead is,
$$
h = R(1-\cos\theta)
$$
So the acceleration along the $x$ is,
$$
a_{x} =  a_{t} \cos\theta - a_{R} \sin\theta =0
$$
