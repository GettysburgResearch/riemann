# M-25301 — Review protocol for signed parabolic carry transport

Claim ID: `M-25301`  
Status: `PROPOSED METHODOLOGY`  
Issue: #253

A claimed completion of the parabolic carry route must pass all of the
following gates.

## Mandatory source ledgers

1. Emit the complete prime-power constraint list.
2. Reconstruct the parabolic seed and every initial signed defect.
3. Preserve both positive defect and negative slack before any norm or
   positive-part operation.
4. Emit every adjacent-flow or tapered-comb coordinate.
5. Recompute the complete constraint vector after the repair.
6. Recompute every `b_F(m)` and reject any negative value.
7. Recompute the exact objective cost from the flow.
8. Bind the square-screw consumer and its one-sided Landau orientation.

## Automatic rejection conditions

Reject a proposal that:

- uses the monotone tail cover of `L-24502` with sub-square-root claimed cost;
- bounds only `(d_X)_+` and discards the negative slack;
- omits a prime-power row or a noncoprime divisor interaction;
- treats `{2,3,4,5}` as an ordinary path instead of its complete
  divisibility matrix;
- repairs a constraint at `q` but omits prime-power divisors of `q-1` or
  `q+1`;
- applies a continuum transport without an outward finite-floor error;
- proves feasibility only on a fixed finite ladder;
- uses the PNT lower bound as though it supplied the required
  `X^epsilon` error;
- loses the smoothed-Mertens first integrated coordinate;
- changes the sign orientation of the square-screw/Landau consumer.

## Required mutations

A proof-producing checker should include:

```text
omit one prime-square dual row
understate the E(1/37) interval
delete the q=2 double-neighbor interaction
drop one divisor of j-1 or j+1
force a negative repaired b coordinate
understate the transport cost
replace signed defect by positive defect
mutate the square-screw sign
```

The output must distinguish exact finite algebra, directed analytic bounds,
classical imported theorems, and the still-open signed transport theorem.
