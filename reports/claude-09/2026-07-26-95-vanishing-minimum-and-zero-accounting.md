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

### X-9504 (EMPIRICAL) — the deficit law, and the bound on the route

Having built the right statistic, I measured what it would take to close it.

```text
deficit vs T   (n=53, h=log2/3)      1 - rho ~ K * S_T,  K = 3.434
                                     flat over T in [600,1000], spread 0.438
deficit vs n   (h=log2/3, T=1000)    1 - rho ~ 0.0651 * n^(-0.582)
deficit vs h   (n=40, T=1000)        minimum at h = pi/gamma_1 = 0.222261,
                                     deficit 4.62e-03 vs 7.47e-03 at log(2)/3
```

The deficit is the unaccounted zero tail and nothing else: the constant `K` is
flat, so no choice of direction `b` recovers the tail.  Inverting the two laws:

```text
deficit 1e-12  needs  T ~ 3.3e13   (~1.5e14 certified zero bins)
deficit 1e-12  needs  n ~ 3.8e18   (prime cutoff e^(8.8e17))
```

with `n` additionally capped near `90` by any `10^9`-entry prime table.

**Both knobs of the arithmetic-progression route are out of reach.**  I do not
expect a finite RH witness from arithmetic-progression screw filters at any
step `h`.  This bounds the *route*, not `L-9504`, `L-9505` or `L-9507`, which
remain correct.

One genuine structural finding on the way: `h = log(2)/3` is a poor spectral
choice.  It was picked in `X-9502` because it makes the prime-power threshold
the exact integer predicate `q^3 <= 2^k` — a real advantage for exact replay,
but an arithmetic convenience, not a spectral one.  The lowest-zero resonance
`h = pi/gamma_1` improves the deficit by a factor `1.6-1.8`, because `gamma_1`
carries by far the largest `gamma^{-2}` weight and `sin^2(gamma_1 h/2)` is the
weight with which it enters `Z_Gamma`.  The analogous resonances for
`gamma_2, gamma_3, gamma_4` do not help, so the effect is specific to the
lowest zero.  My first guess at the mechanism — "maximize the total mass
`2 Psi(h)`" — is wrong: `Psi` is slightly smaller at `pi/gamma_1` than at
`pi/gamma_2`.


### L-9508 / X-9505 / X-9506 (second pass) — the obstruction is the weight, not the route

Surveying the repository turned up a large **zero-deflation cluster** sharing
one shape — issues #84, #93, #121, #137 and PRs #90, #96, #97, #99, #100, #101,
plus `L-9505` here.  All certify critical-line zeros, subtract them from an
RH-nonnegative quantity, and hunt for a negative residual.  Several are
separately commissioning certified bins at real cost.

`L-9508` isolates what such a route can detect.  If RH gives
`Q = sum_gamma w(gamma)` with `w >= 0`, and `Gamma` is certified, then the test
fires exactly when the relative discrepancy `delta` exceeds the uncertified
tail fraction `F_Gamma`.  Precision cannot push the threshold below `F_Gamma`
and zero certification cannot push it below the enclosure width: the two costs
bound different terms and do not trade.  `F(T)` is then fixed by the decay of
`w`, and in the heavy band each decimal digit of sensitivity costs a factor
`10` in certified zeros.

`X-9506` measures the bands (target deficit `1e-12`):

```text
1/gamma^2  (screw; xi'/xi Pick at a point)   F(1000)=4.2e-02   T ~ 2.2e14   1.1e15 zeros
Weil, C^0  test function (sinc^2)            F(1000)=3.6e-02   T ~ 1.9e14   9.2e14 zeros
Weil, C^2  test function (sinc^4)            F(1000)=1.0e-05   T ~ 2.8e05   4.3e05 zeros
Weil, C^6  test function (sinc^8)            F(1000)=3.4e-12   T ~ 1.2e03   8.1e02 zeros
Weil, C^10 test function (sinc^12)           F(1000)=6.8e-20   T ~ 2.2e02   8.8e01 zeros
```

Eighteen orders of magnitude, driven purely by smoothness.  The screw route is
pinned to `gamma^{-2}` by Krein's normalization — the slowest decay for which
the expansion converges — so its deflation is structurally blocked.  This
reproduces the `X-9504` order of magnitude by an independent method
(`2.2e14` vs `3.3e13`).  A `C^0` test function puts a Weil route in the *same*
band; `C^6` needs `812` zeros.  **Smoothness, not search, is the decisive
design variable**, and in the light band the binding constraint moves off zero
certification entirely and onto arithmetic-side precision.

`X-9505` closes the last geometric knob on the screw route.  `X-9504`'s
recorded next attack was to leave the equally-spaced cone; `L-9501` supplies
the general-node form.  Optimizing node positions freely (warm-started from the
best arithmetic set, with a conditioning guard) buys a factor `1.03-1.28` over
equal spacing, with no trend in `m`:

```text
   m      rho arith       rho free    gain
   6    0.982147760    0.982704834   1.032
  14    0.988714440    0.990374136   1.172
  24    0.993475814    0.994913993   1.283
```

The mechanism is that `P(gamma) = sum_j c_j e^{i gamma t_j}` is an exponential
polynomial — almost periodic, bounded, non-decaying — so `|P|^2/gamma^2` keeps
an irreducible `gamma^{-2}` envelope for *every* finite node set.  Nodes
reshape the almost-periodic factor; they cannot change the decay class.

Two methodology errors from my first version of `X-9505` are recorded in the
claim file: warm-starting the free search from a fixed rather than the best
arithmetic spacing (which produced a spurious gain of `0.945`, i.e. optimizer
failure read as geometry), and the absence of a conditioning guard, which let
the optimizer run to nearly-coincident nodes where the ratio is noise.

Net: every geometric knob on the screw route — `n`, `h`, full node freedom —
is a bounded factor.  Only `T` moves the deficit, and only as `log(T)/T`.

## Candidate counterexamples

**None.**  No `Z-####` is assigned.  `rho_Gamma <= 1` held at every `T`, `n`
and `h` tested; the results are consistent with RH.  Nothing here is a
counterexample, and nothing here proves anything infinite about RH.

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
added   claims/lemmas/L-9508-deflation-sensitivity-equals-tail-fraction.md
added   claims/experiments/X-9504-zero-accounting-deficit-law.md
added   claims/experiments/X-9505-free-node-screw-witnesses.md
added   claims/experiments/X-9506-deflation-tail-budget.md
added   experiments/screw_free_nodes.py
added   experiments/deflation_tail_budget.py
added   experiments/results/X-9505-screw-free-nodes/free_nodes.json
added   experiments/results/X-9506-deflation-tail-budget/budget.json
added   experiments/screw_deficit_law.py
added   experiments/results/X-9504-screw-deficit-law/deficit.json
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
X-9504   NEW, EMPIRICAL.  Bounds the arithmetic-progression route.
L-9508   NEW, PROPOSED.  Deflation sensitivity = tail fraction; ranks the
         repository's whole deflation cluster by weight decay.
X-9505   NEW, EMPIRICAL.  Free nodes buy only 1.03-1.28x; closes the last
         geometric knob on the screw route.
X-9506   NEW, EMPIRICAL.  Tail-fraction budget by weight class.
```

## Recommended next actions

Items 1 and 2 of my original list were carried out within this session and
became `X-9504`; `sup_h rho_Gamma` does stay well below `1`, and the resulting
bound on the route is recorded there.  What remains:

1. **Leave the arithmetic-progression cone.**  `L-9504`'s cone is the
   equally-spaced one, whose Gram vectors are geometric progressions in
   `e^{i gamma h}`; the `X-9504` deficit law is a statement about that
   structure.  General nodes `t_1,...,t_m` give Gram vectors
   `(e^{i gamma t_j})_j` — arbitrary frequency sampling — and the law does not
   apply.  `L-9501`'s three-value determinant and `L-9502`'s Gaussian kernel
   already live outside the cone and were never pushed.
2. **Test multi-step combinations.**  Several steps `h_1,...,h_r` at once:
   tail contributions decorrelate across steps while low-zero contributions can
   be made to add.  Whether that beats `K S_T` is open and is cheap to test
   with the code now in the repository.
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
