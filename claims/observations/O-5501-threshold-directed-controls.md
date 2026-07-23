# O-5501 — Threshold-directed ranking and directed positive controls near `10^8`

Claim ID: O-5501  
Title: 108,536 thresholds were ranked; one entire first microcell and one full-cell endpoint were excluded for exact dyadic vectors  
Status: PARTIAL  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: X-5501; L-5501--L-5505; conditional L-4202/L-4203 gate  
Scope: finite negative-search result at `T=4709203636353.65`, `K=1024`  
Related counterexample candidates: none

## Statement

X-5501 regenerated the complete D-0801 prime operator at `c=10^8` and ranked
every prime-power threshold in

\[
 10^8<q\le1.02\times10^8.
\]

There were exactly `108,536` thresholds. The ordinary-floating baseline leading
screen was approximately

```text
margin  +0.0066431696431843434
gap     +0.23960825343052772
```

and is discovery data only.

The top endpoint-susceptibility nomination was

```text
q=p=100011547
signed downward derivative      +5.429893639161426e-7
full isolated first-cell drop   +9.767867593186754e-9
```

The smallest of the five searched next-threshold microcells was nominated at

```text
threshold  100013561
cutoff     100013578
```

A 48-bit Gaussian-dyadic endpoint vector and an exact manifest containing

```text
5,762,210 primes
1,404 higher prime powers
5,763,614 total terms
```

were replayed with 192-bit MPFR directed arithmetic. The resulting leading
fixed-vector interval at the right endpoint was

\[
 0.0066414786110346293
 < M_v <
 0.0066414786110346302.
\]

The exact smooth-background bound, entering-event interval, and nonprime gate
give the whole-microcell lower envelope

\[
 \boxed{M_v(L)>0.0065451574898472229}
\]

throughout the first next-threshold microcell. Thus this complete microcell is a
certified positive exclusion for that exact vector, conditional only on the
proposed analytic block formulas used by the gate. It is not evidence for RH.

For the rank-one top nomination, a separately frozen 48-bit dyadic vector was
replayed at the limiting integer endpoint of the isolated first deposition
cell:

```text
threshold  100011547
cutoff     101828730
terms      5,862,050
```

The directed endpoint margin was

\[
 0.0065827830732268066
 <M_v<
 0.0065827830732268075,
\]

and the exact entering-event contribution was approximately
`9.775724152638723e-9`. This certifies the endpoint on the exact vector. It does
not certify the whole large cell, because many later prime powers enter before
that endpoint and the coarse combined background bound is unresolved.

No negative directed interval and no `Z-####` candidate was found.

## Exact provenance

Microcell manifest digest:

```text
76d23c38b2b5cbf45f6d9f018fcb01c68454fb1b05f43f929b504dd396620d8d
```

Microcell vector digest:

```text
56aab2547d590e9c3af84c59f7b84ebeabd8aab4ba09b67ba917933c738b3910
```

Rank-one endpoint manifest digest:

```text
c835b1b6dd89534dc1aef4fa41c91495c100706da7153853e3612538e0f15124
```

Rank-one vector digest:

```text
9bad8f553f3897fbf874b9862d27f528a1fa1f5a14778abe122f6195176c624c
```

## Independent control

At cutoff `100002`, an independent 100-decimal mpmath/SymPy implementation gave

```text
0.8912728134812008157624647954411958317751318054273758983712237663...
```

which lies inside the committed MPFR-directed interval. This checks formulas
and signs at small scale but is not an independent directed full-manifest
reproduction.

## Interpretation

The threshold events themselves are much smaller than the current positive
margin on this mode. The ranking is still useful because it reduces the search
from all cutoffs to structurally selected cells and reveals precisely when the
endpoint mass is too small to matter.

The exact L-5502 mesh contained 51 old-term deposition knots in the selected
17-integer microcell. Ordinary evaluations showed no near crossing; the
rigorous coarse L-5503 envelope already excluded the entire cell, so directed
knot-by-knot replay was unnecessary there.

## Proof boundary

- Ranking, eigenvalues, and mesh display values are ordinary floating discovery.
- The two fixed-vector endpoint intervals are directed finite computations.
- The whole-microcell exclusion uses a directed smooth bound and event bound.
- The nonprime gate is rigorous conditional on L-4202/L-4203.
- D-0801 admissibility and the Guinand--Weil normalization remain PROPOSED.
- A positive fixed-vector control does not prove the full matrix positive.

## Production blocker

PR #44 does not commit the `c=10^11`, `K=1024` leading vector or a digest-bound
coefficient/vector manifest. Therefore the requested production replay cannot
be honestly instantiated at that cell from current repository data. The X-5501
producer and checker establish the exact interface and a complete manageable-
cutoff control; the next required artifact is the production vector export.

## Suggested next attack

1. Export the PR #44 leading vector at 48, 64, and 80 dyadic bits.
2. Bind it to the exact 50-shard manifest.
3. Run one segmented MPFR fixed-vector replay.
4. Compare its interval directly with the existing `2.5e-10` gate.
