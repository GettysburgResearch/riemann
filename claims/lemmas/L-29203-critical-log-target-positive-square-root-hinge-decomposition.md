# L-29203 — The critical logarithmic target is a positive square-root hinge mixture

Claim ID: `L-29203`  
Title: Every finite critical carry target is an exact nonnegative combination of self-similar square-root difference targets  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: elementary convexity and finite divided differences  
Scope: exact target decomposition; no carry-flow existence or RH conclusion

## 1. Two target families

Fix an integer `X>=3`.  The critical target is

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad2\le q\le X.
\tag{L-29203.1}
\]

For every integer `3<=T<=X`, define the stopped square-root hinge

\[
\boxed{
h_T(q)=
\begin{cases}
q^{-1/2}-T^{-1/2},&2\le q\le T,\\
0,&q>T.
\end{cases}}
\tag{L-29203.2}
\]

Every `h_T` is nonnegative and has exact factor-two self-similarity:

\[
\boxed{
h_{2T}(2q)=2^{-1/2}h_T(q).}
\tag{L-29203.3}
\]

## 2. Convex coordinate

Put

\[
x_q=q^{-1/2},
\qquad x_X<x_{X-1}<\cdots<x_2.
\tag{L-29203.4}
\]

Then

\[
w_X(q)=F_X(x_q),
\qquad
F_X(x)=2x\log(x/x_X).
\tag{L-29203.5}
\]

On `[x_X,x_2]`,

\[
F_X(x_X)=0,
\qquad
F_X''(x)=\frac2x>0.
\tag{L-29203.6}
\]

Thus `F_X` is strictly convex.

## 3. Exact discrete hinge coefficients

For `2<=q<=X-1`, define the secant slopes

\[
\sigma_q
=\frac{w_X(q)-w_X(q+1)}{x_q-x_{q+1}}.
\tag{L-29203.7}
\]

Convexity gives

\[
\sigma_2\ge\sigma_3\ge\cdots\ge\sigma_{X-1}>0.
\tag{L-29203.8}
\]

Set

\[
\boxed{
\lambda_X=\sigma_{X-1},
\qquad
\lambda_T=\sigma_{T-1}-\sigma_T
\quad(3\le T<X).
}
\tag{L-29203.9}
\]

Then

\[
\boxed{
\lambda_T\ge0
\qquad(3\le T\le X).
}
\tag{L-29203.10}
\]

## 4. Positive hinge identity

For every `2<=q<=X`,

\[
\boxed{
w_X(q)=\sum_{T=3}^{X}\lambda_T h_T(q).}
\tag{L-29203.11}
\]

### Proof

At `q=X` both sides vanish.  Taking the first difference in `q`,

\[
h_T(q)-h_T(q+1)
=\begin{cases}
x_q-x_{q+1},&T\ge q+1,\\0,&T\le q.
\end{cases}
\tag{L-29203.12}
\]

Therefore the first difference of the right side is

\[
(x_q-x_{q+1})
\sum_{T=q+1}^{X}\lambda_T.
\]

The definition (L-29203.9) telescopes to

\[
\sum_{T=q+1}^{X}\lambda_T=\sigma_q.
\tag{L-29203.13}
\]

By (L-29203.7), this equals `w_X(q)-w_X(q+1)` divided by
`x_q-x_(q+1)`.  Hence the two sides have the same first differences and the
same value at `q=X`.

## 5. Carry-flow consequence

Suppose that for every `3<=T<=X` there is a nonnegative split flow `d_T`
supported on rows `n<=T` whose carry load is exactly `h_T(q)`.  Extend each
flow by zero to endpoint `X` and put

\[
\boxed{d_X=\sum_{T=3}^{X}\lambda_Td_T.}
\tag{L-29203.14}
\]

Then `d_X` is nonnegative, retains every rowwise support condition satisfied by
the `d_T`, and by (L-29203.11) satisfies

\[
L_q(d_X)=w_X(q)
\qquad(2\le q\le X).
\tag{L-29203.15}
\]

In particular:

\[
\boxed{
\text{support-feasible square-root flows for all }T
\Longrightarrow SF\text{-}MCF(X).
}
\tag{L-29203.16}
\]

## 6. Continuous companion

The same identity has the integral form

\[
\boxed{
q^{-1/2}\log(X/q)
=2(q^{-1/2}-X^{-1/2})
 +\int_q^X
 \frac{q^{-1/2}-Y^{-1/2}}Y\,dY.
}
\tag{L-29203.17]
\]

The closing bracket in the tag is typographical only.  Equation (L-29203.11)
is its exact finite convex-hinge analogue.

## 7. Strategic consequence

The logarithmic target no longer has to be propagated through a recursive
construction.  It is enough to solve the one-parameter family

\[
\boxed{
h_T(q)=q^{-1/2}-T^{-1/2}.}
\tag{L-29203.18}
\]

This family is:

- positive and decreasing;
- exactly self-similar under factor two;
- free of logarithmic Jordan terms;
- closed under positive superposition into the critical target.

Thus the preferred PPMFL producer should be built first for the square-root
family.  The critical logarithm is recovered at the final finite level by
(L-29203.14), with no loss and no sign issue.

## 8. Proof boundary

Closed exactly:

- strict convexity in the square-root coordinate;
- explicit nonnegative hinge coefficients;
- the finite positive decomposition (L-29203.11);
- the factor-two self-similarity;
- positive-flow superposition.

Open:

- support-feasible exact flows for `h_T`;
- PPMFL/SF-MCF;
- RH.
