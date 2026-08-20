# L-99610 — The factor-67 SHARP Harnack source has an exact positive reciprocal-Julia owner compiler

Claim ID: `L-99610`  
Status: **PROVED EXACT ARITHMETIC THEOREM**  
Created: 2026-08-20  
Depends on: PR #653 `L-99271`; PR #647 scalar source  
RH status: **not assumed**

Put `p=67` and

\[
\beta_p(n)=\mu(n)-\mathbf1_{p\mid n}\mu(n/p).
\]

Then the SHARP Harnack defect is

\[
\mathfrak H_p(x)=
\sum_{n\le x}\frac{\beta_p(n)}{\sqrt n}T(x/n),
\qquad T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\tag{L-99610.1}
\]

## 1. Exact inverse pair

Define

\[
B_p(z)=\frac{1-p^{-z}}{\zeta(z)}
      =\sum_{n\ge1}\frac{\beta_p(n)}{n^z},
\qquad
G_p(z)=\frac{\zeta(z)}{1-p^{-z}}
      =\sum_{n\ge1}\frac{g_p(n)}{n^z}.
\]

If `n=p^e m` and `(m,p)=1`, then

\[
\boxed{g_p(n)=e+1>0}
\tag{L-99610.2}
\]

and, when `m` is squarefree,

\[
\boxed{
\beta_p(p^em)=\mu(m)(1,-2,1,0,\ldots)_e.
}
\tag{L-99610.3}
\]

Otherwise `beta_p(n)=0`.  Hence

\[
\boxed{|\beta_p(n)|\le g_p(n),\qquad
       \beta_p*g_p=\delta_1.}
\tag{L-99610.4}
\]

The two coefficient channels

\[
u_p^\pm(n)=g_p(n)\pm\beta_p(n)
\]

are nonnegative.

## 2. Positive logarithmic owner source

Write

\[
-\frac{G_p'(z)}{G_p(z)}
=\sum_{d\ge2}\frac{\Lambda_p(d)}{d^z}.
\]

The only nonzero values are

\[
\boxed{
\Lambda_p(q^k)=\log q\quad(q\ne p),\qquad
\Lambda_p(p^k)=2\log p.
}
\tag{L-99610.5}
\]

Thus `Lambda_p>=0`.  Coefficient comparison gives

\[
g_p(n)\log n
=\sum_{\substack{d\mid n\\d>1}}\Lambda_p(d)g_p(n/d),
\tag{L-99610.6}
\]

\[
\beta_p(n)\log n
=-\sum_{\substack{d\mid n\\d>1}}\Lambda_p(d)\beta_p(n/d).
\tag{L-99610.7}
\]

For `n>1`, put

\[
P_n(d)=
\frac{\Lambda_p(d)g_p(n/d)}
     {g_p(n)\log n}.
\tag{L-99610.8}
\]

This is a probability distribution on prime-power divisors `d>1` of `n`.
With

\[
f_p(n)=\frac{\beta_p(n)}{g_p(n)}\in[-1,1],
\]

one has

\[
\boxed{
f_p(n)=-\sum_dP_n(d)f_p(n/d).
}
\tag{L-99610.9}
\]

Therefore, on the descending owner chain `N_(t+1)=N_t/d_t`,

\[
\boxed{M_t=(-1)^t f_p(N_t)}
\tag{L-99610.10}
\]

is a bounded martingale.

## 3. Exact logarithmic coefficient energy

Only the first three `p`-adic fibres contribute.  Consequently

\[
\sum_{n\le X}\frac{\beta_p(n)^2}{g_p(n)n}
\le
\left(1+\frac2p+\frac1{3p^2}\right)(1+\log X).
\tag{L-99610.11}
\]

Also

\[
\sum_{n\le X}\frac{g_p(n)}n
\le
(1-p^{-1})^{-2}(1+\log X).
\tag{L-99610.12}
\]

The SHARP Harnack source therefore has a positive reciprocal channel, an exact
parity martingale, and only logarithmic coefficient energy.  No unsigned rough
reservoir is introduced.
