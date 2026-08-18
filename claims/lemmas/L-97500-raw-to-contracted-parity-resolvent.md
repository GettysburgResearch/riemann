# L-97500 — Exact raw-to-contracted parity resolvent transfer

Claim ID: `L-97500`  
Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**  
Created: 2026-08-18  
Frozen base: PR #576 at `0f6ea6eae813c1d867ae50744cf5fd57e2720bb7`  
RH status: **not assumed**

## 1. Raw rough recursion

Let `V` be a finite rough-history DAG in topological order. Let `R` be a
strictly upper-triangular nonnegative operator. Its entry `r_(v,w)` is the
literal raw rough coefficient on the edge `v -> w`; cumulative parity is
encoded by the minus sign in

\[
 f+Rf=b. \tag{L-97500.1}
\]

Here `b` is the vector of local complete grouped observations and `f` is the
exact parity-resummed scalar. Since `R` is nilpotent,

\[
 \boxed{f=(I+R)^{-1}b.} \tag{L-97500.2}
\]

## 2. Any contracted recursion has one forced current

Let `T` be any other strictly upper-triangular nonnegative operator, intended
as a safe-child recursion. The same exact scalar `f` satisfies

\[
 f+Tf=g \tag{L-97500.3}
\]

if and only if

\[
 \boxed{
 g=(I+T)(I+R)^{-1}b
   =b+(T-R)f.
 } \tag{L-97500.4}
\]

Thus the current is not freely chosen. Reducing a raw edge coefficient moves
the omitted coefficient into the current, evaluated on the **complete child
state** `f_w`.

## 3. Chain formula

On a chain with raw coefficients `r_0,...,r_(L-1)` and contracted coefficients
`t_0,...,t_(L-1)`, the coefficient of a local datum `b_k`, `k>=1`, in the root
current `g_0` is

\[
 \boxed{
 (-1)^{k-1}(t_0-r_0)r_1\cdots r_{k-1}.
 } \tag{L-97500.5}
\]

For constant `r,t`,

\[
 \boxed{
 g=b+(t-r)\sum_{k\ge1}(-r)^{k-1}S^k b,
 } \tag{L-97500.6}
\]

where the sum terminates at the chain depth. Unless `t=r`, the exact current
contains nonzero contributions at every available history depth and alternates
in sign.

## 4. Proof

Equation (L-97500.4) follows by substituting (L-97500.2) into (L-97500.3).
For the chain, solve backward:

\[
 f_i=b_i-r_i f_{i+1},
 \qquad
 g_i=f_i+t_i f_{i+1}
     =b_i+(t_i-r_i)f_{i+1}.
\]

Expanding `f_(i+1)` proves (L-97500.5); the constant-edge specialization gives
(L-97500.6).

## 5. Scope

This theorem is coefficient and parity exact. It does not assert positivity of
`g`. It identifies the nonlocal object that any contracted factor-67 proof must
actually control.
