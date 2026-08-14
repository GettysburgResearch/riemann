# L-91388 — Direct native \(Y_4\)-slack minimization is a fail-closed linear program

Claim ID: `L-91388`  
Status: **PROVED EXACT FINITE PRIMAL/DUAL FORMULATION**  
Created: 2026-08-14  
Depends on: `L-91377`, `L-91378`, `L-91379`, `T-91314`  
RH status: **unproved**

## 1. Finite native packet

Fix a finite endpoint \(X\). Let \(d(j)\ge0\) be the current component-row
variables. Let \(\alpha_b\ge0\) be coefficients of source-disjoint recursive
typed packets \(P_b\), with endpoints \(Y_b\le X/67+C_0\).

For every physical ordinary column \(q\), define

\[
C^{\rm rec}(q)=\sum_b\alpha_b C_{P_b}(q),
\]

and for every detail column,

\[
\Xi^{\rm rec}(q)=\sum_b\alpha_b\Xi_{P_b}(q).
\]

Introduce native ordinary and detail slack variables

\[
o(q)=w_X(q)-C_d(q)-C^{\rm rec}(q)\ge0,
\]

\[
s(q)=\Omega_X(q)-\Xi_d(q)-\Xi^{\rm rec}(q)\ge0.
\tag{L-91388.1}
\]

All retained boundary and common-port coordinates receive analogous
nonnegative one-use slacks.

## 2. Exact objective

`L-91378` gives the positive dual weight

\[
Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k)
\]

and the exact identity

\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
-\sum_b\alpha_b\bigl[J_\Lambda(Y_b)-\mathcal H(P_b)\bigr]
=
\sum_qY_4(q)s(q).
}
\tag{L-91388.2}
\]

Thus the direct NRCT objective is

\[
\boxed{
\min \sum_qY_4(q)s(q).
}
\tag{L-91388.3}
\]

There is no independent hidden score coordinate. The objective is exactly the
unused native radix-four capacity after recursive ownership is removed.

## 3. Triangular reconstruction

The recurrence

\[
Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q)
\]

is dual to the triangular relation

\[
\Xi(q)=C(q)-2C(4q).
\]

Consequently one may use either:

```text
ordinary variables plus detail equalities;
detail variables plus the positive finite renewal that reconstructs ordinary
feasibility.
```

No signed detail functional is assumed positive on arbitrary rows.

## 4. Score-free repair directions

If

\[
Y_4(q)=0,
\]

then neither \(q\) nor any \(q/4^k\) is a prime power. Slack or target-null
repair in that detail coordinate has zero endpoint cost in (L-91388.3).
Such columns are legitimate score-free repair directions, provided the ordinary
renewal, row nonnegativity and one-use ports remain satisfied.

They may be used to repair local positivity or boundary geometry. They may not
be used to conceal overdraw in a positive-\(Y_4\) column.

## 5. Exact finite certificate format

On a fixed endpoint/activation cell all maps are finite and linear. The
certificate is

\[
Bx=b,\qquad Gx\le c,\qquad x\ge0,
\]

where \(x\) contains:

```text
current row coefficients;
source-labelled child coefficients;
ordinary/detail/port slacks;
optional target-null repair generators.
```

The objective is (L-91388.3).

Analytic coefficients involving roots and logarithms are enclosed by directed
rational intervals. A proof-grade primal certificate gives rational variables
whose worst-case interval evaluation satisfies every constraint. If no such
point exists, a rational dual vector supplies an exact Farkas separator.

## 6. Relation to NRCT

A family of certificates with

\[
\sum_b\alpha_b<\frac18,
\qquad
Y_b\le X/67+C_0,
\]

and

\[
\sum_qY_4(q)s(q)=O(1)
\]

is exactly the strong weighted-slack form of `T-91314`. It yields the bounded
deficit consumer `T-91312` and the endpoint implication `T-91313`.

```text
native objective = Y4-weighted slack EXACT
finite primal/dual formulation       EXACT
Y4-zero repair directions            EXACT
live certificate                     OPEN
Riemann Hypothesis                    UNPROVED
```
