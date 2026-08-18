# O-98400 — Selected-horizon future-completion scan at \(N=10^8\)

Status: **DIAGNOSTIC ONLY — NOT AN ALL-SCALE CERTIFICATE**

The exact quotient DAG at

\[
N=100,000,000
\]

has 19,999 distinct coordinates.  A deterministic C++ implementation processes
all 5,761,454 odd primes in descending order with the exact floor transition
and long-double evaluation of the half-order reciprocal-Julia coefficient.

The retained run reports

```text
updates:                 85,555,516
minimum Bellman slack:   0.188199976219113106072
witness prime:           3
witness coordinate:      48,379
maximum boundary:        0.811800023780886893928
final root boundary:     0.238865273631748588882
```

No FCBI violation was observed on this selected quotient profile.  The run is
not directed interval arithmetic and does not quantify all horizons; it proves
neither FCBI nor RJTE.  Its role is discovery and regression only.
