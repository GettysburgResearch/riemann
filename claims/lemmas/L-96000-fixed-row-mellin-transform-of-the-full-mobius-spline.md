# L-96000 — Every prime-sieved component row has an explicit reciprocal-zeta Mellin transform

Claim ID: `L-96000`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: the row formula in `L-94200`; the full-row identity in `L-94201`  
RH status: **not assumed**

Fix \(j\ge2\), and put

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

The canonical component row is

\[
 Q_X(j)=
 \frac{A_j}{\sqrt j}\log\frac Xj\,\mathbf1_{X\ge j}
 -
 \frac{B_j}{\sqrt{j+1}}\log\frac X{j+1}\,\mathbf1_{X\ge j+1}
 +
 C_j\sum_{m\ge j+2}
 \frac1{\sqrt m}\log\frac Xm\,\mathbf1_{X\ge m}.
\tag{L-96000.1}
\]

Define

\[
 f_j(X)=c_X(j)=
 \sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\tag{L-96000.2}
\]

The prime-sieved theorem gives \(f_j(X)\ge0\).

For \(\Re s>1/2\), termwise integration is absolute and

\[
 \int_m^\infty \log\frac Xm\,X^{-s-1}\,dX=\frac{m^{-s}}{s^2}.
\]

With \(z=s+\tfrac12\),

\[
 \int_1^\infty Q_X(j)X^{-s-1}\,dX=\frac{H_j(z)}{s^2},
\]

where

\[
 H_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
 +C_j\sum_{m\ge j+2}m^{-z}.
\]

Write

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
 -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

Then \(H_j(z)=C_j\zeta(z)+P_j(z)\). After the substitution \(X=kY\),

\[
\begin{aligned}
 \mathcal C_j(s)
 &:={}
 \int_1^\infty f_j(X)X^{-s-1}\,dX\\
 &=
 \left(\sum_{k\ge1}\frac{\mu(k)}{k^{s+1/2}}\right)
 \frac{H_j(s+1/2)}{s^2}.
\end{aligned}
\]

Hence initially for \(\Re s>1/2\),

\[
 \boxed{
 \mathcal C_j(s)=
 \frac{C_j}{s^2}+
 \frac{P_j(s+\tfrac12)}
 {s^2\zeta(s+\tfrac12)}.
 }
\tag{L-96000.3}
\]

This gives meromorphic continuation to \(\Re s>0\). For real \(s>0\),
\(\zeta(s+\tfrac12)\) has no real zero; the pole at \(s=\tfrac12\) is harmless
because \(1/\zeta\) vanishes there. Therefore \(\mathcal C_j\) is analytic at
every positive real \(s\).

At a nontrivial zero \(\rho\), cancellation can occur only if \(P_j(\rho)=0\).
The next lemma proves that no open-strip zero cancels every sufficiently large
row.

```text
fixed-row Mellin transform             exact
reciprocal-zeta factor                 exact
real-axis analyticity for s>0          exact
off-line-zero cancellation             reduced to P_j(rho)
prime-sieved row positivity            imported finite theorem
RH                                     not assumed
```
