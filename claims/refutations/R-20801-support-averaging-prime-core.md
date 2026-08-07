# R-20801 — Fixed-packet support averaging cannot close the prime-side core

Claim ID: `R-20801`  
Title: Fixed-height and fixed-order support averaging do not prove the source Schur sign  
Status: `PROVED SCOPE NARROWING`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `L-20703`, `L-20801`, `L-20802`  
Scope: the cofinal D-0001 prime-side LMI

## Refuted shortcut

A small support-averaged outer remainder and a well-conditioned finite zero
frame do not imply eventual nonnegativity of the source Schur quotient.

`L-20703` proves that frame graphs do not change the complete Schur pivot.
`L-20801` identifies that pivot with one scalar resolvent value. `L-20802` shows
that a fixed off-line zero survives every fixed-order support average with size

\[
 e^{bL}L^{-O(1)}.
\]

Therefore outer-tail averaging and frame conditioning do not control the fixed
arithmetic core.

## Valid use of support averaging

A valid strategy may separate:

1. a fixed-frequency core represented exactly;
2. a moving high-zero tail handled by a large-sieve estimate;
3. a growing endpoint-notch packet with a uniform derivative and metric ledger.

The third item must prove a uniform estimate such as

\[
 |g_L(a+ib)|\le e^{bL-\omega_L(b)},
 \qquad \omega_L(b)-bL\to+\infty,
\]

for every fixed \(0<b<1/2\). Counting endpoint conditions alone is not enough.

## Remaining exact sign

After every valid averaging and structured inversion, the core remains

\[
 \boxed{
 S_{R,N,c}
 =A_{RR}-A_{RW}A_{WW}^{-1}A_{WR}
 ={g^2\over \ell A^{-1}\ell^*}.
 }
\]

A proof must establish this lower sign or construct a complete growing-notch
comparison dominating every possible fixed off-line mode. A finite verified
height or an empirical \(1/\log c\) fit is insufficient.

The independent square-support identity `L-20704/T-20701` places the same fixed
arithmetic obstruction in a principal coordinate of the complete matrix.

This result narrows the route; it does not disprove the prime-side program and
makes no RH claim.
