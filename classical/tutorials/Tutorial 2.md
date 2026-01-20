# Question 1
---
$$
z_{2} = \left( 1+\frac{3}{1-i} \right)^{2}
$$
Not very exciting.
$$
z_{2} = 4 + \frac{15}{2}i
$$
Convert to polar:
$$
\theta = \arctan\left( \frac{15 /2}{4} \right) = \arctan \left( \frac{15}{8} \right)
$$
$$
\lvert z_{2} \rvert = \frac{289}{4}
$$
- Oops I forgot to square root this afterwards
So polar form is:
$$
z_{2} = \frac{289}{4} \exp \left[ i\arctan\left( \frac{15}{8} \right) \right]
$$
- This is disgusting maybe I did it wrong lol?
---
Prove that:
$$
\cos(2\theta) = \cos ^{2}\theta - \sin ^{2}\theta
$$
$$
\cos(2\theta) = \frac{e^{ 2i\theta } + e^{ -2i\theta }}{2}
$$
$$
\cos ^{2}\theta - \sin ^{2}\theta = \left( \frac{e^{ i\theta }+e^{ -i\theta }}{2} \right)^{2} - \left( \frac{e^{ i\theta }-e^{ -i\theta }}{2} \right)^{2}
$$
- This sucks and it's just algebra
# Question 2
---
$$
\dot{x} = -A\omega \sin(\omega t) + B\omega \cos(\omega t)
$$
$$
x(0) = A=x_{0}
$$
$$
\dot{x}(0) = B\omega=v_{0} \implies  B = \frac{v_{0}}{\omega}
$$
---
$$
\dot{x} = -C\omega \sin(\omega t+\phi)
$$
$$
x(0) = C \cos \phi = x_{0} \implies  C = \frac{x_{0}}{\cos \phi}
$$
$$
\dot{x}(0) = -C\omega \sin(\phi) = v_{0} \implies  C = -\frac{v_{0}}{\omega \sin \phi}
$$
$$
\frac{x_{0}}{\cos \phi} = -\frac{v_{0}}{\omega \sin \phi} \implies  \tan \phi = -\frac{v_{0}}{\omega x_{0}}
$$
---
$$
\dot{x} = E(i\omega)e^{ i\omega t } + F(-i\omega)e^{ -i\omega t } = i\omega (Ee^{ i\omega t } - Fe^{ -i\omega t })
$$
$$
x(0) = E+F = x_{0}
$$
$$
\dot{x}(0) = i\omega(E-F) = v_{0}
$$
System of equations:
$$
\begin{align}
E+F & = x_{0} \\
E-F & = \frac{v_{0}}{i\omega}
\end{align}
$$
$$
2E = x_{0} + \frac{v_{0}}{i\omega} \implies  E = \frac{1}{2} \left( x_{0} - \frac{iv_{0}}{\omega} \right)
$$
$$
2F = x_{0} - \frac{v_{0}}{i\omega} \implies  F = \frac{1}{2} \left( x_{0}+\frac{iv_{0}}{\omega} \right)
$$
# Question 3
---
1.
$$
\dot{z} = i\omega z \implies  z = c_{1}e^{ i\omega t }
$$
$$
z(0) = c_{1} e^{ 0 } = c_{1} = z_{0}
$$
Solution is,
$$
z(t) = z_{0} e^{ i\omega t }
$$
---
2.
- Forward Euler method
- Radius increases and it curves outwards

---
3.
- Backward Euler method
- If you do a Taylor series analysis, you will find that the forward and backward Euler methods will approach each other
- Radius reduces and it curves inwards
