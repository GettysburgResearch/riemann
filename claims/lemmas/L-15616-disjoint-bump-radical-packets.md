# L-15616 — Uniform rank-`lambda^(2-delta)` repaired radical packets

Claim ID: `L-15616`  
Title: Disjoint compact zero-mean source bumps give a uniformly normalized growing arithmetic-radical packet with rapidly vanishing exterior tails  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: the Connes–Consani `E`-range radical theorem and Poisson identity; elementary disjoint-support algebra; Schwartz decay  
Scope: the uniformly controlled repaired source packet requested in Issue #156  
Related counterexample candidates: none

## Purpose

`L-15613` shows that a growing repaired source packet needs both:

1. a lower arithmetic `E`-Gram bound;
2. a uniform exterior-tail operator bound.

A generic Hermite or prolate packet does not provide the first bound because
its Mellin transform can concentrate near zeros of `zeta`.  The present lemma
constructs a different packet for which the Gram floor is local and exact: on
a multiplicative interval near the upper endpoint, only the `n=1` summand of
the arithmetic map survives.

The construction loses an arbitrarily small power from the natural
`lambda^2` phase-space rank but has no source-codimension loss and no Mellin
small-denominator problem.

## Fixed source atom

Choose a real function

\[
 \psi\in C_c^\infty(-1/4,1/4),
 \qquad
 \|\psi\|_{L^2(\mathbb R)}=1,
 \qquad
 \int_{\mathbb R}\psi(x)\,dx=0.
 \tag{L-15616.1}
\]

For example, take the normalized derivative of a nonzero real bump.

Fix

\[
 0<\delta<1,
 \qquad
 q_\lambda=\lambda^\delta,
 \qquad
 \ell_\lambda=\frac{q_\lambda}{\lambda}.
 \tag{L-15616.2}
\]

Inside the positive interval

\[
 I_\lambda^+=\left(\frac58\lambda,\frac78\lambda\right)
 \tag{L-15616.3}
\]

choose points `x_(lambda,k)` whose intervals

\[
 x_{\lambda,k}+\ell_\lambda(-1/4,1/4)
 \tag{L-15616.4}
\]

are pairwise disjoint and separated by at least `ell_lambda/2`.  One may choose

\[
 \boxed{
 d_\lambda
 \ge c_0\frac{\lambda}{\ell_\lambda}-1
 =c_0\lambda^{2-\delta}-1}
 \tag{L-15616.5}
\]

for one absolute `c_0>0`.

Define the positive bump

\[
 b_{\lambda,k}(x)
 =\ell_\lambda^{-1/2}
 \psi\!\left(\frac{x-x_{\lambda,k}}{\ell_\lambda}\right)
 \tag{L-15616.6}
\]

and its normalized even repair

\[
 \boxed{
 f_{\lambda,k}(x)
 =2^{-1/2}\bigl(b_{\lambda,k}(x)+b_{\lambda,k}(-x)\bigr).}
 \tag{L-15616.7}
\]

The positive and negative supports are disjoint for large `lambda`.

## Exact source properties

The family

\[
 f_{\lambda,1},\ldots,f_{\lambda,d_\lambda}
 \tag{L-15616.8}
\]

is real, even, smooth, compactly supported, and orthonormal.  Moreover, every
member satisfies the exact Connes–Consani source constraints

\[
 \boxed{
 f_{\lambda,k}(0)=0,
 \qquad
 \widehat f_{\lambda,k}(0)
 =\int f_{\lambda,k}=0.}
 \tag{L-15616.9}
\]

Thus every coefficient combination belongs to the exact source space; no
kernel restriction and no external corrector are needed.

### Proof

The support avoids the origin.  The integral vanishes because the fixed atom
has zero integral.  Orthogonality follows from disjoint support, including the
reflected negative intervals. QED.

## Arithmetic map and local Gram floor

Use the arithmetic map

\[
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu),
 \qquad u>0.
 \tag{L-15616.10}
\]

Let `C_lambda=C^(d_lambda)` with its Euclidean norm, and put

\[
 \mathcal F_\lambda c
 =\sum_{k=1}^{d_\lambda}c_kf_{\lambda,k},
 \qquad
 r_\lambda(c)=E(\mathcal F_\lambda c).
 \tag{L-15616.11}
\]

For

\[
 u\in I_\lambda^+,
\]

every term with `n>=2` has `nu>lambda`, outside the positive source support.
Therefore

\[
 E(\mathcal F_\lambda c)(u)
 =u^{1/2}\mathcal F_\lambda c(u)
 \qquad(u\in I_\lambda^+).
 \tag{L-15616.12}
\]

Since exactly one half of the source norm is on the positive axis,

\[
\begin{aligned}
 \|r_\lambda(c)\|_{L^2(d^*u)}^2
 &\ge
 \int_{I_\lambda^+}
 |u^{1/2}\mathcal F_\lambda c(u)|^2\frac{du}{u}\\
 &=\frac12\|c\|_2^2.
\end{aligned}
 \tag{L-15616.13}
\]

Hence the complete global arithmetic Gram satisfies the dimension-free bound

\[
 \boxed{
 \mathcal F_\lambda^*E^*E\mathcal F_\lambda
 \succeq\frac12 I_{d_\lambda}.}
 \tag{L-15616.14}
\]

In the notation of `L-15613`, one may take

\[
 \boxed{g_\lambda^2\ge1/2.}
 \tag{L-15616.15}
\]

This lower bound is independent of zeta values and packet dimension.

## Exact upper-tail vanishing

Every source is supported inside `(-lambda,lambda)`.  Thus

\[
 \boxed{r_\lambda(c)(u)=0\qquad(u>\lambda).}
 \tag{L-15616.16}
\]

Indeed, `nu>lambda` for every `n>=1`.

## Uniform lower-tail estimate

The exact Poisson identity on the codimension-two source space gives

\[
 E(f)(u)=E(\widehat f)(u^{-1}).
 \tag{L-15616.17}
\]

Let

\[
 T_\lambda c
 =1_{(0,1/\lambda)}r_\lambda(c).
 \tag{L-15616.18}
\]

For every integer `N>=2`, Schwartz decay of the fixed atom gives a constant
`C_N` such that, uniformly in `lambda`, `k`, and real `xi`,

\[
 |\widehat f_{\lambda,k}(\xi)|
 \le C_N\ell_\lambda^{1/2}
 (1+\ell_\lambda|\xi|)^{-N}.
 \tag{L-15616.19}
\]

For `||c||_2=1`, Cauchy–Schwarz and (L-15616.5) imply

\[
 |\widehat{\mathcal F_\lambda c}(\xi)|
 \le C_N\sqrt{d_\lambda\ell_\lambda}
 (1+\ell_\lambda|\xi|)^{-N}
 \le C_N'\lambda^{1/2}
 (1+\ell_\lambda|\xi|)^{-N}.
 \tag{L-15616.20}
\]

For `v>=lambda`, summing over `n` yields

\[
 \left|
 \sum_{n\ge1}
 \widehat{\mathcal F_\lambda c}(nv)
 \right|
 \le C_N''\lambda^{1/2}
 (\ell_\lambda v)^{-N}.
 \tag{L-15616.21}
\]

Using `v=1/u` in (L-15616.17), one obtains

\[
\begin{aligned}
 \|T_\lambda c\|_{L^2(d^*u)}^2
 &=\int_\lambda^\infty
 \left|\sum_{n\ge1}
 \widehat{\mathcal F_\lambda c}(nv)
 \right|^2dv\\
 &\le C_N
 \lambda^2q_\lambda^{-2N}.
\end{aligned}
 \tag{L-15616.22}

Therefore

\[
 \boxed{
 \|T_\lambda\|_{C_\lambda\to L^2(d^*u)}
 \le C_N\lambda q_\lambda^{-N}
 =C_N\lambda^{1-\delta N}.}
 \tag{L-15616.23}
\]

Since `N` is arbitrary, the whole-packet exterior tail is smaller than every
prescribed inverse power of `lambda`.

### Hardy-strip version

For

\[
 0\le\tau<1/2,
\]

the same calculation with the multiplicative Hardy weight gives

\[
 \boxed{
 \|T_\lambda\|_{C_\lambda\to X_{\lambda,\tau}}
 \le C_{N,\tau}
 \lambda^{1+\tau}q_\lambda^{-N}.}
 \tag{L-15616.24}
\]

More generally, every tail seminorm obtained by inserting a fixed finite number
of logarithmic derivatives and polynomial weights has the form

\[
 C_{N,m}\lambda^{A_m}q_\lambda^{-N}
 \tag{L-15616.25}
\]

and is rapidly decreasing after choosing `N` large.  Thus any fixed finite
form/graph norm with polynomial support loss is controlled uniformly over the
entire growing packet.

## Normalized repaired-packet conclusion

Let

\[
 J_\lambda
 =1_{[1/\lambda,\lambda]}
 E\mathcal F_\lambda.
 \tag{L-15616.26}
\]

Equations (L-15616.14) and (L-15616.23) give, for sufficiently large
`lambda`,

\[
 J_\lambda^*J_\lambda
 \succeq\left(\frac12-o(1)\right)I.
 \tag{L-15616.27}
\]

Consequently the packet has exact rank `d_lambda` and its normalized tail
synthesis satisfies

\[
 \boxed{
 \|T_\lambda J_\lambda^{-1}\|
 =O_M(\lambda^{-M})
 \qquad\text{for every }M>0.}
 \tag{L-15616.28}
\]

The rank obeys

\[
 \boxed{
 d_\lambda\gg_\delta\lambda^{2-\delta}.}
 \tag{L-15616.29}
\]

Thus the uniformly controlled repaired source packet requested in the scalar
capacity route exists unconditionally, at every rank below the natural
`lambda^2` phase-space scale by an arbitrarily small power.

## Near-radical form and residual consequence

Every `r_lambda(c)=E(F_lambda c)` lies in the global Weil radical.  Splitting it
into its localized piece and exterior tail transfers the complete localized
form and cross residual to the tail, as in `L-14309/L-14313`.

If the declared tail/form continuity constants grow at most polynomially in
`lambda`, then (L-15616.25) gives, uniformly on the whole packet,

\[
 -\alpha_\lambda G_\lambda
 \preceq B_\lambda\preceq
 \alpha_\lambda G_\lambda,
 \qquad
 \mathcal R_\lambda
 \preceq\beta_\lambda^2G_\lambda,
 \tag{L-15616.30}
\]

with

\[
 \boxed{
 \alpha_\lambda=O_M(\lambda^{-M}),
 \qquad
 \beta_\lambda=O_M(\lambda^{-M})}
 \tag{L-15616.31}
\]

for every `M` after increasing the Schwartz order used in the estimate.

The exact polynomial continuity budget for the Suzuki/Weil form must still be
bound to its normalization; no non-polynomial hidden loss may be omitted.

## Consequence for the scalar deficit target

The source-packet side of

\[
 \operatorname{Tr}D_\lambda
 -d_\lambda(G_\lambda-\alpha_\lambda)
 \le G_\lambda-\Gamma_\lambda
 \tag{L-15616.32}
\]

is now explicit:

\[
 d_\lambda\gg\lambda^{2-\delta},
 \qquad
 \alpha_\lambda,\beta_\lambda
 =O_M(\lambda^{-M}).
 \tag{L-15616.33}
\]

What remains is solely the complete arithmetic deficit estimate.  In
particular, a sufficient asymptotic is

\[
 \boxed{
 \operatorname{Tr}D_\lambda
 \le(1-\eta)G_\lambda d_\lambda}
 \tag{L-15616.34}
\]

for some fixed `eta>0`, with `Gamma_lambda` chosen inside the resulting moat.
The construction does not prove (L-15616.34).

## Interaction with the zero-evaluation obstruction

The packet is made of exact radical sources and therefore lies in the
certified-zero near-kernel, as required by `L-15304`.  It is not claimed to
approximate the complete evaluation-visible low packet.  Instead it supplies a
large proof-grade low packet for the count-saturation argument of
`L-15610/L-15612`; any surplus evaluation-visible directions must still be
excluded by the arithmetic deficit or finite visible Schur gate.

## Proof boundary

- The disjoint-bump construction, exact source constraints, rank, and local
  arithmetic Gram floor are elementary.
- The lower-tail estimate imports the exact Poisson identity and Fourier
  normalization of the Connes–Consani `E` map.
- The Hardy/form seminorm extension requires the declared form continuity
  constants to have at most polynomial support growth.
- The construction gives rank `lambda^(2-delta)`, not the endpoint
  `lambda^2` rank.
- No complete arithmetic deficit bound is proved, and no proof of RH is
  claimed.
