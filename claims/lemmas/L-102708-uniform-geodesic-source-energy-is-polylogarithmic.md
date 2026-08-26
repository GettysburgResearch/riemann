# L-102708 — Uniform geodesic and tangent source energies are polylogarithmic

Claim ID: `L-102708`  
Status: **PROVED UNCONDITIONALLY AT LABELLED/SAME-PRODUCT SCOPE**  
Created: 2026-08-22  
Depends on: `L-102707`; PR #719 `L-102702`  
RH status: **not assumed**

Let

\[
\ell_\tau(x)
=\tau\sqrt{1-x}+(1-\tau)\sqrt{1-x^2}
=\sum_{k\ge0}a_{\tau,k}x^k.
\]

Uniformly for `0<=tau<=1`,

\[
a_{\tau,0}=1,
\qquad
a_{\tau,1}=-\frac\tau2,
\qquad
|a_{\tau,k}|\ll k^{-3/2}\quad(k\ge2).
\]

Therefore, for every ordinary prime,

\[
\boxed{
\sum_{k\ge0}\frac{|a_{\tau,k}|^2}{p^k}
=1+\frac{\tau^2}{4p}+O(p^{-2}),
}
\tag{L-102708.1}
\]

uniformly in `tau`.

Let `Lambda_tau` be the complete labelled source of `L-102707`.  Euler-product
comparison gives

\[
\boxed{
\sum_{n\le Y}\frac{|\Lambda_\tau(n)|^2}{n}
\ll
(\log(2Y))^{\tau^2/4}
\le(\log(2Y))^{1/4}.
}
\tag{L-102708.2}
\]

The second labelled `67` changes only the implied constant.

## Tangent energy

For one local Hilbert vector `v_p(tau)` of coefficients
`a_(tau,k)p^(-k/2)`, decompose its derivative into the component parallel to
`v_p` and the orthogonal component.  Uniformly,

\[
\frac{\langle v_p',v_p\rangle}{\|v_p\|^2}
=\frac{\tau}{4p}+O(p^{-2}),
\]

and

\[
\frac{\|v_p'\|^2}{\|v_p\|^2}
\ll\frac1p.
\]

Differentiating the tensor product and using orthogonality of distinct local
orthogonal components yields

\[
\boxed{
\sum_{n\le Y}\frac{|\dot\Lambda_\tau(n)|^2}{n}
\ll
(\log(2Y))^{1/4}(\log\log(3Y))^2.
}
\tag{L-102708.3}
\]

This bound is uniform in `tau`.

## Same-product collapse

For the convolution coefficients

\[
\Delta_\tau=\dot\Lambda_\tau*\Lambda_\tau,
\]

factor-pair Cauchy and the uniform divisor bound give

\[
\boxed{
\sum_{n\le Y}\frac{|\Delta_\tau(n)|^2}{n}
=Y^{o(1)}
}
\tag{L-102708.4}
\]

uniformly in `tau`. Integrating over `tau` preserves the subpower bound.

Thus the continuous geodesic introduces no new labelled diagonal or
same-product multiplicity obstruction.  The remaining term is still the
physical overlap of distinct products—now in a root-free polarized current
uniformly parameterized by `tau`.