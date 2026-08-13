# X-91118 — Integrated fractional terminal omission

Small exact regression for `L-91329`.

It checks the rational case splits in the real-column breakpoint proof and the
final coefficient ledger:

```text
uniform derivative floor after q+1:  1/2 * s^(-3/2)
omission width:                        200000
continuum omission coefficient:       99999
fractional top-collar coefficient:     22784
net omission coefficient:              77215
existing terminal error coefficient:   28836
strict reserve:                         48379
```

The script uses only `Fraction`. The analytic breakpoint inequality is proved in
the claim file rather than inferred from sampling.
