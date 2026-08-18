# L-95502 — Any power saving for SACF implies a fixed zeta zero-free strip

Claim ID: `L-95502`  
Status: **PROPOSED COMPLETE ANALYTIC CONSEQUENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95401/T-95400`; `L-95501`  
Scope: implication from SACF bounds to zeta zero exclusion

## 1. Parent decomposition

Fix

\[
H=(\log(2X))^B
\]

and let \(\mathcal S_H(X)\) be PR #580's separated annular coprime form.
The diagonal and every deleted sector in PR #580 satisfy

\[
\boxed{
|\mathcal A(X)|^2
=
\mathcal S_H(X)
+O_B(\log^{B+2}(2X)).
}
\tag{L-95502.1}
\]

This includes the annular diagonal, near-diagonal, large-gcd, and small reduced
Type-I pieces.

## 2. General exponent dictionary

Assume for some \(0\le\theta<1/2\) that

\[
\boxed{
|\mathcal S_H(X)|\ll X^{2\theta}
}
\tag{L-95502.2}
\]

for all sufficiently large `X`. Equation (L-95502.1) gives

\[
\mathcal A(X)=O(X^\theta+\log^{(B+2)/2}(2X)).
\tag{L-95502.3}
\]

Consequently

\[
\int_1^\infty\mathcal A(X)X^{-z-1}\,dX
\]

is holomorphic in \(\Re z>\theta\).

By PR #580 and `L-95501`, its meromorphic expression is

\[
-\widehat J_0(z)M_o'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_o(z+\tfrac12),
\]

and every zero \(\rho\) of zeta with \(\Re\rho>1/2\) produces an uncancelled
pole at \(z=\rho-1/2\). Holomorphy therefore implies

\[
\boxed{
\zeta(\rho)=0
\Longrightarrow
\Re\rho\le\frac12+\theta.
}
\tag{L-95502.4}
\]

## 3. Fixed power saving

If for some \(\delta>0\),

\[
|\mathcal S_H(X)|\ll X^{1-\delta},
\]

then \(2\theta=1-\delta\), so

\[
\boxed{
\zeta(\rho)=0
\Longrightarrow
\Re\rho\le1-\frac\delta2.
}
\tag{L-95502.5}
\]

Thus any genuine fixed exponent improvement over the source-blind
\(O(X\operatorname{polylog}X)\) scale proves a fixed classical zero-free
strip for zeta.

## 4. Polylogarithmic SACF

If

\[
|\mathcal S_H(X)|\ll\log^A(2X),
\]

then (L-95502.3) has exponent \(\theta=0\). Hence no zero satisfies
\(\Re\rho>1/2\); functional-equation symmetry gives

\[
\boxed{
\mathrm{SACF}\Longrightarrow\mathrm{RH}.
}
\tag{L-95502.6}
\]

## 5. Interpretation

The statement does not say that dispersion, Type-II, or pretentious methods
cannot prove SACF. It states exactly what such a proof must accomplish. A
fixed power saving is already a fixed zero-free strip; the requested
polylogarithmic bound is a complete RH-producing estimate.

## 6. Boundary

```text
SACF exponent -> zeta zero-free exponent     PROVED
fixed SACF power saving -> fixed strip        PROVED
polylog SACF -> RH                            PROVED CONDITIONAL
unconditional fixed power saving              NOT PROVED
SACF                                           OPEN / RH-BEARING
RH                                             UNPROVEN
```
