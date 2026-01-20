# Continuity equation for EM waves
Generally speaking, continuity equations say stuff like: "Everything that goes in must go out, or it must stay there"
$$
\frac{1}{c} \frac{ \partial I_{\nu} }{ \partial t } + \frac{ \partial I_{\nu} }{ \partial z } =0
$$
Lets consider a situation with a lab of area $A$, and width $\Delta z$. The intensity illuminating the slab is $I_{\nu}$ and the intensity leaving the slab is some $I_{\nu}+\Delta I$
- INSERT IMAGE HERE

Now lets try to pack the continuity equation provided to us. Well, the EM energy density is defined to be,
$$
u_{\nu} = \frac{I_{\nu}}{c} \implies  \frac{ \partial  }{ \partial t } (u_{\nu}\times \text{Volume}) = \frac{A(\Delta z)}{c} \frac{ \partial I_{\nu} }{ \partial t }
$$
This is the change in energy density in the slab. Which we can equate to the change in intensity on the area of the slab
$$
A(\Delta I) = -\frac{A(\Delta z)}{c} \frac{ \partial I_{\nu} }{ \partial t }
$$
- Honestly, I have no idea where the $A(\Delta I)$ came from

Divide both sides by $A(\Delta z)$ to find,
$$
\frac{\Delta I}{\Delta z} = -\frac{1}{c} \frac{ \partial I_{\nu} }{ \partial t }
$$
Which is an approximation of the continuity equation.

However, lets suppose that the slab is now a gain medium. In this case we wouldn't expect the RHS to be 0, we would expect something like,
$$
\frac{1}{c} \frac{ \partial I_{\nu} }{ \partial t } + \frac{ \partial I_{\nu} }{ \partial z } =c_{1}
$$
Where $c_{1}$ is some constant.

So far, our understanding of the number of excited atoms within the laser is governed by this equation:
$$
\frac{dN_{2}}{dt} = -\frac{\sigma(\nu)}{h\nu} (N_{2}-N_{1}) - A_{21}N_{2}
$$
- The $N_{2}-N_{1}$ term indicates the changes resulting from simulated emission and absorption
- The $A_{21}N_{2}$ term is the loss from spontaneous emission. In a two level system, these particles are shot out because of decay from $2\to 1$, but cannot be regained

Recall that $\sigma(\nu)$ has the form,
$$
\sigma(\nu) = \frac{\lambda^{2}A_{21}}{8\pi} S(\nu)
$$
The change in the EM energy density of a propagating wave is:
$$
\frac{d}{dt}(\text{EM energy dense...}) = \sigma I\tilde{N}_{2} - \sigma I \tilde{N}_{1} \left( \frac{g_{2}}{g_{1}} \right)
$$
Where $\tilde{N}=N /\text{Volume}$
- This has arisen because we are looking for the energy change from the gain medium, that is, when the RHS term is non-zero. Which is why it scales with the number of particles in the excited and ground states of the system
- Notice that the spontaneous emission term does not show up, this is because for a propagating wave, it does not effect the overall energy
	- Little fuzzy on this one
- The $g_{2} /g_{1}$ term arises from energy degeneracy in the system
	- The degeneracy terms are constants, they are the number of states in the upper or lower levels

Implementing this gain equation back into the continuity equation we had:
$$
\frac{1}{c} \frac{ \partial I_{\nu} }{ \partial t } + \frac{ \partial I_{\nu} }{ \partial z } = \sigma(\nu) \left[ \tilde{N}_{2} - \frac{g_{2}}{g_{1}} \tilde{N}_{1} \right] I_{\nu}
$$
The portion on the right hand side:
$$
g(\nu) = \left[ \tilde{N}_{2} - \frac{g_{2}}{g_{1}} \tilde{N}_{1} \right]
$$
Is called the gain coefficient. The negative version $a(\nu)=-g(\nu)$ is called the absorption coefficient.

This begs the question: What do we require for the gain coefficient to be positive?
$$
\tilde{N}_{2} - \frac{g_{2}}{g_{1}} \tilde{N}_{1} > 0 \implies  \frac{\tilde{N}_{2}}{g_{2}} > \frac{\tilde{N}_{1}}{g_{1}}
$$
This is effectively telling us that the number of atoms per quantum state must be higher in the excited level than the ground level. This is called *inversion*
- *Inversion:* The number of atoms per quantum state is higher in the excited manifold than ground manifold
- It is called inversion because it goes against the state atoms would like to be in: where most atoms are in the ground state
