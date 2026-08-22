# R-90004 — Fourfold cumulative positivity of the first-entrance Möbius kernel fails

Claim ID: `R-90004` (provisional range; allocate before integration)  
Status: **EXACT RATIONAL REFUTATION OF A NATURAL GFEP INDUCTION SHORTCUT**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-28001` first-entrance algebra; the critical source definitions  
Scope: refutes one high-order Abel/cumulative proof mechanism; it does not refute GFEP

## 1. The transformed first-entrance kernel

Fix an endpoint `X`, target `n`, and entrance coordinate `p in [n,2n)`.
Let

\[
F(m)=mE_n(m,p),
\]

where `E_n` is the exact first-entrance probability.  Thus

\[
F(p)=p,
\qquad
F(q)=0\quad(n\le q<2n,\ q\ne p),
\]

and for `m>=2n`,

\[
\boxed{
F(m)=\frac12\bigl(
F(\lfloor m/2\rfloor)+F(\lceil m/2\rceil)
+F(\lceil m/3\rceil)+F(\lfloor2m/3\rfloor)
\bigr).}
\tag{R-90004.1}
\]

Put

\[
c(m)=F(m)-F(m-1)
\]

with `F(n-1)=0`, and define the Dirichlet-convolution kernel

\[
\boxed{
K(q)=\sum_{d\mid q}c(d)\mu(q/d).}
\tag{R-90004.2}
\]

If

\[
U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
\qquad R_X(m)=U_X(m)-U_X(m+1),
\]

then finite summation by parts and divisor switching give the exact scalar
identity

\[
\boxed{
\Sigma_{X,n}(p)
=\sum_{m=n}^{X}F(m)R_X(m)
=\sum_{q\le X}K(q)w_X(q).}
\tag{R-90004.3}
\]

This suggests an Abel strategy: prove that a fixed high-order cumulative sum of
`K` is nonnegative and use the corresponding finite difference of the critical
weight.

## 2. The fourfold proposal

Define successive prefixes

\[
C_1(Q)=\sum_{q\le Q}K(q),
\qquad
C_{r+1}(Q)=\sum_{u\le Q}C_r(u).
\tag{R-90004.4}
\]

Equivalently,

\[
C_4(Q)=\sum_{q\le Q}\binom{Q-q+3}{3}K(q).
\tag{R-90004.5}
\]

A tempting extension of the certified `X/20` band argument is

\[
C_4(Q)\ge0
\quad\text{for every first-entrance kernel and every }Q.
\tag{R-90004.6}
\]

It is false.

## 3. Exact witness

Take

\[
\boxed{X=1000,\qquad n=21,\qquad p=21.}
\tag{R-90004.7}
\]

The recurrence (R-90004.1) uses only division by two, so every `F(m)`, `c(m)`,
`K(q)`, and `C_r(Q)` is a dyadic rational.  Exact `Fraction` arithmetic gives

\[
\boxed{
C_4(841)=-\frac{21060753}{8}<0.}
\tag{R-90004.8}
\]

For orientation, the successive minimum values are

\[
\min C_1=-\frac{441}{8},
\qquad
\min C_2=-\frac{86331}{64},
\]

\[
\min C_3=-\frac{15781689}{256},
\qquad
\min C_4=-\frac{21060753}{8},
\]

\[
\min C_5=-\frac{1208117841}{128}.
\tag{R-90004.9}
\]

The sixth prefix happens to be nonnegative for this one witness, but that is not
a uniform mechanism: the first nonnegative cumulative order changes with
`X,n,p` and grows in further reconnaissance.

## 4. Meaning for GFEP

The certified bands in `T-90003/T-90005` use source-sign-aware occupancy
minorants tied to fixed ratio cells.  They do **not** iterate automatically to
all smaller ratios by a fixed fourth-order Abel positivity theorem.

The exact failure (R-90004.8) explains why the band proof becomes increasingly
expensive: deeper negative Möbius layers require complete ancestry
recombination rather than a fixed number of scalar cumulative integrations.

This refutation does not challenge the numerical or certified positivity of
`Sigma` itself.  At the witness above,

\[
\Sigma_{1000,21}(21)>0.
\]

It only removes the proposed sufficient certificate (R-90004.6).

## 5. Boundary

Refuted exactly:

- universal fourfold cumulative positivity of the transformed first-entrance
  kernel;
- automatic propagation of the `X/20` GFEP certificate by a fixed-order Abel
  induction.

Retained:

- the exact transformed identity (R-90004.3);
- all certified GFEP bands;
- GFEP and RH, both still open at their unconditional scopes.
