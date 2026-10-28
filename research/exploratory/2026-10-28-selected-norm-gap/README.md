# Endpoint gap in the selected-norm contraction

Status: exploratory audit of one scalar step. No new zero-free region is proved; the imported analytic reflection and tracker theorem have not been reviewed or replayed.

Source: Joseph Bebel, [QuasiRiemannTracker PR #93](https://github.com/GTimG/QuasiRiemannTracker/pull/93), inspected at head `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`. The result is a submitted claim and remains subject to the tracker's review and admission. The load-bearing files for this observation are `src/Candidate/Local/Qrh/JointDetector/Contraction.lean`, `SelectedNormIteration.lean`, `NaturalSelectedNorm.lean`, `FineNaturalSelectedNormContract.lean`, and `AdaptivePrice.lean` under `submissions/2026-10-28-joint-detector-fine-chain/` at that head.

The scalar contraction is

```
r(delta) = (1-delta)/delta,
e_0(delta) = 1+delta,
e_(n+1)(delta) = 2*delta-1+r(delta)*e_n(delta).
```

The source explicitly proves `e_n(delta)=delta+r(delta)^n`. Therefore, for each fixed `n`, `e_n(delta)-delta` tends to one as `delta` decreases to `1/2`. No fixed depth makes `e_n(delta)<delta+epsilon` uniformly over all `delta>1/2` when `epsilon<1`. At `delta=1/2+eta`, with `0<eta<1/2`, the exact necessary and sufficient inequality is

```
n > log(1/epsilon)/(2*atanh(2*eta)),     0 < epsilon < 1.
```

This follows from `r=(1-2*eta)/(1+2*eta)` and `-log r = 2*atanh(2*eta)`. In particular the required depth is asymptotic to `log(1/epsilon)/(4*eta)` as `eta` tends to zero. For `eta=10^-6` and `epsilon=10^-6` it is approximately 3.454 million, for the scalar recurrence alone. These numbers describe the existence argument, not an assertion that Lean performs this many kernel steps; no bound on constants or mesh size is inferred.

The squarefree all-source norm proved in `SelectedNormIteration.lean` assumes a fixed positive `gap` and `delta>=1/2+gap`. The fine natural aggregate interface uses `delta>=500001/1000000`; downstream the adaptive count uses a separate amplitude cutoff `1001/2000`. The gap cannot simply be replaced by zero through the existing *fixed-depth* contraction. A direct candidate improvement would be an endpoint all-source selected estimate of the form `C Z^epsilon (L+sqrt(B L))`, with the same early mesh, common coefficient masks, natural roots, arbitrary source sets, and fixed slot-width lower bound as the existing contract. This is an open input here, not a consequence of the scalar calculation. Another possible route is a fully quantitative near-endpoint estimate controlling the reflection constants and mesh in depth and gap; growing depth with `Z` cannot be justified using the source's current existential constants alone.

The scalar barrier does not establish that an endpoint operator estimate is false or that any zero-free boundary is optimal. Other methods may avoid it; in particular, a selected norm at the endpoint is not an automatic statement about the original L-functions until its full detector, price, low-bound and return interfaces are supplied.
