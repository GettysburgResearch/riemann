# O-108523 — The torsion multiplicity law: how strongly each resonance divides the tower invariant

```text
Claim ID: O-108523
Status:   OBSERVATION (exact, 40/40 at odd m over the committed
          factorizations; the even-m bookkeeping is OPEN with the
          systematic deviations recorded). The class-count inputs are
          the PROVED objects of T-108513; the law's mechanism reading
          is identified but its local-branching proof is deposited,
          not claimed.
Created:  2026-08-31 (pass 3 continuation; quantitative refinement of
          O-108512/T-108513)
Programme: #764 (deformation spectrum towers)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          mult_law_check.py + mult_law_check.json, over the exact
          factorizations disc_slice_factor_lcs.json and
          disc_slice_m16_m17.json (m = 5..17, ten torsion points)
RH status: RH and GRH are unproved; this claim does not address them.
```

## The law (odd m; exact, 40/40)

For a torsion point with root of order M and class counts
`n_c(m) = #{0 <= j <= m : 2j - m == c (mod M)}` (T-108513's crowding
counts), the multiplicity of the point's minimal polynomial in the
exact factorization of `disc_z M_m(a, 1)` is, at every ODD m in the
data range,

```text
mult(m) = sum over interior pairs {c, -c}  mu_c (mu_c - 1)
        + 2 * floor(mu_{M/2}/2)^2          (boundary class, z = -2),
mu_c = n_c(m) - 1
```

— verified exactly at all 40 (point, odd m) cells, m = 5..17
(e.g. the a = 0 tower is mult = k(k+1), k = (m-3)/2: 2, 6, 12, 20,
30, 42, 56). In particular T-108513's threshold theorem is the
STATEMENT that this quantity first becomes positive at m = 2R+1 via
an interior pair; the law refines the threshold into the full
growth profile of each resonance.

## Mechanism reading (identified, not yet proved)

The interior term is exactly what transversal separation predicts:
an interior class-pair `{c, -c}` forces `mu_c` coinciding spectrum
points at `z = 2cos(c theta)`; if the colliding branches separate
LINEARLY in `(a - a_0)` — as the perfect quadratic profile
`mu(mu-1)` at every tested cell indicates — each of the
`2*C(mu, 2)` discriminant factors `(z_i - z_j)^2` vanishes to order
exactly 2. The boundary term's halved square is the shadow of the
square-root branching at `z = +-2` (spectrum points reaching the
boundary collide in pairs). PROOF TARGET (deposited): local Puiseux
analysis of `M_m(z; a)` at the torsion points — transversality at
interior collisions, pair-branching at the boundary.

## Even m: OPEN, with the deviation table recorded

The same formula overshoots at EVERY even-m cell (29/29; deviations
-2 to -14, recorded in mult_law_check.json). The discrepancy
concentrates in the boundary classes, where the even-m trivial
factor `(1 + T)` interferes with the `z = -2` count and the `z = +2`
class `c = 0` (absent at odd m) needs its own rule; partial fits
(shifting mu by the trivial factor's absorption) repair single cells
but not all, so the even-m bookkeeping is deposited OPEN rather than
guessed. This mirrors T-108513's structure, where the even boundary
(the m = 2R near-miss, the a = 0 m = 6 gap) was also the delicate
part — and was eventually derived; the same is expected here.
```
