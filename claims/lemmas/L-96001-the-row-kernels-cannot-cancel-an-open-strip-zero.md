# L-96001 — No open-strip zeta zero is cancelled by all component-row Mellin kernels

Claim ID: `L-96001`  
Status: **PROPOSED COMPLETE ANALYTIC NONCANCELLATION LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-96000`  
RH status: **not assumed**

Let

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
 -C_j\sum_{m=1}^{j+1}m^{-z}.
\]

Fix \(z\) with \(0<\Re z<1\), \(z\ne1\), and suppose \(\zeta(z)=0\).
Euler--Maclaurin gives

\[
 \sum_{m=1}^{j+1}m^{-z}
 =
 \frac{(j+1)^{1-z}}{1-z}
 +\frac12(j+1)^{-z}
 +O_z(j^{-\Re z-1}).
\]

Using

\[
 A_j=1+\frac2{j-1},\qquad B_j=1-C_j,\qquad
 C_j=\frac2{j(j-1)}
\]

and expanding the neighboring powers yields

\[
 \boxed{
 P_j(z)=
 -\frac{z(z+1)}{1-z}\,j^{-z-1}
 +O_z(j^{-\Re z-2}).
 }
\tag{L-96001.1}
\]

The leading coefficient is nonzero at every nontrivial zeta zero. Thus there is
\(J(z)\) such that

\[
 \boxed{P_j(z)\ne0\qquad(j\ge J(z)).}
\tag{L-96001.2}
\]

If the zero has multiplicity \(m\), then the same row retains a pole of order
\(m\). No uniform effective bound for \(J(z)\) is needed: after choosing a
hypothetical zero, Landau's argument uses one fixed row.

```text
finite cancellation polynomial          explicit
large-j leading coefficient             nonzero
uniform effective j                      not required
off-line zero survives some fixed row    proved
```
