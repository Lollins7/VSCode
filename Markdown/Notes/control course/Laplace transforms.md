#### 线性叠加性
$$
	\mathcal{L}\left[af\left(t\right)+bg\left(t\right)\right]=
	a\mathcal{L}\left[f\left(t\right)\right]+b\mathcal{L}\left[g\left(t\right)\right]
$$

#### 微分性质
$$
\mathcal{L}\left[f^{(n)}\left(t\right)\right]=
	s^{n}\mathcal{L}\left[f\left(t\right)\right]-s^{n-1}f\left(0\right)-s^{n-2}f^{\prime}\left(0\right)-\ldots-f^{(n-1)}\left(0\right)
$$

#### 积分性质
$$
\mathcal{L}\left[\underbrace{\int_0^tdt\int_0^tdt\ldots\int_0^t}_{n\text{重}} f \left ( t \right ) dt \right ]
	= \frac 1 {s^n}\mathcal{L}\left[f\left(t\right)\right]
$$

#### 相似性质
$$
\mathcal{L}[f(at)]=\frac1aF(\frac sa)
$$

#### 位移性质
$$
\mathcal{L}[e^{at}f(t)]=F(s-a)
$$



#### 常见变化
$$
\begin{aligned}
		 & \mathcal{L}\left[1\right]=\frac1s                                                      \\
		 & \mathcal{L}\left[e^{at}\right]=\frac{1}{s-a}                                           \\
		 & \mathcal{L}\left[t^{n}e^{at}\right]=\frac{\Gamma(n+1)}{\left(s-a\right)^{n+1}}\{n>-1\} \\
		 & \mathcal{L}\left[t^n\right]=\frac{\Gamma(n+1)}{s^{n+1}}\{n>-1\}                        \\
		 & \mathcal{L}\left[\sin at\right]=\frac{a}{s^2+a^2}                                      \\
		 & \mathcal{L}\left[\cos at\right]=\frac{s}{s^{2}+a^{2}}                                  \\
		 & \mathcal{L}\left[\sin\text{h}at\right]=\frac{a}{s^2-a^2}                               \\
		 & \mathcal{L}\left[\cos\text{h}at\right]=\frac{s}{s^2-a^2}                               \\
		 & \mathcal{L}\left[t\sin at\right]=\frac{2as}{\left(s^2+a^2\right)^2}                    \\
		 & \mathcal{L}\left[t\cos at\right]=\frac{s^{2}-a^{2}}{\left(s^{2}+a^{2}\right)^{2}}
	\end{aligned}
$$