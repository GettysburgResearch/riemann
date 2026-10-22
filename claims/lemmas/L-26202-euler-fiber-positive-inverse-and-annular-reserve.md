# L-26202 — Positive inverse, sign-complete dyadic fiber, and strict annular reserve

Claim ID: `L-26202`  
Status: `PROPOSED COMPLETE — exact Dirichlet algebra and Fourier-multiplier reserve pending independent review`  
Scope: source-specific reflected interface for `L-26201`  
Date: 2026-08-08  
Depends on: `L-26201`; corrected generalized Selberg sign convention in PR #241

Retain

\[
P(s)=(1-2^{1-s})(1-2^{1/2-s})^2,
\qquad
B_{\mathcal E}(s)=\frac{P(s)}{\zeta(s)}.
\tag{L-26202.1}
\]

## 1. Positive inverse coefficients

Define

\[
\boxed{
A_{\mathcal E}(s)=B_{\mathcal E}(s)^{-1}
=\frac{\zeta(s)}
 {(1-2^{1-s})(1-2^{1/2-s})^2}.}
\tag{L-26202.2}
\]

At every odd prime, the local coefficients of `A_E` are all one.  At the prime two, put `z=2^(-s)`.  The local factor is

\[
\frac1{(1-z)(1-2z)(1-\sqrt2 z)^2}.
\tag{L-26202.3}
\]

Hence, if `n=2^nu m` with `m` odd,

\[
\boxed{
 a_{\mathcal E}(n)
 =\sum_{\substack{j,k\ge0\\j+k\le\nu}}
 2^j(k+1)2^{k/2}>0.}
\tag{L-26202.4}
\]

In particular,

\[
\boxed{a_{\mathcal E}(n)>0\qquad(n\ge1),}
\tag{L-26202.5}
\]

and

\[
a_{\mathcal E}*b_{\mathcal E}=\varepsilon.
\tag{L-26202.6}
\]

This is a fixed positive inverse.  No conjectural carry-profile sign is being assumed.

## 2. Positive generalized prime sequence

Let `Lambda_E^#` be defined by

\[
-\frac{A_{\mathcal E}'}{A_{\mathcal E}}(s)
=\sum_{n\ge1}\frac{\Lambda_{\mathcal E}^{\#}(n)}{n^s}.
\tag{L-26202.7}
\]

Taking logarithmic derivatives of (L-26202.2) gives

\[
\boxed{
\Lambda_{\mathcal E}^{\#}(n)
=\Lambda(n)
 +(\log2)
 \left(2^k+2^{k/2+1}\right)
 \mathbf1_{n=2^k,\ k\ge1}.}
\tag{L-26202.8}
\]

Thus

\[
\boxed{
\Lambda_{\mathcal E}^{\#}(n)\ge0.}
\tag{L-26202.9}
\]

Using the corrected sign convention for a Dirichlet series and its inverse, the exact Selberg coefficient identity is

\[
\boxed{
 b_{\mathcal E}*(a_{\mathcal E}\log^2)
 =\Lambda_{\mathcal E}^{\#}\log
  +\Lambda_{\mathcal E}^{\#}*
   \Lambda_{\mathcal E}^{\#}.}
\tag{L-26202.10}
\]

Every coefficient on the right is nonnegative.

The reflected conjugate-product subtraction therefore supplies the exact Hermitian square

\[
2\left|\frac{A_{\mathcal E}'}{A_{\mathcal E}}
 (\sigma+it)\right|^2
=\mathcal C_{\times}(\sigma,t)
 -\mathcal C_+(\sigma,t)
 -\mathcal C_-(\sigma,t),
\tag{L-26202.11}
\]

with the complete source retained.  PR #241 gives the correct two-frequency physical-block realization of this equality.

## 3. The fixed sign-complete two-adic fiber

For odd `m`, multiplicativity gives

\[
 b_{\mathcal E}(2^\nu m)=\mu(m)p_\nu,
\tag{L-26202.12}
\]

where the local polynomial is

\[
\boxed{
\begin{aligned}
p(z)
&=(1-z)(1-2z)(1-\sqrt2 z)^2\\
&=1-(3+2\sqrt2)z
 +(4+6\sqrt2)z^2\\
&\quad -(6+4\sqrt2)z^3+4z^4.
\end{aligned}}
\tag{L-26202.13}
\]

Thus every odd Möbius coefficient sits in one explicit five-tap fiber.  The roots encode exactly the source moments

\[
p(1)=0,
\qquad
p(1/2)=0,
\qquad
p(1/\sqrt2)=p'(1/\sqrt2)=0.
\tag{L-26202.14}
\]

They are, respectively,

```text
Möbius inversion mass,

pole-model cancellation,

double half-pole cancellation.
```

This gives a bounded sign-complete companion family for every same-sign odd-prime Möbius cube.  It does not assert that the resulting reflected block is automatically coercive; it provides the exact fixed source on which that question must be decided.

## 4. Strict annular multiplier reserve

Fix

\[
0<\eta<\frac14
\]

and let

\[
\frac12+\eta\le\sigma\le1-\eta.
\tag{L-26202.15}
\]

For every real `t`, reverse triangle inequalities give

\[
\begin{aligned}
|1-2^{1-\sigma-it}|
&\ge 2^\eta-1,\\
|1-2^{1/2-\sigma-it}|
&\ge1-2^{-\eta}.
\end{aligned}
\tag{L-26202.16}
\]

Consequently

\[
\boxed{
|P(\sigma+it)|
\ge
\kappa_\eta,
\qquad
\kappa_\eta
=(2^\eta-1)(1-2^{-\eta})^2>0.}
\tag{L-26202.17}
\]

For every measurable vertical-line profile `F`, this yields the exact source-specific reserve

\[
\boxed{
\int_{\mathbb R}|P(\sigma+it)F(t)|^2dt
\ge
\kappa_\eta^2
\int_{\mathbb R}|F(t)|^2dt.}
\tag{L-26202.18}
\]

In particular, on compact substrips, an upper bound for the Euler-filtered inverse-zeta source controls the unfiltered source with one explicit constant.  This is a genuine strict reserve, not a dimension count or a synthetic Schur example.

## 5. Why the reserve is correctly scoped

The reserve does **not** prove an upper bound for the filtered source.  It proves that a successful reflected estimate on the new source cannot have discarded the RH-bearing mode.

It also survives the mandatory mutations:

1. `P` has no zero in `1/2<Re s<1`;
2. odd Möbius coefficients are unchanged;
3. the two-adic fiber has fixed length five;
4. the reserve is uniform in the vertical frequency;
5. no arbitrary-vector Farey or Bohr operator norm is invoked.

## 6. Proof boundary

Closed in this claim:

- coefficientwise positivity of the exact inverse;
- coefficientwise positivity of the generalized prime sequence;
- the exact Selberg forcing identity;
- the five-tap two-adic source fiber;
- the explicit strict annular reserve.

Not closed:

- a physical-block upper estimate from the reflected identity;
- a strict lower-scale recurrence;
- RH.
