# Audit of the apparent Thorin/GGC shortcut to the central xi law

Agent: `gpt56-pro-global-01`  
Date: 2026-08-07  
Status: **scope audit; no RH claim**

## Target under review

An apparent shortcut to the final Brownian saturation is to argue that the
half-tilted Brownian/gamma log law has a positive Thorin or generalized gamma
convolution representation.  If that representation extended to the center with
a positive measure, one might hope to obtain total positivity or a real-zero
Mellin transform.

The accessible Polson manuscript `arXiv:1804.10043v8` does not establish that
central continuation.

## 1. The displayed algebraic continuation step is false

The manuscript's equation (30) uses the claimed identity

\[
e^{-\sigma t}
=
\exp\left(
-\frac{\sqrt{1+\sigma}-1}{\sqrt{1+\sigma}+1}\,2t
\right)
\exp\left(-\bigl((\sqrt{1+\sigma})^2-1\bigr)t\right).
\tag{1}
\]

But

\[
(\sqrt{1+\sigma})^2-1=\sigma.
\]

Therefore the second factor on the right of (1) is already `e^(-sigma t)`.
Equation (1) would require

\[
\exp\left(
-\frac{\sqrt{1+\sigma}-1}{\sqrt{1+\sigma}+1}\,2t
\right)=1
\]

for all positive `sigma,t`, which is false.

The subsequent measure transformation depending on (1) therefore cannot be
used as a proof of the central Thorin representation.

## 2. Holomorphy at the center is the RH-bearing step

A Thorin or Stieltjes representation in the ordinary Euler-product half-plane is
compatible with known zero-free regions there.  Extending it to the centered
argument requires a holomorphic positive-measure representation across the
critical strip.

If such a representation supplied the claimed centered zero-free or
Laguerre--Polya consequence, it would already exclude the off-line poles whose
absence is RH.  The continuation cannot be treated as a routine closure of the
off-center GGC theorem.

## 3. Bernstein-function closure does not repair the gap

One tempting repair introduces

\[
u(\sigma)=\bigl(\sqrt{1+\sigma}-1\bigr)^2.
\]

Direct differentiation gives

\[
u''(\sigma)>0
\qquad(\sigma>0),
\]

whereas a Bernstein function must have completely monotone derivative and hence
nonpositive second derivative.  Thus the standard Bernstein-composition closure
cannot be invoked for this map.

## 4. Additive GGC versus multiplicative Mellin zeros

The BPY variable

\[
\Sigma_2=\frac2{\pi^2}
 \sum_{n\ge1}\frac{\Gamma(2)_n}{n^2}
\]

is indeed an additive generalized gamma convolution.  The RH endpoint concerns

\[
\mathbb E_{1/4}^{\Sigma}
 [e^{it\log\Sigma_2}],
\]

which is a Mellin/Fourier transform of the logarithm under fractional size bias.
There is no general implication

```text
additive GGC
=> fractional-size-biased logarithm is PF_infinity
=> Mellin transform has only critical-line zeros.
```

Such an implication here would itself prove RH and therefore requires a theorem
special to this exact gamma sequence, not generic GGC terminology.

## 5. Consequence for PR #217

The final saturation chain must retain the explicit open statement

\[
\operatorname{Var}^{\Sigma}_{1/4}(\log\Sigma_2)
\le
8\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.
\]

Neither the erroneous identity (1), the off-center Thorin result, nor a
Bernstein-composition argument proves this inequality.

## Verdict

The Brownian/gamma representation is valuable and exact.  The proposed central
Thorin shortcut is not presently a proof of SAT.  Any replacement must establish
one of the following independently:

- the reverse variance inequality;
- the `Z+C <=cx U` martingale transport;
- a valid central positive Thorin representation with all analytic continuation
  and measure-positivity steps proved;
- the corrected completed prime-annihilator identity.

Until then, the central GGC/Thorin step remains RH-bearing rather than an
available lemma.