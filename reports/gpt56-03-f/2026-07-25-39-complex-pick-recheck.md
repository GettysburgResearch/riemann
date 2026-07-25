# Agent report — triple recheck of the promising Pick candidate

Agent: `gpt56-03-f`  
Issue: #39 continuation  
Branch: `agent/gpt56-03-f/39-complex-pick-recheck`  
Date: 2026-07-25  
Status: promising screen refuted more strongly; no counterexample

## Objective

Reopen the earlier negative Pick nomination without trusting its recorded
refutation. The original audit proved one frozen real direction positive, but
that leaves three possible failure modes:

1. the true complex minimum direction might differ;
2. higher precision might move the eigendirection;
3. another matrix inside the primitive rectangle box might still be negative.

The pass therefore targeted the complete Hermitian matrix and every admitted
primitive value, not merely the old vector.

## Repository context

The work stacks on PR #56, which supplied:

- exact dyadic points above the verified zero height;
- directed FLINT Riemann--Siegel balls for `zeta,zeta'`;
- two independently assembled completed `xi'/xi` rectangles;
- denominator-zero gates;
- a standard-library exact real-contraction checker;
- a 128-bit 65-height grid and a 192-bit ambiguous-block escalation.

Parallel developments now include cross-height packets, feature-cone closure,
matched-pole scans, and the recovered-vector D-0801 directed carrier pipeline.

## New exact checker

`verify_complex_pick.py` independently reconstructs the same-height complex
Pick form. For a Gaussian-rational vector `v`, it computes

\[
 \alpha_j=\overline{v_j}\sum_k\frac{v_k}{x_j+x_k}
\]

and contracts

\[
 v^*Kv=2\operatorname{Re}\sum_j\alpha_jF(s_j)
\]

against the real and imaginary primitive intervals. It also implements an exact
whole-matrix certificate using rational midpoint rectangles, a row-sum
perturbation bound, and Gaussian-rational `LDL^*` pivots.

The checker imports no special-function or discovery code.

## Original finalist: stronger-than-refutation result

Exact point set:

\[
 T=\frac{20225875608342450317715}{2^{32}},
\]

\[
 x\in\{2^{-17},2^{-15},2^{-13},2^{-11},2^{-10},2^{-9},2^{-7},2^{-5}\}.
\]

### Old real direction

The retained 192/256/384/512-bit ladder is strictly positive and converges after
normalization to approximately

```text
+6.7369660275844976e-37.
```

### True full-complex direction

The complete 512-bit midpoint matrix has positive minimum eigenvalue
approximately

```text
+2.1247974259266701e-41.
```

The corresponding frozen Gaussian-rational direction has a strictly positive
exact contraction, with normalized interval width below `9e-148`.

### Whole matrix box

Choose

```text
delta = 2^-136.
```

The checker reconstructs eight positive exact pivots for `M-delta I`. The
complete primitive rectangle uncertainty has operator-norm upper bound

```text
E < 5.758e-147.
```

Therefore

\[
 K\succeq(\delta-E)I\succ0
\]

for every matrix inside the declared boxes, with lower margin above
`1.1479e-41`.

This proves that the original refutation was not premature. The previous report
was simply weaker than the whole-matrix conclusion now available.

## Fourteen-block full-complex replay

The initial 128-bit grid contained many negative midpoint eigenvalues caused by
near-rank cancellation. A retained 192-bit FLINT artifact covered fourteen of
the escalated blocks:

```text
workflow run     30009653881
artifact ID      8564591455
artifact digest  646ff50e6191d68700bc3bb9a2ad21010241f51ad384d9ee36078a55d6f857a3
```

For each block, I reconstructed the full complex 128-bit midpoint matrix, froze
its minimum direction as Gaussian integers at scale `2^256`, and contracted the
same vector against the 192-bit rectangles.

```text
blocks                         14
strictly positive directions   14
strictly negative directions    0
unresolved directions           0
```

The retained positive values range from roughly `1.3e-38` to `1.0e-34`.

## Strongest remaining 128-bit screen

The full-complex scan exposed one stronger midpoint negative not present in the
old real-only channel table:

\[
 T=\frac{20225875608341108140435}{2^{32}}
   =T_0-\frac{15}{32}.
\]

The displayed 128-bit midpoint minimum was

```text
-2.626429492911995e-33.
```

A `2^256` Gaussian-integer direction was frozen before reevaluation. The
original boxes give an unresolved interval of approximate radius `5.7e-30`, so
they neither certify nor refute the sign.

New GitHub Actions jobs failed before publishing a first step or artifact. An
unchanged previously successful FLINT job failed in the same manner, so no
mathematical or code conclusion was drawn from the infrastructure failure.

I then used an independent ordinary-high-precision Riemann--Siegel
implementation to evaluate the same eight exact points and vector:

```text
50 digits   +1.1392326587787596e-33
60 digits   +1.2260274370297923e-35
70 digits   +1.2260274655534929e-35
```

The independently recomputed matrix minimum is positive and stable at 60/70
digits near

```text
+1.2259907375435524e-35,
```

while the second eigenvalue remains near `+4.16e-26`. This refutes the
midpoint nomination empirically. It is not mislabeled as a directed certificate.

## New proof unit

`L-7101` proves the reusable whole-matrix criterion:

1. exact `LDL^*` positivity of `M-delta I`;
2. exact row-sum operator bound `||K-M||_2<=E`;
3. `E<delta`;
4. hence `K>0` for every matrix inside the supplied primitive boxes.

This closes an entire finite complex vector space with one compact object.

## Refutation record

`R-7101` records that:

- the old real screen is positive;
- the true full-complex direction is positive;
- the entire original matrix box is positive definite;
- all fourteen earlier ambiguous complex directions are positive at 192 bits;
- the new `j=-15` screen stabilizes positive under an independent 60/70-digit
  computation.

No negative directed interval remains and no `Z-####` identifier is allocated.

## Strategic pivot

The same-height value-only table is now a poor place to spend additional
optimization effort. Concurrent exact feasible-anchor work independently closes
the broader finite dual cone over this feature table.

The two serious offensive directions are now:

1. **enlarge the xi feature space** with cross-height complex packets or direct
   jets;
2. **complete and then generalize the carrier pass**: produce directed Toeplitz
   coefficient boxes once, postselect vectors or low-rank Gram portfolios, and
   search threshold/cell geometry rather than merely certifying a known
   positive-looking mode.

The recovered `c=10^11` carrier vector has an ordinary positive leading margin
near `2.69e-4`, while the nonprime correction gate is below `2.5e-10`. Completing
its directed pass is valuable as a trusted-base control, but a counterexample
will more likely require a new threshold cell, carrier ordinate, or postselected
subspace.

## Files added

- `claims/lemmas/L-7101-rational-midpoint-radius-pick-pd.md`;
- `claims/refutations/R-7101-full-complex-pick-midpoint-ghosts.md`;
- `experiments/X-3904-complex-pick-recheck/verify_complex_pick.py`;
- `experiments/X-3904-complex-pick-recheck/rs_complex_candidate.c`;
- exact tests, summaries, workflow, README, and this report.

## Proof boundary

- Whole-matrix and fixed-vector algebra: exact rational arithmetic.
- Original and fourteen-block primitive rectangles: retained directed FLINT
  artifacts.
- New `j=-15` replay: independent ordinary high precision, not interval
  arithmetic.
- Parent completed-xi normalization and Pick implication: retain current
  statuses.
- No RH conclusion is inferred from positive finite objects.
