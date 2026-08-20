# L-99920 — Exact native priority-Hasse flow on a weighted Euler cube

Claim ID: `L-99920`  
Status: **PROVED EXACT FINITE IDENTITY**  
Created: 2026-08-20  
Depends on: PR #667 normalization firewall  
RH status: **not assumed**

Let the ordered labels be `1,...,k`, with native normalized activities

\[
0\le a_i<1.
\]

For the zero-free normalized box, `a_i=1/p_i`; the prime `67` occurs as two distinct labels, both with activity `1/67`.

For a subset `A` put

\[
w(A)=\prod_{i\in A}a_i,
\qquad
s_i=\prod_{h\le i}(1-a_h),
\qquad
\lambda_i=a_i s_{i-1},
\]

with `s_0=1`.  For every

\[
A\subseteq\{i+1,\ldots,k\},
\]

place mass

\[
\boxed{J_{i,A}=\lambda_i w(A)}
\tag{L-99920.1}
\]

on the Hasse edge joining `A` and `A union {i}`, oriented from its odd-parity endpoint to its even-parity endpoint.

Then:

\[
\boxed{
\begin{aligned}
\operatorname{out}(S)&=w(S)&&(|S|\text{ odd}),\\
\operatorname{in}(S)&=w(S)&&(|S|\text{ even},\ S\ne\varnothing),\\
\operatorname{in}(\varnothing)&=1-s_k.
\end{aligned}}
\tag{L-99920.2}
\]

Hence the only unused even capacity is the positive empty-set residual `s_k`.

## Proof

Let `S` be nonempty and put `i=min S`.  The edge owned by `i` contributes

\[
\lambda_i w(S\setminus\{i\})=s_{i-1}w(S).
\]

For each `j<i`, the edge `(j,S)` contributes `lambda_j w(S)`.  Since

\[
\sum_{j<i}\lambda_j=1-s_{i-1},
\]

the total incident flow in the parity-prescribed direction is exactly

\[
[s_{i-1}+1-s_{i-1}]w(S)=w(S).
\]

For the empty set, the incoming mass is

\[
\sum_i\lambda_i=1-s_k.
\]

This proves the claim.

## Native duplicate-67 scope

With one Boolean label of activity `1/p` for each prime `p!=67` and two labels of activity `1/67`, aggregation of the two `67` labels gives the exact local fibres

\[
1,\quad -\frac2{67},\quad \frac1{67^2},
\]

which are precisely `beta(n)/n` for

\[
\beta=(\varepsilon-\delta_{67})*\mu.
\]

Thus this flow belongs to the literal normalized source of PR #667.  It is not the auxiliary `p^{-1/2}` operator rejected by `R-99900`.
