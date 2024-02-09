令周期$T \rightarrow \infty$，可以得到
$$
f(t) = \frac1{2\pi}\int_{-\infty}^{\infty}e^{i\omega t}(\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\mathrm{dt})\mathrm{d\omega}
$$
其中，我们称
$$
F(\omega) = \int_{-\infty}^{\infty}f(t)e^{-i\omega t}\mathrm{dt}
$$
为**傅里叶变换**。
同时，我们称
$$
f(t) = \frac1{2\pi}\int_{-\infty}^{\infty}e^{i\omega t}F(\omega)\mathrm{d\omega}
$$
为**傅里叶变换的逆变换**。
