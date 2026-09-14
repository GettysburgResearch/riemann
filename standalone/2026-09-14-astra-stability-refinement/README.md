# A small quantitative advance, not another RH reformulation

**SR26: proposed mathematics, independent review required.** This packet responds
to the criticism that the recent arithmetic programmes repeatedly renamed the
same missing RH-scale cancellation. It targets simple critical-line zero density
instead, retaining an extra finite-dimensional stability parameter.

The result is modest but numerical: using the SAME previously certified
seven-point pressure, the derived bound changes from

    0.673009652279136912...   (main's 280-block expression)

to

    0.673009665251783092...   (281 blocks, c=400059/200000).

The gain is about 1.30e-8 in proportion, or 1.30e-6 percentage points.
This is neither a new finite zero census nor progress from 67 percent to all zeros. No current-record or
external novelty claim is made. The new corollary retains the existing
seven-point certificate and published BGST/Riemann--von Mangoldt inputs.
These are not new RH-equivalent hypotheses, but they were not re-proved by the
finite checker in this pass.

## Read the actual mathematics

[PROOF.md](PROOF.md) supplies the whole deduction:

1. A free-threshold extension of the existing stability rank--inertia inequality.
2. The sharp defect lower bound for EVERY PSD trace-m matrix at EVERY admissible
   variance, with an explicit equality family.
3. A direct finite-multiset operator transfer retaining the stability and excess
   multiplicity terms. It uses the Lamzouri setting, not a new Weil-grid adapter.
4. The inherited seven-point theorem, exact block/endpoint accounting, and a
   smooth-window pressure estimate.
5. Removal of the rational pair weight using two fixed smooth tests, followed
   by a sequential height/window limit. All multiplicities and nonreal zeros
   are retained; RH is not assumed.
6. An exact rational choice of parameters with a certified strict improvement.

The existing c=2 lemma and pressure method are credited to the frozen ainta
source and the integrated supplement. The exact matrix envelope is not claimed
to be globally new to matrix analysis. The purpose is a checkable improved
application, not renaming standard machinery.

## What actually remains

Independent review must check the new finite inequality and analytic adapter.
No further arithmetic cancellation premise is delegated to that reviewer.
The seven-point computation and analytic pair-correlation theorem remain named
source dependencies. The much larger target RH is still unproved.

For a substantially larger gain this method needs new information about the
translation Gram matrix or a stronger pressure theorem. Trace and variance
alone cannot improve the sharp envelope proved here. A density bound, even one
near unity, cannot exclude an isolated or density-zero exceptional set.

## Reproduce the new bounded checks

```sh
python -B check.py --check results.json --self-test
python -O -B check.py --check results.json --self-test
python -OO -B check.py --check results.json --self-test
```

The standalone checker uses only integer and Fraction arithmetic. It encloses
the constants, tests exact spectral equality/inequality families and noncommuting
matrix examples, and rejects altered records. It does NOT run the old seven-point
exhaustion, verify BGST, compute zeta zeros or machine-prove the new paper proofs.
See [SOURCES_AND_VALIDATION.md](SOURCES_AND_VALIDATION.md) for exact pins and scope.
