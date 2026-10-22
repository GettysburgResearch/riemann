# M-105100 — Hostile review contract for the second-residue ledger

Claim ID: M-105100

Status: **REVIEW METHODOLOGY**

Created: 2026-08-23

RH status: **unproved**

Reject T-105100 if any item below fails.

## Algebra

- Q is exactly \(p^2/(p'p'')\), not \(p/(p'p'')\).
- A zero of \(p'\) contributes \((p/p'')^2\).
- A zero of \(p''\) contributes \(p^2/(p'p''')\); it is not discarded.
- The coefficient extracted at infinity is the coefficient of \(z^{-1}\).
- Root moments are centered before the \(V_2,V_4\) formula is used.
- The formula is tested away from the even and centered special cases.

## Coverage

- Every zero of \(p'\) and \(p''\) is included with multiplicity one under the
  claim's simplicity hypotheses.
- Repeated critical points are outside the claim, not silently perturbed.
- For real p, nonreal \(p'\)-zeros remain as an algebraic conjugate-pair
  correction.
- Squared algebraic residues at nonreal points are not replaced by absolute
  squares.

## Continuation boundary

- The finite identity is not called an entire-function theorem.
- The global all-critical-point sum is not called a height-truncated Xi
  identity.
- A localization theorem must retain exterior residues, window-boundary terms,
  and the order of truncation/height limits.
- Canonical-product exhaustion must justify convergence of the root ledger and
  both residue sums.
- No sign is assigned to the off-real correction or second-level debt without
  a new theorem.
- The PR #720 context is identified as post-freeze, draft, and unreviewed.

## Scientific status

These fields must remain false:

    canonical_product_limit_proved
    height_localization_proved
    off_real_correction_controlled
    second_level_debt_controlled
    rcmv104530_proved
    rh_established

No exact fixture, finite polynomial identity, or root-moment asymptotic proves
RCMV104530 or RH.
