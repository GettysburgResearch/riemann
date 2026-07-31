# L-15410 — The triangular prime signal is a critical derivative of one positive primitive

Claim ID: `L-15410`  
Title: The pole-free prime window is the `e^(x/2)`-rescaled derivative of a positive Mertens average and a finite difference of the zeta screw function  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15409`; Nakamura--Suzuki's exact prime formula for `g_zeta`; the prime number theorem for the limiting constant  
Scope: structural positive route for `T-15406`  
Related counterexample candidates: none

## Tilted window

Let `F_h,G_h` be the triangular windows of `L-15409`, with `h=log 4`. Put

\[
 \widetilde F_h(u)=e^{-u/2}F_h(u),
 \qquad
 \widetilde G_h(u)=e^{-u/2}G_h(u).
 \tag{L-15410.1}
\]

Since

\[
 2e^{-h/2}=1,
\]

one has the exact cancellation

\[
 \boxed{
 \widetilde G_h(u)=
 \widetilde F_h(u)-\widetilde F_h(u-h).}
 \tag{L-15410.2}
\]

Define

\[
 \boxed{
 H_h(u)=\int_{u-h}^{u}\widetilde F_h(v)\,dv.}
 \tag{L-15410.3}
\]

Then

\[
 H_h\ge0,
 \qquad
 \operatorname{supp}H_h\subset[0,3h],
 \qquad
 H_h'=\widetilde G_h.
 \tag{L-15410.4}
\]

## Positive arithmetic primitive

Define

\[
 \boxed{
 A_h(x)=
 \sum_{n\ge2}\frac{\Lambda(n)}{n}
 H_h(x-\log n).}
 \tag{L-15410.5}
\]

This is a finite sum at every `x`, and

\[
 \boxed{A_h(x)\ge0.}
 \tag{L-15410.6}
\]

Away from the finitely many translated breakpoints, termwise differentiation
is classical; globally the identity holds in distributions and by continuity:

\[
\begin{aligned}
 e^{x/2}A_h'(x)
 &=e^{x/2}
   \sum_n\frac{\Lambda(n)}n
   \widetilde G_h(x-\log n)\\
 &=\sum_n\frac{\Lambda(n)}{\sqrt n}
   G_h(x-\log n).
\end{aligned}
\]

Therefore

\[
 \boxed{Q_h(x)=e^{x/2}A_h'(x).}
 \tag{L-15410.7}
\]

The positive route is equivalently the critical energy estimate

\[
 \boxed{
 \sup_{X\ge1}\frac1X
 \int_{x_0}^{x_0+X}e^x|A_h'(x)|^2dx<\infty.}
 \tag{L-15410.8}
\]

## PNT limit

The measure

\[
 d\mu(t)=\sum_{n\ge2}\frac{\Lambda(n)}n
 \delta_{\log n}(dt)
 \tag{L-15410.9}
\]

has unit asymptotic density under translation as a consequence of the prime
number theorem. Hence, for the fixed compact continuous kernel `H_h`,

\[
 A_h(x)\longrightarrow\int_{\mathbb R}H_h(u)du.
 \tag{L-15410.10}
\]

By Fubini,

\[
 \int H_h(u)du
 =h\int\widetilde F_h(u)du
 =h\widehat F_{h,L}(1/2).
 \tag{L-15410.11}
\]

Since `e^(-h/2)=1/2`,

\[
 \widehat F_{h,L}(1/2)
 =\left(\frac{1-1/2}{h/2}\right)^2
 =\frac1{h^2}.
\]

Thus

\[
 \boxed{A_h(x)\longrightarrow\frac1h.}
 \tag{L-15410.12}
\]

This is unconditional.

The missing RH estimate is now visible without transforms:

```text
PNT gives:       A_h(x) -> 1/h;
RH target gives: A_h'(x) = O(e^(-x/2))
                 or its critical weighted mean-square analog.
```

Positivity and convergence of `A_h` alone do not imply that derivative scale.
A real-variable proof must exploit the arithmetic correlations in `mu`.

## Exact screw-function bridge

For `t>=0`, let

\[
 K(t)=\sum_{n\le e^t}
 \frac{\Lambda(n)}{\sqrt n}(t-\log n).
 \tag{L-15410.13}
\]

Nakamura--Suzuki's exact function is

\[
\begin{aligned}
 g_\zeta(t)={}&K(t)
 -4(e^{t/2}+e^{-t/2}-2)\\
 &-\frac t2\bigl(\psi(1/4)-\log\pi\bigr)\\
 &+\frac14\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)
 -\Phi(1,2,1/4)
 \right].
\end{aligned}
 \tag{L-15410.14}
\]

Define the finite-difference operator

\[
 \mathcal D_hf(t)=\frac1{h^2}
 \bigl[f(t)-4f(t-h)+5f(t-2h)-2f(t-3h)\bigr].
 \tag{L-15410.15}
\]

`L-15409` gives

\[
 \mathcal D_hK=Q_h.
 \tag{L-15410.16}
\]

The coefficient polynomial kills constants, linear functions, and `e^(t/2)`.
Moreover, the nominal `e^(-t/2)` archimedean term cancels internally:

\[
 -4e^{-t/2}
 +\frac14e^{-t/2}\Phi(e^{-2t},2,1/4)
 =\frac14e^{-t/2}
  \bigl[\Phi(e^{-2t},2,1/4)-16\bigr].
 \tag{L-15410.17}
\]

The bracket is `O(e^(-2t))`. Consequently there is one explicit function
`R_h(t)=O_h(e^(-5t/2))` such that, for `t>3h`,

\[
 \boxed{
 Q_h(t)=\mathcal D_hg_\zeta(t)+R_h(t).}
 \tag{L-15410.18}
\]

The correction is obtained by applying `-mathcal D_h` to the right side of
(L-15410.17), and is fully explicit.

## Connection to infinite divisibility

Nakamura and Suzuki prove that RH is equivalent to `exp(g_zeta)` being the
characteristic function of an infinitely divisible distribution. Under RH,

\[
 g_\zeta(t)=
 \sum_\gamma m_\gamma
 \frac{e^{-i\gamma t}-1}{\gamma^2}.
 \tag{L-15410.19}
\]

Equation (L-15410.18) shows that the triangular prime signal is one fixed finite
difference of this Lévy exponent, up to an exponentially decaying elementary
correction. Thus the positive prime-window route and the screw/infinite-
divisibility route are not separate programmes:

\[
 \boxed{
 \text{bounded }Q_h
 \quad\Longleftrightarrow\quad
 \text{bounded pole-free finite difference of }g_\zeta.}
 \tag{L-15410.20}
\]

A proof that `g_zeta` is conditionally negative definite would prove much more
than (L-15410.8), and would settle RH through the cited theorem. Conversely,
termwise positivity of the prime formula is unavailable: the cancellation in
(L-15410.17) and the terminal-prime/polar cancellation of `L-15404` are
load-bearing.

## Why the positive primitive is useful

1. It removes the enormous pole contribution before differentiation.
2. It gives a nonnegative finite arithmetic object `A_h` converging to the exact
   constant `1/h`.
3. It identifies the missing estimate as a weighted Dirichlet energy, not a
   pointwise prime-counting approximation.
4. It provides an exact direct producer:
   construct `A_h` from positive terms and differentiate its fixed affine pieces.
5. It supplies a potential route through a nonlinear or matrix-valued energy
   inequality, while ruling out arguments based only on positivity and ordinary
   convergence.

## Gap audit

- PNT convergence of `A_h` has no critical rate and does not imply RH.
- A positive convergent function may have derivatives much larger than
  `e^(-x/2)`; arithmetic structure must be used.
- The screw formula and Hurwitz--Lerch normalization require independent source
  review.
- Conditional negative definiteness of `g_zeta` is itself an RH-equivalent
  statement, not an available theorem.
- This lemma exposes the positive object and exact missing energy estimate; it
  does not prove that estimate.
