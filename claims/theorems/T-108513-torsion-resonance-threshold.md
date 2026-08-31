# T-108513 — The torsion resonance threshold: forced spectrum collisions begin at m = 2 ord(alpha^2) + 1, colliding first at z = a

```text
Claim ID: T-108513
Status:   PROVED: the forward half for ALL m (collisions forced from
          m = 2R+1, first collision at z = a, the m = 2R near-miss and
          the a = 0, m = 6 gap derived) AND — via the monic-sieve
          addendum — the COMPLETE two-sided law for every torsion point
          of every order in the range m <= 17 (exact factorizations +
          Gauss's lemma; matrix/disc_slice_factor_lcs.json extended by
          matrix/disc_slice_m16_m17.json: at m = 16 and 17 the monic
          factors are again exactly the threshold-respecting torsion
          polynomials — the ord-16 quartic duly entering at 17 — and
          the single remaining factor has non-unit leading coefficient,
          deg 292 / lc ~ 2.2e32 and deg 384 / lc ~ 6.1e41). The
          converse for m >= 18 remains open, reduced to the same
          checkable normal form per m
Created:  2026-08-31 (pass 3 continuation; converts O-108512's law)
Programme: #764 (moduli resonances of the defect tower)
Depends on: T-108500, T-108509; grew from O-108512's held-out rounds
Proof:    standalone/2026-08-31-torsion-resonance-threshold/PROOF.md
Machine:  matrix/torsion_field_probe.py + torsion_field_probe.json
          (exact number-field table m = 5..27, now FOURTEEN points:
          twelve entries all at exactly m = 2R+1 with (z-a)^2 at entry
          12/12 — ord-16 at m=17 and ord-24 at m=25 were the sixth and
          seventh held-out rounds, predicted in-code before their run —
          plus ord-15/ord-30 (R=15, entry 31) certified absent through
          m=27); replay experiments/X-108513-torsion-threshold/
          (self-contained stdlib: direct regrouping-lemma divisibility
          in K[T], the entry table, the z=a collision, the m=2R
          near-miss — all green)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

At a torsion point of the self-dual slice (`b = 1`,
`a = 2 cos theta`, `alpha = e^{i theta}` of order `M >= 3`,
`R = ord(alpha^2)`):

1. **Regrouping**: `N_m(T) = prod_c (1 - alpha^c T)^{n_c - 1} G(T)`
   where `n_c` counts the exponents `2j - m (mod M)`, `j = 0..m` —
   every crowded weight-monomial class donates its excess as a
   REPEATED root of the defect, unconditionally.
2. **Threshold**: classes triple exactly from `m = 2R` (`j` repeats
   with period `R`); at `m = 2R` the unique triple lands on the
   boundary class `c = 0` (`z = 2`, a single doubled quadratic — no
   collision), and at `m = 2R + 1` the triples land on `c == +-1`,
   forcing TWO spectrum points to coincide at

   ```text
   z = alpha + alpha^{-1} = a :
   ```

   the spectrum's first forced collision is AT THE ORIGINAL TRACE, and
   `disc_z M_{2R+1} = 0` with `(z - a)^2 | M_{2R+1}` over `Q(a)`.
3. **Derived bookkeeping**: the `m = 2R` non-entry at every point, and
   the one table anomaly — `a = 0` (R = 2) absent at `m = 6` — follow
   from the same counting (`M = 4` puts the m = 6 triples on
   `T = +-1`, i.e. the boundary values `z = +-2`, one of them the
   even-m trivial factor), as does its return at `m = 8`
   (`mult_T(1) = 4` = two spectrum points at `z = 2`).

## Mechanism named

The resonance is CLASS CROWDING: the `m + 1` weight monomials
`alpha^{2j - m}` of `Sym^m` occupy only `R` classes modulo the torsion
order, and once a class holds three of them the defect numerator
inherits a forced double root away from `T = +-1`. "Extra symmetry
forces spectral degeneracy", here as an exact statement about binomial
partial fractions — no analysis involved.

## What remains open

The converse: for `m < 2R + 1` the cofactor `G` (explicit binomial
sums `D_c`) never accidentally vanishes at a doubled class or acquires
repeated roots. Ten points x all sub-threshold m are certified exact
(zero accidental collisions observed); a proof needs non-vanishing of
explicit binomial-sum resultants and is the deposited next problem.
```
