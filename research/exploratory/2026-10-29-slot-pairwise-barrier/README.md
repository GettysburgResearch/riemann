# Pairwise slot cancellation and the one-half threshold

**Status:** This is an elementary matrix reduction and counterexample, not a new character-sum estimate or a zero-free theorem. It explains a barrier to deriving strong selected-row counts from individual slot correlations alone.

Let V be an M-by-N matrix with `|V_ip|≤1`, let `H=VV*`, and let a be one common slot coefficient vector with `||a||²≤S`. Suppose all M rows are selected at squared amplitude at least T:

    |(Va)_i|² ≥ T  for every i.

Assume `H_ii≤N` and `|H_ij|≤R` for `i≠j`, taking `0≤R≤N` (larger R can be replaced by N). Then Schur's bound gives

    M T ≤ ||Va||² ≤ S ||H|| ≤ S (N+(M−1)R).                 (1)

Thus the usable count estimate

    M ≤ S(N−R)/(T−SR)                                        (2)

requires `T>SR`; if `T≤SR`, (1) by itself gives no upper bound on M. At prime scale P, one has `N≈P/log P`, `S≤N/P≈1/log P`, and the target is `T=P^σ`. Even the ideal pairwise estimate `R≈sqrt(P)` up to logarithms gives `SR≈sqrt(P)/log P`. For fixed `σ<1/2`, inequality (2) therefore does not apply. For `σ>1/2`, it gives the familiar scale `M≪P^(1−σ)` up to logarithms. In particular the critical PR94 slope `σ=223/500<1/2` lies on the side where individual square-root correlations do not force a useful count by this method. This observation is independent of whether such square-root bounds for the sextic characters are actually known.

## An explicit matrix showing the limitation is real

Fix `σ<1/2` and choose `1/2<c<1−σ`. For arbitrarily large real P, put `N=floor(P/log P)`, `k=floor(sqrt(P))`, and `M=floor(P^c)`. For large P, `M≤N−k`. Construct V by taking k all-one columns, followed by M distinct rows of the unnormalized `(N−k)`-point Fourier matrix. Every entry has modulus one and

    H = (N−k) I_M + k 1_M 1_M*,
    H_ii=N,  H_ij=k≤sqrt(P) for i≠j.                          (3)

The [finite phase lemma](../2026-10-29-prime-slot-graph-obstruction/README.md) produces one vector with `|a_p|≤P^(−1/2)`, hence `S≤N/P`, such that at least M/2 rows have

    |(Va)_i|² ≫ N²/[P M log(2N)] ≍ P/[M(log P)^3] ≥ P^σ

for large P. After retaining those selected rows, (3) still holds on the retained submatrix. Therefore even simultaneously having modulus-one entries, pairwise square-root correlation, the usual coefficient bound, and more than `sqrt(P)` selected rows is consistent at every fixed `σ<1/2`.

This V is an abstract Fourier construction, not a matrix of sextic characters or fixed smooth prime-slot coefficients. It does not refute an arithmetic selected-row count, a selected operator estimate, or a zero-free region. It shows exactly what an argument using only these matrix properties cannot achieve; arithmetic collective cancellation or additional detector structure would have to enter separately.

**Independent review:** High_match checked the Schur threshold, the exact Fourier Gram matrix and the common-phase lemma's selected-response exponent, including the distinction between the abstract matrix and arithmetic applications.
