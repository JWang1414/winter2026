# Question 1
---
a.
The 4-level system is more efficient when,
$$
A_{10}N_{1} \gg  A_{21}N_{2}, A_{21} \left( \frac{I}{2I_{s}} \right)N_{1}, A_{21} \left( \frac{I}{I_{s}} \right)N_{2}
$$
Divide by $N_{1}$, and make the approximation that the rate of stimulated emission is roughly equivalent to the pumping rate to end up with,
$$
A_{10} \gg  \left\{  A_{21} \left( \frac{I}{I_{s}} \right), P  \right\}
$$
Which is valid because we are assuming this is the case above threshold (so the laser is firing).

The reason it is more efficient is because absorption from $1\to 2$ is reduced by the depopulation of 1. This means we need less pumping strength to create inversion.

---
b.
Collisional broadening $\delta \nu$ is proportional to the atomic number-density $\tilde{N}=N /V$. So for $N_{A}=2N_{B}$ we have $\delta \nu_{A}=2(\delta \nu_{B})$.

The absorption of light is exponential:
$$
e^{ -a(\nu)l } = e^{ -\tilde{N}\sigma(\nu)l }
$$
The cross-section here is,
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu) \qquad S(\nu_{0}) \approx \frac{1}{\delta \nu}
$$
The second equation is true on resonance. So therefore we have approximately:
$$
\sigma_{A} (\nu_{0}) = \frac{1}{2} \sigma_{B} (\nu_{0})
$$
Combining what we know:
$$
\frac{a_{A}}{a_{B}} = \frac{\tilde{N}_{A} \sigma_{A}}{\tilde{N}_{B}\sigma_{B}} = 1
$$
So the two cells have equal absorption on resonance.
# Question 2
---
a.
Neglecting degeneracy we have,
$$
\frac{dN_{2}}{dt} = -\frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) - A_{21}N_{2} = -\frac{dN_{1}}{dt}
$$
Use the identity:
$$
I_\text{sat} = \frac{h\nu A_{21}}{2\sigma(\nu)} \implies  \sigma(\nu) = \frac{h\nu A_{21}}{2I_\text{sat}}
$$
Then we have,
$$
\frac{dN_{2}}{dt} =- A_{21} \frac{I_{\nu}}{2_\text{sat}} N_{2} + A_{21} \frac{I_{\nu}}{2I_\text{sat}} N_{1} - A_{21} N_{2}
$$
The first term is the one we are interested in.

---
b.
The ratio of stimulated to spontaneous emission is:
$$
\frac{I}{2I_\text{sat}} = \frac{3}{2}
$$
---
c.
The ratio of stimulated emission to absorption is:
$$
\frac{A_{21}(I /2I_\text{sat})N_{2}}{A_{21}(I /2I_\text{sat})N_{1}} = \frac{N_{2}}{N_{1}}
$$
Solve for the steady state ratio between the two:
$$
0=- A_{21} \frac{I_{\nu}}{2_\text{sat}} N_{2} + A_{21} \frac{I_{\nu}}{2I_\text{sat}} N_{1} - A_{21} N_{2}
$$
Which yields,
$$
\frac{1}{2}s \bar{N}_{1} = \left( \frac{1}{2}s +1 \right) \bar{N}_{2}
$$
Where we have defined: $s=I /I_\text{sat}$.

Solve for the ratio to find,
$$
\frac{\bar{N}_{2}}{\bar{N}_{1}} = \frac{s /2}{1 + s /2} = \frac{3}{5}
$$
