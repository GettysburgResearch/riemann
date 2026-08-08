# Binary–ternary carry continuation: half-moment collapse and profit/debt audit

Agent: `gpt56-pro-09-w`  
Date: 2026-08-08  
Parent proposal: PR #247  
Status: **NEW EXACT STRUCTURE; NO UNCONDITIONAL RH PROOF CLAIMED**

## 1. Objective

The active PR had reached an explicit binary–ternary fragmentation producer and
isolated the cofinal estimate

\[
 \sum_{n=2}^X|A_X(n)|\sqrt n=X^{o(1)}.
\]

This pass attacked that estimate rather than adding another conditional
composition theorem.

## 2. Exact collapse of the BTF rate

For every `0<theta<1`, the producer satisfies

\[
 -\sum_mr_X(m)m^\theta
 =\sum_nA_X(n)\Delta_\theta(n),
\]

where `Delta_theta` is the concavity defect of the declared binary–ternary
splits.  At `theta=1/2`,

\[
 \kappa_-\sqrt n\le\Delta_{1/2}(n)
 \le\kappa_+\sqrt n
\]

with explicit positive constants.  Therefore, if the producer is nonnegative,
its full weighted variation is equivalent to the single scalar moment

\[
 \mathfrak H_X=-\sum_mr_X(m)\sqrt m.
\]

The exact coefficient sequence of this moment has Dirichlet series

\[
 {1\over\zeta(s)}
 \sum_{m\ge1}{\sqrt m-\sqrt{m-1}\over m^s}.
\]

Thus the BTF rate still contains one reciprocal-zeta channel.  The recurrence
has compressed the analytic difficulty; finite positivity alone does not remove
it.

## 3. Independent reconnaissance

An independent compiled implementation of the exact recurrence found:

- nonnegative producer coefficients through endpoints as large as `10^7`;
- weighted variation of apparent polylogarithmic size;
- exact agreement of the half-moment identity to floating precision.

This is strong evidence for the proposed sign and rate, but it is not a proof
and is not used as a theorem in the branch.

## 4. Profit/debt coordinate

For

\[
 F(n)=\log(n!)-\sum_{q\le n}\lfloor n/q\rfloor,
\]

the profit of a split is

\[
 \pi(n,j)=F(n)-F(j)-F(n-j)
 =\log\binom nj-\sum_q\chi_{n,j}(q).
\]

For every exact balanced flow,

\[
 \sum d_{n,j}\pi(n,j)
 =\mathcal P(X)-\mathcal C(X).
\]

Consequently, a flow whose total negative profit is `X^{o(1)}` proves the sharp
prime ramp.  A particularly reviewable sufficient theorem is to use
unprofitable rows only at an absolute finite set of parent sizes.  Since every
split of parent `n` consumes column `q=n`, the coefficient mass at each fixed
bad parent is at most `w_X(n)=O(log X)`.  Finite exceptional debt is therefore
only logarithmic.

This is recorded in `L-23813`.

## 5. What did not close

No proof was found of either:

1. cofinal positivity of the binary–ternary coefficients;
2. the scalar half-moment bound;
3. a finite-exception profitable fragmentation theorem;
4. subpolynomial negative fragmentation debt.

Each of these would complete the active carry route through the existing
square-screw/Landau transfer.  None may be inferred from finite LP tables.

## 6. Recommended next review order

1. `L-23810` — exact floor inversion and divergence;
2. `L-23811` — exact producer recurrence;
3. `L-23812` — half-moment collapse;
4. `R-23803` — scope correction;
5. `L-23813` — profit/debt criterion;
6. `T-23803` — conditional RH composition.

The reviewer should attack producer positivity and the scalar half-moment
separately.  A proof of only one is not a proof of BTF.

## 7. Final status

```text
exact recurrence and divergence             RETAINED
exact half-moment collapse                   PROVED IN THIS PASS
exact profit/debt criterion                  PROVED IN THIS PASS
cofinal producer positivity                  OPEN
scalar half-moment / BTF rate                OPEN
unconditional proof of RH                    NO
```
