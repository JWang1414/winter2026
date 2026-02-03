# Damped Oscillators
---
1a.
Combining all the forces we have,
$$
F = -ky-bv-mg=ma
$$
Which we can rearrange to,
$$
m\ddot{y} + b\dot{y} + ky=-mg
$$
Where I have substituted the velocity and acceleration with the differential forms.

You can solve this ODE with change of variables,
$$
y = z-\frac{mg}{k}
$$
Which transforms this to:
$$
m\ddot{z} + b\dot{z} + kz=0
$$
So we know have a homogeneous ODE, which we can easily compare to our previous problems

---
1b.
Recall the definition of $\omega$,
$$
\omega(\gamma) = \sqrt{ \omega_{0}^{2}-\gamma^{2} }
$$
According to the given information,
$$
\sqrt{ \omega_{0}^{2}-\gamma^{2} } = \frac{\sqrt{ 3 }}{2} \omega_{0}
$$
Solve this equation for $\gamma$
$$
\gamma = \frac{\omega_{0}}{2}
$$
And so we therefore have,
$$
b = 2\gamma m = \frac{\omega_{0}}{m}
$$
---
2.
This system is critically damped so:
$$
\omega_{0} = \gamma = \sqrt{ \frac{k}{m} }
$$
Solve for $k$ using typical method:
$$
kx-mg=0 \implies  kx=mg \implies  k = \frac{mg}{x}
$$
The value of $b$ is,
$$
b = 2\gamma m = 2\sqrt{ km } = 2\sqrt{ \left( \frac{mg}{x} \right) m } = 2m\sqrt{ \frac{g}{x} }
$$
---
3a.
Recall we have,
$$
Q = \frac{\omega_{0}}{\gamma} \qquad \omega_{d} = \sqrt{ \omega_{0}^{2}-\gamma^{2} } = \omega_{0} \sqrt{ 1-Q^{-2} }
$$
- I think this question is just plugging in numbers
# Simple Driving
The amplitude is,
$$
A = \frac{\omega_{0}^{2}A_{f}}{\sqrt{ \omega_{0}^{2}+\omega^{2})^{2}+4\gamma^{2}\omega^{2} }}
$$
And the response is,
$$
\delta(\omega) = \arctan\left( \frac{2\gamma \omega}{\omega_{0}^{2}-\omega^{2}} \right)
$$
- Or something like this anyways. We're running out of time