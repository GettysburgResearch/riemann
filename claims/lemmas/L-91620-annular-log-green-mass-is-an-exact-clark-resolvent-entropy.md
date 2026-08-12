# L-91620 — Annular log-Green mass is an exact Clark resolvent entropy

Claim ID: `L-91620`  
Status: **PROVED EXACT SCALAR CLARK/GREEN IDENTITY**  
Created: 2026-08-12  
Depends on: `L-91520`; `L-91420`; sibling `L-91610`  
RH status: **unproved**

## 1. One crossed-zero Blaschke factor

Let

\[
 \zeta=x+iy,
 \qquad x>0,
\]

be a right-half-plane crossed-zero coordinate, and let

\[
 b_\zeta(z)=\frac{z-\zeta}{z+\overline\zeta}
\]

be its half-plane Blaschke factor.  At a fixed real interior node `eta>0`,

\[
 \boxed{
 |b_\zeta(\eta)|^2
 =\frac{(\eta-x)^2+y^2}{(\eta+x)^2+y^2}
 =:X_\zeta\in(0,1).
 }
\]

The logarithmic Green charge is

\[
 \boxed{
 g_\eta(\zeta)
 =-\log X_\zeta
 =\log\frac{(\eta+x)^2+y^2}{(\eta-x)^2+y^2}.
 }
\]

## 2. Exact Clark resolvent integral

Put

\[
 D_\zeta=1-X_\zeta.
\]

Then

\[
 \boxed{
 g_\eta(\zeta)
 =\int_0^1
  \frac{D_\zeta}{X_\zeta+tD_\zeta}\,dt.
 }
\]

This is the scalar Julia/Clark entropy formula

\[
 -\log X=\int_0^1\frac{1-X}{X+t(1-X)}dt.
\]

Thus every crossed-zero Green charge is the resolvent-integrated defect of its
one-node Blaschke return.

## 3. Annular product

Let `C_(a,b)` be the annular Blaschke product of `L-91520`, with zeros counted
with multiplicity.  Then

\[
 |C_{a,b}(\eta)|^2
 =\prod_{\zeta\in Z_{a,b}}X_\zeta^{m_\zeta}
\]

and therefore

\[
 \boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 =-2\log|C_{a,b}(\eta)|
 =\sum_{\zeta\in Z_{a,b}}m_\zeta g_\eta(\zeta).
 }
\]

No cancellation between crossed zeros is possible.

## 4. Hyperbolic-mass resolvent formula

The annular hyperbolic mass is

\[
 H_{a,b}^{\rm ann}(\eta)
 =\frac{|C_{a,b}(\eta)|^{-2}-1}{2\eta}.
\]

Hence

\[
 |C_{a,b}(\eta)|^{-2}=1+2\eta H_{a,b}^{\rm ann}(\eta),
\]

and

\[
 \boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 =\int_0^1
  \frac{2\eta H_{a,b}^{\rm ann}(\eta)}
       {1+2\eta tH_{a,b}^{\rm ann}(\eta)}dt.
 }
\]

The logarithmic annular obstruction is therefore a bounded resolvent average
of the one-node hyperbolic port.

## 5. Dyadic entropy telescope

At the dyadic scales of `L-91520`,

\[
 \Lambda_{a_J}(\eta)
 =\sum_{j=1}^J\Lambda_{a_j,a_{j-1}}^{\rm ann}(\eta).
\]

Each term is simultaneously:

```text
a sum of positive zero Green charges;
a log determinant of the annular Blaschke return;
a Clark resolvent entropy of the hyperbolic port.
```

This places the model obstruction in the same additive entropy coordinate as
the safe prime logarithmic generator of sibling `L-91610`.

## 6. Exact boundary

```text
one-zero Green charge                           EXACT
one-zero Clark resolvent entropy                EXACT
annular charge additivity                       EXACT
hyperbolic-mass resolvent formula               EXACT
dyadic entropy telescope                        EXACT
arithmetic source-to-model entropy identification OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
