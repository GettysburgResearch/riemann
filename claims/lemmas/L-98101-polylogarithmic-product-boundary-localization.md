# L-98101 — Every noncritical product history has child below the logarithmic fourth-power frontier

Claim ID: `L-98101`  
Status: **PROVED UNCONDITIONAL REDUCTION**  
Created: 2026-08-18  
Depends on: `L-98100`; PR #599 `L-97912`  
RH status: **unproved**

Let `Z=Z_X` be the slowly growing cutoff of `L-98100`. Install the remaining
rough primes

\[
Q_L=\prod_{Z<p\le X/2}p.
\]

The exact normalized source is

\[
U_{\rm full}(X)
=
\sum_{v\mid Q_L}{\mu(v)\over v}U_Z(X/v).
\tag{L-98101.1}
\]

Write

\[
A_Z=a_*P_Z,
\qquad
U_Z(Y)=A_Z+\varepsilon_Z(Y),
\qquad
|\varepsilon_Z(Y)|\le {C_bE_Z\over\sqrt Y}.
\tag{L-98101.2}
\]

Then

\[
U_{\rm full}(X)
=
\underbrace{A_Z\prod_{Z<p\le X/2}(1-1/p)}_{\mathfrak M(X)>0}
+
\sum_{v\mid Q_L}{\mu(v)\over v}\varepsilon_Z(X/v).
\tag{L-98101.3}
\]

By Mertens,

\[
\mathfrak M(X)\asymp {1\over\log X}.
\tag{L-98101.4}
\]

Fix `epsilon>0` and put

\[
Y_\epsilon(X)=(\log X)^{4+\epsilon}.
\tag{L-98101.5}
\]

Split the error according to

\[
v\le X/Y_\epsilon
\qquad\text{and}\qquad
v>X/Y_\epsilon.
\]

For the first part, `v^{-1/2}<=sqrt(X/Y_epsilon)/v`, so

\[
\begin{aligned}
|\mathfrak E_{\rm bulk}(X)|
&\le {C_bE_Z\over\sqrt X}
\sum_{v\mid Q_L\atop v\le X/Y_\epsilon}v^{-1/2}\\
&\le {C_bE_Z\over\sqrt{Y_\epsilon}}
\prod_{Z<p\le X/2}(1+1/p)\\
&\ll
{E_Z\over(\log X)^{2+\epsilon/2}}
{\log X\over\log Z}.
\end{aligned}
\tag{L-98101.6}
\]

By `L-98100`, `E_Z=(log X)^{o(1)}`. Hence

\[
\boxed{
\mathfrak E_{\rm bulk}(X)
=o(1/\log X)
=o(\mathfrak M(X)).
}
\tag{L-98101.7}
\]

Define the exact remaining boundary

\[
\boxed{
\mathfrak R_\epsilon(X)
=
\sum_{v\mid Q_L\atop v>X/Y_\epsilon}
{\mu(v)\over v}\varepsilon_Z(X/v).
}
\tag{L-98101.8}
\]

Then

\[
\boxed{
U_{\rm full}(X)
=
\mathfrak M(X)
+o(1/\log X)
+\mathfrak R_\epsilon(X).
}
\tag{L-98101.9}
\]

Every active history in `mathfrak R_epsilon` has endpoint

\[
\boxed{
X/v<Y_\epsilon(X)=(\log X)^{4+\epsilon}.
}
\tag{L-98101.10}
\]

Histories with `v>X/2` are inactive (`X/v<2`) and contribute the pure constant
error `epsilon_Z(X/v)=-A_Z`; they are retained exactly rather than deleted.

Thus the complete unresolved factor-67 product boundary is supported on either

1. a genuinely active child below `(log X)^(4+epsilon)`, or
2. the inactive alternating Euler-product tail.

No fixed power `X^delta` remains.