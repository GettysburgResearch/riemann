# M-105108 — Review contract for Green–Gram selector conditioning

Claim ID: M-105108

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105105; L-105107; L-105108

RH status: **unproved**

## Green and local-normalization checks

- The positive convention is \(g_\Omega=-\log\rho_\Omega\), with no
  historical factor two.
- The conformal-radius exponent is exactly \(d_c-1\).
- A nontarget contributes exponent \(d_a\) to \(|y_c|\); another target
  contributes only \(d_a-1\).
- The potential formula is the exact selector norm only for one target.
- Complex phases of \(\beta_c\), \(y_c\), and off-diagonal Pick entries may
  not be discarded.
- Under a coordinate change the jet coefficient transforms together with
  the conformal radius; dimensional covariance may not be asserted from the
  radius alone.

## Gram and interpolation checks

- Use the normalized Szegő Gram matrix, not the radially polluted raw Pick
  kernel condition number.
- The exact joint operator is
  \(G^{-1/2}D_yG^{1/2}\); \(Y\sqrt{\kappa(G)}\) is an upper bound.
- Ill-conditioning of \(G\) alone does not force the actual data norm to
  grow.  Constant data have optimum \(Y\) for every target geometry.
- Opposite-phase two-target data attain the condition-number upper bound, so
  the factor cannot be removed for uniform arbitrary-data control.
- The centered spectral and cardinal envelopes must retain their constant
  term \(|\eta|\).
- \(\delta_c\) contains targets only.  Full-event nontarget contributions
  are already embedded in \(|y_c|\).
- Dividing by \(\delta_c\) raises other-target exponents from \(d_a-1\) to
  \(d_a\); this produces an upper envelope, not an equality.
- Product separation, diagonal dominance, and pair thresholds are finite
  sufficient or necessary tests.  None replaces the full Pick matrix.

## Domain and boundary checks

- Fixed-data domain enlargement is adverse or neutral by restriction.
- The exact monotonicity ratio and Euclidean sandwich are single-target
  statements unless explicitly proved otherwise.
- A comparison across windows with newly added events is a different
  interpolation problem and is not covered by fixed-manifest monotonicity.
- The interior Green theorem does not require boundary rectifiability; the
  contour residue bridge does.
- The extremal remains constant-modulus on the full boundary, so harmonic
  measure alone does not improve an individual-edge supremum bound.
- Exterior poles of a rational disk extremal must still be rechecked after a
  window change.

## Exact-fixture checks

- At nodes \(\pm1/2\), values \((2,2)\) and \((-2,2)\) have the same
  magnitudes and geometry but norms \(2\) and \(4\).
- With targets \(\pm1/5\), a simple nontarget at zero, and equal target
  data one, the forced values are \((-5,5)\) and the optimum is \(25\), not
  the diagonal load \(5\) or the cardinal envelope \(26\).
- For \((-1/2,0,1/2)\), values \((-1,1,-1)\), every pair threshold is at
  most \(2+\sqrt3\), while the full threshold is \(4+\sqrt{15}\).
- In \(B(0,R)\), for \(R>1/2\), the stated order-two
  target/order-two nontarget fixture has norm \(4R^3\).
- For integers \(n\ge2\), \(m\ge1\), a nontarget of order \(m\) at
  \(1/n\) forces norm \(n^m\) in the unit disk.

## Prior-art and scope firewall

- Historical annular Green claims are unintegrated, use a different
  normalization, and are not dependencies.
- Accepted actual-Xi Pick matrices concern a different kernel.
- Historical L-91014 is ID-colliding/unintegrated; L-92302 is quarantined.
- No Xi manifest, rectangle conformal certificate, cofinal Green or Gram
  estimate, quotient edge decay, multiplicity-defect estimate, strict
  coherence margin, RCMV104530, or RH conclusion follows.
