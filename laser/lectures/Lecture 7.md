As it turns out, inside a two-level system, we cannot use pumping to population invert a laser. This is because it eventually saturates at the higher level. The population increases, but very slowly.

We can get around this with a three level laser as opposed to a two level. So we pump to the third level, and these atoms drop to the second level.
![[Pasted image 20260128132957.png]]
Note that we are still only interested in the populations of 1 and 2. So regardless of how much the atoms decay from level 3, we expect to see more in level 2.

Another method is to use a four level system.
![[Pasted image 20260128133152.png]]
This method helps to populate the higher level, but it also de-populates the lower level.

Recall the fundamental equations for the transitions in a laser:
$$
\frac{dN_{2}}{dt} = -\frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) - A_{21}N_{2}
$$
$$
\frac{dN_{1}}{dt} = \frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) + A_{21}N_{2}
$$
Now what happens if we add a third level? Well this is the level being pumped to, so
$$
\frac{dN_{3}}{dt} = PN_{1} - A_{32} N_{3} + \text{Sim. Emission} + \text{Absorption}
$$
However, these last two terms are proportional to the intensity between levels $3\to 2$ and $3\to 1$. This is quite similar to the two levels we have already considered, but because of the model of our laser, these terms will be very small. So, we will ignore them.

Furthermore, the two equations between levels 1 and 2 are modified to be:
$$
\frac{dN_{2}}{dt} = -\frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) - A_{21}N_{2} + A_{32}N_{3}
$$
$$
\frac{dN_{1}}{dt} = \frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) + A_{21}N_{2} - PN_{1}
$$
Which models the decay from $3\to 2$ and the pumping from $1\to 3$.

Furthermore, the decay from $3\to 2$ it intended to be very fast, almost instant. So instead we will replace it with the pumping term in $N_{3}$ to obtain the new two level system:
$$
\frac{dN_{2}}{dt} = -\frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) - A_{21}N_{2} + PN_{1}
$$
$$
\frac{dN_{1}}{dt} = \frac{\sigma(\nu)}{h\nu} I_{\nu} (N_{2}-N_{1}) + A_{21}N_{2} - PN_{1}
$$
In the case when the laser is below or at threshold, the stimulated processes will be weak, therefore we approximate,
$$
\frac{dN_{2}}{dt} = -A_{21}N_{2} + PN_{1}
$$
$$
\frac{dN_{1}}{dt} = - \frac{dN_{2}}{dt}
$$
Where we have removed the first term, the one that models the effects of stimulated emission.

Now, in the steady state:
$$
\frac{dN_{1}}{dt} = - \frac{dN_{2}}{dt} =0
$$
Therefore,
$$
-A_{21} \bar{N}_{2} + P\bar{N}_{2} =0 \implies  \frac{\bar{N}_{2}}{\bar{N}_{1}} = \frac{P}{A_{21}}
$$
# Threshold condition
Specifically the threshold condition for a 3 level scheme.

In the steady state, we have already established that,
$$
P\bar{N}_{1} = A_{21} \bar{N}_{2}
$$
Which we can generalize to include collisional de-excitation
$$
P\bar{N}_{1} = \Gamma_{21} \bar{N}_{2}
$$
In combination with our other condition: $\bar{N}_{1}+\bar{N}_{2}=N_\text{tot}$ we obtain,
$$
\bar{N}_{1} = \frac{\Gamma_{21}}{P+\Gamma_{21}} N_\text{tot} \qquad \bar{N}_{1} = \frac{P}{P+\Gamma_{21}} N_\text{tot}
$$
Which tells us something very similar: If we want there to be more atoms in the higher level, we need our pumping to beat out the decay.

The threshold with finite cavity output coupling requires $\Delta N_{tot}$. What $P$ is required to provide $\bar{N}_{2}-\bar{N}_{1}=\Delta N_{tot}$?
$$
P_{t} = \Gamma_{21} \frac{N_\text{tot} + \Delta N_\text{tot}}{N_\text{tot}- \Delta N_\text{tot}} > \Gamma_{21}
$$
Which is called the threshold pumping rate.
