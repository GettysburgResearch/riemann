# R-106670 — Height, signed index, and raw volume do not close the free-energy gate

Claim ID: `R-106670`  
Status: **PROVED EXACT FINITE FIREWALLS**  
Created: 2026-08-26  
Depends on: `L-106670`, `L-106673`; `T-105650/L-105653` for scope  
RH status: **not assumed**

## 1. One shallow pair with arbitrary horizontal separation

Fix `epsilon>0` and take right-half-plane poles

\[
z=\epsilon,
\qquad
w=\epsilon+iL.
\]

Their heights, degree, and signed-index data agree.  Nevertheless

\[
\boxed{
\mathfrak Z_1
={4\epsilon^2\over4\epsilon^2+L^2},
\qquad
1-\mathfrak Z_1
={L^2\over4\epsilon^2+L^2}\longrightarrow1.
}
\tag{R-106670.1}
\]

Moreover

\[
-\log\mathfrak Z_1
=
\log\left(1+{L^2\over4\epsilon^2}\right)
\longrightarrow\infty.
\tag{R-106670.2}
\]

Thus shallow-height mass and clipped signed index do not control horizontal
transport, and the unregularized logarithmic volume is not a bounded consumer.

## 2. One bad direction inside a large block

Let the favorable-overlap eigenvalues be

\[
\lambda_1=0,
\qquad
\lambda_2=\cdots=\lambda_m=1.
\]

The exact canonical charge is only `1`, but

\[
\det K=0,
\qquad
-\log\det K=+\infty,
\qquad
m\left(1-(\det K)^{1/m}\right)=m.
\]

Hence a raw determinant or geometric-mean volume can overpay one adverse
direction by the full dimension.

The regularized free energy repairs this exactly:

\[
\boxed{
\mathfrak F_\tau
={-\log(1-\tau)\over\tau},
}
\tag{R-106670.3}
\]

which is dimension independent and tends to the correct charge `1` as
`tau -> 0`.

## 3. Convex-majorization boundary

Root-critical doubly-stochastic majorization controls one-divisor convex
observables.  It does not couple the two endpoint divisors and does not bound
the oscillatory energy in `L-106673`.  The present firewalls therefore leave
open, but require, an Xi-specific source/outer-factor estimate for the
regularized Pick determinant.
