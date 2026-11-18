# Two-sided local comparison for the negative eigenvalue count

**Status.** Proposed analytic refinement of the [Gaussian Weil matrix](weil-gaussian-nov18.md). The local zero census in the converse is a hypothesis. No numerical certificate is asserted. The matrix on the arithmetic side retains all prime-power phases and pole and gamma terms.

Use the [bandwidth theorem's matrix](weil-bandwidth-nov18.md) with its exact convolution taper, and retain its $X,d,H,B$ satisfying $K_1H\le B\le\sqrt{XH}$ for sufficiently large absolute $K_1$. Its radius satisfies $e^{2L}=X/(2\pi)+O(XH/B)$, its frequencies satisfy $|k\pi/L-X|\le C'B$, and it has dimension $O(B\log X)$. There are absolute constants $K,D$ for which the following holds, choosing the fixed cutoff and bandwidth constants sufficiently large as in that theorem. Let $n_-$ count its ordinary eigenvalues $\le-e^{-K H}$ with multiplicities.

1. Any set of defects with $|t-X|\le B$, depth $|a|\ge d$, and pairwise height differences at least one has cardinality at most $n_-$. In particular the total multiplicity of such defects in the inner interval is $O((\log X)n_-)$ without a separation assumption.
2. $n_-$ is at most the number of **distinct conjugate pairs** of off-real centered zeros with $|t-X|\le DB$ and $|a|>e^{-2KH}$. In particular, a certified negative eigenvalue at this threshold implies an actual off-line zero in this fixed multiple of the search bandwidth. Other zeros at all heights are allowed.

These two conclusions concern different depth resolutions. Near-line zeros cannot be dropped from the exact Weil form. They have a small explicitly bounded potential negative part at the stated precision.

## Estimates used from the source matrix

The source proof gives, for each inner defect, a coefficient vector of norm $\le e^{C_0 H}$ with zero-evaluation error at most $X^{-2}$ in $\ell^2(\Gamma)$ relative to its ideal signed cluster indicator. To obtain this extra power, require the omitted Gaussian modes and the spatial-periodization errors to be $O(X^{-M})$ for a fixed larger $M$ throughout the construction. The slack $CH$ in the spatial exponent and $C'^2H/2$ in the frequency exponent pay this additional cost since $H\ge\log X$. All these parameters are fixed before choosing the exterior constant $D$.

The [exterior complement estimate](weil-local-complement-nov18.md), with width $H/B$ as in the bandwidth theorem, bounds the full exterior zero contribution in operator norm by $e^{-aH}$ for any fixed $a>0$, by choosing $D$ sufficiently large. This follows from the Fourier product of $\lceil H\rceil$ box averages and the actual unit-interval count of zeros. No local-sign hypothesis enters the exterior bound.

## Lower count from disjoint clusters

For $q$ separated defects in the inner interval the signed ideal indicators $p_i$ have disjoint supports, since each of the two associated disks has radius $\le1/4$. Conjugation $J$ of the sample index set sends each $p_i$ to $-p_i$, and $\|p_i\|^2=2m_i\ge2$. For scalars $b_i$, the manufactured evaluation vector is $p+e$, where $p=\sum b_i p_i$ and $\|e\|\le q^{1/2}X^{-2}\|b\|_2$. Here $q\le 2B+1=O(X)$ by separation. Hence $\|e\|=o(1)\|p\|$, and
\[
 \langle J(p+e),p+e\rangle\le-\tfrac12\|p\|^2\le-\|b\|_2^2 .
\]
The coefficient norm is at most $\sqrt q\,e^{C_0H}\|b\|_2$. In particular the coefficient map is injective. Min–max gives $q$ eigenvalues $\le-e^{-KH}$ for a sufficiently large absolute $K$. A maximal separated subset covers all the inner defect ordinates by radius-one intervals, each counting $O(\log X)$ total multiplicity by Riemann–von Mangoldt.

## Upper count from the actual local pairs

For a unit coefficient vector the physical test $g$ satisfies $\|g\|_2\le1$ by orthonormality of the uncut modes and $0\le\chi\le1$. Write $F=\widehat g$. At each nonreal conjugate pair with ordinate $t$, depth $|a|$, and common multiplicity $m$, put $E=(F(t+ia)+F(t-ia))/2$ and $O=(F(t+ia)-F(t-ia))/2$. Its Hermitian quadratic form is $2m(|E|^2-|O|^2)$, with negative part dominated by a rank-one form. A line zero contributes nonnegatively. For $|a|\le e^{-2KH}$ one has
\[
 |O|\le\int_{-L}^L|g(u)|\sinh(|a|L)du\le\sqrt{2L}\sinh(|a|L).
\]
There are $O((1+DB)\log X)$ local ordinates counted with multiplicity for fixed $D$ and sufficiently small $H/X$. The total possible loss of all these shallow pairs is therefore $\le e^{-2KH}$ for $K$ sufficiently large. With $K$ now fixed, take $D$ to make the exterior loss $\le e^{-2KH}$ as well, enlarging $X$ afterward to absorb constants depending on $D$.

Impose $O=0$ at each distinct remaining local nonreal pair. These are linear conditions on the coefficients of total codimension at most the number of those pairs. On their joint kernel the full form is $\ge-2e^{-2KH}>-e^{-KH}$. Min–max proves the upper count, including the strict margin at the threshold. This is a finite-resolution converse for the actual matrix, independent of any distributional model of the exterior zeros.
