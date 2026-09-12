# Attempt, outcome, and independent review priorities

## The actual objective

Prove a source-specific sign that rules out net production of off-central zeros
along PR #876's fixed-point homotopy, including collisions and boundary entry.
That sign would connect its zero-safe gamma endpoint to literal Xi. Neither
Laplace positivity nor a small response inverse already proves it.

## What was tried in this pass

1. Construct a gamma-adapted expansion for the WHOLE fixed-point family from the
   exact rational moment recursion.
2. Differentiate its coefficients at the Brownian endpoint and scout the
   resulting raw-root response using high-precision finite sums.
3. Check stability under a substantial increase of truncation order before
   promoting any apparent sign.
4. Establish a complete analytic source bound when the scout failed that test.
5. Examine the parameter endpoint's exact small-value density rather than
   assuming that all intermediate transforms are entire.

The scouts do not establish the attempted sign. Orders 1000 and 1500 disagree
strongly at moderate heights; see SCOUTING.md. An order-2500 job did not finish
and is not reported as a verification. No positive or negative native collision
coefficient is claimed.

## Completed proposed proofs

BLS1: every actual pair density q_theta satisfies
`integral q_theta^2/g <1500^2` in ONE fixed gamma reference measure, uniformly in
theta. The whole physical tail and small-x endpoint are included.

BLS2: complete Mellin expansion and explicit scalar coefficient-tail bound.
The proof supplies the test-space norm, all gamma/rate factors, and the common
holomorphic domain. It does not assert a pointwise density series or uniform
relative accuracy near zeros.

Section 4: a second exact triangular nonlinear coefficient recurrence. The
mean mode is prescribed, not inverted through its zero denominator. The beta
operator is diagonal; the W operator has signed off-diagonal entries. The
first such forcing is -7/32. A stable diagonal is not a positive spectral sign.

BLS3: uniform leading small-x asymptotic, exact pole residues, and the quadratic
residue limit at the Xi endpoint.

BLS4: a pair of simple real zeros outside the critical strip approaches those
poles. This is a parameter-asymptotic theorem with an unevaluated onset, NOT a
numerical root certificate and NOT an off-line zeta zero. In particular, an
entire pole-clearing multiplier cannot make the intermediate family globally
Lee–Yang, because it cannot cancel these existing zeros. This is a stronger-class
obstruction, not a refutation of critical-strip confinement.

## Load-bearing review questions

- Reconstruct the inherited order bounds and the exact mean/rate convention.
- Check the uniform multiplier density bound and both tilted inverse-moment
  bounds, then the one-factor use of q<=456000 x^(3/2)e^(-3x/2) in the L2 proof.
- Check scaled Laguerre orthogonality, completeness and the complex L2 pairing;
  no complex conjugation may change (-p)_j into (-conjugate p)_j in the final
  analytic series.
- Check the tail ratio, including the zero Pochhammer case and the condition
  N+1>=|p|^2+2Re p. The telescoping comparison must include every later index.
- Check the beta diagonalization and the shared W scaling in the independent
  coefficient recurrence. Degree-one normalization is essential.
- Check the uniform O(x^(5/2)) density remainder and its convolution, both
  residues of H, and the coefficient 1024/11907 multiplying pi^5.
- Check local uniform convergence AFTER pole subtraction, and Rouché on the
  fixed disks around -10 and 11. The zeros found there are outside the strip.
- Reject any purported final inference that a density L2 cap, rational moment
  recursion, or norm-convergent source representation establishes RH.

## A worthwhile next attempt, without presuming its outcome

Use the exact coefficient recurrence together with a sharper, independently
proved coefficient-response tail to form a real test of the collision formula.
A proof of the sign must exploit both double-zero constraints, not merely
replace a positive response measure by its absolute norm. Fixed-parameter
function-value certificates are possible with BLS2, but existence of successful
cofinal zero-confinement certificates is still a separate mathematical claim.

The packet does not assign that missing claim to reviewers as a routine lemma.
No statement here establishes that an endpoint zero-production bound is easier
than RH, nor that the project is a specified distance from completion.
