# Review and source boundary

1. Check DC-1 with inner products conjugate-linear in the first variable.
   D_N-C_N, not C_N, is the positive matrix. All prime powers contribute,
   including powers of the same prime. The diagonal log j uses the exact
   identity sum_(n|j)Lambda(n)=log j.
2. Check the real-x factorial estimates for M(x). The upper constant 3 comes
   from an elementary dyadic Chebyshev bound, not a PNT asymptotic. The
   asymptotic lambda_max=log N+O(1) is independently bounded on both sides.
3. The application switches explicitly to #792's T. Verify W normalization,
   both signs in the full zero representation, and the factor 3/2 in the form.
   The source-only H bound is used for a coarse W bound, not to infer RH.
4. Check the singular local triangle decomposition. W'' has an integrable
   positive weighted contribution uW''(u) at zero, not a finite curvature
   measure on an interval containing zero. Cross cells are separated from zero.
5. Check ALL potential cross-cell knots: the integer nj-i is forced to zero
   by 2N ell_N<1. The cusp contributes an overlap integral at s=t with a
   minus sign after the two integrations by parts. No knot is discarded.
6. The all-N positive result has zero DAMPED mean in EACH interval. It is
   not positivity for arbitrary f supported on the union, and the sets shrink
   in measure. The negative-index upper bound is only N, not zero.
7. The original pass9 arithmetic approximation remains valid but cannot
   supply the window-mass sign from a bound on its approximation error.

Exact repository inputs are in SOURCE_LOCK.json. The #792 proof text was
read through its arithmetic, curvature, gluing and scope arguments. This is
not an independent verdict on every ancestor or on its interval implementation;
none of its finite positivity certificates are imported by DC-3. The local
coercivity used here is rederived with deliberately coarse constants.

Classical background: weighted graph Laplacian sums of squares, elementary
Chebyshev estimates, Laplace/Fourier uniqueness and convex triangle kernels.
For a general graph-Laplacian reference see Spielman--Teng, arXiv:0808.4134;
its theorems are not dependencies of the elementary proof here. A web search
also surfaced further Weil-positivity manuscripts, but no unreviewed claimed
RH proof or numerical window result was used. No external novelty or priority
assessment is claimed.

The completion attempt is retained in PROOF.md Section 8. In particular,
one must not delete the mean/primitive cross terms or identify the divisor
Laplacian with the full source without a proved map. No such map is supplied.
