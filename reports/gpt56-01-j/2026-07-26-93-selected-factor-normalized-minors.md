# Agent report — selected-factor deflation and normalized modulus minors

Agent: `gpt56-01-j`  
Issue: #93  
Date: 2026-07-26  
Branch: `agent/gpt56-01-j/93-exact-factor-normalized-minors`

## Objective

Continue the PR #71 direct completed-xi attack after the complete D-0801 fixed vector was certified positive. The immediate questions were:

1. Can narrow directed critical-line zero balls be used more strongly than X-9301's far-endpoint deflation?
2. Are the tiny PR #71 logarithmic Loewner determinants genuine residual near-nulls or forced by clustered-node geometry?
3. Does an exhaustive selected-factor replay over the full nine-point block reveal a negative object omitted by the inherited row manifest?

## Main theorem 1: selected-factor removal

`L-9304` proves that proof-grade critical-line zero balls may be used to remove the corresponding actual factors

```text
log(u + (T-gamma)^2)
```

from the direct completed-xi logarithmic modulus. The unknown squared distance is carried as an exact rational interval obtained from the zero ball.

Under RH, the selected factors are genuine members of the canonical product. Removing finitely many of them leaves the same positive Stieltjes/Cauchy representation over the unselected zeros. Therefore complete monotonicity, cross-Loewner total positivity, and algebraic two-point inequalities remain valid.

This strictly improves the conservative endpoint subtraction from `L-9301`: the latter leaves a positive interval measure from the true squared distance to the far endpoint bound; exact factor removal leaves none of that selected zero's mass.

## Main theorem 2: geometry-free minors

`L-9305` factors every cross minor as

```text
raw determinant
=
row Vandermonde * column Vandermonde * normalized Stieltjes minor.
```

The normalized minor has a nonnegative continuous Cauchy-Binet integral, descends under certified zero deflation, and has a finite confluent limit as nodes coalesce.

This gives a stable ranking quantity. A raw determinant near `1e-90` can be ordinary geometry if the exact Vandermonde factor is comparably small.

## Exact checker

`X-9302` uses only Python integers and `fractions.Fraction` after JSON parsing. It supports:

- direct positive modulus-square intervals;
- exact squared horizontal nodes;
- pairwise-disjoint selected critical-line zero balls;
- lower multiplicity counts and immutable gate digests;
- selected-factor algebraic monotonicity;
- selected-factor logarithmic cross minors through order four;
- exact row and column Vandermonde ledgers;
- raw and normalized sign intervals.

Seven adversarial tests pass.

## Strict synthetic separation

The model

```text
H(u)=(u-5)^2 (u+1)^50
```

has a modeled off-line dip hidden by fifty selected line factors.

The undecomposed rows are positive:

```text
raw monotonicity       +88812771367611610316284546634444121
raw Loewner determinant approximately +5.8985579416206204
```

After exact selected-factor removal:

```text
selected monotonicity  strictly negative
selected determinant  -4*(log 2)^2
normalized determinant approximately -0.213534672852534
```

Both negative rows are certified with exact finite arithmetic. They are synthetic controls, not Riemann-xi evaluations.

## Exhaustive PR #71 replay

At the exact PR #71 ordinate, all nine existing dyadic horizontal offsets were evaluated through ordinary high-precision Riemann-Siegel arithmetic. The scan tested every disjoint cross minor:

```text
order 2     756
order 3   1,680
order 4     630
```

plus every divided difference through order eight.

The scan was repeated after removing increasing nearest-zero prefixes through all 173 empirical line-zero ordinates in the retained X-5602 window. No negative object was found.

After sixteen refined zero removals, the minimum normalized minors were approximately:

```text
order 2   +7.02e-2
order 3   +4.89e-6
order 4   +4.29e-11
```

After all 173 empirical removals:

```text
order 2   +9.26e-6
order 3   +3.22e-13
order 4   +2.71e-18
```

The smallest raw order-four determinant was about `8.30e-88`. Normalization therefore explains a large part of the visual near-null.

The 173-root replay is discovery arithmetic only. Its root list and direct-xi values are not directed proof artifacts.

## Counterexample status

No strict Riemann-xi negative interval was produced. No `Z-####` identifier is allocated.

The current PR #71 block should be treated as:

- mathematically well motivated;
- dominated by nearby line-zero mass and node geometry;
- still positive in exhaustive ordinary replay;
- awaiting one directed selected-factor replay for rigorous closure.

## Recommended production sequence

1. Finish or recover one directed PR #71 completed-xi primitive artifact.
2. Recover the directed Hardy-zero block from the same exact ordinate.
3. Replay the unchanged rows with both L-9301 endpoint deflation and L-9304 selected-factor deflation.
4. Rank unresolved rows by normalized radius, not raw determinant magnitude.
5. Refine only the dominant zero balls or completed-xi rectangles.
6. If the normalized intervals are strictly positive, move to another rigorously isolated large-gap ordinate.

## Files for review

1. `claims/lemmas/L-9304-selected-critical-line-factor-deflation.md`
2. `claims/lemmas/L-9305-vandermonde-normalized-modulus-minors.md`
3. `experiments/X-9302-selected-factor-modulus/verify_selected_factor.py`
4. `claims/observations/O-9301-pr71-selected-factor-exhaustive-scan.md`
5. synthetic certificate, summary, and tests

## Proof boundary

Exact:

- L-9304/L-9305 finite algebra after accepting the RH canonical-product interface;
- X-9302 rational interval operations;
- synthetic negative controls;
- test results.

Empirical:

- direct PR #71 completed-xi values used in the exhaustive scan;
- refined and approximate line-zero ordinates;
- all displayed PR #71 minimum values.

External obligations for a real negative:

- directed completed-xi production;
- directed critical-line zero isolation and multiplicity gates;
- independent backend reproduction;
- independent analytic review of the direct-xi canonical-product normalization.
