# Removing finitely many trend coefficients per dyadic block

**Status.** Proposed extension of the [dyadic prime-error criterion](causal-octave-nov18.md). Its arithmetic input is the classical zero-density estimate $N(\sigma,T)=o(T)$ for every fixed $\sigma>1/2$. The conclusion remains a criterion.

Fix $a\in(1/2,1)$, a nonnegative integer $d$, and $L=\log 2$. Write $E(y)=\pi(y)-\int_2^y dt/\log t$. Suppose that for each integer $j\ge1$ there is a real polynomial $P_j$ of degree at most $d$ with
$$
\int_0^L |E(2^j e^u)-P_j(u)|^2\,du\le B^2 2^{2aj}
$$
for one finite $B$. Then $\zeta$ has no zero in $\Re s>a$. Under RH this bound holds for every such $a$ with $P_j=0$, so the hierarchy over $a$ characterizes RH for every fixed $d$.

**Proof.** On $\Re s>1$, define $Q(s)=s\int_2^\infty E(y)y^{-s}dy/y$ and define $R$ using the residual after subtracting the fitted polynomial on each block. The stated bound gives local uniform absolute convergence of the residual integral in $\Re s>a$. Norm equivalence in the fixed finite-dimensional polynomial space on $[0,L]$ and $E(2^j e^u)=O(2^j)$ give $|P_j^{(k)}(0)|+|P_j^{(k)}(L)|=O_d(2^j)$ for $0\le k\le d$. Repeated integration by parts gives
$$
s^d(Q-R)=\sum_{k=0}^d s^{d-k}\sum_{j\ge1}2^{-js}
  \left(P_j^{(k)}(0)-2^{-s}P_j^{(k)}(L)\right).
$$
Each inner series is holomorphic on $\Re s>1$, with period $ih$ for $h=2\pi/L$. Let $\Delta H(s)=H(s+ih)-H(s)$. Then $\Delta^{d+1}[s^d(Q-R)]=0$ there.

Put $V=(d/ds)^{d+1}(s^d Q)$. Its continuation is meromorphic in $\Re s>1/2$: the product rule uses derivatives $Q^{(k)}$ with $k\ge1$, and the earlier criterion gives the meromorphic expression for $Q'$, with residues equal to zeta-zero multiplicities. Moreover $\Delta^{d+1}V$ continues holomorphically into $\Re s>a$ by the identity with $(d/ds)^{d+1}\Delta^{d+1}(s^dR)$ there.

Near a zero $\rho$, a local primitive $Q$ has singular part $m\log(s-\rho)$ for $m$ its multiplicity. In differentiating $s^d m\log(s-\rho)$ a total of $d+1$ times, the only contribution to the residue comes from the monomial $(s-\rho)^d m\log(s-\rho)$, which gives $d!m/(s-\rho)$. Fix any $s_0$ of real part greater than $a$. Let $m_n$ be the zero multiplicity at $s_0+inh$ for $n\in\mathbb Z$, and use zero at regular points. Taking residues gives $\Delta^{d+1}m_n=0$ for all $n$, with the ordinary forward difference on integers. The sequence is polynomial of degree at most $d$. If nonzero anywhere, it is nonzero at all but finitely many positive indices, contradicting the quoted zero-density theorem at $\sigma=\Re s_0$ (the zero-free region $\Re s\ge1$ is classical). Hence no such zero exists.

The constants implicit in the proof depend on $d$. No conclusion is asserted for degree growing with the octave index or for approximation on only part of each octave.
