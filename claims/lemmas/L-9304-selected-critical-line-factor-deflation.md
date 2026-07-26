# L-9304 — Selected critical-line factor deflation

Claim ID: `L-9304`  
Title: Directed critical-line zero balls may be removed as interval-valued factors from the direct completed-xi modulus  
Status: `PROPOSED`  
Authoring agent: `gpt56-01-j`  
Created: 2026-07-26  
Dependencies: `L-7501`, `L-7504`, `L-9301`, proof-grade critical-line zero balls  
Scope: division-free completed-xi modulus witnesses  
Related counterexample candidates: none

## Motivation

`L-9301` uses only a lower zero count in a bin. If a selected critical-line zero has squared distance

\[
y=(T-\gamma)^2\le B,
\]

it subtracts the universally safe factor `log(u+B)`. The residual retains the positive kernel

\[
K_y-K_B
=\int_y^B\frac{ds}{(u+s)(v+s)}.
\]

This is exactly the right construction when only a count and a farthest-distance bound are known. It is not the strongest construction when a directed computation has already isolated the zero in a narrow ordinate ball.

This lemma removes the selected *actual* zero factors, with the unknown ordinates carried as intervals. It is logically stronger than endpoint deflation and reuses the same direct completed-`xi` primitive table.

## Statement

Fix a real ordinate `T` and put

\[
H_T(x^2)=\left|\xi\!\left(\frac12+x+iT\right)\right|^2,
\qquad
G_T(u)=\log H_T(u),\quad u>0.
\]

Let

\[
I_r=[a_r,b_r]\qquad(1\le r\le R)
\]

be pairwise-disjoint closed ordinate intervals. Suppose `I_r` is independently certified to contain at least `m_r>=1` actual critical-line zeros, counted with multiplicity. Choose any `m_r` such zeros and write their ordinates as `gamma_{r,l}`. Define

\[
y_{r,l}=(T-\gamma_{r,l})^2
\]

and the exact selected-factor residual

\[
\boxed{
G_{T,J}(u)
=
G_T(u)-\sum_{r=1}^{R}\sum_{\ell=1}^{m_r}\log(u+y_{r,\ell}).
}
\]

Assume RH. Then:

1. `G_{T,J}'` is completely monotone on `(0,infinity)`.
2. Its secant kernel
   \[
   L_{T,J}(u,v)=\frac{G_{T,J}(u)-G_{T,J}(v)}{u-v}
   \]
   has a positive Cauchy-Gram representation.
3. Every cross-Loewner minor on increasing positive row and column lists is nonnegative.
4. For `0<u<v`,
   \[
   \boxed{
   H_T(v)\prod_{r,\ell}(u+y_{r,\ell})
   \ge
   H_T(u)\prod_{r,\ell}(v+y_{r,\ell}).
   }
   \]
5. A strict directed negative enclosure of any one of these quantities is a finite RH-disproof witness, subject to independent validation of the completed-`xi` rectangles, critical-line zero gates, and analytic normalization.

No completeness of the selected zero list is required. Every unselected zero remains in the positive residual.

## Proof

Under RH, the canonical product from `L-7501` gives, up to an additive real constant,

\[
G_T(u)
=
C+\sum_{\gamma}m_\gamma\log\bigl(u+(T-\gamma)^2\bigr).
\]

The certified bins allow us to select the declared number of actual line zeros without double counting because the bins are disjoint. Subtracting their exact logarithmic factors leaves

\[
G_{T,J}(u)
=
C+\sum_{\gamma\notin J}m_\gamma\log\bigl(u+(T-\gamma)^2\bigr),
\]

with any excess multiplicity at a selected ordinate left in the sum. Hence

\[
G_{T,J}'(u)
=
\sum_{\gamma\notin J}\frac{m_\gamma}{u+(T-\gamma)^2}
\]

is completely monotone. Its secant kernel is

\[
L_{T,J}(u,v)
=
\sum_{\gamma\notin J}m_\gamma
\int_{(T-\gamma)^2}^{\infty}
\frac{ds}{(u+s)(v+s)},
\]

which is a positive Cauchy-Gram kernel. `L-7504` then gives all cross-minor inequalities. The two-point multiplicative inequality follows by exponentiating `G_{T,J}(v)>=G_{T,J}(u)` and clearing the positive selected factors. ∎

## Directed zero-ball realization

The actual ordinate is not known exactly. For one certified bin `I=[a,b]`, define the exact squared-distance interval

\[
Y_I
=
\{(T-t)^2:t\in[a,b]\}
=[A_I,B_I].
\]

It is obtained by squaring the rational interval `[T-b,T-a]`, with lower endpoint zero when that interval crosses zero. For a sampled exact node `u>0`, every selected factor lies in

\[
u+Y_I=[u+A_I,u+B_I].
\]

Therefore an exact checker may enclose

\[
G_{T,J}(u)
\in
\log H_T(u)
-
\sum_r m_r\log(u+Y_{I_r})
\]

using outward rational interval arithmetic. If the bin contains several selected zeros at different ordinates, each logarithm lies in the same interval and their sum lies in its `m_r`-fold Minkowski sum.

For the algebraic two-point row, the actual products satisfy

\[
\prod_{\ell=1}^{m_r}(u+y_{r,\ell})
\in
(u+Y_{I_r})^{m_r}.
\]

Consequently the interval expression

\[
H_T(v)\prod_r(u+Y_{I_r})^{m_r}
-
H_T(u)\prod_r(v+Y_{I_r})^{m_r}
\]

contains the exact selected-factor monotonicity value. Shared zero-location dependence is discarded by ordinary interval multiplication, so the enclosure can be wider than necessary, but it cannot exclude the true value.

## Strict relation to endpoint deflation

For one selected actual zero with `y<=B`, `L-9301` leaves the residual kernel

\[
K_y-K_B
=
\int_y^B\frac{ds}{(u+s)(v+s)}\succeq0,
\]

whereas exact selected-factor removal leaves zero from that factor. Hence, for the same actual zero configuration, the exact residual Stieltjes measure is dominated by the endpoint-deflated residual measure.

By `L-9303`, every exact selected-factor cross minor is no larger than the corresponding endpoint-deflated minor under RH. Narrowing a zero ball improves the interval enclosure monotonically and converges to exact factor removal.

This comparison is structural. A dependency-blind interval implementation may temporarily widen when a bin is split or reparameterized; that is an implementation issue, not a failure of the underlying Loewner-order statement.

## Multiplicity and uniqueness

The theorem needs only a lower multiplicity count.

- If a bin contains one simple zero, select it once.
- If it contains a multiple zero of multiplicity at least `m`, select `m` copies.
- If it contains several zeros with total multiplicity at least `m`, select any `m` of them.
- Extra zeros and extra multiplicity remain in the residual.

A production certificate must bind the meaning of the lower count to critical-line zeros. A total-strip count is not interchangeable with a critical-line count.

## Existential completeness

Suppose RH fails at

\[
\rho=\frac12+\delta+i\gamma,
\qquad d=\delta^2>0.
\]

Near `u=d`,

\[
G_\gamma(u)=2m\log|u-d|+A(u),
\]

with `A` analytic. Removing any finite collection of critical-line factors subtracts a function analytic near the positive point `d`. Therefore the interlaced four-point determinant from `L-7504` retains the leading term

\[
-\frac{(2m\log2)^2}{h^2}+O(h^{-1})<0
\]

for sufficiently small `h`. Selected-factor deflation preserves the existential completeness of the direct-modulus route.

## Certificate discipline

A production selected-factor certificate must bind:

- the exact rational ordinate `T`;
- every exact rational zero-ball endpoint;
- a positive critical-line lower multiplicity count;
- pairwise-disjoint selected bins;
- immutable gate and source digests;
- direct completed-`xi` rectangles and normalization;
- point identities and exact squared horizontal nodes;
- outward logarithm and determinant arithmetic.

The final checker must fail closed if a completed-`xi` modulus interval touches zero, a zero gate is missing, selected bins overlap, or a determinant interval touches zero.

## Gap audit

1. A narrow empirical root approximation is not a proof-grade zero ball.
2. Subtracting a midpoint zero factor without a radius is invalid.
3. Reusing one zero in two bins double counts positive mass.
4. The interval enclosure loses correlation between the same zero factor at different horizontal nodes; this may reduce power but not validity.
5. A negative synthetic model row is not a Riemann-`xi` result.
6. A strict Riemann-`xi` negative still requires independent special-function and zero-isolation reproduction.

## Suggested next attack

Run the PR #71 ladder twice from the same directed artifacts:

1. the conservative `L-9301` endpoint-deflated rows;
2. the `L-9304` selected-factor interval rows from the isolated Hardy-zero balls.

Rank any unresolved difference by the zero balls whose width contributes most to the selected-factor interval. Refine only those balls, then replay the unchanged direct-`xi` rectangles.
