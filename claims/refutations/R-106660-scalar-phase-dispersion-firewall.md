# R-106660 — Scalar phase optimization is exact in rank one but not in several channels

Claim ID: `R-106660`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-26  
Depends on: `L-106660`  
RH status: **not assumed**

## 1. One-pole calibration

Use the finite-inner pair from corrected `L-106514`,

\[
B_-(z)=\frac{z-i}{z+i},
\qquad
B_+(z)=\frac{z-1-i}{z-1+i}.
\]

The exact quantities are

\[
\mathcal O=\frac45,
\qquad
\mathcal C=1-\mathcal O=\frac15,
\]

and

\[
\Delta
=
\frac{12}{25}-\frac{16}{25}i,
\qquad
|\Delta|=\frac45.
\]

Therefore

\[
\boxed{
1-|\Delta|=\frac15=\mathcal C.
}
\tag{R-106660.1}
\]

By contrast, the unrotated phase mean is

\[
1-\operatorname{Re}\Delta=\frac{13}{25}.
\]

Thus the constant phase optimization removes the complete one-channel slack.

## 2. Two-channel phase-dispersion firewall

At the abstract principal-channel level, take two equal overlap weights
\(r^2\) with opposite trace phases. Then

\[
\mathcal O=2r^2,
\qquad
\Delta=r^2-r^2=0.
\]

For denominator dimension \(m_-=2\),

\[
\mathcal C=2-2r^2,
\qquad
m_- -|\Delta|=2.
\]

At \(r=1/2\),

\[
\boxed{
\mathcal C=\frac32,
\qquad
m_- -|\Delta|=2,
\qquad
\text{slack}=\frac12.
}
\tag{R-106660.2}
\]

This fixture is a linear-algebra firewall: a single scalar phase cannot recover
a positive overlap whose principal channels carry cancelling phases. An
application to finite inner functions must therefore prove Xi-specific phase
alignment; it cannot promote `L-106660` to equality source-blindly.

## 3. Resolvent strictness

For a scalar compression eigenvalue \(0<x<1\) and \(\tau>0\),

\[
\mathcal Q_\tau(x)-x
=
\frac{\tau x(1-x)}{1+\tau x}>0.
\]

Thus the resolvent certificate is also a genuine upper envelope at fixed
\(\tau\). It becomes exact only as \(\tau\downarrow0\), or on projection
eigenvalues \(0,1\).

## Disposition

```text
rank-one optimized phase = canonical charge        TRUE
many-channel optimized phase = canonical charge    FALSE IN GENERAL
fixed-tau resolvent = canonical charge              FALSE IN GENERAL
Xi phase alignment / Xi resolvent estimate          OPEN
```
