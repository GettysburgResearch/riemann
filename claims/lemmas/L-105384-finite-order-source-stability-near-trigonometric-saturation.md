# L-105384 — Every finite Xi source order is stable near the trigonometric saturation law

Claim ID: `L-105384`  
Status: **PROVED EXACT FINITE-ORDER STABILITY THEOREM**  
Created: 2026-08-23  
Depends on: `L-105380--L-105382`  
RH status: **not assumed**

## 1. Unit-scale trigonometric moment sequences

Let

\[
\tau_n^{\rm odd}
=
\sum_{j=0}^{\infty}
{8\over\pi^2(2j+1)^2}
\left({4\over\pi^2(2j+1)^2}\right)^n,
\tag{L-105384.1}
\]

and

\[
\tau_n^{\rm even}
=
\sum_{j=1}^{\infty}
{2\over\pi^2j^2}
\left({1\over\pi^2j^2}\right)^n.
\tag{L-105384.2}
\]

These are the tangent and regularized-cotangent source sequences of
`L-105382` at frequency one. For `p in {odd,even}` define

\[
\mathsf T_{k,p}^{(0)}
=[\tau_{r+s}^{p}]_{r,s=0}^{k-1},
\qquad
\mathsf T_{k,p}^{(1)}
=[\tau_{r+s+1}^{p}]_{r,s=0}^{k-1}.
\tag{L-105384.3}
\]

The representing measures have infinite positive support, so

\[
\boxed{
\delta_{k,p}^{(a)}
:=\lambda_{\min}(\mathsf T_{k,p}^{(a)})>0
}
\tag{L-105384.4}
\]

for every finite `k`, parity `p`, and block `a in {0,1}`.

## 2. Coefficient stability implies matrix positivity

Let `F` be an odd or even source at scale `omega>0`, with regularized source
coefficients `a_n(F)`. Put

\[
\widehat a_n(F;\omega)
={a_n(F)\over\omega^{2n}}.
\tag{L-105384.5}
\]

Fix `k` and `a in {0,1}`. Suppose

\[
\boxed{
\max_{0\le n\le 2k-2+a}
\left|
\widehat a_n(F;\omega)-\tau_n^p
\right|
\le
{\delta_{k,p}^{(a)}\over2k}.
}
\tag{L-105384.6}
\]

Let `D_omega=diag(1,omega^(-2),...,omega^(-2k+2))`. Then

\[
D_\omega\mathsf A_k^{(0)}(F)D_\omega
=[\widehat a_{r+s}]_{r,s=0}^{k-1},
\tag{L-105384.7}
\]

and

\[
\omega^{-2}D_\omega\mathsf A_k^{(1)}(F)D_\omega
=[\widehat a_{r+s+1}]_{r,s=0}^{k-1}.
\tag{L-105384.8}
\]

The entrywise error from the corresponding trigonometric matrix is at most
`delta/(2k)`. Its operator norm is at most `k` times the maximum entry, hence
at most `delta/2`. Weyl's inequality gives

\[
\boxed{
\mathsf A_k^{(a)}(F)\succ0.
}
\tag{L-105384.9}
\]

Thus every prescribed finite source order has a quantitative open
neighbourhood around the trigonometric moment law.

## 3. Odd tilted-law moment concentration supplies coefficient convergence

For the odd law of `L-105380`, choose

\[
\omega^2=\mathbb E[X]
\]

and write

\[
q_j={\mathbb E[X^j]\over\omega^{2j}}.
\tag{L-105384.10}
\]

The normalized recurrence obtained from `L-105380.6` expresses
`widehat a_n` as a polynomial with rational coefficients in
`q_1,...,q_n`, and `q_1=1`. At the point `(1,...,1)` it equals
`tau_n^odd`. Therefore, for each fixed `N`,

\[
\boxed{
q_j\longrightarrow1
\quad(1\le j\le N)
\Longrightarrow
\widehat a_n\longrightarrow\tau_n^{\rm odd}
\quad(0\le n\le N).
}
\tag{L-105384.11}
\]

No complex contour theorem is used in this algebraic implication.

## 4. Even tilted-law moment concentration supplies coefficient convergence

For the even law of `L-105381`, again choose

\[
\omega^2=\mathbb E[X].
\]

Assume, for every fixed `j`,

\[
{\mathbb E[X^j]\over\omega^{2j}}\longrightarrow1
\tag{L-105384.12}
\]

and also

\[
\omega^2\mathbb E[X^{-1}]\longrightarrow1.
\tag{L-105384.13}
\]

The regularized quotient recurrence is rational-polynomial in these normalized
moments with denominator one. Hence

\[
\boxed{
\widehat a_n
\longrightarrow
\tau_n^{\rm even}
}
\tag{L-105384.14}
\]

for every fixed `n`.

## 5. Finite-order high-tail consequence

Suppose a derivative sequence of the Xi tilted laws satisfies the normalized
moment concentration in Sections 3 or 4. Then for every fixed `k`, both source
matrices

\[
\mathsf A_k^{(0)},
\qquad
\mathsf A_k^{(1)}
\]

are eventually positive definite. The derivative threshold may depend on
`k`; no uniform all-order assertion is made.

This source conclusion is substantially weaker than the unresolved moving
complex-saddle theorem: it asks only for finitely many moments of a positive
real probability law at a time.

## 6. Scope

The theorem does not prove the required moment concentration for the Xi kernel,
does not control the smallest trigonometric eigenvalues as `k` grows, and does
not compare the source matrices with the critical atomic matrices. Therefore
it does not prove `OSCC105371`, `BRP105220`, or RH.
