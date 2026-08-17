# L-97403 — Exact scope of the compact-plus-MPFR Target–Lorenz certificate

Claim ID: `L-97403`  
Status: **RECONSTRUCTED CERTIFICATE CONTRACT; GLOBAL PARITY COMPENSATION EXCLUDED**  
Created: 2026-08-18  
Frozen source: PR #550 at `20646a78c3e8843001cb49ea0c9741f6d0d446f7`

For canonical terminal parameters

`p>=67`, `1<=y<67`, `2<=j<=66`,

let `Theta_j(p,y)` be the proportional determinant controlling the canonical Target–Lorenz row margin. The frozen stack partitions the domain as follows.

## Compact sector

For `py<166000`, the compact theorem works cell by cell in the real `(p,y)` parameter plane. Activation boundaries are formed by exact algebraic equalities in the source arguments. The proof must include both one-sided cell limits and all boundary cases. It establishes `Theta_j(p,y)>=0` in canonical orientation.

## Tail sector

For `py>=166000`, the repaired verifier uses MPFR 4.2.2 at 256 bits. Primitive square roots and logarithms are enclosed with directed RNDD/RNDU rounding; all later interval operations are outward. The event order is exact integer arithmetic. The campaign covers all 65 rows and the complete event census, with strict lower bound

`Theta_j(p,y)>26.7858198871370094575061`.

The compact and tail domains are disjoint and exhaustive; the boundary `py=166000` belongs to the tail.

## What the certificate proves

In canonical parity, the leftmost even Target–Lorenz submeasure of the complete grouped `P_61` source has nonnegative row margins for every row `2<=j<=66`. One coefficient vector is used in target and every certified row. Rows above 66 vanish by support.

## What it does not prove

1. It does not make the canonical orientation valid after an odd rough history.
2. It does not prove global target capacity after completed parity expansion.
3. It does not prove the scalar Lorenz inequality `CPSL67`.
4. It does not justify colorwise terminalization.
5. It does not turn target/scalar TP2 into global Hall.

The explicit witness `X=61841`, history `(67)`, terminal `(71,13)` is inside the compact domain but requires the reversed target orientation. The certificate is true at its stated canonical scope and unavailable at that leaf in isolation.

The finite certificate is therefore a valid local input to a global completed-parity LP, not a substitute for that LP’s uniform feasibility theorem.
