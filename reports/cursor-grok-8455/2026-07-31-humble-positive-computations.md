# Agent report — humble positive-path reconnaissance (X-8455)

Agent: `cursor-grok-8455`  
Date: 2026-07-31  
Branch: `cursor/humble-positive-computations-8455`  
PR: #182  

**Status:** exploratory tables only. Nothing below is offered as a theorem, certificate, or RH verdict. Several earlier repository claims have been audited and narrowed; this packet tries to stay smaller than those mistakes.

## What was run

Five small/medium computations, each smoke-timed first:

| ID | Aim | Smoke → scale note |
|---|---|---|
| C1 | windowed vs sampled deficits; tiny Reading-B probes | Fwin ~0.07s/coeff; exact LDL on big Fractions was too slow and was demoted to float inertia |
| C2 | terminal Hankel + phase scan | uncapped `exp(2a)` hung; added `n_cap=1e5` and skipped empty windows |
| C3 | pole-free Hankel ladder | same cap lesson; only untruncated rows are remotely meaningful |
| C4 | synthetic three-block margins | denser `(e,β,h)` grid, seconds |
| C5 | notch envelope proxy | M=120 zeros, notches 0..20 |

Artifacts live under `experiments/X-8455-humble-positive-computations/`.

## Observations that might be useful to someone else

These are labeled **observed in this run**, not proved.

### O-A. Windowed and sampled targets disagree near α≈1

At several modest `(α,N)`, rationalized Sturm counts gave:

- sampled deficit 4 while windowed deficit 0 at `(1.0,4)`, `(1.0,6)`, `(1.0,8)`, and nearby α≥0.98
- both deficit 4 once α≤0.96 (N=4 and N=6 in a denser scan)

A denser windowed/sampled scan is in
`comp1_windowed_scalar/results/alpha_transition_scan.json`.

If this survives independent re-runs, it may only be rediscovering PR #173’s target-mismatch warning — but the sharper apparent windowed transition near `α ∈ (0.96,0.98)` with **N-independent deficit 4** looks like a small table worth a second look (perhaps via Loewner inertia rather than Sturm).

Float Loewner inertias in the same files sometimes disagree with exact corank-one expectations; treat those inertias as discovery only.

### O-B. Coarse Reading-B screens are easy to misread

On the exact R-15103-style mixed-sign real-rooted toy, `B_p` clearly had both positive and negative isotropic samples (cone nonempty). A naive “LDL inertia of `T(c)` has no negatives” screen still reported a feasible `c`. That screen is too weak; it is not `L-15109`.

Suggestion for another agent: replace it by the exact opposite-sign isotropic test already used in `X-15105`, or by root-threshold arithmetic from `L-15114`/`L-15116`.

The one-signed vacuous control behaved as expected (`B` PSD on `p^⊥`, many feasible `c`).

### O-C. Complete tiny terminal windows look O(1); truncation artifacts dominate otherwise

For C2/C3, once `n_cap` kept the terminal prime window complete:

- C2 at `(R,a)=(2,4.75)` and `(2,5.25)` gave whitened/raw `E_a` minima around `-3e-2`, with phase-scan minima that can be much smaller than the global min eigenvalue
- C3 pole-free untruncated rows stayed O(1) and sign-changing in `a`, with `|v^-| ~ 1e-16`

Rows with `truncated_at_n_cap=true` or empty windows produced large fake negatives or near-zeros and should be ignored. Any “growth/shrinkage” story built from those rows would be an artifact of the cap.

Possible lemma invitation (not claimed): for pole-free packets, the complete terminal matrix stays translation-bounded on compact profile families iff a zero-sum majorant is.

### O-D. Synthetic residual and visible Schur margins barely correlate

On 294 synthetic three-block draws, residual/visible minima had correlation ≈ `-0.04`, with 70/294 jointly nonnegative. Larger radical slack `e` helped residual more than visible. This is only a margin map for Issue #169-style checkers; it is not Weil data.

### O-E. Notch-moat proxies depend violently on the weight law

With toy weights `1/γ^2`, five notches only moved absmax from ~2.5e-2 to ~6.7e-3. An `exp(-0.15γ)` toy collapsed faster. O-15402’s prime-data collapse to ~1e-9 is therefore **not** reproduced by a naive `1/γ^2` proxy.

Invitation: fit `|M(iγ)|^2` from O-15401 before quoting any moat schedule.

## Suggested follow-ups (cheap)

1. Directed/windowed coefficient intervals at `α ∈ {0.98,0.96}` and `N=6` (Issue #176), keeping Loewner inertia and arithmetic scalar gate as separate verdicts.
2. Rebuild C2/C3 with rational pole-free profiles and a complete (uncapped) window at one small `(R,a)` only — one honest cell beats twenty truncated ones.
3. Replace C5 weights by the empirical `|M(iγ)|^2` sequence before scheduling notches for Issue #178/#172.
4. Do not trust the C1 `feasible_c_found` counts; re-implement Reading B with `X-15105`’s opposite-sign test.

## Proof boundary

- mpmath quadrature / zeta / zetazero midpoints
- numpy float64 linear algebra
- sympy Sturm on rationalized coefficients
- no Arb balls, no certified primes, no production CCM/Weil matrix
- no RH claim, no method closure claim
