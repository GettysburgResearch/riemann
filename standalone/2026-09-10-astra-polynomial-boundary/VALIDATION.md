# Validation and limits — AC29

## Mathematical boundary

The requested positive-eta estimate, uniformly over every polynomial degree,
remains OPEN. The new manuscript contains quantitative boundary constructions,
not a proof of that estimate or of RH. It does not refute positive eta either.
The parent already establishes the zero-exclusion and eta=0 conclusions by
another method; the new direct constructions are not new zero-location results.

## Completed executions

From this packet directory:

```
python -B check.py --write results.json --self-test
python -O -B check.py --check results.json --self-test
python -OO -B check.py --check results.json --self-test
```

All completed successfully and produced the same semantic digest:

```
326989a406ede7cb51451f15c2ecd3074c4b8d231c656914cc69f6447bca9c1e
```

A fresh addition-only patch application, manifest check, and normal/optimized
replays were also completed successfully before publication.

## Exact bounded scope

- 65 rational cutoff values, derivative bounds and the expanded cubic identity.
- Three REAL strip parameters 1/4, 1/2, 3/4, each enclosed by odd Euler sums at
  the complete even boundaries 128 and 256, including the entire discrepancy
  tail. These parameters are NOT zeta zeros.
- 27 complete smoothed-remainder and logarithmic-derivative bounds at fixed v.
- 24 finite dilation derivatives reconstructed by two formulas, with their
  complete analytic error envelopes.
- 12 Bernstein-primitive polynomial controls, using full native infinite
  even-zeta moments, including every cross term in both squared norms.
- 204 exact Bernstein coefficient/basis comparisons and approximation checks.
- Ten distinct altered-and-resealed reports are rejected in each self-test
  through the same acceptance function that checks reports. These are NOT ten
  separately launched CLI mutation processes.

The checker regenerates the entire expected payload. It does not merely check
its digest. Floating numbers and duplicate keys in an input JSON are rejected.
Acceptance uses explicit exceptions, not assertions disabled by optimization.

## Primitive arithmetic

Positive quarter-powers are enclosed by integer fourth-root inequalities with
160-bit dyadic endpoints. The odd Euler tail has an explicit analytic bound;
no uncomputed terms are assumed zero. Even-zeta values for polynomial controls
use the classical Bernoulli formula with directed Machin-pi intervals and
complete alternating tails. All arithmetic comparisons occur on rational
intervals BEFORE their outward rounding for the compact report.

One standard-library checker contains separately evaluated derivative and
Bernstein formulas. This is SAME-AUTHOR implementation cross-checking, not an
independent referee, proof assistant, or independent mathematical review.
The bounded samples do not machine-prove the all-parameter analytic lemmas,
Young's inequality, density, or the existence of a critical-line zero.

## Exploratory computations and development limitations

Non-directed mpmath scouting used a derivative-normalized odd-Legendre basis
at dimensions 24,32,64. No scouting value is a certificate input or evidence
for all degrees. An initial display read a negative matrix index incorrectly
and printed zero; the display was corrected and those readings were discarded.
The dimension-64 combined call exceeded its timeout after printing results;
it is NOT counted as a completed validation. No large-degree positivity claim
or numerical counterexample is made from this scouting.

No actual critical-zero ordinate, zeta derivative at a zero, complex-power
numerical integral, or unbounded zero census is evaluated. Critical-root
constructions in the manuscript are conditional on the explicitly stated
classical existence input, and off-critical constructions are conditional on
a HYPOTHETICAL root. No off-critical root is asserted to exist.

## Repository scope

Source head: b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e, PR845.
Main observed: f99d9e3908dde4865377c75d9ca051c1f545bf4f.
Only this new directory is added. No parent research, canonical status,
workflow, permission, or main file is modified. The parent proof's byte hash
is pinned in SOURCES.json and matches its recorded Git blob.

An actual git ls-remote attempt failed with `Could not resolve host:
github.com`. Consequently no authenticated full checkout, repository-wide
validator execution, or remote CI success is claimed. GitHub connector
publication and the local addition-only patch test are different events.
