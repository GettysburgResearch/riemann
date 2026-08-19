# R-99210 — The equality-score shortcut is false, while samplewise integral leaves are unnecessary

Claim ID: `R-99210`  
Status: **PROVED EXACT CORRECTION AND SCOPE FIREWALL**  
Created: 2026-08-19  
RH status: **unproved**

`L-99213` proves for the full finite Möbius row

\[
 \mathcal H(c_X)=P_\Lambda(X),
\]

not `4sqrt(X)`. Therefore score-last row identity does not itself prove a
`4sqrt(X)-O(log X)` lower bound. Any such estimate is additional arithmetic.
Voluntarily applying larger thinning cannot repair a false constant-loss
identity, because the less-thinned row would remain available if its hypotheses
were true.

Accordingly, the T-99020/T-99050 score composition is not used in T-99210.

A separate firewall from PR #632 says expectation-only rounding is not
samplewise feasibility. That statement is correct. It is not an obstruction to
the present route: the random key is retained as a source coordinate and all
nonnegative observations are integrated. The conclusion-producing object is a
deterministic real component row, not one sampled integer Hall leaf.

The surviving route is

```text
endpoint-nested source + literal Hall/random-key partition
 -> full Möbius component row is nonnegative
 -> fixed-row reciprocal-zeta Mellin transform
 -> Landau
 -> RH candidate.
```

It uses no score deficit, native capacity, prime-square moat, or samplewise
integral physical leaf.
