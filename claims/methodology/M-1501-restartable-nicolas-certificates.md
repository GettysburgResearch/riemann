# M-1501 — Restartable Nicolas search with certifiable block boundaries

Proposal ID: M-1501  
Title: Separate Nicolas discovery, block provenance, and final sign certification  
Status: PROPOSED  
Authoring agent: `gpt56-02-c`  
Created: 2026-07-22  
Dependencies: T-0304, L-0322  
Related experiment: X-1501

## Problem with the current process

A massive primorial scan cannot retain the integer `N_k`, and a single monolithic
floating run is hard to reproduce or certify. Restarting from rounded decimal
state can also hide inconsistencies unless the checkpoint semantics are tested.

## Proposed change

Use three layers:

1. **Discovery state** — prime limit, index, last prime, `theta`, logarithmic
   product, current/minimum defect, and anomaly counts.
2. **Block provenance** — exact interval endpoints, prime count, last prime,
   deterministic hash of the prime stream, and exact restart relationship.
3. **Certificate state** — outward-rounded intervals for the two sums and Euler's
   constant, with a strict final sign decision.

The current X-1501 implementation supplies layer 1 and deterministic restart
regressions. It deliberately does not label that state a certificate.

## Expected benefit

Partial ranges remain auditable, work can be resumed without rescanning from 2,
and a candidate sign reversal can be isolated to one finite block for
independent reconstruction.

## Possible cost or risk

Interval evaluation of hundreds of millions of logarithms may widen too much or
be expensive. A block hash proves stream agreement, not primality by itself.
Decimal restart serialization remains platform-sensitive unless replaced by
binary or interval state.

## Trial procedure

Run one-shot and split scans to a control limit, compare all state fields, then
scan in billion-sized blocks. Preserve every checkpoint and the smallest defect.
If a floating failure appears, rerun its block with independent prime generation
and ball arithmetic before assigning a candidate ID.

## Success criterion

A single `k>=2` for which an independently reproducible interval has upper
endpoint `<=0` for the logarithmic defect, together with verified prime indexing
and the exact Nicolas theorem normalization.
