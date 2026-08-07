# L-23401 — Fixed-ratio Mertens shells are compact zero-safe inverse-zeta signals

Claim ID: `L-23401`  
Title: One multiplicative Mertens increment has an exact compact Laplace window, no open-strip transform zeros, and a finite positive balanced Gram on every block  
Status: **PROPOSED — COMPLETE EXACT TRANSFORM AND FINITE-GRAM ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: elementary Mellin summation; `L-23003/T-23002` for the special ratio `c=2/3`  
Scope: every fixed real `0<c<1`

## 1. The fixed-ratio shell

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad M(x)=0\quad(0<x<1),
\]

and fix

\[
0<c<1,
\qquad L=\log(1/c)>0.
\]

Define

\[
\boxed{
I_c(x)=M(x)-M(cx)
      =\sum_{cx<n\le x}\mu(n).}
\tag{L-23401.1}
\]

On logarithmic scale put

\[
\boxed{
Q_c(t)=e^{-t/2}I_c(e^t),
\qquad t\ge0.}
\tag{L-23401.2}
\]

Finally define the compact window

\[
\boxed{
H_c(u)=e^{-u/2}{\bf1}_{[0,L)}(u).}
\tag{L-23401.3}
\]

Then, pointwise away from harmless endpoint conventions and in `L2_loc`,

\[
\boxed{
Q_c(t)=\sum_{n\ge1}{\mu(n)\over\sqrt n}
       H_c(t-\log n).}
\tag{L-23401.4}
\]

Indeed, one summand is active exactly when

\[
0\le t-\log n<L
\iff ce^t<n\le e^t,
\]

and its active value is

\[
{\mu(n)\over\sqrt n}e^{-(t-\log n)/2}
=\mu(n)e^{-t/2}.
\]

Thus the first critical Farey cell of `L-23003`, for `c=2/3`, is the distinguished point value

\[
Q_{2/3}(\log D)
=D^{-1/2}\bigl[M(D)-M(2D/3)\bigr].
\tag{L-23401.5}
\]

## 2. Exact Mellin/Laplace transform

For `Re(s)>1`, termwise integration gives

\[
\begin{aligned}
\int_1^\infty I_c(x)x^{-s-1}dx
&=\sum_{n\ge1}\mu(n)
  \int_n^{n/c}x^{-s-1}dx\\
&={1-c^s\over s}\sum_{n\ge1}{\mu(n)\over n^s}.
\end{aligned}
\]

Hence

\[
\boxed{
\int_1^\infty I_c(x)x^{-s-1}dx
={1-c^s\over s\zeta(s)}.}
\tag{L-23401.6}
\]

Equivalently, with `s=z+1/2`,

\[
\boxed{
\int_0^\infty Q_c(t)e^{-zt}dt
={1-c^{z+1/2}\over
 (z+1/2)\zeta(z+1/2)},
\qquad \Re z>{1\over2}.}
\tag{L-23401.7}
\]

The window transform is therefore

\[
\boxed{
\widehat H_c(z)
={1-c^{z+1/2}\over z+1/2}.}
\tag{L-23401.8}
\]

The apparent singularity at `z=-1/2` is removable.

## 3. Zero-safe property

If

\[
c^s=1,
\]

then taking absolute values gives

\[
c^{\Re s}=1.
\]

Because `0<c<1`, this forces

\[
\Re s=0.
\]

Consequently

\[
\boxed{
1-c^s\ne0\qquad(\Re s>0).}
\tag{L-23401.9}
\]

In particular, at every hypothetical zeta zero `rho` satisfying

\[
\Re\rho>\frac12,
\]

the numerator in (L-23401.6) is nonzero. The fixed shell window cannot cancel an off-line zero.

This is a simpler source-specific zero-safe multiplier than the completed prime windows: the inverse-zeta signal has no zeta pole to remove.

## 4. Exact finite block Gram

Fix a block length `B>0` and define

\[
\boxed{
E_{c,B}(J)=\int_J^{J+B}|Q_c(t)|^2dt.}
\tag{L-23401.10}
\]

Only integers in

\[
e^{J-L}<n\le e^{J+B}
\]

occur. For two positive integers `m,n`, put

\[
a_{J}(m,n)=\max\{J,\log m,\log n\},
\]

\[
b_{J,B}(m,n)=
\min\{J+B,\log m+L,\log n+L\}.
\]

Define

\[
\boxed{
K_{c,B,J}(m,n)=
\begin{cases}
 e^{-a_J(m,n)}-e^{-b_{J,B}(m,n)},&a_J(m,n)<b_{J,B}(m,n),\\
 0,&a_J(m,n)\ge b_{J,B}(m,n).
\end{cases}}
\tag{L-23401.11}
\]

Expanding (L-23401.10), the factors `m^{-1/2}`, `n^{-1/2}` cancel the two exponential window numerators, giving the exact finite identity

\[
\boxed{
E_{c,B}(J)
=\sum_{m,n}\mu(m)\mu(n)K_{c,B,J}(m,n).}
\tag{L-23401.12}
\]

No prime, divisor, or endpoint term is omitted.

The kernel is positive semidefinite because

\[
K_{c,B,J}(m,n)
=\int_J^{J+B}
 e^{-t}
 {\bf1}_{\{ce^t<m\le e^t\}}
 {\bf1}_{\{ce^t<n\le e^t\}}dt.
\tag{L-23401.13}
\]

Thus it is the Gram kernel of the real functions

\[
t\longmapsto
 e^{-t/2}{\bf1}_{\{ce^t<n\le e^t\}}.
\]

## 5. Balanced factor-ratio geometry

If

\[
K_{c,B,J}(m,n)>0,
\]

then there is a common `t` such that both `m` and `n` lie in `(ce^t,e^t]`. Therefore

\[
\boxed{
c<{m\over n}<c^{-1}}
\tag{L-23401.14}
\]

up to boundary conventions. The exact first-cell energy is consequently one compact balanced Möbius Type-II Gram, not a generic Farey operator norm.

Writing

\[
X=e^J,
\qquad u={m\over X},
\qquad v={n\over X},
\]

one has the homogeneous kernel

\[
\boxed{
K_{c,B,J}(m,n)
={1\over X}
\left[
 {1\over\max(1,u,v)}
 -{1\over\min(e^B,u/c,v/c)}
\right]_+,}
\tag{L-23401.15}
\]

where the positive part includes the condition that the second denominator exceed the first in logarithmic order.

## 6. Full-line autocorrelation control

For finite coefficient support, integrating over the complete real line gives the translation-invariant autocorrelation

\[
R_c(v)=\int_{\mathbb R}H_c(u)H_c(u+v)du.
\]

For `0\le v\le L`,

\[
\boxed{
R_c(v)=e^{-v/2}-ce^{v/2},}
\tag{L-23401.16}
\]

and `R_c(v)=0` for `v>L`, with even extension. Hence the complete-line arithmetic kernel is

\[
\boxed{
{1\over\sqrt{mn}}R_c(|\log(m/n)|)
=
\left[
 {1\over\max(m,n)}
 -{c\over\min(m,n)}
\right]_+.}
\tag{L-23401.17}
\]

This is an exact Brownian/Green-type multiplicative kernel. The critical difficulty is not kernel positivity; it is the source-specific upper bound for its moving local blocks.

## 7. Proof boundary

Closed exactly in this lemma:

- the fixed-ratio shell representation;
- the Mellin and Laplace transforms;
- absence of multiplier zeros in `Re(s)>0`;
- the finite positive block Gram;
- compact balanced factor-ratio support;
- the full-line autocorrelation formula.

Not closed here:

- a subexponential upper bound for `E_(c,B)(J)`;
- the balanced Möbius correlation estimate;
- RH.
