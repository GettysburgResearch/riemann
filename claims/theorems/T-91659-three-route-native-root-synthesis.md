# T-91659 — Three-route native-root synthesis

Claim ID: `T-91659`  
Status: **CONDITIONAL SYNTHESIS / NOT A COMPLETE RH PROOF**  
Created: 2026-08-14  
Depends on: `L-91686`--`L-91689`, `T-91312/T-91313/T-91316`  
RH status: **unproved**

## 1. Statement

Assume a producer closes Gate A and Gate B of `L-91689` for every sufficiently large native packet. Then there is an exact one-use decomposition
\[
 P_X=P_X^{\rm cur}+\sum_b\alpha_bU_bP_{Y_b},
\]
with
\[
 Y_b\le X/67+C_0,
 \qquad
 \alpha_b\ge0,
 \qquad
 \sum_b\alpha_b<1/8,
\]
which holds simultaneously in source, row, ordinary capacity, radix-four capacity, literal score, and all retained ports.

If the current debt is uniformly bounded, `T-91312` gives `O(1)`. If only the logarithmic positive-packet bound is used, `T-91316` gives `O(log X)`. Both are `o(log^2X)`, so the resident one-sided endpoint consumer would imply RH.

## 2. Current achievement

This packet proves:

```text
rough native/reservoir ownership algebra            exact;
P61 causal target and score Hall margins             exact/directed;
unbounded prime tail for those margins               closed;
finite endpoint correction is decomposition-blind    exact on explicit inputs;
all three producer routes share one finite row gate  exact reduction.
```

It does not prove either remaining gate. In particular, no theorem here converts canonical finite-Euler capacity into native capacity without an explicit reservoir allocation, and no replay here certifies every target-Lorenz or joint-flow row gain.

## 3. Immediate falsifiers

Reject any claimed completion that:

```text
uses stopped-leaf survival-only Hall;
uses L-91364 beyond row 66 without a new proof;
uses separate target and score transports as though they were one source flow;
counts a rough reservoir fiber as both current and recursive;
checks ordinary capacity but not radix-four detail;
applies endpoint corrections once per color or leaf;
uses a synthetic fixture instead of the live native source matrix.
```

## 4. Exact status

```text
three routes radically advanced             YES
full unconditional proof proposal           NO
remaining finite row-gain theorem           OPEN
remaining native ownership/slack theorem    OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```
