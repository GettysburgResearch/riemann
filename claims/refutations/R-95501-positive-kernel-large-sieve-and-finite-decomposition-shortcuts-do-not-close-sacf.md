# R-95501 — Positive-kernel, generic large-sieve, and finite-decomposition shortcuts do not close SACF

Claim ID: `R-95501`  
Status: **EXACT SCOPE FIREWALLS**  
Created: 2026-08-18  
Depends on: `L-95501/L-95502/L-95503`; PR #580 `R-95400`

## 1. Positive ratio kernel

The multiplicative autocorrelation of the exact ten-band kernel has Fourier
transform \(|\widehat\gamma_L(t)|^2\ge0\), with nonzero mass near `t=0`.
A positive-kernel completion therefore converts the arithmetic source into a
positive reciprocal-zeta square. It does not create an oscillatory sign.

## 2. Fixed Mellin window

PR #580 proves

\[
\int_{-T}^{T}\left|\sum c_m m^{-it}\right|^2dt
\le(2T+CX)\sum|c_m|^2.
\]

The exact annular kernel is compact in log position but not compact in
frequency. For `T=polylog(X)`, the `CX` term remains. The local kernel cannot
remove it because `L-95501` gives nonzero low-frequency mass.

## 3. Finite coefficient decompositions

Vaughan/Heath–Brown identities and the prime-divisor expansion are exact
rearrangements of derivatives of `M_o`. On reassembly they return the local
factor `(1-u)(1-v)`. An estimate that treats every resulting factor only by
source-blind size cannot beat the parent diagonal/firewall examples.

## 4. Quantitative burden

By `L-95502`, any bound

\[
|\mathcal S_H(X)|\ll X^{1-\delta}
\]

already proves a fixed zero-free strip \(\Re\rho\le1-\delta/2\). Thus a claimed
routine Type-II power saving must be reviewed as a new zeta zero-free theorem,
not as an ordinary large-sieve consequence.

These statements do not prove that all Type-II methods fail. They identify the
exact arithmetic gain that a successful proof must supply.


## 5. Classical gain boundary

The actual odd Möbius coefficients do yield the standard zero-free-region gain
through exact partial summation, as recorded in `L-95504`.  That estimate is
subexponential in `log X`, not a fixed power of `X`.  It therefore confirms
that arithmetic input matters without supplying the fixed exponent needed by
`L-95502`.
