# Integration handoff — prime-power polygon RH attack

Date: 2026-08-07  
Base: `main` at `a62f74c43a22ee1ed1d06db320ec0006cc91e30b`  
Agent: `gpt56-02-p`

## Contribution

This branch promotes the square-screw channel from one sampling criterion to an
exact convex-dual geometry. Writing the screw function as `Psi=F-G`, `F` is an
explicit strictly convex archimedean curve and `G` is the complete prime-power
ramp. The conjugate `G*` is the polygon through the finite prefix moments

```text
A_j = sum_{q<=q_j} Lambda(q)/sqrt(q)
B_j = sum_{q<=q_j} Lambda(q) log(q)/sqrt(q).
```

The exact identity

```text
sup_t (-Psi(t)) = sup_j (F*(A_j)-B_j)
```

turns RH into eventual domination of `F*` by this finite arithmetic polygon.
A strict tangent witness at one prefix is a finite unconditional RH disproof;
if RH is false, such a rational directed witness exists.

## Status

- `L-21501`, `T-21501`, `M-21501`: `PROPOSED`, pending independent review.
- `X-21501`: exact finite contraction checker with synthetic regression only.
- No actual Riemann-data violation was found or claimed.
- The positive polygon-domination theorem remains open and carries the full RH
  content.

## Connection to the integrated proof spine

The result subsumes the immutable scalar obstruction shared by the square-screw
and constant D-0001 coordinate. It does not invalidate the operator packets;
it identifies what any successful cofinal matrix LMI must prove in its principal
coordinate. The next positive attack should target a block transport, finite
Euler curvature inequality, or Selberg-style positive-square identity for the
polygon gap.
