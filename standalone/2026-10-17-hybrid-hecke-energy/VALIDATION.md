# Validation, review boundaries, and reproduction

This packet has one proof/code author. No independent mathematical referee,
proof-assistant build, upstream theta reconstruction, full-repository validator,
or remote CI result is claimed. The upper-bound argument is written in full;
finite checks do not establish its infinite inequalities.

## Actually executed

1. `python check_hybrid.py` and `python -O check_hybrid.py` produce byte-identical
   EXACT.json. The exact arithmetic is Python integers and fractions.Fraction.
2. Both modes of `check_hybrid.py --numerical` produce byte-identical
   NUMERICAL.json. mpmath runs at 60 decimal digits. These are ordinary
   high-precision calculations, NOT directed/interval bounds.
3. Five separately executed corrupted `python -O` processes are rejected:
   collapsing conjugate ideals; an invalid unit/angle exponent; a wrong
   powerful coefficient; dropping the periodic Fourier aliases; and a wrong
   critical-energy Jacobian. Their commands and terminal errors are in
   MUTATIONS.json. None is a synthetic declaration that a mutation would fail.
4. Final syntax, manifest, and archive round-trip checks are performed before
   delivery. Remote Git blob read-back authenticates the published packet;
   it is not a mathematical acceptance test.

## Exact coverage

- Complete ideal enumeration for EVERY norm through 512 in Q(omega): 311
  ideals. Its 512 norm-fiber counts agree with the separate divisor sum
  sum_(d|n)chi_-3(d). Conjugate ideals are never collapsed.
- 77 ideals through norm 128: norm-one angular values and all six unit choices;
  400 product checks; every pair in this smaller set satisfies the exact
  nonassociate lattice gap; equal-norm angular distinctions are retained.
- 44 local positive tensor configurations, with k=1,2,3,4; m=2,3,4,6,7;
  q=7,13,25. Odd m is tested at square q=25, so its weight is rational.
  The nonzero degree-one correction and its critical coefficient mass are
  checked, not silently discarded.
- All 54 nonzero Eisenstein rows of norm at most 13 and the prime ideals of
  norms 7,7,25: literal nonunit zeros and the neutral sixth-power mask.
  The first two ideals of norm 7^6 are separate exact local fixtures, not a
  claimed complete high-norm census.
- Six complete finite tensor regroupings use every supported ideal through
  norm 64 at m=2,4,6 and product orders 2,3. All shared factors are retained.
- The class-character gate has finite cyclic-group diagnostics. There is no
  numerical ideal-class census for class number >1; that extension is proved
  using the finite class group and its fractional-ideal lattices.

The per-predicate counts in EXACT.json describe loops, not that many independent
analytic cases or theorems.

## Numerical coverage

Fifteen periodic Fourier checks compare the discrete Gaussian sum directly
with its Poisson-periodized expression. Six independent real integrals check
the Gaussian pair kernel including the dX/X^2 Jacobian and the CDF shift.
Four continuous Gaussian Fourier integrals check the Mellin multiplier.
The recorded defects are below 1e-45; no tolerance is called a certificate.

Eight energy panels include every supported ideal under the explicit finite
caps 32,64,128 and all their pairs. The columns include both native and coupled
sources, and the m=2 powerful channel. These panels are FINITE polynomials;
they do not evaluate the entire infinite Gaussian source or justify an
asymptotic exponent. The m=6 high-prime-power range is tested only in the
separate exact local fixtures.

## Adversarial mathematical review requested

Review THEOREMS.md (10)--(11), especially the off-origin Gaussian sum with NO
additive constant and the full infinite norm tail. Check the finite class
adapter for arbitrary imaginary quadratic fields. Next check (13), retaining
all squared-energy cross terms, and distinguish (16)'s positive diagonal
secondary term from #953's negative prime-quotient subtotal. Finally review
HIGHER_MOMENTS.md (20)--(23): powerful weight, actual convolution overlap,
uniformity in m, and the stated D^k spectral-area cost.

The substantive fixed-principal signed estimate is not claimed or assumed.
Classical large-sieve/mean-value methods are explicitly credited; global
historical priority was not established by this pass.
