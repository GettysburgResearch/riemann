# R-90902 — Absolute Chebyshev majorants cannot close the first-Hermite criterion

Claim ID: `R-90902`  
Status: **PROPOSED COMPLETE EXPONENT BARRIER**  
Created: 2026-08-11  
Depends on: the pole-subtracted log-coordinate formula underlying PRs #375/#379

The first-Hermite prime formula contains a raw saddle of size \(e^{q/4}\), but its leading part is exactly the zeta-pole continuum and cancels against the explicit pole term.  What remains is a Gaussian transform of the Chebyshev error.  This note quantifies why classical absolute error bounds still cannot prove the RH-equivalent sign.

Let

\[
 E(x)=\psi(x)-x.
\]

After exact pole subtraction and one Stieltjes integration by parts, the arithmetic part of the first-Hermite scalar is a finite linear combination of integrals of the shape

\[
 \int_0^\infty
 E(e^t)e^{-t/2}
 P_q(t)e^{-t^2/(4q)}e^{-ixt}\,dt,
\tag{R-90902.1}
\]

where \(P_q\) is polynomial in \(t,q^{-1}\) and does not alter exponential rates.

Assume only a pointwise source bound

\[
 |E(X)|\le X^\theta(\log X)^A
 \qquad(X\ge X_0)
\tag{R-90902.2}
\]

for some \(\theta>1/2\).  Taking absolute values in (R-90902.1) gives the saddle exponent

\[
 (\theta-1/2)t-\frac{t^2}{4q},
\]

whose maximum is attained at

\[
 t_*=2q(\theta-1/2)
\]

with value

\[
 \boxed{q(\theta-1/2)^2.}
\tag{R-90902.3}
\]

Thus every argument using only (R-90902.2) and absolute values yields, up to powers of \(q\),

\[
 |\text{arithmetic error}|
 \le\exp\big(q(\theta-1/2)^2+o(q)\big).
\tag{R-90902.4}
\]

A terminal off-line zero at depth

\[
 y=\Re\rho-1/2>0
\]

contributes on the zero side at scale

\[
 \exp(qy^2).
\tag{R-90902.5}
\]

Therefore an absolute-majorant proof can dominate the error only when

\[
 \theta<1/2+y=\Re\rho.
\tag{R-90902.6}
\]

But a bound (R-90902.2) with \(\theta<\Re\rho\) already excludes a zeta pole at \(\rho\) by the classical Mellin/Landau argument.  In particular:

```text
PNT / Vinogradov--Korobov majorants + absolute values
    cannot prove the all-depth first-Hermite sign;

a fixed power-saving Chebyshev bound
    is already a fixed zero-free strip;

square-root-scale control for every epsilon
    is RH-strength.
```

The first-Hermite route must exploit source-specific oscillation, a positive matrix/factorization, or an equivalent cancellation before absolute values.  This is the same methodological wall recorded repeatedly in the Anthropic coordination volume, now with the exact Gaussian saddle exponent.
