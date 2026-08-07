# L-15444 — Bohr diagonalization of the gauged Chebyshev second difference

Claim ID: `L-15444`  
Title: In the global coefficient metric, the Selberg–Mourre form is diagonal and its complete negative part is a finite first-prime boundary charge  
Status: `PROPOSED — EXACT DIRICHLET-COEFFICIENT IDENTITY; LOCAL PHYSICAL EMBEDDING OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15443`; Carlson/Bohr mean orthogonality for absolutely square-summable Dirichlet coefficients  
Cross-route connections: PR #158 `M-15110`; PRs #216/#222/#224; PR #218 half-knot debt  
Scope: the actual integer-dilation Chebyshev source; this is not a local Hardy estimate and does not prove RH

## 1. Gauged source coefficients

Fix an integer

\[
a\ge2,
\qquad
\ell=\log a.
\tag{L-15444.1}
\]

For the actual Chebyshev second-difference ray of `L-15443`,

\[
G_a(z)
=(1-a^{-z})(1-a^{-z-1/2})[-\zeta'(1+z)].
\tag{L-15444.2}
\]

Since

\[
-\zeta'(1+z)
=\sum_{n\ge2}{\log n\over n}n^{-z}
\qquad(\Re z>0),
\tag{L-15444.3}
\]

one has the exact Dirichlet expansion

\[
\boxed{
G_a(z)=\sum_{n\ge2}b_a(n)n^{-z},}
\tag{L-15444.4}
\]

where

\[
\boxed{
\begin{aligned}
b_a(n)={1\over n}\Big[&\log n
-(a+\sqrt a)\mathbf1_{a\mid n}\log(n/a)\\
&+a^{3/2}\mathbf1_{a^2\mid n}\log(n/a^2)\Big].
\end{aligned}}
\tag{L-15444.5}
\]

For the scale-four route,

\[
\boxed{
b_4(n)={\log n-6\mathbf1_{4\mid n}\log(n/4)
+8\mathbf1_{16\mid n}\log(n/16)\over n}.}
\tag{L-15444.6}
\]

These are exactly the integer coefficients underlying the finite numerator in `L-15148`.

## 2. Global Bohr-mean diagonalization

Fix `sigma>0` and put

\[
c=-{1\over2}+\sigma.
\tag{L-15444.7}
\]

The coefficient sequence in (L-15444.4) is square summable with weight `n^(-2c)` because `b_a(n)=O_a((log n)/n)`. Carlson/Bohr orthogonality gives

\[
\lim_{T\to\infty}{1\over2T}
\int_{-T}^T
 n^{-it}m^{it}\,dt
=\mathbf1_{n=m}.
\tag{L-15444.8}
\]

Since differentiating `n^{-z}` multiplies it by `-log n`,

\[
G_a''(z)+\ell G_a'(z)
=\sum_{n\ge2}
\log n(\log n-\ell)b_a(n)n^{-z}.
\tag{L-15444.9}
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathfrak Q_{a,\sigma}^{\rm Bohr}
&:=\lim_{T\to\infty}{1\over2T}\operatorname{Re}
\int_{-T}^T
\overline{G_a(c+it)}
[G_a''+\ell G_a'](c+it)dt\\
&=\sum_{n\ge2}
\log n(\log n-\ell)|b_a(n)|^2n^{1-2\sigma}.
\end{aligned}}
\tag{L-15444.10}
\]

This is the coefficient-space version of the physical logarithmic identity in `L-15443`.

## 3. Complete sign ledger

For every integer `n`:

\[
\log n(\log n-\ell)
\begin{cases}
<0,&2\le n<a,\\
=0,&n=a,\\
>0,&n>a.
\end{cases}
\tag{L-15444.11}
\]

Hence the entire negative part of (L-15444.10) is finite:

\[
\boxed{
\mathfrak Q_{a,\sigma}^{\rm Bohr}
\ge
-\sum_{2\le n<a}
\log n(\ell-\log n)|b_a(n)|^2n^{1-2\sigma}.}
\tag{L-15444.12}
\]

For `n<a`, no dilation term is active, so `b_a(n)=log(n)/n`. Thus

\[
\boxed{
\mathfrak Q_{a,\sigma}^{\rm Bohr}
\ge
-\sum_{2\le n<a}
{(\log n)^3(\log a-\log n)\over n^{1+2\sigma}}.}
\tag{L-15444.13}
\]

The right side is a fixed finite boundary constant, uniformly in the cofinal truncation.

At scale four only two integers occur:

\[
\boxed{
\mathfrak Q_{4,\sigma}^{\rm Bohr}
\ge
-{(\log2)^3\log2\over2^{1+2\sigma}}
-{(\log3)^3\log(4/3)\over3^{1+2\sigma}}.}
\tag{L-15444.14}
\]

Thus the complete proposed endpoint lower bound of the Selberg–Mourre programme is already closed—indeed constant—in the global coefficient/gauge metric.

## 4. Why this does not yet prove the local prime-energy theorem

The RH-bearing norm is not the Bohr mean in (L-15444.10). It is a local or compactly weighted identity-orbit integral such as

\[
\int_{\mathbb R}
|\widehat H(\sigma+it)|^2
|P_1(1/2+\sigma+it)|^2dt,
\tag{L-15444.15}
\]

or its physical Chebyshev square-function equivalent.

On a local vertical interval, distinct phases `n^{-it}` are not orthogonal. Their off-diagonal interaction is exponentially larger than the final energy and supplies the complete RH-scale cancellation. `R-22301` on PR #224 proves that no universal Dirichlet-Hardy-to-identity-orbit embedding can convert a coefficient norm into (L-15444.15).

Therefore the implication

```text
Bohr/gauge diagonal positivity
=> local physical prime-energy bound
```

is invalid without special arithmetic input.

## 5. Exact interpretation of the current full-proof proposals

### PR #158

`M-15110.17/.18` should be separated into two layers:

1. the global coefficient/gauged bulk and endpoint sign, already given exactly by (L-15444.10)--(L-15444.14);
2. a restricted local-to-Bohr or gauge-to-physical estimate for the actual Chebyshev source.

Only the second layer can prove RH.

### PRs #216/#222

The bounded-ratio signed semiprime form is precisely the off-diagonal correction discarded by the Bohr limit. A successful common-cell dispersion estimate supplies the missing local conversion.

### PR #224

The critical `H1` convolution-square criterion is another exact formulation of the same local conversion. Its universal embedding no-go is fully consistent with (L-15444.10): coefficient positivity is true but insufficient.

### PR #218

The finite negative boundary in (L-15444.13) is the logarithmic-coordinate analogue of the unavoidable first-prime debt in the sharp half-knot theorem. Both say that a positive finite filter cannot eliminate the boundary charge; it can only transport it into the positive bulk.

## 6. New smallest theorem

After `L-15443/L-15444`, the combined Selberg–Mourre/prime-Hardy programme no longer needs a conjectural global Selberg bulk factorization. It needs one ray-specific estimate:

\[
\boxed{
\text{local identity-orbit energy of the actual filtered prime ray}
\ \le\ \operatorname{poly}(X)
\times
\bigl(1+\text{its gauged/Bohr energy}\bigr).}
\tag{L-15444.16}
\]

Any subexponential version sufficient for the Hardy exponent proves RH. The universal version is false; the arithmetic prime/semiprime structure must enter.

## 7. Proof boundary

Closed exactly:

- coefficient formula (L-15444.5);
- scale-four specialization;
- Bohr diagonal identity (L-15444.10);
- finite complete negative ledger (L-15444.13);
- the distinction between global coefficient and local identity-orbit metrics.

Open:

- the ray-specific local-to-Bohr estimate (L-15444.16);
- the signed semiprime/Carleson estimate proposed on PRs #222/#224;
- the physical-norm polynomial inverse required by PR #158.

This lemma does not prove RH. It closes the bulk and endpoint pieces only in the exact metric where they are genuinely diagonal.