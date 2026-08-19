# L-99240 — Every canonical component row factors through the SHARP target with a strictly positive anchor-free kernel

Claim ID: `L-99240`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-19  
Frozen parent: PR #636 at `387f775f95d5e21e01c3fb39d91acc5b67f62b02`  
RH status: **not assumed**

## 1. Canonical row coefficients

Fix an integer `j>=2` and put

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

Define

\[
 \gamma_j(m)=
 \begin{cases}
  A_j,&m=j,\\
  -B_j,&m=j+1,\\
  C_j,&m\ge j+2,\\
  0,&m<j.
 \end{cases}
\tag{L-99240.1}
\]

Then the canonical parabolic component row is exactly

\[
 Q_Y(j)
 =\sum_{m\le Y}\frac{\gamma_j(m)}{\sqrt m}
  \log\frac Ym.
\tag{L-99240.2}
\]

Let the single-SHARP target be

\[
 T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1}.
\tag{L-99240.3}
\]

## 2. The new row kernel

Put

\[
 \phi(u)=\frac{4u^{-3/2}-1}{3}\mathbf 1_{u\ge1}
\tag{L-99240.4}
\]

and

\[
 \boxed{
 \kappa_j(t)
 =\sum_{m\le t}\frac{\gamma_j(m)}{\sqrt m}\phi(t/m).
 }
\tag{L-99240.5}
\]

The key identity is

\[
 \boxed{
 \int_m^Y T(Y/t)\phi(t/m)\frac{dt}{t}
 =\log\frac Ym
 \qquad(Y\ge m).
 }
\tag{L-99240.6}
\]

Indeed, with `R=Y/m` and `u=t/m`, the integrand is

\[
 \frac{(4\sqrt{R/u}-3)(4u^{-3/2}-1)}{3u}.
\]

Its four elementary power terms integrate to `log R`; all three boundary
power terms cancel exactly. Substituting (L-99240.6) into (L-99240.2) and
using finite Fubini gives

\[
 \boxed{
 Q_Y(j)=\int_1^Y T(Y/t)\kappa_j(t)\frac{dt}{t}.
 }
\tag{L-99240.7}
\]

Thus the SHARP target, rather than the disputed equality-score state, is the
primitive source of every component row.

## 3. Strict positivity of the kernel

The kernel vanishes on `t<j`. We prove

\[
 \boxed{\kappa_j(t)>0\qquad(t\ge j).}
\tag{L-99240.8}
\]

On an activation cell `N<=t<N+1`, put

\[
 G_{j,N}=\sum_{m\le N}m\gamma_j(m),\qquad
 H_{j,N}=\sum_{m\le N}\frac{\gamma_j(m)}{\sqrt m}.
\]

Then

\[
 3\kappa_j(t)=\frac{4G_{j,N}}{t^{3/2}}-H_{j,N}.
\]

For `N=j`, this is

\[
 \frac{A_j}{\sqrt j}
 \left[4(j/t)^{3/2}-1\right],
\]

which is positive through the whole cell because

\[
 4\left(\frac j{j+1}\right)^{3/2}>1
 \qquad(j\ge2).
\]

For `N>=j+1`, direct summation gives the exact moment identity

\[
 G_{j,N}=\frac{N(N+1)}{j(j-1)}.
\tag{L-99240.9}
\]

The cell expression decreases with `t`, so it is enough to take the limiting
right endpoint. Dividing by `C_j=2/[j(j-1)]` reduces positivity to

\[
 \Delta_{j,N}:=
 \frac{2N}{\sqrt{N+1}}
 -
 \left[
 \frac{j(j+1)}{2\sqrt j}
 -\frac{(j+1)(j-2)}{2\sqrt{j+1}}
 +\sum_{m=j+2}^{N}\frac1{\sqrt m}
 \right]>0.
\tag{L-99240.10}
\]

At `N=j+1`,

\[
 \Delta_{j,j+1}
 =(j+1)\left[
 \frac2{\sqrt{j+2}}-\frac{\sqrt j}{2}
 +\frac{j-2}{2\sqrt{j+1}}
 \right]>0.
\]

For `j=2` this is immediate. For `j>=3`, use

\[
 \frac{j-2}{\sqrt{j+1}}\ge\frac{j-3}{\sqrt j}
\]

(the squared numerator difference is `j^2+j-9>0`) and

\[
 \frac4{\sqrt{j+2}}>\frac3{\sqrt j}.
\]

Finally,

\[
 \Delta_{j,N+1}-\Delta_{j,N}
 =
 \frac{2(N+1)}{\sqrt{N+2}}
 -\frac{2N+1}{\sqrt{N+1}}>0,
\]

because after squaring the positive sides the difference is exactly

\[
 4(N+1)^3-(2N+1)^2(N+2)=3N+2>0.
\]

This proves (L-99240.8) without a finite scan.

## 4. Mellin-symbol audit

The two elementary Mellin factors are

\[
 \int_1^\infty T(y)y^{-s-1}dy
 =\frac{s+\frac32}{s(s-\frac12)}
\]

and

\[
 \int_1^\infty \phi(y)y^{-s-1}dy
 =\frac{s-\frac12}{s(s+\frac32)}.
\]

Their product is exactly `1/s^2`, the Mellin multiplier of the logarithmic
ramp. This is an independent transform audit of (L-99240.6).

## 5. Scope

This theorem is row-specific. That is sufficient for the fixed-row
Mellin--Landau consumer: after a hypothetical zero is chosen, one fixed
sufficiently large row is selected.

The theorem does not assert positivity of the signed global equality weight.
It replaces the second-order equality-frame inversion by a first-order,
source-normalized factorization whose boundary normalization is already fixed
by (L-99240.6).
