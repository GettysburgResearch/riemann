# Integration patch — prime-prefix Fenchel transport

Authoring agent: `gpt56-03-u`  
Date: 2026-08-07  
Stack: PR #208

## New claim IDs

```text
T-20802  prime-prefix Fenchel–Suzuki RH criterion
L-20808  Bregman prime-curvature transport recurrence
L-20809  elementary entropy envelope for the Fenchel barrier
M-20802  full-RH prime-curvature transport attack
O-20805  finite transport reconnaissance through 10^7
X-20806  reproducible ordinary-high-precision prefix scan
```

## Dependency order

```text
D-9501 + L-9503
    -> T-20802
    -> L-20808
    -> L-20809
    -> M-20802
    -> O-20805 / X-20806
```

## Status boundary

- `T-20802`, `L-20808`, and `L-20809` contain exact identities and inequalities,
  but remain `PROPOSED` pending independent review.
- `O-20805/X-20806` are empirical finite reconnaissance, not a directed
  certificate.
- No theorem in this patch proves the cofinal prime-prefix sign.
- No RH proof or counterexample is claimed.

## Integration recommendation

The scalar criterion should be cross-linked from the Suzuki screw route and the
square-screw route, but it should not replace their existing records.  It is a
new exact global-minimum adapter and prime-transport induction, not a
retroactive verification of prior claims.

The next proof-facing artifact should be a directed block-transport producer,
not a larger ordinary finite scan.
