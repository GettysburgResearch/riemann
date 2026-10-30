# Independent review of the common X detector base

The common-base counting argument is consistent with conductor and mask upper bounds alone; I found no step that requires the individual conductor to be comparable from below with X. This is an audit of the argument **conditional on** the fixed-field detector-transfer and source large-sieve inputs identified in the README, not an independent proof of those inputs.

For a good cube-free index g=ab², the good primes of ab are precisely the good primes at which χ_g ramifies. The fixed background ν is unramified there, so its twist cannot cancel this ramification. Thus the conductor bound implies `N(ab)≤X` up to the fixed conventions for the bad set; the original deleted-factor radical is also `≪X`, and the primitive conductor is `≤X`. Rows with very small individual conductor are still included.

In the nested-bin construction there are only finitely many rows and presentation/conjugate choices for each X. The number of bins is bounded in terms of the chosen bin width, not in terms of the row conductors. The logarithmic-control argument uses the upper bounds on the primitive analytic conductor and deleted radical. On the reflected line the conductor factor is `Q^(a−1/2+O(e))`; for the relevant `a>3/4` its exponent is positive, so replacing Q by its upper bound `≪X` is valid. Euler deletions are controlled by their radical upper bound; they have no zeros for positive real part. The fixed degree and fixed infinity type give polynomial dependence on the actual height, hence `X^{O(τ)}` throughout the chosen `X^τ` height window even for bounded Q. The sole potentially principal or pure norm-character row g=1 can be removed before the entire-function contour shift and counted separately using the standard individual zero bound, at cost `X^{τ+o(1)}`. It is not permissible to infer a uniform bound at all heights from the finite buffer.

For the saturated convolution the inverse cutoff D=X, and the fact that the true conductor is smaller does not change `Σ_{l|n} μ(l)=0` for `1<Nn≤D`. A fixed sufficiently large smoothing exponent B makes the shifted integral negligible based on the common conductor/height bounds. The detector then supplies the witness described in the README, provided its rowwise coefficient and frequency profiles satisfy the stated common-profile Sobolev hypothesis. The inference `m≤1/2+O(η)` and hence `r≥1/2−O(η)` uses the buffered pointwise bounds and `r+m≥1−o(1)`; neither uses a conductor lower bound.

For the global cubic large-sieve bound, cover `Na Nb≤X` by O(log²X) dyadic boxes. Endpoints give only fixed constants in `AB≪X`. With `M=min(A,B)≤N=max(A,B)`,

    M^(2/3)N^(1/3)≤(MN)^(1/2)≪X^(1/2),
    M^(1/3)N^(2/3)D^(2/3)≪X^(2/3)D^(2/3)≪X+X^(1/2)D.

The last inequality splits at D=X^(1/2). Positivity allows enlargement to complete rectangles; the subsequent finite ray-class and Sobolev partitions must retain the exact noncoprime zero masks and common coefficients as stated in the README. The squared mass of the normalized squarefree inverse coefficients is O(1), including fixed unitary twists. The global estimate and the witness imply the claimed count uniformly for r in its displayed range. If r is slightly below 1/2, its loss is O(η); if r is at most 1+o(1), the worst exponent is `3/2−δ+O(η)`.

The same argument works algebraically for the proposed general-order conjugate-pair rectangular sieve when n≥3: `M^(1−1/n)N^(1/n)≤(MN)^(1/2)` and

    M^(1/n)N^(1−1/n)D^(2/n) ≪ X^(1−1/n)D^(2/n) ≪ X+X^(1/2)D,

again splitting at D=X^(1/2). For n>3 this only treats g=ab^(n−1) with the stipulated squarefree/coprime indices. The full general-n sieve remains a source-replay hypothesis rather than an asserted theorem of De Faveri.

The unresolved dependencies are the fixed-field/fixed-unitary saturated detector with its differentiated rowwise profiles, polynomial height orders and masks; the general-n source replay when applicable; and the imported analytic conductor, functional equation and individual zero-count facts. Nothing here establishes an individual zero-free region or a priority claim.
