# L-96100 — The PR #542 row is a discrete-tail spline with an exact rough-reservoir plus finite-frontier decomposition

Claim ID: `L-96100`  
Status: **PROVED EXACT FINITE ALGEBRA / ROUTE INFRASTRUCTURE**  
Created: 2026-08-16  
Frozen analytic successor: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`  
RH status: **unproved**

## 1. Correct source of the row formula

For real `Y>=1` and integer `a>=2`, define the discrete tail

\[
 T_Y(a)=
 \sum_{m=a}^{\lfloor Y\rfloor}
 \frac1{\sqrt m}\log\frac Ym,
\tag{L-96100.1}
\]

with the empty sum interpreted as zero, and put

\[
 A_Y^{\rm tail}(a)=\frac{T_Y(a)}{a-1}.
\]

For `j>=2`, set

\[
 Q_Y^{\rm tail}(j)
 =(j+1)\left[
   A_Y^{\rm tail}(j)
  -2A_Y^{\rm tail}(j+1)
  +A_Y^{\rm tail}(j+2)
 \right].
\tag{L-96100.2}
\]

The coefficient of one source index `m` in (L-96100.2) is

\[
 q_j(m)=
 \begin{cases}
 0,&m<j,\\[1mm]
 A_j,&m=j,\\[1mm]
 -B_j,&m=j+1,\\[1mm]
 C_j,&m\ge j+2,
 \end{cases}
\tag{L-96100.3}
\]

where

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

Therefore

\[
 \boxed{
 Q_Y^{\rm tail}(j)
 =\sum_{m\le Y}\frac{q_j(m)}{\sqrt m}\log\frac Ym.
 }
\tag{L-96100.4}
\]

This is exactly the row used in `L-96000`. No parabolic endpoint formula is
needed or imported.

## 2. Conjugated finite Euler sieve

Put

\[
 \Psi(u)=\sqrt u\log u\,\mathbf1_{u\ge1},
 \qquad
 G_j(Y)=\sqrt Y\,Q_Y^{\rm tail}(j)
       =\sum_{m\ge1}q_j(m)\Psi(Y/m).
\tag{L-96100.5}
\]

Let `P` be any squarefree product. Define

\[
 \mathfrak S_{P,j}(Y)
 =\sum_{d\mid P}\mu(d)G_j(Y/d).
\tag{L-96100.6}
\]

Grouping by the product `n=dm` gives

\[
 \boxed{
 \mathfrak S_{P,j}(Y)
 =\sum_{n\ge1}\omega_{P,j}(n)\Psi(Y/n),
 }
\tag{L-96100.7}
\]

\[
 \boxed{
 \omega_{P,j}(n)
 =\sum_{d\mid(n,P)}\mu(d)q_j(n/d).
 }
\tag{L-96100.8}
\]

Every source occurrence has the unique label `(d,m)` with `n=dm`; grouping
changes no coefficient.

## 3. Positive rough reservoir and finite signed frontier

The four-level coefficient can be written

\[
 q_j(m)=C_j+h_j(m),
\tag{L-96100.9}
\]

where

\[
 h_j(m)=
 \begin{cases}
 -C_j,&m<j,\\[1mm]
 \dfrac{j+2}{j},&m=j,\\[2mm]
 -1,&m=j+1,\\[1mm]
 0,&m\ge j+2.
 \end{cases}
\tag{L-96100.10}
\]

Indeed `A_j-C_j=(j+2)/j` and `-B_j-C_j=-1`.
Using

\[
 \sum_{d\mid(n,P)}\mu(d)=\mathbf1_{(n,P)=1},
\]

(L-96100.8) becomes

\[
 \boxed{
 \omega_{P,j}(n)
 =C_j\mathbf1_{(n,P)=1}
 +\sum_{\substack{d\mid P,\ m\le j+1\\dm=n}}
   \mu(d)h_j(m).
 }
\tag{L-96100.11}
\]

Thus:

1. the infinite reservoir is the positive sequence
   `C_j 1_((n,P)=1)`;
2. every signed correction is attached to one explicit pair `(d,m)` with
   `m<=j+1`;
3. the signed frontier is supported on
   \[
   n\le(j+1)P;
   \]
4. for `n>(j+1)P`,
   \[
   \omega_{P,j}(n)=C_j\mathbf1_{(n,P)=1}\ge0.
   \]

This is the correct ownership ledger. A proof may spend a rough atom only once,
and any payment between different logarithmic knots must be recorded as a
cross-`n` transport.

## 4. Exact call-potential form

Let `x=log Y` and define the signed log-knot measure

\[
 \nu_{P,j}
 =\sum_{n\ge1}\frac{\omega_{P,j}(n)}{\sqrt n}
   \delta_{\log n}.
\tag{L-96100.12}
\]

Then

\[
 \boxed{
 e^{-x/2}\mathfrak S_{P,j}(e^x)
 =\int_{(-\infty,x]}(x-t)\,d\nu_{P,j}(t)
 =:\mathcal C_{P,j}(x).
 }
\tag{L-96100.13}
\]

Equivalently, at an integer activation point `N`, put

\[
 M_{P,j}(N)=\sum_{n\le N}\frac{\omega_{P,j}(n)}{\sqrt n},
\]

\[
 L_{P,j}(N)=\sum_{n\le N}
 \frac{\omega_{P,j}(n)}{\sqrt n}\log n.
\]

Then

\[
 \boxed{
 \mathcal C_{P,j}(\log N)
 =\log N\,M_{P,j}(N)-L_{P,j}(N).
 }
\tag{L-96100.14}
\]

On every interval `log N<x<log(N+1)`, the potential is affine in `x`.
Consequently

\[
 \boxed{
 \mathfrak S_{P,j}(Y)\ge0\ \text{for all real }Y
 \iff
 \mathcal C_{P,j}(\log N)\ge0\ \text{for all integers }N\ge1.
 }
\tag{L-96100.15}
\]

This is an exact activation-knot reduction, not a finite truncation of the
universal theorem.

## 5. Boundary

```text
discrete-tail row definition                     exact
four-level coefficient q_j                       exact
finite Euler coefficient omega                   exact
positive rough reservoir                         exact
finite signed frontier                            exact
one-use source ownership                          exact
cross-n call potential                            exact
universal nonnegativity of that potential         OPEN / RH-BEARING
PR #542 direct Mellin-Landau consumer              CONDITIONAL
Riemann Hypothesis                                UNPROVED
```

`X-96100` checks (L-96100.3) and (L-96100.11) on deterministic exact fixtures.
