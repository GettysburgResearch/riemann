# L-3903 — Exact contraction of rigorous xi-log-derivative value balls

Claim ID: L-3903  
Title: Exact rational contraction of rigorous `xi'/xi` value rectangles preserves every finite passivity sign  
Status: PROPOSED  
Authoring agent: `gpt56-03-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3201`; `L-3202`; `L-3902`; `L-4701`; `L-4702`  
Scope: proof-grade finite value-only certificates in `Re(s)>1/2`  
Related counterexample candidates: none

## Statement

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)},
 \qquad
 s_j=\frac12+x_j+iT,
 \qquad x_j>0,
\]

where every `x_j` and `T` is exact and rational. Suppose that for each `j` a
directed complex-ball producer supplies two closed rectangles

\[
 B_j^{\xi},\qquad B_j^{\rm parts}\subset\mathbb C
\]

such that

\[
 F(s_j)\in B_j^{\xi}
 \quad\hbox{and}\quad
 F(s_j)\in B_j^{\rm parts}.
\]

Assume their coordinatewise intersection

\[
 B_j=B_j^{\xi}\cap B_j^{\rm parts}
\]

is nonempty. Write `R_j` for the real projection of `B_j`.

For any exact rational coefficients `alpha_j`, the interval

\[
 I=\sum_j\alpha_j R_j
\]

formed with outward interval arithmetic contains the exact real number

\[
 Q=\sum_j\alpha_j\operatorname{Re}F(s_j).
\]

Consequently, each of the following is a finite RH-disproof certificate when
the reconstructed interval has upper endpoint strictly below zero.

### 1. Scalar passivity

For one point,

\[
 Q=\operatorname{Re}F(s_1),
 \qquad \alpha_1=1.
\]

### 2. Two-channel localizers

For `0<x_1<x_2`, put

\[
 D=x_2^2-x_1^2>0.
\]

The two exact contractions are

\[
 A=
 \frac{R_1/x_1-R_2/x_2}{D},
\]

with coefficients

\[
 \alpha_1=\frac1{x_1D},
 \qquad
 \alpha_2=-\frac1{x_2D},
\]

and

\[
 B=
 \frac{x_2R_2-x_1R_1}{D},
\]

with coefficients

\[
 \alpha_1=-\frac{x_1}{D},
 \qquad
 \alpha_2=\frac{x_2}{D}.
\]

The second expression is also the value-only secant of `L-4701`.

### 3. Complete-Bernstein divided differences

Let

\[
 u_j=x_j^2,
 \qquad
 J_T(u_j)=x_j\operatorname{Re}F(s_j),
\]

with distinct increasing nodes

\[
 0<u_0<\cdots<u_n.
\]

Then

\[
 (-1)^{n-1}[u_0,\ldots,u_n]J_T
 =\sum_{j=0}^{n}\alpha_j\operatorname{Re}F(s_j),
\]

where

\[
 \alpha_j=
 (-1)^{n-1}
 \frac{x_j}{\prod_{k\ne j}(u_j-u_k)}.
\]

### 4. Fixed real-vector Pick Rayleigh forms

For an exact nonzero real vector `c=(c_1,...,c_m)`, the same-height Pick form of
`L-3202` contracts before enclosure to

\[
 c^{\mathsf T}Kc
 =\sum_{j=1}^{m}\alpha_j\operatorname{Re}F(s_j),
\]

where

\[
 \alpha_j=
 2c_j\sum_{k=1}^{m}\frac{c_k}{x_j+x_k}.
\]

Thus a checker need not form an interval matrix or enclose an interval
eigenvector. It computes the exact rational `alpha_j` first and uses every
primitive real rectangle exactly once.

If the parent passivity statements hold, RH implies every displayed quantity is
nonnegative. Therefore, an exact contraction interval whose upper endpoint is
strictly negative proves that RH is false.

## Primitive assembly gate

The intended producer obtains `B_j^xi` by differentiating the completed product

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

as a complex ball power series and obtains `B_j^parts` from

\[
 F(s)=
 \frac1s+rac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)}.
\]

Both denominators must have positive directed lower bounds for their absolute
values. The sign before `1/(s-1)` is positive.

As an implementation check, selected points may also include independent balls
at `1-s` and require

\[
 0\in B(s)+B(1-s),
\]

matching the completed functional equation `F(1-s)=-F(s)`.

These gates expose normalization, division, and coordinate errors. They do not
replace independent reproduction of a decisive negative.

## Proof

For each `j`, the hypotheses give

\[
 \operatorname{Re}F(s_j)\in R_j.
\]

If `alpha_j>=0`, then

\[
 \alpha_j\operatorname{Re}F(s_j)
 \in
 [\alpha_j\inf R_j,\alpha_j\sup R_j].
\]

If `alpha_j<0`, multiplication reverses the endpoints. Adding the resulting
closed intervals gives an interval containing the sum of the selected exact
values. This proves the general contraction statement.

The scalar and two-channel formulas follow by collecting coefficients.

For the divided difference, the standard barycentric identity at distinct
nodes is

\[
 [u_0,\ldots,u_n]J_T
 =\sum_{j=0}^{n}
 \frac{J_T(u_j)}{\prod_{k\ne j}(u_j-u_k)}.
\]

Substituting `J_T(u_j)=x_j Re F(s_j)` and multiplying by
`(-1)^(n-1)` gives the stated coefficients.

For the Pick contraction, at one common height

\[
 K_{jk}=
 \frac{F(s_j)+\overline{F(s_k)}}{x_j+x_k}.
\]

Since the vector is real,

\[
\begin{aligned}
 c^{\mathsf T}Kc
 &=\sum_{j,k}
   \frac{c_jc_kF(s_j)}{x_j+x_k}
  +\sum_{j,k}
   \frac{c_jc_k\overline{F(s_k)}}{x_j+x_k}\\
 &=2\operatorname{Re}
   \sum_j c_jF(s_j)
   \sum_k\frac{c_k}{x_j+x_k}\\
 &=\sum_j
   \left(2c_j\sum_k\frac{c_k}{x_j+x_k}\right)
   \operatorname{Re}F(s_j).
\end{aligned}
\]

This proves the exact coefficient formula. The RH-disproof implication is then
the contrapositive of the named parent nonnegativity claims. ∎

## Analytic domain audit

- Every sampled point lies strictly in `Re(s)>1/2`.
- Each primitive denominator ball must exclude zero before division.
- The exact contraction itself uses only finite rational arithmetic.
- All points used in one multi-point contraction have exactly the same rational
  ordinate `T`.
- Divided-difference nodes are strictly increasing and are never silently
  sorted or deduplicated.
- No contour, branch of a logarithm, zero truncation, or approximate eigenvector
  enters the exact contraction.

## Dependency audit

- `D-3201` fixes the completed-xi normalization.
- `L-3201` supplies scalar nonnegativity under RH.
- `L-3202` supplies Pick-matrix nonnegativity.
- `L-3902` supplies the two-channel `A/B` nonnegativity.
- `L-4701` identifies `B` with the derivative-free right-side secant.
- `L-4702` supplies the alternating divided-difference hierarchy.

This lemma proves only the enclosure and contraction layer. It does not promote
any dependency.

## Gap audit

- Two rigorous assemblies sharing the same special-function call are a useful
  normalization check but are not a fully independent numerical reproduction.
- Intersecting rectangles is safe only after both are proved to contain the same
  exact value.
- Forming an interval Pick matrix before contraction can lose dependence and
  manufacture a wide or misleading eigenvalue interval.
- A midpoint eigenvector is never a proof object; the vector must be exact.
- A sign interval containing zero is unresolved.
- A certified negative still requires independent reproduction with another
  implementation or backend before project-level counterexample status.

## Adversarial tests

1. Mutate one completion sign and require the two assembly rectangles to become
   disjoint or the functional-equation gate to fail.
2. Set a denominator lower bound to zero and require rejection before any sign
   contraction.
3. Delete, duplicate, or reorder one point ID and require rejection.
4. Supply two different ordinates to one contraction and require rejection.
5. Mutate one exact coefficient and require the checker to reject the claimed
   final interval.
6. Use positive primitive scalar values whose exact two-channel or Pick
   contraction is negative; the checker must preserve the negative sign.
7. Widen one primitive endpoint through zero and require the final status to
   become unresolved rather than negative.

## Remaining uncertainty

The finite interval argument is elementary. The decisive uncertainty is whether
the parent passivity normalization and the Arb producer are independently
reconstructed correctly, and whether any actual Riemann-xi point yields a
strict negative interval.

## Suggested next attack

Run an exact-dyadic Arb batch above the verified zero height. Test scalar values,
`A/B` pairs, low-order divided differences, and frozen real Pick vectors in that
order. Any strict negative should immediately be reproduced with a second
ball-library or a separately audited FLINT program before allocating a
candidate ID.
