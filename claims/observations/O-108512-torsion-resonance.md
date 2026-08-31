# O-108512 — Torsion resonance of the deformation spectrum: order-N collision loci enter at m = N + 1

```text
Claim ID: O-108512
Status:   OBSERVATION (each stated factorization/vanishing is an exact,
          machine-verified polynomial fact for the named m; the ENTRY
          LAW is a pattern over m <= 11 with ONE genuine held-out
          confirmation; the mechanism is OPEN)
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
order-4  torsion (a = 0):            enters at m = 5   (factor a^2)
order-6  torsion (a = +-1):          enters at m = 7   ((a-1)^2 (a+1)^2)
order-8  torsion (a^2 = 2):          enters at m = 9   ((a^2-2)^2)
order-5/10 torsion (a^2 -+ a = 1):   enters at m = 11  (both golden-
                                     ratio quadratics, squared)
```

Every torsion factor appears with EVEN multiplicity (ramification
without splitting-field change: genuine double collisions of spectrum
points), the multiplicities grow with m (e.g. the a-power: a^2 at m=5,
a^6 at 7, a^12 at 9, a^20 at 11), and at each m the remaining factor
of `D_m` is a single large even polynomial. Non-appearance is also
exact: `(a^2 - b)` does NOT divide `D_5` or `D_6` (values 9b^2-..., 3b,
3b^3 at a^2 = b), so the m = 7 entry is genuine, and similarly for the
other thresholds.

## The held-out confirmation (recorded as it happened)

After seeing m <= 9, the law "order-N enters at m = N + 1" predicted
that m = 11 would newly contain the order-10 torsion — the
golden-ratio quadratics `a^2 - a - 1`, `a^2 + a - 1`. `M_10, M_11`
were then computed fresh (m10_m11_spectrum.json): m = 10 contains NO
new torsion beyond order 8, and m = 11 contains EXACTLY the two
predicted quadratics (each squared). One clean confirmation; the next
test the law proposes is order-12 (`a^2 - 3`) entering at m = 13.

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
slices `h_k` is periodic, the T-108500(5) denominator degeneration is
maximal, and the collision locus should be derivable as the shadow of
that degeneration; deriving the `m = N + 1` threshold from it is the
deposited problem.
```
