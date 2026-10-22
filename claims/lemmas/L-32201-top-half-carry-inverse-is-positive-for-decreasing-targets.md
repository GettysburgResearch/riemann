# L-32201 — Top-half carry inverse positivity for every decreasing target

Claim ID: `L-32201`
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — INDEPENDENT REVIEW REQUESTED**
Created: 2026-08-08
Scope: exact top-half triangular carry algebra; no RH conclusion

## 1. Carry matrix in the top half

Fix an endpoint `T>=3` and put

\[
N=\left\lfloor\frac T2\right\rfloor.
\]

For `N<q<=n<=T` one has `n<2q`, hence

\[
\boxed{
\beta_{nq}=\frac{2q-n-1}{n+1}.}
\tag{L-32201.1}
\]

Let `h(q)` be any nonnegative nonincreasing target on `N<q<=T`, and set
`h(T+1)=0`.  Let `c(n)` be the unique coefficients solving

\[
h(q)=\sum_{n=q}^{T}c(n)\beta_{nq},
\qquad N<q<=T.
\tag{L-32201.2}
\]

## 2. Exact inversion

Put

\[
d_n=\frac{c(n)}{n+1},
\qquad
S_q=\sum_{n=q}^{T}d_n.
\tag{L-32201.3}
\]

Then

\[
h(q)=\sum_{n=q}^{T}d_n(2q-n-1).
\tag{L-32201.4}
\]

Subtracting the equation at `q+1` gives

\[
h(q)-h(q+1)=(q-1)d_q-2S_{q+1}.
\tag{L-32201.5}
\]

Consequently

\[
(q-1)S_q=h(q)-h(q+1)+(q+1)S_{q+1}.
\tag{L-32201.6}
\]

Define

\[
V_q=q(q-1)S_q.
\]

Multiplying (L-32201.6) by `q` yields the telescoping recurrence

\[
V_q=q[h(q)-h(q+1)]+V_{q+1}.
\]

Thus

\[
\boxed{
V_q=\sum_{m=q}^{T}m[h(m)-h(m+1)]\ge0.}
\tag{L-32201.7}
\]

Moreover

\[
\begin{aligned}
d_q
&=S_q-S_{q+1}\\
&=\frac{h(q)-h(q+1)}{q-1}
 +\frac{2V_{q+1}}{q(q^2-1)}.
\end{aligned}
\tag{L-32201.8}
\]

Both terms are nonnegative. Therefore

\[
\boxed{c(q)=(q+1)d_q\ge0\qquad(N<q<=T).}
\tag{L-32201.9}
\]

This proves top-half positivity without Mobius inversion, asymptotics, or a
computer check.

## 3. Critical square-root hinge

For

\[
h_T(q)=q^{-1/2}-T^{-1/2},
\qquad q<=T,
\tag{L-32201.10}
\]

the hypotheses hold. Hence every exact hinge coefficient with `2n>T` is
nonnegative.

The theorem is deliberately stronger at this scope: every nonnegative
decreasing target has a nonnegative exact inverse on its top triangular half.

## 4. Proof boundary

Closed exactly:

- the top-half affine carry kernel;
- the explicit tail-sum inversion;
- nonnegativity for every decreasing target;
- the complete top half of every critical square-root hinge.

Not proved:

- positivity below `T/2`;
- full hinge saturation;
- Carry Saturation;
- RH.
