# L-102600 — Moving completion and greatest-owner first chaos cancel exactly

Claim ID: `L-102600`  
Status: **PROVED EXACT FINITE SOURCE IDENTITY**  
Created: 2026-08-22  
Depends on: PR #715 `L-102500--L-102503`  
RH status: **not assumed**

Let \(\ell_1,\ldots,\ell_m\) be an ordered finite multiset of labelled primes.
The two copies of \(67\) are distinct labels.  Put

\[
r_j=p_j^{-1/2},
\qquad
Z_j=e^{-i\vartheta_j}U_j,
\]

where the \(U_j\) commute.  Define the native, positive-completion and squared
prefixes

\[
E_j=\prod_{h\le j}(I-r_hZ_h),
\]

\[
A_j=\prod_{h\le j}(I+r_hZ_h),
\]

\[
C_j=A_jE_j
=\prod_{h\le j}(I-r_h^2Z_h^2).
\]

Write \(E_0=A_0=C_0=I\).

## 1. The two first-chaos atoms

The native greatest-owner update, completed only on the preceding prefix, is

\[
\begin{aligned}
O_j
&=A_{j-1}(E_j-E_{j-1})\\
&=-r_jZ_jC_{j-1}.
\end{aligned}
\]

The moving-completion update on the same preceding native prefix is

\[
\begin{aligned}
T_j
&=(A_j-A_{j-1})E_{j-1}\\
&=+r_jZ_jC_{j-1}.
\end{aligned}
\]

Therefore

\[
\boxed{O_j+T_j=0.}
\tag{L-102600.1}
\]

The cancellation is coefficient-exact, phase-exact and source-exact.  It occurs
before labelled products are collapsed to integers and before an absolute
value or norm is taken.

## 2. Simultaneous update

Completing and activating the same label simultaneously gives

\[
\begin{aligned}
C_j-C_{j-1}
&=A_jE_j-A_{j-1}E_{j-1}\\
&=-r_j^2Z_j^2C_{j-1}.
\end{aligned}
\]

Hence

\[
\boxed{
\text{native owner}
+
\text{completion transfer}
+
\text{cross term}
=
\text{squared update}.
}
\tag{L-102600.2}
\]

The surviving activity is \(p_j^{-1}\) on the shift \(U_{p_j^2}\).

## 3. Channel functoriality

Every fixed operator commuting with the multiplicative shifts preserves these
identities.  In particular they hold simultaneously for

\[
\Phi_*,
\qquad
D\Phi_*,
\qquad
\frac12(D+\tfrac32)\Phi_*,
\]

and for every exact source-owned regional restriction.

## Scope

Equation (L-102600.1) proves that the moving scale-transfer atom and the
unsquared-owner OCC atom are the same first-chaos object with opposite signs.
It does not identify the native source with its squared completion.  That
remaining difference is isolated in `L-102602`.
