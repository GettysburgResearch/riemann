# Direct Euler-row factor-54 resolution proposal

Date: 2026-08-13  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
PR: #399  
Status: **full RH proof proposal pending independent adversarial review**

## 1. Why the route changed

The review on PR #405 correctly refuted tensorization of the one-prime completed
two-state matrix.  The provisional target-Hall residual subsequently closed the
scalar target and score gates, but did not automatically type the signed
arithmetic component row.

The corrected proposal uses neither shortcut.  Its load-bearing identity is the
exact Euler row split

\[
 D_{P_{79}}(py)
 =p^{-1/2}D_{P_{79}}(y)+D_{P_{79}p}(py).
\]

The second term is the actual arithmetic residual row.  `L-91346` proves its
inherited coordinates are strictly positive.  Target and score satisfy the same
Euler identity, and `L-91351` proves the residual score exceeds its target by
more than

\[
 \frac{58}{2075}\sqrt{py}.
\]

## 2. Finite certificates

A fresh checkout replayed successfully:

```text
X-91122  P79 terminal target Hall / row positivity;
X-91125  P79 one-prime inherited-row splice;
X-91127  corrected finite low-prefix target and score Hall;
X-91128  child first-moment upper bound.
```

The corrected low-prefix checker performs `383472` directed rational interval
checks.  Its target and score margins are respectively above `4.31` and `5.27`.

`R-91308` records the superseded convex-cell proof step; `R-91309` records why a
target-Hall residual alone is not row typing.

## 3. Typed one-prime packet

For each least-prime branch `p>=83`, with terminal child ratio `1<=y<83`, the
exact packet is:

```text
terminal child:
    p^(-1/2) times the positive P79 terminal packet at y;

current residual:
    the exact arithmetic P79-plus-p row at py;
    inherited rows nonnegative;
    current frontier handled by the resident finite producer;
    residual target positive;
    residual score strictly larger than target.
```

The child coefficient is below one.  No completed matrix product, independent
branch copy of the parent source, or fractional finite-column evaluation is
used.

## 4. Global recurrence

The exact least-prime source decomposition is substochastic and source-disjoint.
All current rows are summed before the one finite quantization and safety loss.
The proposed recurrence is

\[
 \mathfrak L_X
 \le\sum_b\theta_b\mathfrak L_{X_b}+C,
 \qquad
 \sum_b\theta_b\le1,
 \qquad
 X_b\le c_0X+C_0.
\]

The local residual score surplus contributes no positive loss.  All remaining
finite corrections have absolute bounded cost.  Iteration gives

\[
 \mathfrak L_X=O(\log X)=o(\log^2X).
\]

The conditional endpoint-score consumer then yields RH.

## 5. Mandatory hostile-review checklist

A reviewer must independently verify:

1. the analytic reduction and directed finite tail in `L-91346/X-91125`;
2. the corrected activation-cell logic in `L-91350/X-91127`;
3. the first-moment prefix statement in `X-91128`;
4. that every row beyond the inherited block is indeed charged only to the
   already closed current-generation frontier;
5. exact least-prime source provenance and substochastic normalization;
6. one-use sum-before-quantize physical capacity;
7. score orientation and normalization in `T-91302`;
8. absence of any dependency on the superseded completed-cascade or Hall-row
   shortcuts.

## 6. Status

```text
finite analytic/discrete layer        replayed / proposed closed
terminal P79 packet                    replayed / proposed closed
one-prime inherited residual row       replayed / proposed closed
residual target and score              certified positive
substochastic reset recurrence         proposed complete
Riemann Hypothesis                     PROPOSED / NOT INDEPENDENTLY VERIFIED
```

No merge or public proof claim should occur before the checklist above receives
an independent frozen-commit review.
