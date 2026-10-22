# L-90004 — Exact prime-seed Mellin symbol and the prime-square pole

Claim ID: `L-90004` (provisional range; allocate before integration)  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: the definitions of `T-90001`; elementary Mellin integration; the Euler product and Möbius inversion for the prime zeta derivative  
Scope: exact transform and pole audit for the undifferenced prime endpoint scalar; no sign theorem and no RH claim

## 1. The endpoint scalar

For real `X>=1`, retain the zero-extended parabolic seed

\[
b_X(m)=2\sqrt m\left(\log\frac Xm-2\left(1-\sqrt{m/X}\right)\right)
\mathbf 1_{m\le X},
\]

\[
v_p(X)=\sum_{k\ge1}\bigl(b_X(kp)-b_X(kp+1)\bigr),
\]

and

\[
w_X(p)=p^{-1/2}\log(X/p)\mathbf 1_{p\le X}.
\]

Define

\[
J_{\mathbb P}(X)=\sum_p(\log p)v_p(X),
\qquad
P_{\mathbb P}(X)=\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp,
\]

and

\[
\boxed{A(X)=J_{\mathbb P}(X)-P_{\mathbb P}(X).}
\tag{L-90004.1}
\]

At integer endpoints this is exactly the undifferenced scalar `A_X` of
`T-90001/L-90006`.

## 2. Exact radical switching

Write

\[
\operatorname{rad}(n)=\prod_{p\mid n}p,
\qquad \operatorname{rad}(1)=1.
\]

Finite switching gives

\[
\begin{aligned}
J_{\mathbb P}(X)
&=\sum_{m\le X}b_X(m)\sum_{p\mid m}\log p
 -\sum_{m\le X}b_X(m)\sum_{p\mid m-1}\log p\\
&=\boxed{
\sum_{m=2}^{\lfloor X\rfloor}b_X(m)
\bigl(\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1)\bigr).}
\end{aligned}
\tag{L-90004.2}
\]

This identity is useful computationally, but the prime-by-prime form exposes the
analytic continuation more directly.

## 3. Mellin transform of one seed value

For `Re z>0`, direct integration gives

\[
\begin{aligned}
\int_1^\infty b_X(n)X^{-z-1}\,dX
&=2n^{1/2-z}
\int_1^\infty
\bigl(\log x-2+2x^{-1/2}\bigr)x^{-z-1}\,dx\\
&=n^{1/2-z}
\left(\frac2{z^2}-\frac4z+\frac4{z+1/2}\right)\\
&=\boxed{\frac{n^{1/2-z}}{z^2(z+1/2)}.}
\end{aligned}
\tag{L-90004.3}
\]

Put

\[
s=z+\frac12,
\qquad w=s-1=z-\frac12,
\]

and define

\[
\mathcal P_1(s)=\sum_p\frac{\log p}{p^s},
\tag{L-90004.4}
\]

\[
\mathcal D(w)=
\sum_p(\log p)
\sum_{k\ge1}\bigl((kp)^{-w}-(kp+1)^{-w}\bigr).
\tag{L-90004.5}
\]

Both initial series converge absolutely in the half-plane needed below.  Fubini
and (L-90004.3) yield, initially for `Re z>1/2`,

\[
\boxed{
\widehat J_{\mathbb P}(z)
:=\int_1^\infty J_{\mathbb P}(X)X^{-z-1}\,dX
=\frac{\mathcal D(s-1)}{s z^2}.}
\tag{L-90004.6}
\]

Likewise

\[
\boxed{
\widehat P_{\mathbb P}(z)
=\frac{\mathcal P_1(s)}{z^2}.}
\tag{L-90004.7}
\]

Consequently

\[
\boxed{
\widehat A(z)
=\frac{\mathcal G(s)}{z^2},
\qquad
\mathcal G(s)=\frac{\mathcal D(s-1)}s-\mathcal P_1(s).}
\tag{L-90004.8}
\]

This is the exact prime-only endpoint symbol.  No continuum approximation or
prime-number theorem has entered.

## 4. Continuation of the shifted-difference series

For `Re w>0`, expand the second term in (L-90004.5):

\[
1-(1+(kp)^{-1})^{-w}
=\sum_{r\ge1}(-1)^{r+1}\frac{(w)_r}{r!}(kp)^{-r}.
\]

Since `p>=2`, the expansion is uniformly summable, and

\[
\boxed{
\mathcal D(w)
=\sum_{r\ge1}(-1)^{r+1}\frac{(w)_r}{r!}
\zeta(w+r)\mathcal P_1(w+r).}
\tag{L-90004.9}
\]

Separate the first term:

\[
\boxed{
\mathcal D(w)
=w\zeta(w+1)\mathcal P_1(w+1)+\mathcal H(w),}
\tag{L-90004.10}
\]

where the `r>=2` series `mathcal H` is holomorphic for `Re w>-1`.
Indeed, its first prime argument is `w+2`, and the remaining series converges
exponentially in `r`.

For `Re s>1`, the Euler product gives

\[
-\frac{\zeta'}{\zeta}(s)
=\sum_{m\ge1}\mathcal P_1(ms).
\]

Möbius inversion therefore gives

\[
\boxed{
\mathcal P_1(s)
=\sum_{m\ge1}\mu(m)
\left(-\frac{\zeta'}{\zeta}(ms)\right).}
\tag{L-90004.11}
\]

The right side supplies the meromorphic continuation needed here.  In every
half-plane `Re s>=1/2+delta`, the tail `m>=2` converges normally.  At the
boundary point `s=1/2`, only the `m=2` copy of the pole of zeta is singular, and

\[
\boxed{
\mathcal P_1\left(\frac12+z\right)
=-\frac1{2z}+O(1).}
\tag{L-90004.12}
\]

## 5. The prime-square pole at `z=0`

Put `z=s-1/2`.  By (L-90004.10)--(L-90004.12),

\[
\mathcal D\left(-\frac12+z\right)
=\frac{\zeta(1/2)}{4z}+O(1).
\tag{L-90004.13}
\]

Dividing by `s=1/2+z` and subtracting (L-90004.12) gives

\[
\boxed{
\mathcal G\left(\frac12+z\right)
=\frac{1+\zeta(1/2)}{2z}+O(1).}
\tag{L-90004.14}
\]

Hence

\[
\boxed{
\widehat A(z)
=\frac{1+\zeta(1/2)}{2z^3}+O(z^{-2}).}
\tag{L-90004.15}
\]

The third-order pole is not a zeta-zero contribution.  It is the prime-square
singularity of the prime-only Euler series.  In the physical variable it creates
the deterministic term

\[
\boxed{
\frac{1+\zeta(1/2)}4\log^2X.}
\tag{L-90004.16}
\]

Since `zeta(1/2)<-1`, this quadratic logarithmic drift is negative.

## 6. Pole at `s=1` cancels; every nontrivial zero survives

At `s=1`, or `z=1/2`, one has

\[
(s-1)\zeta(s)\longrightarrow1,
\qquad \mathcal H(s-1)=O(s-1).
\]

Thus `mathcal D(s-1)/s` and `mathcal P_1(s)` have the same residue.  Their
difference `mathcal G(s)` is regular:

\[
\boxed{z=1/2\text{ is not a pole of }\widehat A.}
\tag{L-90004.17}
\]

Let `rho` be a nontrivial zeta zero of multiplicity `m_rho`, and put

\[
z_\rho=\rho-\frac12.
\]

The `m=1` term in (L-90004.11) gives residue `-m_rho` to `mathcal P_1`.
The product `zeta(s)mathcal P_1(s)` in (L-90004.10) is regular at `rho`, even
when the zero is multiple. Therefore

\[
\boxed{
\operatorname*{Res}_{z=z_\rho}\widehat A(z)
=\frac{m_\rho}{z_\rho^2}\ne0.}
\tag{L-90004.18}
\]

The endpoint scalar retains every off-line zero with exactly the same
`1/(rho-1/2)^2` smoothing as the resident prime-ramp consumer.  No reciprocal
zeta numerator or dyadic blind spot appears.

## 7. Dyadic shell transform

Define the exact real-ratio shell

\[
\mathscr T(X)=A(X)-A(X/2).
\tag{L-90004.19}
\]

Scaling in the Mellin integral gives

\[
\boxed{
\widehat{\mathscr T}(z)
=(1-2^{-z})\widehat A(z)
=\frac{1-2^{-z}}{z^2}\mathcal G\left(z+\frac12\right).}
\tag{L-90004.20}
\]

At the origin, (L-90004.14) gives

\[
\boxed{
\widehat{\mathscr T}(z)
=\frac{(1+\zeta(1/2))\log2}{2z^2}+O(z^{-1}).}
\tag{L-90004.21}
\]

Thus the dyadic shell has the deterministic logarithmic drift

\[
\boxed{
\kappa\log X,
\qquad
\kappa=\frac{(1+\zeta(1/2))\log2}{2}
=-0.1595467149\ldots .}
\tag{L-90004.22}
\]

At a nontrivial zero the residue is

\[
\boxed{
\operatorname*{Res}_{z=z_\rho}\widehat{\mathscr T}(z)
=\frac{m_\rho(1-2^{-z_\rho})}{z_\rho^2}.}
\tag{L-90004.23}
\]

The finite factor vanishes only on the imaginary dyadic lattice, but the zero
is irrelevant to the converse because the undifferenced transform
(L-90004.18) remains available.  Under RH, (L-90004.23) is absolutely summable
because

\[
\sum_\rho\frac{m_\rho}{1+|\Im\rho|^2}<\infty.
\]

## 8. Real-endpoint interpolation

The function `A(X)` is continuous at integer endpoints.  Moreover

\[
A(X)-A(\lfloor X\rfloor)
\ll\frac{\log(2X)}{\sqrt X}.
\tag{L-90004.24}
\]

For the ramp term this is `L-90006.20--21`.  For the seed term, use
(L-90004.2), differentiate `b_X(m)` in `X`, and sum by parts against
`log rad(m)`: the endpoint derivative vanishes at `m=X`, while

\[
\partial_X b_X(m)=\frac{2\sqrt m}{X}-\frac{2m}{X^{3/2}}
\]

has first difference

\[
\ll \frac1{X\sqrt m}+\frac1{X^{3/2}}.
\]

Since `log rad(m)<=log m`, summation gives the displayed bound. Therefore
replacing `X/2` by `floor(X/2)` changes the dyadic shell by `o(1)`.

## 9. Proof boundary

Closed exactly, subject to review:

1. radical switching for the prime seed;
2. the one-cell Mellin kernel;
3. the exact symbol (L-90004.8);
4. continuation (L-90004.9)--(L-90004.12);
5. the prime-square Laurent coefficient at `z=0`;
6. cancellation of the real main pole;
7. survival and residue of every nontrivial zero;
8. the dyadic logarithmic drift coefficient;
9. integer/real endpoint compatibility.

Not proved here:

- any unconditional sign of `mathscr T`;
- RH;
- the contour-shift asymptotic, which is stated and proved separately in
  `T-90006`.
