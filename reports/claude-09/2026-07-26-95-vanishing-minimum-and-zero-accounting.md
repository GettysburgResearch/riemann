# claude-09 — vanishing screw minimum and the zero-accounting ratio

```text
Agent:   claude-09
Issue:   #95  (continuation of the gpt56-08 screw prime-knot route)
Branch:  claude/screw-toeplitz-zero-deflation-3o18bz
         (based on agent/gpt56-08/95-screw-prime-knot, draft PR #98)
Date:    2026-07-26
```

## Starting hypothesis

The handoff proposed continuing the `L-9504`/`L-9505` program: push
`lambda_min(H^(n)(h))` lower by full Toeplitz optimization, deflate certified
critical-line zero bins, reoptimize the residual, and look for a sign change.

I began by trying to reproduce the branch's numbers before extending them, and
by attacking PR #98's unresolved doubt #1 — the `D-9501` normalization audit —
since every downstream number depends on it.

That audit passed.  But reproducing the mode surfaced a structural problem with
the progress metric the program is built on, and the session turned into
(i) an audit, (ii) a negative result about the metric, and (iii) a replacement
statistic.

## Approaches attempted

1. **Normalization audit of `D-9501.1`** by two independent routes — a mean/sup
   test against the unconditional constant `2 + gamma_E - log(4 pi)`, and an
   entrywise comparison of the prime-side Toeplitz symbol against the same
   symbol resummed over computed zeros.  Both passed.
2. **Independent reproduction** of the `X-9502` frozen mode and attribution
   table, from the claim files rather than the code, with no shared library.
   Both reproduced.
3. **Analysis of the progress metric.**  Led to `L-9506`.
4. **Design and first evaluation of a scale-free replacement.**  Led to
   `L-9507`.
5. **Feasibility assessment of the `L-9505` two-sided box.**  Negative.

## New results

### L-9506 (PROPOSED) — the minimum is monotone and vanishing

Three parts, the first two unconditional:

- `H^(n)(h)` is the leading principal submatrix of `H^(n+1)(h)`, so by Cauchy
  interlacing `lambda_min(H^(n+1)(h)) <= lambda_min(H^(n)(h))` for every `n`
  and `h`.  **The minimum is guaranteed to decrease.**
- The all-ones increment vector `b` corresponds to `c = e_0 - e_n` and gives
  the exact identity `b^T H^(n)(h) b = 2 Psi(nh)`, hence
  `lambda_min(H^(n)(h)) <= 2 Psi(nh)/n`.
- Under RH, `0 <= Psi <= 2 S_2` with `S_2 = sum_gamma gamma^{-2} = 0.0462111...`,
  so `lambda_min(H^(n)(h)) <= 4 S_2/n < 0.1849/n -> 0`.

**Consequence.**  A search that reports a smaller minimum at larger `n` has
produced no evidence about RH; the decrease is forced in advance.  A search of
the form "increase `n` until the minimum goes negative" cannot terminate under
RH, and its margin shrinks like `1/n` while the prime-side cutoff needed to
certify row `n` grows like `e^{nh}` — at `h = log(2)/3`, like `2^{n/3}`.

This does **not** refute `L-9504` or `L-9505`.  Their finite implications
remain correct, and a negative `W_h(c)` at any fixed `n` would still be a
disproof.  What it refutes is the reading of a small positive minimum as
progress — including the continuation report's adaptive-deflation table, whose
residual minimum falling from `1.40e-05` to `5.06e-06` is the same forced decay
seen through a different lens.

### L-9507 (PROPOSED) — the zero-accounting ratio

For a finite set `Gamma` of positive ordinates with certified multiplicities,
let `Z_Gamma(h) = 2 sum Re(u_gamma u_gamma^*)`, a real symmetric PSD Toeplitz
matrix with entries
`8 sum_gamma sin^2(gamma h/2) cos((j-k) gamma h)/gamma^2`.
RH implies `H^(n)(h) - Z_Gamma(h) >= 0`, hence

```text
rho_Gamma := lambda_max(Z_Gamma, H^(n)(h)) <= 1.
```

A directed certificate of `rho_Gamma > 1` disproves RH.  The bound is sharp:
with `Gamma` the full ordinate set, `Z_Gamma = H` and `rho = 1` exactly.

Why this is the right target: it is invariant under the `L-9506` vanishing; it
needs only a **lower** count of zeros in bins, with no completeness requirement
and no zero-tail bound; and it is a single generalized eigenvalue rather than a
deflate-and-reoptimize loop.

### X-9503 (EMPIRICAL) — the numbers

```text
D-9501.1 normalization audit                       PASS (two routes)
  mean Psi / (2+gamma_E-log 4pi)                   1.000975
  max Psi / bound                                  0.745896
  entrywise prime-side vs zero-side, max diff      3.849e-03  (= the tail)
  gpt56-08 m=0 folding, max diff                   3.553e-15

X-9502 reproduction
  lambda_min(H^(53)(log2/3))                       1.9285536890e-05
    vs X-9502's 1.9285536220e-05, rel. diff        3.48e-08
  top-5 attribution                                44.33%  (X-9502: 44.3%)
  top-20 attribution                               63.93%  (X-9502: 63.5%)
  five influential ordinates                       agree to ~1e-11

L-9506 evidence (h = log2/3, n = 2..60)
  lambda_min non-increasing                        True, every n
  identity b^T H b = 2 Psi(nh), rel. error         0.0, every n
  n^2 * lambda_min for n >= 36                     ~0.054  (EMPIRICAL only)

L-9507 evidence (n = 53, h = log2/3, 649 zeros < 1000)
  rho_Gamma                                        0.993360504
  deficit                                          6.639e-03
  same ratio for the frozen lambda_min eigenvector 0.727487
  any rho > 1 observed                             NO
```

## Candidate counterexamples

**None.**  No `Z-####` is assigned.  `rho_Gamma <= 1` held at every `T` tested;
the results are consistent with RH.  Nothing here is a counterexample, and
nothing here proves anything infinite about RH.

## Certified computations

**None.**  This container has no numerical libraries at all — `numpy`,
`mpmath`, `sympy`, `gmpy2`, `python-flint` and `scipy` are all absent, and
there are no GMP/MPFR/FLINT headers.  Every number in `X-9503` is IEEE binary64
with round-to-nearest.  There is no directed rounding, no interval arithmetic
and no certified enclosure anywhere in this session's output.

The same absence means `experiments/screw_toeplitz_mpfr.c` **cannot be built or
run in this container**.  The `X-9502` 128/192/256-bit directed artifacts were
read but not reproduced; this session confirms the binary64 value they enclose,
not the endpoints themselves.  Their independent replay remains open.

## Failed approaches / negative results

1. **The `L-9505` two-sided box is not reachable at these parameters.**  The
   excess-positive mode needs `4 n S_T` below the Rayleigh scale.  At `n=53`
   against `1.9e-05` that needs `T ~ 10^8`, i.e. about `2.5 x 10^8` certified
   bins *plus* exact completeness of coverage.  At `T=1000` the box endpoint
   exceeds the target by a factor `2.1 x 10^4`.  Recorded so no one re-derives
   it.  `L-9507` was written to avoid the requirement.
2. **Deflating against the frozen `lambda_min` eigenvector optimizes the wrong
   direction.**  That eigenvector exposes `72.75%` of the form; the optimal
   direction exposes `99.34%`.  The `X-9502` ranking of "most influential
   zeros" is a ranking against a badly suboptimal `b`.
3. **Driving `n` upward is counterproductive**, per `L-9506`.  The `n=59`
   binomial and `n=53` Toeplitz "records" are on a forced curve.

## Potential errors

- `L-9506(a)` and `L-9506(b)` are elementary and I am confident in them; (b)
  was checked against the assembled matrix to `0.0` relative error at every
  tested `n`.  `L-9506(c)` inherits the `D-9501` import.
- `L-9507(a)` follows from `L-9504.11`, which is `L-9504`'s RH-conditional Gram
  expansion.  If `L-9504.11` has a convention error — in particular in the
  `u_gamma` vs `conj(u_gamma)` replacement its proof waves through — then
  `L-9507`'s matrix would be conjugated.  For **real** `b` this does not change
  the ratio, which is what `X-9503` computes, but a complex-`b` certificate
  would need the convention pinned down.  Test A2 passing entrywise is strong
  evidence the convention is right.
- The `rho_Gamma` computation goes through a Cholesky congruence of a matrix
  with condition number `6.3e4`.  I did not compute a backward-error bound.
  Given `rho = 0.9934` is far from `1`, this does not affect the conclusion,
  but it would matter for any value near `1`.
- The zero ordinates are floating sign changes, not certified bins.  The
  `S(T) = +0.38` count check argues none were missed but does not prove it.
- Part A probes `t <= 14` only; a normalization defect appearing only at large
  `t` would escape it.

## Files changed

```text
added   claims/lemmas/L-9506-screw-toeplitz-minimum-vanishing.md
added   claims/lemmas/L-9507-zero-accounting-ratio.md
added   claims/experiments/X-9503-independent-audit-and-zero-accounting.md
added   experiments/screw_lib.py
added   experiments/screw_zeta_zeros.py
added   experiments/screw_audit_and_ratio.py
added   experiments/results/X-9503-screw-audit-ratio/audit.json
added   experiments/results/X-9503-screw-audit-ratio/zeros1000.json
added   reports/claude-09/2026-07-26-95-vanishing-minimum-and-zero-accounting.md
```

No file authored by `gpt56-08` was modified.

## Claims affected

```text
D-9501   audited, normalization confirmed by two independent routes.
         PR #98 unresolved doubt #1 is resolved in the affirmative.
L-9504   used unchanged.  Its gap audit already noted that "a small positive
         eigenvalue is not a counterexample"; L-9506 upgrades that remark to a
         theorem with a rate, and to a statement that the decrease is forced.
L-9505   unchanged and correct, but its two-sided box is shown to be
         numerically unreachable at n=53.  Its fixed-vector bound
         (L-9505.10-11) is reused by L-9507(d).
X-9502   independently reproduced in binary64.  Its directed MPFR endpoints
         remain unreproduced (no MPFR in this container).
L-9506   NEW, PROPOSED.
L-9507   NEW, PROPOSED.
X-9503   NEW, EMPIRICAL.
```

## Recommended next actions

1. **Optimize over `h`, not `n`.**  `L-9506` makes larger `n` actively
   counterproductive, but `h` is free and enters `Z_Gamma` through
   `sin^2(gamma h/2)`, which controls how visible each zero is.  Maximize
   `rho_Gamma(n,h)` over exact rational `h` at modest `n` with a fixed
   `Gamma`.  Cheapest high-information experiment available.
2. **If `sup_h rho_Gamma` stays well below `1`, record it as a negative result
   bounding the whole arithmetic-progression route.**  That is worth more than
   another record-small eigenvalue.
3. **Certify bins for the zeros the *optimal* `b` loads**, not the ones the
   frozen `lambda_min` eigenvector loads.  The Arb request posted to Issue #84
   for indices `121, 60, 207, 105, 244` is aimed at the wrong direction and
   should be re-derived from `L-9507`'s optimizer before anyone spends
   certification effort on it.
4. **Settle the `Theta(n^{-2})` rate** in `L-9506`, or leave it labelled
   EMPIRICAL.  The symbol of `H^(n)(h)` is the atomic measure
   `sum_gamma 4 sin^2(gamma h/2) gamma^{-2} delta_{gamma h mod 2 pi}`; this is
   the least eigenvalue of a Toeplitz matrix of a singular measure.
5. **Independently replay the `X-9502` MPFR artifacts in a container that has
   GMP/MPFR.**  Still open.

## Organizational improvement ideas

1. **A claim's progress metric should be audited like its arithmetic.**  This
   branch carried a metric — "smallest positive mode" — whose decrease is
   forced by Cauchy interlacing, and three reports treated shrinkage as
   progress.  A one-line entry in the claim template, *"why is this quantity
   not forced to move in the reported direction?"*, would have caught it before
   the MPFR producer was written.  Proposed as `M-9502` if the integrator
   agrees.
2. **Record the container's numerical capabilities in the experiment file.**
   `X-9502` is a directed MPFR certificate that cannot be rebuilt in the
   default container.  The environment block should state what was *available*,
   not only what was used, so a later agent knows before starting whether a
   replay is possible.
3. **Distinguish "reproduced the value" from "reproduced the certificate"** in
   the verification ledger.  I reproduced `X-9502`'s binary64 value to `3.5e-8`
   and none of its directed endpoints; those are very different verification
   states and the current ledger has one column for both.
