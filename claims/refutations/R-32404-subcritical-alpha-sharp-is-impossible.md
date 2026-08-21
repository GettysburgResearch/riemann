# R-32404 — Subcritical alpha-SHARP is impossible

Claim ID: `R-32404`  
Title: For every fixed `0<alpha<1/2`, the average-carry inverse of the fractional hinge cannot remain nonnegative cofinally; the known critical-line zeros force sign changes already in the fixed row-two/row-three combination  
Status: **PROPOSED COMPLETE ANALYTIC REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32408`; corrected `T-32403`; Hardy's theorem that zeta has infinitely many zeros on `Re s=1/2`; Landau's one-sign theorem  
Scope: refutes average-row fractional SHARP for every exponent strictly below one half; does not refute other non-average-row carry constructions

## 1. Fractional average-row inverse

Fix

\[
 0<\alpha<{1\over2}
\]

and define the endpoint-vanishing hinge

\[
 h_{T,\alpha}(q)=q^{-\alpha}-T^{-\alpha},
 \qquad2\le q\le T.
\tag{R-32404.1}
\]

Let `c_(T,alpha)(j)` be its unique triangular inverse in the average-carry matrix of PR #329:

\[
 h_{T,\alpha}(q)
 =\sum_{n=q}^T c_{T,\alpha}(n)\beta_{nq}.
\tag{R-32404.2}
\]

Put

\[
 N_{j,\alpha}(T)=j(j-1)c_{T,\alpha}(j).
\tag{R-32404.3}
\]

The row-dual coefficient algebra in `T-32403` is independent of the target. Therefore its five-to-one combination gives exactly

\[
\boxed{
 5N_{2,\alpha}(T)+N_{3,\alpha}(T)
 =-6D_\alpha(T),
}
\tag{R-32404.4}
\]

where

\[
\boxed{
 D_\alpha(T)
 =\sum_{2\le q\le T}\omega(q)
 \left(q^{-\alpha}-T^{-\alpha}\right),
 \qquad
 \omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu.
}
\tag{R-32404.5}

Equivalently,

\[
 5N_{2,\alpha}+N_{3,\alpha}
 =2[5c_{T,\alpha}(2)+3c_{T,\alpha}(3)].
\tag{R-32404.6}

## 2. Exact Mellin transform

The Dirichlet series of `omega` is

\[
 \Omega(s)
 ={(1-2^{-s})(2-2^{-s})\over\zeta(s)},
 \qquad \omega(1)=2.
\tag{R-32404.7}

For one integer `q`,

\[
 \int_q^\infty
 (q^{-\alpha}-T^{-\alpha})T^{-z-1}dT
 ={\alpha\over z(z+\alpha)}q^{-z-\alpha}.
\]

Hence

\[
\boxed{
 \int_1^\infty D_\alpha(T)T^{-z-1}dT
 ={\alpha\over z(z+\alpha)}
 \left[
 { (1-2^{-z-\alpha})(2-2^{-z-\alpha})
  \over\zeta(z+\alpha)}-2
 \right].
}
\tag{R-32404.8}

The `-2` is the omitted unit coefficient and is analytic in the open half-plane under discussion.

## 3. Every critical-line zero becomes a positive-real-part pole

The finite numerator factors in (R-32404.8) vanish only when

\[
 \Re(z+\alpha)=0
 \quad\text{or}\quad
 \Re(z+\alpha)=-1.
\]

They therefore cannot cancel a nontrivial zeta zero on the critical line.

By Hardy's theorem there are infinitely many zeros

\[
 \rho={1\over2}+i\gamma.
\]

Each produces an uncancelled pole of (R-32404.8) at

\[
\boxed{
 z_\rho={1\over2}-\alpha+i\gamma.
}
\tag{R-32404.9}

Because `alpha<1/2`, all of these poles have the strictly positive real part

\[
 {1\over2}-\alpha>0.
\]

This conclusion is unconditional; RH is not assumed.

## 4. There is no positive-real singularity

For positive real `z`, the argument `z+alpha` is positive real. Zeta has no zero on the positive real axis. At `z+alpha=1`, the zeta pole makes the reciprocal term vanish rather than diverge. The finite numerator and the omitted-unit term are regular.

Thus (R-32404.8) has no singularity at any positive real `z`.

## 5. Landau forces infinitely many sign changes

Suppose `D_alpha(T)` were eventually one-signed. After changing sign if necessary and adding a compactly supported correction, `D_alpha(e^t)` would give a nonnegative locally integrable function.

The poles (R-32404.9) force its Laplace transform to have positive abscissa of convergence. Landau's one-sign theorem would then force a singularity at the corresponding positive real boundary point. Section 4 proves that no positive-real singularity exists.

Therefore

\[
\boxed{
 D_\alpha(T)\text{ is not eventually one-signed}
 \qquad(0<\alpha<1/2).
}
\tag{R-32404.10}

In particular it changes sign arbitrarily far out in the continuous endpoint variable. The same conclusion holds on any sufficiently fine endpoint sampling for which the interpolation error is Mellin-holomorphic across `Re z=1/2-alpha`.

By (R-32404.4), the fixed positive row combination

\[
 5c_{T,\alpha}(2)+3c_{T,\alpha}(3)
\]

also cannot remain nonnegative cofinally.

Hence the all-row statement

\[
 c_{T,\alpha}(n)\ge0
 \quad\text{for every }n
\]

is impossible cofinally for every `alpha<1/2`.

## 6. Consequence: one half is the unique critical exponent for SHARP

`L-32408` remains correct: the logarithmic critical target is a positive hinge mixture for every `alpha<=1/2`. But the average-row positive realization can only plausibly close at the **boundary exponent**

\[
\boxed{\alpha=1/2.}
\]

For `alpha<1/2`, known critical-line zeros move into the positive Mellin half-plane and force sign oscillation. At `alpha=1/2`, those same poles sit exactly on the boundary `Re z=0`; the Landau contradiction disappears, and eventual positivity becomes equivalent to excluding only zeros to the right of the line.

This explains why directed finite tests can look positive for moderately large endpoints at exponents below one half and still be doomed asymptotically.

## 7. Proof boundary

Refuted, subject to review:

- cofinal average-row alpha-SHARP for every fixed `0<alpha<1/2`;
- any proof strategy which attempts to escape the RH-critical exponent by choosing a smaller fractional hinge exponent.

Retained:

- the positive target decomposition `L-32408`;
- the square-root `alpha=1/2` SHARP frontier;
- non-average-row fractional carry constructions, which are not addressed by this theorem;
- RH, which remains unproved.
