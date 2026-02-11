# General definitions related to Fourier series
Recall we wanted to break a square wave into a summation of sines and cosines with Fourier series. Something like:
$$
F(t) = \frac{A_{0}}{2} \sum_{n=1}^{\infty} [A_{n} \cos(\omega_{n}t) + B_{n} \sin(\omega_{n}t)] \qquad \omega_{n} = \frac{2\pi n}{T}
$$
One can prove that the Fourier series for some function always exists, and is unique.

Recall that we solve for the coefficients with:
$$
A_{n} = \frac{2}{T} \int_{0}^{T} F(t)\cos(\omega_{n}t) \, dt \qquad B_{n} = \frac{2}{T} \int_{0}^{T} F(t)\sin(\omega_{n}t) \, dt
$$
- The interval can be any interval $T$ in length. $-T /2$ to $T /2$ also works.
# Orthogonality of Fourier modes
Define the inner product,
$$
f\cdot g = \frac{2}{T} \int_{-T /2}^{T /2} f(t)g(t) \, dt
$$
We have used the definition including the normalization factor $2 /T$. Which helps to keep the sine and cosine functions neat. Recall the orthogonality of the sine and cosine functions:
$$
\begin{align}
\sin(\omega_{m}t) \cdot \sin(\omega_{n}t) &= \delta_{mn} \\
\cos(\omega_{m}t) \cdot \cos(\omega_{n}t) &= \delta_{mn} \\
\sin(\omega_{m}t) \cdot \cos(\omega_{n}t) &= 0
\end{align}
$$
Where $\delta_{mn}$ is the familiar Kronecker delta,
$$
\delta_{mn} = \begin{cases}
1 & m=n \\
0 & \text{otherwise}
\end{cases}
$$
![[Pasted image 20260211160043.png]]
A graphical visualization of the orthogonality relations between two sine functions
# Simplifications related to function parity
For odd functions, $F(-t)=-F(t)$
$$
A_{n}=0 \qquad F(t) = \sum_{n=1}^{\infty} B_{n}\sin(\omega_{n}t)
$$
Because cosine is an even function. Furthermore, since the product of two odd numbers is always even, we need only compute the coefficient over half the interval, and multiply the result by 2,
$$
B_{n} = \frac{4}{T} \int_{0}^{T /2} F(t)\sin(\omega_{n}t) \, dt
$$
For even functions, $F(-t)=F(t)$,
$$
B_{n} = 0 \qquad F(t) = \frac{A_{0}}{2} + \sum_{n=1}^{\infty} A_{n} \cos(\omega_{n}t)
$$
And,
$$
A_{n} = \frac{4}{T} \int_{0}^{T /2} F(t) \cos(\omega_{n}t) \, dt
$$
- The rest of the lecture is composed of examples I should already be familiar with
