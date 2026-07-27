# Second-pass addendum — later Opus/Fable contributions

Auditor: `gpt56-06-g`  
Date: 2026-07-27  
Parent: Issue #138 / PR #140

The first inventory ended at O-5613. A commit-history sweep found four later
load-bearing records: R-5602, R-5603, O-5614, and O-5615.

## Verdict matrix

| Source | Verdict | Correct conclusion |
|---|---|---|
| `R-5602` anti-Herglotz sign | **PASSED** | As written, `i F(1/2+i tau)` is anti-Herglotz on the upper half-plane under RH; the Herglotz normalization is its negative. The right-half-plane Pick kernel numerics are unaffected. |
| `R-5603` 128-bit “coin flip” | **PASSED CORE / RHETORIC NARROWED** | The old midpoint-only screen is numerically uncertified and its strongest negative is a precision ghost. The 53.3% rate is tied to one chosen random-error model and one table; it is not a probabilistic theorem for deterministic rounding or every ordinate. See `R-13805`. |
| `O-5614` positive-node walls and ladders | **PASSED FINITE COMPUTATIONS WITH INDEPENDENCE/SCOPE REPAIR** | The six exact wall checks and declared PA-1/3/7 matrix packets are directed positive finite exclusions, conditional on their theorem chain. Principal-log versus direct-product overlap is I1 assembly independence, not an independent backend. The continuous anchor family remains open. |
| `O-5615` global scalar screw scan | **VERSION-1 ARTIFACT REFUTED; FINITE CONCLUSION RESTORED** | The original loop omitted the terminal cell after the last prime-power knot. The audit replay included all 665,135 cells and certified the complete finite range positive with lower bound `0.02322795137452749...`. See `R-13804` and the retained replay artifacts. |
| first line-mass budget in X-5605 | **PASSED AS A FIXED-WITNESS MEASUREMENT** | A certified subset mass below the same frozen nonnegative response is a sound lower-accounting test. The reported `0.1%` saturation is specific to that witness and slab and is not a route-wide detection threshold. |

## R-5602 reconstruction

Let

```text
Xi(z)=xi(1/2+i z),
F=xi'/xi.
```

Then

```text
Xi'(z)/Xi(z)=i F(1/2+i z).
```

Under RH the zeros of `Xi` are real and the symmetric log derivative has terms
`1/(z-gamma)`, whose imaginary parts are negative in the upper half-plane.
Thus `iF` is anti-Herglotz and `-iF` is Herglotz. The sign correction is sound.

Two scope notes remain:

1. the full symmetric Hadamard normalization must be fixed explicitly;
2. the substitution sends the upper `z` half-plane to the **left** `s`
   half-plane, with the functional equation carrying it back to the right.

The existing right-half-plane kernel computations do not inherit the sign error.

## R-5603 reconstruction

The experiment gives a valuable diagnosis:

```text
true lambda_min       about +1.226e-35
128-bit simulated spread about 2.99e-33
```

so the signal is far below the table's primitive sensitivity. A midpoint sign
at that precision is not meaningful.

The strongest permanent statement is deterministic:

```text
if the complete directed/sensitivity interval meets both signs, the midpoint
screen cannot nominate a candidate.
```

The random flag rate is illustrative, not load-bearing. Actual evaluator errors
are correlated and deterministic, and another ordinate can have a different
spectral moat. Precision should be chosen from the active uncertainty ledger,
not a universal `>=160 bits` rule.

## O-5614 reconstruction

The direct wall code uses:

- exact rational node and response coefficients;
- outward modulus-square conversion from rational rectangles;
- Arb logarithms;
- high-precision ball moment contractions;
- ball Schur solves and strict gap tests.

Positive gaps remain sound despite lost correlations because independent ball
widening is conservative. The main audit repairs are about evidence language:

1. a second factor assembly through python-flint/Arb is not backend-independent;
2. agreement with a 70-digit scan is a convention regression, not proof;
3. decimal ball strings are less portable than exact endpoint serialization;
4. local `D=0` context does not contribute to the finite wall sign;
5. six anchors and three nested packets do not close every positive node set.

The finite `CERTIFIED_INSIDE` / `CERTIFIED_PSD` rows are retained.

## O-5615 coverage defect and restoration

Version 1 had 665,134 prime powers and reported 665,134 cells. The advertised
range has one more cell because

```text
last prime power = 9,999,991 < cutoff = 10,000,000.
```

The omitted terminal interval was replayed separately:

```text
[log(9,999,991),log(10,000,000)]
terminal lower bound
[0.037976880209225143510091755 +/- 4.85e-28] > 0.
```

A four-chunk complete replay then checked all cells:

```text
prime powers                 665,134
cells including terminal     665,135
strictly positive cells      665,135
maximum bisection depth      0

global lower bound
[0.023227951374527490554974016282146664631 +/- 2.98e-40]
```

This restores the finite conclusion

```text
Psi(t)>0 for 1/2 <= t <= log(10^7)
```

under the D-9501 normalization and Arb trust base. It does not close other
screw criteria or heights.

## Independence correction

The later Fable records repeatedly use “independent backend” for a different
assembly or sieve using the same FLINT/Arb library. `M-13802` replaces this with
an explicit I0--I5 taxonomy. The O-5614/X-5606 audit replays are I1/I2
consistency checks, not I3 backend-independent reproductions.

## New files from the second pass

```text
R-13804  X-5606 terminal-cell coverage defect and repaired verdict
R-13805  R-5603 probabilistic-language scope correction
M-13802  certified-computation independence levels
certified_scan.py v2
terminal_cell_replay.py and exact result
chunked complete replay source, four chunk results, summary, SHA ledger
```

No RH counterexample is claimed. The repaired scalar screw interval is a
positive finite exclusion.
