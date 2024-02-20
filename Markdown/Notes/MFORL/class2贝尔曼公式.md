#### Some notations

Consider the following **single-step** process:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}
$$

- $t,t+1$: discrete time instances(时刻)
- $S_t$: state at time $t$
- $A_t$: the action taken at state $S_t$
- $R_{t+1}$: the reward obtained after taking $A_t$
- $S_{t+1}$: the state transited to after taking $A_t$

Note that $S_t, A_t, R_{t+1}$ are all *random variable*.

This step is governed by the following probability distributions:

- $S_t\rightarrow A_t$, is governed by $\pi(A_t=a|S_t=s)$
- $S_t, A_t\rightarrow R_{t+1}$ is governed by $\begin{aligned}p(R_{t+1}=r|S_t=s,A_t=a)\end{aligned}$
- $S_t, A_t\rightarrow S_{t+1}$ is governed by $\begin{aligned}p(S_{t+1}=s'|S_t=s,A_t=a)\end{aligned}$



Consider the following **multi-step** trajectory:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}\xrightarrow{A_{t+1}}R_{t+2},S_{t+2}\xrightarrow{A_{t+2}}R_{t+3},\ldots
$$
The **discounted return** is 
$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\ldots
$$

- $\gamma \in [0,1)$ is a discount rate
- $G_t$ is also a random variable since $R_{t+1},R_{t+2},...$ are random variable

#### State value

The expectation(or called expected value or mean) of $G_t$, is defined as the *state-value* function or simply *state value*:
$$
v_\pi(s)=\mathbb{E}[G_t|S_t=s]
$$
Remarks:

- It is a function of $s$. It is a conditional expectation with the condition that the state starts from $s$.
- It is based on the policy $\pi$. For a different policy, the state value may be different.
- It represents the "value" of a state. If the state value is greater, then the policy is better because greater cumulative rewards can be obtained.

#### Deriving the Bellman equation

Consider a random trajectory:
$$
S_t\xrightarrow{A_t}R_{t+1},S_{t+1}\xrightarrow{A_{t+1}}R_{t+2},S_{t+2}\xrightarrow{A_{t+2}}R_{t+3},\ldots
$$
The return $G_t$ can be written as 
$$
\begin{aligned}
G_{t}& \begin{aligned}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\ldots,\end{aligned}  \\
&=R_{t+1}+\gamma(R_{t+2}+\gamma R_{t+3}+\ldots), \\
&=R_{t+1}+\gamma G_{t+1},
\end{aligned}
$$
Then, it follows from the definition of the state value that
$$
\begin{aligned}
v_{\pi}(s)& \begin{aligned}=\mathbb{E}[G_t|S_t=s]\end{aligned}  \\
&=\mathbb{E}[R_{t+1}+\gamma G_{t+1}|S_{t}=s] \\
&=\mathbb{E}[R_{t+1}|S_t=s]+\gamma\mathbb{E}[G_{t+1}|S_t=s]
\end{aligned}
$$
Therefore, we have
$$
\begin{aligned}
\color{red}{v_\pi(s)}& \begin{aligned}=\mathbb{E}[R_{t+1}|S_{t}=s]+\gamma\mathbb{E}[G_{t+1}|S_{t}=s],\end{aligned}  \\
&\begin{aligned}=\underbrace{\sum_a\pi(a|s)\sum_rp(r|s,a)r}_{\text{mean of immediate rewards}}+\underbrace{\gamma\sum_a\pi(a|s)\sum_{s'}p(s'|s,a)v_\pi(s'),}_{\text{mean of future rewards}}\end{aligned} \\
&\begin{aligned}=\sum_a\pi(a|s)\left[\sum_rp(r|s,a)r+\gamma\sum_{s'}p(s'|s,a)v_\pi(s')\right],\quad\forall s\in\mathcal{S}.\end{aligned}
\end{aligned}
$$
Highlights:

- The above equation is called the *Bellman equation*, which characterizes the relationship among the state-value functions of different states.
- It consists of two terms: the immediate reward term and the future reward term.
- A set of equations: every state has an equation like this!!!

#### Matrix-vector form of the Bellman equation

























