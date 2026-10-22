# R-105105 — Squaring the first jet flux loses the second moment

Claim ID: R-105105

Status: **PROPOSED EXACT MUTATION FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105104; L-105105

RH status: **unproved**

Let \(f(x)=x^4-1\). At its order-three critical point zero,

\[
\rho^{\rm jet}=-\frac14,
\qquad
(\rho^{\rm jet})^2=\frac1{16}.
\]

The two original quotients are

\[
P=\frac x4-\frac1{4x^3},
\qquad
Q=\frac{x^3}{48}-\frac1{24x}+\frac1{48x^5}.
\]

The reduced first selector is \(W_1=x^2\), so

\[
\operatorname{Res}_0(W_1P)=-\frac14.
\]

But squaring this weighted quotient gives

\[
(W_1P)^2
=\frac{x^6}{16}-\frac{x^2}{8}+\frac1{16x^2},
\]

whose residue is zero. A square of a simple-pole flux creates a double pole;
it does not square the residue.

The correct second selector is

\[
W_2=3x^4.
\]

Indeed,

\[
\operatorname{Res}_0(W_2Q)=\frac1{16}.
\]

Omitting the factor three gives only \(1/48\), the leading \(Q\)-coefficient
\((\rho^{\rm jet})^2/r\). The unweighted ordinary \(Q\)-residue is instead
\(-1/24\). Thus none of

- the ordinary second residue;
- the square of the first weighted quotient; or
- the second selector without its multiplicity factor

recovers the jet second moment.

Nontarget annihilation is independently load bearing. For
\(f=x^3-3x+1\), the unweighted \(Q\)-residues at \(-1,0,1\) are

\[
\frac14,-\frac1{18},\frac1{36},
\]

whose sum is \(2/9\), while the two target jet squares sum to \(5/18\).
The selector \(W_2=x^2\) preserves the target values and kills the
\(F''\)-only pole at zero exactly.
