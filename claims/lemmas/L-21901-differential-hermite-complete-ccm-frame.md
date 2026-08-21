# L-21901 — Differential-Hermite polynomials give an exact complete even CCM source frame

Claim ID: `L-21901`  
Title: One Gaussian Xi source and the dilation operator generate every finite even CCM Fourier vector by an explicit Vandermonde interpolation  
Status: **PROPOSED — COMPLETE ALGEBRAIC/ANALYTIC FRAME THEOREM; UNIFORM TAIL METRIC SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15101`; `L-14304`; the Connes--Consani arithmetic-map normalization  
Scope: the exact source/finite-space congruence gate in the prolate and whole-matrix positive programmes

## 1. The exact Xi source

Use the additive Fourier convention

\[
 \mathcal Ff(\xi)=\int_{\mathbb R}f(x)e^{2\pi i x\xi}\,dx.
 \tag{L-21901.1}
\]

Let

\[
 h(x)=\left(\pi^2x^4-\frac{3\pi}{2}x^2\right)e^{-\pi x^2}
 \tag{L-21901.2}
\]

be the exact source of `L-15101`, and put

\[
 K(t)=E(h)(e^t).
 \tag{L-21901.3}
\]

The imported, normalization-pinned identities are

\[
 h(0)=0,
 \qquad \int_{\mathbb R}h=0,
 \qquad \mathcal Fh=h,
 \tag{L-21901.4}
\]

and

\[
 \boxed{\widehat K(z)=\Xi(z).}
 \tag{L-21901.5}
\]

Here the transform in `t` is

\[
 \widehat K(z)=\int_{\mathbb R}K(t)e^{-izt}\,dt.
 \tag{L-21901.6}
\]

## 2. The dilation intertwiner

Define on additive source functions

\[
 \mathcal D=x\frac d{dx}+\frac12
 \tag{L-21901.7}
\]

and on logarithmic arithmetic images

\[
 \partial_t=u\frac d{du},
 \qquad u=e^t.
 \tag{L-21901.8}
\]

For every Schwartz source for which termwise differentiation is valid,

\[
\begin{aligned}
 E(\mathcal Df)(u)
 &=u^{1/2}\sum_{n\ge1}
 \left[nu f'(nu)+\frac12f(nu)\right]\\
 &=u\frac d{du}
 \left[u^{1/2}\sum_{n\ge1}f(nu)\right].
\end{aligned}
\]

Therefore

\[
 \boxed{E(\mathcal Df)(e^t)=\partial_tE(f)(e^t).}
 \tag{L-21901.9}
\]

Put

\[
 \mathcal A=-\mathcal D^2.
 \tag{L-21901.10}
\]

Then

\[
 \boxed{E(\mathcal Af)(e^t)=-\partial_t^2E(f)(e^t).}
 \tag{L-21901.11}
\]

Since the Fourier multiplier of `-partial_t^2` is `z^2`, every polynomial
`P in C[X]` satisfies

\[
 \boxed{
 \widehat{E(P(\mathcal A)h)}(z)
 =P(z^2)\Xi(z).
 }
 \tag{L-21901.12}
\]

## 3. Every polynomial source is an exact radical source

If `f` is even Schwartz, `f(0)=0`, and `int f=0`, then the same is true of
`mathcal D f`:

\[
 (\mathcal Df)(0)=0
 \tag{L-21901.13}
\]

and integration by parts gives

\[
 \int_{\mathbb R}\mathcal Df
 =-\frac12\int_{\mathbb R}f=0.
 \tag{L-21901.14}
\]

Thus every

\[
 h_P=P(\mathcal A)h
 \tag{L-21901.15}
\]

belongs to the exact two-cancellation source space.

Moreover

\[
 \mathcal F\mathcal D=-\mathcal D\mathcal F,
 \tag{L-21901.16}
\]

so `mathcal A` commutes with `mathcal F`. Since `mathcal Fh=h`,

\[
 \boxed{\mathcal Fh_P=h_P.}
 \tag{L-21901.17}
\]

Consequently every arithmetic image `E(h_P)` is inversion-even and belongs to
the exact global weak Weil radical in the normalization of `L-16205`.

## 4. Exact finite even Fourier frame

Fix a centered interval

\[
 I_\ell=[-\ell,\ell]
 \tag{L-21901.18}
\]

and frequencies

\[
 \omega_k=\frac{\pi k}{\ell},
 \qquad 0\le k\le N.
 \tag{L-21901.19}
\]

Let `V_(ell,N)^+` be the even sector of the centered CCM Fourier space.  By
`L-14304`, changing between these coordinates and the source paper's CCM
coordinates is one exact diagonal sign congruence.

For a Schwartz logarithmic function, periodization has Fourier coefficient

\[
 \left\langle
 (2\ell)^{-1/2}e^{i\omega_kt},
 \Sigma_{2\ell}K_P
 \right\rangle
 =(2\ell)^{-1/2}\widehat K_P(\omega_k).
 \tag{L-21901.20}
\]

In the normalized even cosine basis this differs only by the explicit diagonal
factor `1` at `k=0` and `sqrt(2)` for `k>0`.  Thus the projected image of
`h_P` has `k`th coordinate

\[
 s_k(2\ell)^{-1/2}\Xi(\omega_k)P(\omega_k^2),
 \qquad
 s_0=1,\quad s_k=\sqrt2\ (k>0).
 \tag{L-21901.21}
\]

Assume the finite nonresonance condition

\[
 \Xi(\omega_k)\ne0,
 \qquad 0\le k\le N.
 \tag{L-21901.22}
\]

Take `P_m(X)=X^m`, `0<=m<=N`. The source-to-target matrix is a product of
three invertible matrices:

\[
 \operatorname{diag}
 \left(s_k(2\ell)^{-1/2}\Xi(\omega_k)\right),
 \tag{L-21901.23}
\]

the squared-frequency Vandermonde

\[
 V_{km}=(\omega_k^2)^m,
 \tag{L-21901.24}
\]

and an optional transpose according to the coefficient convention. Its
determinant is, up to the declared nonzero diagonal normalization,

\[
 \boxed{
 \det V
 =\prod_{0\le i<j\le N}
 (\omega_j^2-\omega_i^2)\ne0.
 }
 \tag{L-21901.25}
\]

Therefore

\[
 \boxed{
 P_N\Sigma_{2\ell}E
 \left(\operatorname{span}
 \{h,\mathcal Ah,\ldots,\mathcal A^Nh\}
 \right)
 =V_{\ell,N}^{+}.
 }
 \tag{L-21901.26}
\]

This is an explicit exact source-frame theorem. It does not use density of the
full source range, a zeta-cycle theorem, or a numerical right inverse.

## 5. Explicit interpolation inverse

Let

\[
 x_k=\omega_k^2.
 \tag{L-21901.27}
\]

For any even target vector `y=(y_0,...,y_N)`, define the unique polynomial of
degree at most `N` by

\[
 \boxed{
 P_y(x_k)
 ={\sqrt{2\ell}\,y_k
  \over s_k\Xi(\omega_k)}.
 }
 \tag{L-21901.28}
\]

Equivalently,

\[
 P_y(X)=\sum_{k=0}^N
 {\sqrt{2\ell}\,y_k
  \over s_k\Xi(\omega_k)}
 \prod_{\substack{0\le j\le N\\j\ne k}}
 {X-x_j\over x_k-x_j}.
 \tag{L-21901.29}
\]

Then

\[
 \boxed{
 P_N\Sigma_{2\ell}E(P_y(\mathcal A)h)=y.
 }
 \tag{L-21901.30}
\]

In particular, every finite even prolate vector, the repaired Xi target, and
every vector in its finite orthogonal complement have explicit smooth exact
radical preimages.

## 6. Exact denominator formula

Put

\[
 a=\left({\pi\over\ell}\right)^2,
 \qquad x_k=ak^2.
 \tag{L-21901.31}
\]

The Lagrange denominators are elementary:

\[
 \boxed{
 \prod_{j=1}^N|x_0-x_j|
 =a^N(N!)^2,
 }
 \tag{L-21901.32}
\]

and, for `1<=k<=N`,

\[
 \boxed{
 \prod_{\substack{0\le j\le N\\j\ne k}}
 |x_k-x_j|
 ={a^N\over2}(N-k)!(N+k)!.
 }
 \tag{L-21901.33}
\]

Thus the algebraic part of the inverse, including every factorial and support
scale, is explicit.  The only nonalgebraic denominator is the finite diagonal
`Xi(omega_k)`, which may be bounded after a zeta-safe support is selected as in
`L-21506`.

## 7. What this closes

The theorem closes the following finite statement:

```text
exact smooth two-cancellation sources
        -> exact projected arithmetic images
        -> complete even CCM Fourier space.
```

It also gives an exact congruence from the differential-Hermite source
coordinates to any chosen even prolate basis.  Hence the first load-bearing
item in the PR #202 review—existence of one exact finite source/CCM congruence—
can be discharged with this alternative frame.

## 8. What it does not close

The interpolation inverse need not preserve the prolate omitted-tail metric.
In particular, an algebraically exact source preimage can have a large
alias-and-projection-corrected tail.  Therefore (L-21901.26) does **not** prove:

1. the dimension-uniform arithmetic tail-Gram floor;
2. the `d_4/d_8` target hierarchy for the completed frame;
3. the line-centered local-Weyl scalarization;
4. the actual-minus-line support-average estimate.

Those are metric/profile statements, not source-surjectivity statements.

## 9. Literature connection

The polynomial Mellin structure is the operator form of the classical
Hermite/Meixner--Pollaczek Mellin transform.  Here no special-function formula
is required: the exact identity follows from the single intertwining relation
(L-21901.9).  The special-function literature supplies an independent
orthogonal-polynomial interpretation of the same ladder.

## 10. Proof boundary

- Equations (L-21901.9)--(L-21901.17) are elementary differentiation,
  integration by parts, and Fourier intertwining.
- The Xi normalization is inherited from `L-15101` and must use the same
  completed-zeta convention as the finite CCM matrix.
- The finite frame and inverse are exact under the finite nonresonance
  condition.
- The theorem is a newly proposed source congruence, not a proof of the growing
  tail-profile LMIs or RH.
