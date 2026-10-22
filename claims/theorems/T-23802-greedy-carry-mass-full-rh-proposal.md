# T-23802 — Greedy carry mass full RH proposal

Claim ID: `T-23802`  
Title: One canonical descending nonnegative carry packing with asymptotically sharp mass would prove the Riemann Hypothesis  
Status: **FULL PROPOSAL — ONE FINITE GREEDY MASS THEOREM OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`--`L-23805`, `L-19801`  
Scope: proposed elementary completion

## 1. Canonical finite producer

For every integer `X>=2`, start with

\[
\rho_X^{(X)}(q)=w_X(q),
\qquad2\le q\le X.
\]

For `n=X,X-1,...,2`, define

\[
\boxed{
 d_X^{\rm gr}(n)
 =\min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 {\rho_X^{(n)}(q)\over\beta_{nq}},}
\tag{T-23802.1}
\]

and subtract the corresponding row:

\[
\rho_X^{(n-1)}(q)
=ho_X^{(n)}(q)-d_X^{\rm gr}(n)\beta_{nq}
\qquad(q\le n).
\tag{T-23802.2}
\]

Every residual and every coefficient is nonnegative. Hence

\[
\boxed{
B_X^T d_X^{\rm gr}\le w_X.}
\tag{T-23802.3}
\]

The producer uses only floors, logarithms, square roots, minima, and finite
subtraction. It is deterministic after an exact tie-breaking rule is fixed.
No zeta zero, prime asymptotic, or Möbius estimate enters its construction.

## 2. Sole open theorem

The proposed arithmetic theorem is

> **GCM — Greedy Carry Mass theorem.** For every `epsilon>0`,
> \[
> \boxed{
> \sum_{n=2}^{X}n\,d_X^{\rm gr}(n)
> \ge8\sqrt X-C_\epsilon X^\epsilon
> }
> \tag{T-23802.4}
> \]
> for every sufficiently large integer `X`.

For the RH deduction it is enough to prove (T-23802.4) on square endpoints
`X=N^2`.

GCM is strictly weaker than Carry Saturation:

- it does not require the exact triangular inverse to be nonnegative;
- it permits off-diagonal greedy pivots;
- it permits a nonzero final residual;
- it asks only that the total weighted packing mass lose a subpolynomial amount.

It is also weaker than the two-sided Carry Sandwich theorem of `T-23801`.

## 3. Deduction of the prime ramp

By `L-23804`, every feasible carry packing satisfies

\[
\sum_n d_X(n)\ll\log X.
\]

Therefore the entropy ledger gives

\[
\begin{aligned}
\sum_n d_X^{\rm gr}(n)G_n
&\ge{1\over2}\sum_n n d_X^{\rm gr}(n)-O(\log^2X)\\
&\ge4\sqrt X-X^{o(1)}.
\end{aligned}
\tag{T-23802.5}
\]

The exact carry/Legendre identity and `Lambda>=0` imply

\[
\boxed{
\mathcal P(X)
=\sum_{q=p^a\le X}{\Lambda(q)\over\sqrt q}\log{X\over q}
\ge4\sqrt X-X^{o(1)}.}
\tag{T-23802.6}
\]

## 4. Deduction of RH

At the square endpoint `X=N^2`, the explicit screw formula gives

\[
\Psi(2\log N)
=4N-\mathcal P(N^2)+O(\log N).
\tag{T-23802.7}
\]

Thus (T-23802.6) yields

\[
\boxed{
\Psi(2\log N)\le N^{o(1)}.}
\tag{T-23802.8}
\]

The upper-envelope version of the square-sampling Landau transfer in
`L-23804` excludes every zeta zero in `Re s>1/2+epsilon`, for every positive
`epsilon`. Functional-equation symmetry then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-23802.9}
\]

Hence the complete proposal is

\[
\boxed{
\begin{aligned}
&\text{finite carry matrix}\\
&\longrightarrow\text{canonical nonnegative greedy packing}\\
&\longrightarrow\text{GCM mass }8\sqrt X-X^{o(1)}\\
&\longrightarrow\text{binomial entropy }4\sqrt X-X^{o(1)}\\
&\longrightarrow\text{prime-ramp lower bound}\\
&\longrightarrow\text{square-screw upper envelope}\\
&\longrightarrow\mathrm{RH}.
\end{aligned}}
\tag{T-23802.10}
\]

## 5. Proposed attack on GCM

The producer has a rigid pivot geometry. If at row `n` the minimum in
(T-23802.1) is attained at `q<n`, then column `q` is saturated and every row
from `n-1` down through `q` that sees this column has zero admissible increment.
The nonzero steps therefore form a descending pivot forest rather than an
arbitrary LP solution.

The proposed proof uses three coupled ledgers.

### 5.1 Continuum mass ledger

`L-23805` proves that the scaled inverse carry operator has exact first mass
`8`. This supplies the target potential and the leading constant.

### 5.2 Quotient-layer residual ledger

For

\[
{X\over r+1}<m\le {X\over r},
\]

the Möbius decoder of `L-23803` involves only
`mu(1),...,mu(r)`. All rows in one complete quotient layer are to be recombined
before a sign or absolute value is taken. The desired block invariant is that
off-diagonal pivots can leave only subpolynomial total residual potential.

### 5.3 Pivot-potential ledger

Use the positive column potential

\[
a(q)=2-q^{-1/2}.
\tag{T-23802.11}
\]

The initial potential has the sharp elementary asymptotic

\[
\sum_{q=2}^Xa(q)w_X(q)
=8\sqrt X+O(\log^2X).
\tag{T-23802.12}
\]

The finite row inequality

\[
\sum_{q=2}^n a(q)\beta_{nq}\le n
\tag{T-23802.13}
\]

is proposed as a first atomic target. Together with a subpolynomial bound for
the final greedy residual in the same potential, it implies GCM immediately.
A weaker corrected weight `2-Cq^(-1/2)` with any fixed `C>0` is equally
acceptable; the leading constant remains eight and the correction remains
polylogarithmic.

This separates the proof into:

1. a source-free floor-sum potential inequality;
2. a source-specific quotient-layer estimate for the residual left by
   off-diagonal pivots.

The first is elementary divisor geometry. The second is the only location at
which the Möbius firewall of `L-23803` can enter.

## 6. Proof-producing form

A certificate for endpoint `X` contains

```text
X
complete carry rows beta_(nq)
initial target intervals w_X(q)
exact or directed greedy pivots
nonnegative coefficients d_X^gr(n)
final residuals
weighted mass lower endpoint
coefficient-mass and entropy-error bounds
proof-object digest
```

The consumer rejects:

- a negative coefficient or residual;
- omission of a carry column;
- a rounded minimum without separation or an exact tie declaration;
- use of primes only while retaining the all-column packing implication;
- a mass estimate inferred from finitely many endpoints;
- replacement of GCM by floating positivity of the exact inverse.

## 7. Proof boundary

Closed exactly in the proposal:

- the finite carry matrix and Legendre identity;
- a canonical feasible nonnegative packing at every endpoint;
- logarithmic coefficient mass for every packing;
- entropy conversion;
- the one-sided screw/Landau deduction;
- the continuum symbol and the sharp constant eight.

Open:

- GCM, equivalently a subpolynomial greedy mass deficit;
- the proposed pivot-potential and quotient-layer residual estimates;
- RH.

This is a full proof proposal with one explicitly named finite theorem. It is
not a completed proof of GCM or RH.