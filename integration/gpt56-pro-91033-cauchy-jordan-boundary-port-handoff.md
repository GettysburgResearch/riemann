# Handoff — compact arithmetic gate and exact critical boundary ports

## Frozen route

```text
repository: gfreund123/riemann
PR:         #396
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
RH status:  UNPROVED
```

This handoff is normative for the latest continuation and supersedes older frontier summaries on the branch where they differ.

## Review order

1. `claims/lemmas/L-91023-weighted-harris-fkg-all-green-jordan-hierarchy.md`
2. `claims/lemmas/L-91026-green-removal-is-one-explicit-boundary-density.md`
3. `claims/lemmas/L-91028-green-removal-is-positive-at-all-sufficiently-small-scales.md`
4. `claims/lemmas/L-91030-unit-atom-barrier-closes-all-scales-a-at-least-one-third.md`
5. `experiments/X-91024-corrected-green-removal-threshold/`
6. `claims/lemmas/L-91024-all-order-cauchy-storage-residuals-are-hardy-square-mixtures.md`
7. `claims/lemmas/L-91025-three-state-cauchy-allpass-is-a-symmetric-square.md`
8. `claims/lemmas/L-91031-completed-safe-side-cauchy-jordan-stinespring-factor.md`
9. `claims/refutations/R-91004-safe-positive-stinespring-measure-cannot-be-naively-continued-to-the-critical-boundary.md`
10. `claims/lemmas/L-91033-horizontal-contour-crossing-selects-exactly-zeros-deeper-than-the-cauchy-scale.md`
11. `claims/lemmas/L-91029-first-cauchy-storage-is-a-one-switch-compensated-wavelet.md`
12. `claims/lemmas/L-91032-every-finite-euler-factor-preserves-green-removed-cauchy-positivity.md`
13. final report `reports/gpt56-pro/2026-08-12-cauchy-jordan-boundary-ports.md`
14. inherited `L-91020/L-91021/L-91022/T-91007`

## Main DAG

```text
weighted logarithmic-integer Harris-FKG
 -> all Green divisions E_(s,m)>=0

all-order Cauchy storage density W_m
 -> canonical causal Hardy direct integral

three-state all-pass
 -> symmetric square of one two-state rotation

three-Green Jordan channel
 + sharp Cauchy numerator
 -> positive contact
  + positive arithmetic atoms
  + unique density B_(2a,a)

small-a scaling theorem
 + unit-atom large-a barrier
 -> B_(2a,a)>=0 outside one compact scale interval

prime-local preservation
 -> no finite bad Euler factor

positive rational/Gamma/Erlang convolution
 -> explicit safe-side Stinespring measure

horizontal contour to q=-1/2-a+ix
 -> deterministic stable ports
  + exactly the hyperbolic ports with zero depth d>a

absence of hyperbolic ports
 <-> RH.
```

## Mandatory correction

The first version of `L-91030` used

```text
zeta(1+s)>=1+2^(-1-s)+integral_2^infinity x^(-1-s)dx,
```

which double-counts part of the `n=2` range. That proof is invalid and has been removed.

The corrected theorem uses:

1. monotonicity of `G(s)=s zeta(1+s)` on `s>=2/3`, proved by a unimodal negative-tail bound;
2. an exact rational lower certificate at `s=2/3`:
   ```text
   (2/3) sum_(n<=30) n^(-5/3)+31^(-2/3)
      > 1.414214 > sqrt(2).
   ```

Reviewers should reject any stale text relying on the double-counted bound.

## Load-bearing joints

1. Weighted Harris is applied to two decreasing functions under the independent geometric prime-exponent product measure.
2. The all-Green power is exactly `q^(-(m+1))`.
3. The boundary contact after cubic Green removal is exactly `rho''(0)=1`.
4. The sole continuous density is
   ```text
   -c_s+(A+B)E_(s,0)+AB E_(s,1).
   ```
5. Concavity between knots and upward knot jumps justify reduction to left limits.
6. Small-scale vague convergence is upgraded pointwise using the one-sided slope law.
7. The corrected large-scale proof uses the exact X-91024 certificate.
8. The safe-side positive measure is not continued by ordinary exponential moments.
9. The critical substitution is `q=-1/2-a+ix`.
10. A zero of depth `d` is crossed exactly when `d>a`.
11. Deterministic Cauchy poles and source-dependent zero poles must not be conflated.
12. The finite density scans remain reconnaissance only.

## Exact status

```text
weighted all-Green Jordan hierarchy               PROPOSED COMPLETE
all-order Hardy target                             EXACT
symmetric-square state reduction                   EXACT
unique arithmetic boundary density                EXACT
small-scale arithmetic positivity                  PROPOSED COMPLETE
large-scale arithmetic positivity a>=1/3           PROPOSED COMPLETE
compact middle arithmetic gate                     OPEN
prime-local positivity preservation                EXACT
completed safe Stinespring factor                  EXACT CONDITIONAL
naive positive-measure critical continuation       REFUTED
critical residue-port dictionary                   EXACT
conservative Darboux/scattering boundary identity  OPEN
hyperbolic port exclusion                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```

## Binary rejection tests

Reject or repair the route if:

- a counterexample to the weighted FKG inequality is found;
- the corrected `s=2/3` rational certificate fails;
- an omitted distributional contact appears in Green removal;
- the density is negative in a rigorously claimed small/large region;
- the symmetric-square conjugacy fails;
- an ordinary safe-measure boundary limit is used to cross `q=-a`;
- a zero with `d>a` is omitted from the contour ledger;
- the absence of crossed hyperbolic ports is assumed rather than proved;
- any finite replay is described as proving RH.
