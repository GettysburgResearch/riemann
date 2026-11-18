# An explicit finite cutoff for reciprocal power-trace tests

18 November 2026. For a fixed finite reciprocal spectrum, simultaneous phase approximation gives a cutoff in terms of the largest off-circle modulus. For roots of a monic integral polynomial with normalization radius $\sqrt q$, $q$ a positive integer, the algebraic norm gives a gap depending only on $q$ and the degree. No publication priority is claimed. [Finite-spectrum criterion](../../frontiers/geometry64_minimal_polarization.md) · [Independent finite-spectrum audit](positivity64_geometric_skeptic.md)

## Witness from a supplied modulus gap

Let $\{z_j\}_{j=1}^d$ be a nonempty multiset of nonzero normalized roots stable, with multiplicities, under conjugation and inversion. Let $s_n=\sum_j z_j^n\in\mathbb R$ and $R=\max_j|z_j|$. If the spectrum is off the unit circle, inversion gives $R>1$. Take an integer $n_0$ with $n_0>\log(2d)/\log R$ and write $z_j=|z_j|e^{2\pi i\theta_j}$.

For any vector $v\in\mathbb R^m$ and integer $Q\ge2$, put $0,v,\ldots,Q^m v$ modulo $\mathbb Z^m$ into $Q^m$ half-open boxes of side length $1/Q$. A difference gives an integer $1\le k\le Q^m$ with $\|kv_j\|_{\mathbb R/\mathbb Z}<1/Q$ in each coordinate. Applying this to all $d$ original phases with $Q=\lceil12n_0\rceil$ gives $\|n_0 k\theta_j\|<1/12$ and the proposed bound $n=n_0 k\le n_0\lceil12n_0\rceil^d$.

A smaller witness comes from applying the very same argument directly to the **scaled** phases $n_0\theta_j$, with $Q=6$. Then for $n=n_0 k$ every phase in $z_j^n$ has cosine greater than $1/2$. In particular
$$
s_n=\sum_j |z_j|^n\cos(2\pi n\theta_j)>
\tfrac12\sum_j |z_j|^n\ge\tfrac12R^n>d,\qquad n\le n_0 6^d.
$$
The interior roots cause no cancellation because their phases are controlled too. Conjugation makes $s_n$ real, and multiplicities contribute positive weights. When choosing $n_0$ even, both real phases have cosine one automatically. Applying the box argument to one phase for each nonreal conjugate pair of distinct roots then gives $n\le n_0 6^{\lfloor d/2\rfloor}$, with the convention $k=1$ for an empty list. A violation $s_n>d$ fails the two-term test, for example at $p(X)=1-X^n$.

## Uniform algebraic gap for integral polynomials

Let the unnormalized spectrum consist of the roots $\alpha_j$ of a monic polynomial $P(X)\in\mathbb Z[X]$ of degree $d$. Assume $z_j=\alpha_j/\sqrt q$ satisfy the same symmetries, for fixed $q\in\mathbb Z_{\ge1}$. No early trace inequalities are needed for the following gap calculation. If $R>1$, choose a root $\alpha$ of maximal modulus and put $\beta=\alpha\bar\alpha=qR^2>q$. This is an algebraic integer. Every conjugate of $\beta$ is a product of two roots of $P$, because any embedding extends to the splitting field and permutes the roots. All conjugates therefore have absolute value at most $\beta$. If $\alpha$ is real, $\beta=\alpha^2$ has degree at most $d$. If it is nonreal, the conjugates are obtained as products of two distinct roots, so the degree is at most $\binom d2$. In both cases set $D=\max(d,\binom d2)$.

When $\beta\ge q+1$ the gap is at least one. Otherwise $\beta<q+1$, and every conjugate $\beta'$ satisfies $|\beta'-q|<2q+1$. Taking the norm of the nonzero algebraic integer $\beta-q$ in $\mathbb Q(\beta)$ gives
$$
1\le|\operatorname{Norm}(\beta-q)|
\le (\beta-q)(2q+1)^{D-1}.
$$
Thus in either case $\beta-q\ge\delta$ for $\delta=(2q+1)^{1-D}$. For $\beta<q+1$, integrating $1/(q+u)$ from zero to $\beta-q$ gives
$$
\log R=\tfrac12\log(\beta/q)\ge\frac{\beta-q}{2(q+1)}
\ge\frac{\delta}{2(q+1)}.
$$
For $\beta\ge q+1$, the same lower bound follows first by replacing $\beta$ by $q+1$ and then integrating up to $u=1$. The argument needs no coefficient bound, since either $\beta$ itself lies in a bounded strip above $q$, which controls every conjugate, or there is already a larger gap. The norm step also works at $\alpha$ repeated, since distinct embeddings and distinct products are what bound the degree.

Consequently the following is an explicit, generally coarse cutoff. Choose the even integer
$$
n_0=2\left(1+\left\lfloor(q+1)(2q+1)^{D-1}\log(2d)\right\rfloor\right),
\qquad
B_{q,d}=n_0 6^{\lfloor d/2\rfloor}.
$$
If $s_n\le d$ at every positive $n\le B_{q,d}$, then the spectrum is on the unit circle. The converse follows from the triangle inequality. The cutoff also applies to the two-sided tests $|s_n|\le d$, equivalent to positivity on $a+bX^n$ under reciprocal symmetry. The bound is uniform for these integral polynomials of degree $d$ and weight-one radius $\sqrt q$. Other integral weight radii $\sqrt{q^w}$ with $w\ge0$ are covered by using $q^w$ in place of $q$. It actually suffices to test the multiples of $n_0$ through $B_{q,d}$, since the constructed witness is among those multiples. One can use the purely integral choice $n_0=4d(q+1)(2q+1)^{D-1}$ in the same formulas, since $\log(2d)<2d$. The bound gives no restriction of the witness to prime indices.
