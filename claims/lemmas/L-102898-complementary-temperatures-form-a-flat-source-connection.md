# L-102898 — Complementary completion temperatures form a flat source connection

Claim ID: `L-102898`  
Status: **PROVED EXACT SOURCE/KERNEL IDENTITY**  
Created: 2026-08-24  
Depends on: `L-102892--L-102897`; `L-102701`; PR #715 common mother  
RH status: **not assumed**

Work in the finite labelled Euler algebra before physical collapse.  The two
copies of \(67\) remain distinct labels.  For a real or complex parameter
\(t\), define

\[
\boxed{
\sigma_t
=
\prod_{\ell}
(1-x_\ell)(1+x_\ell)^t,
\qquad
x_\ell=p_\ell^{-1/2}U_\ell.
}
\tag{L-102898.1}
\]

Every identity below is coefficientwise on a finite horizon, so the binomial
series is finite in each physical coefficient.

Let

\[
\Gamma_{1/2}:=\sigma_{1/2}*\sigma_{1/2}
=\eta*\eta
=\beta*\beta^\square.
\]

## 1. Exact complementary-temperature factorization

At one labelled prime,

\[
(1-x)(1+x)^t\,
(1-x)(1+x)^{1-t}
=
(1-x)^2(1+x).
\]

Hence, for every \(t\),

\[
\boxed{
\sigma_t*\sigma_{1-t}
=
\Gamma_{1/2}.
}
\tag{L-102898.2}
\]

This includes the three distinguished gauges

```text
t=0:      native source × squared completion;
t=1/2:    geometric midpoint × itself;
t=1:      squared completion × native source.
```

The detector-bearing product source is independent of the temperature split.

## 2. Flat connection and tangent cancellation

Put

\[
\Lambda
=
\sum_{\ell}\log(1+x_\ell),
\]

where the logarithm is its finite-horizon formal series.  Then

\[
\partial_t\sigma_t=\sigma_t*\Lambda.
\tag{L-102898.3}
\]

Differentiating (L-102898.2) gives the exact flatness identity

\[
\boxed{
(\partial_t\sigma_t)*\sigma_{1-t}
=
\sigma_t*(\partial_s\sigma_s)|_{s=1-t}.
}
\tag{L-102898.4}
\]

Equivalently, the antisymmetric tensor current

\[
\boxed{
\mathcal W_t
=
(\partial_t\sigma_t)\otimes\sigma_{1-t}
-
\sigma_t\otimes(\partial_s\sigma_s)|_{s=1-t}
}
\tag{L-102898.5}
\]

belongs to the kernel of arithmetic convolution.

At the midpoint,

\[
\mathcal W_{1/2}
=
\dot\eta\otimes\eta-\eta\otimes\dot\eta.
\]

In the free labelled tensor Hilbert space it is also orthogonal to the
symmetric source vector:

\[
\boxed{
\langle \eta\otimes\eta,\mathcal W_{1/2}\rangle=0.
}
\tag{L-102898.6}
\]

Thus the temperature direction is a genuine gauge-null direction before
physical collapse.

## 3. Complex complementary line

For every real \(\tau\),

\[
\boxed{
\sigma_{1/2+i\tau}*\sigma_{1/2-i\tau}
=
\Gamma_{1/2}.
}
\tag{L-102898.7}
\]

On the real Euler half-line the two factors are coefficientwise conjugate.
The midpoint square therefore admits a fixed complex-temperature polarization
without changing its arithmetic source, detector, or hypothetical pole set.

## 4. Common-mother physical current

Let \(A\) and \(A_-=(D-\tfrac12)A\) be the ratio-four kernels of
`L-102701`, so that

\[
\Phi_*=2A_-*_M A.
\]

Define

\[
F_{t,-}(Y)
=
\sum_n\frac{\sigma_t(n)}{\sqrt n}A_-(Y/n),
\]

\[
F_{1-t,+}(Z)
=
\sum_m\frac{\sigma_{1-t}(m)}{\sqrt m}A(Z/m).
\]

Finite arithmetic and Mellin Fubini give, for every \(t\),

\[
\boxed{
H_{\Gamma_{1/2},\Phi_*}(X)
=
2\int_0^\infty
F_{t,-}(Y)F_{1-t,+}(X/Y)\frac{dY}{Y}.
}
\tag{L-102898.8}
\]

Differentiating under the finite integral yields the exact Wronskian
conservation law

\[
\boxed{
\int_0^\infty
\left[
\dot F_{t,-}(Y)F_{1-t,+}(X/Y)
-
F_{t,-}(Y)\dot F_{1-t,+}(X/Y)
\right]\frac{dY}{Y}
=0.
}
\tag{L-102898.9}
\]

Every fixed scale derivative, dyadic filter, outer-ray operator, owner
projection and source-owned regional projection commutes with this identity.

## Meaning

The geometric midpoint is not an isolated factorization.  It lies on a flat
one-parameter family of exact polarized factorizations of the same
conclusion-bearing source.  Different source regions may use different
complementary temperatures provided each region is assigned exactly once.
No source, terminal packet, or positive reserve is duplicated.
