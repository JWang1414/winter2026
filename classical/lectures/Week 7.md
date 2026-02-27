# Energy conservation in oscillators
## Simple harmonic motion
In our mass + spring system, with $-kx$ as the only acting force, then we have SHM with $\omega_{0}=\sqrt{ k /m }$. 

The total energy in the system with reference to the angular frequency is,
$$
E = \frac{1}{2} m (\dot{x}^{2} + \omega_{0}^{2}x^{2})
$$
Generally speaking when energy is conserved we can write this equation in the form:
$$
E = a \dot{q}^{2} + bq^{2}
$$
There $q$ is some variable related to position, and $E$ must be constant. Therefore we have,
$$
\dot{E} = 2a \dot{q} \ddot{q} + 2bq \dot{q} = 2 \left( \ddot{q} + \frac{b}{a}q \right)a \dot{q} =0
$$
And so we conclude the term in parenthesis is zero. This form matches the SHO equation with $\omega_{0}^{2}=b /a$.

A more explicit example might consider the general equations of motion,
$$
x(t) = A \cos(\omega_{0}t) \qquad \dot{x}(t) = -\omega_{0}A \sin(\omega_{0}t)
$$
Which therefore yields,
$$
\begin{align}
E & = \frac{1}{2} kx^{2} + \frac{1}{2} mv^{2} \\
 & = \frac{1}{2} m\omega_{0}^{2} A^{2} \cos ^{2}(\omega_{0}t) + \frac{1}{2} mA^{2} \omega_{0}^{2} \sin ^{2}(\omega_{0}t) \\
 & = \frac{1}{2} m\omega_{0}^{2} A^{2}
\end{align}
$$
![[Pasted image 20260224212120.png]]
A plot of the potential and kinetic energy reveals how the two oscillate, but sum up to a perfectly constant total energy.
- Energy is proportional to the square of the amplitude
- Frequency in the energy juggling is the twice the frequency of the motion
- The period of $K$ and $U$ is half that of $x$ and $v$
## Lightly-damped harmonic motion
This system is no longer conservative because of the addition of the $F_{d}=-bv$ term, which depends on $v$ and not $x$.
- Recall that this analysis holds only on 1-D

The friction completely removes energy from the system, it is a physical expression of the fact that there is no point in defining a potential energy for a non-conservative system.

The energy of the system reuses the same expression,
$$
E = \frac{1}{2}m (v^{2}+\omega_{0}^{2}x^{2})
$$
In some sense the damping represents a leak in the energy of our system,
$$
\frac{dE}{dt} = \frac{d}{dt} \left( \frac{1}{2}mv^{2} + \frac{1}{2} kx^{2} \right) = (ma+kx)v
$$
According to Newton's 2nd law we have,
$$
ma = -kx-bv
$$
Therefore,
$$
\frac{dE}{dt} = -bv^{2}
$$
Modelling a lightly-damped oscillator with,
$$
x(t) = A_{0} e^{ -\gamma t } \cos(\omega_{d}t) \qquad v(t) = -A_{0} e^{ -\gamma t } \left[ \omega_{d} \sin(\omega_{d}t) + \gamma \cos(\omega_{d}t) \right]
$$
If you solve for the KE and PE in this system, you will find,
$$
E = K+U \approx \frac{1}{2} kA_{0}^{2} e^{ -2\gamma t }
$$
So the mechanical energy decays exponentially. The e-folding decay scale is $1 /2\gamma$.
![[Pasted image 20260224214835.png]]
For a moderately high $Q$, the approximation works quite well here.
## Pendulum
Recall that the magnitude of a pendulum for small angles is $v_{\theta}=l\dot{\theta}$. The kinetic energy is therefore,
$$
K = \frac{1}{2} mv_{\theta}^{2} = \frac{1}{2} m(l\dot{\theta})^{2}
$$
The potential energy is,
$$
U = mgh = mgl(1-\cos\theta) \approx \frac{1}{2} mgl\theta^{2}
$$
Where we have defined $U=0$ when $\theta=0$ and $h=l(1-\cos\theta)$ as the "height above rest position". The final approximation has been done using the small angle approximation.

The mechanical energy is therefore,
$$
E = \frac{1}{2} m(l\dot{\theta})^{2} + mgl(1-\cos\theta) = \frac{1}{2} ml(l\dot{\theta}^{2} + g\theta^{2})
$$
Recall that we can use the ratio of coefficients for PE and KE to determine the natural angular frequency. We obtain,
$$
\omega_{0}^{2} = \frac{g}{l}
$$
# Motion in a general potential
When you have $U(x)\propto x^{2}$ the natural frequency can be determined by dividing the coefficient multiplying $x^{2}$ in PE and the one multiplying $\dot{x}^{2}$ in the KE.

What if we have a general potential without the $x^{2}$ term? Recall that from conservation of energy,
$$
v = \pm \sqrt{ \frac{2}{m} [E-U(x)] }
$$
Now lets say we have some arbitrary energy plot like this:
![[Pasted image 20260224215731.png]]

- Consider a particle between $x_{A}$ and $x_{B}$ when the particle reaches these outer points $v=0$ and the motion reverses. These are called *turning points*
	- This essentially means the particle is stuck in the well
- By solving $v=dx /dt \implies dt=dx /v$ you can obtain the period of oscillation between $x_{A}$ and $x_{B}$.
- If the particle starts with $E>U_{c}$ then the particle is unbounded with just one turning point on the left-side
- If a particle is inside a potential well, you can determine an escape velocity required to leave.

---
Example:
Start between $x_{A}$ and $x_{B}$ in the image above.

We require some $E>U_{c}$ to escape.
$$
E = \frac{1}{2} mv_{e}^{2} + U(x_{0}) > U_{c}
$$
Solve for $v_{e}$ to find,
$$
v_{e} = \sqrt{ \frac{2}{m} \left[ U_{c} - U(x_{0}) \right]  }
$$
- If the particle was instead moving left, it would still escape, but it would first turn back from the left before escaping on the right

---
# When can we approximate the general potential as a quadratic potential?
This is the process we had just gone with the pendulum in order to determine the angular frequency.

Consider a particle starting at least at some point $x_{0}$, with $U$ minimum.
$$
F = -\frac{dU}{dx} =0
$$
Now give the particle a small push. Expand $U(x)$ with Taylor series using some small distance $\varepsilon<x_{0}$ to find,
$$
U(x) = U(x_{0}+\varepsilon) = U(x_{0}) + \varepsilon U'(x_{0}) + \frac{1}{2} \varepsilon^{2} U''(x_{0}) + \mathcal{O}(\varepsilon^{3})
$$
$U'(x_{0})=0$ as just shown earlier.

The kinetic energy is,
$$
K = \frac{1}{2} m\dot{x}^{2} = \frac{1}{2} m\dot{\varepsilon}^{2}
$$
Define a new quantity for energy $\bar{E}=E-U(x_{0})$ which is,
$$
\bar{E} \approx \frac{1}{2} m\dot{\varepsilon}^{2} + \frac{1}{2} U''(x_{0})\varepsilon^{2}
$$
As an approximate, conserved equation for the energy.
- This works because potential energy, and therefore energy, are always defined up to a constant without loss of generality

In this notation, the equivalent method for the frequency of a SHO is,
$$
\omega^{2} = \frac{U_{0}''(x_{0})}{m}
$$
This form for the oscillation frequency will be true for motion in any force near a local minimum in the potential.
- This is valid for any case where $U''(x_{0})=0$ in the Taylor series (almost always true)

---
Example: Morin 5.9

A particle moves under the influence of a potential $U(x)=-Cn^{n} e^{ ^{-ax} }$. Find the frequency of small oscillations around the equilibrium point located at $x>0$. Assume that $n\geq 2$.

First, find the equilibrium point,
$$
F = -\frac{dU}{dx} =0
$$
$$
U'(x) = -Cnx^{n-1}e^{ -ax } + Cax^{n} e^{ -ax } = -Ce^{ -ax } x^{n-1} (n-ax) =0
$$
Which is satisfied when,
$$
x = x_{e} = \frac{n}{a}
$$
Now computer the second derivative at $x_{e}$,
$$
U''(x_{e}) = C e^{ -n } n^{n-1} a^{-(n-2)}
$$
Therefore by our definition we have,
$$
\omega^{2} = \frac{Ce^{ -n }n^{n-1}}{ma^{n-2}}
$$
This is well defined so long as $U''>0$ and $U(x_{e})$ is a minimum.

---
# General energy potentials: the view from phase space
## Simple harmonic motion
A spring has total energy,
$$
E = \frac{1}{2}mv^{2} + \frac{1}{2} kx^{2}
$$
Which describes an ellipse for all values $E>0$. The points $x=\pm \sqrt{ 2E /k }$ are the turning points, because $v=0$ and the particle turns around.
![[Pasted image 20260226221454.png]]
The energy in the SHO, plotted on a contour grid.

The trajectory of the mass attached to the oscillating system goes along the constant lines of energy.

We can see here that the oscillation occurs around the energy minimum, proceeding in a clockwise motion.
## Projectile motion
For projection motion we instead have,
$$
E = \frac{1}{2}mv^{2} + mgz
$$
Which results in the phase plot:
![[Pasted image 20260226221703.png]]

Notice how in this case, there is no energy minimum or oscillatory motion, the trajectories correspond to the rising and falling motion of vertically projected particles.
# Non-linear pendulum
The equation of motion for some non-linear pendulum is,
$$
\ddot{\theta} + \omega_{0}^{2} \sin \theta =0
$$
Where $\omega_{0}$ is the angular frequency in the weak-amplitude limit.

The potential energy from the gravitational force is,
$$
U(\theta) = mgl(1-\cos\theta)
$$
Conservation of energy states,
$$
E = \frac{1}{2} ml^{2}\dot{\theta}^{2} + mgl(1-\cos\theta) = mgl(1-\cos\Theta)
$$
Where $\Theta$ is the maximum angle of oscillation.

Using our previously derived equation to find the period of oscillation:
$$
T = \frac{2\sqrt{ 2 }}{\omega_{0}} \int_{0}^{\Theta} \frac{1}{\sqrt{ \cos\theta - \cos\Theta }}  \, d\theta
$$
And its energy can be shown to be,
![[Pasted image 20260226222400.png]]

There are two unique regimes that arise here. For $E<2mgl$, the energy of the oscillator is insufficient to roll, and the trajectory follows an ellipses, mirroring simple harmonic motion.

For $E>2mgl$ we have rolling motion. The pendulum escapes the local potential well and "spins around" the pendulum.

The boundary $E=2mgl$ is called the *separatrix*, it is highlighted in red. Furthermore, notice that the crossings in the separatrix occur at local maximum, unstable equilibriums.

![[Pasted image 20260226224129.png]]
The numerical integration of the non-linear pendulum using the Euler-Cromer method.

The pendulum oscillates with some period $T$, but the oscillations aren't quite sinusoidal. The $\dot{\theta}$ curve in particular is a-sinusoidal.
- Larger $\Theta$ will result in larger distortions

![[Pasted image 20260226224318.png]]
A numerical integration of the non-linear pendulum, visualized in a phase-plot using the Euler-Cromer method.

The "diamond-like" shape of the phase plot shows us that the behaviour of SHM is gone.
## Fourier analysis of the non-linear pendulum
There is no clean analytical solution for the behaviour of a non-linear pendulum, and so we must instead use numerical analysis and FFTs to determine its behaviour.

The resulting Fourier modes look like
![[Pasted image 20260226225019.png]]
So it is clear that the dominant mode coefficient is -2.5 radians.

On a semi-log scale, the $\lvert A_{n} \rvert$s are:
![[Pasted image 20260226225154.png]]
Which helps to visualize the effects of the higher harmonics.

A few things to notice here:
- Mode 1 dominates
- Odd-modes appear to decay by some constant factor
- Even-modes are significantly smaller.
## Non-linear effects create higher frequencies
Our approach will be to represent non-linearities as weak perturbations to the linear oscillation.

Use the Taylor series expansion of $\sin\theta$ to obtain,
$$
\ddot{\theta} + \omega_{0}^{2} \theta = -\frac{\omega_{0}^{2}}{6} \theta^{3}
$$
Where the equation has been re-arranged to depict the higher order approximations to sine as a forcing to the harmonic oscillator.

For simplicity, lets just assume the oscillation of the forcing has $\omega=2\pi /T$ with a sinusoidal form. In this case the linear forcing will be proportional to,
$$
\cos ^{3}(\omega t) = \frac{\cos(3\omega t) + 3 \cos(\omega t)}{4}
$$
So the non-linear term includes both a $\omega$ frequency and a forcing oscillating at $3\omega$.
- This term is of course comparatively very small

If we then approximate the signal to be,
$$
\theta \approx \Theta_{1} \cos \omega t + \Theta_{3} \cos(3\omega t)
$$
And plug this back into the non-linear term $\omega_{0}^{2}\theta^{3} /6$ the result will have more frequencies. These frequencies have odd-numbered modes, and the coefficients corresponding to higher-numbered modes are progressively weaker.

One other way to imagine this, is that if you add up more corrections to the Taylor series expansion,
$$
\sin\theta \approx \theta - \frac{\theta^{3}}{3!} + \frac{\theta^{5}}{5!} - \frac{\theta^{7}}{7!} + \dots
$$
You create more occasions to create more frequencies.