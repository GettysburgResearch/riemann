# L-91669 — Superseded ledger; historical root input was false

Claim ID: `L-91669`  
Status: **SUPERSEDED / NOT A VALID CONCLUSION LEDGER**  
Superseded by: `L-91671`  
RH status: **unproved**

This file historically depended on `L-91668` for the claim that the labelled
balanced/reserve source realized one copy of the native equality row. PR #457
proved that the cited realization gives `3c_X`. Therefore the historical
one-row ledger does not apply to the native packet.

The surviving ideas are retained in the successor:

```text
finite-window, not global, positivity of the equality weight;
one-use endpoint quantization and current corrections;
same-index child replacement;
coefficient-one loss algebra;
no root-only packet copied to a child.
```

The normative successor `L-91671` replaces the false root input by the exact
single-SHARP source `3P^(4/3)`, proves the finite equality-seed identity
`R[b_X^star]=c_X`, and states the complete typed one-generation ledger.

This historical file must not be used as an alternate proof.
