假设随机变量$X_1, X_2, ..., X_n$是独立同分布的正态变量, 其中$X_i \sim N(\mu,\sigma^2)$, 记
$$
\bar{X}=\frac1n \sum_{i=1}^{n}X_i,~S_n^2 = \frac1n\sum_{i=1}^{n}(X_i-\bar{X})^2
$$
有如下结论成立:
1. $\bar{X}$与$S_n^2$相互独立;
2. $\bar{X}\sim N(\mu,\frac{\sigma^2}n)$;
3. $\frac{nS_n^2}{\sigma^2} \sim \chi_{n-1}^2$.

#### 证明
设有正交矩阵
$$
\boldsymbol{A}=\begin{pmatrix}\frac1{\sqrt{n}}&\frac1{\sqrt{n}}&\frac1{\sqrt{n}}&\cdots&\frac1{\sqrt{n}}\\\frac1{\sqrt{2}}&\frac{-1}{\sqrt{2}}&0&\cdots&0\\\frac1{\sqrt{3\cdot2}}&\frac1{\sqrt{3\cdot2}}&\frac{-2}{\sqrt{3\cdot2}}&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\\frac1{\sqrt{n(n-1)}}&\frac1{\sqrt{n(n-1)}}&\frac1{\sqrt{n(n-1)}}&\cdots&\frac{-(n-1)}{\sqrt{n(n-1)}}\end{pmatrix}
$$
令$\mathbf{Y} = \mathbf{AX}$, 其中$\boldsymbol{X}=(X_1,X_2,\cdots,X_n)^\mathrm{T}$, $\boldsymbol{Y}=(Y_1,Y_2,\cdots,Y_n)^\mathrm{T}$. 根据多元统计分析的知识, 我们可以知道
$$
\boldsymbol{X}\sim N(\boldsymbol{\mu},\sigma^2\boldsymbol{I}_n),\quad\boldsymbol{Y}\sim N(\boldsymbol{A}\boldsymbol{\mu},\sigma^2\boldsymbol{I}_n).
$$
其中$\boldsymbol{\mu}=(\mu,\mu,\cdots,\mu)^\mathrm{T}\in\mathbb{R}^n,~\boldsymbol{I}_n$为$n$阶单位矩阵. 并且
$$
\begin{aligned}
Y_1&=\frac1{\sqrt{n}}\sum_{i=1}^nX_i\sim N(\sqrt{n}\mu,\sigma^2).\\
Y_i&\sim N(0,\sigma^2),\quad i=2,3,\cdots,n.
\end{aligned}
$$
且$Y_i$之间相互独立, 又有
$$
\begin{aligned}
nS_{n}^{2}& =\sum_{i=1}^n(X_i-\overline{X})^2=\sum_{i=1}^nX_i^2-n\overline{X}^2  \\
&=\sum_{i=1}^nY_i^2-Y_1^2=Y_2^2+Y_3^2+\cdots+Y_n^2.
\end{aligned}
$$

1. 注意到$\overline{X}=\frac1n\sum_{i=1}^nX_i=\frac1{\sqrt{n}}Y_1$, 可知$\overline{X}$与$S_n^2$相互独立; 
2. 由$Y_1=\frac1{\sqrt{n}}\sum_{i=1}^nX_i\sim N(\sqrt{n}\mu,\sigma^2)$, 得到$\overline{X}\sim N{\left(\mu,\frac{\sigma^2}n\right)}$;
3. $\frac{nS_n^2}{\sigma^2}=\sum_{i=2}^n\frac{Y_i^2}{\sigma^2}\sim\chi_{n-1}^2.$

参考文章[Fisher 引理](https://math.fandom.com/zh/wiki/Fisher_%E5%BC%95%E7%90%86).
