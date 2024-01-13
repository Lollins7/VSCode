#### 周期：$T = 2L$
$f(t) = f(t + 2L)$，换元，令$x = \frac{\pi}{L}t$，得到
$$
f(\frac{L}{\pi}x) = f(\frac{L}{\pi}(x + 2\pi)) = g(x)
$$
此时$T = 2\pi$，$g(x) + g(x + 2\pi)$。
推导，得
$$
f(t) = \frac{a_0}2 + \sum_{n = 1}^{\infty}[a_n\cos(\frac{n\pi}L t) + b_n \sin(\frac{n\pi}L t)]
$$
其中$a_0 = \frac{1}{L}\int_{-\pi}^{\pi}f(t)\mathrm{dt}$, $a_n = \frac{1}{L}\int_{-\pi}^{\pi}f(t)\cos(\frac{n\pi}L t)\mathrm{dt}$, $b_n = \frac{1}{L}\int_{-\pi}^{\pi}f(x)\sin(\frac{n\pi}L t)\mathrm{dt}$。

#### 实际工程中
$t$从$0$开始，$T = 2L$，$\omega = \frac{2\pi}{2L} = \frac{\pi}{L}$。
$$
f(t) = \frac{a_0}2 + \sum_{n = 1}^{\infty}[a_n\cos(n\omega t) + b_n \sin(n\omega t)]
$$
其中$a_0 = \frac{2}{T}\int_{-\pi}^{\pi}f(t)\mathrm{dt}$, $a_n = \frac{2}{T}\int_{-\pi}^{\pi}f(t)\cos(n\omega t)\mathrm{dt}$, $b_n = \frac{2}{T}\int_{-\pi}^{\pi}f(x)\sin(n\omega t)\mathrm{dt}$。