# Single-scalar prefix shadow and annular filter firewall

This pass continued independently from frozen PR #551 and used PR #552 only as a negative-control source.

The main exact advance is the collapse of the unique `5:3` scalar to one four-scale weighted-Mertens prefix. The all-scale prime sieve has the exact source-correct recurrence

```text
M_(Pp)(N)=M_P(N)-p^(-1/2)M_P(floor(N/p)).
```

This removes the invalid rough-block surrogate and makes the required induction explicit.

A second exact result closes an entire tempting annular subroute: the positive-source Green multiplier has a zero at the positive real point `s=1/2`. Every zero-safe finite shift multiplier preserves that zero, so its nonzero filtered kernel must change sign. Compact annular localization survives, but source-blind one-sign filtering cannot prove its arithmetic discrepancy.

A diagnostic scan found the scalar prefix positive through `10^8`; this is reconnaissance only and is not theoremized. No unconditional all-scale producer was obtained. RH remains unproved.
