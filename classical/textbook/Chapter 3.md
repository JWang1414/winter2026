# Newton’s laws
- *First law*: A body moves with constant velocity (which may be zero) unless acted on by a force.
- *Second law*: The time rate of change of the momentum of a body equals the force acting on the body.
- *Third law*: For every force on one body, there is an equal and opposite force on another body

The first law provides us a definition of zero force, and the *inertial frame* (the frame of reference when the first law holds)

The second law is the familiar statement that $\vec{F}=m\vec{a}=m\ddot{x}$. It is valid only in an inertial frame.
# ODE methods in Cartesian Coordinates
Generally speaking, Newton's second law can be written like,
$$
m \frac{dv}{dt} = F(t)
$$
Which we can sometimes solve using separation of variables,
$$
m \, dv = F(t) \, dt \implies m \int_{v_{0}}^{v(t)}  \, dv' = \int_{t_{0}}^{t} F(t') \, dt'
$$
From which we have:
$$
v(t) = v_{0} + \frac{1}{m} \int_{t_{0}}^{t} F(t') \, dt'
$$
It is also possible to express $x$ in terms of $v$ by integrating the definition,
$$
v = \dot{x} \implies x(t) = x_{0} + \int_{t_{0}}^{t} v(t') \, dt'
$$
If we instead have a velocity dependent force we instead use:
$$
m = \frac{dv}{dt} = F(v) \implies m \frac{dv}{F(x)} = dt \implies t-t_{0} = m \int_{v_{0}}^{v(t)} \frac{1}{F(v')} \, dv'
$$
And then we can solve for $v(t)$ from here.

For position dependent forces, we will use chain rule to express the acceleration as a function of the position.
$$
a = \frac{dv}{dt} = \frac{dv}{dx} \frac{dx}{dt} = \frac{dv}{dx} v
$$
And so Newton's second law becomes,
$$
mv \frac{dv}{dx} = F(x)
$$
Which can once again be solved with separation of variables.
# Polar Coordinates
Recall the coordinate scalar transformations:
$$
x=r\cos\theta \qquad y=r\sin\theta
$$
And the unit vector transformations:
$$
\hat{r} = \cos\theta \hat{x} + \sin\theta \hat{y} \qquad \hat{\theta} = - \sin\theta \hat{x} + \cos\theta \hat{y}
$$
$$
\hat{x} = \cos\theta \hat{r} - \sin\theta \hat{\theta} \qquad \hat{y} = \sin\theta \hat{r} + \cos\theta \hat{\theta}
$$
Assuming $\theta$ is a function of time $\theta(t)$ the derivatives of the radial unit vectors are,
$$
\frac{d\hat{r}}{dt} = \dot{\theta}\hat{\theta} \qquad \frac{d\hat{\theta}}{dt} = - \dot{\theta} \hat{r}
$$
The position and velocities are,
$$
\vec{r} = x\hat{x}+y\hat{y} = r\hat{r} \qquad \vec{v} = \dot{r} \hat{r} + r\dot{\theta} \hat{\theta}
$$
The velocity has been solved for by taking the derivative of $\vec{r}$  and applying the chain rule on $r$ and $\hat{r}$.

The acceleration is similarly,
$$
\vec{a} = (\ddot{r} - r\dot{\theta}^{2})\hat{r} + (2\dot{r}\dot{\theta} + r \ddot{\theta}) \hat{\theta}
$$
Newton's second law is therefore,
$$
\vec{F} = m\vec{a} = m(\ddot{r} - r\dot{\theta}^{2})\hat{r} + m(2\dot{r}\dot{\theta} + r \ddot{\theta}) \hat{\theta} = m \begin{bmatrix}
\ddot{r} - r\dot{\theta}^{2} \\
2\dot{r}\dot{\theta} + r \ddot{\theta}
\end{bmatrix}
$$
Where the first element represents $\hat{r}$ and the second represents $\hat{\theta}$.
