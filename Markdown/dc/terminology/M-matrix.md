若$A$为$M-matrix$，则其满足：

1. 所有的主对角线元素（即$A$的第$i$行第$i$列元素）都是非负的：$A(i,i)≥0$，对于所有的$i$。
2. 所有的非主对角线元素（即$A$的第$i$行第$j$列元素，其中$i≠j$）都是负的或零：$A(i,j)≤0$，对于所有的$i≠j$。
3. $A$的每一列的元素和都是非负的：$\sum_{i}A(i,j)≥0$或每一行的元素和都是非负的：$\sum_{j}A(i,j)≥0$，只要满足其中之一就好了。



**定义**：任意一个矩阵$A=sI-B$，若$B\geq 0,s\geq \rho(B)$，则称$A$为$M-matrix$。



**定理**：对于A为$M-matrix$，P是一个正定矩阵，那么
$$
Q = AP+PA^T
$$
为一个正定矩阵。

**注**：其实在这个定理中，$-A$为一个Hurwitz矩阵。