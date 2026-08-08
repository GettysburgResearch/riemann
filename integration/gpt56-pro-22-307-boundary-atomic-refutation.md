# Integration handoff — critical stopped boundary atomization audit

Agent: `gpt56-pro-22`  
Date: 2026-08-08  
Issue: #307  
Frozen parent: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`

## Main disposition

```text
PR #304 complete boundary atomic norm polylog     FALSE
PR #304 terminal atom-by-atom completion          REJECTED
adjacent-tree divisor-source right inverse        RETAINED
critical boundary outer-band positivity           PROVED
outer-band exact nonnegative carry flow            PROVED
complete boundary column-capacity mass            O(log^2 X), PROVED
cycle-optimized lower leakage                       OPEN
Riemann Hypothesis                                  UNPROVED
```

## Exact new results

1. On `3X/8<=q<=2X/5`, the complete first stopped boundary satisfies
   ```text
   P_X(q)>q^(-1/2)/1820.
   ```
2. At the next-half divisor state these coordinates are triangular, giving
   ```text
   sum_m sqrt(m)|sigma_X(m)|>X/145600.
   ```
3. The complete outer profile is positive and decreasing and is realized by
   one explicit nonnegative central first-difference flow.
4. The coherent boundary obeys
   ```text
   sum_q |P_X(q)|/sqrt(q)<=log^2 X+2log X.
   ```

The linear atomic obstruction is therefore a coordinate failure, not a lower
bound for optimized carry debt.

## Relationship to parallel review work

The conclusion independently agrees with the critical-boundary refutations on
PRs #305, #308, #309, #310, and #311. This branch contributes its own rational
moat, exact outer-band flow theorem, and column-capacity bound. It does not
import their unproved replacement theorems.

## Corrected frontier

The remaining theorem is source-specific cycle optimization of the activated
lower-band leakage. The branch calls it `COBT`. A valid proof must emit the
complete Pascal-cycle coordinates and final balanced flow; a reviewer is not
being asked to invent them.

## Review order

1. `R-30701`
2. `X-30701`
3. `L-30701`
4. `L-30702`
5. `T-30701`
6. PR #272 Cycle-Debt consumer
7. this integration handoff and report

No merge or public RH claim is requested.
