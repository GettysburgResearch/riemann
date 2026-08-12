# Handoff — weighted FKG and exact Cauchy Green removal

## Frozen stack

```text
repository: gfreund123/riemann
PR:         #396
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
RH status:  UNPROVED
```

## Review order

1. `claims/lemmas/L-91023-weighted-harris-fkg-all-green-jordan-hierarchy.md`
2. `claims/lemmas/L-91026-green-removal-is-one-explicit-boundary-density.md`
3. `claims/lemmas/L-91027-green-removal-is-unconditionally-positive-at-terminal-scales.md`
4. `claims/lemmas/L-91024-all-order-cauchy-storage-residuals-are-hardy-square-mixtures.md`
5. `claims/lemmas/L-91025-three-state-cauchy-allpass-is-a-symmetric-square.md`
6. `experiments/X-91023-weighted-fkg-hardy-green-removal/`
7. session report
8. parent files `L-91020/L-91021/L-91022/T-91007`

## Main dependency chain

```text
positive logarithmic-integer product measure
 -> weighted Harris-FKG
 -> E_(s,m)(t)>=0 for every Green order m
 -> phase-resolved safe-side PSD kernels

positive Cauchy storage densities W_m
 -> direct-integral causal Hardy-square target

three-state all-pass U_a
 -> fixed symmetric-square lift of one two-state rotation

three-Green centered Jordan channel
 + exact Cauchy numerator
 -> one positive contact
  + positive arithmetic atoms
  + one density B_(2a,a)(t)

B_(2a,a)>=0
 -> positive zero-Green arithmetic measure
 -> completed source-to-Hardy boundary colligation [still open]
 -> coefficient-one recurrence
 -> RH.
```

## Load-bearing review joints

1. The weighted Harris application must use two coordinatewise decreasing functions.
2. The left Riemann sum for the truncated logarithmic power must dominate the full integral to `e^t`.
3. The power of `q` in the all-Green Laplace transform must be `m+1`.
4. The scaling factor in the Hardy mixture must be `a^(m+2)`.
5. The fixed conjugacy `U=O Sym^2(R) O^T` must use the stated signs.
6. The boundary contact in the cubic Green-removal identity must be exactly `rho''(0)=1`.
7. The continuous density must be
   ```text
   -c_s+(A+B)E_(s,0)+AB E_(s,1).
   ```
8. The first-cell endpoint inequalities must remain strict for all `a>0`.
9. In the eventual bound, minima occur at knot left limits because the density is concave between knots and jumps upward.
10. The finite scan must remain classified as reconnaissance.

## Exact statuses

```text
weighted FKG for every decreasing test              PROPOSED COMPLETE
all finite Green divisions                          PROPOSED COMPLETE
phase-resolved safe kernels                         PROPOSED COMPLETE
continuous Hardy-square factorization               EXACT
three-state = symmetric square                       EXACT
unique arithmetic Green-removal density             EXACT
first-cell density positivity                       PROPOSED COMPLETE
explicit eventual positivity                        PROPOSED COMPLETE
all terminal scales a>=1/2                          PROPOSED COMPLETE
middle density 0<a<1/2                              OPEN
completed source-to-boundary Hardy intertwiner       OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```

## Binary rejection tests

Reject or repair this packet if:

- any weighted-FKG finite counterexample exists;
- the Green-removal numerator produces an omitted distributional contact;
- the density has a negative value in the rigorously claimed first or terminal regions;
- the symmetric-square conjugacy fails;
- an uploaded finite scan is described as an analytic proof;
- positivity of the arithmetic density is silently promoted to the completed critical-boundary theorem.
