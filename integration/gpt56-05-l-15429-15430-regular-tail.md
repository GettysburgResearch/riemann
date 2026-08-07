# Integration handoff — corrected regular augmented tail

Add after `T-15410`:

- `L-15429`: exact moving endpoint, raw tail, and boundary--tail cross split;
- `R-15406`: raw regular tail is not a positive Gram;
- `L-15430`: one-Green tail criterion and smoothed Jordan inequality;
- `X-15413`: exact rational endpoint/cross/tail regression;
- session audit report.

Scope correction:

```text
A_reg * ghat  <-> positive raw Volterra tail Gram
```

is false. The corrected positive target must retain the full moving endpoint
Gram and apply one Mellin/Green primitive to the regular tail. Do not claim the
smoothed Jordan derivative inequality has been proved.
