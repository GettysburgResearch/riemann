# Exact divisor conjugation of the signed prime matrix

**Status.** Proposed arithmetic decomposition and pointwise positivity theorem on a sparse physical subspace. The decomposition applies to the full [frequency-local matrix](weil-bandwidth-nov18.md), including all its growing modes. It identifies the signed quadratic estimate still needed for that matrix's smallest eigenvalue.

## A native diagonal reserve throughout the search space

Translate the compact physical interval to $[0,U]$, $U=2L$, extending all inputs by zero. Translation leaves the Weil form, the pole sum, and the signed prime autocorrelations unchanged. For integer $n\ge1$ set $T_nf(u)=f(u+\log n)$ on this interval. The translations compose as $T_nT_m=T_{nm}$, and they vanish almost everywhere when $n>e^U$. Define
\[
 K=\sum_{n\le e^U}n^{-1/2}T_n,\quad
 K^{-1}=\sum_{n\le e^U}\mu(n)n^{-1/2}T_n,\quad
 V=\sum_{n\le e^U}\Lambda(n)n^{-1/2}T_n .
\]
The stated inverse follows from the exact divisor identity $\mu*1=\mathbf1_{\{1\}}$. The prime term is $P(g)=2\Re\langle Vg,g\rangle$. For any trial vector $g$ take $f=K^{-1}g$. The second divisor identity $\sum_{d\mid n}\Lambda(d)=\log n$ gives
\[
 VKf=\sum_{n\le e^U} (\log n)n^{-1/2}T_n f.
\]
Consequently, with no sign discarded,
\[
 U\|g\|^2-P(g)=D_U(f)+E_U(f),
\]
where
\[
 D_U(f)=\int_0^U [U H_{\lfloor e^y\rfloor}-2J_{\lfloor e^y\rfloor}]|f(y)|^2dy,
 \quad H_N=\sum_{n\le N}n^{-1},\quad J_N=\sum_{n\le N}(\log n)/n ,
\]
\[
 E_U(f)=2\Re\sum_{1\le m<n\le e^U}
 \frac{U-\log(mn)}{\sqrt{mn}}
 \int_0^{U-\log n} f(u+\log n)\overline{f(u+\log m)}\,du .
\]
This is just the double expansion of $\|Kf\|^2$ and its log-weighted partner, including their common cutoff.

There is an absolute $c>0$ with $D_U(f)\ge c U\|f\|^2$ for every $U\ge1$. Indeed $H_N\ge\log N+1/2$ by the trapezoid inequality for $1/x$. For $N\ge3$, monotonicity of $(\log x)/x$ on $[3,\infty)$ gives
\[
 2J_N\le \log^2 N+\log2+\tfrac23\log3-\log^2 3
          <\log^2 N+1/4 .
\]
Thus $(\log N)H_N-2J_N\ge(1/2-1/(4\log3))\log N$ for $N\ge3$. Direct substitution handles $N=1,2$ (at $N=2$ the difference is $(\log2)/2$). Adding $(U-\log N)H_N$ gives the claimed lower bound uniformly.

For a near-carrier test $g(u)=e^{-iXu}b(u)$ the input is exactly
\[
 f(u)=e^{-iXu}b_M(u),\qquad b_M(u)=\sum_{k\le e^{U-u}}\mu(k)k^{-1/2-iX}b(u+\log k).
\]
In $E_U$ the oscillatory phase is $(n/m)^{-iX}$ times the complete translated $b_M$ correlation. If $G(g)$ and $Z(g)$ denote the signed gamma integral and the two pole terms, the exact residual is
\[
 W(g)=D_U(f)+E_U(f)+G(g)-U\|g\|^2+Z(g).
\]
For instance an exact source-specific sufficient condition for pointwise positivity is
\[
 -E_U(f)+|G(g)-U\|g\|^2+Z(g)|\le D_U(f)
\]
for every coefficient vector in the prescribed local trial space. The left side contains near equal ratios and arithmetic phases for all translated Möbius sources. A bound for separate translations after taking absolute values has not been obtained. In particular the mean spectral count does not supply this pointwise signed estimate.

## A pointwise lower bound for a growing physical subspace

There are absolute $c_*,c_0>0$ with the following property. Take any sufficiently large $U$, $Y=e^U$, $w=c_*/Y$, and $N=\lfloor e^{U-3w}\rfloor$. Inside $[0,U]$ place the intervals
\[
             I_n=w+\log n+[0,w],\qquad 1\le n\le N.
\]
For every smooth test $g$ supported in their union and satisfying on each interval the three moment conditions
\[
 \int_{I_n}g(u)du=\int_{I_n}g(u)e^{u/2}du
                 =\int_{I_n}g(u)e^{-u/2}du=0 ,
\]
one has $W(g)\ge c_0\|g\|^2$. The bound is uniform in every vector in this space, including arbitrary complex phases and superpositions across intervals. Nonzero smooth shapes exist, for example by taking $(\partial_u^2-1/4)\partial_u$ of any smooth bump compactly supported in a single interval.

Choose $c_*<1/4$ so that $w<\log(1+1/N)$. The intervals are disjoint. Two translated intervals can overlap under a prime-power translation by $\log d$ only when the corresponding centers agree exactly, namely $m=dn$. Indeed if the integer $dn$ differs from $m\le N$, their log distance is at least $\log(1+1/N)$. Write $b_n(v)=g(w+\log n+v)$ for $v\in[0,w]$. Then the prime quadratic form is exactly
\[
 P(g)=2\Re\sum_{dn\le N}\frac{\Lambda(d)}{\sqrt d}\langle b_{dn},b_n\rangle .
\]
Use positive Schur weights $v_n=n^{-1/2}$. The weighted row sum at $n$ of the real symmetric adjacency matrix is
\[
 \sum_{d\mid n}\Lambda(d)+\sum_{d\le N/n}\Lambda(d)/d
 =\log n+\log(N/n)+O(1)=\log N+O(1).
\]
Here $\sum_{d\le x}\Lambda(d)/d=\log x+O(1)$ is the classical first Mertens estimate with prime powers, uniformly for $x\ge1$. The Schur bound follows directly by applying $2ab\le a^2 v_j/v_i+b^2 v_i/v_j$ on each edge, and holds for the Hilbert-valued coefficients $b_n$ as well. Thus $P(g)\le(\log N+C_1)\|g\|^2$. The coefficient $1$ is sharp to leading order: take $b_n=n^{-1/2}b$ for one common admissible shape to obtain $P(g)/\|g\|^2=2J_N/H_N=\log N-\gamma_E+o(1)$.

To bound the signed gamma integral from below, the primitive $p(u)=\int_{-\infty}^u g(v)dv$ is supported in the same intervals by their zero integrals. Cauchy–Schwarz on each interval gives $\|p\|_2\le w\|g\|_2$. Plancherel and $|\widehat g(t)|=|t\widehat p(t)|$ imply
\[
 \frac1{2\pi\|g\|^2}\int_{|t|\le A}|\widehat g(t)|^2dt\le w^2 A^2 .
\]
Integrating the normalized bound with $A=e^{-s}/w$ for $s\ge0$ shows that the spectral expectation of $\log^- (w|t|)$ is at most $1/2$. Since $\Re\psi(1/4+it/2)-\log\pi\ge\log|t|-C_2$ by Stirling and continuity, $G(g)\ge[\log(1/w)-C_2-1/2]\|g\|^2$. The two exponential moments kill both pole evaluations. Choose $c_*$ so small that $-\log c_*>C_1+C_2+2$. The explicit formula gives the uniform gap.

The intervals occupy total physical length at most $c_*$. Their moment conditions force a broad frequency distribution. The proof does not put the narrow-band cluster projectors in this sparse subspace. For those projectors the exact off-diagonal $E_U$ above remains uncontrolled.

## The relative precision already forced by one actual Fourier mode

For $Y=X/(2\pi)$, $U=\log Y$, let $g_\omega(u)=U^{-1/2}\chi(u)e^{-i\omega u}$, where $0\le\chi\le1$ equals one outside fixed-width endpoint regions in $[0,U]$, and is supported inside this interval. Average with normalized Lebesgue measure on $X\le\omega\le2X$. The exact signed covariance above satisfies
\[
 \mathbb E D_U(K^{-1}g_\omega)=\frac{U^3}{12\zeta(2)}+O(U^2),
 \qquad
 \frac{\mathbb E[-E_U(K^{-1}g_\omega)]}{\mathbb E D_U(K^{-1}g_\omega)}
 =1-\frac{12\zeta(2)+O(1/U)}{U^2}.
\]
In particular there cannot be a fixed $\tau>0$ with $E_U(f)\ge-(1-\tau)D_U(f)$ uniformly over these actual trial vectors at large $X$. More generally, any uniform margin $\tau_X$ in that inequality must satisfy $\tau_X\le(12\zeta(2)+o(1))/U^2$. This is a ratio of arithmetic averages, not an assertion about the distribution of their pointwise ratio.

In fact the Montgomery–Vaughan mean-value estimate applied at each $u$ gives
\[
 \mathbb E |(K^{-1}g_\omega)(u)|^2
 = U^{-1}\left[\sum_{k\le e^{U-u}}\frac{\mu(k)^2}k\chi(u+\log k)^2
         +O(e^{U-u}/X)\right]
 =\frac{U-u}{U\zeta(2)}+O(1/U).
\]
Here $\sum_{k\le e^v}\mu(k)^2/k=v/\zeta(2)+O(1)$ by squarefree counting and partial summation. Deleting either endpoint region costs $O(1)$ uniformly in $u$ by the harmonic sum over an interval of bounded log-length. On the full interval the exact diagonal weight is $u(U-u)+O(U)$ by the harmonic integral estimates. Its integration gives the first formula since $\int_0^U u(U-u)^2du=U^4/12$. Finally $U\|g_\omega\|^2=U+O(1)$ while $\mathbb E P(g_\omega)=O(X^{-1/2})$ by direct phase integration as in the [arithmetic second moment](weil-prime-average-nov18.md). Substitution into the exact conjugation proves the relative estimate.
