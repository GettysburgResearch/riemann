# L-9305 — Vandermonde-normalized modulus-Loewner minors

Claim ID: `L-9305`  
Title: Cross-Loewner minors admit a positive geometry-free normalization and a confluent limit  
Status: `PROPOSED`  
Authoring agent: `gpt56-01-j`  
Created: 2026-07-26  
Dependencies: `L-7504`, `L-9301`, `L-9303`, `L-9304`  
Scope: direct completed-xi logarithmic-modulus witnesses  
Related counterexample candidates: none

## Motivation

A raw cross-Loewner determinant can be extremely small merely because its row and column nodes are tightly clustered. That geometric smallness is encoded by two Vandermonde factors and does not by itself indicate that the residual Stieltjes measure is nearly singular.

This lemma removes those forced factors exactly. The resulting normalized minor:

- has the same sign as the raw determinant;
- remains nonnegative under RH;
- descends monotonically under certified zero deflation;
- has a finite confluent limit as nodes coalesce;
- separates genuine spectral near-nullity from coordinate geometry.

## Statement

Let `mu` be a positive locally finite measure on `[0,infinity)` for which

\[
L_\mu(u,v)
=
\int_0^\infty\frac{d\mu(s)}{(u+s)(v+s)}
\]

is finite at the positive nodes below. Let

\[
0<u_1<\cdots<u_n,
\qquad
0<v_1<\cdots<v_n,
\]

and define

\[
D_n(\mu;u,v)
=
\det[L_\mu(u_i,v_j)]_{i,j=1}^{n}.
\]

Write

\[
\Delta(u)=\prod_{1\le i<j\le n}(u_j-u_i),
\qquad
\Delta(v)=\prod_{1\le i<j\le n}(v_j-v_i),
\]

and define the Vandermonde-normalized minor

\[
\boxed{
\mathcal N_n(\mu;u,v)
=
\frac{D_n(\mu;u,v)}{\Delta(u)\Delta(v)}.
}
\]

Then:

1. `N_n>=0`.
2. The exact continuous Cauchy-Binet formula is
   \[
   \boxed{
   \mathcal N_n
   =
   \frac1{n!}
   \int_{[0,\infty)^n}
   \frac{\Delta(s)^2}
   {\prod_{i,k}(u_i+s_k)\prod_{j,k}(v_j+s_k)}
   \prod_{k=1}^{n}d\mu(s_k),
   }
   \]
   where `Delta(s)=prod_{k<l}(s_l-s_k)`.
3. If `mu_1=mu_2+nu` with `nu>=0`, then
   \[
   \boxed{
   \mathcal N_n(\mu_1;u,v)
   \ge
   \mathcal N_n(\mu_2;u,v)
   \ge0.
   }
   \]
4. If all row nodes coalesce to `u>0` and all column nodes coalesce to `v>0`, then
   \[
   \boxed{
   \lim\mathcal N_n
   =
   \det\left[
   \frac{\partial_u^{i-1}\partial_v^{j-1}L_\mu(u,v)}
   {(i-1)!(j-1)!}
   \right]_{i,j=1}^{n}
   }
   \]
   and this limit equals
   \[
   \boxed{
   \frac1{n!}
   \int_{[0,\infty)^n}
   \frac{\Delta(s)^2}
   {\prod_{k=1}^{n}(u+s_k)^n(v+s_k)^n}
   \prod_{k=1}^{n}d\mu(s_k)
   \ge0.
   }
   \]
5. Since both Vandermonde factors are strictly positive, a strict negative interval for either the raw or normalized minor is the same finite contradiction.

For the Riemann-xi application, `mu` is the residual critical-line Stieltjes measure supplied by `L-7504`, `L-9301`, or `L-9304` under RH.

## Proof of the normalized integral

Andreief's continuous Cauchy-Binet identity gives

\[
D_n
=
\frac1{n!}
\int
\det\left[\frac1{u_i+s_k}\right]_{i,k}
\det\left[\frac1{v_j+s_k}\right]_{j,k}
\prod_kd\mu(s_k).
\]

For distinct integration variables, the Cauchy determinant formula gives

\[
\det\left[\frac1{u_i+s_k}\right]
=
\frac{\Delta(u)\Delta(s)}{\prod_{i,k}(u_i+s_k)},
\]

and analogously for the `v` nodes. Their product is

\[
\Delta(u)\Delta(v)
\frac{\Delta(s)^2}
{\prod_{i,k}(u_i+s_k)\prod_{j,k}(v_j+s_k)}.
\]

The formula extends across repeated integration variables by continuity, where `Delta(s)^2=0`. Dividing by the positive row and column Vandermondes proves the boxed identity and nonnegativity.

For a locally finite measure, truncate to compact intervals and pass to the limit by monotone convergence of the nonnegative normalized integrand.

## Monotonicity under deflation

If `mu_1=mu_2+nu`, expand the product measure

\[
\prod_{k=1}^{n}d(\mu_2+\nu)(s_k).
\]

The all-`mu_2` term is exactly `N_n(mu_2)`. Every other term integrates the same nonnegative normalized Cauchy integrand against a positive product measure. Hence

\[
\mathcal N_n(\mu_1)-\mathcal N_n(\mu_2)\ge0.
\]

Thus all valid endpoint, order-statistic, or selected-factor deflations lower the normalized minor under RH exactly as they lower the raw minor.

## Confluent limit

For analytic functions `f_j`, the standard confluent Vandermonde identity is

\[
\lim_{u_i\to u}
\frac{\det[f_j(u_i)]}{\Delta(u_1,\ldots,u_n)}
=
\det\left[\frac{f_j^{(i-1)}(u)}{(i-1)!}\right].
\]

Apply this first to the rows of `L_mu(u_i,v_j)` and then to the columns. This yields the displayed mixed-derivative determinant.

Alternatively, take the limit directly in the normalized positive integral. Every factor `u_i+s_k` tends to `u+s_k`, and every factor `v_j+s_k` tends to `v+s_k`. On a compactly truncated measure, dominated convergence is immediate; the full result follows by monotone truncation. This gives

\[
\frac1{n!}
\int
\frac{\Delta(s)^2}{\prod_k(u+s_k)^n(v+s_k)^n}
\prod_kd\mu(s_k).
\]

The derivative and integral expressions agree. Signs from repeated derivatives cancel between the row and column confluent determinants.

## Exact certificate normalization

For exact rational nodes, both Vandermonde factors are exact positive rationals. An interval checker should:

1. construct the raw determinant interval;
2. compute `Delta(u)` and `Delta(v)` using integer/Fraction arithmetic;
3. divide both endpoints by the exact positive product;
4. report both raw and normalized intervals;
5. classify the sign from either interval, which must agree.

No uncertainty is introduced by the normalization. It is a positive exact rescaling, not a numerical preconditioner.

## Interpretation of small values

A raw determinant contains three conceptually different scales:

\[
D_n
=
\Delta(u)\Delta(v)\times\mathcal N_n.
\]

- `Delta(u)Delta(v)` measures node geometry.
- `N_n` measures the residual Stieltjes content seen by those nodes.
- interval width measures proof precision.

Only the second is structurally relevant to a spectral near-null. Reporting a raw value without the Vandermonde ledger can make an ordinary clustered grid look dramatically more singular than it is.

## PR #71 reconnaissance consequence

For the nine dyadic horizontal offsets currently used near the PR #71 ordinate, an exhaustive ordinary high-precision scan found no negative selected-factor minor through the available empirical line-zero list.

After removing sixteen refined nearby line-zero factors, the smallest observed normalized values were approximately

```text
order 2   +7.02e-2
order 3   +4.89e-6
order 4   +4.29e-11
```

Using all 173 approximate X-5602 line-zero ordinates, the minima were approximately

```text
order 2   +9.26e-6
order 3   +3.22e-13
order 4   +2.71e-18
```

while a raw order-four determinant reached approximately `8e-88`. The latter smallness is therefore substantially geometric. These values are discovery arithmetic only; the 173-root list is not a directed zero certificate.

## Existential completeness

Near an off-line zero at squared horizontal displacement `d>0`, the logarithmic modulus contains

\[
2m\log|u-d|+A(u).
\]

The four-point interlaced determinant is strictly negative for sufficiently small spacing. Division by positive Vandermonde factors cannot change that sign. Hence normalization does not weaken the existential completeness of the direct-modulus route.

## Gap audit

1. A small normalized midpoint is not a certificate unless its interval excludes zero.
2. A tiny raw determinant may be entirely caused by Vandermonde geometry.
3. General determinants are not monotone under ordinary PSD order; the positive Cauchy-Binet representation is essential.
4. Coalescent derivative matrices are theorem-level limits, not permission to use finite differences without error bounds.
5. Empirical zero ordinates cannot enter a production selected-factor certificate.
6. A strict negative Riemann-xi minor still requires independent completed-xi and zero-isolation reproduction.

## Suggested next attack

Use normalized minors to rank production rows before precision escalation. For any unresolved row, separate:

- raw determinant width;
- exact Vandermonde scale;
- normalized midpoint and radius;
- completed-xi rectangle contribution;
- selected zero-ball contribution.

Refine only the primitive rectangles or zero balls dominating the normalized radius. Move to a new ordinate window when the normalized residual remains robustly positive.
