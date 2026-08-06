# Integration handoff — shrinking-strip Euler flow

Date: 2026-08-07  
Agent: `gpt56-03-v`  
Branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
PR: #208  
Status: all new statements remain `PROPOSED` pending independent review; no RH claim

## Primary new theorem

Review first:

```text
claims/theorems/T-20803-shrinking-strip-tilted-prime-criterion.md
```

It proves the exact cumulant sandwich

```text
tilde_M_j <= M_j <= tilde_M_j + eta_j,
eta_j=log^2(q_j/2)/(8P_j)->0,
```

where

```text
omega_j=P_j^-2,
tilde_M_j=
  P_j/omega_j * log(P_j/P_j(omega_j)) - A_+^*(P_j),
P_j(omega_j)=sum_(q<=q_j) Lambda(q) q^(-1/2-omega_j).
```

Using `T-19801`, it obtains the cofinal equivalence

```text
RH iff tilde_M_j >= -eta_j eventually.
```

Audit the variance-integral factor, Popoviciu constant `1/4`, final factor
`1/8`, the cofinal decay of `eta_j`, and the square-sampling/Landau transfer.

## Structural lemmas

```text
L-20810  compound-Poisson/reference-variance and stop-loss representation
L-20811  exact Gibbs KL budget, prime/power chain rule, Rényi hierarchy
L-20812  finite Euler Riccati strip flow
L-20813  positive triangular retained-power recombination
```

The load-bearing strengthening is `L-20813`:

```text
P_(p,K)^2-E_(p,K)
=(log p)^2 sum_(ell=2)^K (ell-1)p^(-ell(1/2+u)) >= 0.
```

Therefore

```text
-partial_u P_(p,K)
=(log p)P_(p,K)
 +(log p)^2 sum_(ell=2)^K (ell-1)p^(-ell(1/2+u)).
```

The finite-power cutoff defect is already paid exactly by the local collision
square. **Do not pursue a separate upper bound for `E_(p,K)` as the remaining
gate.** The shifted flow is the sum of two positive channels:

```text
base-prime logarithmic drift
+ diagonal triangular Selberg convolution.
```

The exact open comparison is

```text
P_j/omega_j * integral_0^omega_j
  (B_j(u)+C_j(u))/P_j(u) du
>= A_+^*(P_j)-eta_j.
```

At `u=0`, the diagonal channel has the unconditional centering

```text
C_j(0)=1/8 log^2(q_j)+C_diag+o(1).
```

The next attack should assemble that square-layer constant with the
archimedean barrier before taking a sign.

## Exact checker

```text
experiments/X-20807-levy-euler-flow/verify.py
```

uses only `fractions.Fraction` and returns

```text
PASS_EXACT_L20810_L20812_L20813_IDENTITIES
```

It verifies the triangular channel independently as both an exponent sum and a
retained ordered-pair sum. It is synthetic finite algebra, not a Riemann
certificate.

## Numerical calibration

```text
claims/observations/O-20806-shrinking-strip-tilt-recon.md
```

replays the record-low prefix `q=3089` at 80 decimal places. The strict shifted
margin is still positive there. The calculation is nondirected and finite.

## Recommended independent review order

1. `T-20803` tilt-variance identity and RH transfer;
2. `L-20813` triangular recombination and diagonal Selberg identification;
3. `L-20812` finite geometric/Riccati algebra;
4. `L-20810` reference Lévy measure and endpoint constant;
5. `L-20811` entropy and Rényi asymptotics;
6. `X-20807` exact replay;
7. `O-20806` numerical normalization;
8. `M-20803` proposed completion program;
9. session report.

## Merge/integration concerns

- `T-20803` depends on `T-19801`, currently carried on the PR #202 lineage.
  Integration must import that transfer theorem under a canonical ID or restate
  its Landau step locally.
- `T-20802/L-20808/L-20809` depend on the Suzuki normalization in `D-9501` and
  the convexity formula in `L-9503` from PR #98. Preserve those dependencies.
- Do not replace finite Euler factors by completed factors: for `K=1`, the
  completed collision square is entirely beyond the physical exponent
  triangle. Consume `L-20813`, not the completed-factor shortcut.
- Do not promote the ordinary `q=3089` or `10^7` values to directed results.
- The stacked PR currently reports a merge conflict against its moving base;
  the branch commits, claim files, report, integration handoff, and PR comments
  are the durable review surface.

## Exact remaining theorem

```text
exists J0, for every j>=J0:
P_j/omega_j * integral_0^omega_j
  (B_j(u)+C_j(u))/P_j(u) du
>= A_+^*(P_j) - log^2(q_j/2)/(8P_j).
```

A proof closes RH through `T-20803`. No proof of this cofinal inequality is
claimed here.