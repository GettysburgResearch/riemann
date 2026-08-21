# L-103304 — The positive half-divisor completion constructs the exact convolution square root of the Möbius source

Claim ID: `L-103304`  
Status: **PROVED EXACT ARITHMETIC FACTORIZATION**  
Created: 2026-08-21  
Depends on: PR #696 `L-102010`  
RH status: **not assumed**

Let the positive multiplicative function `eta` be defined by

\[
\sum_{k\ge0}\eta(p^k)z^k=(1-z)^{-1/2}.
\]

PR #696 proves

\[
\eta*\eta=\mathbf1.
\tag{L-103304.1}
\]

Put

\[
\lambda=\mu*\eta.
\]

Then

\[
\boxed{
\lambda*\lambda
=\mu*\mu*(\eta*\eta)
=\mu*\mu*\mathbf1
=\mu*(\mu*\mathbf1)
=\mu.
}
\tag{L-103304.2}
\]

Equivalently, every ordinary-prime local generating function of `lambda` is

\[
(1-z)^{1/2}.
\tag{L-103304.3}
\]

For the duplicate-67 source

\[
\beta=(\delta_1-\delta_{67})*\mu,
\]

let `chi_67` be supported on powers of `67` with local generating function
`(1-z)^(1/2)`, and put

\[
\lambda_{67}=\lambda*\chi_{67}.
\]

Then

\[
\boxed{
\lambda_{67}*\lambda_{67}=\beta.
}
\tag{L-103304.4}
\]

Thus the half-divisor field of PR #696 is not an auxiliary completion: in the
untruncated limit it is the literal convolution square root of the source.
For any Mellin-kernel factorization `K=F *_M G`, finite Fubini gives

\[
\boxed{
\sum_n{\beta(n)\over\sqrt n}K(X/n)
=\int_0^\infty
 \mathcal H_F(Y)\mathcal H_G(X/Y){dY\over Y},
}
\tag{L-103304.5}
\]

where

\[
\mathcal H_F(Y)=\sum_n{\lambda_{67}(n)\over\sqrt n}F(Y/n)
\]

and similarly for `G`.  This is the exact arithmetic interface connecting the
balanced Vaughan half-field of PR #696 to the cubic Gram factorization of
`L-103303`.
