# Pumping in a 4-level system
Recall that in a 4-level system, we need to account for the simulated emission from 2 to 1, particles being pumped to 3 (and dropping to 2 instantly), spontaneous emission from 2 to 1, and the fast drop form 1 to 0. These manifest as:
$$
\frac{dN_{2}}{dt} = -\frac{\sigma I}{h\nu} (N_{2}-N_{1}) - \Gamma_{21} N_{2} + P N_{0}
$$
$$
\frac{dN_{1}}{dt} = \frac{\sigma I}{h\nu} (N_{2}-N_{1}) + \Gamma_{21} N_{2} - \Gamma_{10} N_{1}
$$
Recall that the first term is the one that arises from stimulated emission.

The steady state solution for $N_{1}$ tells us,
$$
\Gamma_{21} \bar{N}_{2} = \Gamma_{10} \bar{N}_{1} \implies  \bar{N}_{1} = \frac{\Gamma_{21}}{\Gamma_{10}} \bar{N}_{2}
$$
And this coefficient we expect to be very small, because we are trying to make the decay $1\to 0$ as quick as possible, and $2\to 1$ as slow as possible. So, in response to this we approximate $N_{1}\approx 0$.

Furthermore, we also have the constraint that,
$$
N_{0} + N_{1} + N_{2} \approx N_{0} + N_{2} = N_{T}
$$
Where $N_{T}$ is the total number of atoms in the system. Under these approximations we find the solutions,
$$
\bar{N}_{2} = \frac{P}{P + \Gamma_{21} + \sigma I /h\nu} N_{T} \qquad \bar{N}_{0} = \frac{\Gamma_{21} + \sigma I /h\nu}{P + \Gamma _{21} + \sigma I /h\nu} N_{T}
$$
$\bar{N}_{2}$ is sometimes denoted as $\Delta \bar{N}$.

The gain in this system will be something like,
$$
g(\nu) = g_{0}(\nu) \frac{P+\Gamma}{P+\Gamma + \sigma I /h\nu} \equiv  g_{0}(\nu) \frac{1}{1+I /I_{sat, 4}}
$$
Where,
$$
I_{sat, 4} = \frac{h\nu}{\sigma} (P+\Gamma)
$$
Is called the gain saturation intensity.

We expect the change in photons within the system from this gain is,
$$
\frac{dq}{dt} = \frac{cl}{L} \left[ g(\nu, I) - g_{t} \right] q
$$
Where,
$$
g_{t} = \frac{1}{2l} (1-r_{1}r_{2})
$$
Is the gain threshold we are trying to beat. $l$ is the length of the cavity.

The steady state solution to this system is,
$$
\frac{dq}{dt} =0 \implies g(\nu, I) = g_{t}
$$
Which tells us that,
$$
g(\nu) = g_{0}(\nu) \frac{1}{1+I /I_{sat, 4}} = g_{t} \implies  I = I^{(+)} + I^{(-)} = I_{sat, 4} \left( \frac{g_{0}(\nu) + g_{t}}{g_{t}} \right)
$$
![[Pasted image 20260204190759.png]]
A depiction of the intensity under small-signal gain. Notice that when $g_{t}<0$ we naturally default to saying that the intensity is zero.

![[Pasted image 20260204190924.png]]
A plot showing gain clamping, where, prior to the threshold gain, the actual gain increases before clamping and stopping once LASE occurs.

- Note that small-signal gain is when we consider the solutions to the equations close to the threshold gain where the intensity is very weak
