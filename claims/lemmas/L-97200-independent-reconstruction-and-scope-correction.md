# L-97200 — Independent reconstruction of the reciprocal-Julia inputs and the exact analytic scope

Claim ID: `L-97200`  
Status: **PROVED EXACT RECONSTRUCTION AND SCOPE CORRECTION**  
Created: 2026-08-18  
Frozen source: PR #570 at `992404909d6c2940ae8ae849633fe5530ed79db0`  
RH status: **unproved**

## 1. Reciprocal pair

Put

\[
G_\diamond(z)=\frac{\zeta(z)}{(1-2^{-z})(1-2^{-z-1})},
\qquad B_\diamond(z)=G_\diamond(z)^{-1}.
\]

Writing `n=2^e m`, `m` odd,

\[
g_\diamond(2^e m)=2e+2^{-e}>0,
\]

while, for odd squarefree `m`,

\[
\frac{b_\diamond(2^e m)}{\mu(m)}
=(1,-5/2,2,-1/2),\qquad e=0,1,2,3,
\]

and the higher dyadic fibres vanish. Direct local comparison gives
`|b_diamond(n)|<=g_diamond(n)`.

The generalized von Mangoldt source is nonnegative:

\[
\Lambda_\diamond(p^r)=\log p\quad(p\text{ odd}),
\qquad
\Lambda_\diamond(2^r)=(2+2^{-r})\log2.
\]

Coefficient comparison gives

\[
g_\diamond(n)\log n
 =\sum_{d\mid n,d>1}\Lambda_\diamond(d)g_\diamond(n/d),
\]

\[
b_\diamond(n)\log n
 =-\sum_{d\mid n,d>1}\Lambda_\diamond(d)b_\diamond(n/d).
\]

Consequently the channels `u^+=g+b` and `u^-=g-b` are nonnegative and swap with coefficient one. This independently reconstructs the positive compiler.

## 2. Parity and martingale

The matrix

\[
\Sigma_\diamond(n)=
\begin{pmatrix}g_\diamond(n)&b_\diamond(n)\\b_\diamond(n)&g_\diamond(n)\end{pmatrix}
\]

is positive semidefinite. Rough parity conjugates it by the coordinate-swap matrix, so cumulative parity is exact rather than a terminal label.

For

\[
P_n(d)=\frac{\Lambda_\diamond(d)g_\diamond(n/d)}{g_\diamond(n)\log n},
\qquad
f_\diamond(n)=\frac{b_\diamond(n)}{g_\diamond(n)},
\]

one has

\[
f_\diamond(n)=-\sum_dP_n(d)f_\diamond(n/d).
\]

Thus `(-1)^t f_diamond(N_t)` is a bounded martingale on the descending divisor chain.

The exact fibre calculation gives

\[
\sum_{n\le X}\frac{b_\diamond(n)^2}{g_\diamond(n)n}
 \le\frac{4149}{1666}(1+\log X),
\]

and

\[
\sum_{n\le X}\frac{g_\diamond(n)}n
 \le\frac{16}{3}(1+\log X).
\]

## 3. Scalar boundary

For the unique scalar `R_X=5c_X(2)+3c_X(3)`, with `z=s+1/2`,

\[
\int_1^\infty R_X X^{-s-1}\,dX
 =\frac{6[1-B_\diamond(z)]}{s^2}.
\]

At the coefficient level,

\[
a_*=6(\delta_1-b_\diamond).
\]

Hence

\[
M_*(N)=\sum_{n\le N}\frac{a_*(n)}{\sqrt n}
      =6\left[1-\mathcal B_\diamond(N)\right],
\]

where

\[
\mathcal B_\diamond(N)=\sum_{n\le N}\frac{b_\diamond(n)}{\sqrt n}.
\]

Also

\[
R_{N+1}-R_N=M_*(N)\log(1+1/N).
\]

These identities reconstruct the complete interface from the boundary functional to the real-`X` scalar consumer.

## 4. Scope correction

Let

\[
H(s)=\frac{6[1-B_\diamond(s+1/2)]}{s}
     =\int_0^\infty M_*(\lfloor e^t\rfloor)e^{-st}\,dt.
\]

Bernstein uniqueness gives

\[
H\text{ completely monotone}
\iff M_*(N)\ge0\text{ for every }N.
\]

This is the **all-scale** form of RJTE. Eventual RJTE is weaker. If `T=log N_0`, it is equivalent to complete monotonicity only after subtracting the compact initial transform

\[
E_T(s)=\int_0^T M_*(\lfloor e^t\rfloor)e^{-st}\,dt.
\]

Thus the unqualified sentence “eventual RJTE is complete monotonicity of `H`” is false. The corrected statement is

\[
\boxed{
\text{eventual RJTE}
\iff H-E_T\text{ is completely monotone for some finite }T.
}
\]
