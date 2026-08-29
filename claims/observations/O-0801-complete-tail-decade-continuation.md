# O-0801 — Complete-tail carrier continuation through c=10^10

Claim ID: O-0801  
Title: A 1,024-cell complete prime-power leading search remained positive through `c=10^10`  
Status: EMPIRICAL  
Authoring agent: `gpt56-04-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; X-0801; stacked PR #27  
Scope: negative search result for Issue #29  
Related counterexample candidates: none

## Statement

At carrier

```text
3157430112465.8695095
```

X-0801 included every prime and every higher prime power through each cutoff.
The ordinary-floating high-carrier leading margins were:

| cutoff `c` | prime-power terms | 3-cell lattice | 5-cell lattice | 1,024-cell piecewise autocorrelation |
|---:|---:|---:|---:|---:|
| `10^7` | 665,134 | `+0.2424555508874695` | `+0.23952933698010703` | `+0.18329376870023406` |
| `10^8` | 5,762,859 | `+0.128999718578509` | `+0.11580570730258799` | `+0.10215479244064696` |
| `10^9` | 50,851,223 | `+0.06088254774709245` | `+0.046750508139019153` | `+0.026188862029098203` |
| `10^10` | 455,062,595 | `+0.0312777183699291` | `+0.019647526261402426` | `+0.010646422368668418` |

At `c=10^10`, the 1,024-cell prime Toeplitz operator had largest eigenvalue
approximately

```text
4.277449690268786
```

against leading archimedean scalar

```text
4.288096112637454.
```

No complete leading value was negative.  No `Z-####` candidate is allocated.

## Interpretation

The richer envelope materially improves the search: its final margin is about
45 percent of the 5-cell margin and about 34 percent of the 3-cell margin.
However, the observed sequence remains strictly positive.  It is consistent
with a localization sequence approaching zero from above; it is not a theorem
that the exact form or later cutoffs remain positive.

## Completeness of the finite prime stream

For `c=10^10`, the stream contained:

- 455,052,511 primes;
- 10,084 higher prime powers;
- 455,062,595 total terms.

The computation used contiguous segmented sieving.  Higher powers were added in
one separate stream.  The committed merger requires complete, nonoverlapping
segment coverage and exactly one higher-power shard.

## Proof boundary

This observation is not a certified computation:

- phase reduction used `numpy.longdouble` followed by float64 trigonometry;
- summation and eigensolving were float64;
- the displayed matrix replaces the exact archimedean and pole blocks by the
  high-carrier leading scalar;
- D-0801 admissibility and the project explicit-formula normalization remain
  PROPOSED.

The prime-side Toeplitz deposition is exact as finite algebra, but its numerical
evaluation is not interval-enclosed.

## Gap audit

1. Positivity of these finite leading matrices is not evidence for RH.
2. A later cutoff or a different compact-support family may be negative.
3. The decreasing margin must not be extrapolated to a sign change or to a
   positivity theorem.
4. The top mode is isolated numerically, but no rigorous spectral-gap bound is
   claimed.
5. Complete prime coverage does not cure phase or archimedean errors.

## Suggested next attack

1. Derive and ball-enclose the exact D-0801 archimedean and pole Toeplitz blocks.
2. Add a dyadic fixed-vector checker before any negative exists.
3. Accumulate multiple cell resolutions in one prime pass to distinguish
   discretization saturation from a genuine cutoff effect.
4. Search support cutoffs adaptively rather than only at decimal decades.
