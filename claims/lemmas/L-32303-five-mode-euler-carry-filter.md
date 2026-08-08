# L-32303 — Five-mode Euler–carry filter

Claim ID: `L-32303`  
Title: One positive-inverse dyadic filter simultaneously annihilates the Green pole models and both long carry moments while preserving every off-line zeta pole  
Status: **PROPOSED COMPLETE EXACT SYNTHESIS — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26201`; `L-32302`  
Scope: exact analytic/source/carry adapter; no RH estimate is asserted

## 1. Universal filter

With `x=2^-s`, define

\[
\boxed{
P_\Box(x)
=(1-x)(1-x/2)(1-2x)(1-\sqrt2 x)^2.
}
\tag{L-32303.1}
\]

The roots have the following roles:

```text
x=1             kills the constant floor tail;
x=2             kills the affine carry tail;
x=1/2           kills the e^t pole model;
x=1/sqrt(2)     double root: kills e^(t/2) and t e^(t/2).
```

Define

\[
\boxed{
B_\Box(s)={P_\Box(2^{-s})\over\zeta(s)}.
}
\tag{L-32303.2}
\]

Every root of the finite numerator lies on one of

\[
\Re s=-1,\;0,\;1,\;1/2.
\]

Therefore

\[
\boxed{
P_\Box(2^{-\rho})\ne0
\quad\text{whenever }\Re\rho\in(1/2,1).
}
\tag{L-32303.3}
\]

No hypothetical off-line zeta zero is cancelled.

## 2. Positive inverse and generalized primes

The inverse is

\[
A_\Box(s)
={\zeta(s)\over
(1-2^{-s})(1-2^{-s-1})(1-2^{1-s})(1-2^{1/2-s})^2}.
\tag{L-32303.4}
\]

Every dyadic denominator is of the form `1-c 2^-s` with

\[
c\in\{1,1/2,2,\sqrt2,\sqrt2\},
\]

so its geometric coefficients are nonnegative.  Their product has strictly positive power-of-two coefficients; convolution with `zeta` gives

\[
\boxed{a_\Box(n)>0\quad(n\ge1).}
\tag{L-32303.5}
\]

Likewise logarithmic differentiation gives

\[
\boxed{
\Lambda_\Box(n)
=\Lambda(n)
 +(\log2)
 \left(1+2^{-r}+2^r+2\,2^{r/2}\right)
 \mathbf1_{n=2^r}
\ge0.
}
\tag{L-32303.6}
\]

Hence the generalized Selberg identity retains a coefficientwise nonnegative prime and prime-pair forcing channel.

## 3. Positive compact Green factorization

Retain the carry Green kernel of PR #263,

\[
\widehat H(s)={s(s+1)\over(s-1)(s-1/2)^2}.
\]

For

\[
\alpha\in\{1,1/2,1/2,0,-1\},
\]

put

\[
u_\alpha(t)=e^{\alpha t}\mathbf1_{0\le t\le\log2}.
\]

Every `u_alpha` is nonnegative and compactly supported, with

\[
\widehat u_\alpha(s)
={1-2^{\alpha-s}\over s-\alpha}.
\]

Define

\[
\boxed{
W_5=u_1*u_{1/2}*u_{1/2}*u_0*u_{-1}.
}
\tag{L-32303.7}
\]

Then

\[
W_5\ge0,
\qquad
\operatorname{supp}W_5\subset[0,5\log2].
\tag{L-32303.8}
\]

A direct transform calculation gives

\[
\boxed{
P_\Box(2^{-s})\widehat H(s)
=[s(s+1)]^2\widehat W_5(s).
}
\tag{L-32303.9}
\]

Thus, as causal distributions,

\[
\boxed{
P_\Box(\tau)H
=(\partial_t^2+\partial_t)^2W_5.
}
\tag{L-32303.10}
\]

This simultaneously extends the positive compact Green factor of PR #263 and the carry-localizing filter of `L-32302`.

## 4. Compact carry geometry

Let the coefficient expansion be

\[
P_\Box(x)=\sum_{j=0}^5c_jx^j.
\]

Because `P_Box(1)=0`, the source-contracted floor primitive

\[
g_m(y)=\sum_{2^j m\le y}c_j
\]

vanishes once `y>=32m`.  Therefore the pointwise source-contracted carry is the compact wavelet

\[
\boxed{
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j),
\qquad
\operatorname{supp}g_m\subset[m,32m).
}
\tag{L-32303.11]
\]

(the bracket typo in the tag is typographical only).

Because `P_Box(2)=0`, the affine Möbius carry contraction also vanishes after every tap is active:

\[
\boxed{
\sum_{q=2}^n b_\Box(q)\beta_{nq}=0
\qquad(n\ge32).
}
\tag{L-32303.12}
\]

Thus the complete averaged carry source has only thirty finite bottom rows.

## 5. What the five-mode filter actually repairs

The filter removes four distinct false-shortcut modes before any positivity assertion:

```text
long constant floor tail;
long affine carry tail;
continuous e^t pole model;
continuous e^(t/2), t e^(t/2) half-pole model.
```

It does **not** remove the arithmetic odd-Möbius source: on odd integers the finite dyadic filter leaves the original Möbius coefficient.  Same-sign odd Möbius cubes remain a mandatory mutation.

## 6. Correct research interface

A completion based on this source would need only a source-specific estimate for the finite bottom/transition bank and the independent-frequency reflected channel.  Generic positivity of a compact B-spline or a rank-one parity Gram is not asserted.

The advantage over the earlier filters is exact compatibility of all currently known annihilation requirements in one source with a positive inverse.

## 7. Proof boundary

Closed exactly:

- all five finite Euler factors and their roles;
- off-line pole preservation;
- positive inverse coefficients;
- positive generalized-prime coefficients;
- positive compact five-window Green factorization;
- factor-32 pointwise carry localization;
- exact vanishing of averaged carry rows above 31.

Open:

- the finite source-specific transition estimate;
- an independent-frequency reflected reserve for the complete source;
- RH.
