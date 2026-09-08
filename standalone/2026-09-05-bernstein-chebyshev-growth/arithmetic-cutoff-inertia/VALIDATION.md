# Validation record and independent-review requirements

## Executed

From this directory, normal and optimized Python freshly reconstructed the
saved result and each completed 141 exact rational checks:

```
python verify_cutoff.py --check result.json
python -O verify_cutoff.py --check result.json
```

Their complete outputs are byte-identical. REPLAY.json records interpreter
version, command, exit code, and stdout SHA-256. The normal/optimized reruns do
not create additional distinct mathematical controls.

The groups comprise 17 bump checks, 24 exponential-moment annihilation checks,
18 norm controls, 35 scalar-majorant controls, 23 multiplier identities, 12
piecewise-continuum Laplace identities, 9 rational constant checks, and 3 parent
source-integrity checks. The coefficient certificate for the all-ell scalar
inequality is reconstructed as the polynomial ell+(9/20)ell^2; finite sample
checks do not replace that proof.

Twelve deliberately corrupted cases were rejected with the intended error:
wrong saved norm, floating-point type alias, Boolean type alias, duplicate JSON
key, changed new proof bytes, and changed parent commit lock, each in normal
and optimized Python. Source code uses explicit exceptions, not assert-based
acceptance. The saved JSON is freshly reconstructed and strictly compared,
including Python value types. The parent proof's Git blob is checked against
a literal source constant, not only a self-declared manifest entry.

The checksum manifest binds all eight other files in this packet. The included
manifest is an integrity record, not a mathematical proof.

## A separate non-certifying analytic sanity check

A local 40-digit mpmath check compared the finite gamma partial-fraction
multiplier (10,000 terms) with digamma at frequencies 0, 1/3, 2, and 10. The
remaining difference was approximately -1.2498e-9, consistent with the omitted
gamma tail. The same non-directed calculation gave about -0.6955873 for the
X=2 compensated multiplier numerator. Neither floating-point output enters
acceptance or the analytic proof; the proof uses strict elementary bounds.
No mpmath or other special-function library is imported by verify_cutoff.py.

## Not executed or not established

No complete infinite-prime form was numerically evaluated. No broad prime or
zero sweep, external zero census, predecessor checker suite, Lean build,
independent referee review, or remote CI success is claimed. The exact finite
checks do not machine-prove Fourier/Plancherel, trace-norm convergence, min-max,
infinite inertia, or the uniform-in-X assertion. No RH proof or new signed
bound for the full arithmetic source was obtained.

## Priority independent review

Check the distinction between arithmetic cutoffs and full-source matrix
compressions; the moment constraints before transforming the growing
exponential; the b=3/2 and factor-two prime normalizations; the convergent gamma
regrouping; chi's endpoint regularity; the derivative-norm bound; the direction
of the Rayleigh inequality; and the construction of arbitrarily large negative
subspaces rather than an inference from one negative vector.

For the averaged-tail repair, check its exact piecewise kernel, cancellation
of the growing exponential, the sign of the sine term in its multiplier, and
the elementary strict X=2 sign. That one repair counterexample must not be
reported as a theorem excluding every cofinal positive completion scheme.

The changing f_X and vanishing negative gap are essential: these results
provide no fixed negative witness for the full operator and no disproof of RH.
