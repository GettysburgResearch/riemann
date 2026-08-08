# L-27701 — Central carry residual and unconditional two-pass packing

Claim ID: `L-27701`  
Title: The central first-difference packing has an explicit alternating-block residual; for the critical carry target that residual is again decreasing, yielding an unconditional second packing stage  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — PENDING INDEPENDENT REPLAY**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #247 `L-23808`, `L-23814`  
Scope: finite carry algebra and a two-stage unconditional prime-ramp lower bound; no RH claim

## 1. Central split carry pattern

For an integer parent `n>=2` put

\[
j_n=\lfloor n/2\rfloor,
\qquad
\chi_n(q)=
\left\lfloor{n\over q}\right\rfloor
-\left\lfloor{j_n\over q}\right\rfloor
-\left\lfloor{n-j_n\over q}\right\rfloor.
\]

Then

\[
\boxed{
\chi_n(q)=1
\iff
n\bmod 2q\in\{q,q+1,\ldots,2q-2\}.
}
\tag{L-27701.1}
\]

Indeed the two central child residues add to the residue of `n` modulo `q`; a
carry occurs precisely on the displayed half-block.  The endpoint `2q-1` is
excluded because one central child is divisible by `q`.

## 2. Exact residual operator

Let `r(2),...,r(X)` be any nonnegative nonincreasing target, set
`r(X+1)=0`, and put

\[
a(n)=r(n)-r(n+1)\ge0.
\]

Place the coefficient `a(n)` on the central split `[n,j_n]`.  Its load at
column `q` is

\[
\begin{aligned}
L_r(q)
&=\sum_{n=q}^{X}a(n)\chi_n(q)\\
&=\sum_{k\ge0}
\left[r((2k+1)q)-r((2k+2)q-1)\right],
\end{aligned}
\tag{L-27701.2}
\]

where values beyond `X` are zero.  Therefore the unused target is exactly

\[
\boxed{
(\mathcal T_Xr)(q)
:=r(q)-L_r(q)
=\sum_{k\ge1}
\left[r(2kq-1)-r((2k+1)q)\right].
}
\tag{L-27701.3}
\]

Every summand is nonnegative, so `mathcal T_X r>=0`.  Thus the central
first-difference construction is not merely feasible: it has a closed residual
operator.

Equation (L-27701.3) is the discrete object whose continuum limit was missing
from the one-pass theorem `L-23814`.

## 3. Critical target and first residual monotonicity

For the critical carry target define, on the real interval `0<t<=X`,

\[
w_X(t)=t^{-1/2}\log(X/t),
\]

and put `w_X(t)=0` for `t>X`.

Set

\[
h_X(t)=-t w_X'(t)
=t^{-1/2}\left(1+\frac12\log(X/t)\right).
\tag{L-27701.4}
\]

Both `w_X` and `h_X` are positive and strictly decreasing on `(0,X)`.
For fixed `k>=1`, on every interval on which both arguments are below `X`,

\[
g_k(x)=w_X(2kx-1)-w_X((2k+1)x)
\]

satisfies

\[
\begin{aligned}
-g_k'(x)
&={2k\over2kx-1}h_X(2kx-1)
-{1\over x}h_X((2k+1)x)\\
&>0,
\end{aligned}
\tag{L-27701.5}
\]

because

\[
{2k\over2kx-1}>{1\over x}
\quad\text{and}\quad
h_X(2kx-1)>h_X((2k+1)x).
\]

If the second argument has crossed `X`, then `g_k(x)=w_X(2kx-1)` and is
still decreasing; after the first argument crosses `X`, it is zero.  The
transitions are continuous since `w_X(X)=0`.

Consequently every `g_k` is nonincreasing, and the finite sum in
(L-27701.3) gives

\[
\boxed{
R_X(q):=(\mathcal T_Xw_X)(q)
\text{ is nonnegative and nonincreasing in }q.
}
\tag{L-27701.6}

This is the new sign theorem.

## 4. Unconditional second stage

Because `R_X` is decreasing, define

\[
b(n)=R_X(n)-R_X(n+1)\ge0
\]

and put `b(n)` on the same central split `[n,j_n]`.  The second-stage load is
nonnegative and bounded columnwise by `R_X`.  Adding the first and second
stages therefore gives a genuine nonnegative balanced carry packing under the
original target `w_X` at every finite endpoint.

No Möbius sign estimate, numerical positivity ladder, or LP existence theorem
is used.

## 5. Two-stage entropy constant

Let

\[
\ell_n=\log\binom n{\lfloor n/2\rfloor}.
\]

Uniform Stirling estimates give

\[
\ell_n=n\log2+O(\log(n+1)).
\tag{L-27701.7}
\]

For every decreasing nonnegative target `r`, summation by parts gives

\[
\sum_n n[r(n)-r(n+1)]
=\sum_{q=2}^{X}r(q)+O(r(2)),
\tag{L-27701.8}
\]

and

\[
\sum_n [r(n)-r(n+1)]\log(n+1)
\le r(2)\log(X+1).
\tag{L-27701.9}
\]

For `w_X`, elementary integral comparison gives

\[
S_0(X):=\sum_{q=2}^{X}w_X(q)
=4\sqrt X+O(\log X).
\tag{L-27701.10}
\]

The total all-integer central carry count `c_n=sum_q chi_n(q)` satisfies

\[
c_n=n\log2+O(\sqrt n+\log(n+1)),
\tag{L-27701.11}
\]

by combining the balanced entropy comparison already proved in PR #247 with
(L-27701.7).  Since

\[
\sum_n\sqrt n\,[w_X(n)-w_X(n+1)]
=O((\log X)^2),
\]

summing the first-stage load over all columns yields

\[
\sum_qL_{w_X}(q)
=(\log2)S_0(X)+O((\log X)^2).
\tag{L-27701.12}
\]

Hence the first residual has mass

\[
\boxed{
S_1(X):=\sum_qR_X(q)
=4(1-\log2)\sqrt X+O((\log X)^2).
}
\tag{L-27701.13}
\]

Applying (L-27701.7)--(L-27701.9) to the decreasing target `R_X`, the second
stage contributes

\[
(\log2)S_1(X)+O((\log X)^2).
\]

Therefore the complete two-stage packing has entropy

\[
\boxed{
4\log2\,(2-\log2)\sqrt X
+O((\log X)^2).
}
\tag{L-27701.14}
\]

By Legendre/Kummer positivity this gives the unconditional prime-power ramp
bound

\[
\boxed{
\sum_{p^a\le X}{\Lambda(p^a)\over\sqrt{p^a}}
\log{X\over p^a}
\ge
4\log2\,(2-\log2)\sqrt X-O((\log X)^2).
}
\tag{L-27701.15}
\]

Numerically the constant is about `3.624`, improving the one-pass constant
`4 log 2` (about `2.773`) without any new arithmetic input.

## 6. What this does and does not prove

This theorem proves that the missing mass in `L-23814` is genuinely reusable;
it is not a one-pass artifact.  It does **not** prove that every later residual
is decreasing.  In fact finite reconnaissance shows tiny monotonicity defects
can appear after further discrete iterations.  Those defects are therefore the
correct next object, rather than an assertion of global pointwise producer
positivity.

The continuum cascade and the precise lattice-stability theorem needed for all
remaining stages are isolated in `L-27702/T-27701`.
