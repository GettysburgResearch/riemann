# Independent check of the fixed-prefix moment constant

Take equation (80) of [rstation_48_v2](../sources/ratio62_q1_priority/rstation_48_v2.md) as the finite-dimensional starting point. Write $P_k$ for the Legendre polynomial with $P_k(1)=1$, $\delta=1-b$, and $a=(1+b)/\delta$. For $m\ge1$,
$$
\boxed{c_m(b)=m^2+2\int_1^{a}[P'_{m-1}(x)]^2\,dx.}
$$
The integral is polynomial in $a-1$. An explicit sum follows by setting $n=m-1$, $z=a-1=2b/\delta$, and $A_j=2^{-j}\binom nj\binom{n+j}j$ to obtain
$$
c_m(b)=m^2+2\sum_{i,j=1}^n
  \frac{ij A_i A_j}{i+j-1}z^{i+j-1}.
$$
The sum is empty when $m=1$.

## Derivation

Let $p_b$ be the Riesz representer on real polynomials of degree below $m$ for
$\ell_b(q)=-q(0)+m\int_0^b q$, with inner product $\int_b^1 pq$.
The monomial Gram matrix is $M$ and the functional vector is $v$, so completing the square yields
$$
c_m(b)=\max_p\left[m^2b+2\ell_b(p)-\int_b^1p(t)^2\,dt\right].
$$
The maximizing coefficient vector is $M^{-1}v$ and depends smoothly on $b$. Differentiation at stationarity gives $c_m'(b)=(p_b(b)+m)^2$.

The reproducing kernel on $[b,1]$ is
$$
K_b(s,t)=\frac1\delta\sum_{k=0}^{m-1}(2k+1)P_k(x(s))P_k(x(t)),
\qquad x(t)=\frac{2t-1-b}{\delta}.
$$
Consequently, if $D_k=-P_k(a)+(m\delta/2)\int_1^a P_k(x)\,dx$, orthogonality and parity give
$$
c_m(b)=m^2b+\frac1\delta\sum_{k=0}^{m-1}(2k+1)D_k^2,
\qquad p_b(b)=\frac1\delta\sum_{k=0}^{m-1}(2k+1)D_k .
$$
First use $\sum_{k<m}(2k+1)P_k=P'_m+P'_{m-1}$, which telescopes from $(2k+1)P_k=P'_{k+1}-P'_{k-1}$ for $k\ge1$ and $P'_1=P_0$. Since $P_j(1)=1$, the integrated sum yields
$$
\delta p_b(b)=-(P'_m+P'_{m-1})(a)+\frac{m\delta}{2}(P_m+P_{m-1}-2)(a).
$$
The identity $(x+1)(P'_m-P'_{m-1})=m(P_m+P_{m-1})$ follows by subtracting the adjacent Legendre differentiation recurrences and eliminating $P_{m-2}$ with the three-term recurrence. For $m=1$ it follows from $P_0=1$ and $P_1=x$. Using $\delta/2=1/(a+1)$ now gives $p_b(b)+m=-2P'_{m-1}(a)/\delta$. The initial value $c_m(0)=m^2$ follows from the same kernel, since $D_k=-1$ at $b=0$. Integrate the derivative using $da/db=2/\delta^2$. Expanding Rodrigues' formula at $x=1$ gives $P_n(1+z)=\sum_{j=0}^n A_jz^j$ and proves the explicit sum.

## Checks and endpoint regimes

- $c_1(b)=1$, $c_2(b)=4/\delta$, and $c_3(b)=3(b^3+9b^2+3b+3)/\delta^3$.
- For $m\ge2$, $P'_{m-1}(x)>0$ on $[1,\infty)$, so $c_m$ is strictly increasing and $c_m(b)>m^2$. Retaining the constant Taylor coefficient of $P'_{m-1}$ also gives $c_m(b)\ge m^2+m^2(m-1)^2b/\delta$, with equality for $m=2$ and strict inequality for $m>2$ when $b>0$.
- For fixed $m\ge2$ and $b\uparrow1$, the top Taylor coefficient gives
  $$
  c_m(b)\sim 4(2m-3)\binom{2m-4}{m-2}^{\!2}\delta^{-(2m-3)}.
  $$
  The leading term of $P_{m-1}(a)$ cancels in $D_{m-1}$ because integration divides the leading coefficient by $m$, and $\delta a/2=1-\delta/2$. Counting the pole order by squaring the uncorrected leading power of $P_{m-1}(a)$ would incorrectly give $2m-1$.
- For fixed $b\in(0,1)$ and $m\to\infty$, put $\rho=a+\sqrt{a^2-1}=(1+\sqrt b)/(1-\sqrt b)$. Then
  $$
  c_m(b)\sim\frac{(1-b)^2}{8\pi b}\rho^{2m-1}.
  $$
  To see this, use the Laplace representation $P_n(x)=\pi^{-1}\int_0^\pi(x+\sqrt{x^2-1}\cos\theta)^n\,d\theta$. Laplace's method at $	heta=0$ gives $P_n(x)\sim R(x)^{n+1/2}/\sqrt{2\pi n\sqrt{x^2-1}}$, for $R(x)=x+\sqrt{x^2-1}$, uniformly on any compact subinterval of $(1,\infty)$. The identity $(x^2-1)P_n'=n(xP_n-P_{n-1})$ gives $P_n'\sim nP_n/\sqrt{x^2-1}$ with the same uniformity. Split the integral for $c_m$ at any $x_0\in(1,a)$. Monotonicity of $P_n'$ on $[1,x_0]$ follows from its nonnegative Taylor coefficients and bounds that piece by $(x_0-1)P_n'(x_0)^2$, exponentially smaller than the contribution near $a$. On $[x_0,a]$, the derivative of $\log R(x)$ is $1/\sqrt{x^2-1}$. Endpoint Laplace asymptotics for $2\int_{x_0}^a(P_n')^2$ give $R(a)^{2n+1}/[2\pi(a^2-1)]$. Since $a^2-1=4b/\delta^2$, this proves the claimed prefactor.

The guess $c_m(b)=m^2/\delta$ for every $m\ge2$ fails from $m=3$ on, as does the upper bound $c_m(b)\le m^2/\delta^{2m-3}$ already for $m=3$ and every $0<b<1$. As a concrete instance $c_3(1/2)=165$, while these two expressions are $18$ and $72$.

These computations use only the moment matrix of (80). Both asymptotics are statements about its finite-dimensional constant. In the arithmetic problem the prefix is fixed before the approximating parameter $N$ tends to infinity. Pointwise convergence alone gives no diagonal asymptotic even for positive functions that increase in $b$. For instance $F_N(b)=c_m(b)(1+b^N)$ has the correct pointwise limit but $F_N(1-1/N)/c_m(1-1/N)\to1+e^{-1}$.

Exact rational Gaussian elimination and the Taylor sum agreed in all 72 tested cases for multiplicities 1 through 12 at six rational prefixes. [Reproduce the checks](../scripts/prefix_skeptic62.py)
