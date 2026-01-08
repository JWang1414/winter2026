Generally speaking, when we have time dependent forces we solve the problem
$$
m \frac{dv}{dt} = F(t)
$$
Which we can solve with whatever ODE methods we please.

You can solve with separation of variables like so:
$$
m \frac{dv}{dt} = F(t) \implies m \, dv = F(t) \, dt \implies m \int_{v_{0}}^{v(t)}  \, dv = \int_{t_{0}}^{t} F(t) \, dt
$$
Where $v_{0}$ and $t_{0}$ are the initial velocity and time, and $v(t)$ and $t$ denote the current time in the system.