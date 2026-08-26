# L-105504 — The native signed-cell deficit and tail-pair Hodge gate are RH-equivalent

Claim ID: `L-105504`

Status: **PROVED EXACT EQUIVALENCE REDUCTION; TERMINAL SOURCE-SPECIFIC ESTIMATE OPEN**

Created: 2026-08-27

Depends on: `L-100310--L-100311`; fixed negative-mass Mellin–Landau consumer; `L-103201`; `L-105501--L-105503`

RH status: **unproved**

Let

\[
G_2(X)
=
\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}K_2(X/n),
\qquad K_2=DK_1.
\tag{L-105504.1}
\]

## 1. Exact negative area of one cell

Fix \(m\ge1\), put

\[
a=\sqrt m,\qquad b=\sqrt{m+1},
\]

and let \(u=G_2(m+)\), \(v=G_2((m+1)-)\).  On the cell,

\[
G_2(t^2)=A+Bt,
\]

where

\[
B=\frac{v-u}{b-a},
\qquad
A=\frac{bu-av}{b-a}.
\]

Put

\[
F(t)=A\log t+Bt.
\]

Define

\[
\mathfrak n_m(u,v)
=
2\int_a^b\frac{(-A-Bt)_+}{t}\,dt.
\tag{L-105504.2}
\]

This has the exact elementary form

\[
\mathfrak n_m(u,v)=
\begin{cases}
0,&u,v\ge0,\\
-2(F(b)-F(a)),&u,v\le0,\\
-2(F(r)-F(a)),&u<0<v,\\
-2(F(b)-F(r)),&u>0>v,
\end{cases}
\tag{L-105504.3}
\]

where, in the sign-changing cases,

\[
r=\frac{av-bu}{v-u}.
\]

No quadrature or smoothing is involved.

## 2. Purely discrete endpoint data

For

\[
c_n=\frac{\mu(n)}{\sqrt n},
\]

let \(W_\mu\) be (L-105503.7).  Equations
(L-105503.10)--(L-105503.12) give

\[
\boxed{
u_m=-\Delta_4W_\mu(m),
}
\tag{L-105504.4}
\]

\[
\boxed{
v_m
=
-\Delta_4W_\mu(m+1)
-\Delta_{4,\rm at}c(m+1).
}
\tag{L-105504.5}
\]

Therefore, for integer \(Y\),

\[
\boxed{
\int_1^Y(G_2(X))_-\frac{dX}{X}
=
\sum_{1\le m<Y}\mathfrak n_m(u_m,v_m).
}
\tag{L-105504.6}
\]

Define

```text
NATIVECELL105504:
  sum_(1<=m<Y) n_m(u_m,v_m) = Y^o(1).
```

The Mellin transform of \(G_2\) is

\[
\frac{\widehat K_2(s)}{\zeta(s+\frac12)}.
\]

The multiplier (L-105503.2) is nonzero for
\(0<\Re s<1/2\).  The fixed negative-mass Mellin–Landau theorem and the
standard RH converse therefore give

\[
\boxed{
\mathrm{NATIVECELL}_{105504}
\Longleftrightarrow
\mathrm{RH}.
}
\tag{L-105504.7}
\]

## 3. Derivative Type-I with a frozen sixth-power cutoff

The derivative kernel is of bounded variation and satisfies

\[
\int_1^{16}K_2(y)y^{-3/2}\,dy
=
\widehat K_2(1/2)=0.
\tag{L-105504.8}
\]

Put

\[
k_2(x)=x^{-1/2}K_2(1/x).
\]

The bounded-variation Riemann-sum estimate yields

\[
\boxed{
\sum_{m\ge1}\frac1{\sqrt m}K_2(Y/m)
=
O_{K_2}(Y^{-1/2}).
}
\tag{L-105504.9}
\]

Because \(K_2\) has jumps, the stronger \(Y^{-3/2}\) estimate valid for
\(K_1\) is not claimed.

On the dyadic block \(I_j=[2^j,2^{j+1})\), freeze

\[
U_j=\lfloor2^{j/6}\rfloor.
\]

For every sufficiently large \(j\), one has \(U_j<X/16\) throughout
\(I_j\), so compact support removes the finite \(2\mu_{U_j}\) row.  The
finitely many initial blocks have finite logarithmic mass and are absorbed
once into the initial ledger.  Applying the exact Vaughan identity to the
fixed scalar \(G_2\) then gives, on every cofinal block,

\[
G_2=T_{2,j}+B_{2,j}
\quad\text{on }I_j.
\tag{L-105504.10}
\]

Equation (L-105504.9) gives

\[
|T_{2,j}(X)|
\ll
\frac{U_j^2}{\sqrt X}
\ll X^{-1/6}.
\tag{L-105504.11}
\]

Hence the complete Type-I row has finite logarithmic \(L^1\) mass.

## 4. Exact native F1 tail-Hodge gate

By `L-105501`, the balanced source on \(I_j\) is the tail pair

\[
b_{U_j}=a_{U_j}*\nu_{U_j}.
\]

Let \(\mathcal D_j(x)\) be the mismatch energy (L-105502.4) in the extreme
tail gauge.  Then

\[
B_{2,j}(e^x)
=
-2L(D)\mathcal D_j(x),
\qquad
L(D)=D(D+\tfrac32)(D-\tfrac12).
\tag{L-105504.12}
\]

Define

```text
NATIVEF1XD105504:
  after the dyadic-frozen recombination,

  sum_j integral_(I_j cap [1,Y])
    ( L(D) D_j(log X) )_+ dX/X
  = Y^o(1).
```

By (L-105502.8),

\[
(B_{2,j})_-
=
2(L(D)\mathcal D_j)_+.
\]

Together with the absolutely integrable Type-I row,

\[
\boxed{
\mathrm{NATIVEF1XD}_{105504}
\Longleftrightarrow
\mathrm{NATIVECELL}_{105504}
\Longleftrightarrow
\mathrm{RH}.
}
\tag{L-105504.13}

This is the source-faithful F1 geometry of the live ordinary-Möbius
same-\(K_1\) cross-core frontier.  The estimate in
`NATIVEF1XD105504` remains open.
