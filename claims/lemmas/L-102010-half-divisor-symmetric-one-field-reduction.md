# L-102010 — Positive half-divisor completion reduces the two-field packet to one field energy

Claim ID: `L-102010`
Status: **PROVED EXACT SYMMETRIZATION AND HARDY REDUCTION; FINAL ENERGY OPEN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: `L-102009`
RH status: **not assumed**

Let `eta` be the nonnegative multiplicative function determined by

\[
\sum_{k\ge0}\eta(p^k)z^k=(1-z)^{-1/2},
\qquad
\eta(p^k)=\frac{\binom{2k}{k}}{4^k}.
\tag{L-102010.1}
\]

Coefficient comparison in

\[
(1-z)^{-1/2}(1-z)^{-1/2}=(1-z)^{-1}
\]

gives the exact Dirichlet-convolution identity

\[
\boxed{\eta*\eta=\mathbf1.}
\tag{L-102010.2}
\]

Retain

\[
b_U(n)=\mu(n)\mathbf1_{n>U}
\]

and define the positively half-completed tail

\[
\boxed{h_U=b_U*\eta.}
\tag{L-102010.3}
\]

Since `a_U*a_U*mu=b_U*b_U*1` by `L-102009`, one has

\[
\boxed{a_U*a_U*\mu=h_U*h_U.}
\tag{L-102010.4}
\]

Thus the two source factors may be chosen identical.

## Symmetric ratio-four fields

With the ratio-four kernels `A_-`, `A_+` of `L-102009`, put

\[
H_{U,-}(Y)
=\sum_{n\ge1}\frac{h_U(n)}{\sqrt n}A_-(Y/n),
\tag{L-102010.5}
\]

\[
H_{U,+}(Y)
=\sum_{n\ge1}\frac{h_U(n)}{\sqrt n}A_+(Y/n).
\tag{L-102010.6}
\]

Both sums are finite at each endpoint, and `h_U(n)=0` for `n<=U`. From
`h_U*h_U=a_U*a_U*mu` and `K_1=A_-*_M A_+`,

\[
\boxed{
\mathcal B_U(X)
=\int_U^{X/U}
H_{U,-}(Y)H_{U,+}(X/Y)\frac{dY}{Y}.
}
\tag{L-102010.7}
\]

## Exact Hardy relation between the kernels

Write the kernels in logarithmic coordinate. Since

\[
A_-=(D-1/2)A,
\qquad
A_+=(D+3/2)A=A_-+2A,
\]

and `A` is compactly supported, the right-boundary Green formula is

\[
A(u)
=-\int_0^\infty e^{-t/2}A_-(u+t)\,dt.
\tag{L-102010.8}
\]

Define

\[
(\mathcal Tf)(u)=\int_0^\infty e^{-t/2}f(u+t)\,dt.
\]

Then

\[
\boxed{A_+=A_--2\mathcal TA_-.}
\tag{L-102010.9}
\]

On the Fourier line, `mathcal T` has multiplier

\[
\frac1{1/2-i\xi}.
\]

Therefore `I-2mathcal T` has multiplier

\[
\frac{-3/2-i\xi}{1/2-i\xi},
\]

whose modulus is at most `3`, with equality at `xi=0`. Plancherel gives the
sharp full-line bound

\[
\boxed{
\|f-2\mathcal Tf\|_{L^2(du)}\le3\|f\|_{L^2(du)}.
}
\tag{L-102010.10}
\]

The relation commutes with every source translation.

## Finite-endpoint localization

For the integral (L-102010.7), only values in

\[
I_X=[U,X/U]
\]

are observed. Truncate `h_U` at `n<=X/U`; this changes neither field on
`I_X`, because `A_-` and `A_+` are supported on `[1,4]`. The truncated minus
field is supported in

\[
I_X^+=[U,4X/U].
\]

Applying (L-102010.10) to this finite field gives

\[
\boxed{
\|H_{U,+}\|_{L^2(I_X,dY/Y)}
\le3\|H_{U,-}\|_{L^2(I_X^+,dY/Y)}.
}
\tag{L-102010.11}
\]

Define the single field energy

\[
\boxed{
\mathcal H_U(X)
=\int_U^{4X/U}|H_{U,-}(Y)|^2\frac{dY}{Y}.
}
\tag{L-102010.12}
\]

Cauchy--Schwarz in (L-102010.7), followed by (L-102010.11), yields

\[
\boxed{
|\mathcal B_U(X)|
\le3\mathcal H_U(X).
}
\tag{L-102010.13}
\]

This is an exact deterministic reduction. No separate plus-field estimate is
needed.

## Conclusion-facing condition

For `U_X=floor(X^(1/3))`, define

\[
\boxed{
\mathrm{HHFE102010}(L):
\quad
\int_{2^L}^{2^{L+1}}
\mathcal H_{U_X}(X)\frac{dX}{X}
=2^{o(L)}.
}
\tag{HHFE102010}
\]

Then (L-102010.13) gives `BVD100310`; the Type-I theorem and Mellin--Landau
consumer of `L-100310--L-100312` imply

\[
\boxed{\mathrm{HHFE102010}\Longrightarrow RH.}
\tag{L-102010.14}
\]

`HHFE102010` remains open. Its exact source is narrower than the original
balanced trilinear:

```text
one signed tail b_U;
one positive half-divisor renewal eta;
one compact ratio-four step kernel A_-;
one endpoint-local logarithmic L2 energy.
```

Source-blind coefficient diagonals still lose a power, so the theorem is a
reduction rather than an unconditional closure.
