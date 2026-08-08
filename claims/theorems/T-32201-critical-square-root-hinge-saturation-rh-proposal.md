# T-32201 — Critical square-root hinge saturation would prove RH

Claim ID: `T-32201`
Status: **FULL ELEMENTARY PROPOSAL — CHS OPEN / RH UNPROVED**
Created: 2026-08-08
Dependencies: `L-32201`, `L-32202`; carry/entropy and square-screw/Landau interfaces

## 1. Hinge basis

Put

\[
x_q=q^{-1/2}.
\]

For `3<=T<=X`, define

\[
\boxed{
h_T(q)=(x_q-x_T)_+
=\begin{cases}
q^{-1/2}-T^{-1/2},&q<=T,\\
0,&q>T.
\end{cases}}
\tag{T-32201.1}
\]

The critical carry target is

\[
w_X(q)=q^{-1/2}\log(X/q)
=2x_q\log(x_q/x_X).
\tag{T-32201.2}
\]

Let

\[
\phi_X(x)=2x\log(x/x_X).
\]

Then

\[
\phi_X''(x)=2/x>0.
\tag{T-32201.3}
\]

Take the piecewise-linear interpolant of `phi_X` on the increasing knot list

\[
x_X<x_{X-1}<\cdots<x_2.
\]

Its successive slopes are increasing by strict convexity.  The elementary
hinge representation of a convex piecewise-linear function therefore gives
nonnegative coefficients `lambda_(X,T)>=0` such that exactly on every knot

\[
\boxed{
 w_X(q)=\sum_{T=3}^{X}\lambda_{X,T}h_T(q),
 \qquad2\le q\le X.}
\tag{T-32201.4}
\]

For completeness, the coefficient at the outer hinge is the first secant
slope, and every subsequent coefficient is the difference of two consecutive
secant slopes.  Thus no limiting or analytic approximation is used.

## 2. Critical Hinge Saturation (`CHS`)

For each endpoint `T`, let `c_T(n)` be the unique triangular carry inverse of
`h_T`:

\[
h_T(q)=\sum_{n=q}^{T}c_T(n)\beta_{nq}.
\tag{T-32201.5}
\]

The proposed theorem is

> **CHS.** For every integer `T>=3`,
> \[
> \boxed{c_T(n)\ge0\qquad(2\le n\le T).}
> \tag{CHS}
> \]

`L-32201` proves CHS unconditionally on the complete top half `2n>T`.
`L-32202` identifies the exact Mertens-smoothed step source controlling the
remaining inner half.

## 3. CHS gives exact Carry Saturation

Assume CHS.  Embed each hinge flow at endpoint `T` into the endpoint-`X`
carry matrix and set

\[
 d_X(n)=\sum_{T=n}^{X}\lambda_{X,T}c_T(n).
\tag{T-32201.6}
\]

Every term is nonnegative.  Using (T-32201.4)--(T-32201.5) and interchanging
finite sums gives

\[
\boxed{
 B_X^Td_X=w_X,
 \qquad d_X\ge0.}
\tag{T-32201.7}
\]

Thus CHS implies the complete finite Carry Saturation theorem, not merely a
subpacking.

## 4. Entropy and prime ramp

Let

\[
G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj.
\]

The exact Legendre/carry identity is

\[
G_n=\sum_{p^a\le n}\Lambda(p^a)\beta_{n,p^a}.
\tag{T-32201.8}
\]

The reviewed entropy bound gives

\[
G_n\ge n/2-O(\log(n+1)).
\tag{T-32201.9}
\]

For every exact Carry Saturation vector the sharp carry-mass identity/dual
estimate gives

\[
\sum_n n d_X(n)\ge8\sqrt X-O(\log^2X),
\qquad
\sum_n d_X(n)=O(\log X).
\tag{T-32201.10}
\]

Consequently

\[
\begin{aligned}
\mathcal P(X)
&:=\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}\log(X/p^a)\\
&=\sum_n d_X(n)G_n\\
&\ge4\sqrt X-O(\log^2X).
\end{aligned}
\tag{T-32201.11}
\]

All equalities are finite.

## 5. RH consumer

At square endpoints `X=N^2`, the source-pinned square-screw identity has the
form

\[
\Psi(2\log N)=4N-\mathcal P(N^2)+O(\log N).
\tag{T-32201.12}
\]

Equation (T-32201.11) gives a polylogarithmic upper envelope for `Psi` on the
square mesh.  The reviewed one-sided Landau/square-mesh interpolation theorem
then excludes every zeta zero with real part greater than `1/2`; functional-
equation symmetry gives RH.

Hence

\[
\boxed{\mathrm{CHS}\Longrightarrow\mathrm{RH}.}
\tag{T-32201.13}
\]

## 6. Why CHS is not being called proved

The exact endpoint update is

\[
 c_{T+1}(j)=c_T(j)+
 [T^{-1/2}-(T+1)^{-1/2}]s_T(j),
\]

and `s_T(j)` contains explicit Mertens sums.  Large finite scans showing
positive `c_T(j)` therefore do not remove the arithmetic obstruction.

A valid CHS proof must supply a source-level inequality for the complete
Mertens-smoothed sum of `L-32202`, not a finite-height scan, a fixed-order Abel
positivity theorem, or a generic total-positivity claim about the carry matrix.

## 7. Exact status

```text
positive hinge decomposition of critical target     PROPOSED COMPLETE
complete top-half hinge inverse positivity           PROPOSED COMPLETE
exact Mertens-smoothed hinge update                   PROPOSED COMPLETE
Critical Hinge Saturation below the top half          OPEN / RH-BEARING
CHS -> Carry Saturation -> sharp prime ramp -> RH     COMPLETE CONDITIONAL
Riemann Hypothesis                                    UNPROVED
```
