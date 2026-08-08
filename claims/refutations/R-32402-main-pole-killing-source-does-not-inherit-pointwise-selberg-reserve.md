# R-32402 — The main-pole-killing source does not inherit the pointwise Selberg reserve

Claim ID: `R-32402`  
Title: The `lambda=2` main-pole-killing positive-inverse source has a negative generalized Selberg row already at `(n,j)=(6,2)`  
Status: **PROPOSED COMPLETE EXACT REFUTATION OF THE NAIVE RESERVE TRANSFER**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32403`; generalized Selberg identity  
Scope: refutes only the rowwise transplant of PR #302 `L-28009`; does not refute a coupled physical reserve or MPKS

## 1. General local-Euler row at `(6,2)`

For the local-Euler family

\[
 A_\lambda(s)={\zeta(s)\over1-\lambda2^{-s}},
\]

let `Lambda_lambda` be its generalized von Mangoldt sequence and

\[
 C_\lambda
 =\Lambda_\lambda\log
  +\Lambda_\lambda*\Lambda_\lambda.
\]

Define the carry-row coordinates

\[
 P_\lambda(n,j)
 =\sum_q\Lambda_\lambda(q)\chi_{n,q}(j),
\]

\[
 S_\lambda(n,j)
 =\sum_q C_\lambda(q)\chi_{n,q}(j).
\]

At `(n,j)=(6,2)`, the only carry-active prime powers in the first moment are
`3` and `5`, and direct substitution gives

\[
 \boxed{
 P_\lambda(6,2)=\log3+\log5.
 }
\tag{R-32402.1}
\]

For the second Selberg moment, the active convolution through the dyadic factor
adds the `2*3` cross channel. The exact result is

\[
 \boxed{
 S_\lambda(6,2)
 =\log^23+\log^25
  +2(1+\lambda)\log2\log3.
 }
\tag{R-32402.2}
\]

Therefore

\[
 \boxed{
 P_\lambda(6,2)^2-S_\lambda(6,2)
 =2\log3\,[\log5-(1+\lambda)\log2].
 }
\tag{R-32402.3}
\]

## 2. Exact failure at the pole-killing parameter

For `lambda=2`,

\[
 P_*^2-S_*
 =2\log3\,(\log5-3\log2).
\tag{R-32402.4}
\]

Since

\[
 5<8=2^3,
\]

one has

\[
 \boxed{
 P_*(6,2)^2-S_*(6,2)<0.
 }
\tag{R-32402.5}
\]

No numerical approximation enters this contradiction.

## 3. Sharp local threshold

Equation (R-32402.3) also identifies the exact threshold for this row:

\[
 P_\lambda(6,2)^2-S_\lambda(6,2)\ge0
\]

if and only if

\[
 \boxed{
 \lambda\le {\log5\over\log2}-1.
 }
\tag{R-32402.6}
\]

The threshold is strictly between `1` and `2`, because

\[
 4<5<8.
\]

Thus the exact two-contact point `lambda=1` lies safely on the positive side,
while the main-pole-killing point `lambda=2` lies on the negative side.

## 4. Consequence for MPKS

`L-32403` remains valuable: the `lambda=2` source has positive inverse data,
nonnegative generalized-prime coefficients, exact main-density cancellation,
no artificial eta-line poles in the physical detector, and retains every
nontrivial zeta zero.

But a completion may **not** import the pointwise row theorem `L-28009` from
`lambda=1`. The missing reserve must instead be one of:

1. a coupled independent-frequency physical reserve where negative local rows
   are absorbed by cross-row terms;
2. an explicit finite correction of the exceptional transition rows followed by
   a uniform positive theorem outside that table;
3. a mixed-parameter/local-Euler decomposition which preserves the pole-killing
   physical combination while assigning the reserve to positive subchannels.

Any proof which simply asserts `P_*^2>=S_*` is rejected by (R-32402.5).

## 5. Proof boundary

Refuted exactly:

- direct transplantation of the `lambda=1` pointwise Selberg reserve to the
  `lambda=2` main-pole-killing source.

Not refuted:

- `L-32403` source/pole algebra;
- a source-coupled matrix reserve;
- a finite corrected reserve;
- MPKS;
- RH.