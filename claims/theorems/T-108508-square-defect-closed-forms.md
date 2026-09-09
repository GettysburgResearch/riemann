# T-108508 — Closed forms for the pointwise-square defect at ranks ≤ 5, with the correction-layer structure

```text
Claim ID: T-108508
Status:   PROVED for ranks 2-5 (each closed form is a polynomial identity
          in free variables e_1..e_d, established by exact symbolic
          expansion — a complete finite proof — and cross-checked at exact
          integer instantiations); the general-rank law is OPEN with the
          layer pattern deposited as machine-verified structure
Created:  2026-08-31 (continuation pass; resolves the open problem posed
          by O-108505's rank-4 refutation)
Programme: #764, research modes 1/3
Depends on: T-108500 (coefficient formula), O-108505 (witnesses)
Machine proofs: research/exploratory/2026-08-30-two-programme-pass/matrix/
          rank4_hunt.py + rank4_hunt.json (rank 4, symbolic),
          rank5_symbolic.py + rank5_symbolic.json (rank 5, symbolic),
          rank5_probe.py + rank5_probe.json (instantiation cross-checks);
          instantiation replay: experiments/X-108505-rank-uniform-defects/
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement

For the generic degree-`d` local object with elementary symmetric data
`e_1, ..., e_d`, write the pointwise-square defect as

```text
sum_k h_k^2 T^k = N_{2,d}(T) / det(1 - Sym^2(A) T),   deg N_{2,d} = C(d,2),
```

and let `G_d(T) := sum_j (-1)^{j(j-1)/2} e_j(Ext^2 A) T^j` be the
Gauss-sign exterior-square polynomial. Then, as PROVED polynomial
identities:

```text
d = 2:  N = G_2                                   ( = 1 + e2 T )
d = 3:  N = G_3
d = 4:  N = G_4 + 2 e4 h2 T^3 - 2 e4^2 e2 T^5
d = 5:  N = G_5 + 2 (e4 h2 - e5 h1) T^3
              - 2 e5 h3 T^4
              - 2 (e1^2 e3 e5 - 2 e1 e4 e5 - 2 e2 e3 e5 + e2 e4^2 + 2 e5^2) T^5
              - 2 e5 (e1^2 e5 - e1 e2 e4 + e3 e4) T^6
              - 2 e5 (e1 e3 e5 - e1 e4^2 + e4 e5) T^7
              + 2 e5^2 (e1 e5 - e2 e4) T^8
              + 2 e5^4 T^10
```

(`h_k` = complete homogeneous in the inverse roots: `h_1 = e_1`,
`h_2 = e_1^2 - e_2`, `h_3 = e_1^3 - 2 e_1 e_2 + e_3`).

## Structure observed (machine-verified; general law OPEN)

1. **Corrections are graded by the deep elementaries**: every correction
   term carries `e_4` or `e_5`; ranks 2-3 (no `e_4`) have none. The
   mechanism identified at rank 4 — disjoint-pair weight products
   `x_i x_j · x_k x_l` hitting the CONSTANT `e_4` (the three perfect
   matchings; the `Ext^2 x Ext^2 -> det` pairing) — is the first layer;
   rank 5 adds `e_5`-layers with non-constant resonances.
2. **The `h`-pattern of the first layers**:
   `corr_3 = 2(e_4 h_2 - e_5 h_1)` and `corr_4 = -2 e_5 h_3` — complete
   homogeneous polynomials paired against deep elementaries with
   alternating signs; the continuation
   `corr_3(d) = 2 sum_{i>=4} (-1)^i e_i h_{6-i}` is now CONFIRMED at
   rank 6 by exact instantiation (five for five, including `e_6 h_0`
   terms: matrix/layer_probes.json) — proved at ranks 4-5, exact-verified
   at rank 6, general d OPEN.
3. **Top-coefficient sign law, proved for d <= 5**:
   `N_{2,d}` has top coefficient `(-1)^{(d-1)(d-2)/2} (det A)^{d-1}` —
   the Gauss-sign prediction is corrected at the top exactly when
   `d ≡ 1 (mod 4)`-type parity flips it (d = 5: `+e_5^4` vs predicted
   `-e_5^4`). **Pass-3 addendum (2026-08-31): now proved for ALL d** by
   T-108510 (defect codimension law), whose reciprocity argument gives
   `c_top(N_{2,d}) = (-1)^{C(d-1,2)} e_d^{d-1}` directly (the two sign
   forms agree; exponents differ by the even number 2d); the same law
   proves `deg N_{m,d} = C(d+m-1,m) - d` for every m, d.
4. Degeneration loci (reduced denominators) occur at special
   instantiations and are recorded, consistent with T-108500(5).

## Pass-3 continuation addendum (2026-08-31): the general-d law is CLOSED

T-108522 (standalone/2026-08-31-alternant-defect/) proves the closed
alternant form

```text
N_{2,d}(T) = sum_j x_j^{d-1} prod_{a != j}(1 - x_a^2 T)
             prod_{a<b != j}(1 - x_a x_b T) / prod_{a != j}(x_j - x_a)
```

for EVERY rank d (symbolically equal to the d = 3, 4 forms above;
integer-point-verified at d = 5, 6, 7). The correction-layer
structure of this claim is the expansion of that alternant minus the
Gauss-sign polynomial; the OPEN general-d problem posed here is
resolved.

## Method note (why "symbolic expansion" is a proof)

Each identity is an equality of polynomials in the free variables
`e_1..e_d` and `T`; verifying it by exact expansion over `Z[e_1..e_d][T]`
(sympy 1.14.0, with the tail-vanishing through the certified window and
stdlib Fraction instantiation cross-checks as an independent route) is a
complete proof, not evidence. The OPEN part is the general-`d` law, for
which ranks 4-5 are now data points with proved closed forms.
```
