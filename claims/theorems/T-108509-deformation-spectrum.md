# T-108509 — The deformation spectrum: every d=2 power defect is a canonical product of self-dual rank-2 local L-data

```text
Claim ID: T-108509
Status:   PROVED (Theorems 1-3; Theorem 3's odd case for ALL m by a
          supersingular-specialization argument; the even case's factor
          SIMPLICITY is machine-verified for m <= 10 and labelled as
          data beyond; elementary complete proofs, machine-verified two
          independent ways)
Created:  2026-08-31 (pass 3)
Programme: #764, axes A/B, question 9; generalizes T-108507 (m=3) to all
          m and closes the "obstruction-duality tower" question it posed
Depends on: T-108500 (rationality/degree/self-duality); T-108507 (m=3)
Proof:    standalone/2026-08-31-deformation-spectrum/PROOF.md
Machine:  matrix/c1_defect_atlas.py (symbolic, m=2..9, residual-zero) +
          experiments/X-108509-deformation-spectrum/ (stdlib replay, BM
          route independent of the coefficient formula)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

For the generic degree-2 local object (Satake `1 - aT + bT^2`) and every
`m >= 2`, the power-defect numerator `N_m` of T-108500 has the exact
normal form

```text
N_m(T) = (1 + b^{m/2} T)^eps * T^nu * M_m(b^m T + 1/T),
eps = [m even],  nu = floor((m-1)/2),
```

with a UNIQUE monic `M_m in Z[a,b][z]` of degree `nu` — the DEFORMATION
SPECTRUM POLYNOMIAL. Equivalently: the m-th power defect is
`det(1 - S_m T)` for a canonical rank-`(m-1)` self-dual "spectral
object" `S_m` = (rank-1 datum `-b^{m/2}` iff m even) `(+)` a direct sum
of `nu` RANK-2 SELF-DUAL LOCAL L-DATA of determinant `b^m` whose traces
are the roots of `M_m`.

Consequences (all proved):

1. `M_3 = z + 2ab`: the cube-defect bridge (T-108507) is the first case.
2. `M_4 = z + b(3a^2 - 2b)`: a previously unnamed m=4 bridge — the
   quartic defect is `(1 + b^2 T)` times ONE self-dual deformation.
3. Purity transfer at every m: the defect is pure iff every spectrum
   point is TEMPERED (`z_i` real, `z_i^2 <= 4 b^m`) — the bridge's
   stratification transfer holds for the whole family.
4. The tower invariants `D_m = disc_z M_m` (exact, machine-computed to
   m=9): `D_5 = a^2 b^2 (16a^4 - 48a^2b + 41b^2)` — the rank-5 ansatz
   invariant of matrix/layer_probes.json is now DERIVED, and the m=3
   bridge field generator `a^2 - b` recurs as a ramification factor of
   `D_7, D_8, D_9`.
5. m=5 splitting law: `N_5` splits over Q at an integer point iff `D_5`
   is a perfect square (192-point census 12/12 both directions; the
   quadratic-level equivalence is exact in the replay).

## Why this matters for #764

"Deformations obstruct each other" (T-108507) becomes quantitative and
total: the obstruction to the m-th pointwise power is a canonical
MULTISET of `floor((m-1)/2)` self-dual deformations — the spectrum of
the defect — with an explicit discriminant tower governing how the
spectrum degenerates and splits. Every question about defect purity,
splitting, or degeneration is now a question about `M_m`.
```
