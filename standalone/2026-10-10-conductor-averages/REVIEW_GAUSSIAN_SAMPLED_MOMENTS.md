# Independent content review: the Gaussian sampled-moment criterion

Reviewer: root research agent, independent of the note's author.
Review date: 2026-10-10.
Reviewed file: GAUSSIAN_SAMPLED_MOMENTS.md.
Reviewed SHA-256:
53625b2fc8da8162792bb40cbb329cd609ddf152d362f05fad32ac7b841d41d4.

This is an AI mathematical content review. The exact committed-blob
binding is supplied separately after the source commit is frozen.
It is not human external acceptance, formal verification, or a proof
of the assumed arithmetic moment.

## Verdict and scope

Accept the displayed deterministic interpolation, finite-truncation,
causal-inversion, and conditional extraction results at this content
hash. I reconstructed each of these arguments, rather than relying
on the author's summary. I found no remaining mathematical defect in
the reviewed text. The sampled arithmetic bound is explicitly an
assumption throughout.

## Checks that carry mathematical weight

1. **Uniform counting and entire continuation.** The Stieltjes estimate
   uses \(J(T)\ll T\), including \(J(T)=0\) below one. The integral
   \(\int y|G'(y)|\,dy\) is finite and gives \(O(D)\) uniformly in
   the row for every \(D>0\). The complex shift has modulus exactly
   \(e^{(\Im z)^2/2}G(Nn/(Xe^{\Re z}))\). Normal convergence on
   compact sets follows from a Gaussian majorant, and the Mellin
   transform is exactly \(e^{s^2/2}\), with the stated normalization.

2. **Derivative constants are quantitative.** Cauchy's formula at
   radius \(\sqrt m\) gives
   \(CXe^{\sqrt m+m/2}m^{-m/2}\) for the derivative divided by
   \(m!\). A fixed exponential constant absorbs \(e^{\sqrt m}\).
   This verifies the all-order rate used to choose the observation
   count; an unspecified smoothness estimate would not justify it.

3. **Arbitrarily located apertures.** Chebyshev leaves a set of half
   the original measure. A greedy selection gives \(m\) points at
   separation \(\gamma\ell/(4m)\), and ordered point separation
   supplies the factorial denominators in the Lagrange sum. The
   remainder bound is valid for complex-valued functions by the
   divided-difference integral formula, without a real mean-value
   theorem. The argument uses only the total aperture measure.

4. **Moving-height rows are covered.** All interpolation uses the
   same rows \(Nu\le X^h\). Observed scales lie in \([X,2X]\),
   whose moving row windows contain this set. Output scales lie in
   \([X/2,X]\), whose row windows are contained in it. Applying
   the row \(\ell^p\) triangle inequality is therefore valid.
   This previous-interval step is necessary; a same-interval
   argument at fixed lower row height would omit rows.

5. **The smaller grid has no polynomial loss.** For
   \(n_X=\lceil8\log(e^eX)/\log\log(e^eX)\rceil\),
   \(n_X\log n_X/(2\log X)\to4\) and
   \(n_X/\log X\to0\). Hence the remainder is
   \(X^{-3+o(1)}\) before the row count and the grid multiplier
   is \(X^{o(1)}\). The aperture condition
   \(\log(1/\gamma_X)=o(\log\log X)\) gives the same conclusion.
   A fixed negative power of \(\log X\) for the aperture measure
   is correctly excluded from this assertion.

6. **Finite observations approximate the entire family.** The tail
   inequality follows term by term from
   \(e^{-t^2/2}\le e^{-R^2/4}e^{-t^2/4}\) when \(|t|\ge R\).
   The variance-two count gives \(CD e^{-R^2/4}\), and the proposed
   window yields \(D^{-A}\). The finite sum is used only to
   approximate values; its moving endpoints are never differentiated.

7. **Causal inversion does not assume the desired conclusion.**
   The coefficient error follows from \(J(Y)=c_KY+O(\sqrt Y)\);
   the bound also holds for \(N\operatorname{rad}d>Y\).
   A dilation costs \((Nd)^{-\sigma}\) in the weighted norm.
   The Euler factors and inverse in (6.8) multiply to one, and
   their nonconstant coefficient norms are summable over primes.
   Taking \(0<\delta<\min(\sigma,1/2)\) makes the error series
   converge. A finite-interval Neumann inverse is uniform in its
   upper endpoint. The low part of the function has a finite
   global weighted norm; its image under the positive operator
   does also. Taking the upper endpoint to infinity is then
   legitimate, without assuming integrability at infinity first.

8. **Replicas and extraction keep their exact normalization.**
   The geometric local correction cancels the inverse factor at
   every prime of \(v\), with no coprimality condition on \(r,v\).
   The absolute double sum is finite. Distinct ideals \(v\) give
   distinct selected element rows \(rv^6\), and their count is
   \(J(Y_r(D))\asymp D^{h/6}\) for fixed \(r\). Jensen therefore
   leaves the exponent \(k+5h/6+e\). Weighted Hölder and the
   superpolynomial low-scale decay justify Mellin continuation.
   The fixed finite Euler corrections and Gaussian Mellin
   transform are nonzero for the relevant positive real parts.
   This gives exactly
   \(1/2+5h/(12k)+e/(2k)\), under the stated sampled moment.

## Limits retained in the accepted statement

The result is cofinal in the dyadic scale and uses one fixed detector.
Its finite number of observations at each scale is not a finite
verification of all scales. No upper bound for those arithmetic
observations was proved in this note. Constants need not be uniform
in \(k\). No zero-free region or critical-line conclusion is obtained
without the corresponding moment assumptions and character coverage.

No numerical fit or finite zero census enters this review. A small
exact-arithmetic diagnostic may check displayed exponent identities,
but does not authenticate the analytic lemmas reviewed above.
