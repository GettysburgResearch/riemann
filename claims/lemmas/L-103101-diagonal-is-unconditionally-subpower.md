# L-103101 — The complete half-completed coefficient diagonal is unconditionally subpower

**Status:** PROVED UNCONDITIONALLY.

In the notation of `L-103100`, the diagonal of the field energy is

\[
\mathcal D_{U,N}
=R(0)\sum_{U<n\le N}\frac{h_U(n)^2}{n}
=3\log2\sum_{U<n\le N}\frac{h_U(n)^2}{n}.
\]

Every local half-divisor coefficient satisfies `0<eta(p^k)<=1`. Therefore

\[
|h_U(n)|
\le\sum_{d\mid n}\eta(n/d)
\le\tau(n).
\]

For every `epsilon>0`, the elementary divisor bound gives

\[
\tau(n)\ll_\epsilon n^\epsilon.
\]

Consequently

\[
\boxed{
\mathcal D_{U,N}\ll_\epsilon N^{2\epsilon}
}
\tag{L-103101.1}
\]

uniformly in `U<N`. Equivalently,

\[
\boxed{\mathcal D_{U,N}=N^{o(1)}.}
\tag{L-103101.2}
\]

Thus the coefficient diagonal, including the positive half-divisor renewal, is not the RH-scale obstruction. Only the signed off-diagonal near-collision remains.
