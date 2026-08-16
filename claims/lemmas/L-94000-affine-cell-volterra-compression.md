# L-94000 — Every complete positive Volterra cell has an exact two-node finite compression

Claim ID: `L-94000`  
Status: **PROVED EXACT**  
Date: 2026-08-16  
Depends on: the verified formula for `g_s` and positivity of `p_s=R g_s`

## 1. Affine cell geometry

Fix an integer `n>=1` and let `n<=s<n+1`. Since the active seed support is constant on this half-open cell,

\[
g_s=a_n-s^{-1/2}b_n,
\]

where

\[
a_n(m)=\sqrt m\,\mathbf1_{m\le n},
\qquad
b_n(m)=m\,\mathbf1_{m\le n}.
\]

For the finite linear component-row map `R`, put

\[
A_n=\mathcal Ra_n,
\qquad B_n=\mathcal Rb_n.
\]

Then

\[
\boxed{p_s=A_n-s^{-1/2}B_n.}
\]

Thus the complete row family on one endpoint cell is affine in the single scalar coordinate `u=s^(-1/2)`.

## 2. Exact positive compression

Let `I=[a,b]` be any subinterval of `[n,n+1]`, and let `w(s)>=0` be integrable and not identically zero. Define

\[
M_I=\int_Iw(s)\,ds,
\qquad
\bar u_I=M_I^{-1}\int_Iw(s)s^{-1/2}\,ds.
\]

Because `s^(-1/2)` is monotone,

\[
b^{-1/2}\le\bar u_I\le a^{-1/2}.
\]

Set

\[
\theta_I=
\frac{\bar u_I-b^{-1/2}}{a^{-1/2}-b^{-1/2}}
\in[0,1].
\]

Using the one-sided endpoint values of the affine row gives

\[
\boxed{
\int_Iw(s)p_s\,ds
=M_I\left[\theta_Ip_a+(1-\theta_I)p_{b-}\right].
}
\]

Both endpoint rows are nonnegative, so the integral is represented by two actual nonnegative finite rows with nonnegative coefficients. No approximate quadrature, mesh limit, B-spline collar, or compactness argument occurs.

## 3. Volterra specialization

On a factor-67 outer cell use

\[
w_X(s)=\frac{2L(X/s)}s.
\]

The frozen directed bound

\[
L(x)>159/500\qquad(1\le x<67)
\]

makes this a strictly positive weight. Consequently every complete outer cell of the Volterra source has an exact two-node finite realization. Summing the finitely many cells produces a coefficientwise nonnegative finite row and preserves every linear observation, including ordinary columns at `q` and `4q`, radix-four detail, entropy, and all declared component rows.
