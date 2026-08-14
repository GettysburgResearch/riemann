# R-91701 — Scalar root ledgers do not identify a positive literal current row

Claim ID: `R-91701`  
Status: **EXACT LOGICAL REFUTATION / TYPE FIREWALL**  
Created: 2026-08-14  
Targets: any use of target, score, or total-mass identities as a substitute for coefficientwise native-row feasibility  
Depends on: elementary ordered-vector algebra; the review diagnosis of `L-91659`  
RH status: **unproved**

## 1. Refuted inference

Let `V` be the finite literal row space, with positive cone `V_+`.  Suppose a
native parent datum is written formally as

\[
 N=C+R,
 \tag{R-91701.1}
\]

where `R` is called recursive and `C=N-R` is called current.  Additive scalar
functionals such as target and declared score may satisfy

\[
 T(C)\ge0,
 \qquad
 S(C)\ge0.
 \tag{R-91701.2}
\]

The inference

\[
 \boxed{
 (R\text{-91701.1})+(R\text{-91701.2})
 \Longrightarrow C\in V_+
 }
 \tag{R-91701.3-FALSE}
\]

is false.

## 2. Exact two-coordinate countermodel

Take

\[
 V=\mathbb R^2,
 \qquad
 V_+=\mathbb R_{\ge0}^2,
\]

and put

\[
 N=(1,1),
 \qquad
 R=(2,0),
 \qquad
 C=N-R=(-1,1).
 \tag{R-91701.4}
\]

Let both scalar ledgers be total mass,

\[
 T(x_1,x_2)=S(x_1,x_2)=x_1+x_2.
 \tag{R-91701.5}
\]

Then

\[
 N=C+R,
 \qquad
 T(C)=S(C)=0,
 \tag{R-91701.6}
\]

but

\[
 C\notin V_+.
 \tag{R-91701.7}
\]

Thus even exact parent/recursive/current identities and nonnegative scalar
remainders do not establish one literal row coefficient, one ordinary column,
one radix-four column, or one boundary-port inequality.

## 3. Consequence for the native-root problem

A valid root theorem must use one of the following stronger proof objects.

1. A componentwise residual-capacity calculation in every literal coordinate.
2. A positive-source representation of the current row.
3. An explicit positive decomposition whose response and score identities are
   obtained by applying linear functionals only after row positivity is known.

The direct-row architecture has such a representation available *after* target
Hall: positive residual sources `c_s,c_h`, positive row bonuses `B_s,B_h`, and
endpoint-monotone component rows.  `L-91702` records the exact implication.

## 4. Boundary

This refutation does **not** say that the desired native current row is negative.
It says that its sign cannot be inferred from a coordinate name, a scalar target
identity, a declared-score identity, or a tautological complement.  The exact
post-Hall source identity must be supplied in literal row coordinates.

```text
scalar target/score complement implies row sign       FALSE
coordinatewise residual proof                          SUFFICIENT
positive-source current representation                 SUFFICIENT / L-91702
native root Hall row identity                           STILL REQUIRED
Riemann Hypothesis                                      UNPROVEN
```
