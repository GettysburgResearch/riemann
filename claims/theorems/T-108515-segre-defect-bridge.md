# T-108515 — The Segre bridge: the powered-coefficient defect is the K-polynomial cofactor of the Segre embedding of (P^1)^m

```text
Claim ID: T-108515
Status:   PROVED (Theorem 1 for all m; Theorem 2 = exact machine
          computation of the m = 3 equivariant Betti table; Theorem 3
          = geometric second proof of the defect functional equation
          with one labelled classical import; Corollaries 1-2), with
          the general-rank Lascoux identification DEPOSITED, not
          claimed
Created:  2026-08-31 (pass 3 continuation, Lane 1 of the six-hour
          plan; realizes Priority 1 of the external programme review,
          proved independently of its sketch)
Programme: #764 (Generalized L-Objects) with #763 mechanism reading
Depends on: T-108500 (statements (1), (3)), T-108508 (Corollary 2)
Proof:    standalone/2026-08-31-segre-defect-bridge/PROOF.md
Replay:   experiments/X-108515-segre-bridge/ (stdlib, EXACT_RATIONAL,
          all green incl. python3 -O)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          segre_coarse_check.py (symbolic m <= 4), segre3_betti.py +
          .json (the Betti table), segre_rank3_check.py (held-out)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary; the standalone file is authoritative)

Let `R_m = (+)_r (Sym^r V)^{tensor m}` be the Segre ring of `(P^1)^m`
(dim V = 2, generic `A` with trace `a`, det `b`). Then:

1. **Hilbert identification**: `Hilb_{R_m}(A; T) = sum_r h_r^m T^r` —
   the powered-coefficient series of T-108500 IS the equivariant
   Hilbert series of the Segre ring.
2. **Coarse bridge (all m)**: the equivariant K-polynomial factors as
   `K_m = N_m(T) * prod_{k>=1} det(1 - Sym^{m-2k}(A) b^k T)^{c_k}`,
   `c_k = C(m,k) - C(m,k-1)`: the defect numerator is the Segre
   K-polynomial divided by explicit lower-plethysm-strand factors.
3. **Fine bridge (m = 3)**: the full equivariant Betti table of the
   2x2x2 Segre is `C; 3 det^2 Sym^2 @ 2; (2 det^3 Sym^3 + 4 det^4
   Sym^1) @ 3; 3 det^5 Sym^2 @ 4; det^9 @ 6` — exactly
   `det^9`-self-dual — and reassembles to
   `K_3 = N_3 * det(1 - A b T)^2` with `N_3 = 1 + 2abT + b^3 T^2`:
   the cube-bridge defect recovered from syzygy characters alone.
4. **Geometric second proof of the defect functional equation
   T-108500(3)**: `R_m` is the normal toric ring of the unit m-cube
   (explicit saturation), its interior ideal is a `b^m T^2`-shift of
   itself ([-1,1]^m reflexive, `omega = b^m R(-2)`), and Stanley
   reciprocity (IMPORTED_THEOREM) then forces
   `N_m(T) = b^{m(m-1)/2} T^{m-1} N_m(1/(b^m T))`. The self-duality
   of the obstruction IS Gorenstein duality of the cube.
5. **Eulerian specialization**: `N_m(2, 1) = A_m(T)`, the Eulerian
   polynomial — the defect is a two-parameter GL_2-equivariant
   deformation of the Eulerian polynomial, and its FE deforms
   Eulerian palindromy.
6. **Held-out rank-3 corollary**: for dim V = d, m = 2:
   `K_{2,d} = N_{2,d} * det(1 - Lambda^2(A) T)`; at d = 3 this was
   predicted then machine-verified against T-108508's `N_{2,3} = G_3`,
   and at d = 4 verified against the correction-layered
   `N_{2,4} = G_4 + 2 e_4 h_2 T^3 - 2 e_4^2 e_2 T^5` (X-108515 V5).
   Deposited direction: read T-108508's correction layers off the
   Lascoux resolution strands of `P^{d-1} x P^{d-1}`.

## Why it matters for #763/#764

The defect `N_m` was born analytic (the obstruction to pointwise
transforms surviving as L-objects). This theorem gives it a second,
independent life as GEOMETRY: a syzygy character sum of a Gorenstein
toric variety, with the functional equation supplied by cube
reflexivity rather than coefficient combinatorics. Every defect
structure found this pass (spectrum polynomials T-108509, codimension
law T-108510, torsion resonances T-108513) now sits over a named
geometric object, and the mechanism-transfer questions of #763 gain a
third world (analytic / spectral / toric-geometric) with exact
dictionaries between them.
```
