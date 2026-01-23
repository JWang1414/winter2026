$$
y(x) = y_{\mu} e^{ -\frac{(x-\mu)^{2}}{2\sigma^{2}} } \qquad y(x) = \frac{y_{\mu}}{x\sigma} e^{ -\frac{(\ln x-\mu)^{2}}{2\sigma^{2}} } \qquad y(x) = y_{\mu} e^{ -\frac{\lvert x-\mu \rvert }{\sigma} }
$$
The mean value determine from raw measurements was computing using the mean value formula:
$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_{i} = \frac{1}{2} (72.86 + 72.42) = 72.64
$$
Where $x_{i}$ is a single data point. Based on this mean, the standard deviation can be computed like so:
$$
\sigma = \sqrt{ \frac{1}{n-1} \left( \sum^n_{i=1}(x_{i}-\bar{x})^2 \right) } = \sqrt{ \frac{1}{2-1} \left( (72.86-72.64)^{2} + (72.42-72.64)^{2}  \right) } \approx 0.311
$$
And the standard error is determined by dividing this result with the square root of the number of trials:
$$
u(\bar{x}) = \frac{\sigma}{\sqrt{ n }} \approx \frac{0.311}{\sqrt{ 2 }} \approx 0.22
$$
The 26 unit calibration square was measured to have side lengths $(121\pm 2)$ mm. The fractional error for this quantity is approximately 0.016. The conversion ratio is therefore:
$$
\frac{\text{Units}}{\text{Millimetres}} \approx \frac{26}{121} \approx 0.216
$$
And the uncertainty, carried from the fractional uncertainty is roughly,
$$
0.216 \times 0.016 \approx 0.003
$$
The conversion from raw measurements is done like so:
$$
\text{Millimetres} \times \text{Scale Factor} \times \text{Conversion Ratio} = \text{Units}
$$
The scale factor is a constant without any uncertainty, and so the uncertainty is propagated as a product between two values $x$ and $y$ with some uncertainty $u(x)$ and $u(y)$.
$$
u(f) = sf\sqrt{ \left( \frac{u(x)}{x} \right)^2 + \left( \frac{u(y)}{y} \right)^2 } \approx 1\times 15.66 \sqrt{ \left( \frac{0.22}{72.64} \right)^{2} + \left( \frac{0.003}{0.216} \right)^{2} } \approx 0.25
$$
Where $f$ is the final, average measurement expressed in units.