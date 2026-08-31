# Native theta sources can have off-central completed zeros

This is a corollary of two accepted analytic packets, not an additional
zero-search certificate or an external novelty claim. The implication was
independently checked against both complete parent proofs during pass 3.

## Frozen parents

- Fixed-weight divisor theorem: science
  `ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf`, reviewed at
  `0f29fd2d687c57402a14723dde2bc2b7e74fa317`;
  [proof](CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md), especially its protected
  denominator-zero and numerator-zero disks.
- Actual matrix theta source: science
  `fdd349dcf6ba1b104e27866ae66b4c89752d5f05`, reviewed at
  `8b2bb44f3b82059b6e3721aba9b2cff2a70fd7d0`;
  [proof](CUSP_MATRIX_PERIOD_POSITIVITY.md), including the unquotiented
  Mellin identity and inherited Petersson vacuum.

## Corollary and proof

Use the fixed-weight packet's weight-24 basis `(g,b)`, where `b=Delta^2`,
and its normalized Hecke eigenforms. Put

    delta = 24 sqrt(144169),
    A(s) = pi^(-s) Gamma(s) (4 pi)^(-s-23) Gamma(s+23),
    H(s) = Z(s)[S_+(s)+S_-(s)] - 2 C(s),
    N(s) = Z(s)^2 S_+(s) S_-(s) - C(s)^2.

The exact completed-period identities in that packet are

    I_s(b,b)          = A(s) H(s) / delta^2,
    det I_(g,b)(s)    = A(s)^2 N(s) / delta^2,
    Q_1(s)           = A(s) N(s) / H(s).

The factor `A(s)` is holomorphic and nonzero in `Re s>1`. The protected
pole disks for `Q_1` contain zeros of `H` and no zeros of `N`; the protected
zero disks contain zeros of `N` and no zeros of `H`. The theorem gives
separately at least `c_P T` and `c_Z T` distinct such zeros, for large `T`,
in every fixed substrip `1<sigma_1<sigma_2<=1+eta` of its near-1 region.
Consequently the first disks give genuine zeros of `I_s(b,b)`, and the
second give genuine zeros of the full completed period determinant.

Now apply the actual-source construction with the one-dimensional space
`V=span(b)` and no quotient (`W=0`). Its completed observation is exactly
`L_V(s)=I_s(b,b)`, with the literal positive Petersson vacuum. It has the
smooth, strictly positive reciprocal theta source and positive Mellin
feature kernel supplied by that theorem. Its pole-cleared function
`s(s-1)L_V(s)` is entire and retains all the stated zeros in `Re s>1`.
Reflection supplies the reflected off-central zeros as well.

## Exact scope

- `Delta^2` is a genuine cusp form but not a Hecke eigenform: its first
  Fourier coefficient is zero while its second is nonzero.
- Restriction to `span(b)` BEFORE completion is not the pointwise source
  Schur quotient of the full two-dimensional source. This corollary does
  not settle the zero geometry of that proper quotient.
- The near-1 width, onset and positive counting constants are inherited
  from the fixed-weight theorem and are not effective here. No zero
  simplicity, complete zero census or certified individual ordinate is
  asserted.
- No scalar Euler product, new automorphic lift, RH counterexample or
  general scattering normalization is claimed. The determinant statement
  is not an eigenvalue-by-eigenvalue matrix-zero classification.

The precise selection failure is therefore stronger than the synthetic
positive-source example: positive reciprocal source structure and an
actual modular period origin still do not force critical-line zeros.
Additional arithmetic compatibility must be specified and proved; it
cannot be inferred from those properties alone.
