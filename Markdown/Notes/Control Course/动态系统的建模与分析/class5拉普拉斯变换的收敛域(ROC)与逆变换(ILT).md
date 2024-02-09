## 收敛域(Region of Convergence)
对于函数$f(t) = e^{-at}$，
$$
\mathcal{L}[f(t)] = \frac1{s+a} = \int_{0}^{\infty}e^{-(s+a)t}\mathrm{dt} = \int_{0}^{\infty}e^{-(\sigma+a)t}e^{-j\omega t}\mathrm{dt}
$$
为了保证积分收敛，$-(\sigma + a) < 0 \Rightarrow \sigma > -a$。

## 微分方程
描述动态世界。
常系数线性微分方程$\Leftrightarrow$线性时不变系统。

## 用Laplace Transform求解微分方程
1. 从$t \rightarrow s$；
2. 求解代数方程；
3. 从从$s \rightarrow t$。

#### 例1
$$
F(s) = \frac{-s+5}{s^2+5s+4} = \frac{-3}{s+4} + \frac{2}{s+1}
$$
$$
\mathcal{L}^{-1}[F(s)] = -3e^{-4t} + 2e^{-t}
$$