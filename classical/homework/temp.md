e.
Drag and gravity now point in opposite directions
$$
m\ddot{x} = mg - cv^{2}
$$
Re-arrange to find an expression for $\dot{v}$:
$$
\dot{v} = g\left( 1 - \left( \frac{v}{v_\text{ter}} \right)^{2} \right)
$$
Align the direction so that $g$ is negative
$$
\dot{v} = -g \left[ 1-\left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Apply the chain rule:
$$
\frac{dv}{dt} = \frac{dv}{dy} \frac{dy}{dt} = v \frac{dv}{dy} = -g \left[ 1-\left( \frac{v}{v_\text{ter}} \right)^{2} \right]
$$
Integrate both sides:
$$
\int_{v_{0}}^{v} \frac{v}{1-(v /v_\text{ter})^{2}} \, dv = -g \int dy
$$
The result is:
$$
-\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = -gy
$$
After some algebra:
$$
\ln \left| v_\text{ter}^{2}-v^{2} \right| = \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|
$$
Simplify the absolute value by making the assumption that $v^{2}\leq v_\text{ter}^{2}$:
$$
v^{2} - v_\text{ter}^{2} = \exp \left[ \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right| \right]
$$
Solve for $v$:
$$
v = \sqrt{ v_\text{ter}^{2} + \exp \left[ \frac{2gy}{v_\text{ter}^{2}} + \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right| \right] }
$$
---
f.
Instead of using the final equation, I will instead substitute $y_\text{max}$ into this midpoint:
$$
\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = gy
$$
Which yields:
$$
\frac{v_\text{ter}^{2}}{2} (\ln \left| v_\text{ter}^{2}-v^{2} \right| - \ln \left| v_\text{ter}^{2}-v_{0}^{2} \right|  ) = -\frac{v_\text{ter}^{2}}{2} \ln\left( \frac{v_\text{ter}^{2}+v_{0}^{2}}{v_\text{ter}^{2}} \right)
$$
Apply the properties of logarithms to simplify the expression into:
$$
\ln\left( \frac{\left| v_\text{ter}^{2}-v^{2} \right| }{\left| v_\text{ter}^{2}-v_{0}^{2} \right| } \right) = \ln \left( \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}} \right)
$$
If I assume that $v_{0}<v_\text{ter}$ and $v<v_\text{ter}$ I obtain:
$$
\frac{v^{2}-v_\text{ter}^{2}}{v_{0}^{2}-v_\text{ter}^{2}} = \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
Re-arrange:
$$
v^{2} = \frac{v_\text{ter}^{2}}{v_\text{ter}^{2}+v_{0}^{2}} (v_{0}^{2}-v_\text{ter}^{2}) + v_\text{ter}^{2} = \frac{2v_\text{ter}^{2}v_{0}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
Aligning the directions, the velocity when the ball hits the ground is,
$$
v_{g} = - \frac{\sqrt{ 2 }v_\text{ter}^{2}v_{0}^{2}}{v_\text{ter}^{2}+v_{0}^{2}}
$$
- This is a factor $\sqrt{ 2 }$ off the correct answer. Not sure why