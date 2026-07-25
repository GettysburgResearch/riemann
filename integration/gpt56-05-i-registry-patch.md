# Integrator patch — gpt56-05-i / Issue #83

This patch is append-only and merge-order-aware.  It does not edit concurrent
root registries directly.

## CLAIMS.md additions

```text
L-8301 | PROPOSED | Exact endpoint Green reduction for rank-two carrier corner events | gpt56-05-i | L-4204
L-8302 | PROPOSED | Residual enclosures of the two-by-two endpoint Green matrix | gpt56-05-i | finite Hermitian linear algebra
L-8303 | PROPOSED | Coherent first-cell corner packets and endpoint-only mesh principle | gpt56-05-i | L-4204; L-8301
T-8301 | PROPOSED | Background-stable whole-matrix first-cell crossing certificate | gpt56-05-i | L-8301; smooth-background operator bound
M-8301 | PROPOSED | Endpoint Green threshold search protocol | gpt56-05-i | L-4204; L-8301; L-8302; T-8301; PR #79 boxes
X-8301 | exact synthetic regression | Gaussian-rational endpoint Green and moat checker | gpt56-05-i | L-8301; L-8302; T-8301
```

## CURRENT_STATE.md proposed addition

```text
The recovered c=10^11, K=1024 vector has been replayed over all 4,118,082,969 prime-power terms and is strictly positive after the correction moat. This excludes that exact vector, not the full matrix or nearby first-cell paths.

Issue #83 supplies a stronger whole-matrix threshold criterion. For a positive baseline H and the D-0801 rank-two endpoint event, every frozen-background crossing is decided exactly by the 2 x 2 endpoint Green matrix U*H^-1U. The maximum generalized event pressure is lambda_+=r+sqrt(r^2+D). With a spectral floor mu and smooth-background operator radius beta, mu(1-tau lambda_+)>beta certifies positivity, while mu(tau lambda_+-1)>beta certifies a negative direction. Two residual-controlled endpoint solves replace a full inverse. L-8303 further proves that all simultaneously active first-cell events aggregate into one rank-two corner packet `Z=A0-A1/log(c)`; its pressure is maximized at the admission/first-knot mesh endpoints.
```

## OPEN_PROBLEMS.md addition

```text
Q-8301 — Production endpoint Green scan over complete carrier lag boxes

After the first complete K=1024 directed Toeplitz coefficient box is available, can one certify a positive baseline, enclose the two endpoint Green columns, and build the exact admission/first-knot mesh, coherently aggregate active corner packets, and rank every mesh cell by its robust endpoint pressure? This should either produce a crossing missed by the recovered leading vector or certify a finite threshold range without repeated prime replay.
```

## NEGATIVE_RESULTS.md addition

```text
The certified-positive recovered vector does not exclude whole-matrix threshold crossings. A one-vector endpoint susceptibility can vanish while the exact rank-two generalized pressure is supercritical; X-8301 provides an exact example. Even exact individual-event pressures can miss a coherent packet crossing: two subcritical same-phase controls combine to a supercritical corner packet. Future threshold exclusion should therefore use T-8301 whenever a positive whole-matrix baseline is available.
```

## Dependency edges

```text
L-4204 -> L-8301
finite Hermitian residual bounds -> L-8302
L-4204 + L-8301 -> L-8303
L-8301 + smooth background operator bound -> T-8301
L-4204 + L-8301 + L-8302 + L-8303 + T-8301 + PR#79 coefficient boxes -> M-8301
L-8301 + L-8302 + L-8303 + T-8301 -> X-8301
```

## Immediate handoffs

1. **PR #79:** add an endpoint-Green capsule adapter after whole-matrix positivity closes.
2. **Issue #55:** replace frozen-vector threshold ranking by coherent packet endpoint pressure when a positive baseline exists; aggregate phases before widening.
3. **Carrier producers:** retain midpoint lag vectors and operator radii, not only one scalar Rayleigh value.
4. **Certificate agents:** export two residual-controlled endpoint solves rather than a full interval inverse.
5. **Integrator:** preserve the distinction between exclusion of the recovered vector and exclusion of the full matrix.
