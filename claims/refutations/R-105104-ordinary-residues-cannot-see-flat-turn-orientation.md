# R-105104 — Ordinary residues cannot see flat-turn orientation

Claim ID: R-105104

Status: **PROPOSED EXACT NO-GO FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105103; L-105104

RH status: **unproved**

On \([-1,1]\), let

\[
f_\pm(x)=x^6\pm\frac1{64}.
\tag{R-105104.1}
\]

Both endpoint values are positive. Both derivatives have the same unique
critical support:

\[
f_\pm'(x)=6x^5,\qquad f_\pm''(x)=30x^4,
\]

so at zero \((m,r,s)=(0,5,4)\). For
\(P_\pm=f_\pm/f_\pm'\) and
\(Q_\pm=f_\pm^2/(f_\pm'f_\pm'')\),

\[
P_\pm(x)=\frac x6\pm\frac1{384x^5},
\tag{R-105104.2}
\]

\[
Q_\pm(x)
=\frac{x^3}{180}
\pm\frac1{5760x^3}
+\frac1{737280x^9}.
\tag{R-105104.3}
\]

Therefore

\[
\operatorname{Res}_0P_\pm
=\operatorname{Res}_0Q_\pm=0.
\tag{R-105104.4}
\]

Zero is the only finite denominator-support point, so the complete ordinary
first and second boundary residue charges are also zero for both functions.
Their event supports, orders, endpoint signs, and ordinary merged Laurent
corrections are identical.

Nevertheless,

\[
N_{\mathbb R}^{\mathrm{mult}}(f_+;(-1,1))=0,
\qquad
N_{\mathbb R}^{\mathrm{mult}}(f_-;(-1,1))=2.
\tag{R-105104.5}
\]

Indeed, with \(y=x^2\),

\[
y^3-\frac1{64}
=(y-\tfrac14)(y^2+\tfrac14y+\tfrac1{16}),
\]

\[
y^3+\frac1{64}
=(y+\tfrac14)(y^2-\tfrac14y+\tfrac1{16}),
\]

and both quadratic factors have discriminant \(-3/16\). Thus the minus
case has exactly the roots \(x=\pm1/2\), while the plus case has none.

The leading jet carriers do distinguish the pair:

\[
\rho_{0,+}^{\mathrm{jet}}=\frac1{384},
\qquad
\rho_{0,-}^{\mathrm{jet}}=-\frac1{384}.
\tag{R-105104.6}
\]

The plus event is a wrong flat minimum and the minus event is a good flat
minimum. Their \(Q\)-leading coefficient is the same positive square
\(1/737280=(\rho^{\mathrm{jet}})^2/5\).

Hence endpoint signs, event orders, and the ordinary \(w^{-1}\) residues of
\(P,Q\) do not determine flat-turn orientation and cannot by themselves
supply the good-turn input in an L-104522-type bound. The leading principal
coefficient—or equivalent orientation data—is load bearing.

Common-event mass is independently load bearing: \(f(x)=x^m\) has zero
ordinary \(P,Q\) residues at zero, but the parent zero has multiplicity
\(m=(m-1)+1\), exactly the common derivative-order mass plus one support
point in (L-105104.2).
