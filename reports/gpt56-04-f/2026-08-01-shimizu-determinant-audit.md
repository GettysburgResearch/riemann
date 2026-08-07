# Audit and recovery of the July 2026 Shimizu determinant claim

## Source

Yoshinori Shimizu, *Proof of the Riemann Hypothesis*, version 8, submitted
2026-07-01 and posted 2026-07-03 on Preprints.org. The version is explicitly
non-peer-reviewed. An older Zenodo revision carries a fatal-error disclaimer;
this audit does not infer that the revised version is wrong merely from the old
disclaimer.

## Accepted core

The following operator theory is correct:

```text
K=K* in S2
 -> det_2(I+iwK) entire
 -> zeros w=i/lambda_j
 -> exact trace-moment expansion
 -> finite-rank S2 limits preserve det_2 and every trace power m>=2.
```

If the resulting determinant is exactly `xi(1/2+w)`, RH follows. Conversely RH
constructs such a paired diagonal model. The exact target identity is therefore
RH-equivalent, not a soft consequence of having built some self-adjoint compact
operator.

## Load-bearing gap

The manuscript's central comparison must prove, for every order `m>=2`, that the
classical finite-part coefficient equals `Tr(K_M^m)`, that every residual factor
is annihilated, and that the limits/infinite series may be interchanged.

The text states this architecture but does not isolate an independently
reconstructible theorem carrying all those conclusions. Passing to a canonical
representative modulo a residual subspace is a linear operation; determinant
moments are nonlinear cyclic tensor functionals. The quotient argument needs a
separate tensor-ideal annihilation theorem.

Thus the recovered paper is a conditional theorem:

```text
self-adjoint S2 construction
+ complete all-order arithmetic/determinant moment match
+ analytic majorant
=> det_2 identity
=> RH.
```

The second line remains unproved.

## Amendments pushed

- `L-15128`: exact determinant calculus, moment gates, and RH equivalence;
- `R-15106`: central-comparison/moment-gap audit;
- `T-15109`: proof-producing recovery theorem;
- `X-15111`: Fraction-only finite moment/Hankel checker.

## Relation to PR #158

The all-order moment defect is another representation of the complete signed
arithmetic residual. Under false RH the off-line cardinal block must appear in
one of them. Neither can be eliminated by a finite verified height or a
phase-blind tail.

No proof of RH is claimed.
