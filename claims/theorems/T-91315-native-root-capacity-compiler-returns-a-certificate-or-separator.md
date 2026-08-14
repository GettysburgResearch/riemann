# T-91315 — The native-root compiler returns an NRCT certificate or an exact separator

Claim ID: `T-91315`  
Status: **PROVED FAIL-CLOSED COMPILER THEOREM; NRCT NOT YET CERTIFIED**  
Created: 2026-08-14  
Depends on: `R-91316`, `L-91386`–`L-91388`, `T-91314`  
RH status: **unproved**

## 1. Purpose

This theorem replaces open-ended proof composition by a fail-closed producer
campaign. It accepts one of three outputs:

```text
PASS_NATIVE_ROOT_CAPACITY_THEOREM;
an exact row/column/port Farkas separator;
an exact normalization separator proving that a proposed packet is not native.
```

No high-level RH composition is accepted without the first output.

## 2. Route A — compile the fixed-window root Hall packet

Compile PR #464 into every coordinate of `T-91314` using the native
normalization of `L-91377`–`L-91379`.

`R-91316` supplies the result for the packet as presently declared:

\[
\boxed{
\text{EXACT NATIVE-RESERVOIR SEPARATOR}.
}
\]

At \(X=136,q=2\), retaining the canonical finite-Euler current together with
the rough recursive reservoir overdraws native ordinary capacity by more than
\(1/816\). Therefore PR #464 is not, as written, a direct unconditional NRCT
certificate.

This does not refute its finite root Hall inequalities. It identifies the exact
additional object required: a source-disjoint physical allocation of every
rough-reservoir term and an explicit nonnegative native slack.

## 3. Route B — stopped-leaf live primal/Farkas certificate

Use the complete arithmetic profile orders and cutoff theorem of PR #467.
`L-91386` proves that the leftmost target fill is the simultaneous optimum for
score and every component row. Therefore the unrestricted stopped-leaf LP is
feasible exactly when that single basis satisfies the row constraints.

`L-91387` reduces those signs to a finite activation-cell campaign. Every cell
must return either:

```text
a directed positive row certificate; or
one exact failed row separator.
```

No alternative LP basis is searched after a leftmost row failure, because the
optimizer theorem makes such a search mathematically unnecessary.

## 4. Route C — direct native \(Y_4\)-slack LP

Use `L-91388` to solve the native physical problem directly. A primal solution
must display:

\[
d_X^{\rm cur}\ge0,
\]

source-disjoint children of total target coefficient below \(1/8\), all
ordinary/detail/port slacks, and the exact objective

\[
\sum_qY_4(q)s(q).
\]

A bounded objective gives `PASS_NATIVE_ROOT_CAPACITY_THEOREM`. An infeasible
cell returns a rational Farkas separator. Columns with \(Y_4=0\) are available
as score-free repair directions.

## 5. Proof boundary

The companion replay verifies:

* the exact PR #464 native-reservoir separator;
* the rough-monoid convolution on a finite regression range;
* the leftmost optimizer on exhaustive finite vertices of rational fixtures;
* a deliberate exact row-separator fixture;
* the \(Y_4\) recurrence and finite summation-by-parts identity.

It does not certify every live activation cell and does not prove NRCT.

```text
PR464 direct native compilation         SEPARATED EXACTLY
target-Lorenz optimizer                 PROVED
target-Lorenz live cell campaign        OPEN / FAIL-CLOSED
direct Y4 native LP                     FORMULATED EXACTLY
PASS_NATIVE_ROOT_CAPACITY_THEOREM       NOT YET ISSUED
Riemann Hypothesis                      UNPROVED
```
