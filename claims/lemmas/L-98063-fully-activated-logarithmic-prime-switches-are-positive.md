# L-98063 — Every fully activated prime switch below the logarithmic wall is positive

Claim ID: `L-98063`  
Status: **PROVED UNCONDITIONAL UNIFORM ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98061/L-98062`; the prime number theorem  
RH status: **not assumed**

Let

\[
h(Y)={F_{61}(Y)\over\sqrt Y}
=a_*+{c_*\over\sqrt Y}+O_{P_{61}}(Y^{-2}),
\qquad a_*>0,\quad c_*<0,
\tag{L-98063.1}
\]

as in `L-98061`.  For a prime `q>=67`, install every earlier rough prime and
put

\[
U_{<q}(Y)
=
\prod_{67\le r<q\atop r\ {m prime}}
\mathcal E_r h(Y),
\qquad
(\mathcal E_rf)(Y)=f(Y)-{1\over r}f(Y/r).
\tag{L-98063.2}
\]

Fix `epsilon>0`.  Uniformly for primes

\[
67\le q\le(1-\epsilon)\log X,
\tag{L-98063.3}
\]

one has, for all sufficiently large `X`,

\[
\boxed{
U_{<q}(X/q)-U_{<q}(X/q^2)>0.
}
\tag{L-98063.4}

Consequently the hyperbolic cutoff-switch strip of `L-98062` is positive:

\[
\boxed{
\mathcal J_{(2,X/q]}^+(X)-\mathcal J_{(2,X/q]}^-(X)>0
}
\tag{L-98063.5}

for every prime in (L-98063.3).

## Uniform finite-cube expansion

Let

\[
P(q)=\prod_{67\le r<q}r.
\]

Whenever `Y/P(q)` is beyond the fixed asymptotic threshold in (L-98063.1),
expanding every Euler factor gives

\[
\boxed{
U_{<q}(Y)
=A_q+{C_q\over\sqrt Y}+R_q(Y),
}
\tag{L-98063.6}

where

\[
A_q=a_*\prod_{67\le r<q}\left(1-{1\over r}\right)>0,
\tag{L-98063.7}
\]

\[
C_q=c_*\prod_{67\le r<q}\left(1-{1\over\sqrt r}\right)<0,
\tag{L-98063.8}
\]

and

\[
\boxed{
|R_q(Y)|
\le {C\over Y^2}
\prod_{67\le r<q}(1+r)
}
\tag{L-98063.9}

for one fixed `P_61` constant `C`.  Indeed, a subset product `d` contributes
`d^{-1}O((Y/d)^{-2})=O(d/Y^2)`, and summing over all subsets gives the product
in (L-98063.9).

The prime number theorem gives

\[
\log P(q)=q+o(q).
\tag{L-98063.10}
\]

Under (L-98063.3), for large `X`,

\[
{X/q^2\over P(q)}\longrightarrow\infty,
\tag{L-98063.11}
\]

uniformly.  Thus (L-98063.6) applies at both `X/q` and `X/q^2`.

## Positive leading increment

Subtracting the two expansions gives

\[
\begin{aligned}
U_{<q}(X/q)-U_{<q}(X/q^2)
={}&{|C_q|(q-\sqrt q)\over\sqrt X}\\
&+O\!\left(
{q^4\over X^2}
\prod_{67\le r<q}(1+r)
\right).
\end{aligned}
\tag{L-98063.12}

The first term is positive because `C_q<0`.  Moreover

\[
\prod_{67\le r<q}
\left(1-{1\over\sqrt r}\right)
\ge
\exp\!\left[-C_1{\sqrt q\over\log q}ight]
\tag{L-98063.13}
\]

and

\[
\prod_{67\le r<q}(1+r)
\le
\exp(q+o(q)).
\tag{L-98063.14}
\]

Hence the positive term in (L-98063.12) is

\[
X^{-1/2-o(1)},
\]

whereas the error is

\[
X^{-1-\epsilon/2+o(1)}.
\]

The main term dominates uniformly, proving (L-98063.4).

## Interpretation

The logarithmic wall is geometric, not an arbitrary cutoff.  Below
`q=(1-epsilon)log X`, the primorial of all earlier rough primes is smaller than
the bottom strip endpoint `X/q^2`; every source colour is fully activated and
the negative constant `c_*` forces a positive two-scale increment.  At
`q about log X`, the primorial reaches the endpoint and product-boundary
activation begins.  The asymptotic argument then ceases to be uniform.

Thus a complete adaptive-cutoff attack may move every prime below the
logarithmic wall at nonnegative cost.  The remaining signed debt starts only
where the source product itself meets the active boundary.  This matches, by a
different exact mechanism, the growing-prime wall isolated in PR #592 and the
product-boundary reductions in PRs #599/#605.

```text
prime switches q<=(1-epsilon)log X     PROVED POSITIVE
fully activated curvature sector        CLOSED
logarithmic primorial/activation wall    IDENTIFIED EXACTLY
post-wall product-boundary strips        OPEN / RH-BEARING
GPC67 / RH                              UNPROVEN
```