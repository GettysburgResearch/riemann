# R-105560 — Theorem D normalization firewall

Claim ID: `R-105560`  
Status: **PROVED SOURCE AUDIT**

The file

```text
Zeta23/ThmD/Final.lean
```

contains an optimized theorem near `0.6725007`, but its conclusion is expressed
through `N0star`, the distinct matched line-zero object. The ordinary simple
zero theorem in that file has the smaller `0.5065` constant.

The correct multiplicity-aware simple-zero source is the separate theorem

```text
Zeta23.ThmD.thmD₀_simple_mult
```

in

```text
Zeta23/ThmD/Mult.lean
blob a36b073fd6b04b568aac377026eafcce129946d1
```

at commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`. It has no hypotheses and
concludes the exact `H0` lower bound for `N0simple` after its multiplicity-aware
positive-index ledger.

Therefore citing only `Final.lean` for the simple-zero baseline is ambiguous
and potentially wrong. `T-105560` freezes the correct theorem path and blob.
