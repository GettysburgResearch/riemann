# L-26001 — Conditional Hankel positivity forces derivative-kernel positivity

Claim ID: `L-26001`  
Title: A conditionally positive Hankel kernel of order one has a positive semidefinite second-derivative Hankel kernel  
Status: **PROPOSED COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Scope: audit of PR #243 and `R-9510`

## 1. Statement

Let `I` be an open interval and let `f` be `C^2` on `I+I`. Assume that the
Hankel kernel

\[
K_f(x,y)=f(x+y)
\]

is conditionally positive semidefinite of order one: for every finite set
`x_1,...,x_n` in `I` and every real vector `c` with

\[
\sum_i c_i=0,
\]

one has

\[
\sum_{i,j}c_i c_j f(x_i+x_j)\ge0.
\tag{L-26001.1}
\]

Then the second-derivative Hankel kernel

\[
K_{f''}(x,y)=f''(x+y)
\]

is positive semidefinite on the interior: for arbitrary real `a_1,...,a_n`,

\[
\boxed{
\sum_{i,j}a_i a_j f''(x_i+x_j)\ge0.}
\tag{L-26001.2}
\]

Consequently every two-point Gram of `f''(x+y)` has nonnegative determinant.
A negative local determinant for `f''` refutes conditional positivity of
`f(x+y)`, not merely ordinary unconstrained Hankel positivity.

## 2. Proof

Fix interior points `x_i` and choose `h>0` small enough that `x_i+h` remains in
`I`. Define the finite signed measure

\[
\mu_h={1\over h}\sum_i a_i(\delta_{x_i+h}-\delta_{x_i}).
\tag{L-26001.3}
\]

Its total mass is exactly zero, independently of the values of `a_i`. Applying
(L-26001.1) to the coefficients of `mu_h` gives

\[
0\le \iint f(x+y)\,d\mu_h(x)d\mu_h(y).
\]

Expanding,

\[
\begin{aligned}
0\le
\sum_{i,j}a_i a_j
{f(x_i+x_j+2h)-2f(x_i+x_j+h)+f(x_i+x_j)\over h^2}.
\end{aligned}
\tag{L-26001.4}
\]

Since `f` is `C^2`, the centered forward second difference in (L-26001.4)
converges to `f''(x_i+x_j)` as `h` tends to zero. Taking the limit proves
(L-26001.2).

For two points `u,v`, positive semidefiniteness gives

\[
\det
\begin{pmatrix}
f''(2u)&f''(u+v)\\
f''(u+v)&f''(2v)
\end{pmatrix}
\ge0.
\tag{L-26001.5}
\]

This completes the proof.

## 3. Application to `R-9510`

PR #243 proposes a zero-mass conditional-Hankel square whose derivative kernel
is the interior spline kernel `F_T''(x+y)`. `R-9510` computes, in the first open
cell,

\[
F_T''\,(F_T'')''-((F_T'')')^2=-{233\over64}<0.
\]

Equivalently, sufficiently close two-point Grams of the derivative kernel have
negative determinant. By the theorem above, this is incompatible with the
claimed zero-mass conditional positivity.

Thus the reviewer’s local determinant is a valid obstruction to the proposed
conditional-Hankel middle line, even though an arbitrary two-point vector need
not itself have zero sum. The finite-difference lift (L-26001.3) supplies the
required zero-mass witness.

## 4. Exact scope

This confirms the following narrow verdict.

```text
PR #243 positive-Bernstein / conditional-Hankel derivation   REFUTED
PR #243 displayed carry-profile positivity statement         NOT DISPROVED
RH                                                             UNPROVED
```

The theorem does not establish that the carry profile changes sign. It prevents
an incorrect “refutation of the refutation” based solely on the zero-mass
constraint.
