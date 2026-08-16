# L-96000 — Every prime-sieved component row has an explicit reciprocal-zeta Mellin transform

Claim ID: `L-96000`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: the row formula in `L-94200`; the full-row identity in `L-94201`  
RH status: **not assumed**

## 1. Fixed row and coefficients

Fix an integer `j>=2`. Put

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

For real `X>=1`,

\[
 Q_X(j)=
 \frac{A_j}{\sqrt j}\log\frac Xj\,\mathbf1_{X\ge j}
 -\frac{B_j}{\sqrt{j+1}}\log\frac X{j+1}\,\mathbf1_{X\ge j+1}
 +C_j\sum_{m\ge j+2}\frac1{\sqrt m}\log\frac Xm\,\mathbf1_{X\ge m}.
\tag{L-96000.1}
\]

Define the full Möbius row

\[
 f_j(X):=c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\tag{L-96000.2}
\]

The prime-sieved theorem `L-94200--L-94201` gives

\[
 \boxed{f_j(X)\ge0.}
\tag{L-96000.3}
\]

An elementary absolute estimate gives `f_j(X)=O_j(sqrt(X) log(2X))`, so its Mellin transform has a finite abscissa of convergence.

## 2. Mellin transform of one canonical row

For `Re(s)>1/2`, termwise integration is absolute. Since

\[
 \int_m^\infty \log\frac Xm\,X^{-s-1}\,dX=\frac{m^{-s}}{s^2},
\]

we obtain, with `z=s+1/2`,

\[
 \int_1^\infty Q_X(j)X^{-s-1}\,dX=\frac{H_j(z)}{s^2},
\tag{L-96000.4}
\]

where

\[
 H_j(z)=A_jj^{-z}-B_j(j+1)^{-z}+C_j\sum_{m\ge j+2}m^{-z}.
\tag{L-96000.5}
\]

Write

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}-C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-96000.6}
\]

Then

\[
 H_j(z)=C_j\zeta(z)+P_j(z).
\tag{L-96000.7}
\]

## 3. Full Möbius transform

Interchanging the finite row with the absolutely convergent Möbius Dirichlet series gives

\[
\begin{aligned}
 \mathcal C_j(s)&:=\int_1^\infty f_j(X)X^{-s-1}\,dX\\
 &=\left(\sum_{k\ge1}\frac{\mu(k)}{k^{s+1/2}}\right)\frac{H_j(s+1/2)}{s^2}.
\end{aligned}
\]

Hence initially for `Re(s)>1/2`,

\[
 \boxed{
 \mathcal C_j(s)=\frac{C_j}{s^2}+\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
 }
\tag{L-96000.8}
\]

The right side supplies the meromorphic continuation to `Re(s)>0`.

## 4. Positive real axis

For real `s>0`, the argument `s+1/2` lies in `(1/2,infinity)`. The zeta function has no real zero there. Its pole at `s+1/2=1` is harmless in (L-96000.8), because `P_j/zeta` tends to zero. Therefore

\[
 \boxed{\mathcal C_j(s)\text{ is analytic at every real }s>0.}
\tag{L-96000.9}
\]

At a nontrivial zero `rho`, the only possible cancellation of the pole of `1/zeta` is the explicit finite factor `P_j(rho)`. The next lemma proves that no open-strip zero cancels every row.

## 5. Boundary

```text
fixed-row Mellin transform             exact
reciprocal-zeta factor                 exact
real-axis analyticity for s>0          exact
off-line-zero cancellation             reduced to P_j(rho)
prime-sieved row positivity            imported finite theorem
RH                                     not assumed
```
