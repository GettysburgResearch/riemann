# M-15604 — Proof-producing phase-aware pole-free prime-bound pipeline

Claim ID: `M-15604`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15613`, `L-15614`, `T-15604`

## Objective

Produce one finite interval comparison

\[
 Q_G(x)-S_{\mathcal Z}(x)-T_M(x)
 \notin[-B,B]
\]

with every endpoint directed and every prime power present. Such a strict
comparison disproves RH.

## Stage 1 — freeze the window

Bind one exact window definition:

```text
base dyadic infinite convolution,
finite certified-zero notch factors,
physical translation,
convolution square,
pole-annihilating two-shift factor,
support endpoints,
Laplace-transform convention.
```

Verify exactly `g(1/2)=0` and `g(z)!=0` for `0<Re z<1/2`. Use the finite-spline/tail or self-similar evaluator of `L-15408`; FFT samples are discovery-only.

## Stage 2 — selected phase model

Choose a finite set of certified simple critical-line zeros. For each zero:

1. bind a directed ordinate ball and multiplicity;
2. evaluate `g(i gamma)` outward;
3. range-reduce `gamma*x` with directed arithmetic;
4. accumulate the exact conjugate-pair phase contribution.

Retain the first `M` trivial zeros similarly.

## Stage 3 — residual zero budget

Partition the remaining finite ordinate range. Each cell records:

```text
left/right rational endpoints,
total zero-count upper,
selected multiplicity already modeled,
transform-magnitude upper.
```

Use exact Turing counts where available. Otherwise use `upper count at right - lower count at left`, never a difference of two upper bounds. After the finite partition, use either a derivative-L1 tail and `L-15613.16` or the universal product power bound `L-15613.20`--`L-15613.22`.

## Stage 4 — complete prime producer

For exact translation `x`, enumerate all prime powers in

\[
 e^{x-B}\le n\le e^{x-A}.
\]

For every event certify `Lambda(n)`, `sqrt(n)`, `u=x-log n`, and `G(u)`, then accumulate outward. The producer fails closed on a manifest gap, duplicate, unresolved logarithm range, or unsupported window cell.

## Stage 5 — exact comparison

Export rational endpoints to `X-15605`. Possible verdicts are:

```text
CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_POSITIVE
CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_NEGATIVE
FINITE_VALUE_CONSISTENT_WITH_RH_BOUND
UNRESOLVED_BOUNDARY_OVERLAP
```

## Stage 6 — matrix escalation

If a scalar violation is absent, build a real two-profile packet and compute the complete centered terminal matrix. Use `L-15614` to model selected zero phases as matrices and freeze any suspicious direction to rationals.

## First target

Use `O-15607`:

```text
five-notch universal window,
x=8578244975439/549755813888,
first 100 certified positive zeros,
complete 64,542-term prime-power annulus,
first 40 trivial zeros,
product tail beyond the 100th zero.
```

Run at two directed working precisions and require nesting. Independently replay both the prime side and selected zero side.

## Non-negotiable gates

- No midpoint zero is a notch certificate.
- No FFT value enters a final interval.
- No primes-only manifest is accepted.
- No shell upper is formed as upper-minus-upper.
- No finite violation is promoted without independent explicit-formula review.
- A passing finite value is not evidence for RH beyond that declared bound.
