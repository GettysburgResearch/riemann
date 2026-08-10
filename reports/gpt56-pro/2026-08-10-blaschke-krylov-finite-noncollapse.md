# Blaschke–Krylov continuation after Anthropic Zeta23

Date: 2026-08-10  
Status: **new exact finite-packet theorem; RH unproved**

## Competitive signal

The imported Anthropic/Claude package in PR #361 is a genuine unconditional
advance: it proves that more than \(0.6725\) of the zeta zeros are simple and on
the critical line, with a formalized \(2/3\) core. It is not an RH proof.

Its decisive reusable object is the signature-\((1,1)\) block contributed by a
reflected off-line pair. PRs #363 and #364 computed the pair spectrum and exact
finite interpolation cost, but left open the possibility that nuisance zeros
force the target Schur complement to collapse.

## New theorem

The Q4 all-pass factor suggests a Krylov coordinate
\((1,\phi,\ldots,\phi^{k-1})\). For a reflected pair with
\(r=|\phi(z)|<1\), the open evaluation block has eigenvalues

\[
m\left(
k\pm\frac{\sinh(k\tau)}{\sinh\tau}
\right),
\qquad r=e^{-\tau}.
\]

The negative eigenvalue grows exponentially. That growth is **not free**:
scalar inner multiplication is exactly reflected-\(J\)-unitary, and a completely
closed coherent channel bank collapses as in PR #363.

The legitimate gain is different. One scalar polynomial in the inner
coordinate can interpolate the target pair. Its exact minimum cost is bounded,
and after arbitrary finite line/off-line nuisance constraints the target Schur
cost converges to a finite Szegő-Schur value. Therefore finite packet Gram
collapse is not a genuine obstruction.

For the exact eight-point rational control in the replay, the cost decreases

```text
k=8     25821.7280
k=16      359.0939
k=32      142.9382
k=64      127.4639
limit     9800/81 = 120.987654...
```

The large initial values reproduce the conditioning phenomenon seen on PR #364;
the bounded limit demonstrates the new noncollapse mechanism.

## New frontier

The remaining full-RH theorem is now a joint tail passage:

```text
finite-packet Blaschke–Krylov capture bounded
+ compact-delay truncation
+ corrected arithmetic floor -> 0
+ unseen-zero tail -> 0
----------------------------------------------
negative complete Weil direction
-> RH.
```

No local target-pair conditioning theorem remains. What remains is the
dependency-preserving global passage: the test, support, packet, and tail must
be changed together.

## Exact boundary

```text
Anthropic 0.6725 theorem                     imported external
finite off-line pair signature               imported exact
finite arbitrary-packet interpolation        imported exact
scalar inner-power amplification             refuted exactly
Krylov open-pair spectrum                     proved exactly
pair-only capture limit                       proved exactly
finite nuisance Schur noncollapse             proved
compact finite-delay approximation            proved
uniform complete-tail passage                 open / RH-bearing
Riemann Hypothesis                            unproved
```
