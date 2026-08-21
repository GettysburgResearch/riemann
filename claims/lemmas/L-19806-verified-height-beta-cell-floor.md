# L-19806 — Verified-height lower floor for the beta square-cell criterion

Claim ID: `L-19806`  
Title: Certified critical-line zeros below the square-root height contribute positively, while the complete unverified tail costs only logarithmically  
Status: `PROPOSED — COMPLETE FINITE-HEIGHT CONSEQUENCE`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `T-19804`; `L-19805`; exact zero-count certification below a finite height

## 1. Setting

Use the beta-smoothed square-cell scalar

\[
\mathscr C_\beta(n)
 =\int_0^1 30u^2(1-u)^2
 \Psi(\log(n^2+(2n+1)u))du.
\tag{L-19806.1}
\]

Its zero-side expansion is

\[
\mathscr C_\beta(n)
 =\sum_\gamma m_\gamma
 {1-J_{\beta,n}(\gamma)\over\gamma^2},
\tag{L-19806.2}
\]

where

\[
J_{\beta,n}(\gamma)
 =\int_0^1 30u^2(1-u)^2
 (n^2+(2n+1)u)^{-i\gamma}du.
\tag{L-19806.3}
\]

## 2. Every certified line-zero pair is nonnegative

Let `gamma` be real. Then

\[
J_{\beta,n}(-\gamma)
 =\overline{J_{\beta,n}(\gamma)}
\tag{L-19806.4}
\]

and positivity of the averaging measure gives

\[
|J_{\beta,n}(\gamma)|\le1.
\tag{L-19806.5}
\]

Therefore the paired contribution is

\[
\boxed{
{1-J_{\beta,n}(\gamma)\over\gamma^2}
+{1-J_{\beta,n}(-\gamma)\over\gamma^2}
={2(1-\Re J_{\beta,n}(\gamma))\over\gamma^2}
\ge0.}
\tag{L-19806.6}
\]

Multiplicity only multiplies this nonnegative quantity.

Thus any finite proof-grade zero census showing that every zero in a symmetric
ordinate slab lies on the critical line contributes a rigorously nonnegative
block; individual zero phases need not be evaluated.

## 3. Complete unverified tail

Fix `A>0`. Suppose every nontrivial zero whose centered ordinate satisfies

\[
|\Re\gamma|<An
\tag{L-19806.7}
\]

has been certified on the critical line, with complete multiplicity and endpoint
semantics.

By Section 2, the entire inner zero block is nonnegative. By `L-19805`, the
complete outer block, including every unverified on-line or off-line zero,
satisfies

\[
\left|
\sum_{|\Re\gamma|\ge An}
 m_\gamma{1-J_{\beta,n}(\gamma)\over\gamma^2}
\right|
\le C_{\beta,A}\log(n+2).
\tag{L-19806.8}
\]

Consequently

\[
\boxed{
\mathscr C_\beta(n)
 \ge-C_{\beta,A}\log(n+2).}
\tag{L-19806.9}
\]

The constant is effective once an explicit Riemann--von Mangoldt unit-interval
count bound is inserted into the proof of `L-19805`.

## 4. Prime-side finite comparison

`T-19804` supplies the independent finite-prime identity

\[
\mathscr C_\beta(n)
 =\mathcal B_\beta(n)-\mathcal R_\beta(n),
\tag{L-19806.10}
\]

where the prime sum is complete through `(n+1)^2` with explicit nonnegative
weights. Therefore a directed production level has two independent routes:

1. prime side: evaluate (L-19806.10) directly;
2. zero side: retain no individual phase below `An`, use only certified line
   location and (L-19806.6), then apply the universal high-tail radius
   (L-19806.8).

Their intervals must overlap. A discrepancy is a normalization, manifest, or
zero-census failure; it is not silently widened away.

## 5. Consequences and limitation

The logarithmic lower floor is already at the subpolynomial RH scale. However,
for one fixed finite verified height `H`, equation (L-19806.9) applies only to

\[
n<H/A.
\tag{L-19806.11}
\]

It cannot be extended cofinally without an unbounded verified-height theorem or
a direct proof of the prime-side inequalities. Thus finite zero verification
can certify an enormous initial square-cell ladder but cannot by itself prove
RH.

Conversely, a strict prime-side upper interval

\[
\mathscr C_\beta(n)<-C_{\beta,A}\log(n+2)
\]

at a level whose inner zero census is complete would force an off-line zero
above the retained height or expose a producer error. With two independently
verified producers, it becomes a finite off-line-zero witness.

## 6. Proof boundary

- Positivity of the certified line-zero block is exact.
- The high-zero radius is unconditional but must be instantiated with explicit
  constants for production.
- A finite verified height does not supply a cofinal proof.
- No current production beta-cell interval or explicit tail constant is claimed
  here.