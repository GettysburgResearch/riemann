# M-0601 — Event-directed cutoff-free Weil search

Proposal ID: M-0601  
Status: PROPOSED  
Authoring agent: `gpt56-01-a`  
Created: 2026-07-22  
Issue: #8, continuation of #1

## Problem with the previous search

A grid containing only integer cutoffs can sample a new prime-power term exactly
where that term vanishes. A sparse log grid can also miss narrow interior
avoided crossings. Recomputing every dense cell at proof precision is too
expensive, while finite-`T` shortcuts can create spurious negatives.

## Proposed procedure

1. Enumerate prime powers exactly and partition the path by their log cutoffs.
2. At each left endpoint, compute the smallest eigenpairs and the exact endpoint
   overlap `M_0=r_N^T v`.
3. Rank events using the frozen susceptibility
   `r_N^T Q_N(q)^{-1}r_N`, but never treat its predicted crossing as a result.
4. Search each interval in `u=log(c)` with endpoint-biased and adaptive samples.
5. Search the full even sector and pole-neutral variants separately. Use
   moment-neutral offsets adapted to `L-0602` rather than reusing first-order
   schedules.
6. Escalate precision automatically when the value is small relative to the
   entry norm or changes sign between runs.
7. Round a stable negative eigenvector to a low-height dyadic vector.
8. Send only that fixed object to an independent cutoff-free ball assembler and
   the exact rational Rayleigh verifier from X-0001.
9. Require independent analytic normalization review and a second numerical
   backend before allocating a `Z-####` ID.

## Tiny-support extension

Use `L-0604` to evaluate `c=exp(L)` close to `1`, where the direct correction
series would take `O(1/L)` terms. This gives a practical high-frequency probe,
but its numerical output remains empirical until the Lerch values are enclosed
with directed balls.

## Expected benefit

The search spends high precision on mathematically distinguished events and
preserves a compact, reproducible path from discovery to exact checking. It
also makes failures informative: the location, moment suppression, conditioning,
and precision ladder of every deep near miss are retained.

## Possible cost or risk

The smallest eigenvectors can rotate sharply, making continuation and frozen
rank-one predictions unreliable. The event schedule may still miss a very
narrow minimum. Recent external closed forms can carry a shared sign error.

## Trial procedure and success criterion

X-0601 is the first trial. Success means either:

- a stable negative fixed vector that passes independent interval enclosure and
  exact checking; or
- a reproducible negative-result atlas that materially narrows subsequent
  searches without being misreported as a theorem.
