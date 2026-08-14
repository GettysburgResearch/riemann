# R-91673 — Stopped-leaf Hall cannot be reimported into the root closure

Claim ID: `R-91673`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-14  
Depends on: review PR #456 / `R-91656`  
RH status: **unproved**

## Statement

The universal stopped-leaf no-upward Hall assertion used in the former direct-row proposal is false. At the admissible leaf

```text
p = 67,
y = 13,
py = 871,
threshold = 13,
```

the survival Hall prefix is strictly negative. The directed review replay gives

```text
-2.140 < normalized prefix < -2.139,
physical prefix < 0.
```

For fixed `y=13` this failure persists for every sufficiently large rough prime, because the relevant coefficient of `sqrt(p)` is strictly increasing while

\[
\sum_{n\le13}\frac{\mu(n)}n=-\frac{2323}{30030}<0.
\]

Consequently none of the following may be used in a proof:

```text
separate survival Hall at every stopped leaf;
separate hazard Hall at every stopped leaf;
summing those leafwise Hall outputs into a positive native row;
T-91656 or L-91671 insofar as they depend on that implication.
```

The following survive:

```text
least-prime source disjointness before Hall;
exact one-prime target/score/row cocycle;
native ordinary and radix-four response formulas;
same-index arbitrary-child replacement;
fixed-67 literal entropy theorem;
finite endpoint dual and one-sided endpoint criterion.
```

## Replacement domain

The successor route applies score Hall only to the certified root quotient window

\[
1\le x\le c_0^{-1}<54.2192,
\]

where the original finite directed Hall certificate is valid. Rough-prime recursion after that root projection uses complete causal differences and does not Hallize stopped leaves.

```text
stopped-leaf Hall                         FALSE
fixed-window root score Hall              SEPARATE / L-91673
causal positive recursion                 RETAINED
Riemann Hypothesis                        UNPROVEN
```
