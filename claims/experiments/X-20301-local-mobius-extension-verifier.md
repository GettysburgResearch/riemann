# X-20301 — Exact local Möbius extension verifier

Claim ID: `X-20301`  
Title: Fraction-only replay of source cancellation, divisor reconstruction, graph-kernel algebra, and zero residual  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: `L-20301`; `L-20302`

## Scope

The checker verifies a piecewise-constant bounded-variation model of the local
Möbius extension.

It reconstructs:

- the exact Möbius values through the declared cutoff;
- the source integral correction;
- the positive distance of the source support from zero;
- every open reconstruction cell in the retained interval;
- the truncated divisor coefficients
  \[
  A_N(k)=\sum_{d\mid k,\ d\le N}\mu(d);
  \]
- declared lower-tail sample values;
- one exact selected-zero graph kernel;
- the formal identity `tail evaluation = -target evaluation` at a zeta zero.

## Retained model

```text
target support             [2,5]
Möbius cutoff              3
safe cutoff slack          1
g integral                 5/2
P_N(1)                     1/6
source correction          5/12
source integral            0
reconstruction cells       4
graph kernel vector        (1,-1/6)
graph metric norm          37/36
formal zero target         7/5
formal zero tail          -7/5
```

The lower-tail samples are

```text
u=3/4   tail=-10/3
u=1/2   tail= 1/6
u=1/4   tail= 4/3
```

The proof-object SHA-256 is

```text
5a682844bcf83a618b76f796a988764902d7ade58b9db43a695c399a103c0bd4
```

## Boundary

This is an exact finite arithmetic regression. It does not evaluate zeta,
construct a production Weil matrix, or prove convergence of the Möbius tail.
