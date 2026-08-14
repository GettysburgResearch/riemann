# O-91686 — The next native-root generator is source-owned current thinning

Claim ID: `O-91686`  
Status: **RESEARCH FRONTIER / FAIL-CLOSED NEXT ATTACK**  
Created: 2026-08-14  
Depends on: `T-91659`, `R-91686`, `L-91686`, `L-91687`  
RH status: **unproved**

The newest branches have now removed several false degrees of freedom:

1. stopped-leaf Hall is unnecessary for raw row/score sign after PR `#469`;
2. arbitrary stopped-leaf LP basis discovery is unnecessary after `L-91686`;
3. the unthinned raw current cannot be placed in native capacity after `R-91686`;
4. ordinary capacity need not be solved separately once the direct radix-four slack is source-owned, by `L-91687`.

The next generator should therefore not be another positive packet added to the current. Positive addition worsens the separated native column. It must be a **source-owned current-thinning or replacement generator**.

## Preferred exact campaign

For each activation/cutoff cell:

1. freeze the recursive child detail vector `R^(4)` and every source label;
2. use the exact target-Lorenz basis for the target/score/row producer;
3. solve
   \[
   d(s)=B^{-1}\mathcal R_4[\Omega-R^{(4)}-s]\ge0
   \]
   with atomwise source ownership and all ports;
4. first pivot through `Y_4`-zero columns, because these repair rows at no endpoint-score cost;
5. use positive-`Y_4` columns only when the remaining row deficit cannot be moved by the zero-cost triangular cone;
6. certify a stable basis on the full activation cell with directed intervals;
7. on failure, return an exact dual and add only the minimal target-null thinning template that pairs positively with that dual.

## Why this is more promising than enlarging Hall

The exact separator is a capacity overdraw. Enlarging a positive Hall/current cone without a replacement operation cannot reduce that overdraw. By contrast, the slack variable acts with the correct sign:

\[
s\uparrow
\quad\Longrightarrow\quad
\Xi_{\rm current}\downarrow,
\quad
C_{\rm current}\downarrow,
\]

while the triangular inverse exposes precisely which row coordinates are lost or gained.

The `Y_4`-zero columns begin

```text
6, 10, 14, 15, 18, 21, 22, 24, 26, 30, ...
```

and are numerous: `3962` among `2<=q<=5000`. This is a large score-free repair cone, but its lower-row tail and provenance must be controlled exactly.

## Falsifiers

Reject a claimed closure immediately if any of the following occurs:

```text
a raw canonical reservoir is counted as native current;
a terminal child is retained without freeing its ordinary/detail capacity;
a leftmost LP failure is followed by a search for a non-leftmost rescue basis;
a zero-Y4 response direction is used without reconstructing its full row tail;
ordinary and detail constraints use inconsistent child packets;
source labels disappear before thinning;
a shared port is allocated independently to multiple channels;
Y4 slack is bounded only after dropping positive columns.
```

## Exact frontier

```text
best stopped-leaf target/score/row basis        EXPLICIT / LEFTMOST
raw row and response sign                       CLOSED ON TERMINAL LEAVES
raw native placement                            FALSE / EXACT SEPARATOR
score-free triangular response directions       EXPLICIT
source-owned thinning realization               OPEN / SONTR
Native-Root Capacity Theorem                    OPEN
Riemann Hypothesis                              UNPROVEN
```
