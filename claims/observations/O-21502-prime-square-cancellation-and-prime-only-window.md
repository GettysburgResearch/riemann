# O-21502 — Prime-square cancellation and the prime-only boundary-difference window

Claim ID: `O-21502`  
Status: `EMPIRICAL / DISCOVERY ONLY`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Experiments: `X-21502`, `X-21503`  
Theorem suggested by the data: `T-21502`

## 1. Layer decomposition of the pushed `10^7` computation

The complete `X-21502` manifest contains all 665,134 prime powers through
`10^7`. Replaying the same exact piecewise-linear event integration while
separating exponent one from exponents at least two gives the following block
energies.

For each unit block, write

\[
 Q_G=Q_{\rm prime}+Q_{\rm high}
\]

and decompose

\[
 \int|Q_G|^2
 =\int|Q_{\rm prime}|^2
 +2\int Q_{\rm prime}Q_{\rm high}
 +\int|Q_{\rm high}|^2.
\]

| block `j` | prime-prime | twice prime/high | high-high | total |
|---:|---:|---:|---:|---:|
| 5 | `0.3567519093` | `-0.6920500683` | `0.3373362925` | `0.00203813347` |
| 8 | `0.6940647581` | `-1.3918710569` | `0.6992964111` | `0.00149011231` |
| 12 | `0.3581152866` | `-0.7126062016` | `0.3557571874` | `0.00126627239` |
| 16 | `0.2991686594` | `-0.6016764668` | `0.3040682872` | `0.00156047987` |

The tiny total is not produced by a tiny prime layer or a tiny higher-power
layer. Two order-one signals cancel almost completely.

## 2. Prime squares dominate the higher-power cancellation

A finer split into primes, squares, cubes, fourth powers and exponents at least
five shows that the square layer is the principal partner of the prime layer.
At block `j=16`, for example,

```text
prime energy                  0.2991686594
square energy                 0.2382357352
cube energy                   0.0020212526
fourth-power energy           0.00005152
exponent >=5 energy           0.00013282

twice prime/square cross     -0.5325869725
twice prime/cube cross       -0.04899095
all remaining interactions    restore the final 0.00156048
```

This is explained structurally by Möbius inversion:

\[
 P_1(s)=D(s)-D(2s)-D(3s)-\cdots,
 \qquad
 D(s)=-\zeta'(s)/\zeta(s).
\]

The analytically continued prime layer contains a boundary pole from
`-D(2s)`, while the square layer in the full von Mangoldt signal supplies the
opposite channel. `T-21502` converts this observation into an exact prime-only
criterion by adding one boundary difference.

## 3. Prime-only boundary-difference reconnaissance

Put

\[
 H(u)=G(u)-G(u-1).
\]

Using ordinary primes only, define

\[
 Q_H^{\mathbb P}(x)
 =\sum_p{\log p\over\sqrt p}H(x-\log p).
\]

The same complete event sweep gives:

| block `j` | prime-only `H` energy |
|---:|---:|
| 5 | `0.1094098229` |
| 8 | `0.0649961037` |
| 10 | `0.0333391343` |
| 12 | `0.01046060895` |
| 13 | `0.00421582040` |
| 14 | `0.00318453333` |
| 15 | `0.00325330792` |
| 16 | `0.00481055687` |

The corresponding diagonal at block `16` is about `89.35`, so the prime-only
off-diagonal form still cancels more than `99.99%` of its diagonal.

Testing the family

\[
 (1-e^{-z})^r\widehat G(z),
 \qquad r=0,1,2,3,
\]

shows that exactly one additional difference is best over the retained range.
Further differences increase the block energy. This matches the analytic
structure: there is exactly one new boundary pole, at `z=0`, after eliminating
higher prime powers.

## 4. Interpretation

The original dramatic cancellation has two layers:

1. **exact layer cancellation:** primes against prime squares remove the
   Möbius-inversion boundary singularity;
2. **genuine RH-scale cancellation:** after that boundary channel is removed,
   ordinary primes still exhibit a tiny coherent Gram energy relative to the
   diagonal.

The first layer is now proved by `T-21502`. The second is the actual remaining
arithmetic theorem.

## 5. Proof boundary

- The prime-power manifest through `10^7` is complete for the retained blocks.
- The event integration uses the exact piecewise-linear shape but long-double
  arithmetic.
- No outward rounding or independent compiler replay is supplied.
- These values are discovery evidence for the layer structure, not evidence for
  RH.
- The global prime-only criterion is a separate analytic theorem; its
  subexponential energy estimate remains open.
