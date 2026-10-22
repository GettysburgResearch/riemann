# M-105107 — Review contract for boundary-optimal selectors

Claim ID: M-105107

Status: **HOSTILE REVIEW CONTRACT**

Created: 2026-08-23

Depends on: L-105103; L-105105; L-105106; L-105107

RH status: **unproved**

## Forced zeros

- Actual post-cancellation orders are used.
- Nontarget exponent is \(d_a\); target exponent is \(d_c-1\).
- Other targets enter each forced product with exponent \(d_a-1\).
- The target normalization retains \(b_c'(c)^{d_c-1}\).
- Omitting the self derivative, using target exponent \(d_c\), or reducing a
  nontarget exponent must fail an exact local congruence.
- Dividing by the forced inner function leaves ordinary target values, not a
  new confluent derivative problem.

## Pick optimum

- The complete Pick matrix is
  \((u^2-y_j\overline y_k)/(1-c_j\overline c_k)\).
- Diagonal inequalities, entrywise positivity, determinant alone for larger
  matrices, or another Xi Pick kernel are insufficient.
- The optimum is the first \(u\) for which the full Hermitian matrix is
  positive semidefinite.
- The singular extremal and its finite-inner degree are scoped to the finite
  classical Pick problem.
- The selector is optimal for \(\|W\|_\infty\), not automatically for
  \(\|Wh\|_\infty\).

## Window transport

- General-window target normalization includes both \(\phi'(c)\) and every
  mapped Blaschke product.
- Jordan continuity is distinguished from holomorphic extension through the
  boundary.
- Rectangle corners are handled by the rectifiable-Jordan contour theorem;
  analytic continuation through a corner is not inferred.
- Conjugation and parity require the full manifest and data compatibility.
- Averaging a nonextremal solution need not preserve innerness.
- Reflected rational poles are authenticated against each current window and
  may not be ignored under later enlargement.

## Prior-art firewall

- Accepted actual-Xi Pick claims through order three concern a different
  kernel and are context only.
- PR #720 L-104502 explicitly warns that diagonal or other-kernel positivity
  does not prove the required Pick positivity.
- The proposed historical local-Pick L-91014 collides by ID with a different
  accepted main claim and is not a dependency.
- Quarantined L-92302 supplies no growing-order estimate.
- The classical finite Nevanlinna–Pick theorem is stated locally rather than
  attributed to an unintegrated repository claim.

## Scope firewall

- Fixed-window optimality is not a cofinal Xi norm bound.
- No Xi manifest, conformal-coordinate certificate, growing Pick-eigenvalue
  estimate, quotient edge bound, or cofinal passage is inferred.
- No multiplicity-defect estimate, strict coherence margin, RCMV104530, or RH
  conclusion follows.
