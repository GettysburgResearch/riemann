# Exact sources and boundaries

## Repository inputs

* PR #803, parent 4370ed19eb7b2630602740468cd9ecbaa870d848,
  `standalone/2026-09-06-logarithmic-core/PROOF.md`, Git blob
  f7420d1ddf603a3765331649d3f5b9d04f23e8e7. Entire proof read locally from the
  supplied archive and authenticated by its Git blob. The effective-form
  definition is used by WP2. WP1 does not depend on the parent's operator-core,
  strong-residual, or conditional strictness claims.
* PR #792, source head465cb28ed8cbfa1bb071d9a85eeda9890decfe6b,
  `standalone/2026-09-05-bernstein-chebyshev-growth/energy-schur-reduction/PROOF.md`,
  Git blob0d12ff6039dcc79f6576538edeebd2a0c5b539c0; and
  `finite-window-coercivity/PROOF.md`, blob35d8d38a77bee896b0b2e729b095ccdef5d7a50f.
  Their exact kernel and effective form are preserved. Their positive-sector
  estimates are not silently promoted to whole-window signs.
* Policy baseline main051808c1f8367b4320c52f94b40908eb2173d622. AGENTS.md was
  freshly read; no main, formal, review, or original source changes are made.

## Classical analytic inputs

1. NIST DLMF5.11.2 and5.11(ii), https://dlmf.nist.gov/5.11 . The page was read,
   including the explicit complex secant remainder bound. It justifies the
   bound(14) of PROOF.md after19 Bernoulli terms and64 shifts. The asymptotic
   notation alone would not justify a certified interval.
2. The Euler--Maclaurin zeta expansion with periodic Bernoulli remainder;
   see DLMF25.2, https://dlmf.nist.gov/25.2 . Its differentiated finite
   expression and the Cauchy-circle remainder bound are derived in PROOF.md.
3. The standard Euler product and logarithmic derivative for Re(s)>1,
   the identity zeta(2)=pi^2/6, and ordinary Fourier completeness/Parseval
   on a circle. No critical-line or zero-counting theorem is used.

## Prior art and novelty

Local Weil positivity, positive-definite extensions, spectral-mixture
certificates, and finite-window methods are established subjects. A current
search also surfaced arXiv2608.24827, with a larger reported window for a
related Weil form. Only search-indexed abstract metadata was available in this
pass; an attempted primary abstract-page fetch failed. That paper's proof,
code, window normalization, and numerical claims were NOT audited or imported.
No largest-window, first-local-positivity, or external novelty claim is made.
The present object is a self-contained source-specific length-one extension
certificate in the exact #792 compact-resolvent normalization.

## Discovery versus proof

Exploration used SciPy linear programming with ordinary floating point and
mpmath approximations of the first40 zero ordinates. Twenty rounded rational
frequencies were retained, along with nonnegative rational weights and64
rational spline values. Those numbers are free witness parameters, NOT claimed
zeta values or zero certificates. They are fully recorded in certificate.json.
The optimization solves positivity inequalities for the periodic remainder's
first2049 cosine coefficients, maximizing a common scaled margin. Its success
is not an input to acceptance. Rounding or optimizer errors are exposed by
verify.py, which reconstructs everything from the arithmetic source.

All discovery calls are excluded from the proof dependencies. Neither SciPy,
mpmath, floating point, an optimizer, a zero table, nor any upstream producer
is imported by the accepting scripts. Python integer/Fraction arithmetic,
the published analytic identities and the supplied coverage argument are the
trust boundary. Independent review remains required.
