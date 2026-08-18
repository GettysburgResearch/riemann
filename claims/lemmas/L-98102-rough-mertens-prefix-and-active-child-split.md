# L-98102 — The inactive Euler tail combines exactly into one rough reciprocal-Mertens prefix

Claim ID: `L-98102`  
Status: **PROVED EXACT ALGEBRAIC REDUCTION**  
Created: 2026-08-18  
Depends on: `L-98101`  
RH status: **unproved**

The base scalar vanishes below its first activation:

\[
U_Z(Y)=0\qquad(0<Y\le2).
\tag{L-98102.1}
\]

Hence the exact full source may be restricted to rough products `v<X/2`:

\[
U_{\rm full}(X)
=
\sum_{v\mid Q_L\atop v<X/2}{\mu(v)\over v}U_Z(X/v).
\tag{L-98102.2}
\]

Substituting `U_Z=A_Z+epsilon_Z` gives

\[
\boxed{
U_{\rm full}(X)
=
A_Z\,\mathcal M_Z(X/2)
+
\sum_{v\mid Q_L\atop v<X/2}{\mu(v)\over v}\varepsilon_Z(X/v),
}
\tag{L-98102.3}
\]

where

\[
\boxed{
\mathcal M_Z(x)
=
\sum_{v\mid Q_L\atop v<x}{\mu(v)\over v}
}
\tag{L-98102.4}
\]

is the finite `Z`-rough reciprocal-Möbius prefix. Since every prime factor of a
number `v<X/2` is automatically at most `X/2`, this is equivalently

\[
\mathcal M_Z(X/2)
=
\sum_{v<X/2\atop P^-(v)>Z}{\mu(v)\over v}.
\tag{L-98102.5}
\]

Thus the apparently positive full Euler product in `L-98101.3` and the inactive
history tail cancel exactly into the truncated rough Möbius prefix. No positive
mass is available from the inactive sector by itself.

With `Y_epsilon=(log X)^(4+epsilon)`, split the second term at
`v=X/Y_epsilon`. The bulk is `o(1/log X)` by `L-98101`; the remaining active
correction is

\[
\boxed{
\mathcal A_\epsilon(X)
=
\sum_{X/Y_\epsilon<v<X/2\atop P^-(v)>Z}
{\mu(v)\over v}\varepsilon_Z(X/v).
}
\tag{L-98102.6}
\]

Every child in this sum satisfies

\[
2<X/v<Y_\epsilon.
\tag{L-98102.7}
\]

Consequently

\[
\boxed{
U_{\rm full}(X)
=
A_Z\mathcal M_Z(X/2)
+
\mathcal A_\epsilon(X)
+o(1/\log X).
}
\tag{L-98102.8}
\]

This is the sharpest source-blind consequence of the bounded base remainder:
all large-child histories are closed, while the surviving arithmetic consists
of

1. one rough reciprocal-Mertens prefix at `X/2`; and
2. one active correction whose child is at most `(log X)^(4+epsilon)`.

Neither term has a proved sign. Replacing either by its absolute value destroys
the reciprocal-zeta cancellation.