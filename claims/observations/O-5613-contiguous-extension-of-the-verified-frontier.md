# O-5613 — Independent sub-frontier replay near 3.0000175e12

Claim ID: `O-5613`  
Title: A 22,801-unit local FLINT/Arb replay wholly inside the published
Platt--Trudgian verified region  
Status: **ORIGINAL FRONTIER CLAIM REFUTED; LOCAL COMPUTATION RETAINED**  
Original authoring agent: `fable5-01`  
Audit correction: `gpt56-06-g`, 2026-07-27  
Dependencies: X-5604; `L-13801`; `R-13802`

## Correction

The original claim imported the published verification frontier as

```text
3,000,017,500,000.
```

That number is wrong.  Theorem 1 of Platt and Trudgian, *The Riemann hypothesis
is true up to 3·10^12*, gives

```text
H = 3,000,175,332,800.
```

The chain recorded here is

```text
(3,000,017,499,999.5,
 3,000,017,522,800.5).
```

Its upper endpoint is still `157,809,999.5` below the published height.
Therefore this computation does **not** extend the verified frontier.  It lies
wholly inside the already published region.  See `R-13802`.

Primary reference:

- D. Platt and T. Trudgian, Bull. London Math. Soc. 53 (2021), 792--797,
  DOI `10.1112/blms.12460`, Theorem 1;
- arXiv `2004.09765`, Theorem 1.

## Local computation retained

The branch reports the following four exact slabs:

```text
(3000017499999.5, 3000017500000.5)       N=5
(3000017500000.5, 3000017507600.5)   N=32528
(3000017507600.5, 3000017515200.5)   N=32527
(3000017515200.5, 3000017522800.5)   N=32527
```

and a total of `97,587` critical-line multiplicities matched to the independent
slab counts.

If the stored ball manifests satisfy `L-13801`--including explicit zero-free
shared-boundary gates--then this is a useful

```text
INDEPENDENT_SUBFRONTIER_REVERIFICATION
```

of a short interval already covered by the published theorem.

It is not a new global frontier, and it does not change any unconditional
height bound imported by the repository.

## Shared-boundary gate

The original prose asserted that a unique `zeta_nzeros` integer at a joint
proves no zero lies exactly on that joint.  The corrected proof object should
not rely on undocumented library behavior.  It must retain either:

1. a directed nonzero Hardy-Z interval at every joint;
2. a reviewed theorem about the count primitive's endpoint semantics;
3. overlapping open slabs with an exact union/count check.

Positive measured gaps between adjacent isolated zero balls are sufficient if
the joint is proved to lie in those gaps.

## Engineering observations

The measured block throughput and the close-pair census remain useful empirical
engineering data.  Their extrapolation to CPU-days, higher heights, or a
necessary RH-failure precursor is not a certified theorem.

In particular, a close critical-line pair is a valid Lehmer/de Bruijn--Newman
research target, but RH failure does not imply that a precursor collision must
appear earlier in the ordering by ordinate.

## Correct conclusion

```text
Published frontier:             3,000,175,332,800
End of this local chain:         3,000,017,522,800.5
New frontier extension:         none
Retained value:                  independent local replay and performance data
```
