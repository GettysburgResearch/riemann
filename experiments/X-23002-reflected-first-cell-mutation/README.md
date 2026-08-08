# X-23002 — Reflected first-cell mutation audit

This exact standard-library regression checks the scalar source claim used in
PR #226 `L-9517/T-9509`.

It verifies that the order-`K` Heath--Brown packet coefficient before the final
logarithm reconstructs the same Möbius function for every `K`, and therefore its
fixed-logarithm first Farey cell remains the first-order increment

```text
M(D)-M(floor(2D/3)).
```

It also exhibits exact finite values for which this first difference is not the
`K`-th geometric difference. Thus increasing the identity order does not itself
export the packet-level mutation claimed in `L-9517.8`.

The regression is finite algebra only. It does not estimate the Mertens
function or prove/disprove RH.
