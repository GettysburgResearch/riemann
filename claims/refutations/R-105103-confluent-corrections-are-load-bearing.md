# R-105103 — Merged Laurent corrections are load bearing

Claim ID: R-105103

Status: **PROPOSED EXACT MULTIPLICITY FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105103

RH status: **unproved**

## 1. A single merged-support polynomial

Let

\[
p(x)=1+x^3+x^4.
\]

Its denominator support consists of the three distinct real points

\[
0,\qquad -\frac34,\qquad -\frac12.
\]

At zero,

\[
(\operatorname{ord}p,\operatorname{ord}p',\operatorname{ord}p'')
=(0,2,1),
\]

so this common \(p'/p''\) point belongs once to the merged exceptional
class. Exact series division gives

\[
\operatorname{Res}_0\frac p{p'}=-\frac49,
\qquad
\operatorname{Res}_0\frac{p^2}{p'p''}=\frac{38}{81}.
\tag{R-105103.1}
\]

At the simple noncommon \(p'\)-zero \(-3/4\),

\[
\rho=\frac{229}{576},
\qquad
\rho^2=\frac{52441}{331776}.
\tag{R-105103.2}
\]

At the isolated simple \(p''\)-zero \(-1/2\),

\[
\tau=-\frac{75}{128}.
\tag{R-105103.3}
\]

The independent residue-at-infinity sums are

\[
\Phi_{1,p}=-\frac3{64},
\qquad
B_p=\frac{169}{4096}.
\tag{R-105103.4}
\]

The merged ledger reconstructs the simple noncommon real stratum:

\[
-\Phi_{1,p}+\Lambda_{1,p}^{\mathrm{mrg}}
=\frac3{64}-\frac49
=-\frac{229}{576},
\tag{R-105103.5}
\]

\[
B_p-D_{2,p}^{s}-\Lambda_{2,p}^{\mathrm{mrg}}
=\frac{169}{4096}+\frac{75}{128}-\frac{38}{81}
=\frac{52441}{331776}.
\tag{R-105103.6}
\]

Dropping \(\Lambda_1^{\mathrm{mrg}}\) manufactures the false positive
carrier \(3/64\), although the true signed carrier is negative. Dropping
\(\Lambda_2^{\mathrm{mrg}}\) produces \(2569/4096\), not the true
second moment. Treating zero as two events, one for each denominator factor,
would double count the same local Laurent residue.

## 2. No favorable merged-residue sign

The family

\[
F(w)=1+w^3+bw^4+cw^5
\]

has \((m,r,s)=(0,2,1)\) at zero and

\[
\operatorname{Res}_0P_F=-\frac{4b}{9},
\qquad
\operatorname{Res}_0Q_F=\frac{38b^2}{81}-\frac{5c}{18}.
\tag{R-105103.7}
\]

Thus \(b=0,c=1\) gives the negative second correction \(-5/18\), while

\[
F(w)=w+\frac{w^5}{5}
\]

has \((m,r,s)=(1,0,3)\) and second correction \(+1/4\). The merged
correction has no universal sign.

Finally, \(F(w)=w^3\) has a common parent/derivative multiplicity event but

\[
P_F(w)=\frac w3,
\qquad
Q_F(w)=\frac{w^3}{18}.
\]

Both residues vanish. Even the simple common event \(F(w)=w^2\) has both
residues zero. Hence neither zero residue nor contour removability is a
simplicity/common-freedom certificate, and the event manifest is logically
independent of the residue sum.
