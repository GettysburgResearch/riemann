# L-105445 — The Xi source anchor pays the differential microscope at every scale

Claim ID: `L-105445`  
Status: **PROVED UNCONDITIONALLY FROM THE POSITIVE XI FOURIER KERNEL**  
Created: 2026-08-24  
Depends on: `L-105418`, `L-105444`  
RH status: **not assumed**

## 1. Statement

For every derivative order `r>=0` and every `h>0`,

\[
\boxed{
\mathcal C_{r,0}(0,h)
={1\over2}
\left[
 h\Re m_r'(ih)-\Im m_r(ih)
\right]
<0,
}
\tag{L-105445.1}

where

\[
m_r={\Xi^{(r)}\over\Xi^{(r+1)}}.
\]

Equivalently,

\[
\boxed{
{1\over h}\Im {\Xi^{(r)}(ih)\over\Xi^{(r+1)}(ih)}
}
\tag{L-105445.2}

is strictly decreasing on `(0,infinity)`.

Consequently the minimal two-height field also satisfies

\[
\boxed{
\mathcal Q_r(0,h)<0
\qquad(h>0).
}
\tag{L-105445.3}

This pays one complete centre line of the RH-equivalent microscope at every
physical scale.

## 2. Even derivative orders

Let `r=2ell`. Up to a common nonzero real sign, put

\[
A_r(h)
=\int_0^\infty u^r\Phi(u)\cosh(hu)\,du>0.
\]

Then

\[
A_r'(h)
=\int_0^\infty u^{r+1}\Phi(u)\sinh(hu)\,du>0
\]

and `L-105418` gives

\[
\Im m_r(ih)={A_r(h)\over A_r'(h)}.
\tag{L-105445.4}

Write

\[
A_r(h)=P_r(h^2),
\qquad
P_r(x)=\sum_{n\ge0}a_nx^n,
\qquad
 a_n={M_{r+2n}\over(2n)!}>0.
\tag{L-105445.5}

The reciprocal normalized phase is

\[
{hA_r'(h)\over A_r(h)}
=2{xP_r'(x)\over P_r(x)}.
\tag{L-105445.6}

Define a probability law on the nonnegative integers by

\[
\mathbb P_x(N=n)={a_nx^n\over P_r(x)}.
\]

Then

\[
{xP_r'(x)\over P_r(x)}=\mathbb E_xN
\]

and

\[
\boxed{
{x\,d\over dx}
{xP_r'(x)\over P_r(x)}
=\operatorname{Var}_x(N)>0.
}
\tag{L-105445.7}

The variance is strict because the Xi kernel has infinitely many positive
moments. Therefore `h A_r'/A_r` is strictly increasing. Its reciprocal

\[
{A_r(h)\over hA_r'(h)}
={1\over h}\Im m_r(ih)
\]

is strictly decreasing, proving (L-105445.1) in even parity.

## 3. Odd derivative orders

Let `r=2ell+1`. Up to a common nonzero real sign, put

\[
S_r(h)
=\int_0^\infty u^r\Phi(u)\sinh(hu)\,du>0.
\]

Then

\[
S_r'(h)
=\int_0^\infty u^{r+1}\Phi(u)\cosh(hu)\,du>0
\]

and

\[
\Im m_r(ih)={S_r(h)\over S_r'(h)}.
\tag{L-105445.8}

Now

\[
S_r(h)=hQ_r(h^2),
\qquad
Q_r(x)=\sum_{n\ge0}b_nx^n,
\qquad
b_n={M_{r+2n+1}\over(2n+1)!}>0.
\tag{L-105445.9}

Hence

\[
{hS_r'(h)\over S_r(h)}
=1+2{xQ_r'(x)\over Q_r(x)}.
\tag{L-105445.10}

With the analogous probability weights `b_nx^n/Q_r(x)`, logarithmic
differentiation gives

\[
\boxed{
{x\,d\over dx}
{xQ_r'(x)\over Q_r(x)}
=\operatorname{Var}_x(N)>0.
}
\tag{L-105445.11}

Therefore `h S_r'/S_r` is strictly increasing and

\[
{S_r(h)\over hS_r'(h)}
={1\over h}\Im m_r(ih)
\]

is strictly decreasing. This proves odd parity.

## 4. Two-height consequence

Put

\[
v_r(h)={1\over h}\Im m_r(ih).
\]

The minimal field is

\[
\boxed{
\mathcal Q_r(0,h)
={4h\over3}[v_r(2h)-v_r(h)].
}
\tag{L-105445.12}

Strict decrease of `v_r` proves (L-105445.3).

## 5. Interpretation

The source-owned anchor is stronger than the previously known sign

\[
\Im m_r(ih)>0.
\]

It pays the complete differential and dyadic Pick-curvature conditions at all
scales. Therefore any first microscope failure must occur away from the anchor
`a=0`.

The proof is a pure positive-source argument: the derivative of the
power-series elasticity is exactly a variance of the Fourier-moment index.
No saddle approximation, critical-point information or RH input is used.

## 6. Scope

The theorem does not control `a!=0`, where oscillatory Fourier phases destroy
the positive coefficient law. It does not prove the global microscope gate or
RH.
