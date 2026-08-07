# L-15442 — Every regular-tail exponential moment decreases with the shift

Claim ID: `L-15442`  
Title: The completed-xi ratio defect has a strictly negative shift derivative at every positive Laplace scale  
Status: `PROPOSED — COMPLETE DIFFERENTIATION AND POSITIVE FACTORIZATION; POINTWISE SHIFT MONOTONICITY NOT CLAIMED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15434`; the positive theta integral for `xi` on the real axis; the absolutely convergent Euler logarithmic derivative for `Re z>1`  
Scope: ordered exponential moments for the final compact smoothed-Jordan certificate  
Related counterexample candidates: none

## 1. Notation

For

\[
0<s<1,
\qquad q>0,
\]

put

\[
N_s(q)
=\widehat n_s(q)
=\pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)},
\tag{L-15442.1}
\]

\[
A_s(q)
={\zeta(1+q)\over\zeta(1+s+q)},
\qquad
c_s={1\over\zeta(1+s)}.
\tag{L-15442.2}
\]

Then `L-15434` gives

\[
\boxed{
\widehat Y_s(q)
={N_s(q)\over q}\bigl(qA_s(q)-c_s\bigr).}
\tag{L-15442.3}
\]

The same lemma proves

\[
\boxed{qA_s(q)-c_s>0.}
\tag{L-15442.4}
\]

## 2. Logarithmic derivative of the beta factor

Let

\[
x=1+s+q.
\tag{L-15442.5}
\]

Differentiating (L-15442.1) gives

\[
\partial_s\log N_s(q)
={1\over2}\log\pi
-{1\over q+s}
-{1\over2}\psi\!\left({3+s+q\over2}\right).
\tag{L-15442.6}
\]

Use

\[
\psi\!\left({x+2\over2}\right)
=\psi(x/2)+{2\over x}
\tag{L-15442.7}
\]

and the completed logarithmic derivative

\[
{\xi'\over\xi}(x)
={1\over x}+{1\over x-1}
-{1\over2}\log\pi
+{1\over2}\psi(x/2)
+{\zeta'\over\zeta}(x).
\tag{L-15442.8}
\]

Then

\[
\boxed{
\partial_s\log N_s(q)
={\zeta'\over\zeta}(x)
-{\xi'\over\xi}(x).}
\tag{L-15442.9}
\]

This identity is the exact archimedean cancellation behind the shift derivative.

## 3. Positive factorization of the derivative

The remaining derivatives are

\[
\partial_s A_s(q)
=-A_s(q){\zeta'\over\zeta}(x)
\tag{L-15442.10}
\]

and

\[
{c_s'\over c_s}
=-{\zeta'\over\zeta}(1+s).
\tag{L-15442.11}
\]

Differentiate (L-15442.3), insert (L-15442.9)--(L-15442.11), and collect the
terms containing `zeta'/zeta(x)`.  They cancel exactly.  The result is

\[
\boxed{
\begin{aligned}
-\partial_s\widehat Y_s(q)
={N_s(q)\over q}\Bigg[&
 \bigl(qA_s(q)-c_s\bigr)
 {\xi'\over\xi}(1+s+q)\\
&+c_s\left(
 {\zeta'\over\zeta}(1+s+q)
 -{\zeta'\over\zeta}(1+s)
 \right)
\Bigg].
\end{aligned}}
\tag{L-15442.12}
\]

Every factor on the right is nonnegative, and the bracket is strictly positive.

### First term

The theta representation

\[
\xi(1/2+v)
=\int_0^\infty\Phi(u)\cosh(vu)\,du,
\qquad
\Phi(u)>0,
\tag{L-15442.13}
\]

implies

\[
\boxed{{\xi'\over\xi}(x)>0\qquad(x>1/2).}
\tag{L-15442.14}
\]

Together with (L-15442.4), the first line of (L-15442.12) is positive.

### Second term

For `x>1`,

\[
{\zeta'\over\zeta}(x)
=-\sum_{n\ge2}{\Lambda(n)\over n^x}.
\tag{L-15442.15}
\]

Therefore

\[
\boxed{
{\zeta'\over\zeta}(1+s+q)
-{\zeta'\over\zeta}(1+s)
=\sum_{n\ge2}{\Lambda(n)\over n^{1+s}}
 \left(1-n^{-q}\right)>0.}
\tag{L-15442.16}
\]

This is an explicit positive prime sum.

Consequently

\[
\boxed{
-\partial_s\widehat Y_s(q)>0
\qquad(0<s<1,\ q>0).}
\tag{L-15442.17}
\]

## 4. Ordered exponential moments

Since

\[
\widehat Y_s(q)
=\int_0^\infty e^{-qt}Y_s(t)\,dt,
\tag{L-15442.18}
\]

one obtains the exact order

\[
\boxed{
0<s_1<s_2<1
\quad\Longrightarrow\quad
\widehat Y_{s_1}(q)>\widehat Y_{s_2}(q)>0
\quad(q>0).}
\tag{L-15442.19}
\]

Equivalently,

\[
\boxed{
\int_0^\infty e^{-qt}
 \bigl[Y_{s_1}(t)-Y_{s_2}(t)\bigr]dt>0}
\tag{L-15442.20}
\]

at every positive exponential scale.

Integrating (L-15442.12) over `s` gives an explicit positive decomposition of
the moment difference:

\[
\boxed{
\widehat Y_{s_1}(q)-\widehat Y_{s_2}(q)
=\int_{s_1}^{s_2}
 \bigl[-\partial_s\widehat Y_s(q)\bigr]ds.}
\tag{L-15442.21}
\]

Thus the numerically observed decrease of the regular density with `s` is not
an artifact at the moment level: every positive Laplace probe sees the same
strict order.

## 5. Use in the finite compact certificate

`T-15413` reduces the global sign to finitely many integer rows

\[
s\longmapsto Y_s(\log N),
\qquad1\le N\le N_*.
\]

Equation (L-15442.17) supplies three proof-facing constraints on every such row.

1. All positive exponential averages are ordered in the same direction.
2. A proposed pointwise-monotonicity proof must be compatible with the exact
   forcing in (L-15442.12), rather than inferred from floating samples.
3. Any negative excursion at a smaller shift must be compensated by a larger
   positive excursion at every exponential scale when compared with a larger
   shift.

The identity can also be used as a correlated interval check: directed
`q`-moment evaluations at several shifts must satisfy the strict nesting
(T-15442.19).

## 6. What this does not prove

Laplace-transform order does **not** imply pointwise order for arbitrary signed
densities.  Therefore this lemma does not claim

\[
Y_{s_1}(t)\ge Y_{s_2}(t)
\]

for every `t`, even though ordinary reconnaissance suggests that stronger
statement.

Likewise, positivity and shift monotonicity of all zeroth exponential moments
do not by themselves prove complete monotonicity in `q`.  The full
`Y_s(t)>=0` problem remains the finite compact endpoint certificate isolated by
`T-15413`.

## 7. Proof boundary

- The derivative factorization is exact.
- Strict positivity uses only the positive real-axis theta representation and
  the absolutely convergent Euler logarithmic derivative.
- No RH assumption enters.
- The result strengthens the global moment geometry but does not close the
  remaining pointwise finite rows or claim RH.
