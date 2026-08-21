# T-32201 — Critical square-root hinge saturation would prove RH

Claim ID: `T-32201`
Status: **FULL ELEMENTARY PROPOSAL — CHS INNER RECYCLE OPEN / RH UNPROVED**
Created: 2026-08-08
Updated: 2026-08-09
Dependencies: `L-32201`, `L-32202`, `L-32203`, `L-32204`; carry/entropy and square-screw/Landau interfaces

## 1. Hinge basis

Put

\[
x_q=q^{-1/2}.
\]

For `3<=T<=X`, define

\[
\boxed{h_T(q)=(x_q-x_T)_+.}
\tag{T-32201.1}
\]

The critical target is

\[
w_X(q)=q^{-1/2}\log(X/q)=2x_q\log(x_q/x_X).
\tag{T-32201.2}
\]

Since

\[
\phi_X''(x)=2/x>0,
\]

the discrete piecewise-linear interpolant on the knots `x_X<...<x_2` has an exact positive hinge representation

\[
\boxed{w_X(q)=\sum_{T=3}^{X}\lambda_{X,T}h_T(q),\qquad\lambda_{X,T}\ge0.}
\tag{T-32201.3}
\]

## 2. Critical Hinge Saturation (`CHS`)

Let `c_T` denote the exact triangular carry inverse

\[
h_T(q)=\sum_{n=q}^{T}c_T(n)\beta_{nq}.
\tag{T-32201.4}
\]

`CHS` is

\[
\boxed{c_T(n)\ge0\qquad(2\le n\le T).}
\tag{CHS}
\]

The present branch now proves substantially more than top-row positivity:

1. `L-32201`: every coefficient with `2n>T` is nonnegative;
2. `L-32204`: these top-half coefficients form a genuine finite packing.  After they saturate every column above `T/2`, **no lower column is overfilled**;
3. for a decreasing discretely convex target, including `h_T`, the exported lower residual is explicitly nonnegative and supported at the strict half scale.

Thus the remaining CHS problem is no longer feasibility of the first elimination.  It is whether the positive exported residual can be recycled completely without creating a negative later coefficient.

## 3. Exact first elimination

Put `N=floor(T/2)`.  `L-32204` constructs nonnegative coefficients on rows `N<n<=T` whose load equals `h_T(q)` for every `q>N`.  On `q<=N` the unused target is

\[
r_T(q)=h_T(q)-\sum_{n=N+1}^{T}c_T(n)\beta_{nq}\ge0.
\tag{T-32201.5}
\]

More precisely, writing

\[
\delta_m=m^{-1/2}-(m+1)^{-1/2},
\]

one has

\[
r_T(q)=h_{N+1}(q)+e_T(q),\qquad e_T(q)\ge0,
\tag{T-32201.6}
\]

and the excess has the exact positive Abel decomposition

\[
\boxed{
 e_T(q)=\delta_{T-1}K_{N,q}(T-1)
 +\sum_{M=N+1}^{T-2}(\delta_M-\delta_{M+1})K_{N,q}(M),}
\tag{T-32201.7}
\]

where

\[
K_{N,q}(M)=M-N-A_M(q)
+\frac{M(M+1)}{N(N+1)}A_N(q)\ge0
\tag{T-32201.8}
\]

and `A_x(q)=sum_(j=0)^x floor(j/q)`.

This is the exact new inner object.  Individual `K_(N,.,M)` need not have a nonnegative carry inverse, so they may not be separated before the critical weights in (T-32201.7) are recombined.

## 4. Mertens firewall

`L-32202` gives the independent exact formula

\[
c_T(j)=\sum_{M=j}^{T-1}
[M^{-1/2}-(M+1)^{-1/2}]s_M(j),
\tag{T-32201.9}
\]

where `s_M(j)` is the carry inverse of the constant step and is an explicit finite Mertens expression.  The continuum hinge inverse has multiplier

\[
\boxed{F_h(p)=\frac{p}{2(p-2)(p-3/2)\zeta(p-1)}.}
\tag{T-32201.10}
\]

Therefore the remaining recycle theorem is genuinely arithmetic.  Finite positivity scans, a generic matrix-positivity assertion, or separating the positive kernels in (T-32201.7) do not prove CHS.

## 5. CHS gives exact Carry Saturation

Assume CHS.  Embed each hinge flow into endpoint `X` and put

\[
d_X(n)=\sum_{T=n}^{X}\lambda_{X,T}c_T(n).
\]

Then `d_X>=0`, and finite interchange of the hinge sums gives

\[
\boxed{B_X^Td_X=w_X.}
\tag{T-32201.11}
\]

Hence CHS gives exact Carry Saturation.

## 6. Carry Saturation gives RH

The exact carry/Legendre identity is

\[
G_n=\sum_{p^a\le n}\Lambda(p^a)\beta_{n,p^a},
\]

with

\[
G_n\ge n/2-O(\log(n+1)).
\]

The reviewed mass and coefficient ledgers for an exact nonnegative saturation give

\[
\sum_n n d_X(n)\ge8\sqrt X-O(\log^2X),
\qquad
\sum_nd_X(n)=O(\log X).
\]

Therefore

\[
\boxed{
\mathcal P(X)
=\sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}\log(X/p^a)
\ge4\sqrt X-O(\log^2X).}
\tag{T-32201.12}
\]

At square endpoints `X=N^2`, the source-pinned square-screw identity gives

\[
\Psi(2\log N)=4N-\mathcal P(N^2)+O(\log N).
\]

The reviewed one-sided square-mesh/Landau theorem excludes every zero with real part greater than `1/2`; functional-equation symmetry then gives RH.

Thus

\[
\boxed{\mathrm{CHS}\Longrightarrow\mathrm{RH}.}
\tag{T-32201.13}
\]

## 7. Exact current frontier

```text
critical target -> positive hinge decomposition     PROPOSED COMPLETE
hinge top-half inverse positivity                   PROPOSED COMPLETE
top-half solve does not overfill lower columns      PROPOSED COMPLETE (L-32204)
positive strict-half residual and Abel ledger       PROPOSED COMPLETE (L-32204)
Mertens / reciprocal-zeta firewall                  PROPOSED COMPLETE
complete inner residual recycle / CHS               OPEN / RH-BEARING
CHS -> Carry Saturation -> sharp prime ramp -> RH   COMPLETE CONDITIONAL
Riemann Hypothesis                                  UNPROVED
```

A reviewer is not asked to invent the recycle theorem.  Review begins with the supplied `L-32201/L-32204` proofs; the branch remains a research proposal until a complete inner recycle proof is produced.
