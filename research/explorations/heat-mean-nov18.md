# Simultaneous First-Hermite positivity through a logarithmic heat range for almost all centers

**Status.** Proposed analytic bound for review. Fix $0<c<2$. For sufficiently large $X$ (depending on $c$), all but $O_c(X/\log X)$ of the interval $[X,2X]$, in Lebesgue measure, consists of centers $x$ satisfying
\[
 M(q,x)>0\qquad\text{for every real }0<q\le c\log X.
\]
This estimate uses the actual von Mangoldt coefficients. Its exceptional set can include a negative witness.

## Source and proof

Use the normalization $z=(\rho-1/2)/i$ and $M(q,x)=\sum_\rho(z-x)^2 e^{-q(z-x)^2}$. Put $L=\log X$, $u=\log n$, $v=u^2/(4q)$, and
\[
 h_q(u)=(1-2v)e^{-v},\quad S_q(x)=\sum_{n\ge2}\Lambda(n)n^{-1/2+ix}h_q(\log n).
\]
The first-Hermite explicit formula (source PR #379) gives a positive archimedean reserve $\gg Lq^{-3/2}$ on the whole dyadic block for $q\ge1$ and large $X$, by integrating the Gaussian weight within $q^{-1/2}$ of $x$ using Stirling. A negative bounded part of the gamma density costs $O(q^{-3/2})$. The pole contribution is $O((1+x^2)e^{-q(x^2-1/4)})$, and the prime contribution is $-\Re S_q(x)/(2\sqrt\pi q^{3/2})$. Consequently $M(q,x)\le0$ requires $|S_q(x)|\ge c_0 L$ with an absolute $c_0>0$. For $q<1$ the integrated exterior wedge covers the full block once $X$ is large.

Let $D=q\partial_q$. The multiplier of $DS_q$ is $(3v-2v^2)e^{-v}$. Both multipliers are a fixed polynomial times $e^{-v}$. Write $b_n$ for the resulting coefficients of either Dirichlet series before the factor $n^{ix}$. Two energy bounds valid for $q\ge1$ are
\[
 \sum_n|b_n|^2\ll q,\qquad \sum_n n|b_n|^2\ll (1+q)^7e^{q/2}.
\]
For the first, $\sum_{n\le e^U}\Lambda(n)^2/n\ll(1+U)^2$ by Chebyshev and partial summation. Apply this in blocks $j\sqrt q\le u<(j+1)\sqrt q$ and sum the resulting polynomial in $j$ times $e^{-j^2/2}$. For the second, use $\Lambda(n)\le u$. On $m\le u<m+1$ there are fewer than $e^{m+1}$ integers. The contribution is bounded by a constant times
\[
 (m+1)^2\big[1+(m+1)^8/q^4\big]\exp\{q/2-(m-q)^2/(2q)\}.
\]
Summing the Gaussian moments gives $O((1+q)^{13/2}e^{q/2})$, within the stated bound.

Montgomery–Vaughan's mean-value theorem for Dirichlet polynomials bounds the squared $L^2([X,2X],dx/X)$ norm by $\sum_n |b_n|^2+O(X^{-1}\sum_n n|b_n|^2)$. The infinite series follow by truncation, or direct uniform convergence on compact $q$ intervals. For $1\le q\le Q=cL$, the second error term is $O_c((1+L)^7 X^{c/2-1})=o_c(1)$. Thus both $S_q$ and $DS_q$ have normalized $L^2$ norm $O_c(\sqrt q)$.

Finally, absolute locally uniform convergence permits differentiation and
\[
 \sup_{1\le q\le Q}|S_q(x)|\le |S_1(x)|+\int_1^Q |DS_r(x)|\,dr/r.
\]
Minkowski's integral inequality bounds the normalized $L^2$ norm of this supremum by $O_c(1+\int_1^Q r^{-1/2}dr)=O_c(\sqrt L)$. Chebyshev's inequality at threshold $c_0L$ proves the assertion.

## Relation to previous work

The earlier large-values branch obtains an exponentially small exceptional fraction for integer $q\le(\log X)^{1-\epsilon}$. Here the exceptional fraction is larger. The weighted mean-value error permits all real parameters through $c\log X$. No numerical or interval computation enters. [Earlier large-values proof](https://github.com/GettysburgResearch/riemann/blob/ea20af8867c3119c23efc27738d343aac2f79362/research/external/anthropic-zeta23/proofs/FIRST_HERMITE_LARGE_VALUES.md) · [Integrated pointwise wedge](../integrated/heat_hermite/FIRST_HERMITE_REGIONS.md)
