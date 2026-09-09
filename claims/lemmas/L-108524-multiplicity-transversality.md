# L-108524 — The multiplicity law's interior term is transversal branch counting: a conditional theorem with machine certificates

```text
Claim ID: L-108524
Status:   PROVED (the conditional theorem: three explicitly checkable
          hypotheses imply O-108523's interior multiplicity term
          exactly), with the hypotheses MACHINE-CERTIFIED in exact
          arithmetic at seven full cells — the a = 0 tower m = 5, 7,
          9, 11, 13 and the golden point a^2 - a - 1 at m = 11, 13 —
          which are therefore proved-by-mechanism cells of O-108523.
          The general law remains reduced to (i) uniform separability
          of the associated polynomials and (ii) the boundary-class
          mechanism (both deposited).
Created:  2026-08-31 (pass 3 continuation)
Programme: #764 (deformation spectrum towers)
Depends on: T-108509 (spectrum M_m, monic), T-108513 (class
          crowding), O-108523 (the law being explained)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          branch_slopes.py + branch_slopes.json (exact sympy over
          Q and Q(sqrt 5))
Imports:  Newton-Puiseux for plane curve germs (single-segment
          polygon case) — Walker, Algebraic Curves, III.1; or
          Brieskorn-Knoerrer, Plane Algebraic Curves, 8.3.
          IMPORTED_THEOREM.
RH status: RH and GRH are unproved; this claim does not address them.
```

## Setting

Odd `m`; torsion point `a0 = 2 cos theta`, `alpha = e^{i theta}` of
order `M >= 3`, minimal polynomial `p in Z[a]`. Class counts
`n_c(m) = #{0 <= j <= m : 2j - m == c (mod M)}`, `mu_c = n_c - 1`
(T-108513). `M_m(z; a)` is the monic spectrum polynomial (T-108509),
`z_c = 2 cos(c theta)`. An interior class-pair is `{c, -c}` with
`c != 0, M/2`; note `n_c = n_{-c}` via `j -> m - j`.

## Hypotheses (all decidable by exact computation per cell)

- **(B) no crowded boundary**: `mu_0 <= 1` and `mu_{M/2} <= 1`.
- **(C) separation / no accident**:
  `deg_z gcd(M_m(.; a0), M_m'(.; a0)) = sum_pairs (mu_c - 1)` over
  interior pairs with `mu_c >= 2`, and `(z - z_c)^{mu_c - 1}` exactly
  divides that gcd for each such pair. (Equivalently: the multiple
  roots of `M_m(.; a0)` are precisely the crowded interior class
  points `z_c`, each of multiplicity exactly `mu_c`.)
- **(T) diagonal transversality**: for each crowded interior pair,
  writing `F(w, s) = M_m(z_c + w; a0 + s)` and
  `c_{i,j} = [s^i w^j] F`:
  `c_{i,j} = 0` whenever `i + j < mu_c`; the associated polynomial
  `A_c(lam) = sum_{k=0..mu_c} c_{k, mu_c - k} lam^k` has degree
  `mu_c`; and `disc(A_c) != 0`.

## Theorem (conditional interior multiplicity law)

Under (B), (C), (T):

```text
mult_p ( disc_z M_m(a, 1) )  =  sum over interior pairs  mu_c (mu_c - 1).
```

## Proof

**1 (which roots collide).** By (C) the root multiset of
`M_m(.; a0)` is: each crowded interior `z_c` with multiplicity
exactly `mu_c`, everything else simple. Distinct interior pairs have
distinct `z_c` (`2 cos(c theta)` injective on class-pair
representatives), so the colliding pairs of root branches at `a0`
are exactly the within-cluster pairs of each crowded class.

**2 (how each cluster splits).** Fix a crowded pair, `mu = mu_c`.
`F(w, 0) = w^mu u(w)` with `u(0) != 0` (step 1), so `c_{0,mu} != 0`;
with (T) the Newton polygon of `F` at the origin is the single
segment from `(0, mu)` to `(mu, 0)`. Blow up: substituting
`w = s (lam_r + v)` and using (T.a) (nothing below the diagonal),

```text
F(s (lam_r + v), s) = s^mu [ A_c(lam_r + v) + s R(v, s) ]
```

with `R` polynomial. Since `A_c(lam_r) = 0` and `A_c'(lam_r) != 0`
(disc != 0), the implicit function theorem gives a unique analytic
`v_r(s)`, `v_r(0) = 0`: an analytic branch
`w^{(r)}(s) = lam_r s + O(s^2)` for each of the `mu` distinct roots
`lam_r` of `A_c` (`deg A_c = mu` by (T)). These `mu` branches are
distinct and exhaust the local zero set (F has w-degree mu locally
by Weierstrass at `c_{0,mu} != 0`; the count matches — the general
Newton-Puiseux machinery, IMPORTED above, is needed only for this
bookkeeping sentence). Hence for every within-cluster pair,
`ord_s (w^{(r)} - w^{(r')}) = 1` exactly.

**3 (assembling the discriminant).** `M_m` is monic in `z`
(T-108509's normal form, machine-asserted at every build), so
`disc_z M_m(a) = prod_{i<j} (z_i(a) - z_j(a))^2` over the full root
system, with no leading-coefficient correction, and
`ord_{a0} disc = sum_{i<j} 2 ord_{a0}(z_i - z_j)`. Pairs not
colliding at `a0` contribute 0; by steps 1-2 the colliding pairs
contribute exactly `2 * C(mu_c, 2) = mu_c (mu_c - 1)` per crowded
pair. (B) ensures no boundary cluster exists.

**4 (from ord to multiplicity of p).** `disc_z M_m in Z[a]` and the
Galois conjugates of `a0` permute the local orders (apply an
automorphism to the factorization over the splitting field), so
`ord` is the same at every root of `p` and equals `mult_p`. Summing
step 3: `mult_p = sum mu_c (mu_c - 1)`. ∎

## Machine certificates (branch_slopes.json; all exact)

| cell | pairs (mu) | (T) | (C)+(S) | law value | matches data |
|---|---|---|---|---|---|
| a=0, m=5 | {1,3} (2) | OK, disc A = 41 | OK | 2 | yes |
| a=0, m=7 | {1,3} (3) | OK, 133788 | OK | 6 | yes |
| a=0, m=9 | {1,3} (4) | OK, ~6.8e10 | OK | 12 | yes |
| a=0, m=11 | {1,3} (5) | OK, ~9.2e18 | OK | 20 | yes |
| a=0, m=13 | {1,3} (6) | OK, ~5.1e29 | OK | 30 | yes |
| golden, m=11 | {1,9} (2) | OK | OK | 2 | yes |
| golden, m=13 | {1,9},{3,7} (2,2) | OK | OK | 4 | yes |

So O-108523's tower row `k(k+1)` and golden row are now
proved-by-mechanism at these m — the first cells of the law with a
proof, not only an exact computation.

## Structure found in the tower's associated polynomials

For the a = 0 tower (mu = (m-1)/2), the extracted `A_mu` satisfy
(machine fact, m = 5..13): leading coefficient `+-2^mu mu!`,
constant term 1, linear coefficient `(-1)^{mu+1}(mu+1)`; e.g.
`A_2 = -8 lam^2 - 3 lam + 1`,
`A_3 = -48 lam^3 - 27 lam^2 + 4 lam + 1`. The slopes are honest
algebraic irrationalities (disc 41, 133788, ...), so no closed-form
slope formula — the deposited route to the UNCONDITIONAL tower law
is a uniform separability proof for this coefficient family (their
reversed polynomials are monic with trace `+-(mu+1)`), not root
formulas.

## What remains open

(i) separability of `A_{c,m}` for all cells at once (the only
obstruction to the full odd-m law given T-108513 + the certified
(C)-pattern); (ii) the boundary-class mechanism behind the observed
`2 floor(mu/2)^2` term (the a = 1 tower's crowded class M/2 = 3 is
the minimal lab); (iii) even m. All deposited.
```
