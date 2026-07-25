# R-5601 — Long-double carrier phases cannot support any D-0801 bound at `T ~ 5e12`

Claim ID: R-5601
Title: The `numpy.longdouble` phase reduction used by the X-0801 stream carries
an uncertainty about 1300 times the quantity it is used to measure
Status: PROPOSED (refutation of a *method*, not of a mathematical claim)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: L-0801; L-5601
Scope: every D-0801 stream produced by `experiments/X-0801-piecewise-carrier-tail/stream.py`
Related counterexample candidates: none

## What is refuted

`experiments/X-0801-piecewise-carrier-tail/stream.py` computes the carrier
phase as

```python
phase = np.remainder(carrier * np.log(q.astype(np.longdouble)), TWO_PI_LD)
```

and its own metadata honestly records
`"phase_reduction": "numpy.longdouble product and remainder; float64 sin/cos"`
together with `"status": "EMPIRICAL_NOT_CERTIFIED"`.  The refutation is not that
the file overstates itself — it does not — but that **the resulting numbers are
too coarse to be informative at the target scale**, which had not been
quantified anywhere in the repository.  Any downstream text that treats the
`c=10^11` leading margin as a number known to several digits, or that treats the
resulting eigenvector as "the" minimizing vector, is unsupported.

## The a priori argument

An `x86` long double has a 64-bit significand.  At `c=10^{11}` and
`T = 4.70920\ldots\times10^{12}`:

- `\log q \le 25.33`, and `\log` at long-double precision already carries an
  absolute error near `25.33\cdot2^{-64}\approx1.4\times10^{-18}`, so
  `T\,\delta(\log q)\approx6.5\times10^{-6}`;
- the product `T\log q\approx1.19\times10^{14}` has a long-double ulp of
  `1.19\times10^{14}\cdot2^{-63}\approx1.3\times10^{-5}`;
- `TWO_PI_LD` itself is `2\pi` only to `\approx3\times10^{-19}`, and the
  quotient in the reduction is `\approx1.9\times10^{13}`, contributing another
  `\approx5.7\times10^{-6}`.

So the phase error is of order `10^{-5}` radians per term.  Since the total
amplitude is `B=\sum_q\Lambda(q)/(\pi\sqrt q)\approx2.0\times10^{5}`, the
triangle inequality allows the normalized prime Rayleigh value to be wrong by up
to `B\cdot10^{-5}\approx2`, against a leading margin of `2.7\times10^{-4}`.

## The measured discrepancy

The 50 committed discovery shards of
`experiments/X-2805-directed-prime-producer/results/target-c1e11/discovery/shards/`
were merged and compared, lag by lag, against the directed stream of O-5601
(same `T`, same `c`, same `K`, same term counts).

```text
shard coverage                 [2, 100000000001)   contiguous, no gap, no overlap
prime count                    4,118,054,813       identical
higher prime power count       28,156              identical
max_d |z_d|                    0.482806
sum_d |z_d|                    123.22
max_d |z_d^{ld} - z_d|         0.00220063          (at lag 1014)
sum_d |z_d^{ld} - z_d|         0.355147
```

The operator perturbation implied by the second-to-last line is

\[
 \|\hat S^{\rm ld}_K-S_K\|_2\;\le\;\eta_0+\sum_{d\ge1}\eta_d\;\approx\;0.355,
\]

which is `1.3\times10^{3}` times the certified margin `2.67\times10^{-4}`.  The
*enumeration* in those shards is therefore complete and correct — that part of
the work stands and was reused as a coverage cross-check — but the arithmetic
carries no bound.

## Why the reported eigenvalue nevertheless looked reasonable

The floating leading eigenvalue recorded in
`results/target-c1e11/vector/frozen-vector-b96.json` is
`4.351450833636324`; the directed value is `4.351452764865313`.  The difference
is `1.93\times10^{-6}`, i.e. about `0.7\%` of the margin — far better than the
worst case, because the `4.1\times10^{9}` phase errors are unstructured and
largely cancel inside a fixed 1024-dimensional quadratic form.

This is exactly the trap the repository's rule 2 is about.  A quantity can be
*empirically* close and still carry no bound; and the direction of the residual
bias is not neutral, because maximizing a Rayleigh quotient over a
1024-dimensional space lets the optimizer exploit noise, which biases the
computed `\lambda_{\max}` **upward** and the reported margin **downward**.  A
discovery run of this kind can therefore manufacture an apparently small margin,
which is the opposite of the safe direction for a counterexample search.

## Consequences for existing artifacts

1. `frozen-vector-b96.json` remains a perfectly valid *exact dyadic vector*.  Its
   coordinates are exact integers and nothing about them is refuted.  What is
   refuted is the claim, implicit in the run plan, that it is the vector that
   minimizes the complete directed form.  Its own `warning` field already said
   as much.
2. The `c=10^{10}` and `c=10^{11}` entries of the PR #37/#44 decade continuation
   should be relabelled: at `c \le 10^{8}` the long-double reduction gives about
   `1.5\times10^{-4}` absolute uncertainty against a margin of `6.6\times10^{-3}`
   (2% — usable for nomination), while at `c=10^{11}` it gives `O(1)` against
   `2.7\times10^{-4}` (useless).
3. The 50-shard architecture, coverage checks, and merge logic are unaffected
   and were independently confirmed here.

## Regression test

`experiments/X-5601-rigorous-carrier-stream/tests/test_stream.py::
test_longdouble_regression` reproduces the failure at `c=10^{7}` (where the
comparison is cheap) and asserts that the long-double stream differs from the
directed stream by more than `10^{-6}` per lag.  If a future numpy/libm ever
made the long-double path accurate, that test fails loudly rather than silently
validating a weaker method.

## Gap audit

1. This refutes a numerical method, not a theorem.  No claim in `claims/` is
   contradicted; several are given a sharper error budget.
2. The measured `\sum_d|\Delta z_d| = 0.355` is a comparison between two
   computations, one of which (mine) is itself only bounded by the L-5601 model.
   The model bound `2.83\times10^{-12}` is eleven orders of magnitude below the
   observed discrepancy, so the attribution is unambiguous.
3. `numpy.longdouble` is `float80` on this platform.  On a platform where it is
   `float64` or IEEE `binary128` the constants change; the argument, not the
   number, is what transfers.

## Suggested next attack

Every future D-0801 stream should be produced by the L-5601 decomposition or by
a directed-rounding kernel.  The cost is small — the directed run at `c=10^{11}`
took 316 seconds on four cores — so there is no longer a performance reason to
accept an unbounded phase.
