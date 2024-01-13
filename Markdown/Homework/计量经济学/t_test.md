#! https://zhuanlan.zhihu.com/p/629014519
不显示的第一行

这学期学习的计量经济学，最近整理一个关于多元线性回归模型的变量显著性检验（t检验）的证明。废话不多说，直接开始吧：

记多元线性回归模型的方程为：$Y = X\beta + \mu$，其中$\mu$为随机干扰项，根据假设，其满足$\mu|X \thicksim N(0,\sigma^{2}I_{n})$，$\hat\beta|X \thicksim N(\beta,\sigma^2 (X^T X)^{-1})$，这里令$C=(X^T X)^{-1}$，$c_{ij}$表示矩阵$C$中第$i$行第$j$列的元素($1 \leq i,j \leq k+1$)。
> 给出$\hat\beta|X \thicksim N(\beta,\sigma^2 (X^T X)^{-1})$的证明：
> $$\begin{aligned}E(\hat\beta|X) &= E((X^TX)^{-1}X^T Y|X)\\
&=E((X^TX)^{-1}X^T (X\beta + \mu)|X) \\
&=E(\beta + (X^TX)^{-1}X^T \mu|X)\\
&= \beta
\end{aligned}\\
\begin{aligned}Var(\hat\beta|X) &= E((\hat\beta-\beta)(\hat\beta-\beta)^T|X)\\
&=E(((X^TX)^{-1}X^T \mu)((X^TX)^{-1}X^T \mu)^T|X) \\
&=((X^TX)^{-1}X^T E(\mu \mu^T|X)(X^TX)^{-1}X^T \mu)^T\\
&= \sigma^2(X^T X)^{-1}\\
\end{aligned}\\
其中Var(\mu|X)=E(\mu \mu^T|X)-E(\mu)E(\mu)^T= E(\mu \mu^T|X)=\sigma^2I_n
$$

$$
Y=\left( \begin{array}{c}
	Y_1\\
	Y_2\\
	\vdots\\
	Y_n\\
\end{array} \right) ,\,\,
\beta =\left( \begin{array}{c}
	\beta _1\\
	\beta _2\\
	\vdots\\
	\beta _n\\
\end{array} \right) ,\,\,
X=\left( \begin{matrix}
	1&		X_{11}&		\cdots&		X_{1k}\\
	1&		X_{21}&		\cdots&		X_{2k}\\
	\vdots&		\cdots&		\ddots&		\vdots\\
	1&		X_{n1}&		\cdots&		X_{nk}\\
\end{matrix} \right) 
$$

-------

(懒了，后面的内容关于条件分布的格式省了)

------
$e$为残差项，另有$Y=X\hat{\beta}+e，\hat{Y}=X\hat{\beta}$.

对于$\beta_{j} \thicksim N(\beta_j,\sigma^2c_{jj})$，要证明：
$$
t=\frac{\hat\beta_j - \beta_j}{S_{\hat\beta_j}}=\frac{\hat\beta_j - \beta_j}{\sqrt{c_{jj} \frac{e^T e}{n-k-1}}} \thicksim t(n-k-1)
$$

易知$\frac{\hat\beta_j - \beta_j}{\sigma\sqrt{c_{jj}}}\thicksim N(0,1)$，故要证明$\frac{e^T e}{\sigma^2}\thicksim \chi^2(n-k-1)$。

 
为了证明$\frac{e^T e}{\sigma^2}\thicksim \chi^2(n-k-1)$，我们需要知道以下这些东西：
> 先证明$e=M\mu，其中P = X(X^T X)^{-1}X^T，M=I_n - P$
> 证明：$$\begin{aligned}e &= Y - X\hat\beta\\
&=Y - X(\beta + (X^TX)^{-1}X^T\mu)\\
&=\mu - X(X^TX)^{-1}X^T\mu\\
&=(I_n - P)\mu\\
&=M\mu 
\end{aligned}$$

>对于上面的$M$与$P$，我们可以发现其为对称幂等矩阵，幂等矩阵的一些性质，大家可以参考[这篇文章](https://zhuanlan.zhihu.com/p/457417086)

> 在证明$tr(P)=k+1$
> 证明：根据$SVD$定理，可以得到$X=U_{n\times (k+1)}\Lambda_{(k+1)\times (k+1)} V_{(k+1)\times (k+1)}^T$，$U,V$为正交矩阵，$U^TU=I_{k+1},V^TV=I_{k+1}$，$UU^T=$$
\left( \begin{matrix}
	I_{k+1}&	0	\\
	0&	0	\\
\end{matrix} \right) 
$$
$
> $$
\begin{aligned}
P &= X(X^T X)^{-1}X^T\\
&= U\Lambda V^T((U\Lambda V^T)^TU\Lambda V^T)^{-1}(U\Lambda V^T)^T\\
&=UU^T\\
&=\left( \begin{matrix}
	I_{k+1}&	0	\\
	0&	0	\\
\end{matrix} \right) 
\end{aligned}$$
故可以得到$tr(P)=k+1$
$
\Longrightarrow tr(M) = tr(I_{n}) - tr(P) = n - k -1
$

> Quadratic Form of Normal Random Variables：若$X\thicksim N_{n}(0,I_n)，Q_{n\times n}$为对称幂等矩阵，$rank(Q) = q$，则$X^TQX\thicksim \chi^{2}(q)$
> 证明：$P$为正交矩阵，有$Q=P\Lambda P^T$，$\Lambda = \left( \begin{matrix}
	I_{q}&	0	\\
	0&	0	\\
\end{matrix} \right) $，
令$Y=P^TX$，$Y\thicksim N_{n}(0,I_n)$
> $$\begin{aligned}
X^TQX &= X^TP\Lambda P^TX\\
&=Y^T\Lambda Y
\end{aligned}$$
$Y^T\Lambda Y \thicksim \chi^2(q)$，故$X^TQX\thicksim \chi^2(q)$

OK，我们现在可以来证明$\frac{e^T e}{\sigma^2}\thicksim \chi^2(n-k-1)$：
首先，对于对称幂等矩阵$M$，有
$$
rank(M)=tr(M)=n-k-1
$$
另有，
$$
\frac{e}{\sigma}\thicksim N_{n}(0,I_n)
$$
最后，
$$
\frac{e^T e}{\sigma^2}=(\frac{e}{\sigma})^TM(\frac{e}{\sigma})\thicksim \chi^2(n-k-1)
$$
证毕！

----


