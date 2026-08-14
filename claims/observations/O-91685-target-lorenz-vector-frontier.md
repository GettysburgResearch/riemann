# O-91685 — Target-Lorenz vector frontier and exact next campaign

Observation ID: `O-91685`  
Status: **CURRENT HANDOFF / NO RH CLAIM**  
Created: 2026-08-14

## Durable advance

`L-91685` converts the surviving Target-Lorenz route into a complete
primal-or-dual theorem for the common-source submeasure cone.

```text
one common source coefficient in every coordinate       EXACT
leftmost target removal maximizes all 65 rows            EXACT
same removal minimizes score                              EXACT
failed row -> separator for every exact-target removal    EXACT
high-dimensional source LP                                ELIMINATED
```

The remaining arithmetic task is now genuinely only the sign family

\[
 \mathfrak L_j(p,y)\ge0.
\]

It is no longer ambiguous whether another exact-target submeasure of the same
even source might succeed after the Target-Lorenz object fails: none can.

## Exact easy regime — `L-91686`

Let `c=c_T(p,y)` be the Target-Lorenz cutoff and `x=py`. The causal component
row is supported only on divisors `d<x/j`. Therefore, whenever

\[
 c\ge x/j,
\tag{O-91685.1}
\]

the Target-Lorenz removal has already consumed every even atom with a nonzero
row, while every omitted odd atom has zero row. Hence

\[
 \boxed{
 \mathfrak L_j(p,y)
 =\sum_{d\mid P_{61}}\mu(d)K_R^{(j)}(d),
 }
\tag{O-91685.2}
\]

the complete signed causal one-prime row.

This is `L-91686`. It reduces the regime to the reviewed inherited-row theorem when `j<=y` and to canonical finite-Euler row positivity when the child row is inactive. No cutoff determinant remains there.

The still nontrivial cells satisfy

\[
 c<x/j.
\tag{O-91685.3}
\]

## Full signed determinant reduction — `L-91687`

Let `mathscr T` and `mathscr R_j` be the complete signed causal target and row.
The unused even residual lies at or to the right of the cutoff, so its row per
target is at most the cutoff ratio. Hence

\[
 \mathfrak L_j
 \ge \mathscr R_j-\rho_j(c)\mathscr T.
\]

It is therefore sufficient to certify the full signed determinant

\[
 \mathscr R_jK_T(c)-\mathscr TK_R^{(j)}(c)\ge0.
\]

This replaces the signed cutoff-prefix determinant by the complete signed
packet plus one cutoff atom. It is sufficient rather than necessary, but every
structured case in the companion reconnaissance satisfies it.

## Correct cell coordinates

The target cutoff does not globally collapse to
`sqrt(y)(sqrt(p)+1)`; `R-91685` gives an exact counterexample. Use instead

\[
 A=\sqrt{py},
 \qquad
 u=\sqrt y.
\]

On each fixed child-activation cell,

\[
 A K_T(d)
 =\frac{4A^2}{d}-\frac{3A}{\sqrt d}
 -\mathbf1_{d\le u^2}
  \left(\frac{4u^2}{d}-\frac{3u}{\sqrt d}\right).
\]

The cutoff inequalities are finite quadratic-algebraic inequalities in
`(A,u)`. After fixing the parent and child row activations,

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}
\]

turns each remaining row margin into one explicit algebraic-logarithmic cell
function.

## Fail-closed certificate campaign

For every one of the 185 cutoffs and 65 rows:

1. discard the easy support regime (O-91685.1);
2. partition the remaining `(A,u)` domain by target, parent-row and child-row
   activation boundaries;
3. return a symbolic positive decomposition, a directed interval/derivative
   lower bound, or an exact negative witness;
4. if negative, emit the `L-91685.8` dual separator;
5. if all positive, export the live atomwise root allocation and solve `ANRL`.

The exact first quotient cell `py<2j` is already positive. Discovery scans in
`X-91685` are consistent with the global minimum lying in that easy cell, but
they are not promoted as an infinite theorem.

## Proof boundary

```text
vector primal/dual closure                     EXACT
false one-scalar cutoff reduction               FENCED
support-easy row regime                         EXACT REDUCTION
remaining cell family                           FINITE-STRUCTURED / OPEN
live native root allocation                     FINITE PRIMAL/DUAL / OPEN
Riemann Hypothesis                              UNPROVEN
```
