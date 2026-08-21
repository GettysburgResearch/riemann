# L-21501 — Prime-power convex duality for the zeta screw function

Claim ID: `L-21501`  
Title: The complete negative depth of the zeta screw function equals the vertical deficit of one explicit prime-power moment polygon  
Status: `PROPOSED — COMPLETE CONVEX-ANALYTIC CONSEQUENCE OF THE IMPORTED SCREW FORMULA`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-19801`; elementary Fenchel duality; the exact Nakamura–Suzuki prime/Lerch formula  
Scope: a global scalar reorganization of the full RH sign problem

## 1. Exact difference-of-convex decomposition

Let `Psi=-g_zeta` be the function of `L-19801` and put

\[
 t_0=\log 2,
 \qquad
 \kappa=\psi(1/4)-\log\pi.
\tag{L-21501.1}
\]

For `t>=t_0`, define the explicit archimedean function

\[
\boxed{
\begin{aligned}
F(t)={}&4\bigl(e^{t/2}+e^{-t/2}-2\bigr)
 +{\kappa t\over2}\\
&-{1\over4}\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)-\Phi(1,2,1/4)
 \right],
\end{aligned}}
\tag{L-21501.2}
\]

and the finite prime-power ramp

\[
\boxed{
G(t)=\sum_{q\ge2}{\Lambda(q)\over\sqrt q}
      (t-\log q)_+.
}
\tag{L-21501.3}
\]

Here only prime powers contribute. The exact screw formula is

\[
\boxed{\Psi(t)=F(t)-G(t).}
\tag{L-21501.4}
\]

Thus all archimedean, pole, and trivial-zero terms are in `F`, while all finite arithmetic is in the positive ramp sum `G`.

## 2. Strict convexity begins before the first prime-power knot

Termwise differentiation of the absolutely convergent Lerch series gives

\[
\begin{aligned}
F''(t)
&=e^{t/2}+e^{-t/2}
  -{e^{-t/2}\over1-e^{-2t}}\\
&={e^{-t/2}(e^{3t}-e^t-1)\over e^{2t}-1}.
\end{aligned}
\tag{L-21501.5}
\]

At `t=t_0`, the numerator is `8-2-1=5`, and it is strictly increasing afterward. Hence

\[
\boxed{F''(t)>0\qquad(t\ge t_0).}
\tag{L-21501.6}
\]

The function `G` is closed, convex, continuous, and piecewise affine. Its derivative has only downward effects on `Psi'`: at a prime power `q`, `G'` jumps upward by `Lambda(q)/sqrt(q)`.

## 3. The prime-power moment polygon

List the prime powers in increasing order:

\[
2=q_1<q_2<\cdots,
\qquad
\nu_j=\log q_j,
\qquad
a_j={\Lambda(q_j)\over\sqrt{q_j}}.
\tag{L-21501.7}
\]

Define the two finite prefix moments

\[
\boxed{
A_j=\sum_{i\le j}a_i,
\qquad
B_j=\sum_{i\le j}a_i\nu_i,
}
\tag{L-21501.8}
\]

and put `A_0=B_0=0`.

Extend `F` and `G` by `+infinity` to `t<t_0`, and let

\[
F^*(A)=\sup_{t\ge t_0}(At-F(t)),
\qquad
G^*(A)=\sup_{t\ge t_0}(At-G(t)).
\tag{L-21501.9}
\]

For `A_(j-1)<=A<=A_j`, direct maximization at the knot `nu_j` gives

\[
\boxed{
G^*(A)
 =B_{j-1}+(A-A_{j-1})\nu_j.
}
\tag{L-21501.10}
\]

In particular,

\[
\boxed{G^*(A_j)=B_j.}
\tag{L-21501.11}
\]

Thus `G^*` is exactly the polygonal line through the finite arithmetic vertices

\[
(0,0),(A_1,B_1),(A_2,B_2),\ldots.
\tag{L-21501.12}
\]

## 4. Exact minimax identity

The complete negative depth of the screw function on `[t_0,infinity)` is

\[
\boxed{
\sup_{t\ge t_0}(-\Psi(t))
 =\sup_{A\ge0}\bigl(F^*(A)-G^*(A)\bigr).
}
\tag{L-21501.13}
\]

### Proof

Fenchel–Moreau gives

\[
G(t)=\sup_A(At-G^*(A)).
\]

Therefore

\[
G(t)-F(t)
\le\sup_A(F^*(A)-G^*(A)).
\]

Conversely, for every `A` and `t`,

\[
At-G^*(A)\le G(t).
\]

Taking the supremum over `t` in `At-F(t)` gives

\[
F^*(A)-G^*(A)
\le\sup_t(G(t)-F(t)).
\]

Taking the corresponding suprema proves (L-21501.13). For `A<0`, both conjugates are supported at the left boundary and their difference is `-F(t_0)`. At `A=0`, one has `G^*(0)=0` and `F^*(0)>=-F(t_0)`, so no larger deficit is lost by restricting to `A>=0`. QED.

On every edge `[A_(j-1),A_j]`, the function `F^*-G^*` is convex because `F^*` is convex and `G^*` is affine. Its maximum on that edge is therefore at an endpoint. Hence the minimax identity sharpens to

\[
\boxed{
\sup_{t\ge t_0}(-\Psi(t))
 =\sup_{j\ge0}\bigl(F^*(A_j)-B_j\bigr).
}
\tag{L-21501.14}
\]

This is an equality of complete infinite objects. It does not discard a zero, a prime power, a phase, or an operator complement.

## 5. Finite tangent witness

Fix one prefix `j`, and let `t_j` maximize `A_j t-F(t)` on `[t_0,infinity)`. Then

\[
F^*(A_j)=A_jt_j-F(t_j).
\tag{L-21501.15}
\]

Because `G^*(A_j)=B_j`, Fenchel's inequality gives

\[
G(t_j)\ge A_jt_j-B_j.
\]

Consequently

\[
\boxed{
\Psi(t_j)
\le B_j-F^*(A_j).
}
\tag{L-21501.16}
\]

Therefore one strict finite inequality

\[
\boxed{F^*(A_j)>B_j}
\tag{L-21501.17}
\]

is an unconditional finite disproof of RH.

More generally, no optimization is needed for a negative certificate. For any rational or directed trial point `t>=t_0`,

\[
\boxed{
A_jt-F(t)-B_j>0
\quad\Longrightarrow\quad
\Psi(t)<0
\quad\Longrightarrow\quad
\mathrm{RH\ is\ false}.
}
\tag{L-21501.18}
\]

The implication is fail-closed because `F^*(A_j)` is a supremum.

## 6. Exact radial form of the archimedean conjugate

Put

\[
r=e^{t/2}\ge\sqrt2,
\qquad
C_0={1\over4}\Phi(1,2,1/4)-8.
\tag{L-21501.19}
\]

Using

\[
\Phi(1,2,1/4)=\pi^2+8G_{\rm Catalan}
\]

if desired, the cancellation of the `r^-1` pole and `k=0` Lerch terms gives the exact rapidly convergent series

\[
\boxed{
F(2\log r)
 =4r+\kappa\log r+C_0
 -4\sum_{k\ge1}{r^{-(4k+1)}\over(4k+1)^2}.
}
\tag{L-21501.20}
\]

Its `t` derivative is

\[
\boxed{
\alpha(r)
 =2r+{\kappa\over2}
 +2\sum_{k\ge1}{r^{-(4k+1)}\over4k+1}.
}
\tag{L-21501.21}
\]

Equation (L-21501.6) says that `alpha` is strictly increasing. If `A>F'(t_0)`, let `r(A)` be the unique solution of

\[
\alpha(r(A))=A.
\tag{L-21501.22}
\]

Then

\[
\boxed{
\begin{aligned}
F^*(A)
={}&(2A-\kappa)(\log r(A)-1)-C_0\\
&+4\sum_{k\ge1}
\left({1\over4k+1}+{1\over(4k+1)^2}\right)
 r(A)^{-(4k+1)}.
\end{aligned}}
\tag{L-21501.23}
\]

Every series term in (L-21501.21) and (L-21501.23) is positive and has a geometric directed tail.

For large `A`,

\[
r(A)={A-\kappa/2\over2}+O(A^{-5})
\tag{L-21501.24}
\]

and

\[
\boxed{
F^*(A)
=(2A-\kappa)
 \left[
 \log{A-\kappa/2\over2}-1
 \right]
 +8-{1\over4}\Phi(1,2,1/4)
 +O(A^{-5}).
}
\tag{L-21501.25}
\]

Thus the prime-power criterion is an exact self-normalized entropy inequality, with a completely explicit archimedean threshold.

## 7. Euler-product curvature coordinates

Define the finite triangular Euler exponential

\[
\mathcal Z_Q(s)
 =\exp\left(
 \sum_{p^k\le Q}{1\over k p^{ks}}
 \right).
\tag{L-21501.26}
\]

At a prime-power endpoint `Q=q_j`,

\[
\boxed{
A_j=-\left.(\log\mathcal Z_Q)'(s)\right|_{s=1/2},
\qquad
B_j=\left.(\log\mathcal Z_Q)''(s)\right|_{s=1/2}.
}
\tag{L-21501.27}
\]

Hence the polygon criterion is equivalently a curvature-versus-slope barrier for finite Euler products. Generic log-convexity gives only

\[
B_j\,\log\mathcal Z_Q(1/2)\ge A_j^2,
\]

which is much weaker than (L-21501.17)'s sharp threshold; the missing strength remains arithmetic rather than convex-algebraic.

## 8. Proof boundary

- The difference-of-convex decomposition, strict convexity, conjugate polygon, minimax identity, and radial formulas are exact.
- The theorem does not establish `B_j>=F^*(A_j)` cofinally.
- A production negative witness must direct every logarithm, square root, special constant, prefix sum, and series tail.
- A finite positive run does not establish the cofinal inequality.
- The status is `PROPOSED` pending independent review; no RH resolution is claimed.
