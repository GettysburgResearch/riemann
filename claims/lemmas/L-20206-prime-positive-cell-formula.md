# L-20206 — Exact prime-positive compact-cell formula

Claim ID: `L-20206`  
Title: Below the first prime knot, the integer-dilation defect is a positive prime ramp plus a positive Lerch series against explicit polar/gamma charges  
Status: `PROPOSED — COMPLETE ALGEBRAIC CONSEQUENCE OF THE IMPORTED SCREW FORMULA`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20205`; `L-19801`  
Scope: `0<t<log 2`, integer `r>=2`

## 1. Exact finite formula

Let

\[
 \kappa=\psi(1/4)-\log\pi
 =-\gamma-\frac\pi2-\log(8\pi)<0.
\]

For `0<t<log 2`, the small-scale prime ramp in `Psi(t)` is empty. Direct
substitution into

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt)
\]

gives

\[
\boxed{
\begin{aligned}
\mathcal D_r(t)={}&
4\left[
 r^2(e^{t/2}+e^{-t/2}-2)
 -(e^{rt/2}+e^{-rt/2}-2)
\right]\\
&+{\kappa\over2}r(r-1)t\\
&+\sum_{q\le e^{rt}}{\Lambda(q)\over\sqrt q}
 (rt-\log q)\\
&+{1\over4}\sum_{k=0}^\infty
 {r^2(1-y_k)-(1-y_k^r)\over(k+1/4)^2},
\end{aligned}}
\tag{1}
\]

where

\[
 y_k=e^{-(2k+1/2)t}.
\]

Every prime power through `e^(rt)` is included exactly once.

## 2. Complete sign ledger

The prime term is nonnegative term by term:

\[
 rt-\log q\ge0.
\]

The Lerch term is strictly positive term by term because

\[
 r^2(1-y)-(1-y^r)
 \ge r(r-1)(1-y)>0
 \qquad(0<y<1).
\]

The polar term is nonpositive:

\[
\begin{aligned}
&4\left[
 r^2(e^{t/2}+e^{-t/2}-2)
 -(e^{rt/2}+e^{-rt/2}-2)
\right]\\
&\qquad=16\left[r^2\sinh^2(t/4)-\sinh^2(rt/4)\right]
\le0.
\end{aligned}
\]

The gamma term is also nonpositive because `kappa<0`.

Thus the exact compact-cell inequality is

\[
\boxed{
\begin{aligned}
&\sum_{q\le e^{rt}}{\Lambda(q)\over\sqrt q}(rt-\log q)
+\mathcal L_r(t)\\
&\quad\ge
16\left[\sinh^2(rt/4)-r^2\sinh^2(t/4)\right]
-{\kappa\over2}r(r-1)t,
\end{aligned}}
\tag{2}
\]

where `mathcal L_r(t)>0` is the displayed Lerch series. Uniform subexponential
control of the deficit in (2) on one fixed interval below `log 2` proves RH by
`T-20205`.

## 3. Positive-kernel Chebyshev–Riesz form

Put

\[
 X=e^{rt}
\]

and write

\[
 \psi(x)=x+E(x).
\]

The prime ramp is

\[
 P_r(t)=\int_{1^-}^{X}x^{-1/2}\log(X/x)\,d\psi(x).
\]

Stieltjes integration by parts gives

\[
\boxed{
P_r(t)=4X^{1/2}-4-2\log X
+\int_1^X E(x)K_X(x)\,dx,}
\tag{3}
\]

with

\[
\boxed{
K_X(x)=x^{-3/2}
\left(1+{1\over2}\log{X\over x}\right)>0
\qquad(1\le x\le X).}
\tag{4}
\]

Consequently

\[
\boxed{
\mathcal D_r(t)
=\mathcal A_r(t)
 +\int_1^{e^{rt}}(\psi(x)-x)K_{e^{rt}}(x)\,dx,}
\tag{5}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal A_r(t)={}&
4r^2(e^{t/2}+e^{-t/2}-2)
-4e^{-rt/2}+4-2rt\\
&+{\kappa\over2}r(r-1)t
+\mathcal L_r(t).
\end{aligned}}
\tag{6}
\]

Unlike `L-20203`, the Riesz kernel here has no negative region at all.

## 4. Exact remaining arithmetic theorem

For any fixed `0<a<b<log2`, it is enough to prove uniformly for `t in [a,b]`

\[
\boxed{
\mathcal A_r(t)
+\int_1^{e^{rt}}(\psi(x)-x)K_{e^{rt}}(x)\,dx
\ge-e^{\epsilon r}}
\tag{7}
\]

for every `epsilon>0` and all sufficiently large integer `r`.

The kernel is positive, but `psi(x)-x` changes sign. Therefore (7) remains a
one-sided Chebyshev-error theorem, not a consequence of kernel positivity alone.
The exact next step must use correlation or transport:

- a Selberg convolution square;
- PR #216's prime-pair energy;
- PR #219's prime-mass quantile polygon.

## 5. Proof-producing advantages

A directed level needs only:

1. one complete prime-power manifest through `e^(rt)`;
2. positive weighted accumulation—no negative prime cancellation;
3. explicit hyperbolic and gamma intervals;
4. a monotone positive Lerch sum and tail;
5. interval minimization over the fixed compact base cell.

The direct scalar and the FIR Gram portfolio of `L-20204` provide independent
algebraic replays.

## 6. Proof boundary

- Every coefficient and sign in (1)–(6) is exact.
- No uniform lower bound (7) is proved.
- Replacing the Chebyshev error by its absolute PNT bound loses the RH-scale
  cancellation and is not sufficient.
- Finite interval verification in `r` does not imply the cofinal statement.
