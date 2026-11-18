# Logarithmic trace growth is equivalent to the weak Mertens hypothesis

**Status.** Proposed two-sided growth-class adapter and conditional asymptotic. The arithmetic hypothesis in the title is open. The equivalence does not establish it.

Let $m_o(x)=\sum_{n\le x,n\text{ odd}}\mu(n)/n$, let $m_a$ denote the same sum over all positive integers, and let $M(x)=\sum_{n\le x}\mu(n)$. Extend the sums by zero for $x<1$. Use the ordinary odd Legendre trace $S_N=\sum_{j<N}\|K\phi_j\|_{L^2(1,3)}^2$ of [#866](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md), where $Kp(t)=\int_0^1m_o(t/u)p(u)\,du/u$ on odd polynomials. The classical bound $|m_o|\le2$ suffices below. Define $F_o(X)=\int_1^X |m_o(x)|^2\,dx$.

For every real $X\ge3$ and integer $D\ge X$, with an absolute implied constant,
$$
 (\log3)\int_3^X|m_o(x)|^2\,dx
 \ \le\int_1^3\frac{dt}{t}\int_t^{tX}|m_o(x)|^2\,dx
 \ \le S_D+O(X^2/D).
\tag{1}
$$
Thus an all-degree trace bound transfers back to the genuine reciprocal-Möbius energy. The other direction already has an explicit finite bound in [#869, arithmetic Theorem 4](https://github.com/GettysburgResearch/riemann/blob/5e559c9cbf5aee84ff7ed78dc91b55df744aef56/standalone/2026-09-12-three-route-completion/arithmetic/PROOF.md). Together these show, for every fixed $k\ge0$, the equivalence
$$
 S_N\ll(\log(2N))^k
 \quad\Longleftrightarrow\quad F_o(X)\ll(\log(2X))^k
 \quad\Longleftrightarrow\quad
 \int_1^X |M(x)/x|^2\,dx\ll(\log(2X))^k .
\tag{2}
$$
The quantifiers are all $N$ or all $X$ with a constant independent of cutoff. For $k=1$ the right side is the classical weak Mertens hypothesis. The reverse estimate (1) uses a polynomial scale but incurs only additive error. An $N^{o(1)}$ multiplicative loss alone could erase logarithmic growth information.

## Proof of the reverse estimate

Fix $1<t<3$, put $G_t(u)=\mathbf1_{u\ge1/X}m_o(t/u)/u^2$ on $0\le u\le1$, and put $g_t(u)=uG_t(u)$. Let $H_t(\theta)=G_t(|\cos\theta|)$ on the circle. Uniformly in $t$, $\|G_t\|_\infty\le2X^2$ and the total variation of $H_t$ is $O(X^2)$. In fact the variation of $G_t$ consists of a cutoff jump $O(X^2)$, the smooth derivative bounded in absolute integral by $\int_{1/X}^1 4u^{-3}\,du$, and jumps of size at most $n/t^2$ at $u=t/n$ for $n\le3X$. These sum to $O(X^2)$. Taking the cosine composition traverses $[0,1]$ only four times on the circle.

Convolve $H_t$ with the nonnegative circle kernel $J_D(\theta)$ proportional to $(\sin(D\theta/2)/\sin(\theta/2))^4$, normalized to unit integral. It has trigonometric degree $2D-2$ and, on $|\theta|\le\pi$, satisfies $J_D(\theta)\ll D(1+D|\theta|)^{-4}$. Indeed its unnormalized fourth power is $O(\min(D^4,|\theta|^{-4}))$ and its integral is comparable to $D^3$ by also restricting to $|\theta|\le 1/D$. The result of the convolution is an even, $\pi$-periodic cosine polynomial, hence $P_t(\cos\theta)$ for an even algebraic polynomial of degree at most $2D-2$. Bounded variation gives $\int|H_t(\theta-z)-H_t(\theta)|\,d\theta\le |z|\operatorname{Var}(H_t)$, by integrating the total variation measure over translated arcs. Since $|du|\le d\theta$ on a single traversal, the kernel's first absolute moment yields
$$
 \int_0^1 |P_t(u)-G_t(u)|\,du\ll X^2/D .
\tag{3}
$$
There is also a uniform weighted supremum $u^2|P_t(u)|\ll1$. To check it take $u=\cos\theta\ge0$. For $|z|\le u/2$, $|\cos(\theta-z)|\ge u/2$ and the integrand $|H_t(\theta-z)|\le8/u^2$. For $|z|>u/2$, it costs at most $2X^2$ times kernel mass $O((1+Du)^{-3})$. Multiplying by $u^2$ bounds this contribution by $O(X^2/D^2)$, uniformly bounded by $D\ge X$.

The allowed polynomial $p_t(u)=uP_t(u)$ therefore satisfies
$$
 \|p_t-g_t\|_2^2
 \le\big(\sup_u u^2|P_t-G_t|\big)\int_0^1|P_t-G_t|\,du\ll X^2/D .
$$
On $0<u<1/X$ the pairing with the untruncated singular row is a convergent ordinary integral. Its absolute value is at most $2\int_0^{1/X}|P_t|\,du\ll X^2/D$ by (3), since $G_t$ vanishes there. For each fixed $t$ the finite-dimensional row norm satisfies
$$
 \sum_{j<D}|K\phi_j(t)|^2
 \ge 2\Re (Kp_t)(t)-\|p_t\|_2^2
 \ge \|g_t\|_2^2-O(X^2/D).
$$
The family $p_t$ is chosen only for this rowwise variational inequality; no common optimizer across different $t$ is assumed. Integrate in $t$ and put $x=t/u$ to obtain (1). The left inequality there follows from $[3,X]\subset[t,tX]$ throughout the output interval.

## The three growth classes

Use $D=\lceil X^2\rceil$ in (1) for the trace-to-source direction. For the converse, the proof of #869 Theorem 4 above its equation (5.6) gives for every $Y\ge2$, $N\ge2$,
$$
 \sqrt{S_N}\le\sqrt{(\log3)F_o(3Y)}
                 +18\sqrt2\,(2N-1)^{3/2}/Y .
$$
Taking $Y=(2N)^{3/2}$ gives the required growth bound. The identities $m_a(x)=m_o(x)-\tfrac12 m_o(x/2)$ and $m_o(x)=\sum_{j\ge0}2^{-j}m_a(x/2^j)$ show that the bound on $F_o$ is equivalent to the corresponding all-integer bound. In the reverse sum Minkowski costs only the convergent geometric factor $\sum_j 2^{-j/2}$ after dilation in $L^2(0,X)$.

For the last conversion write $f(x)=M(x)/x$. Partial summation gives
$$
 f(x)=m_a(x)-x^{-1}\int_1^x m_a(u)\,du,\qquad
 m_a(x)=f(x)-\int_x^\infty f(u)\,du/u .
$$
For the second identity use the classical PNT bound $M(u)\ll_A u/(\log(2u))^A$, the limit $m_a(\infty)=0$ and partial summation. On $[1,X]$ the forward and adjoint Hardy operators truncated to this interval have $L^2$ norm at most two (by extension by zero to the positive half-line and the classical Hardy inequality). Only the constant tail in the second identity needs payment beyond $X$. If $\int_1^Y |f|^2\ll(\log(2Y))^k$ at every $Y$, Cauchy–Schwarz on successive $[2^i X,2^{i+1}X]$ bounds the tail by $O_k(X^{-1/2}(\log(2X))^{k/2})$ after summing a geometrically convergent series. Its squared $L^2(1,X)$ contribution is $O_k((\log(2X))^k)$. This proves (2).

## A leading coefficient under a stronger source hypothesis

If $L=\limsup_{X\to\infty}F_o(X)/\log X<\infty$, then
$$
 \limsup_{N\to\infty} S_N/\log N\le (\log3)L.
\tag{4}
$$
Indeed truncate the input at $u=1/Y$ for $Y=N^{1+\epsilon}$ with fixed $\epsilon>0$. The high-input Hilbert–Schmidt norm is at most $\sqrt{(\log3)F_o(3Y)}$. On the low input the projection row norm $(\sum_{j<N}|\phi_j(u)|^2)^{1/2}$ is $O(N^{3/2}u)$ by DG26 (2.5), and $\int_1^3 |m_o(t/u)|^2dt\le u F_o(3/u)\ll u\log(3/u)$. Minkowski for the rank-one integral bounds its Hilbert–Schmidt norm by $O(N^{3/2}Y^{-3/2}\sqrt{\log(3Y)})=o(1)$. Divide by $\sqrt{\log N}$ and let $\epsilon\downarrow0$. This proves (4). Conversely (1) always gives $\limsup S_N/\log N\ge (\log3)L/2$ with the same $L$.

One sufficient source hypothesis for an exact coefficient is that $L$ equals the finite sum of squared reciprocal leading coefficients $\sum_{\rho}|(\rho-1)(1-2^{-\rho})\zeta'(\rho)|^{-2}$ over simple critical zeros (the sum may have infinitely many terms). In that case (4) and [the simultaneous critical-zero lower bound](trace-zero-residues-nov18.md) force $S_N/\log N\to(\log3)L$. Identifying $L$ with that sum is an additional arithmetic condition. A weak-Mertens upper bound alone gives only boundedness of the normalized energies here.

**Verification scope.** The proof is analytic. The cutoff row is constructed using the full primitive odd Möbius source through $3X$ and the uniform $|m_o|\le2$ bound for the part below the cutoff. The finite-scale estimate retains that origin cost. No power saving or effective numerical value of $L$ is established.
