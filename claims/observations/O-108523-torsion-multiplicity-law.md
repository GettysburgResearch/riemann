# O-108523 — The torsion multiplicity law: how strongly each resonance divides the tower invariant

```text
Claim ID: O-108523
Status:   OBSERVATION (exact, 114/114 at odd m over the committed
          factorizations INCLUDING five fully held-out sieve rows:
          m = 19 (12/12, entries psi_9/psi_18), m = 21 (13/13, entry
          psi_20), m = 23 (15/15, entries psi_11/psi_22 — the first
          odd-order R = N regime), m = 25 (16/16, entry psi_24),
          m = 27 (18/18, entries psi_13/psi_26); the
          even-m bookkeeping is OPEN with the systematic deviations
          recorded, 95 cells through the m = 26 sieve row, all
          overshoots). The interior term is now PROVED under
          machine-certified transversality at seven cells
          (L-108524); the general law's remaining obstruction is
          named there.
Created:  2026-08-31 (pass 3 continuation; quantitative refinement of
          O-108512/T-108513)
Programme: #764 (deformation spectrum towers)
Machine:  research/exploratory/2026-08-30-two-programme-pass/matrix/
          mult_law_check.py + mult_law_check.json, over the exact
          factorizations disc_slice_factor_lcs.json,
          disc_slice_m16_m17.json (m = 5..17, ten torsion points) and
          the memory-lean sieve rows m{18..27}_sieve.json
          (multiplicities keyed by the psi index N = M directly)
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

**Held-out confirmations at m = 19, 21, 23, 25, 27 (74/74 across
the five rows).** The memory-lean sieve rows, computed AFTER the law was
frozen, match the prediction in EVERY cell: m = 19 (12/12), m = 21
(13/13), m = 23 (15/15), m = 25 (16/16), m = 27 (18/18) — including the
a = 0 tower continuing as k(k+1) = 72, 90, 110, 132, 156, and
EIGHT classes never in
any fitting data entering at their T-108513 thresholds with exactly
the predicted multiplicity 2: psi_9/psi_18 at 19, psi_20 at 21,
psi_11/psi_22 at 23 — the first odd orders beyond 9, i.e. the
R = N crowding regime, structurally different from everything the
law was fitted on — psi_24 at 25, and psi_13/psi_26 at 27. Full
comparison table in mult_law_check.json ("sieve_rows").
Odd-m score: 114/114.

## Update: interior mechanism now PROVED conditionally (L-108524)

L-108524 proves: three explicitly checkable hypotheses (no crowded
boundary; the gcd-certified separation/no-accident pattern; diagonal
Newton transversality per crowded class) imply the interior term
EXACTLY, and machine-certifies all three at seven full cells — the
a = 0 tower m = 5..13 and the golden point at m = 11, 13 — making
those the law's first proved-by-mechanism cells. The remaining
obstruction to the full odd-m law is named: uniform separability of
the associated polynomials (structure recorded there), plus the
boundary mechanism below.

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

The same formula overshoots at EVERY even-m cell (95/95 through the
m = 26 sieve row; deviations recorded in mult_law_check.json — e.g.
the m = 24 predictions overshoot by 2 to 22 per cell). The discrepancy
concentrates in the boundary classes, where the even-m trivial
factor `(1 + T)` interferes with the `z = -2` count and the `z = +2`
class `c = 0` (absent at odd m) needs its own rule; partial fits
(shifting mu by the trivial factor's absorption) repair single cells
but not all, so the even-m bookkeeping is deposited OPEN rather than
guessed. This mirrors T-108513's structure, where the even boundary
(the m = 2R near-miss, the a = 0 m = 6 gap) was also the delicate
part — and was eventually derived; the same is expected here.
```
