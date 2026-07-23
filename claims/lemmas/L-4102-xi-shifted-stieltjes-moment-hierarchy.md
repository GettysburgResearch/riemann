# L-4102 — Shifted-Stieltjes moment matrices from `xi'/xi`

Claim ID: L-4102  
Title: Under RH, every horizontal `xi'/xi` slice generates positive Hankel and localizing matrices  
Status: PROPOSED  
Authoring agent: `gpt56-05-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3201`; `L-4101`  
Scope: finite logarithmic-derivative-jet counterexample certificates  
Related counterexample candidates: none

## Statement

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

in the normalization of `D-3201`. Fix real `T`, let `x>0`, and put

\[
 u=x^2,
 \qquad
 s=\frac12+x+iT.
\]

At points where `xi(s)` is nonzero, define the real horizontal slice

\[
 H_T(u)=\frac1{\sqrt u}
 \operatorname{Re}F\!\left(\frac12+\sqrt u+iT\right).
\]

For every integer `n>=0`, define

\[
 m_n(u,T)=\frac{(-1)^n}{n!}\frac{d^n}{du^n}H_T(u).
\]

If RH holds, then

\[
 H_T(u)=\sum_\gamma
 \frac1{u+(T-\gamma)^2}
\]

and

\[
 m_n(u,T)=\sum_\gamma
 \frac1{\left(u+(T-\gamma)^2\right)^{n+1}},
\]

where ordinates are counted with multiplicity.

For every `N>=0`, define the real symmetric matrices

\[
 A_N=(m_{j+k})_{0\le j,k\le N}
\]

and

\[
 B_N=(m_{j+k}-u m_{j+k+1})_{0\le j,k\le N}.
\]

Under RH,

\[
 A_N\succeq0,
 \qquad
 B_N\succeq0
\]

for every choice of `u>0`, `T`, and `N`.

Consequently, any exact rational or dyadic `x,T`, matrix choice
`A_N` or `B_N`, and nonzero exact real/dyadic vector `c` for which rigorous
`xi`-jet enclosures prove

\[
 c^{\mathsf T}A_Nc<0
 \quad\text{or}\quad
 c^{\mathsf T}B_Nc<0
\]

give a finite unconditional counterexample witness to RH.

The hierarchy contains `L-4101` exactly. Namely,

\[
 (B_0)_{00}
 =m_0-u m_1
 =\frac12\left(
 \operatorname{Re}F'(s)+\frac1x\operatorname{Re}F(s)
 \right)
 =\frac12\mathcal D(s).
\]

Therefore every RH failure produces a negative member of this hierarchy on a
nonempty open set: the `1 x 1` localizing matrix already becomes negative to the
right of a right-half-plane zero.

## Exact finite-jet formula

Write

\[
 A_k=\operatorname{Re}F^{(k)}(s).
\]

Then every moment is a finite exact rational combination of one horizontal
`F` jet:

\[
 m_n=
 \sum_{k=0}^{n}
 (-1)^k
 \frac{(2n-k)!}
 {2^{2n-k}n!\,k!\,(n-k)!}
 \frac{A_k}{x^{2n-k+1}}.
\]

Thus:

- `A_N` requires `F,F',...,F^(2N)`;
- `B_N` requires `F,F',...,F^(2N+1)`;
- a direct `xi` implementation may obtain these from a `xi` jet through order
  `2N+2` and logarithmic-series division.

All displayed coefficients are rational, and exact dyadic `x` makes every
power of `x` exact. A checker can therefore reconstruct the moment intervals
without differentiating numerically.

## Definitions

For fixed `u,T` under RH, put

\[
 y_\gamma=(T-\gamma)^2,
 \qquad
 a_\gamma=\frac1{u+y_\gamma}.
\]

Then

\[
 0<a_\gamma\le\frac1u
\]

and

\[
 m_n=\sum_\gamma a_\gamma^{n+1}.
\]

Thus `(m_n)` is a moment sequence for the positive discrete measure

\[
 \sum_\gamma a_\gamma\,\delta_{a_\gamma}
\]

supported in `(0,1/u]`. The matrix `A_N` is its Hankel moment matrix. The matrix
`B_N` is the localizing matrix for the nonnegative support polynomial
`1-u a`.

This interpretation is conditional on RH. Unconditionally, the matrices are
finite real expressions reconstructed from the `xi` jet; a certified negative
value contradicts the conditional representation.

## Motivation

The scalar passivity criterion of `L-3201` uses one value of `F`. The Pick
matrix of `L-3202` combines values at different complex points. The present
hierarchy instead takes one point and combines a finite derivative jet.

It offers three potential advantages:

1. **right-side detection:** `B_0` detects an off-line pole from the side where
   `Re F` itself is positive;
2. **one-point coherence:** all entries come from one ball-valued jet, avoiding
   huge-height phase inconsistencies among multiple points;
3. **higher-order concentration:** exact vectors select polynomials in the
   resolvent variable `a_gamma`, allowing a finite moment matrix to amplify a
   localized violation that is weak in a scalar sign.

No finite positive result supports RH. The hierarchy is used only in the
one-way direction: one rigorous negative quadratic form disproves RH.

## Proof of the Stieltjes representation

Assume RH. By the zero-resolvent expansion used in `L-3201`, at
`s=1/2+x+iT`,

\[
 \operatorname{Re}F(s)
 =\sum_\gamma
 \frac{x}{x^2+(T-\gamma)^2}.
\]

Dividing by `x=sqrt(u)` gives

\[
 H_T(u)=\sum_\gamma
 \frac1{u+(T-\gamma)^2}.
\]

On every compact interval `u>=u_0>0`, the `n`-th derivative of one summand is
bounded by

\[
 \frac{n!}{(u_0+(T-\gamma)^2)^{n+1}}.
\]

The resulting series converges: for large `|gamma|` it is dominated by a
constant multiple of `|gamma|^{-2n-2}`, and the zero-counting growth already
suffices for the `n=0` admissibility sum used in `L-3201`. Hence termwise
differentiation is justified and

\[
 \frac{(-1)^n}{n!}H_T^{(n)}(u)
 =\sum_\gamma
 \frac1{(u+(T-\gamma)^2)^{n+1}}.
\]

This proves the moment formula.

## Proof of matrix positivity

Let `c=(c_0,...,c_N)` be complex. Using
`a_gamma=1/(u+y_gamma)`,

\[
 c^*A_Nc
 =\sum_{j,k}\overline{c_j}c_km_{j+k}
 =\sum_\gamma a_\gamma
 \left|\sum_{j=0}^{N}c_j a_\gamma^j\right|^2
 \ge0.
\]

Also,

\[
 m_n-u m_{n+1}
 =\sum_\gamma a_\gamma^{n+1}(1-u a_\gamma)
 =\sum_\gamma y_\gamma a_\gamma^{n+2}.
\]

Therefore

\[
 c^*B_Nc
 =\sum_\gamma y_\gamma a_\gamma^2
 \left|\sum_{j=0}^{N}c_j a_\gamma^j\right|^2
 \ge0.
\]

Both matrices are positive semidefinite under RH. A directed negative
quadratic form contradicts RH. Because the matrices are real symmetric, a
negative direction may be chosen real; exact dyadic real vectors suffice.

## Proof of the finite-jet formula

Along the horizontal line, let

\[
 A_k(x)=\operatorname{Re}F^{(k)}(1/2+x+iT).
\]

Then `d A_k/dx=A_{k+1}` and

\[
 \frac d{du}=\frac1{2x}\frac d{dx}.
\]

The claimed formula is true for `n=0`, since `m_0=A_0/x`. Suppose it holds for
`n`. A term with index `k` has the form

\[
 c_{n,k}A_k x^{-(2n-k+1)},
\]

where

\[
 c_{n,k}=(-1)^k
 \frac{(2n-k)!}{2^{2n-k}n!k!(n-k)!}.
\]

Since

\[
 m_{n+1}=-\frac1{n+1}\frac1{2x}\frac d{dx}m_n,
\]

this term contributes

\[
 \frac{2n-k+1}{2(n+1)}c_{n,k}
 A_kx^{-(2n-k+3)}
\]

to the next coefficient at `k`, and

\[
 -\frac1{2(n+1)}c_{n,k}
 A_{k+1}x^{-(2n-k+2)}
\]

to the next coefficient at `k+1`. Direct factorial simplification shows that
the sum of the two contributions equals `c_{n+1,k}` for every interior index,
with the same identity at both endpoints. This completes the induction.

## Identification of the scalar localizer

The first two moments from the finite-jet formula are

\[
 m_0=\frac{A_0}{x},
 \qquad
 m_1=\frac{A_0}{2x^3}-\frac{A_1}{2x^2}.
\]

Since `u=x^2`,

\[
 m_0-u m_1
 =\frac{A_0}{2x}+\frac{A_1}{2}
 =\frac12\mathcal D(s).
\]

The converse part of `L-4101` therefore proves existential completeness of the
finite hierarchy.

## Certificate schema consequence

A compact `B_N` certificate should contain:

1. exact dyadic `x,T` with `x>0` and exact `u=x^2`;
2. the matrix order `N` and kind `hankel` or `localizing`;
3. an exact nonzero dyadic vector `c`;
4. directed complex balls for a direct `xi` jet through order `2N+2`, or
   directed balls for `F^(k)` through the required order;
5. proof that the denominator ball used in logarithmic-series division excludes
   zero;
6. outward real intervals for every reconstructed `m_n`;
7. one exact interval quadratic-form evaluation whose upper endpoint is
   negative;
8. producer, library, normalization, and precision fingerprints.

The checker need not compute eigenvalues. It reevaluates or independently
checks the jet, reconstructs the moments using the exact coefficient formula,
and evaluates one fixed-vector quadratic form.

## Analytic domain audit

- `xi` is entire; `F` and its derivatives are meromorphic at zeros of `xi`.
- Every evaluation point lies in `Re(s)>1/2` and must be certified nonzero.
- The transformation `u=x^2` uses positive real `x`; no complex square-root
  branch enters the certificate.
- Under RH, the Stieltjes and differentiated moment series converge locally
  uniformly for `u>0`.
- The moment matrices are finite. No limiting matrix positivity is needed for a
  counterexample certificate.

## Dependency audit

- `D-3201` fixes the completed `xi`, the corrected logarithmic derivative, and
  the shifted half-plane.
- `L-3201` supplies the conditional Poisson/resolvent sum.
- `L-4101` supplies the right-side converse and identifies the one-by-one
  localizer as an existentially complete subcriterion.
- The higher matrix positivity is proved directly here and does not invoke a
  separate moment-problem theorem.

## Gap audit

- The moments use `d/du` at fixed `T`, not derivatives in the vertical
  direction.
- The factor `(-1)^n/n!`, every power of `2`, and the real part of the complex
  derivative are essential.
- The localizer is `m_n-u m_{n+1}`. Reversing the sign would test a polynomial
  that is nonpositive on the support.
- `(B_0)_{00}=D/2`, not `D`.
- A midpoint moment matrix may appear indefinite from cancellation. Promotion
  requires a fixed exact vector and an outward negative upper endpoint.
- A finite list of positive matrices cannot prove RH. It is only a negative
  witness hierarchy.
- High derivative orders can be severely ill-conditioned near a zero; precision
  must be escalated until every division and final sign is resolved.
- A fitted Padé/Stieltjes model may nominate a vector but cannot enter the proof
  object.

## Adversarial tests

1. For a finite synthetic set of critical-line ordinates, compute `m_n` both
   from the explicit positive sum and from the exact finite-jet formula.
2. Check exact positive semidefiniteness through fixed-vector sums for several
   rational vectors and matrix orders.
3. Verify symbolically that `B_0=D/2`.
4. For the off-line quartet `{0.6+/-20i,0.4+/-20i}`, use
   `x=11/100,T=20`; require `Re F>0` but `(B_0)_{00}<0`.
5. Mutate one factorial or power of `2` in the jet conversion and require the
   direct-moment regression to fail.
6. Reverse the localizer sign and require the on-line support proof to fail.
7. Supply a zero-containing denominator ball and require `UNRESOLVED`.

## Remaining uncertainty

No mathematical gap is known. It is not yet known whether matrices larger than
`B_0` provide materially wider or better-conditioned witness basins for the
actual `xi` function above the verified height.

## Suggested next attack

Extend the exact synthetic prototype first, then add `xi` logarithmic-series
jets to Issue #39. Compare scalar, differential, `2 x 2`, and `3 x 3`
localizing margins around the same reconnaissance points. Freeze any negative
direction to dyadics before ball escalation.