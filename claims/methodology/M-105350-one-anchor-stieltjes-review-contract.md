# M-105350 — Hostile review contract for the one-anchor Stieltjes frontier

Claim ID: `M-105350`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Review target

This packet replaces arbitrary separated-node searches for the boundary
Cauchy–Loewner gate by one complete confluent moment hierarchy at a fixed
analytic anchor. The reduction is exact only at **all orders**.

Review in this order:

1. verify the Taylor identity

   \[
   {H(x_*+u)-H(x_*+v)\over u-v}
   =\sum_{r,s\ge0}
   {H^{(r+s+1)}(x_*)\over(r+s+1)!}u^rv^s;
   \]

2. verify that positivity of all anchor Hankel matrices makes the moment
   functional nonnegative on every polynomial square;
3. apply the Hamburger moment theorem and use Cauchy bounds on the even moments
   to prove compact support;
4. verify the Pick representation and its positive kernel;
5. in the parity-symmetric Xi coordinate, verify the split into the two
   Stieltjes matrices `[beta_(r+s)]` and `[beta_(r+s+1)]`;
6. retain the bounded-order firewall `R-105350`.

## Load-bearing assumptions

The following may not be weakened silently:

- `H` is analytic on a conjugation-symmetric neighbourhood of the real
  interval;
- the upper part of that neighbourhood is connected;
- every confluent order is nonnegative;
- the Xi contour and the anchor zero lie in one common regular domain;
- definite parity, not mere centering of roots, is used for the odd boundary
  Cauchy function;
- the nonreal critical correction remains a separate last-defect gate.

## Sign convention

The boundary Loewner kernel is

\[
\mathscr L_H(x,y)={H(x)-H(y)\over x-y}.
\]

At the anchor,

\[
m_n={H^{(n+1)}(x_*)\over(n+1)!},
\]

and the confluent matrix is exactly `[m_(r+s)]`, without extra factorials or
alternating signs.

For odd `H(z)=sum beta_n z^(2n+1)`, the complete Hamburger matrix splits into

\[
[\beta_{r+s}]
\quad\text{and}\quad
[\beta_{r+s+1}].
\]

Both are required.

## Binding scientific boundary

```text
one-anchor/all-packet analytic equivalence       PROVED EXACT
origin Stieltjes parity reduction                PROVED EXACT
bounded confluent order -> all orders            REFUTED
OASH105350 for the Xi boundary sequence          OPEN
BRP105220                                        OPEN
Riemann Hypothesis                               UNPROVEN
```

The finite replay authenticates only algebraic fixture identities and the
bounded-order separator. It does not evaluate Xi or certify any infinite
moment hierarchy.
