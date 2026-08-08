# L-27501 — Shell-profile size and the RH prime-sampling bound

Claim ID: `L-27501`  
Title: Under RH, the weighted parabolic shell-tail sampling remainder is polylogarithmic uniformly in the tail endpoint  
Status: **PROPOSED COMPLETE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen base: PR #240 at `58c70a81dce76cd84ea50a60c15c227537f240c1`  
Dependencies: `L-23823`, `L-23825`; the classical RH estimate for the Chebyshev function  
Scope: the reverse implication `RH => WSTS`; no unconditional estimate is asserted

## 1. Purpose

`T-23811` proves that Weighted Shell-Tail Stability (`WSTS`) implies the
critical prime-ramp lower bound and hence RH.  This lemma proves the converse.
The consequence is important for status and review:

> `WSTS` is not a small auxiliary lemma left after the carry geometry.  It is an
> exact RH-equivalent arithmetic theorem.

The proof also supplies the profile estimates needed to audit the Stieltjes
remainder in `L-23825`.

## 2. Exact parabolic cell formula

Retain

\[
E(\theta)
=F(\theta)-\theta^{-1/2}\log(1/\theta),
\qquad 0<\theta\le1,
\tag{L-27501.1}
\]

where, on

\[
\frac1{N+1}<\theta\le\frac1N,
\]

\[
F(\theta)
=\theta^{-1/2}
 [A_N+S_N(\log\theta+4)]-4N,
\tag{L-27501.2}
\]

with

\[
S_N=\sum_{k=1}^Nk^{-1/2},
\qquad
A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\]

Therefore

\[
\boxed{
E(\theta)
=\theta^{-1/2}
 [A_N+(S_N+1)\log\theta+4S_N]-4N.}
\tag{L-27501.3}
\]

The entering summand at a reciprocal knot has value `g(1)=0`; hence `E` is
continuous and piecewise continuously differentiable.

## 3. Two elementary sum–integral estimates

Monotone integral comparison for `x^(-1/2)` gives

\[
\boxed{S_N=2\sqrt N+O(1).}
\tag{L-27501.4}
\]

For

\[
f(x)=x^{-1/2}\log x,
\]

the integral of `|f'|` on `[1,infinity)` is finite.  Comparing each unit
interval with its left endpoint therefore gives

\[
\begin{aligned}
A_N
&=\int_1^Nx^{-1/2}\log x\,dx+O(1)\\
&=2\sqrt N\log N-4\sqrt N+O(1).
\end{aligned}
\tag{L-27501.5}
\]

All implied constants in this claim are absolute.

Put

\[
x=\theta^{-1},
\qquad N\le x<N+1.
\]

Then

\[
\log x=\log N+O(N^{-1}),
\qquad
\sqrt x=\sqrt N+O(N^{-1/2}).
\tag{L-27501.6}
\]

Substituting (L-27501.4)--(L-27501.6) into the bracket in (L-27501.3) gives

\[
A_N-(S_N+1)\log x+4S_N
=4\sqrt N+O(1+\log N).
\tag{L-27501.7}
\]

The leading term cancels `4N` after multiplication by `sqrt(x)`.  Hence

\[
\boxed{
|E(\theta)|
\le C\theta^{-1/2}
 [1+\log(1/\theta)]
\qquad(0<\theta\le1).}
\tag{L-27501.8}
\]

The finitely many values in the first cell are absorbed by enlarging `C`.

## 4. Piecewise variation bound

Inside one reciprocal cell, differentiation of (L-27501.3) gives

\[
E'(\theta)
=\theta^{-3/2}
\left[
(S_N+1)
-\frac12\{A_N+(S_N+1)\log\theta+4S_N\}
\right].
\tag{L-27501.9}
\]

Equation (L-27501.7) and (L-27501.4) make the two `2 sqrt(N)` terms cancel.
Thus

\[
\boxed{
|E'(\theta)|
\le C\theta^{-3/2}
 [1+\log(1/\theta)]}
\tag{L-27501.10}
\]

on every open cell.  Since `E` is continuous at the reciprocal knots, this is
also a bounded-variation density estimate on every compact subinterval of
`(0,1]`; no knot atoms occur.

## 5. Uniform shell bounds

Let

\[
E_c(\theta)
=E(\theta)
-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.
\tag{L-27501.11}
\]

For the dyadic finite shell in `T-23811`,

\[
c=\frac{\lfloor X/2\rfloor}{X}.
\]

For every `X>=3`, this lies in `[1/3,1/2]`.  The scale factors in
(L-27501.11) cancel the scale factors in (L-27501.8)--(L-27501.10).  Therefore,
uniformly for `1/3<=c<=1/2`,

\[
\boxed{
|E_c(\theta)|
\le C\theta^{-1/2}[1+\log(1/\theta)],}
\tag{L-27501.12}
\]

and, away from the finite cell boundaries,

\[
\boxed{
|E_c'(\theta)|
\le C\theta^{-3/2}[1+\log(1/\theta)].}
\tag{L-27501.13}
\]

The shell is continuous at `theta=c` because `E(1)=0`.

## 6. Classical RH input

Assume RH.  The classical von Koch estimate, together with the elementary
prime-power removal from `psi` to `vartheta`, gives

\[
\boxed{
R(t):=\vartheta(t)-t
=O\left(t^{1/2}\log^2(2t)\right)
\qquad(t\ge2).}
\tag{L-27501.14}
\]

No stronger zero-density, pair-correlation, simplicity, or prime-gap input is
used.

Let

\[
Y=\lfloor X/2\rfloor,
\qquad c=Y/X,
\]

and retain the exact sampling remainder of `L-23825`:

\[
\mathcal E_{X,Y}(z)
=X^{-1/2}
\int_{[z,X]}E_c(t/X)\,dR(t),
\qquad 2\le z\le X.
\tag{L-27501.15}
\]

## 7. Stieltjes integration by parts

The function `E_c` is continuous and piecewise absolutely continuous.  Since
`E_c(1)=0`, Stieltjes integration by parts gives

\[
\begin{aligned}
\mathcal E_{X,Y}(z)
={}&-X^{-1/2}E_c(z/X)R(z^-)\\
&-X^{-3/2}
\int_z^XR(t)E_c'(t/X)\,dt,
\end{aligned}
\tag{L-27501.16}
\]

with the usual harmless endpoint convention when `z` is prime.

By (L-27501.12) and (L-27501.14), the boundary term is

\[
\ll
[1+\log(X/z)]\log^2(2z)
\ll\log^3(2X).
\tag{L-27501.17}
\]

For the integral term, (L-27501.13)--(L-27501.14) give

\[
\begin{aligned}
&X^{-3/2}
\int_z^X|R(t)|\,|E_c'(t/X)|dt\\
&\qquad\ll
\int_z^X
\frac{\log^2(2t)\,[1+\log(X/t)]}{t}\,dt\\
&\qquad\ll \log^4(2X).
\end{aligned}
\tag{L-27501.18}
\]

uniformly in `z`.  Consequently

\[
\boxed{
\sup_{2\le z\le X}
|\mathcal E_{X,\lfloor X/2\rfloor}(z)|
\ll\log^4(2X).}
\tag{L-27501.19}
\]

## 8. RH implies WSTS

`L-23825` decomposes every weighted finite shell tail into

```text
nonpositive continuum shell moat
+ the sampling remainder mathcal E
+ an absolutely summable carry-floor error.
```

The floor error is `O(log^2(2X))` uniformly in the tail endpoint.  Therefore
(L-27501.19) gives

\[
\boxed{
\mathcal B_X
\ll\log^4(2X),}
\tag{L-27501.20}
\]

where `mathcal B_X` is the maximum positive dyadic weighted shell-tail charge in
`T-23811`.

In particular, for every `epsilon>0`,

\[
\mathcal B_X=O_\epsilon(X^\epsilon).
\]

This is exactly `WSTS`.

## 9. Proof boundary

Closed in this lemma, subject to independent review:

1. sharp enough size and variation bounds for the parabolic defect;
2. uniformity for the finite dyadic ratio `floor(X/2)/X`;
3. Stieltjes integration by parts with every endpoint retained;
4. the uniform `O(log^4 X)` sampling bound under RH;
5. `RH => WSTS`.

Imported classical input:

- `RH => vartheta(t)-t=O(sqrt(t) log^2 t)`.

Not proved:

- `WSTS` unconditionally;
- RH.