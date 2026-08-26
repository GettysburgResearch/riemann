# L-103002 — Order-concordant antisymmetric endpoint packets are one-sided

Claim ID: `L-103002`  
Status: **PROVED EXACT PACKET SIGN THEOREM**  
Created: 2026-08-25  
Depends on: `L-103001`  
RH status: **not assumed**

Let `S` be a finite set of positive source locations and let

\[
\gamma_{n,m}=-\gamma_{m,n}
\qquad(n,m\in S)
\]

be real antisymmetric coefficients. Define the common-mother endpoint current

\[
\mathcal J_\gamma(X)
=
\sum_{n<m}
\gamma_{n,m}
\left[
A_-(X/n)A(X/m)-A(X/n)A_-(X/m)
\right].
\tag{L-103002.1}
\]

Split the coefficient array source-exactly into

\[
\gamma_{n,m}
=
\gamma_{n,m}^{\rm con}
-
\gamma_{n,m}^{\rm inv},
\]

where, for `n<m`,

\[
\gamma_{n,m}^{\rm con}=(\gamma_{n,m})_+,
\qquad
\gamma_{n,m}^{\rm inv}=(-\gamma_{n,m})_+.
\tag{L-103002.2}
\]

This is the unique positive/negative decomposition on the declared ordered pair coordinate.

By `L-103001`, the bracket in (L-103002.1) is nonpositive for `n<m`. Hence

\[
\boxed{
\mathcal J_{\gamma^{\rm con}}(X)\le0
\quad\text{for every }X>0.
}
\tag{L-103002.3}
\]

All possible positive contribution to `mathcal J_gamma` comes from the inversion packet:

\[
\boxed{
(\mathcal J_\gamma(X))_+
\le
-\mathcal J_{\gamma^{\rm inv}}(X).
}
\tag{L-103002.4}
\]

Likewise, after reversing the global sign, all possible negative contribution is confined to the same inversion packet.

For every nonnegative physical weight `w`,

\[
\boxed{
\int
(\mathcal J_\gamma)_+w\,{dX\over X}
\le
\sum_{n<m}
\gamma_{n,m}^{\rm inv}
\int
[-\mathcal W_{n,m}(X)]w(X){dX\over X}.
}
\tag{L-103002.5}
\]

## Meaning

The common-mother endpoint kernel itself creates no adverse sign on an order-concordant source packet. The entire adverse endpoint current is supported on source coefficients whose antisymmetric orientation disagrees with the physical product order.

This theorem is exact before any Cauchy inequality. It applies to scalar coefficients, to real parts of Hilbert-space pairings after the coefficient has been formed source-faithfully, and to every fixed source region. It does not assert that the arithmetic inversion packet is small.