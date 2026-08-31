# O-108512 — Torsion resonance of the deformation spectrum: the collision locus of the order-R point of alpha^2 enters at m = 2R + 1

```text
Claim ID: O-108512
Status:   OBSERVATION, half-CONVERTED: the entry law's FORWARD half is
          now PROVED as T-108513 (collisions forced from m = 2R+1,
          first collision at z = a, the m = 2R near-miss and the a=0
          m=6 gap derived — mechanism: class crowding of the Sym^m
          weight monomials mod the torsion order); the CONVERSE (no
          accidental collision below threshold) remains empirical,
          certified exact at ten points for every sub-threshold m
          (torsion_field_probe.json). Each stated factorization/
          vanishing is an exact machine-verified polynomial fact.
Created:  2026-08-31 (pass 3; grows out of T-108509)
Programme: #764 (moduli of local data; resonances of the defect tower)
Machine:  matrix/spectrum_collision_loci.json (m = 5..11; from
          c1_defect_atlas.json + m10_m11_spectrum.json, sympy exact)
Depends on: T-108509 (spectrum polynomial M_m and D_m = disc_z M_m)
RH status: RH and GRH are unproved; this claim does not address them.
```

## The exact facts (all machine-verified polynomial identities)

On the self-dual slice `b = 1`, `a = 2 cos theta`, the collision locus
of the deformation spectrum — the vanishing set of `D_m(a, 1) =
disc_z M_m(a, 1)` — contains, as m grows, the minimal polynomials of
the TORSION VALUES `a = 2 cos(pi k / N)` (Satake parameter a root of
unity of order 2N), with first appearances:

```text
ord(alpha)=4,  ord(alpha^2)=2 (a = 0):        enters at m = 5  (a^2)
ord(alpha)=6,  ord(alpha^2)=3 (a = +-1):      enters at m = 7
ord(alpha)=8,  ord(alpha^2)=4 (a^2 = 2):      enters at m = 9
ord(alpha)=5 AND 10, ord(alpha^2)=5 for both
              (a^2 + a = 1 and a^2 - a = 1):  enter TOGETHER at m = 11
```

THE ENTRY LAW (fits all five first entries with no exception): with
`R := ord(alpha^2)`, the collision locus of the torsion point enters
`disc_z M_m` at exactly

```text
m = 2R + 1,   i.e. when the number of spectrum points
              nu = floor((m-1)/2) first REACHES R.
```

The invariant is `ord(alpha^2)`, not `ord(alpha)`: for even orders the
two laws coincide (`2 ord(alpha^2) + 1 = ord(alpha) + 1`), and the odd
order 5 separates them — `a^2 + a = 1` (ord alpha = 5) does NOT enter
at m = 6 (checked exactly: the m = 6 discriminant factors are nonzero
mod `a^2 + a - 1`) but at m = 11, jointly with ord(alpha) = 10,
EXPLAINED by both having `ord(alpha^2) = 5`.

Every torsion factor appears with EVEN multiplicity (ramification
without splitting-field change: genuine double collisions of spectrum
points), the multiplicities grow with m (the a-power: a^2 at m=5,
a^6 at 7, a^12 at 9, a^20 at 11), and at each m the remaining factor
of `D_m` is a single large even polynomial. Non-appearance is also
exact: `(a^2 - b)` does NOT divide `D_5` or `D_6`, so the m = 7 entry
is genuine, and similarly for the other thresholds.

**The one apparent anomaly, resolved exactly:** `a = 0` (R = 2) is
absent from `disc_z M_6` — but not because nothing collides at m = 6:
`M_6(a=0, z) = z^2 - 4b^6 = (z - 2b^3)(z + 2b^3)`, whose root
`z = -2b^3` IS the trivial even-factor's z-value: at m = 6 the
supersingular collision is between a SPECTRUM point and the TRIVIAL
rank-1 constituent, invisible to `disc_z M_m` but present in the full
discriminant of `N_m`. The full-N_m collision stratigraphy (spectrum-
spectrum vs spectrum-trivial vs T-level double roots such as
`N_4(a=0) = (1+b^2T)(1-b^2T)^2` and the m = 5 example
`M_5(1,1) = (z+2)(z-1)` giving `(T+1)^2 | N_5(1,1)`) is finer than
the z-level law above and is deposited as data, not as a second law.

## The held-out confirmation (recorded as it happened)

After seeing m <= 9, the (then coarser) law predicted that m = 11
would newly contain the order-10 torsion — the golden-ratio
quadratics `a^2 - a - 1`, `a^2 + a - 1`. `M_10, M_11` were then
computed fresh (m10_m11_spectrum.json): m = 10 contains NO new
torsion beyond order 8, and m = 11 contains EXACTLY the two predicted
quadratics (each squared). One clean confirmation. The refined
`ord(alpha^2)` form of the law was found AFTER that confirmation (it
agrees with the prediction as made) while attempting the mechanism
proof, and was then put to a SECOND held-out test
(matrix/m12_m13_spectrum.json, computed fresh): it predicted (i) no
new torsion at m = 12, (ii) `a^2 - 3` (ord alpha = 12, ord alpha^2
= 6) entering at m = 13, (iii) the ord-7 cubic
`a^3 + a^2 - 2a - 1` NOT entering at m = 13. All three held: m = 12
carries only the previously-entered factors, m = 13 gains exactly
`(a^2 - 3)^2`, and the ord-7 cubic divides neither. THIRD held-out
round (matrix/m14_m15_spectrum.json; the predictions were written into
matrix/m14_m15_test.py before the run): m = 14 adds no new torsion;
m = 15 gains BOTH ord-7-related cubics `a^3 + a^2 - 2a - 1`
(2cos 2pi/7, ord alpha = 7) and `a^3 - a^2 - 2a + 1` (2cos pi/7,
ord alpha = 14) — the JOINT entry the `ord(alpha^2) = 7` form demands
— each squared; and the ord-9 cubic `a^3 - 3a + 1`
(`ord(alpha^2) = 9`, predicted entry m = 19) stays absent.

## The definitive table (m = 5..27 x 10 torsion points; exact)

The fourth/fifth rounds (predictions recorded in
matrix/m16_m19_test.py before any run) were executed by a NEW ENGINE,
matrix/torsion_field_probe.py (stdlib, EXACT_RATIONAL): the entire
defect computation — h-powers, Sym^m data, the T-108500 numerator with
tail certification, even division, triangular Laurent peeling to
`M_m`, monicity check, and the `disc_z = 0` test as a gcd-degree test
— is run with `a` = the generator of the number field `Q[a]/(C)` at
`b = 1`. Since each `C` is irreducible and `M_m` is monic in `z`
(T-108509), `disc = 0 in the field` is EXACTLY `C | disc_z M_m(a,1)`;
each cell costs seconds. Result (torsion_field_probe.json), first
entries and monotone persistence:

```text
point (min poly of 2cos)        ord(alpha^2) = R    first entry   2R+1
a - 1            (ord 6)                3                7           7
a^2 - 2          (ord 8)                4                9           9
a^2 + a - 1      (ord 5)                5               11          11
a^2 - a - 1      (ord 10)               5               11          11
a^2 - 3          (ord 12)               6               13          13
a^3 - 3a + 1     (ord 9)                9               19          19
a^3 - 3a - 1     (ord 18)               9               19          19
a^4 - 5a^2 + 5   (ord 20)              10               21          21
ord-11 quintic   (ord 11)              11               23          23
ord-13 sextic    (ord 13)              13               27          27
```

TEN points, TEN exact matches with `m = 2R + 1`, complete absence
certified at every earlier m (5..entry-1, not spot checks), and
monotone persistence at every point after entry (the sole known
non-monotone case remains the a = 0 z-level gap at m = 6, explained
above as a spectrum-trivial collision). Six of the ten entries were
held-out predictions (ord 10 joint; ord 12; ord 9/18 joint; ord 20;
ord 11; ord 13). The supersingular point a = 0 (R = 2, entry 5) is
covered by the earlier symbolic data. The law's remaining status:
empirically exact wherever tested; the proof — plausibly via the same
field engine, where the entry threshold becomes a statement about
gcd(M_m, M_m') over `Q(2cos theta)` — is the deposited problem.

## Collapse lemma at the {0, +-1}-valued slices (PROVED; 5 lines)

At the three tempered torsion slices `(a, b) in {(0,1), (1,1), (-1,1)}`
the h-sequence takes values in `{0, +-1}` (immediate induction on
`h_k = a h_{k-1} - h_{k-2}`: periods 4, 6, 6), so for EVERY odd `m`,
`h_k^m = h_k` pointwise and the whole defect series collapses to the
original local factor:

```text
sum_k h_k^m T^k = 1 / (1 - aT + T^2),  i.e.
N_m (1 - aT + T^2) = det(1 - Sym^m(A) T)   exactly at these slices.
```

These three slices are the ONLY real points with this property
(`h_1 = a` forces `a in {0, +-1}`), and the lemma makes every
collision statement there finitely checkable: the defect numerator at
`a in {0, +-1}` is the fully explicit cyclotomic-type product
`det(1 - Sym^m(A)T)/(1 - aT + T^2)`, so its repeated factors are
Sym^m-monomial coincidences — which is why the `a`- and `(a -+ 1)`-
factors dominate the collision loci with ever-growing multiplicities.
(Machine cross-check: exact for odd m <= 11, k < 60, and the a = +-2
slices provably do not collapse.) The remaining OPEN part of the
mechanism is the slices where `h` leaves `{0, +-1}` (`a^2 = 2`, the
golden points, ...), where `h_k^m != h_k` and the entry threshold
`m = 2 ord(alpha^2) + 1` still awaits a derivation.

## Reading (conjecture-generating; mechanism OPEN)

The defect tower RESONATES at the torsion points of the Satake
parameter: precisely at the angles where the local datum has extra
symmetry (finite-order Frobenius on the slice), pairs of the defect's
canonical deformations (T-108509) collide. This is a third instance of
the pass's recurring phenomenon — critical structure degenerating at
special moduli points (Epstein departures at CM-adjacent moduli,
graph-walk departures at rewiring bifurcations, now spectrum
collisions at torsion angles) — and the only one so far with an exact
ALL-m pattern attached. Suggested mechanism route (open): at torsion
slices `h_k` is periodic with period governed by `ord(alpha^2)`-
classes, the T-108500(5) denominator degeneration is maximal, and the
"first collision when nu reaches R" form of the law smells of a
pigeonhole on `alpha^2`-classes of spectrum points; making that exact
— the classes available to the nu points number R, forcing a
coincidence at nu = R (not R + 1, so the counting must include the
pairing constraint) — is the deposited problem.
```
