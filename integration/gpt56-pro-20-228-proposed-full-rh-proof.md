# Integration handoff — Issue #228 critical Möbius local-to-Bohr attempt

## Retain

```text
L-22801  exact completed Möbius–Farey packet and reduced coefficients
R-22801  completed-tail scope firewall
R-22802  refutation of the uniform Farey-cluster operator bound
T-22803  scalar Möbius near-resonance RH criterion, estimate open
O-22801  repository-wide global-coordinate consolidation
X-22801  exact finite local/Bohr regression
```

## Reject or block

```text
T-22801  REJECTED AS STATED
T-22802  GAP/BLOCKED
```

The first proof attempt claimed a subpower uniform operator norm. `R-22802` proves an exact `sqrt(D)` row lower bound, so that proof cannot be repaired by changing finitely many low cells.

## Dependency

The branch is stacked on draft PR #226 at frozen head

```text
53f2cba370fa518d5d12488b5b9948c1826bba88.
```

The exact retained parent chain is:

```text
L-9512  analytic totient identity and Mellin transform
L-9513  positive Jordan Bohr energy and B_D << D
T-22803 scalar completed-packet estimate, OPEN
-> critical second moment
-> RH
```

## Correct research target

Prove specifically for the Möbius divisor vectors

```text
int_(D/2)^D
 |1+S_D(x)+M_D/3+x^2R_D|^2 dx
 <<_epsilon D^(1+epsilon)(1+B_D).
```

A proof must exploit Möbius signs before Cauchy–Schwarz. Do not retry a uniform Farey large-sieve/operator theorem.

## Public status

```text
PROOF ATTEMPT SELF-REFUTED
EXACT ALGEBRA RETAINED
SCALAR MOBIUS ESTIMATE OPEN
RH UNPROVED
```

No merge and no public README change are requested.