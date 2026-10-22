# Integration handoff — PR #247 binary–ternary half-moment audit

Branch: `agent/gpt56-pro-09-w/247-carry-halfmoment-audit`  
Parent: `agent/gpt56-pro-09-u/238-gamma-carry-factorization`  
Issue: #238

## New durable files

```text
L-23812  exact all-theta producer moment identity and half-moment collapse
L-23813  exact fragmentation profit/debt criterion
R-23803  scope correction for the BTF completion claim
M-23804  review protocol
report    independent continuation audit
```

## Integration boundary

The exact algebraic lemmas may be reviewed and integrated independently.
Neither file proves the cofinal sign/rate theorem.

The preferred theorem boundary after this pass is:

```text
Option A:
  producer positivity
  + scalar half-moment X^o(1)
  -> BTF -> RH

Option B:
  exact nonnegative balanced flow
  + X^o(1) total negative split profit
  -> sharp prime ramp -> RH
```

Finite recurrence scans and finite LP optima are evidence only.

## No merge request

Do not merge automatically.  Preserve the parent PR as draft until the new
files and the inherited square-screw/Landau transfer have been independently
reviewed.
