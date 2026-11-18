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

## Growing degree and a pair of model poles

Here is a precise obstruction to using only the Mellin-pole and density hypotheses above with varying degrees. Fix $\rho=\beta+i\gamma$, $1/2<\beta<1$ and $\gamma>0$, and define
$$
H_\rho(y)=-\int_2^y v^{\rho-1}\frac{dv}{\log v},
\qquad H=H_\rho+H_{\bar\rho}.
$$
In place of the prime error this real model gives $Q'_H(s)=2^{\rho-s}/(s-\rho)+2^{\bar\rho-s}/(s-\bar\rho)$ by integration by parts and differentiation for $\Re s>1$. It has unit residues at just one conjugate pair and satisfies the requisite sublinear pole count. The source $H$ is synthetic.

Let $d=d_j\to\infty$ with $d=o(j)$, and put $t=jL$. For either the single complex source or the real conjugate pair, the best respective complex or real $L^2([0,L])$ error of approximating $H_\rho(e^{t+u})$ or $H(e^{t+u})$ by a degree-$d$ polynomial satisfies
$$
\log(\text{best error})=\beta t-\log t-d\log d+O_\rho(d).
$$
Consequently any $d_j\sim c j/\log j$ with $c>(\beta-a)L$ makes the real model satisfy the fitted bound at exponent $a$ even with its pole at $\beta>a$. Conversely $d_j\log d_j=o(j)$ preserves the exponent $\beta$ for this model. Interactions between infinitely many prime-source frequencies remain outside this calculation.

For the proof, write $f_t(u)=H_\rho(e^{t+u})$, so $f'_t(u)=-e^{\rho(t+u)}/(t+u)$. Uniformly on $[0,L]$ and for $1\le n=o(t)$,
$$
f_t^{(n)}(u)=-\frac{e^{\rho(t+u)}\rho^{n-1}}{t+u}(1+O_\rho(n/t)).
$$
Indeed use $1/(t+u)=\int_0^\infty e^{-v(t+u)}dv$ and differentiate $n-1$ times. Replacing $(1-v/\rho)^{n-1}$ by 1 costs at most $\exp(nv/|\rho|)-1$ in absolute value, whose exponentially weighted integral is $O_\rho(n/t^2)$. Taylor approximation of order $d$ now yields the upper bound.

For the lower bound take the coefficient against the real orthonormal shifted Legendre polynomial $\sqrt{(2n+1)/L}\,P_n(2u/L-1)$, for $n=d+1$ or $d+2$. By Rodrigues' formula and $n$ integrations by parts this coefficient is
$$
\frac{\sqrt{(2n+1)/L}}{n!L^n}\int_0^L f_t^{(n)}(u)u^n(L-u)^n du.
$$
The mass of the weight is $L^{2n+1}(n!)^2/(2n+1)!$. Its normalized measure concentrates at $L/2$ as $n\to\infty$ (the rescaled beta distribution of parameters $n+1,n+1$ has variance $O(1/n)$). The coefficient is thus
$$
-\sqrt{(2n+1)/L}\,\frac{L^{n+1}n!}{(2n+1)!}
\frac{e^{\rho(t+L/2)}\rho^{n-1}}t(1+o(1)).
$$
For the real source take twice the real part. The phases of the leading terms at the two consecutive orders differ by $\arg\rho\notin\pi\mathbb Z$, so at least one has absolute cosine bounded below uniformly in $t,n$. The norm of any polynomial approximation error is at least the absolute value of that omitted coefficient. Stirling's formula yields the lower estimate, including the possible shift from $d+1$ to $d+2$ in its $O_\rho(d)$ term.
