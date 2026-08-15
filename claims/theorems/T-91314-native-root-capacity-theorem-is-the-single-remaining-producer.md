# T-91314 — The Native-Root Capacity Theorem is the single remaining producer interface

Claim ID: `T-91314`  
Status: **PROVED CONDITIONAL COMPOSITION / EXPLICIT PRODUCER GATE**  
Created: 2026-08-14  
Depends on: `L-91375/L-91377/L-91378/L-91379`; `T-91312/T-91313`  
RH status: **conditional**

## 1. Native root datum

At endpoint `X`, write the native typed packet as

\[
 \mathcal N_X=
 (J_\Lambda(X),w_X,\Omega_X,\text{row/port coordinates}).
\]

The exact finite-Euler datum `D_(P_61,X)` is larger by the rough reservoir of
`L-91379`; it may not be substituted for `N_X`.

## 2. Native-Root Capacity Theorem (`NRCT`)

For every sufficiently large native packet, construct a current row

\[
 d_X^{\rm cur}\ge0
\]

and source-disjoint recursive typed packets `P_b` with coefficients `alpha_b`
such that:

### Source and scale

\[
 Y_b\le X/67+C_0,
 \qquad
 \alpha_b\ge0,
 \qquad
 \sum_b\alpha_b<\frac18.
\tag{T-91314.1}
\]

### One-use ordinary and detail capacities

Define the recursive physical responses

\[
 R_X^{\rm ord}(q)=\sum_b\alpha_b C_{P_b}(q),
\]

\[
 R_X^{(4)}(q)=\sum_b\alpha_b\Xi_{P_b}(q).
\]

Then

\[
\boxed{
 C_{d_X^{\rm cur}}(q)+R_X^{\rm ord}(q)\le w_X(q),
}
\tag{T-91314.2}
\]

\[
\boxed{
 \Xi_{d_X^{\rm cur}}(q)+R_X^{(4)}(q)\le\Omega_X(q)
}
\tag{T-91314.3}
\]

for every physical column, with the analogous one-use inequalities for every
retained boundary or common-port coordinate.

### Current debt

Use the exact target mass `m_X` of `T-91312`. The current packet must obey

\[
\boxed{
 \Delta_X(d_X^{\rm cur})\le2m_X(\mathcal N_X),
}
\tag{T-91314.4}
\]

and the child target masses must satisfy the same subcritical ledger as
(T-91314.1).

### Provenance

Every arithmetic source atom occurs either in the current packet or in exactly
one child. In particular, no term of the positive rough reservoir in
`L-91379` is charged once through the canonical finite-Euler row and again
through a recursive child.

## 3. Consequence

NRCT is precisely the Hereditary Typed Reset hypothesis of `T-91312`. Therefore

\[
 \Lambda(X)
 \le2+\frac18\Lambda(X/67+C_0),
\]

and

\[
\boxed{
 \Lambda(X)=O(1)=o(\log^2X).
}
\tag{T-91314.5}
\]

`T-91313` then implies RH.

## 4. Equivalent weighted-slack form

By `L-91378`, the current detail condition may be audited through the exact
positive slack

\[
\boxed{
 \Delta_X(d_X^{\rm cur})
 =\sum_qY_4(q)
  [\Omega_X(q)-\Xi_{d_X^{\rm cur}}(q)].
}
\tag{T-91314.6}
\]

Thus a stronger and often cleaner NRCT proof object is:

```text
one explicit nonnegative current row;
source-disjoint children of total mass <1/8;
componentwise one-use native detail capacity;
uniformly bounded Y_4-weighted current slack.
```

## 5. Exact boundary

```text
normalization firewall                         CLOSED
rough reservoir source/physical decomposition EXACT
current causal debt after positive entry       CLOSED
subcritical consumer                           CLOSED
one-sided endpoint-to-RH consumer              CLOSED
NRCT positive native-root disintegration       OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
