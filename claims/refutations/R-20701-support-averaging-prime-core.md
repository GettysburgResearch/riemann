# R-20701 — Support averaging alone cannot close the prime-side core

Claim ID: `R-20701`  
Title: Fixed-height and fixed-order support averaging do not prove the source Schur sign  
Status: `PROVED SCOPE NARROWING`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `L-20704`, `L-20705`, `L-20703`  
Scope: the requested cofinal D-0001 prime-side LMI

## Refuted shortcut

The following proposed implication is invalid:

```text
complete prime/polar/archimedean support average is small
+ well-conditioned zero frame
=> source Schur quotient is eventually nonnegative.
```

`L-20703` proves that frame graphs do not change the complete Schur pivot.
`L-20704` identifies that pivot with one scalar resolvent value. `L-20705` shows
that a fixed off-line zero survives every fixed-order local support average with
amplitude

\[
 e^{bL}L^{-O(1)}.
\]

Therefore outer-tail averaging and frame conditioning do not control the fixed
arithmetic core.

## What support averaging can prove

Support averaging remains useful after a split into:

1. a fixed-frequency core represented exactly;
2. a moving high-zero tail controlled by a large-sieve or integration-by-parts
   estimate;
3. a growing endpoint-notch packet whose derivative and metric cost are retained.

The proof-facing condition is not merely a count of notches. It is the weighted
rate

\[
 (2r_L+1)\log L-2\log|a_{r_L,L}r_L!|\ge bL-o(L)
\]

uniformly in the complete packet metric.

## Remaining exact sign

After all valid averaging and structured inversions, the unsmoothed core is still

\[
 \boxed{
 S_{R,N,c}
 =A_{RR}-A_{RW}A_{WW}^{-1}A_{WR}
 ={g^2\over \ell A^{-1}\ell^*}.
 }
\]

A proof must establish its lower sign or construct a complete growing-notch
comparison that dominates every possible fixed off-line mode. Replacing this by
an ordinary PNT error, a finite verified height, or an empirical \(1/\log c\)
fit is circular or insufficient.

## Classification

This refutation does not disprove the prime-side program. It removes a false
shortcut and identifies the exact extra datum a valid support-averaged proof
must carry.
