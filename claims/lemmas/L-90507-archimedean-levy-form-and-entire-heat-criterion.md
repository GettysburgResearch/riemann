# L-90507 — The pole-null Weil form is a Lévy–prime competition and RH has an entire heat-trace criterion

Claim ID: `L-90507`  
Status: **PROPOSED COMPLETE EXACT FORM / SPECTRAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90506`; the standard digamma integral; trace-class spectral calculus  
Scope: exact archimedean jump form, a modulus inequality, and a one-parameter heat criterion; no proof of the required sign

## 1. Digamma as a Lévy symbol

Recall

\[
 \mu(\tau)
 =\frac1{2\pi}
 \Re\psi\!\left(\frac14+\frac{i\tau}{2}\right)
 -\frac{\log\pi}{2\pi},
 \tag{L-90507.1}
\]

where `psi=Gamma'/Gamma`. The standard integral identity

\[
 \Re\psi(a+it)-\psi(a)
 =\int_0^\infty
 \frac{e^{-ax}[1-\cos(tx)]}{1-e^{-x}}\,dx
 \tag{L-90507.2}
\]

gives, after `x=2y`,

\[
 \boxed{
 \mu(\tau)-\mu(0)
 =\frac1\pi\int_0^\infty
 \frac{e^{-y/2}}{1-e^{-2y}}
 [1-\cos(\tau y)]\,dy.
 }
 \tag{L-90507.3}
\]

Thus `mu(tau)-mu(0)` is a complete Bernstein function of `tau^2` and the characteristic exponent of a symmetric pure-jump process.

The constant is explicit:

\[
 2\pi\mu(0)
 =\psi(1/4)-\log\pi
 =-\gamma-\frac\pi2-3\log2-\log\pi<0.
 \tag{L-90507.4}
\]

## 2. Exact physical-space form

Use the Fourier convention

\[
 \widehat f(\tau)=\int f(u)e^{i\tau u}\,du.
\]

Plancherel and (L-90507.3) imply

\[
 \boxed{
 \int_{\mathbb R}
 [\mu(\tau)-\mu(0)]|\widehat f(\tau)|^2\,d\tau
 =\int_0^\infty
 \frac{e^{-y/2}}{1-e^{-2y}}
 \|f-T_yf\|_2^2\,dy.
 }
 \tag{L-90507.5}
\]

For an exponentially confined admissible `f`, the complete prime sum is absolutely convergent. On the pole-null space `N` of `L-90506`, the explicit formula becomes

\[
\boxed{
\begin{aligned}
 W(f,f)={}&
 \int_0^\infty
 \frac{e^{-y/2}}{1-e^{-2y}}
 \|f-T_yf\|_2^2\,dy\\
 &+2\pi\mu(0)\|f\|_2^2
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \Re\langle f,T_{\log n}f\rangle.
\end{aligned}}
 \tag{L-90507.6}
}

No pole term remains. The first line is a positive continuum jump energy; the last line is a discrete prime-power adjacency.

## 3. Diamagnetic inequality for the pole-free form

For every shift `y`,

\[
 ||f(u)|-|f(u-y)||\le|f(u)-f(u-y)|
 \tag{L-90507.7}
\]

pointwise, and

\[
 \Re\langle f,T_yf\rangle
 \le\langle |f|,T_y|f|\rangle.
 \tag{L-90507.8}
\]

The mass term is unchanged. Hence the right side of (L-90507.6), viewed as the pole-free quadratic form `Q`, satisfies

\[
 \boxed{Q(|f|)\le Q(f)}
 \tag{L-90507.9}
\]

on its natural closed form domain. Smooth compact approximation extends the statement through zeros of `f`.

This is a genuine structural gain: after the two pole coordinates are removed, the dangerous spectral problem is a positivity-preserving Lévy–prime competition rather than a generic indefinite matrix.

It does not by itself prove `Q|_N>=0`, because the pole-null constraints are not preserved by absolute value.

## 4. Entire heat trace

Let `A^(0)` be the pole-null trace-class operator of `L-90506`. Define

\[
 \boxed{
 \Theta_a(\beta)
 =\operatorname{tr}(e^{-\beta A^{(0)}}-I),
 \qquad \beta\in\mathbb C.
 }
 \tag{L-90507.10}
\]

Since `A^(0)` is trace class and bounded, `e^{-beta A^(0)}-I` is trace class and `Theta_a` is entire. If `lambda_j` are the eigenvalues,

\[
 \Theta_a(\beta)
 =\sum_j(e^{-\beta\lambda_j}-1).
 \tag{L-90507.11}
\]

If `A^(0)>=0`, then

\[
 \Theta_a(\beta)\le0
 \qquad(\beta>0).
 \tag{L-90507.12}
\]

Conversely, suppose `lambda_*<0` is the lowest eigenvalue, of multiplicity `m`. The positive-spectrum contribution obeys

\[
 \sum_{\lambda_j>0}(e^{-\beta\lambda_j}-1)
 \ge-\beta\operatorname{tr}(A_+).
\]

Therefore

\[
 \Theta_a(\beta)
 \ge m(e^{\beta|\lambda_*|}-1)
 -\beta\operatorname{tr}(A_+)
 \longrightarrow+\infty.
 \tag{L-90507.13}
\]

Hence

\[
 \boxed{
 A^{(0)}\succeq0
 \iff
 \Theta_a(\beta)\le0\quad\forall\beta>0.
 }
 \tag{L-90507.14}
\]

Equivalently,

\[
 \boxed{
 \operatorname{tr}
 [A^{(0)}e^{-\beta A^{(0)}}]\ge0
 \quad\forall\beta>0.
 }
 \tag{L-90507.15}
\]

A single arbitrarily small negative eigenvalue is exponentially amplified as `beta->infinity`.

## 5. Global prime-word expansion

Let

\[
 m_k^{(0)}=\operatorname{tr}[(A^{(0)})^k].
\]

The heat trace has the globally convergent expansion

\[
 \boxed{
 \Theta_a(\beta)
 =\sum_{k\ge1}
 \frac{(-\beta)^k}{k!}m_k^{(0)}.
 }
 \tag{L-90507.16}
\]

Indeed

\[
 |m_k^{(0)}|
 \le\|A^{(0)}\|^{k-1}\|A^{(0)}\|_1.
\]

Substituting the absolutely trace-norm convergent explicit-formula expansion gives an absolutely convergent all-order prime-word series for every complex `beta`. This improves on the local cumulant expansion of `log det(I+tA)`, whose power series is confined to `|t|<||A||^{-1}`.

Under positivity, the determinant and heat trace are linked by

\[
 \boxed{
 \log\det(I+tA^{(0)})
 =-\int_0^\infty
 \frac{e^{-s}}s\,
 \Theta_a(ts)\,ds
 \qquad(t>0).
 }
 \tag{L-90507.17}
\]

## 6. Proof boundary

Proved here:

- the exact Lévy-Khinchine formula for the gamma factor;
- the physical jump-energy identity;
- an exact pole-null Lévy–prime representation;
- a diamagnetic inequality for the pole-free form;
- an entire one-parameter heat-trace criterion equivalent to positivity;
- a globally convergent all-order prime-word expansion.

Not proved:

- nonpositivity of `Theta_a(beta)`;
- a Feynman-Kac or polymer domination theorem strong enough to imply it;
- RH.
