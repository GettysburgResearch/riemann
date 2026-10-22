# M-23801 — Greedy carry mass review and proof program

Methodology ID: `M-23801`  
Title: Prove or refute the elementary carry proposal through one pivot-potential theorem, one quotient-layer ledger, and a fail-closed producer  
Status: **PROPOSED RESEARCH AND REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238

## 1. Frozen logical spine

The proposal to review is

```text
exact average carry matrix
-> canonical descending nonnegative packing
-> weighted mass 8 sqrt(X)-X^(o(1))
-> entropy value 4 sqrt(X)-X^(o(1))
-> prime ramp lower bound
-> upper square-screw envelope
-> Landau continuation
-> RH.
```

Every arrow except the greedy mass theorem is independently stated in
`L-23801`--`L-23805` and `T-23802`.

## 2. Why this target is narrower than Carry Saturation

The producer is always feasible. It may:

- pivot at an off-diagonal column;
- skip many subsequent rows;
- leave positive terminal residuals;
- differ completely from the signed triangular inverse.

Only the scalar mass

\[
\sum_n n d_X^{\rm gr}(n)
\]

must be sharp. Pointwise positivity of the exact inverse, a nonnegative carry
cover, and equality in every carry column are not required.

## 3. Pivot forest

At a nonzero step `n`, let `p(n)` be the least column attaining the exact
minimum

\[
\rho^{(n)}(q)/\beta_{nq}.
\]

The update saturates column `p(n)`. Every row below `n` that still sees this
column has zero admissible increment until the row index falls below `p(n)`.
Thus the nonzero rows form a strictly descending pivot forest

```text
n_0 > p(n_0)-1 >= n_1 > p(n_1)-1 >= n_2 > ... .
```

Exact Carry Saturation is the special case `p(n)=n`. GCM permits off-diagonal
pivots but requires their cumulative lost potential to be subpolynomial.

## 4. Positive pivot potential

For a fixed constant `0<C<=2 sqrt(2)`, put

\[
a_C(q)=2-Cq^{-1/2}\ge0.
\tag{M-23801.1}
\]

The initial target potential is

\[
\boxed{
\sum_{q=2}^X a_C(q)w_X(q)
=8\sqrt X+O_C(\log^2X).}
\tag{M-23801.2}
\]

This follows by elementary integral comparison:

\[
2\sum_{q\le X}q^{-1/2}\log(X/q)=8\sqrt X+O(\log X),
\]

while

\[
C\sum_{q\le X}q^{-1}\log(X/q)=O_C(\log^2X).
\]

The first source-free target is the row inequality

\[
\boxed{
\sum_{q=2}^n a_C(q)\beta_{nq}\le n
\qquad(n\ge2).}
\tag{M-23801.3}
\]

Reconnaissance strongly favors `C=1`; the larger review-safe choice
`C=2 sqrt(2)` leaves more room while preserving nonnegativity and the sharp
leading constant.

If (M-23801.3) holds, every greedy subtraction of size `d(n)` consumes at most
`n d(n)` units of pivot potential. Therefore

\[
\sum_n n d_X^{\rm gr}(n)
\ge
\sum_q a_C(q)w_X(q)
-
\sum_q a_C(q)\rho_X^{\rm final}(q).
\tag{M-23801.4}
\]

GCM is reduced to the finite residual theorem

\[
\boxed{
\sum_q a_C(q)\rho_X^{\rm final}(q)=X^{o(1)}.}
\tag{M-23801.5}
\]

Equations (M-23801.3)--(M-23801.5) are a preferred two-lemma closure of the
proposal. A different potential is permitted if it has the same sharp initial
mass and nonnegative weights.

## 5. Proposed proof of the row inequality

Write

\[
S_0(n)=\sum_{q=2}^n\beta_{nq},
\qquad
S_{1/2}(n)=\sum_{q=2}^n{\beta_{nq}\over\sqrt q}.
\]

Then (M-23801.3) is

\[
2S_0(n)-C S_{1/2}(n)\le n.
\tag{M-23801.6}
\]

The carry coefficients are a Riemann sum for the kernel `K` of `L-23805`.
The main term is

\[
S_0(n)={n\over2}+O(\sqrt n),
\]

because

\[
\int_1^\infty K(x)x^{-2}dx={1\over2}.
\]

The correction has the positive square-root scale

\[
S_{1/2}(n)\asymp\sqrt n.
\]

A proof should split at `q=sqrt(n)`, group the range `q>sqrt(n)` by the exact
quotient `floor(n/q)`, and retain the correction before taking endpoint errors.
A proof that first bounds `S_0` and `S_(1/2)` independently with wasteful
constants is unlikely to close; the two sums must share the same quotient
ledger.

## 6. Proposed proof of the residual theorem

For each quotient layer

\[
{X\over r+1}<m\le {X\over r},
\]

the Möbius transform in `L-23803` uses only `mu(1),...,mu(r)`.
The review target is a block inequality, not termwise monotonicity:

\[
\sum_{q\in\mathcal Q_r}
 a_C(q)\rho^{\rm final}(q)
\le E_r(X),
\qquad
\sum_rE_r(X)=X^{o(1)}.
\tag{M-23801.7}
\]

Suggested mechanisms, in preferred order:

1. **pivot charging:** charge every skipped column to the saturated pivot that
   caused the skip and prove a strict contraction in the `a_C` potential;
2. **complete quotient-layer recombination:** use the affine Möbius identity
   of `L-23803` before any absolute value;
3. **block LP repair:** solve one exact finite packing on a complete quotient
   layer and export its rational/directed dual certificate;
4. **high-order Euler smoothing:** average a block of adjacent rows, annihilate
   the continuum kernel moments, and retain only endpoint errors;
5. **balanced-Type-II import:** as a last resort, bind the residual potential
   to a source-specific BTP estimate without claiming an independent elementary
   proof.

The first three mechanisms would give a genuinely elementary proof.

## 7. Prime-power-column variant

Because `Lambda(q)=0` away from prime powers, the packing implication itself
needs constraints only at prime-power columns. Dropping the other columns gives
a larger feasible cone and may produce a simpler certificate. Such a variant
must be stated separately:

\[
\sum_n d_n\beta_{nq}\le w_X(q)
\quad\text{only for }q=p^a.
\]

It still implies the same prime-ramp lower bound. A proof object must not mix
this weaker constraint set with all-column claims such as `L-23804.6` unless a
replacement coefficient-mass bound is supplied.

## 8. Automatic rejection conditions

Reject a claimed proof if it:

```text
uses the signed triangular inverse as a nonnegative vector without proof
checks only finitely many endpoints
bounds Möbius quotient terms separately before recombination
uses floating minima without directed separation
forgets prime powers
obtains only (8-c)sqrt(X) for a fixed c>0
loses sqrt(X)/log(X), which is still exponential on logarithmic scale
uses a lower screw envelope when the packing supplies the upper orientation
claims the continuum mass eight proves positivity
```

The error must be `X^(o(1))`, not merely `o(sqrt(X))`.

## 9. Review order

1. `L-23801` — exact carry and entropy identity.
2. `L-23804` — one-sided packing and screw orientation.
3. `L-23805` — continuum symbol and constant eight.
4. `L-23802` — greedy producer.
5. `L-23803` — Möbius firewall.
6. `T-23802` — conditional full composition.
7. finite reconnaissance and proof-object schema.
8. proposed row-potential and residual theorems.

## 10. Status boundary

```text
finite carry algebra                    PROPOSED EXACT
canonical nonnegative producer          PROPOSED EXACT
coefficient-mass/entropy conversion      PROPOSED EXACT
one-sided screw transfer                 PROPOSED EXACT
continuum symbol and mass eight          PROPOSED EXACT
row-potential inequality                 OPEN
subpolynomial final residual potential   OPEN
greedy carry mass theorem                OPEN
RH                                       UNPROVED
```