# X-9312 — Positive-anchor Geronimus gates for direct xi

Experiment ID: `X-9312`  
Agent: `gpt56-04-e`  
Issue: #93  
Stacked base: draft PR #117  
Status: exact finite algebra plus empirical direct-xi nominations

## Objective

Extend the PR #103/PR #116 degree-14 direct-xi response certificate by one exact
positive node. L-9314 proves that every degree-15 half-line-nonnegative response
is decided by one new scalar `b0` and two exact Schur bounds. L-9315 reconstructs
`b0` from one new direct-xi point, one old reference point, and the fifteen
already-certified old moments.

A strict directed failure of either Schur gate gives an explicit polynomial
square response and therefore a finite RH-disproof nomination through L-9308.

## Files

- `positive_anchor.py` — standard-library exact recurrence, Schur, witness, and
  reduced-replay algebra;
- `verify_b0_interval.py` — exact strict-negative checker for a directed `b0`
  interval;
- `tests/` — ten exact regression/adversarial tests;
- `results/nominations.json` — retained empirical anchor ladder;
- `CANDIDATE_HANDOFF.md` — exact one-point production instructions.

## Reproduce the exact midpoint gate

From this directory, using PR #112's retained basis:

```bash
python positive_anchor.py \
  ../X-9306-real-log-portfolio-search/results/basis.json \
  --anchor 4 \
  --output results/pr103-w4-full-regenerated.json

PYTHONPATH=. python -m unittest discover -s tests -v
```

The script evaluates no xi, zeta, logarithm, square root, eigensolver, or
floating-point operation. Every displayed fraction is derived with Python
integers and `fractions.Fraction`.

## Main retained nomination

At the PR #103 atomized minimum and `w=4`:

```text
Schur lower = 27375115.77715610683338270942781224884018...
Schur upper = 27375115.77715610684289268397858616575745...
midpoint b0 = 27375115.77715610683624020837623539349038...
```

The midpoint is positive-side interior, not a counterexample. Its distance from
the lower gate is about `2.8575e-12`. Because the coefficient of the sole new
primitive is only about `2.3291e-10`, a directed residual width substantially
below `0.012` should resolve the gate.

The new point is `x=2`, namely

```text
s = 5/2 + i T,
T = 20225875608343133989267 / 2^32.
```

This is a cheap and clean exact computation compared with another 16-point
high-height table.

## Candidate interval schema

`verify_b0_interval.py` accepts

```text
riemann.x9312-positive-anchor-b0.v1
```

with an exact positive rational anchor and a directed rational `b0_interval`.
It derives exact rational lower- and upper-gate witness directions from the old
moment midpoints, contracts them against the *complete old directed boxes*, and
accepts a negative only when one full quadratic upper endpoint is strictly below
zero. Zero-touching is unresolved.

A nonnegative result in those two fixed directions does not by itself certify
the complete new cone positive; that requires the robust moment-matrix argument
specified in L-9314.

## Proof boundary

- L-9314/L-9315 finite algebra and the scripts' rational calculations are exact.
- The gate is formed from exact midpoints of directed old-moment intervals and is
  a discovery object until a full interval contraction is performed.
- The ordinary mpmath `b0` reconnaissance is not retained as proof data.
- Any negative must be reproduced from directed completed-xi rectangles and
  inherit the reviewed L-9308/count-deflation theorem gates.
- No candidate ID is allocated.
