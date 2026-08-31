# Pass-4 early checkpoint: cusp spectrum, moving roots, and chain maps

Status: reviewed checkpoint, closed early at the user's request.  No new
automorphic L-function, critical-line theorem, or RH/GRH conclusion.

## Native cusp-period theory

The K/P/G/L sequence now gives one coherent mesoscopic theory for the full
level-one completed Eisenstein period operator:

- the finite-part eigenvalues satisfy the leading law `k/(24J)` for
  `J=o(k)`;
- the regularized determinant converges on fixed compact endpoint scales to
  the reciprocal-Gamma model;
- `CUSP_LOGARITHMIC_SPECTRAL_REFINEMENT.md` locates every growing eigenvalue
  within a fixed absolute band around
  `m_(k,J)=(k-1)/(24J)-log((k-1)/(4*pi*J))/2+c_0`;
- `CUSP_SUBSQRT_SHARP_SPECTRUM.md` removes that final band and proves
  `lambda_J=m_(k,J)+o(1)` throughout `J=o(sqrt(k))`;
- `CUSP_GROWING_SIMPLE_PERIOD_ROOTS.md` proves that the exact full period
  determinant has one real positive simple root near `12j/k`, simultaneously
  for every `j<=J_k` with `J_k^3 log(k)=o(k)`.

The root theorem is for the full determinant.  It does not prove survival in
a scalar flag quotient, nested-quotient interlacing, or the fine fixed-depth
displacement.

## Structural synthesis

The accepted Segre/Hadamard/Koszul work remains the honest source above the
universal recurrence numerator: scalar alternants and palindromy are Euler
shadows, not purity.  This pass targets the missing chain maps rather than
another scalar factorization.  Any frozen transgression packet included next
to this checkpoint is finite characteristic-zero algebra and must retain its
own exact-SHA review; it supplies no automorphy or spectral positivity.

## Exact frontier

- Improve the exact-period remainder, not merely the finite-part spectrum, to
  obtain a fine moving-root correction.
- Prove or refute scalar quotient noncancellation in a growing-depth range.
- Compress explicit Segre/Chow transgressions into a uniform
  representation-theoretic construction.
- Supply a polarized arithmetic/archimedean realization; additive Tor
  characters alone cannot do so.

The finite cusp fixtures are directed-ball controls with pinned runtime and
source seals.  They support normalization and finite inequalities only; the
asymptotic theorems are proved analytically.
