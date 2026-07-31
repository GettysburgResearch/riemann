# L-15405 — An explicit smooth compact window with zero-free right-half-plane Laplace transform

Claim ID: `L-15405`  
Title: A dyadic infinite convolution reduces the terminal-prime RH criterion to one fixed window  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: elementary infinite convolution and Fourier analysis  
Scope: the test-function family in `T-15402`  
Related counterexample candidates: none

## Dyadic convolution density

For `j>=1`, let

\[
 u_j(t)=2^j\mathbf1_{[0,2^{-j}]}(t).
 \tag{L-15405.1}
\]

Each `u_j` is a probability density.  Let

\[
 \mu_N=u_1*u_2*\cdots*u_N.
 \tag{L-15405.2}
\]

Equivalently, `mu_N` is the law of

\[
 X_N=\sum_{j=1}^N2^{-j}U_j,
 \qquad U_j\sim\operatorname{Unif}[0,1]
 \tag{L-15405.3}
\]

with independent `U_j`. Since the series converges almost surely, the laws
converge weakly to the law `mu` of

\[
 X=\sum_{j=1}^\infty2^{-j}U_j,
 \qquad 0\le X\le1.
 \tag{L-15405.4}
\]

## Transform

For complex `z`, define the removable value at zero in every factor. The
Laplace transform of `mu` is

\[
\boxed{
 M(z)=
 \prod_{j=1}^\infty
 {1-e^{-2^{-j}z}\over2^{-j}z}.}
 \tag{L-15405.5}
\]

The product converges locally uniformly on the complex plane. Indeed, on every
compact set,

\[
 {1-e^{-2^{-j}z}\over2^{-j}z}
 =1-2^{-j-1}z+O_K(4^{-j}),
 \tag{L-15405.6}
\]

and the deviations from one are summable. Thus `M` is entire.

## Smooth compact density

On the imaginary axis,

\[
 |M(i\xi)|
 \le\prod_{j=1}^\infty
 \min\left\{1,{2^{j+1}\over|\xi|}\right\}.
 \tag{L-15405.7}
\]

For `|xi|>=8`, take

\[
 N=\lfloor\log_2|\xi|\rfloor-2.
\]

The first `N` factors give

\[
 \log_2|M(i\xi)|
 \le {N(N+3)\over2}-N\log_2|\xi|
 =-\frac12(\log_2|\xi|)^2+O(\log|\xi|).
 \tag{L-15405.8}
\]

Hence, for every `m>=0`,

\[
 |\xi|^mM(i\xi)\in L^1(\mathbb R).
 \tag{L-15405.9}
\]

Fourier inversion shows that `mu` has a `C^infinity` density `f`, supported in
`[0,1]`. Since the extension by zero is smooth on the line, every derivative of
`f` vanishes at both endpoints.

The density is nonnegative and

\[
 \int_0^1f(t)dt=1.
 \tag{L-15405.10}
\]

## Shifted profile

Define

\[
 \phi_*(r)=f(r-1).
 \tag{L-15405.11}
\]

Then

\[
 \phi_*\in C_c^\infty(1,2),
 \qquad
 \phi_*\ge0,
 \qquad
 \int\phi_*=1.
 \tag{L-15405.12}
\]

Its Laplace transform is

\[
\boxed{
 \Phi_*(z)=e^{-z}M(z).}
 \tag{L-15405.13}
\]

For `Re z>0`, every factor in (L-15405.5) is nonzero because

\[
 |e^{-2^{-j}z}|<1.
\]

The summable-product criterion then gives

\[
\boxed{
 \Phi_*(z)\ne0
 \qquad(\operatorname{Re}z>0).}
 \tag{L-15405.14}
\]

In fact all zeros of the displayed product factors lie on the imaginary axis.

## Convolution-square window

Put

\[
 F_*=\phi_* * \phi_*.
 \tag{L-15405.15}
\]

Then

\[
 F_*\in C_c^\infty(2,4),
 \qquad F_*\ge0,
 \tag{L-15405.16}
\]

and

\[
\boxed{
 \widehat F_{*,L}(z)=\Phi_*(z)^2\ne0
 \qquad(\operatorname{Re}z>0).}
 \tag{L-15405.17}
\]

Thus `F_*` is simultaneously:

1. one fixed smooth compact test function for `T-15402`;
2. a convolution square arising from one endpoint profile in `L-15404`;
3. zero-free at every possible shifted right-half-plane zeta zero.

## Countable and computable descriptions

The finite convolutions `mu_N` are compactly supported splines with rational
breakpoints. Their transforms are the first `N` factors of (L-15405.5), while
the remaining random tail is supported in `[0,2^{-N}]`. Consequently directed
interval values of `f`, `phi_*`, and `F_*` can be produced through either:

- finite spline convolution plus a rigorously enclosed tail;
- Fourier inversion using the super-polynomial bound (L-15405.8);
- the distributional self-similarity inherited from
  \[
   X\stackrel d={1\over2}(U+X'),
  \]
  where `U` is uniform and `X'` is an independent copy of `X`.

No floating fitted profile is part of the definition.

## Why this matters

`T-15402` initially required bounded terminal translations for every smooth
profile. `F_*` has a Laplace transform which cannot accidentally annihilate an
off-line zero. Therefore a single explicit scalar prime window is enough for a
complete RH criterion, as stated in `T-15403`.

## Gap audit

- The density proof uses weighted Fourier integrability, not a pointwise claim
  about the finite splines.
- Local uniform convergence of the product must retain the removable values at
  zero.
- Zero-freeness is asserted only in the open right half-plane; imaginary-axis
  zeros are harmless for detecting `Re rho>1/2`.
- The exact profile is an infinite convolution. A production evaluator needs a
  rigorous truncation bound.
- This lemma constructs the window; it does not prove its terminal prime
  translations bounded.
