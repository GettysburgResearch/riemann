# T-95310 — Finite odd-core cross correlation is the corrected OCHD frontier

Claim ID: `T-95310`  
Status: **COMPLETE CONDITIONAL REDUCTION — CROSS-CORRELATION THEOREM OPEN**  
Created: 2026-08-17  
Depends on: `L-95310/L-95311`, `R-95310`; the centered-cubic Mellin consumer

Define the finite odd-core packet \(\mathcal C_e(X)\) by (L-95311.3).

A sufficient conclusion-producing theorem is:

> **Finite Odd-Core Cross Correlation (`FOCC`).**  
> For some fixed \(A\),
> \[
> |\mathcal X(X)|\le(\log(2X))^A
> \]
> for every sufficiently large \(X\).

Since the diagonal is already \(O(\log^3X)\), FOCC gives a polylogarithmic
bound for \(\mathcal C_e\). The stable inverse (L-95310.11) gives the same for
the original critical Q4 observation \(\mathcal C_d\).

The Mellin transform is multiplied only by the safe factor

\[
(1+2^{-s})^2,
\]

whose zeros lie on \(\Re s=0\). No hypothetical zeta pole with real part
greater than \(1/2\) is cancelled. The centered-cubic Mellin argument then
gives RH.

Thus

\[
\boxed{
\mathrm{FOCC}
\Longrightarrow
\mathrm{OCHD}
\Longrightarrow
\mathrm{RH}.
}
\]

This packet does not prove FOCC. It replaces the infinite dyadic/passive
formulation by one explicit six-band odd-squarefree correlation and closes its
entire diagonal sector.

```text
infinite dyadic state                  ELIMINATED AT CRITICAL SCALE
finite six-band odd-core packet        EXACT
stable preconditioner inverse          EXACT
same-core diagonal                     POLYLOG
randomized model                       POLYLOG RMS
source-blind sign argument             REFUTED
distinct odd-core correlation FOCC     OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```
