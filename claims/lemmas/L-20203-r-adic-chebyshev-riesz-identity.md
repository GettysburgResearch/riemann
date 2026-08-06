# L-20203 — `r`-adic Chebyshev–Riesz identity

Claim ID: `L-20203`  
Title: The integer-dilation defect is an explicit two-scale Riesz mean whose adverse kernel is confined to the thin old-prime prefix  
Status: `PROPOSED — COMPLETE ELEMENTARY IDENTITY`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-20202`; Stieltjes integration by parts  
Scope: every fixed integer `r>=2`

## 1. Prime weight

Let

\[
 \psi(x)=\sum_{q\le x}\Lambda(q),
 \qquad
 E(x)=\psi(x)-x.
\]

Fix `r>=2`, put

\[
 a=n^{2/r},
 \qquad
 N=n^2,
\]

and define the continuous piecewise-logarithmic weight

\[
 w_{r,n}(x)=
 \begin{cases}
 (r^2-1)\log x-2(r-1)\log n,&1\le x\le a,\\[1mm]
 2\log n-\log x,&a<x\le N,\\
 0,&x>N.
 \end{cases}
 \tag{1}
\]

Continuity at `x=a` is immediate. The complete prime term of `L-20202` is

\[
 \boxed{
 P_r(n)=\int_{1^-}^{N}x^{-1/2}w_{r,n}(x)\,d\psi(x).}
 \tag{2}
\]

No prime power is omitted.

## 2. Exact error kernel

Put

\[
 f_{r,n}(x)=x^{-1/2}w_{r,n}(x).
\]

The endpoint at `N` vanishes, and `psi(1^-)=0`. Piecewise Stieltjes integration
by parts gives

\[
 P_r(n)
 =-\int_1^N\psi(x)f_{r,n}'(x)\,dx.
 \tag{3}
\]

There is no intermediate boundary term because `f_(r,n)` is continuous at `a`.
Define

\[
 K_{r,n}(x)=-f_{r,n}'(x).
\]

Then

\[
\boxed{
K_{r,n}(x)=x^{-3/2}
\begin{cases}
 {1\over2}\left[(r^2-1)\log x-2(r-1)\log n\right]-(r^2-1),
 &1\le x\le a,\\[1mm]
 1+\log n-{1\over2}\log x,
 &a<x\le N.
\end{cases}}
\tag{4}
\]

Splitting `psi=x+E` yields

\[
 P_r(n)=P_r^{\rm main}(n)+\int_1^N E(x)K_{r,n}(x)\,dx.
 \tag{5}
\]

## 3. Elementary main integral

For `u>=0`,

\[
 \int_1^{e^u}x^{-1/2}(u-\log x)\,dx
 =4e^{u/2}-4-2u.
 \tag{6}
\]

Therefore

\[
\boxed{
P_r^{\rm main}(n)
=4n-4r^2n^{1/r}+4(r^2-1)+4(r-1)\log n.}
\tag{7}
\]

Combining (7) with the polar, gamma, and Lerch terms of `L-20202` gives the
exact Riesz form

\[
\boxed{
\mathcal H_r(n)
=\mathcal A_r(n)
 +\int_1^{n^2}(\psi(x)-x)K_{r,n}(x)\,dx,}
\tag{8}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal A_r(n)={}&
4r^2n^{-1/r}-4n^{-1}-4(r^2-1)\\
&+(r-1)(4+\kappa)\log n
+\mathcal L_r(n),
\end{aligned}}
\tag{9}
\]

`kappa=psi(1/4)-log pi`, and the strictly positive Lerch term is

\[
 \mathcal L_r(n)
 ={1\over4}\sum_{k=0}^\infty
 {r^2(1-y_k)-(1-y_k^r)\over(k+1/4)^2},
 \qquad
 y_k=n^{-(4k+1)/r}.
 \tag{10}
\]

Equations (8)–(10) are exact.

## 4. The adverse Riesz support is thin

The outer kernel in (4) is strictly positive. In the lower range, its sign can
be negative only when

\[
 \log x<{2\over r+1}\log n+2.
\]

Thus

\[
\boxed{
K_{r,n}(x)\ge0
\quad\text{for}\quad
 e^2n^{2/(r+1)}\le x\le n^2.}
\tag{11}
\]

Every possible negative kernel value lies in

\[
\boxed{1\le x<e^2n^{2/(r+1)}.}
\tag{12}
\]

For fixed large `r`, almost the entire logarithmic interval up to the square
cutoff therefore carries a positive Riesz weight. The old adverse region is
explicit and has exponent tending to zero as `r` increases.

## 5. What a positive proof must estimate

Equation (8) separates the remaining arithmetic problem into:

1. the explicit threshold `A_r(n)`;
2. a short old-prefix integral over (12);
3. a positive-kernel Chebyshev-error average over the rest of `[1,n^2]`.

A successful proof cannot replace `E(x)` by an absolute PNT error: the order-`n`
main terms have already canceled and the remaining threshold is RH-scale.
The natural next identities are therefore correlation-sensitive:

- Selberg's symmetry formula for `Lambda*Lambda`;
- the prime-pair `H^2` energy of PR #216;
- the mass-quantile transport recurrence of PR #219.

The `r`-adic family supplies a tunable way to make the only negative kernel
support as short as desired before applying those identities.

## 6. Proof boundary

- The Stieltjes identity and every coefficient above are exact.
- Positivity of the kernel on the long outer range does not imply positivity of
  its integral against the sign-changing Chebyshev error.
- No one-sided Selberg or transport estimate at the required scale is proved.
- This lemma sharpens the full arithmetic target but does not establish RH.