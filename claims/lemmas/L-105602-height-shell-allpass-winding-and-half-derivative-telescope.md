# L-105602 — Height-shell all-pass winding has an exact half-derivative telescope

Claim ID: `L-105602`  
Status: **PROVED EXACT FOR REAL POLYNOMIALS AND FINITE REGULAR RECTANGLES; XI TRANSFER OPEN**  
Created: 2026-08-24  
Depends on: `L-105206`, `L-105281`, `L-105442`  
RH status: **not assumed**

## 1. One height counts one horizontal zero strip

Let `p` be a nonzero real polynomial and let `h>0` avoid all root heights.
Define the circle-valued all-pass function

\[
\boxed{
\Theta_{p,h}(x)
={p(x+ih)\over p(x-ih)},
\qquad x\in\mathbb R\cup\{\infty\}.
}
\tag{L-105602.1}
\]

The denominator is the complex conjugate of the numerator on the real axis,
so `|Theta|=1`, and `Theta(infinity)=1`.

A root `rho=alpha+i beta` contributes

\[
{x-\alpha+i(h-\beta)
 \over
 x-\alpha-i(h+\beta)}.
\]

Its phase changes by `-2pi` precisely when `|beta|<h`, and by zero otherwise.
Therefore

\[
\boxed{
\deg\Theta_{p,h}
=-N_p(h),
}
\tag{L-105602.2}
\]

where `N_p(h)` counts roots with `|Im rho|<h`, with multiplicity.

## 2. A height shell is one circle-valued quotient

For regular heights

\[
0<h_1<h_2,
\]
put

\[
\boxed{
\mathcal S_{p;h_1,h_2}
={\Theta_{p,h_2}\over\Theta_{p,h_1}}.
}
\tag{L-105602.3}
\]

Let

\[
M_p(h_1,h_2)
=\#\{\rho:h_1<|\operatorname{Im}\rho|<h_2\}
\]

with multiplicity. Then

\[
\boxed{
\deg\mathcal S_{p;h_1,h_2}
=-M_p(h_1,h_2).
}
\tag{L-105602.4}
\]

Because `p` is real, `M_p` is an even nonnegative integer.

## 3. Derivative-ladder telescope

Let

\[
p_k=p^{(k)},
\qquad
\mathcal S_k=\mathcal S_{p_k;h_1,h_2},
\]

and define the adjacent shell quotient

\[
\boxed{
\mathcal U_k
={\mathcal S_k\over\mathcal S_{k+1}}.
}
\tag{L-105602.5}
\]

Then

\[
\boxed{
\deg\mathcal U_k
=M_{p_{k+1}}(h_1,h_2)
-M_{p_k}(h_1,h_2).
}
\tag{L-105602.6}
\]

Consequently, for every finite terminal rung `R`,

\[
\boxed{
M_{p_0}(h_1,h_2)
=M_{p_R}(h_1,h_2)
-
\sum_{k=0}^{R-1}\deg\mathcal U_k.
}
\tag{L-105602.7}
\]

Every intermediate derivative cancels. This is the height-shell counterpart
of the derivative-ladder Levinson telescope `L-105206`.

## 4. Negative winding is paid by half a derivative

After Cayley compactification, write

\[
\mathcal U_k(e^{it})
=\sum_{n\in\mathbb Z}\widehat{\mathcal U_k}(n)e^{int}.
\]

For a circle-valued `H^(1/2)` map,

\[
\deg\mathcal U_k
=\sum_{n\in\mathbb Z}
 n|\widehat{\mathcal U_k}(n)|^2.
\tag{L-105602.8}
\]

Define its negative Hardy energy

\[
\mathcal E_-(\mathcal U_k)
=\sum_{n<0}|n|\,|\widehat{\mathcal U_k}(n)|^2.
\]

Then

\[
\boxed{
-\deg\mathcal U_k
\le\mathcal E_-(\mathcal U_k)
\le\|\mathcal U_k\|_{\dot H^{1/2}}^2.
}
\tag{L-105602.9}
\]

If the terminal derivative has no root in the shell, (L-105602.7) gives

\[
\boxed{
M_{p_0}(h_1,h_2)
\le
\sum_{k=0}^{R-1}
\mathcal E_-(\mathcal U_k).
}
\tag{L-105602.10}
\]

Since the left side is even,

\[
\boxed{
\sum_{k<R}\mathcal E_-(\mathcal U_k)<2
\quad\Longrightarrow\quad
M_{p_0}(h_1,h_2)=0.
}
\tag{L-105602.11}
\]

Thus one strict two-unit energy threshold removes the entire shell; no
pointwise critical-point selection is required.

## 5. Exact finite-rectangle ledger for entire functions

Let `F` be real entire and let the rectangle

\[
\Omega_{T,h}=\{z:|\Re z|<T,\ |\Im z|<h\}
\]

be regular. Put

\[
\Theta_{F,h}(x)={F(x+ih)\over F(x-ih)},
\qquad -T\le x\le T,
\]

and define the horizontal phase charge

\[
\mathsf W_F(T,h)
={1\over2\pi i}
\int_{-T}^{T}d\log\Theta_{F,h}(x).
\tag{L-105602.12}
\]

Let `mathsf V_F(T,h)` be the two vertical-side contribution to the argument
principle. With the standard counterclockwise orientation,

\[
\boxed{
N_F(T,h)
=-\mathsf W_F(T,h)+\mathsf V_F(T,h).
}
\tag{L-105602.13}
\]

For a shell, define

\[
\mathsf w_F
=\mathsf W_F(T,h_2)-\mathsf W_F(T,h_1),
\qquad
\mathsf v_F
=\mathsf V_F(T,h_2)-\mathsf V_F(T,h_1).
\]

Then exactly

\[
\boxed{
M_F(T;h_1,h_2)
=-\mathsf w_F+\mathsf v_F.
}
\tag{L-105602.14}
\]

For a derivative ladder, put

\[
\mathsf d_k=\mathsf w_{F_k}-\mathsf w_{F_{k+1}}.
\]

The complete finite-window telescope is

\[
\boxed{
M_{F_0}
=M_{F_R}
-
\sum_{k<R}\mathsf d_k
+
(\mathsf v_{F_0}-\mathsf v_{F_R}).
}
\tag{L-105602.15}
\]

All intermediate vertical-side charges cancel. The only analytic correction is
one low-end minus high-end shell boundary term.

If the compactified horizontal quotients are `H^(1/2)` and the endpoint
correction is controlled, then

\[
\boxed{
M_{F_0}
\le
M_{F_R}
+
\sum_{k<R}\mathcal E_-(\mathcal U_k)
+
(\mathsf v_{F_0}-\mathsf v_{F_R})_+.
}
\tag{L-105602.16}
\]

## 6. Xi conclusion interface

For the Xi ladder, take a positive-height shell

\[
0<h_1<h_2\le1/2.
\]

A terminal derivative supplied by the fixed-width saddle programme has no
zeros in a prescribed finite shell rectangle. Therefore the exact sufficient
condition for removing the shell at the base rung is

\[
\boxed{
\sum_{k<R}\mathcal E_-(\mathcal U_k)
+
(\mathsf v_{F_0}-\mathsf v_{F_R})_+
<2.
}
\tag{L-105602.17}
\]

This is the shell-energy gate `HSHE105602`. If it holds on a cofinal family of
rectangles for every rational shell, then every Xi zero is real.

The all-pass programme of PR #731 supplies the exact negative-winding payment
mechanism. What is not yet proved is the physical `H^(1/2)` transfer, including
near-real phase slips and the single surviving endpoint difference.

## 7. Scope

The polynomial theorem is exact. The finite-rectangle identities are exact.
No estimate for the Xi half-derivative energies or endpoint correction is
asserted. In particular, ordinary `L^2` control is insufficient: a narrow
Blaschke phase slip can have arbitrarily small `L^2` mass but one full winding
unit. RH remains unproved.
