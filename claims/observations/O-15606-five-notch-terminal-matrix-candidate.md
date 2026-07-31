# O-15606 — Five-notch phase-complete terminal-matrix candidate

Claim ID: `O-15606`  
Status: `EMPIRICAL CANDIDATE / NOT CERTIFIED`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Dependencies: PR #165 X-15404 reconnaissance; `L-15610`--`L-15612`  
Related counterexample candidates: none

## Retained scalar data

PR #165 evaluated the pole-free universal terminal window with ordinary floating
arithmetic through prime-power cutoff `10^7`. Its notch ladder reported:

```text
notches    empirical RMS       minimum absolute scale
0          5.45e-3             about 1.01e-2
1          7.38e-5             about 1.09e-4
2          1.16e-7             about 2.23e-7
5          1.59e-9             about 3.12e-9
```

The five design ordinates were approximately

```text
14.1347251417
21.0220396388
25.0108575801
30.4248761259
32.9350615877.
```

The full compact support cost of the five-notch window was approximately
`8.17012406797` in the PR #165 convention.

All values are classified `EMPIRICAL_NON_DIRECTED`. The zero ordinates,
window construction, FFT, and prime accumulation were midpoint computations.

## Why the candidate is stronger after L-15612

The scalar terminal value is not itself a visible-block certificate. However,
`L-15612` supplies a same-end packet floor at scale

\[
 \log R-O(1),
\]

while the notched scalar terminal remainder is already numerically many orders
smaller on the retained window.

The decisive missing computation is therefore not another scalar scan. It is
the complete phase-aware matrix

\[
 E_a=
 2\sum c_nC(2a-\log n)
 -2e^a\int e^{-u/2}C(u)du
\]

for a packet containing:

1. the five-notch universal profile;
2. one independent compact profile or exact phase quadrature;
3. the full profile Gram and polar vectors.

## Required production gates

A valid replay must:

- replace every design ordinate by a certified simple critical-line zero ball;
- prove every notch factor has no zero in the open counterexample strip except
  the intended boundary-line zeros;
- enumerate every prime power in the fixed and terminal windows;
- evaluate every convolution entry with directed arithmetic;
- center the matrix before taking a norm;
- certify
  
  ```text
  theta^2 G-E G^-1 E >= 0;
  ```
- compare the full `theta`, not one scalar phase, with the local-Weyl and
  three-block moats;
- reproduce the same matrix through an independent zero-side backend.

## Interpretation

A strict positive visible margin would close one finite support packet only. A
stable pattern across supports would be reconnaissance for the still-unproved
cofinal terminal-norm theorem.

A matrix norm much larger than the scalar values would expose phase hiding and
be equally valuable. No sign or RH claim is made.