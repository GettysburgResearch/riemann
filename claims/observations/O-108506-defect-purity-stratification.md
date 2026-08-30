# O-108506 — The m=3 defect's purity is stratified by the Satake angle

```text
Claim ID: O-108506
Status:   OBSERVATION, PROVED at the stated finite/local scope (exact
          two-case criterion + exact witnesses); the density remark uses
          the Sato-Tate THEOREM (non-CM case; 11a1 is non-CM) as a
          labelled external input, not verified here
Created:  2026-08-30
Programme: bridge #763 x #764 — the #763 detector's purity axiom applied
          to the #764 defect objects of T-108500
Depends on: T-108500 (N_3 = 1 + 2abT + b^3T^2), T-108002 (purity test,
          complete for degree 2)
Replay:   experiments/X-108506-defect-purity/verify.py
RH status: RH and GRH are unproved; not addressed.
```

## Exact statement (degree-2 elliptic normalization, b = p, a = a_p)

The m=3 defect `N_3 = 1 + 2 a p T + p^3 T^2` is an integral, SELF-DUAL
(T-108500 statement 4) quadratic Euler factor whose purity is decided
exactly by the sign of `a^2 - p`:

- if `a_p^2 < p`: discriminant `4p^2(a_p^2 - p) < 0`, complex-conjugate
  inverse roots of common modulus `p^{3/2}` — PURE of weight 3;
- if `a_p^2 > p`: real inverse roots of distinct moduli — IMPURE
  (both cases within the Hasse range `a_p^2 <= 4p`).

Exact witnesses (curve 11a1, exact point counts): at `p = 2`,
`a_2 = -2`, `a^2 = 4 > 2`: `N_3 = 1 - 8T + 8T^2`, real roots, IMPURE;
at `p = 3`, `a_3 = -1`, `a^2 = 1 < 3`: `N_3 = 1 - 6T + 27T^2`,
discriminant `36 - 108 < 0`, PURE of weight 3.

## Reading

The obstruction object attached to the pointwise cube is a boundary
object for the #764 ladder in a sharper sense than "fails L4": it is
integral and self-dual EVERYWHERE but pure only on the part of the set of
good primes where the Satake angle satisfies `|cos theta_p| < 1/2`. Under the
Sato-Tate law (a theorem for non-CM elliptic curves — Clozel-Harris-
Shepherd-Barron-Taylor et al.; used here only as a labelled reading, not
an input) the impure stratum has a fixed positive density. So the ladder's
L4 cell for this object is not a bit: it is a DENSITY. The pass records
this as a discovered phenomenon class — "angle-stratified purity" — and a
reason the survival schema should allow measure-valued cells in a later
revision.

Note the contrast inside the same theorem package: the m=2 defect
`1 + pT` is pure of weight 2 at EVERY prime; stratification begins at
m = 3, exactly where the defect exits the character ring (T-108500
Theorem 2).
```
