# O-9504 — Semicircle totient error is empirically at the RH scale

Claim ID: `O-9504`  
Title: Initial semicircle-totient reconnaissance after exact centering  
Status: `EMPIRICAL`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `T-9501`; `X-9503`  
Scope: ordinary-floating scale reconnaissance only  
Related counterexample candidates: none

## Observation

For

\[
\mathcal E(X)=
\frac2X\sum_{n<X}\frac{\varphi(n)}n
\sqrt{1-(n/X)^2}-\frac3\pi,
\]

`X-9503` computed exact integer totients and ordinary-binary64 semicircle sums
through

\[
X=2,000,000.
\]

The scaled quantity

\[
X^{3/2}\mathcal E(X)
\]

remained order one on the retained sparse grid and changed sign repeatedly.
Representative values are

| `X` | `E(X)` | `X^(3/2) E(X)` |
|---:|---:|---:|
| 100 | `-6.556447521258724e-4` | `-0.6556447521` |
| 1,000 | `+4.798558213559012e-6` | `+0.1517437344` |
| 10,000 | `+1.143938140879541e-7` | `+0.1143938141` |
| 100,000 | `+2.656227238162501e-9` | `+0.0839972806` |
| 1,000,000 | `-1.107223757124132e-9` | `-1.1072237571` |
| 2,000,000 | `+8.772182980010257e-11` | `+0.2481148028` |

The complete table is in

```text
experiments/X-9503-semicircle-totient/results/reconnaissance.json
```

## Interpretation

This behavior is consistent with the critical-line exponent in `T-9501`. It is
also consistent with an oscillatory explicit formula: the centered error is not
expected to have one sign.

The data do not distinguish RH from a sufficiently small off-line displacement,
do not prove a big-O bound, and do not constitute evidence that the scaled
quantity remains bounded.

## Connection to prior empirical work

The same `-3/2` centered exponent appears after subtracting the positive
`12/(pi^2 X)` pole-density term from the `s=1` Jordan/Volterra endpoint. Thus
these data are a direct arithmetic view of the centered profile mode that was
hidden inside the larger operator and Schur packets.

## Proof boundary

- Totients are exact integers.
- All transcendental and summation operations are ordinary binary64.
- No interval or independent special-function backend is present.
- No finite table can certify `T-9501.3`.

## Handoff

Use the exact Bessel--Möbius identity `L-9507` to predict and isolate the
oscillation. The next useful result is an analytic dyadic-block inequality, not
a larger undirected table.
