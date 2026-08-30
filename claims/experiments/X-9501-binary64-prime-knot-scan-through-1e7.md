# X-9501 — Binary64 prime-knot scan through `10^7`

Claim ID: X-9501  
Title: Reconnaissance scalar and finite-matrix screw scan through prime-power cutoff `10^7`  
Status: EMPIRICAL  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-9501, L-9501, L-9502, L-9503  
Scope: non-directed candidate discovery only  
Related counterexample candidates: none

## Statement

The binary64 program

```text
experiments/screw_prime_knot_scan.py
```

enumerated every prime power `q<=10,000,000`, evaluated every knot, evaluated
the unique stationary point in every cell whose derivative changed sign, and
performed small anchored-screw and Gaussian matrix scans on separated
low-value nodes.

It found no negative scalar or matrix nomination.  The smallest scalar value
encountered was

```text
left prime power:  3089
right prime power: 3109
t:                 8.039063759496273
Psi(t):            0.0275205733535131
```

This is an empirical result only.  It neither proves positivity through the
cutoff nor excludes a counterexample, because the arithmetic and manifest
were not directed or independently reproduced.

## Exact command

```bash
python experiments/screw_prime_knot_scan.py \
  --cutoff 10000000 \
  --top 12 \
  --matrix-size 8 \
  --lambdas 0.1,1,10 \
  --json-out experiments/results/X-9501-screw-prime-knot-1e7.json
```

The committed JSON records the script hash, environment, timings, all twelve
retained scalar records, selected matrix nodes, and matrix outputs.

## Observed counts

```text
prime-power rows:          665,134
knot values evaluated:     665,134
stationary cells evaluated: 10,341
A''(log 2), binary64:      1.178511301977579
```

The smallest-cell result was stable in a separate 80-decimal-place replay of
the same mathematical formula:

```text
t = 8.0390637594962717224686998307271024503675216208494100...
Psi(t)
  = 0.0275205733536208048204145750691337826974942559163441...
```

That replay was not interval-valued and was not independent, so it is not
part of a proof.

## Matrix reconnaissance

Eight scalar candidates separated by at least `log(2)` were retained.  The
binary64 results were

```text
anchored screw minimum eigenvalue: 0.020778862409304082
best normalized 2x2 determinant:   0.7437563674368014
```

For the Gaussian kernels:

```text
lambda = 0.1: minimum eigenvalue 0.0020767354468397073
lambda = 1:   minimum eigenvalue 0.020657755611436276
lambda = 10:  minimum eigenvalue 0.19466916333174655
```

All are positive at reconnaissance precision.

## Reproduction artifact

```text
experiments/results/X-9501-screw-prime-knot-1e7.json
```

The stored run used:

```text
Python 3.13.5
NumPy 2.3.5
Linux x86_64
script SHA-256 caf74725919345a97935cbc06e665ce0928ad49bc6522de69eb27b71a3677cbf
```

Timing and peak memory are machine-dependent.  The observed run took roughly
three seconds and about 320 MB RSS; most memory came from retaining the entire
manifest as Python objects.

## Verification performed

1. The script asserts that the sorted prime-power manifest is strictly
   increasing.
2. A smoke run through `10^5` reproduced `9,700` prime powers and the same
   `3089--3109` minimum.
3. The smooth formula was compared numerically with an independent
   high-precision polylogarithmic representation at points from `10^-6` to
   the candidate ordinate.
4. The candidate stationary point was recomputed at 80 decimal places from
   `A'(t)=P_0`.
5. Python bytecode compilation and JSON parsing succeeded after the final
   source changes.

These checks expose implementation mistakes but do not provide directed or
independent certification.

## Analytic domain audit

The scan used only real positive logarithms, square roots, elementary smooth
series, and real symmetric matrices.  It began the complete cell scan at
`log(2)`, where `L-9503` supplies strict convexity.  Matrix nodes were separated
by at least `log(2)`, making every nonzero difference fast for the elementary
smooth series.

## Dependency audit

- `L-9503` justifies evaluating knots plus one stationary point per susceptible
  cell.
- `L-9501` and `L-9502` justify the heuristic matrix predicates under RH.
- No unmerged numerical artifact from another branch was imported.

## Gap audit

- The sieve and prime-power enumeration were not independently checked.
- Binary64 prefix sums suffer rounding and cancellation.
- The smooth-series stopping rule is mathematically motivated but not
  outward-rounded.
- NumPy eigenvalues are discovery outputs only.
- The high-precision replay used the same derivation and is not independent.
- The scan stops at a finite cutoff and says nothing beyond it.
- Positive sampled/cell-minimum approximations are not proof of positive
  directed lower bounds.

## Adversarial tests

1. Rerun with a segmented prime-power producer and compare every row digest.
2. Replay the `3089--3109` cell with Arb at increasing precision.
3. Evaluate the same cell through both the local recurrence and two-prefix
   formula.
4. Perturb the candidate node to neighboring dyadics and verify convex shape.
5. Reconstruct the eight-node matrices from the committed primitive scalar
   table with a separate standard-library checker.

## Remaining uncertainty

No evidence yet indicates that the scalar margin trends toward zero at
accessible cutoffs.  The behavior beyond `10^7` and the sensitivity of larger
metric/Gaussian configurations remain open.

## Suggested next attack

Replace the full-memory manifest with a segmented stream, add directed Arb
prefixes and smooth increments, and push the complete convex-cell certificate
to the largest existing repository prime-power cutoff.
