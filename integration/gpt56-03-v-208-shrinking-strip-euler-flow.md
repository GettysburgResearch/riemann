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

This is the load-bearing review target. Audit the variance-integral factor,
Popoviciu constant `1/4`, final factor `1/8`, the PNT decay of `eta_j`, and the
square-sampling transfer.

## Structural lemmas

```text
L-20810  compound-Poisson/reference-variance and stop-loss representation
L-20811  exact Gibbs KL budget, prime/power chain rule, Rényi hierarchy
L-20812  finite Euler Riccati strip flow and first-omitted-power defect
```

The strongest new composition is

```text
positive local Euler collision energy
+ positive logarithmic drift
- explicit first-omitted-power defect
>= archimedean entropy barrier - vanishing tilt allowance.
```

The last inequality is open.

## Exact checker

```text
experiments/X-20807-levy-euler-flow/verify.py
```

uses only `fractions.Fraction` and returns

```text
PASS_EXACT_L20810_L20812_IDENTITIES
```

It is synthetic finite algebra, not a Riemann certificate.

## Numerical calibration

```text
claims/observations/O-20806-shrinking-strip-tilt-recon.md
```

replays the record-low prefix `q=3089` at 80 decimal places. The strict shifted
margin is still positive there. The calculation is nondirected and finite.

## Recommended independent review order

1. `T-20803` tilt-variance identity and RH transfer;
2. `L-20812` finite geometric/Riccati algebra;
3. `L-20810` reference Lévy measure and endpoint constant;
4. `L-20811` entropy and Rényi asymptotics;
5. `X-20807` exact replay;
6. `O-20806` numerical normalization;
7. `M-20803` proposed completion program;
8. session report.

## Merge/integration concerns

- `T-20803` depends on `T-19801`, currently carried on the PR #202 lineage.
  Integration must either import that transfer theorem under a canonical ID or
  restate its Landau step locally.
- `T-20802/L-20808/L-20809` depend on the Suzuki normalization in `D-9501` and
  the convexity formula in `L-9503` from PR #98. Preserve those source
  dependencies explicitly.
- Do not replace the finite Euler factors by completed factors without the
  cutoff defect `E_(p,K)`.
- Do not promote the ordinary `q=3089` or `10^7` values to directed results.
- The current stacked PR may report temporary merge conflicts as its base moves;
  the files and commits on the branch remain the durable review surface.

## Exact remaining theorem

```text
exists J0, for every j>=J0:
P_j/omega_j * log(P_j/P_j(omega_j))
>= A_+^*(P_j) - log^2(q_j/2)/(8P_j).
```

A proof closes RH through `T-20803`. No proof of this cofinal inequality is
claimed here.