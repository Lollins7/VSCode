欧拉公式：
$$
e^{i\theta} = \cos(\theta) + i \sin(\theta)
$$
由此可以推出
$$
\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}2
$$
$$
\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}
$$
此时的傅里叶展开式为
$$
f(t) = \sum_{n = -\infty}^{\infty} C_n e^{in\omega t}
$$
其中
$$
C_n = \frac1T\int_{0}^{T}f(t) e^{-in\omega t} \mathrm{dt}
$$
