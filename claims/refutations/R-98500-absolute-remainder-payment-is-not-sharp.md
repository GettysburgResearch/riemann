# R-98500 — Absolute rough-mass payment is not the intrinsic annular remainder

Claim ID: `R-98500`  
Status: **SUPERSESSION / EXACT STATEMENT-TO-USE CORRECTION**  
Created: 2026-08-18  
Target: the bounded-remainder step in PR #603  
RH status: **unproved**

The bound
\[
\left|
\sum_m\frac{\mu(m)}{\sqrt m}e(Y/m)
\right|
\le
\|e\|_\infty
\sum_m\frac{\mu^2(m)}{\sqrt m}
\]
is valid. It yields a normalized loss of order \(1/\log z\).

It is not the exact source consumed by the proof. The same rough histories and
parities act on the bounded remainder. `L-98500` proves that the continuum
contribution is instead
\[
\eta(Lu)+\frac1L\int_0^{Lu}
\eta(w)\rho'(u-w/L)\,dw,
\]
whose size is
\[
O\!\left(
\rho(u)\frac{\log(2u)}L
\right).
\]

The remaining discrete error is governed by the prime-harmonic discrepancy,
not by the full unsigned rough count. Therefore the absolute payment is a
correct fallback estimate but is superseded in the high-\(z\) terminal sector.

This does not refute PR #603's theorem. It strengthens its terminal range and
leaves the low-threshold critical Type-II/Lorenz core open.
