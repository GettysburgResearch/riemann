# O-20205 — Pinned endpoint-filter critical-mesh reconnaissance

Claim ID: `O-20205`  
Title: Degrees `2` through `12` remain positive on 34,771 complete finite prime-power levels  
Status: **EMPIRICAL / NON-DIRECTED**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: proposed `T-20206/T-20207`; exact endpoint family `L-20211`  
Scope: finite scheduling evidence only

## Scan

For every degree

\[
 N=2,3,\ldots,12,
\]

I constructed the algebraic endpoint Fejer filter

\[
 P_N(x)=|(1-e^{ix})Q_N(e^{ix})|^2
\]

from `L-20211` and added a small positive first-tap pin. The scan evaluated

\[
 \mathcal E_N\left({2\log n\over N}\right)
\]

for every

\[
 n=2,3,\ldots,3162.
\]

At each level the complete finite screw formula used every prime power through

\[
 n^2\le10^7.
\]

Total levels:

\[
 11\times3161=34{,}771.
\]

Observed negative levels:

\[
\boxed{0.}
\]

## Implementation boundary

- The complete duplicate-free von Mangoldt ledger through `10^7` was generated
  by an ordinary sieve.
- Prime prefix moments were accumulated in binary64.
- Special-function terms and filter coefficients used ordinary/high-precision
  reconnaissance arithmetic, not outward balls.
- The pins were numerical positive approximations selected below the dominant
  endpoint debt; the analytic field-separation theorem was not being certified
  by the scan.

Therefore this table is not a finite proof object and says nothing cofinal.
A future directed run must bind one exact quadratic-field pin, algebraic filter
coefficients, a complete prime-power manifest, and independent source
reproduction.

## Interpretation

The scan does not prove RH, but it provides three useful signals:

1. the field pin does not introduce visible finite-scale sign instability;
2. the endpoint family stays in the RH-compatible basin across several growing
   degrees and all complete levels available from the `10^7` manifest;
3. the next proof effort should target a uniform centered bulk estimate rather
   than search immediately for a low-level negative.

A finite positive ladder cannot substitute for the required eventual or
subpower theorem.
