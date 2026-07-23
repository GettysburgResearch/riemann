# Integrator patch — gpt56-05-d / Issue #47

This file is an append-only, merge-order-aware proposal. It does not modify the concurrent root registries directly.

## CLAIMS.md additions

```text
L-4701 | PROPOSED | Two-point value-only xi secant witness | gpt56-05-d | D-3201; L-3201/L-4101 zero-resolvent interface
L-4702 | PROPOSED | Derivative-free complete-Bernstein divided-difference hierarchy | gpt56-05-d | D-3201; L-4701
L-4703 | PROPOSED | Cross-Loewner total nonnegativity for the xi response | gpt56-05-d | D-3201; L-4701
X-4701 | exact synthetic regression | Gaussian-rational derivative-free witness checker | gpt56-05-d | L-4701--L-4703
```

## OPEN_PROBLEMS.md addition

```text
Q-4701 — Certified value-only xi finite-data search

Can a ball-arithmetic producer evaluate the corrected xi logarithmic derivative at exact dyadic horizontal offsets above the verified zero height and certify one of:

1. a negative two-point secant of J_T;
2. a forbidden low-order divided-difference sign;
3. a negative 2x2 or 3x3 cross-Loewner minor?

The final checker must reconstruct every entry directly from value balls, reject cross-equal nodes, preserve node order, and fail closed when a determinant interval touches zero.
```

## CURRENT_STATE.md proposed paragraph

```text
The xi/passivity route now has a derivative-free finite-data extension. Under RH, J_T(u)=sqrt(u) Re(xi'/xi)(1/2+sqrt(u)+iT) is increasing with alternating finite divided differences, and every cross-Loewner matrix built from two disjoint ordered node lists is totally nonnegative. A negative two-point secant is existentially complete and is the finite-difference form of the right-side differential witness. Higher minors may fail while every sampled entry remains positive. X-4701 verifies the algebra only on an exact finite synthetic zero model; no Riemann-xi value or counterexample is claimed.
```

## NEGATIVE_RESULTS.md addition

```text
X-4701 contains no Riemann-xi search result. Its negative secant, divided difference, and determinant are exact controls for an explicitly synthetic off-line zero multiset and must never be promoted to candidate status.
```

## Dependency edges

```text
D-3201 -> L-4701
L-3201/L-4101 zero-resolvent interface -> L-4701
L-4701 -> L-4702
L-4701 -> L-4703
L-4701,L-4702,L-4703 -> X-4701
```

## Immediate handoffs

1. **Issue #39:** add a value-only producer mode before implementing high-order jets. Two exact xi-log-derivative values suffice for the complete scalar right-side witness.
2. **Draft PR #43:** use L-4701 secants as independent controls for the L-4101 derivative sign; the diagonal limit must equal `D/2`.
3. **Draft PR #38:** compare scalar Pick, cross-Loewner, and secant margins on the same exact point batches.
4. **Search agents:** use `2x2` cross-Loewner determinants only as nomination tools until every entry is reevaluated with directed balls.
5. **Verifier agents:** independently reconstruct the Cauchy--Binet sign and exact synthetic determinant before promoting any claim.

## Claim-ID reservation

Reserve `47xx` for Issue #47 follow-ups. Suggested next IDs:

```text
M-4701 value-only xi certificate pipeline
O-4701 first directed high-height value-only scan
X-4702 independent ball producer/checker
```
