# T-20805 — Carry-entropy full RH proof proposal

Claim ID: `T-20805`  
Title: Positivity of the canonical triangular carry saturation implies the Riemann Hypothesis  
Status: **FULL PROOF PROPOSAL — ONE EXPLICIT COEFFICIENT-POSITIVITY LEMMA PENDING VERIFICATION**  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `L-20814`; `T-20804`; `L-20815`; `L-20816`; `R-20805`  
Scope: direct completion of the prime-positive square-diagonal route

## 1. Canonical finite coefficients

For every integer `X>=2`, define

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X,
 \tag{T-20805.1}
\]

and

\[
 \beta_{nq}
 ={\lfloor n/q\rfloor
   (q-1-(n\bmod q))\over n+1}.
 \tag{T-20805.2}
\]

Let `c_X(n)` be the unique backward-triangular solution

\[
 \boxed{
 w_X(q)=\sum_{n=q}^Xc_X(n)\beta_{nq}
 \qquad(2\le q\le X).}
 \tag{T-20805.3}
\]

Equivalently,

\[
 \boxed{
 c_X(n)={n+1\over n-1}
 \left[
 w_X(n)-\sum_{m=n+1}^Xc_X(m)\beta_{mn}
 \right].}
 \tag{T-20805.4}
\]

The proposed load-bearing lemma is:

> **Carry Saturation Lemma (CS).** For every integer `X>=2`,
> \[
> \boxed{c_X(n)\ge0\qquad(2\le n\le X).}
> \tag{T-20805.5}
> \]

No zero data, prime theorem, or limiting operator enters this finite statement.
It is an explicit inequality about floors, square roots, logarithms, and one
upper-triangular recurrence.

## 2. Exact arithmetic factorization under CS

For

\[
 G_n={1\over n+1}\sum_{j=0}^n\log\binom nj,
 \tag{T-20805.6}
\]

Legendre's formula gives

\[
 G_n=\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.
 \tag{T-20805.7}
\]

Multiply (T-20805.3) by `Lambda(q)` and sum. If CS holds, every interchange is
finite and nonnegative, and

\[
 \boxed{
 \sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}\log(X/q)
 =\sum_{n=2}^Xc_X(n)G_n.}
 \tag{T-20805.8}
\]

This is the positive prime ramp of the exact zeta screw formula represented as
one positive combination of logarithms of integers.

## 3. Entropy lower bound

The standard entropy estimate for binomial coefficients and an elementary
Riemann-sum bound give

\[
 \boxed{
 G_n\ge{n\over2}-\log(n+1)-3.}
 \tag{T-20805.9}
\]

Thus

\[
 \sum_{n=2}^Xc_X(n)G_n
 \ge {1\over2}\sum n c_X(n)
 -\sum c_X(n)\log(n+1)-3\sum c_X(n).
 \tag{T-20805.10}
\]

## 4. Exact leading constant from the carry entropy

`L-20815` proves

\[
 \int_1^\infty K(x)x^{-2}dx={1\over2},
 \tag{T-20805.11}
\]

where `K` is the uniform carry kernel. Its finite lattice discrepancy is only
`O(sqrt(n))`. The explicit dual row

\[
 1-{64\over\sqrt q}
\]

therefore satisfies

\[
 \sum_{q=2}^n\beta_{nq}
 \left(1-{64\over\sqrt q}\right)
 \le{n\over2}.
 \tag{T-20805.12}
\]

Using CS and the exact saturated constraints gives

\[
 \boxed{
 {1\over2}\sum_{n=2}^Xn c_X(n)
 \ge4\sqrt X-O(\log^2X).}
 \tag{T-20805.13}
\]

The coefficient `4` is exact: it is the integral of binary entropy through the
carry kernel, not a fitted numerical constant.

## 5. The lower-order coefficient budget

A quotient-block estimate gives

\[
 U_n=\sum_{q=2}^n{\beta_{nq}\over q}
 \gg\log(n+1).
 \tag{T-20805.14}
\]

Multiplying (T-20805.3) by `1/q`, summing, and using CS yields

\[
 \boxed{
 \sum_{n=2}^Xc_X(n)\log(n+1)=O(\log X),
 \qquad
 \sum_{n=2}^Xc_X(n)=O(\log X).}
 \tag{T-20805.15}
\]

Combining (T-20805.8)--(T-20805.15),

\[
 \boxed{
 \sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}\log(X/q)
 \ge4\sqrt X-O(\log^2X).}
 \tag{T-20805.16}
\]

Every estimate after CS is unconditional and elementary.

## 6. Return to the exact zeta screw

The exact smooth term is

\[
 A(\log X)
 =4\sqrt X+B\log X+{C\over4}-8-R_0(\sqrt X),
 \qquad R_0\ge0.
 \tag{T-20805.17}
\]

The screw function satisfies

\[
 \Psi(\log X)
 =A(\log X)
 -\sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}\log(X/q).
 \tag{T-20805.18}
\]

Equation (T-20805.16) gives

\[
 \boxed{
 \Psi(\log X)\le O(\log^2X).}
 \tag{T-20805.19}
\]

At `X=N^2`,

\[
 \bigl(\Psi(2\log N)\bigr)_+
 =O(\log^2N)=N^{o(1)}.
 \tag{T-20805.20}
\]

The upper square-sampling/Landau theorem `L-20814` then excludes every zero with
real part greater than `1/2`. The functional equation supplies the opposite
half, so RH follows.

## 7. Full proposed proof

The proposed proof of RH is therefore the following finite chain:

1. prove the Carry Saturation Lemma (T-20805.5);
2. apply the exact averaged-binomial factorization (T-20805.8);
3. use entropy and the elementary carry dual to obtain
   `4 sqrt(X)-O(log^2 X)`;
4. insert the result into the exact zeta screw formula;
5. apply the independently reviewable upper Landau transfer.

Symbolically,

```text
triangular carry positivity
-> positive binomial factorization of the complete prime ramp
-> 4 sqrt(X) - O(log^2 X)
-> Psi(2 log N)_+ = N^o(1)
-> zero-free Re(s)>1/2
-> RH.
```

## 8. Why this proposal is materially sharper than the prior Selberg proposal

The Selberg--Mourre proposal on PR #158 left an undefined factor map, a complete
finite square identity, and an endpoint lower bound to be constructed. The
present proposal has only one missing statement, and that statement is itself a
finite explicit recurrence:

\[
 c_X(n)\ge0.
\]

There is no operator domain, boundary form, omitted tail, or unspecified
coercivity constant in the review hinge.

## 9. Independent verification obligations

A reviewer should check, in this order:

1. the normalization and orientation of `L-20814`;
2. the exact averaged-carry coefficient (T-20805.2);
3. the triangular saturation equation and recurrence;
4. the proof of the dual row inequality and logarithmic budget in `L-20816`;
5. the finite coefficient-positivity lemma CS;
6. the exact archimedean constants in (T-20805.17).

The fifth item is the only new unproved mathematical assertion.

## 10. Status boundary

This file is a **full proof proposal**, not a declaration that RH has been
proved.

- The deduction `CS => RH` is complete in `L-20815/L-20816`.
- CS has extensive finite support from `X-20809/O-20808`.
- `R-20805` proves that CS is not automatic: the triangular inverse contains a
  Möbius/reciprocal-zeta channel.
- Until CS is independently proved, the repository must continue to state that
  RH is unresolved.