# L-106701 — A direct fifth-residue transition gate avoids canonical overpayment

Claim ID: `L-106701`  
Status: **PROVED EXACT AT FINITE REGULAR SCOPE**  
Created: 2026-08-27  
Depends on: the elementary reverse--Rolle residue criterion  
RH status: **not assumed**

Let `F` be real on the real axis and let

\[
Q=F^{(5)}.
\]

Suppose

\[
c_1<\cdots<c_M
\]

are simple real zeros of `Q` in a regular interval, and define

\[
\rho_j=\frac{F(c_j)}{F^{(6)}(c_j)}.
\]

If

\[
\rho_j\rho_{j+1}>0,
\]

then

\[
F(c_j)F(c_{j+1})<0
\]

because `F^(6)` alternates sign at consecutive simple real zeros of `F^(5)`. Hence `F` has a real zero in `(c_j,c_{j+1})`.

Let

\[
V_5=\#\{1\le j<M:\rho_j\rho_{j+1}\le0\}.
\]

Retaining endpoint and confluent events explicitly,

\[
\boxed{R_0\ge M-1-V_5-\mathcal E_{\rm reg}.}
\tag{L-106701.1}
\]

If the pinned simple-real fifth-derivative input is

\[
\frac MN>\frac{9863}{10000}-o(1),
\]

then

\[
\boxed{\limsup\frac{V_5+\mathcal E_{\rm reg}}N<\frac{863}{10000}}
\tag{L-106701.2}
\]

implies

\[
\liminf\frac{R_0}N>0.9.
\]

This gate is weaker than paying the complete positive canonical-correlation defect. It targets only the signed residue transitions that actually destroy Rolle intervals.
