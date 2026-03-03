- I need to complete 2c
- Are my processes for Q1 even valid? I'm using mostly stuff from PHY385
	- Check my answers for 1d and 1e
	- Drawings for this question have been done on separate pieces of paper
# Question 2
---
a.
From lecture the provided definition of $I_{R} /I_\text{in}$ can be re-arranged into:
$$
\frac{I_{R}}{I_\text{in}} = R \left| \frac{1-e^{ i\Phi }}{1-R e^{ i\Phi }} \right| ^{2} = \frac{4R \sin ^{2}(\Phi /2)}{(1-R)^{2} + 4R \sin ^{2}(\Phi /2)}
$$
So the transmitted intensity is therefore:
$$
\frac{I_{T}}{I_\text{in}} = 1- \frac{I_{R}}{I_\text{in}} = 1- \frac{4R \sin ^{2}(\Phi /2)}{(1-R)^{2} + 4R \sin ^{2}(\Phi /2)} = \frac{(1-R)^{2}}{(1-R)^{2} + 4R \sin ^{2}(\Phi /2)}
$$
Factor out $(1-R)^{2}$ from the numerator and denominator to find:
$$
\frac{I_{T}}{I_\text{in}} = \frac{(1-R)^{2}}{(1-R)^{2} \left[ 1 + \frac{4R}{(1-R)^{2}} \sin ^{2}(\Phi /2) \right] } = \frac{1}{1+F \sin ^{2}(\Phi /2)}
$$
Where I have used $F=4R /(1-R)^{2}$ in the last step.

---
b.
Use $R$ in the equation for simplicity,
$$
\frac{I_{T}}{I_\text{in}} = \left[ 1 + \frac{4R}{(1-R)^{2}} \sin ^{2}\left( \frac{\Phi}{2} \right) \right] ^{-1}
$$
- Plots have been done in Desmos
- Images saved in `~/Downloads/images`
---
c.
- Complete this question later
- Don't know what FSR is or how to calculate this quantity
# Question 1
---
a.
Consider a system composed of a single lens. The ray propagates some distance $s_\text{obj}$ from the object, goes through a length with focal length $f$, and propagates $s_\text{image}$ to form an image.
$$
\begin{bmatrix}
1 & s_\text{image} \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & s_\text{obj} \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
1-s_\text{image} /f & s_\text{obj} + s_\text{image} - s_\text{obj}s_\text{image} /f \\
-1 /f & 1-s_\text{obj} /f
\end{bmatrix}
$$
A conjugate plane is necessary to form an image, so $B=0$, implying:
$$
s_\text{obj} + s_\text{image} - \frac{s_\text{obj}s_\text{image}}{f} =0
$$
Re-arrange for $1 /f$:
$$
\frac{1}{s_\text{image}} + \frac{1}{s_\text{obj}} - \frac{1}{f} =0 \implies  \frac{1}{f} = \frac{1}{s_\text{obj}} + \frac{1}{s_\text{image}}
$$
As needed.

---
b.
From part A, the ABCD matrix representing the system is:
$$
\begin{bmatrix}
y_\text{image} \\
\alpha _\text{image}
\end{bmatrix} = \begin{bmatrix}
1-s_\text{image} /f & s_\text{obj} + s_\text{image} - s_\text{obj}s_\text{image} /f \\
-1 /f & 1-s_\text{obj} /f
\end{bmatrix} \begin{bmatrix}
y_\text{obj} \\
\alpha_\text{obj}
\end{bmatrix}
$$
Since, in this system, $B=0$, this simplifies into:
$$
\begin{bmatrix}
y_\text{image} \\
\alpha _\text{image}
\end{bmatrix} = \begin{bmatrix}
1-s_\text{image} /f & 0 \\
-1 /f & 1-s_\text{obj} /f
\end{bmatrix} \begin{bmatrix}
y_\text{obj} \\
\alpha_\text{obj}
\end{bmatrix} = \begin{bmatrix}
(1-s_\text{image} /f) y_\text{obj} \\
-y_\text{obj} /f + (1-s_\text{obj} /f)\alpha _\text{obj}
\end{bmatrix}
$$
The spatial magnification of the image is:
$$
\text{Magnification} = \frac{y_\text{image}}{y_\text{obj}} = 1-\frac{s_\text{image}}{f} = \frac{f-(f+x')}{f} = -\frac{x'}{f}
$$
As needed.

---
c.
Consider a system composed of a single lens. Light passes through the lens, and travels $f$ afterwards:
$$
\begin{bmatrix}
y_\text{final} \\
\alpha _\text{final}
\end{bmatrix} = \begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
y_\text{initial} \\
\alpha _\text{initial}
\end{bmatrix} = \begin{bmatrix}
f\alpha _\text{initial} \\
\alpha _\text{initial} - y_\text{initial} /f
\end{bmatrix}
$$
Therefore, at the focus of the lens,
$$
y_\text{final} = f\alpha _\text{initial}
$$
As needed.

---
d.
Consider a system with two identical lenses spaced by $2f$. An object is placed $f$ from the first lens, and light is allowed to propagate another $f$ distance before forming an image.
$$
\begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & 2f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}
$$
The spatial magnification is therefore,
$$
\text{Magnification}=-1
$$
Taken directly from the $A$ element of the matrix. So the resulting matrix has unity magnification, but is inverted.

---
e.
Consider the same system as in part D, but now place the object at $f+x$. If the light propagates some $f+x$ distance from the system afterwards, the resulting system matrix is:
$$
\begin{bmatrix}
1 & f+x \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & 2f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & f+x \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
-1 & -2x \\
0 & -1
\end{bmatrix}
$$
The spatial magnification of this image is therefore,
$$
\text{Magnification} = \frac{y_\text{image}}{y_\text{obj}} = \frac{-y_\text{obj}-2x\alpha _\text{obj}}{y_\text{obj}} = -1-2x \frac{\alpha _\text{obj}}{y_\text{obj}}
$$
The second term here manifests as the blur in the resulting image. Since $B\neq 0$, the input and output are not conjugate planes and so the resulting image is unclear. However, the size of the image remains the same.

- I don't even know if this is true
- If this is right, wouldn't my definition of magnification be wrong? Because now I'm just not taking into account this additional term
---
f.
The radius of curvature for a flat mirror is $R\to \infty$ and therefore the ABCD matrix for a flat mirror is the identity,
$$
\begin{bmatrix}
1 & 0 \\
-2 /R & 1
\end{bmatrix} \to  \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$
So this system reduces to a system that contains two identical lenses separated by $2f$. This is because the light passes through the lens, bounces off the mirror, and then has the opportunity to re-enter the lens.

This means that the properties from parts D and E hold for a cat's eye. In particular, it produces images of unity spatial magnification, and it is telecentric.

If an emitter is located $f$ in front of the cat's eye with $y_\text{initial}=0$ then,
$$
\begin{bmatrix}
y_\text{final} \\
\alpha _\text{final}
\end{bmatrix} = \begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & 2f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
1 & 0 \\
-1 /f & 1
\end{bmatrix} \begin{bmatrix}
1 & f \\
0 & 1
\end{bmatrix} \begin{bmatrix}
0 \\
\alpha _\text{initial}
\end{bmatrix} = \begin{bmatrix}
0 \\
-\alpha _\text{initial}
\end{bmatrix}
$$
Therefore $y_\text{final}=y_\text{initial}=0$ and the emitted light ray ends up back in the same position, but with $\alpha _\text{final}=\alpha _\text{initial}$
# Question 3
---
a.
$$
E_\text{tot} = E_\text{in} \exp(ikx-2\pi i\nu t) - \sqrt{ R }E_\text{in} \exp(ik(2L-x) - 2\pi i\nu t) + R E_\text{in} \exp(ik(2L+x)-2\pi i\nu t)
$$
$$
E_\text{tot} = E_\text{in} e^{ -2\pi i\nu t } \left[ e^{ ikx } - \sqrt{ R } e^{ ik(2L-x) } + R e^{ ik(2L+x) } - R^{3/2} e^{ ik(4L-x) } + \dots \right]
$$
Split into two series such that,
$$
E_\text{tot} = E_\text{right} + E_\text{left}
$$
$$
E_\text{right} = E_\text{in} \exp(ikx-2\pi i\nu t) \left[ 1 + R e^{ 2ikL } + R^{2} e^{ 4ikL } + \dots \right]
$$
$$
E_\text{left} = -\sqrt{ R }E_\text{in} \exp(ik(2L-x)-2\pi i\nu t) \left[ 1 + R e^{ 2ikL } + R^{2} e^{ 4ikL } + \dots \right]
$$
Use geometric series,
$$
E_\text{right} = \frac{E_\text{in} \exp(ikx-2\pi i\nu t)}{1-R e^{ 2ikL }}
$$
$$
E_\text{left} = - \frac{\sqrt{ R }E_\text{in} \exp(ik(2L-x)-2\pi i\nu t)}{1-R e^{ 2ikL }}
$$
The total series is therefore,
$$
E_\text{tot} = \frac{E_\text{in}e^{ -2\pi i\nu t }}{1-R e^{ 2ikL }} \left[ e^{ ikx } - \sqrt{ R } e^{ ik(2L-x) } \right]
$$
The intensity is therefore,
$$
I = \frac{I_\text{in}e^{ -4\pi i\nu t }}{\left| 1-R e^{ 2ikL } \right|^{2} } \left| e^{ ikx } - \sqrt{ R } e^{ ik(2L-x) } \right| ^{2}
$$
$$
\left| 1-R e^{ 2ikL } \right|^{2} = (1-R)^{2} + 4R \sin ^{2}(kL)
$$
$$
\left| e^{ ikx } - \sqrt{ R } e^{ ik(2L-x) } \right| ^{2} = 1+R - \sqrt{ R } (e^{ 2ik(x-L) } + e^{ -2ik(x-L) })
$$
Euler's identity,
$$
1+R - 2\sqrt{ R } \cos(2k(x-L))
$$
Trig identity $\cos(2x)=1-2\sin ^{2}x$
$$
1+R - 2\sqrt{ R } \left[ 1-2\sin ^{2}(k(x-L)) \right] = (1-\sqrt{ R })^{2} + 4\sqrt{ R } \sin ^{2}(k(x-L))
$$
Substitute back in to find,
$$
I = \frac{I_\text{in} \left[ (1-\sqrt{ R })^{2} + 4\sqrt{ R } \sin ^{2}(k(x-L)) \right] }{(1-R)^{2} + 4R \sin ^{2}(kL)}
$$
Factor out $(1-\sqrt{ R })^{2}$ to find,
$$
I_\text{in} \frac{(1-\sqrt{ R })^{2}}{(1-R)^{2}+4R\sin ^{2}(kL)} \left[ 1 + \frac{4\sqrt{ R }}{(1-\sqrt{ R })^{2}} \sin ^{2}(k(x-L)) \right]
$$
Therefore,
$$
A = \frac{(1-\sqrt{ R })^{2} }{(1-R)^{2}+4R\sin ^{2}(kL)} \qquad B = - \frac{4\sqrt{ R }}{(1-\sqrt{ R })^{2}} \qquad \phi(x) = k(x-L)
$$
- This is so messy and honestly probably filled with mistakes but I do not have time to correct them
---
b.
Interested in plotting:
$$
\frac{(1-\sqrt{ R })^{2}}{(1-R)^{2}+4R\sin ^{2}(kL)} \left[ 1 + \frac{4\sqrt{ R }}{(1-\sqrt{ R })^{2}} \sin ^{2}(kx-kL) \right]
$$
This plots look like this where I have arbitrarily chosen $kL=1$
![[Pasted image 20260302224752.png]]
$R=0.1$ is drawn in blue and $R=0.9$ is in green.

---
c.
There appears to always be a standing wave in the cavity, as suggested by $\sin ^{2}\left[ k(x-L) \right]$.

The energy density is defined to be,
$$
u_{\nu} = \frac{I_{\nu}}{c} \implies  \frac{u_\text{max} - u_\text{min}}{u_\text{max} + u_\text{min}} = \frac{I_\text{max}-I_\text{min}}{I_\text{max} + I_\text{min}}
$$
The minimum and maximum values of intensity are bounded by the values of $\sin ^{2}x$ which oscillates between 0 and 1.

The minimum and maximum intensities are therefore,
$$
I_\text{max} = I_\text{in} \frac{(1-\sqrt{ R })^{2}}{(1-R)^{2}} \left[ 1 + \frac{4\sqrt{ R }}{(1-\sqrt{ R })^{2}}  \right]
$$
$$
I_\text{min} = I_\text{in} \frac{(1-\sqrt{ R })^{2}}{(1-R)^{2}+4R}
$$
The visibility is therefore,
$$
\text{Visibility} = \frac{2\sqrt{ R }(R-\sqrt{ R }+1)}{-2R^{3/2}+R^{2} + 4R - 2 \sqrt{ R } + 1}
$$
---
d.
- I have no idea what to do for this question
